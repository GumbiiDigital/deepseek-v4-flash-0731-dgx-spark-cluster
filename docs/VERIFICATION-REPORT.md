# Publication verification report

Verification timestamp: `2026-08-01T03:35:33Z`

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
| Public manifest | Pass | Every configured public file covered; manifest does not hash itself or `.git` internals |
| Privacy scan | Pass | No user-home path, private address, per-host label, personal email, SSH material, credential shape, generated-text field, or account-scoped image origin |
| JSON parse | Pass | All public JSON documents parsed successfully |
| Local links | Pass | All repository-relative Markdown targets resolved |
| Symbolic links | Pass | None present in the publication tree |
| Graphic | Pass | Original 1,168 x 784 Grok JPEG reviewed; exactly eight nodes; no text, logos, people, or environment detail |
| Graphic provenance | Pass with boundary | Original bytes and embedded C2PA markers preserved; dedicated signature validation not run because `c2patool` was unavailable |
| External links | Pass with warning | Eight references returned HTTP 200 through the system client; the xAI brand-guideline page rendered through a browser but returned HTTP 403 to the unauthenticated command-line probe |
| PDF gates | Not applicable | This repository contains no PDFs |
| Reuse terms | Pass | Public but not open source; all-rights-reserved terms recorded in `COPYRIGHT.md` |
| Remote GitHub state | Post-push gate | Repository visibility, default-branch SHA, live links, and raw manifest bytes must be checked after publication |

## External links

Eight unique model, runtime, license, and community references returned HTTP
`200` through an independent redirect-following system-client check. The
official xAI brand-guideline page rendered successfully through a browser, but
the same unauthenticated command-line probe received HTTP `403`. That
client-specific rejection is recorded as a warning rather than mislabeled as
an all-client pass or a broken reader link.

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
