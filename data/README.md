# Sanitized data dictionary

| Path | Contents |
|---|---|
| `run-identity.json` | Model revision, anonymous topology, exact runtime identity, and reproduction boundary |
| `model-files.sha256` | Hashes for 75 checkpoint-directory files; local cache metadata omitted |
| `official-vllm/raw-runs.json` | 24 allowlisted numeric result records, including detailed timing arrays and token lengths |
| `official-vllm/aggregate-results.json` | Recomputed pair and cross-pair headline statistics |
| `public-llama-benchy/results.json` | Four sanitized llama-benchy result sets; no text snippets or request identifiers |
| `public-llama-benchy/request-integrity.json` | Request counts, errors, prompt-token distributions, and observed completion-token disclosure |
| `stage-gates.json` | Twenty sanitized stage outcomes with timestamps and counter-advancement state |
| `telemetry-summary.json` | Aggregate health, memory, lifecycle, thermal, and idle-exception facts |
| `agent-showcase-512.json` | Sanitized counters, latency summaries, capture hashes, media properties, and findings for the fresh live 512-workflow run |
| `agent-showcase-1024.json` | Sanitized counters, latency summaries, capture-filter disclosure, media hashes, and findings for the fresh live 1,024-workflow run |
| `agent-showcase-replication.json` | Six-run replication record: three complete four-pair campaigns per load, run-level distributions, group summaries, excluded-attempt disclosures, and private-receipt hashes |
| `hermes-audit-plan.json` | Planned-only Hermes Agent source snapshot and frozen 1,024-workflow audit contract; contains no run result or vulnerability candidate |

No data file contains generated text, raw logs, commands, local paths, network
addresses, SSH material, or per-host identifiers.

In all three agent-showcase records, `semantic_failures` is the historical
runner field for HTTP status, expected-model identity, and nonempty-response
validation. It is not a model-quality or complete instruction-following score.
The replication JSON carries that definition in its scope object. Marker-gate
findings are reported separately and are not silently relabeled.

Use [recompute_results.py](../scripts/recompute_results.py) to calculate every
headline result directly from the public numeric records.

Use [recompute_replication.py](../scripts/recompute_replication.py) to verify
the frozen run order and eligibility gates, rebuild both group summaries from
the six run-level records, and recompute the 1,024-over-512 ratios. It requires
only Python's standard library.

Use [verify_hermes_audit_plan.py](../scripts/verify_hermes_audit_plan.py) to
check the frozen workflow allocation, source anchors, pre-run labels, and claim
boundary. To independently recompute the upstream source inventory from a
checkout of the exact pinned commit, use
[inventory_hermes_snapshot.py](../scripts/inventory_hermes_snapshot.py) with
`--verify data/hermes-audit-plan.json`.
