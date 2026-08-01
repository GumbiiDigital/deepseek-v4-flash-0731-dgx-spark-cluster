#!/usr/bin/env python3
"""Recompute every headline claim from the sanitized public numeric data."""

from __future__ import annotations

import json
import math
import statistics
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PAIR_IDS = ("A", "B", "C", "D")


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def close(label: str, observed: float, expected: float, tolerance: float = 0.00005) -> None:
    if not math.isclose(observed, expected, rel_tol=0, abs_tol=tolerance):
        raise AssertionError(f"{label}: observed {observed}, expected {expected}")


def main() -> int:
    raw = load(DATA / "official-vllm" / "raw-runs.json")
    aggregate = load(DATA / "official-vllm" / "aggregate-results.json")
    public_results = load(DATA / "public-llama-benchy" / "results.json")
    public_integrity = load(DATA / "public-llama-benchy" / "request-integrity.json")
    gates = load(DATA / "stage-gates.json")
    telemetry = load(DATA / "telemetry-summary.json")
    identity = load(DATA / "run-identity.json")

    runs = raw["runs"]
    if len(runs) != 24:
        raise AssertionError(f"expected 24 official raw runs, found {len(runs)}")
    if len({(r["pair_id"], r["concurrency"], r["repetition"]) for r in runs}) != 24:
        raise AssertionError("official condition identities are not unique")

    completed = failed = 0
    for run in runs:
        metrics = run["metrics"]
        completed += metrics["completed"]
        failed += metrics["failed"]
        if metrics["input_lens"] != [2048] * 20:
            raise AssertionError("official input-length invariant failed")
        if metrics["output_lens"] != [128] * 20:
            raise AssertionError("official output-length invariant failed")
    if (completed, failed) != (480, 0):
        raise AssertionError(f"official completion invariant failed: {(completed, failed)}")

    for pair_id in PAIR_IDS:
        for concurrency in (1, 4):
            selected = [
                r for r in runs if r["pair_id"] == pair_id and r["concurrency"] == concurrency
            ]
            values = [r["metrics"]["output_throughput"] for r in selected]
            expected = aggregate["pairs"][pair_id][f"c{concurrency}"]
            close(
                f"pair {pair_id} c{concurrency} median",
                round(statistics.median(values), 4),
                expected["output_throughput_tok_s_median"],
            )

    for concurrency in (1, 4):
        pair_medians = [
            statistics.median(
                r["metrics"]["output_throughput"]
                for r in runs
                if r["pair_id"] == pair_id and r["concurrency"] == concurrency
            )
            for pair_id in PAIR_IDS
        ]
        pair_mean = statistics.mean(pair_medians)
        spread = (max(pair_medians) - min(pair_medians)) / pair_mean * 100
        repetition_sums = [
            sum(
                r["metrics"]["output_throughput"]
                for r in runs
                if r["concurrency"] == concurrency and r["repetition"] == repetition
            )
            for repetition in (1, 2, 3)
        ]
        expected = aggregate["cross_pair"][f"c{concurrency}"]
        close(f"c{concurrency} mean pair", round(pair_mean, 4), expected["mean_pair_output_tok_s"])
        close(f"c{concurrency} pair spread", round(spread, 4), expected["pair_spread_pct"])
        close(
            f"c{concurrency} aggregate median",
            round(statistics.median(repetition_sums), 4),
            expected["four_pair_aggregate_output_tok_s_median"],
        )
        for observed, stored in zip(
            repetition_sums, expected["per_repetition_four_pair_output_tok_s"], strict=True
        ):
            close(f"c{concurrency} repetition sum", observed, stored, tolerance=1e-10)

    public_pairs = public_results["pairs"]
    if len(public_pairs) != 4 or sum(len(pair["benchmarks"]) for pair in public_pairs) != 32:
        raise AssertionError("public comparison row count failed")
    if public_integrity["overall"]["measured_requests"] != 240:
        raise AssertionError("public measured-request count failed")
    if public_integrity["overall"]["errors"] != 0:
        raise AssertionError("public request errors were recorded")
    if (
        public_integrity["overall"]["client_observed_completion_tokens_minimum"],
        public_integrity["overall"]["client_observed_completion_tokens_maximum"],
        public_integrity["overall"]["client_observed_completion_tokens_mean"],
    ) != (125, 128, 127.7):
        raise AssertionError("public output-token disclosure failed")

    if gates["stage_gate_count"] != 20 or not gates["all_pass"]:
        raise AssertionError("stage-gate integrity failed")
    if telemetry["full_campaign"]["collector_samples"] != 409:
        raise AssertionError("telemetry sample count failed")
    if telemetry["full_campaign"]["container_lifecycle_identity_changes"] != 0:
        raise AssertionError("container lifecycle identity changed during the run")
    if identity["claim_scope"] != "pre-optimization baseline, not a record claim":
        raise AssertionError("claim scope is missing")

    c1 = aggregate["cross_pair"]["c1"]
    c4 = aggregate["cross_pair"]["c4"]
    pair_c1 = [aggregate["pairs"][pair]["c1"]["output_throughput_tok_s_median"] for pair in PAIR_IDS]
    pair_c4 = [aggregate["pairs"][pair]["c4"]["output_throughput_tok_s_median"] for pair in PAIR_IDS]
    print("RECOMPUTE PASS")
    print(f"official_measured_requests={completed} official_failed_requests={failed}")
    print(f"c1_pair_range={min(pair_c1):.4f}-{max(pair_c1):.4f} output_tok_s")
    print(f"c4_pair_range={min(pair_c4):.4f}-{max(pair_c4):.4f} output_tok_s")
    print(
        "four_pair_aggregate_median="
        f"{c1['four_pair_aggregate_output_tok_s_median']:.4f}/"
        f"{c4['four_pair_aggregate_output_tok_s_median']:.4f} output_tok_s"
    )
    print(f"range_over_mean_pair_spread={c1['pair_spread_pct']:.4f}%/{c4['pair_spread_pct']:.4f}%")
    print("public_requested_tg=128 public_observed_completion_tokens=125-128 mean=127.7")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
