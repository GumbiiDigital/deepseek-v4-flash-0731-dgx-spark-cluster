#!/usr/bin/env python3
"""Recompute and verify the public six-run concurrency comparison."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import statistics
from typing import Any


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    index = math.ceil((len(ordered) - 1) * fraction)
    return ordered[max(0, min(len(ordered) - 1, index))]


def distribution(values: list[float]) -> dict[str, float | int]:
    mean = statistics.fmean(values)
    sample_sd = statistics.stdev(values) if len(values) > 1 else 0.0
    return {
        "n": len(values),
        "min": round(min(values), 6),
        "p05": round(percentile(values, 0.05), 6),
        "p25": round(percentile(values, 0.25), 6),
        "p50": round(percentile(values, 0.50), 6),
        "p75": round(percentile(values, 0.75), 6),
        "p95": round(percentile(values, 0.95), 6),
        "p99": round(percentile(values, 0.99), 6),
        "max": round(max(values), 6),
        "mean": round(mean, 6),
        "sample_sd": round(sample_sd, 6),
        "cv_pct": round(100 * sample_sd / mean, 6) if mean else 0.0,
    }


def equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: actual={actual!r} expected={expected!r}")


def verify(record: dict[str, Any]) -> dict[str, Any]:
    scope = record["scope"]
    runs = record["runs"]
    order = [512, 1024, 1024, 512, 512, 1024]
    equal(scope["experimental_unit"], "one complete four-pair campaign", "experimental unit")
    equal(scope["individual_agents_are_independent_replicates"], False, "agent independence")
    equal(scope["run_order"], order, "frozen run order")
    equal(
        scope["semantic_failure_field_definition"],
        "HTTP status, expected-model identity, and nonempty-response validation; not a model-quality or complete instruction-following score",
        "semantic failure definition",
    )
    equal(
        scope["marker_mismatch_definition"],
        "The response completed the transport contract but did not contain the workflow's unique expected marker",
        "marker mismatch definition",
    )
    equal(record["runtime_invariants"]["configured_model_sequence_ceiling"], 16, "model sequence ceiling")
    equal(record["runtime_invariants"]["service_mutation"], False, "service mutation")
    equal(record["runtime_invariants"]["external_x_requests"], False, "external X requests")
    equal(
        record["runtime_invariants"]["transport"],
        "runner_and_inference_on_pair_head_localhost; lan_ssh_control_only",
        "transport",
    )
    equal(len(runs), 6, "run count")
    equal([run["agents"] for run in runs], order, "observed run order")

    prework = record.get("prework_harness_attempt")
    if prework:
        equal(prework["classification"], "harness_failure_before_experimental_work", "pre-work class")
        equal(prework["counted_as_experimental_unit"], False, "pre-work inclusion")
        equal(prework["workload_runs_started"], 0, "pre-work runs")
        equal(prework["model_requests_issued"], 0, "pre-work requests")

    interrupted = record.get("interrupted_campaign_attempt")
    if interrupted:
        equal(interrupted["included_in_replacement_analysis"], False, "interrupted inclusion")
        equal(interrupted["clean_runs_completed_before_interrupt"], 1, "pre-interrupt runs")
        equal(interrupted["interrupted_run_ordinal"], 2, "interrupted ordinal")

    for ordinal, run in enumerate(runs, 1):
        prefix = f"R{ordinal:02d}"
        equal(run["run_label"], prefix, f"{prefix} label")
        equal(run["ordinal"], ordinal, f"{prefix} ordinal")
        equal(run["status"], "pass", f"{prefix} status")
        equal(run["completed_agents"], run["agents"], f"{prefix} completed")
        equal(run["failed_agents"], 0, f"{prefix} failures")
        equal(run["expected_requests"], run["agents"] * 3, f"{prefix} expected requests")
        equal(run["requests_completed"], run["expected_requests"], f"{prefix} completed requests")
        equal(run["max_live_agent_workflows"], run["agents"], f"{prefix} live watermark")
        equal(run["max_client_requests_in_flight"], run["agents"], f"{prefix} request watermark")
        equal(run["normalized_runtime_identity_unchanged"], True, f"{prefix} runtime identity")
        equal(run["functional_probes_passed"], 8, f"{prefix} probes passed")
        equal(run["functional_probes_total"], 8, f"{prefix} probes total")
        equal(run["semantic_failures"], 0, f"{prefix} transport contract")
        equal(run["check_verdict_missing"], 0, f"{prefix} check verdicts")
        equal(run["agent_workflow_seconds"]["n"], run["agents"], f"{prefix} duration count")
        for field in ("thermal_slowdown_observations", "oom_observations", "probe_error_count", "max_swap_used_kib"):
            equal(run["collector"][field], 0, f"{prefix} {field}")

    recomputed: dict[str, dict[str, Any]] = {}
    for agents in (512, 1024):
        selected = [run for run in runs if run["agents"] == agents]
        expected = {
            "agents": agents,
            "experimental_units": 3,
            "run_ordinals": [run["ordinal"] for run in selected],
            "run_level_agent_workflow_medians_seconds": [float(run["agent_workflow_seconds"]["p50"]) for run in selected],
            "run_level_agent_workflow_medians": distribution([float(run["agent_workflow_seconds"]["p50"]) for run in selected]),
            "active_span_seconds": distribution([float(run["active_span_seconds"]) for run in selected]),
            "completion_tokens_per_active_second": distribution([float(run["completion_tokens_per_active_second"]) for run in selected]),
            "requests_per_active_second": distribution([float(run["requests_per_active_second"]) for run in selected]),
            "all_runs_passed": True,
        }
        equal(record["groups"][str(agents)], expected, f"group {agents}")
        recomputed[str(agents)] = expected

    comparison = record["comparison"]
    equal(comparison["agent_count_ratio"], 2.0, "agent-count ratio")
    equal(comparison["campaign_level_n_per_load"], 3, "campaign n")
    equal(comparison["confidence_interval"], None, "confidence interval")
    ratios = {
        "median_of_run_level_agent_workflow_medians_ratio_1024_over_512": round(recomputed["1024"]["run_level_agent_workflow_medians"]["p50"] / recomputed["512"]["run_level_agent_workflow_medians"]["p50"], 6),
        "median_active_span_ratio_1024_over_512": round(recomputed["1024"]["active_span_seconds"]["p50"] / recomputed["512"]["active_span_seconds"]["p50"], 6),
        "median_completion_token_rate_ratio_1024_over_512": round(recomputed["1024"]["completion_tokens_per_active_second"]["p50"] / recomputed["512"]["completion_tokens_per_active_second"]["p50"], 6),
    }
    for key, expected in ratios.items():
        equal(comparison[key], expected, key)
    return {
        "status": "pass",
        "runs": 6,
        "campaign_level_replicates_per_load": 3,
        "marker_mismatches_disclosed": sum(int(run["marker_mismatches"]) for run in runs),
        **ratios,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", nargs="?", type=Path, default=Path("data/agent-showcase-replication.json"))
    args = parser.parse_args()
    print(json.dumps(verify(json.loads(args.record.read_text(encoding="utf-8"))), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
