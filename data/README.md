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

No data file contains generated text, raw logs, commands, local paths, network
addresses, SSH material, or per-host identifiers.

Use [recompute_results.py](../scripts/recompute_results.py) to calculate every
headline result directly from the public numeric records.
