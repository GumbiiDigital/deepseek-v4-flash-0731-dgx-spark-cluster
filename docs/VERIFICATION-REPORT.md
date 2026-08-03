# Publication verification report

Verification timestamp: `2026-08-03T00:04:01Z`

## Result

The final local publication candidate passed its arithmetic, integrity,
privacy, JSON, local-link, image-review, and publication-policy gates. Live
GitHub state is a separate post-push check and is not asserted by this local
report.

| Gate | Result | Evidence |
|---|---|---|
| Private run seal | Pass | 331 entries verified; manifest hash matched the public anchor |
| Model-source anchor | Pass | 151-entry private manifest hash matched; 75 non-cache file hashes exported |
| Official request integrity | Pass | 24 files; 480 completed; 0 failed; all 2,048-in/128-out |
| Public-method request integrity | Pass | 240 measured; 0 errors; observed completion disclosure 125-128, mean 127.7 |
| Independent arithmetic | Pass | Pair medians, mean, repetition sums, aggregate medians, and spread recomputed |
| Stage gates | Pass | 20 of 20 |
| Fresh live 512-workflow record | Pass with findings | 512 / 512 workflows; 1,536 / 1,536 requests; 0 failed; all 512 labels in all 665 corrected source and 300 edit frames; 3 marker-format notes |
| Fresh live 1,024-workflow record | Pass with findings | 1,024 / 1,024 workflows; 3,072 / 3,072 requests; 0 failed; all 1,024 labels in all 1,857 retained source and 300 edit frames; 4 marker-format notes |
| Six-run replication campaign | Pass with findings | Frozen order `512,1024,1024,512,512,1024`; six of six complete four-pair campaigns passed; 4,608 / 4,608 workflows; 13,824 / 13,824 calls; 0 failed workflows; 20 marker findings disclosed |
| Replication arithmetic | Pass | Public standard-library verifier rebuilt both `n=3` group distributions and ratios: 1.985424x workflow median, 1.999551x active span, and 1.002549x completion-token rate |
| Replication failure disposition | Pass with disclosure | Pre-work import failure retained with zero model requests; later collector-interrupted campaign retained and excluded as a whole, including its one clean run; no retry or exclusion inside the eligible replacement campaign |
| 1,024 capture filter | Pass with disclosure | 15 of 1,872 raw frames caught incomplete tmux repaints and were excluded; 1,857 original complete frames retained; no synthetic or replayed frames added |
| 1,024 social edit | Pass with human gate | H.264/yuv420p; 1920x1080; 5 fps; 300 frames; 60 seconds; full decode; no black intervals; browser playback verified; MP4 distributed separately |
| Public manifest | Pass | Every configured public file covered; manifest does not hash itself or `.git` internals |
| Privacy scan | Pass | No user-home path, private address, per-host label, personal email, SSH material, credential shape, generated-text JSON field, or account-scoped image origin; replication data uses anonymous run/pair labels, aggregate values, and hashes only |
| JSON parse | Pass | All public JSON documents parsed successfully |
| Local links | Pass | All repository-relative Markdown targets resolved |
| Symbolic links | Pass | None present in the publication tree |
| Graphic | Pass | Original 1,264 x 712 browser-capture JPEG reviewed; eight visible crops of the official NVIDIA DGX Spark product photograph and the official DeepSeek avatar are present; four rows contain exactly two Spark crops each with four `TP=2` links; no desktop or monitor; exact model and configuration text; visible `Courtesy of NVIDIA`; no person, private room detail, rack photo, host label, address, performance figure, record claim, personal identifier, account URL, or watermark |
| Graphic provenance | Pass with boundary | No AI-generated hardware; official NVIDIA photograph and DeepSeek avatar source URLs and downloaded-byte hashes recorded; the Spark crop uses source coordinates `x=775,y=420,w=320,h=200` and is repeated eight times for visual clarity; third-party pixels and marks remain excluded from Gumbii Digital reuse rights; the repeated crops and connectors are explicitly visual-summary elements rather than physical-topology, inventory, or benchmark evidence |
| Replication graphic | Pass with boundary | Reviewed 1,600 x 900 JPEG; every value derived from the verified public JSON; official Spark crop repeated eight times; official DeepSeek avatar; accepted Grok background hash recorded and limited to decorative abstract light/whale imagery; rejected clipped Quick Look raster not published |
| Hermes source snapshot | Pass | Exact upstream commit `a6defd4f1549da3fe1d08d6f746fc645c64543f0` independently inventoried: 8,345 tracked files, 138,840,634 bytes, 8,248 text files, 2,554,893 text lines, 97 binary files, and zero Python parse errors; recomputed snapshot matched the public JSON exactly |
| Hermes audit pre-run contract | Pass as planned-only record | Workflow lanes total 1,024; allocation is 960 real units, 32 positive controls, and 32 negative controls; three model stages imply 3,072 expected calls; source/document hashes and pre-run labels verified |
| Hermes audit execution | Not run | Audit-unit generation, harness implementation, offline schema test, 64-workflow live canary, 1,024-workflow campaign, candidate reproduction, human review, and disclosure remain planned; no result or finding is claimed |
| External links | Pass with tool disclosure | Twenty-one unique referenced URLs, including the repository and pinned Hermes Agent source/policy links, returned HTTP 2xx/3xx through the system client; the optional Python URL lane failed on its local CA chain rather than on HTTP status |
| PDF gates | Not applicable | This repository contains no PDFs |
| Reuse terms | Pass | Public but not open source; all-rights-reserved terms recorded in `COPYRIGHT.md` |
| Remote GitHub state | Post-push gate | Repository visibility, default-branch SHA, live links, and raw manifest bytes must be checked after publication |

## External links

Twenty-one unique repository, model, runtime, license, community,
product-photography, and rights references returned HTTP `2xx` or `3xx` through
an independent redirect-following system-client check.

The publication framework's optional Python URL checker may depend on the
local Python certificate chain. External-link status was therefore verified
independently with the system HTTP client rather than treating a checker
environment failure as a pass.

## Repeat the local gates

```bash
python3 scripts/recompute_results.py
python3 scripts/recompute_replication.py
python3 scripts/verify_hermes_audit_plan.py
python3 scripts/verify_public_bundle.py
```

To repeat the full upstream source inventory, first check out the exact pinned
Hermes Agent commit, then run:

```bash
python3 scripts/inventory_hermes_snapshot.py \
  --repo /path/to/hermes-agent \
  --verify data/hermes-audit-plan.json
```

Regenerate the publication ledger only after deliberately reviewing a changed
file list:

```bash
python3 scripts/generate_manifest.py
```
