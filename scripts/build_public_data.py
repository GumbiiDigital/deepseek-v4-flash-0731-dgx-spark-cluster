#!/usr/bin/env python3
"""Create the sanitized numeric publication data from the sealed private run.

The script deliberately exports an allowlisted subset. It never copies commands,
logs, generated text, request snippets, local paths, network addresses, SSH data,
or per-host identifiers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import statistics
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


EXPECTED_PRIVATE_MANIFEST_SHA256 = (
    "2efa0d711aed8e383dd58014ae30d45aa285201f9f1e103e8c374d12725df558"
)
EXPECTED_MODEL_MANIFEST_SHA256 = (
    "1579d788beb7c9e759e717ade14e7c8a232d08a8db598f3a19dc2d0e3dcc43f2"
)
EXPECTED_MODEL_REVISION = "9e165c30e2704aec5d9d593cce3eebd58bbef1cb"
EXPECTED_IMAGE_ID = (
    "sha256:7a1e1e3f8cd2e675343a947ac05b0244778ee2667aaf0ab0d586e3ce9a896881"
)
PAIR_IDS = {1: "A", 2: "B", 3: "C", 4: "D"}
_SENSITIVE_ROOTS = [
    "/" + "Users" + "/",
    "/" + "home" + "/",
    "/" + "root" + "/",
    "Identity" + "File",
    "." + "ssh" + "/",
]
PRIVATE_HOST_PATTERN = re.compile(
    "(?:"
    + "|".join(re.escape(value) for value in _SENSITIVE_ROOTS)
    + r"|(?:10|100|192\.168)\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    + r"|spark[1-8](?:-lan|-bypass)?)",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--private-run", type=Path, required=True)
    parser.add_argument("--model-manifest", type=Path, required=True)
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )


def verify_private_manifest(run_dir: Path) -> int:
    manifest = run_dir / "FINAL_SHA256SUMS"
    if sha256(manifest) != EXPECTED_PRIVATE_MANIFEST_SHA256:
        raise RuntimeError("private manifest hash does not match the publication anchor")
    count = 0
    for line_number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            expected, raw_name = line.split(None, 1)
        except ValueError as exc:
            raise RuntimeError(f"invalid private manifest line {line_number}") from exc
        raw_name = raw_name.lstrip("*")
        candidate = (run_dir / raw_name).resolve()
        try:
            candidate.relative_to(run_dir)
        except ValueError as exc:
            raise RuntimeError(f"unsafe private manifest path at line {line_number}") from exc
        if not candidate.is_file() or sha256(candidate) != expected.lower():
            raise RuntimeError(f"private manifest verification failed at line {line_number}")
        count += 1
    if count != 331:
        raise RuntimeError(f"expected 331 sealed private files, observed {count}")
    return count


def numeric_tree(value: Any) -> bool:
    if value is None or isinstance(value, (int, float)):
        return True
    if isinstance(value, list):
        return all(numeric_tree(item) for item in value)
    return False


def iso_from_vllm(value: str) -> str:
    return datetime.strptime(value, "%Y%m%d-%H%M%S").strftime("%Y-%m-%dT%H:%M:%SZ")


def official_data(run_dir: Path, contract: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    runs: list[dict[str, Any]] = []
    start_times: dict[tuple[int, int], list[datetime]] = {}
    for pair_number in range(1, 5):
        for concurrency in (1, 4):
            for repetition in range(1, 4):
                source = read_json(
                    run_dir
                    / "official-vllm"
                    / f"pair{pair_number}"
                    / f"c{concurrency}"
                    / f"rep{repetition}"
                    / "result.json"
                )
                if source["completed"] != 20 or source["failed"] != 0:
                    raise RuntimeError("official request completion gate failed")
                if source["input_lens"] != [2048] * 20:
                    raise RuntimeError("official input-length gate failed")
                if source["output_lens"] != [128] * 20:
                    raise RuntimeError("official output-length gate failed")
                metrics = {
                    key: value
                    for key, value in source.items()
                    if key not in {
                        "date",
                        "endpoint_type",
                        "backend",
                        "label",
                        "model_id",
                        "tokenizer_id",
                        "request_rate",
                        "generated_texts",
                        "errors",
                    }
                    and numeric_tree(value)
                }
                seed = contract["official_vllm"]["seeds_by_concurrency"][str(concurrency)][
                    str(repetition)
                ]
                measured_at = iso_from_vllm(source["date"])
                start_times.setdefault((concurrency, repetition), []).append(
                    datetime.fromisoformat(measured_at.removesuffix("Z"))
                )
                runs.append(
                    {
                        "pair_id": PAIR_IDS[pair_number],
                        "concurrency": concurrency,
                        "repetition": repetition,
                        "seed": seed,
                        "measured_at_utc": measured_at,
                        "metrics": metrics,
                    }
                )

    pairs: dict[str, Any] = {}
    for pair_number, pair_id in PAIR_IDS.items():
        pairs[pair_id] = {}
        for concurrency in (1, 4):
            selected = [
                run
                for run in runs
                if run["pair_id"] == pair_id and run["concurrency"] == concurrency
            ]
            output_values = [run["metrics"]["output_throughput"] for run in selected]
            request_values = [run["metrics"]["request_throughput"] for run in selected]
            pairs[pair_id][f"c{concurrency}"] = {
                "output_throughput_tok_s_runs": output_values,
                "output_throughput_tok_s_median": round(statistics.median(output_values), 4),
                "output_throughput_cv_pct": round(
                    statistics.stdev(output_values) / statistics.mean(output_values) * 100,
                    4,
                ),
                "request_throughput_req_s_median": round(statistics.median(request_values), 4),
                "median_ttft_ms_across_repetitions": round(
                    statistics.median(run["metrics"]["median_ttft_ms"] for run in selected),
                    4,
                ),
                "median_tpot_ms_across_repetitions": round(
                    statistics.median(run["metrics"]["median_tpot_ms"] for run in selected),
                    4,
                ),
            }

    cross_pair: dict[str, Any] = {}
    for concurrency in (1, 4):
        pair_medians = [
            statistics.median(
                run["metrics"]["output_throughput"]
                for run in runs
                if run["pair_id"] == pair_id and run["concurrency"] == concurrency
            )
            for pair_id in PAIR_IDS.values()
        ]
        repetition_sums = [
            sum(
                run["metrics"]["output_throughput"]
                for run in runs
                if run["concurrency"] == concurrency and run["repetition"] == repetition
            )
            for repetition in range(1, 4)
        ]
        pair_mean = statistics.mean(pair_medians)
        cross_pair[f"c{concurrency}"] = {
            "mean_pair_output_tok_s": round(pair_mean, 4),
            "pair_spread_definition": "(maximum pair median - minimum pair median) / mean pair median",
            "pair_spread_pct": round((max(pair_medians) - min(pair_medians)) / pair_mean * 100, 4),
            "per_repetition_four_pair_output_tok_s": repetition_sums,
            "four_pair_aggregate_output_tok_s_median": round(
                statistics.median(repetition_sums), 4
            ),
        }

    skews = [
        int((max(values) - min(values)).total_seconds()) for values in start_times.values()
    ]
    raw_export = {
        "schema_version": 1,
        "description": "Sanitized numeric output from the official vLLM serving-benchmark lane",
        "benchmark": {
            "command_family": "vllm bench serve",
            "backend": "openai-chat",
            "dataset": "synthetic random",
            "server_observed_input_tokens": 2048,
            "output_tokens": 128,
            "measured_requests_per_run": 20,
            "excluded_warmups_per_run": 4,
            "repetitions": 3,
            "concurrency": [1, 4],
        },
        "runs": runs,
    }
    aggregate_export = {
        "schema_version": 1,
        "headline_scope": "baseline, not a record claim",
        "pairs": pairs,
        "cross_pair": cross_pair,
        "integrity": {
            "raw_result_files": len(runs),
            "measured_requests": sum(run["metrics"]["completed"] for run in runs),
            "failed_requests": sum(run["metrics"]["failed"] for run in runs),
            "all_server_observed_input_tokens_exactly_2048": True,
            "all_output_tokens_exactly_128": True,
            "maximum_pair_start_skew_seconds": max(skews),
        },
    }
    return raw_export, aggregate_export


def public_comparison_data(run_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    pairs: list[dict[str, Any]] = []
    overall_ends: list[dict[str, Any]] = []
    pair_integrity: dict[str, Any] = {}
    for pair_number, pair_id in PAIR_IDS.items():
        result = read_json(run_dir / "public-llama-benchy" / f"pair{pair_number}" / "result.json")
        pairs.append(
            {
                "pair_id": pair_id,
                "version": result["version"],
                "timestamp_utc": result["timestamp"],
                "latency_mode": result["latency_mode"],
                "latency_ms": result["latency_ms"],
                "model": result["model"],
                "prefix_caching_enabled": result["prefix_caching_enabled"],
                "benchmarks": result["benchmarks"],
            }
        )
        ends: list[dict[str, Any]] = []
        progress = run_dir / "public-llama-benchy" / f"pair{pair_number}" / "progress.json"
        for line in progress.read_text(encoding="utf-8").splitlines():
            event = json.loads(line)
            if event.get("type") == "request_end":
                ends.append(event)
        if len(ends) != 60:
            raise RuntimeError(f"public request count failed for pair {pair_id}")
        overall_ends.extend(ends)
        observed = [int(event["total_tokens"]) for event in ends]
        prompts = [int(event["prompt_tokens"]) for event in ends]
        pair_integrity[pair_id] = {
            "measured_requests": len(ends),
            "errors": sum(bool(event.get("error")) for event in ends),
            "requested_output_tokens": 128,
            "client_observed_completion_tokens": {
                "minimum": min(observed),
                "maximum": max(observed),
                "mean": statistics.mean(observed),
                "distribution": dict(sorted(Counter(observed).items())),
            },
            "server_observed_prompt_token_distribution": dict(
                sorted(Counter(prompts).items())
            ),
        }
    all_observed = [int(event["total_tokens"]) for event in overall_ends]
    result_export = {
        "schema_version": 1,
        "description": "Sanitized numeric llama-benchy results; no streamed text or request identifiers",
        "source_commit": "e9be344578cec17745066b220798b80a0d2686d3",
        "pairs": pairs,
    }
    integrity_export = {
        "schema_version": 1,
        "requested_shape": {
            "pp": 2048,
            "tg": 128,
            "exact_tg_flag": True,
            "depths": [0, 4096, 16384, 32768],
            "concurrency": [1, 4],
            "measured_runs": 3,
            "excluded_warmups": 1,
            "cache_policy": "no-cache",
            "latency_mode": "api",
        },
        "pairs": pair_integrity,
        "overall": {
            "measured_requests": len(overall_ends),
            "errors": sum(bool(event.get("error")) for event in overall_ends),
            "requested_output_tokens": 128,
            "client_observed_completion_tokens_minimum": min(all_observed),
            "client_observed_completion_tokens_maximum": max(all_observed),
            "client_observed_completion_tokens_mean": statistics.mean(all_observed),
            "client_observed_completion_tokens_exactly_128": sum(
                value == 128 for value in all_observed
            ),
            "client_observed_completion_tokens_not_128": sum(
                value != 128 for value in all_observed
            ),
            "disclosure": (
                "tg128 was requested with exact-tg; client-observed completion counts "
                "were 125-128, and throughput used observed token timestamps"
            ),
        },
    }
    return result_export, integrity_export


def telemetry_data(run_dir: Path, summary: dict[str, Any]) -> dict[str, Any]:
    samples = [
        json.loads(line)
        for line in (run_dir / "collector" / "samples.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    host_keys = sorted(host["alias"] for host in samples[0]["hosts"])
    lifecycle_changes = 0
    for host_key in host_keys:
        identities = {
            (host["container_restarts"], host["container_started_at"])
            for sample in samples
            for host in sample["hosts"]
            if host["alias"] == host_key
        }
        if len(identities) != 1:
            lifecycle_changes += 1
    integrity = summary["integrity_review"]
    telemetry = summary["telemetry"]
    return {
        "schema_version": 1,
        "full_campaign": {
            "collector_samples": len(samples),
            "monitored_devices": len(host_keys),
            "first_sample_utc": telemetry["first_sample_utc"],
            "last_sample_utc": telemetry["last_sample_utc"],
            "minimum_healthy_devices": telemetry["minimum_healthy_count"],
            "non_full_health_samples": telemetry["non_8_healthy_sample_count"],
            "minimum_available_memory_pct": min(
                host["min_mem_available_pct"] for host in telemetry["hosts"].values()
            ),
            "maximum_swap_used_kib": telemetry["max_swap_used_kib"],
            "oom_records": telemetry["oom_record_count"],
            "container_lifecycle_identity_changes": lifecycle_changes,
            "software_or_hardware_thermal_slowdown_records": 0,
        },
        "official_measured_lane": integrity["official_lane"],
        "public_measured_request_windows": integrity["public_measured_request_windows"],
        "retained_idle_exception": {
            "sample_utc": integrity["inactive_request_gate_breaches"][0]["sample_utc"],
            "minimum_gpu_tlimit_margin_c": integrity["inactive_request_gate_breaches"][0][
                "minimum_gpu_tlimit_margin_c"
            ],
            "context": "inter-condition idle cooldown, outside a measured request window",
        },
        "thermal_metric_definition": (
            "GPU T.Limit margin is remaining margin to the device limit, not absolute temperature"
        ),
    }


def gate_data(run_dir: Path) -> dict[str, Any]:
    gates = []
    for path in sorted((run_dir / "gates").glob("*.json")):
        source = read_json(path)
        gates.append(
            {
                "stage": source["stage"],
                "checked_utc": source["checked_utc"],
                "collector_counter_advanced": source["counter_after"] > source["counter_before"],
                "errors": len(source["errors"]),
                "pass": source["pass"],
            }
        )
    if len(gates) != 20 or not all(item["pass"] for item in gates):
        raise RuntimeError("stage-gate export failed")
    return {"schema_version": 1, "stage_gate_count": len(gates), "all_pass": True, "gates": gates}


def filtered_model_manifest(source: Path) -> tuple[str, int, int]:
    if sha256(source) != EXPECTED_MODEL_MANIFEST_SHA256:
        raise RuntimeError("model manifest hash does not match the publication anchor")
    output: list[str] = []
    weight_shards = 0
    for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (\./[^\r\n]+)", line)
        if not match:
            raise RuntimeError(f"invalid model manifest line {line_number}")
        relative = match.group(2)
        if relative.startswith("./.cache/"):
            continue
        if PRIVATE_HOST_PATTERN.search(relative) or ".." in Path(relative).parts:
            raise RuntimeError(f"unsafe model manifest path at line {line_number}")
        output.append(line)
        if re.fullmatch(r"\./model-[0-9]{5}-of-[0-9]{5}\.safetensors", relative):
            weight_shards += 1
    if len(output) != 75 or weight_shards != 48:
        raise RuntimeError("unexpected filtered model manifest shape")
    return "\n".join(output) + "\n", len(output), weight_shards


def assert_public_text_safe(root: Path) -> None:
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in {".json", ".md", ".txt", ".sha256", ".py"}:
            continue
        text = path.read_text(encoding="utf-8")
        match = PRIVATE_HOST_PATTERN.search(text)
        if match:
            raise RuntimeError(f"private pattern found in generated output {path.name}: {match.group(0)}")


def main() -> int:
    args = parse_args()
    run_dir = args.private_run.resolve()
    output_root = args.output_root.resolve()
    if not run_dir.is_dir():
        raise RuntimeError("private run directory is missing")
    if run_dir == output_root or run_dir in output_root.parents:
        raise RuntimeError("public output must be separate from the private run")

    private_entries = verify_private_manifest(run_dir)
    summary = read_json(run_dir / "BASELINE_SUMMARY.json")
    contract = read_json(run_dir / "RUN_CONTRACT.json")
    if not contract.get("complete") or contract["contract_revision"] != "v1.4":
        raise RuntimeError("canonical v1.4 contract is not complete")
    if contract["model_revision"] != EXPECTED_MODEL_REVISION:
        raise RuntimeError("model revision mismatch")
    if contract["image_id"] != EXPECTED_IMAGE_ID:
        raise RuntimeError("image identity mismatch")
    if (run_dir / "campaign.exit-status").read_text(encoding="utf-8").strip() != "0":
        raise RuntimeError("campaign did not exit successfully")

    official_raw, official_aggregate = official_data(run_dir, contract)
    public_results, public_integrity = public_comparison_data(run_dir)
    model_manifest_text, public_model_files, weight_shards = filtered_model_manifest(
        args.model_manifest.resolve()
    )

    data_root = output_root / "data"
    write_json(data_root / "official-vllm" / "raw-runs.json", official_raw)
    write_json(data_root / "official-vllm" / "aggregate-results.json", official_aggregate)
    write_json(data_root / "public-llama-benchy" / "results.json", public_results)
    write_json(data_root / "public-llama-benchy" / "request-integrity.json", public_integrity)
    write_json(data_root / "telemetry-summary.json", telemetry_data(run_dir, summary))
    write_json(data_root / "stage-gates.json", gate_data(run_dir))
    write_json(
        data_root / "run-identity.json",
        {
            "schema_version": 1,
            "claim_scope": "pre-optimization baseline, not a record claim",
            "private_evidence_anchor": {
                "run_id": "20260801T013700Z",
                "sealed_manifest_entries": private_entries,
                "sealed_manifest_sha256": EXPECTED_PRIVATE_MANIFEST_SHA256,
            },
            "model": {
                "repository": contract["model_repository"],
                "revision": contract["model_revision"],
                "private_full_manifest_entries": 151,
                "private_full_manifest_sha256": EXPECTED_MODEL_MANIFEST_SHA256,
                "public_model_file_hash_entries": public_model_files,
                "weight_shards": weight_shards,
                "regular_file_bytes": 166898669245,
                "license_file_sha256": "f2c6c602815669d292889e5be8c802f2ed950653b77999b1584e8e6aed25d040",
            },
            "runtime": {
                "devices": 8,
                "independent_replicas": 4,
                "tensor_parallel_size": 2,
                "expert_parallel_enabled": True,
                "container_image_id": contract["image_id"],
                "vllm_version": contract["vllm_version"],
                "upstream_vllm_commit_embedded_in_version": "264bce1da81e27d638e7cf265b4cbd125d023c38",
                "torch_version": "2.12.0+cu132",
                "transformers_version": "5.14.1",
                "kv_cache_dtype": "fp8",
                "max_model_len": 65536,
                "max_num_seqs": 4,
                "max_num_batched_tokens": 8192,
                "prefix_caching_enabled": True,
                "execution_mode": "eager",
                "speculative_decode_profile": "DSpark, seven greedy proposal tokens",
            },
            "public_reproduction_boundary": {
                "official_benchmark_client": "upstream vLLM bench serve interface",
                "public_comparison_client_commit": contract["llama_benchy_commit"],
                "exact_custom_runtime_image_build_recipe_included": False,
                "transport_evidence": "configured and observed paths; no packet capture retained",
            },
        },
    )
    (data_root / "model-files.sha256").write_text(model_manifest_text, encoding="utf-8")

    assert_public_text_safe(data_root)
    print(f"public_data_written={data_root}")
    print("official_measured_requests=480")
    print("public_measured_requests=240")
    print(f"private_manifest_entries_verified={private_entries}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
