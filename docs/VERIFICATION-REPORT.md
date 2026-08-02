# Publication verification report

Verification timestamp: `2026-08-02T20:04:50Z`

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
| 1,024 capture filter | Pass with disclosure | 15 of 1,872 raw frames caught incomplete tmux repaints and were excluded; 1,857 original complete frames retained; no synthetic or replayed frames added |
| 1,024 social edit | Pass with human gate | H.264/yuv420p; 1920x1080; 5 fps; 300 frames; 60 seconds; full decode; no black intervals; browser playback verified; MP4 distributed separately |
| Public manifest | Pass | Every configured public file covered; manifest does not hash itself or `.git` internals |
| Privacy scan | Pass | No user-home path, private address, per-host label, personal email, SSH material, credential shape, generated-text JSON field, or account-scoped image origin; live-wall stills contain only anonymous pair/cell labels and bounded output from the synthetic showcase corpus |
| JSON parse | Pass | All public JSON documents parsed successfully |
| Local links | Pass | All repository-relative Markdown targets resolved |
| Symbolic links | Pass | None present in the publication tree |
| Graphic | Pass | Original 1,264 x 712 browser-capture JPEG reviewed; eight visible crops of the official NVIDIA DGX Spark product photograph and the official DeepSeek avatar are present; four rows contain exactly two Spark crops each with four `TP=2` links; no desktop or monitor; exact model and configuration text; visible `Courtesy of NVIDIA`; no person, private room detail, rack photo, host label, address, performance figure, record claim, personal identifier, account URL, or watermark |
| Graphic provenance | Pass with boundary | No AI-generated hardware; official NVIDIA photograph and DeepSeek avatar source URLs and downloaded-byte hashes recorded; the Spark crop uses source coordinates `x=775,y=420,w=320,h=200` and is repeated eight times for visual clarity; third-party pixels and marks remain excluded from Gumbii Digital reuse rights; the repeated crops and connectors are explicitly visual-summary elements rather than physical-topology, inventory, or benchmark evidence |
| External links | Pass | Thirteen unique references returned HTTP 200 through the system client |
| PDF gates | Not applicable | This repository contains no PDFs |
| Reuse terms | Pass | Public but not open source; all-rights-reserved terms recorded in `COPYRIGHT.md` |
| Remote GitHub state | Post-push gate | Repository visibility, default-branch SHA, live links, and raw manifest bytes must be checked after publication |

## External links

Thirteen unique model, runtime, license, community, product-photography, and
rights references returned HTTP `200` through an independent
redirect-following system-client check.

The publication framework's optional Python URL checker may depend on the
local Python certificate chain. External-link status was therefore verified
independently with the system HTTP client rather than treating a checker
environment failure as a pass.

## Repeat the local gates

```bash
python3 scripts/recompute_results.py
python3 scripts/verify_public_bundle.py
```

Regenerate the publication ledger only after deliberately reviewing a changed
file list:

```bash
python3 scripts/generate_manifest.py
```
