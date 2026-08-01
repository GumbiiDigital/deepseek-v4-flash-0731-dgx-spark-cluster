# DeepSeek V4 Flash 0731 on Eight DGX Sparks

![Stylized hero view of eight DGX Spark systems in four tensor-parallel pairs with a DeepSeek whale emblem](media/deepseek-v4-flash-0731-dgx-spark-cluster-hero.jpg)

*[Created with Grok](https://x.ai/legal/brand-guidelines). Conceptual artwork;
the Spark form factor and whale emblem are reference-derived, and this is not a
photograph or topology diagram of the live cluster.*

I loaded `deepseek-ai/DeepSeek-V4-Flash-0731` across all eight of my NVIDIA
DGX Spark systems. One replica needs two Sparks, so I split the cluster into
four independent tensor-parallel pairs and ran all four pairs at the same time.

This repository is where I am keeping the whole project: the first frozen
measurements, the exact method, the failures, the changes, and every
optimization that earns its way into a new measured profile.

The first result is a **pre-optimization baseline, not a record claim**. That
distinction matters. I wanted a clean starting line before I began tuning the
four pairs in different ways.

## First measured profile

Each value is the median of three independent repetitions. Every repetition
contains 20 measured requests after four excluded warmups.

| Anonymous pair | c1 output tok/s | c1 TPOT ms | c4 output tok/s | c4 TPOT ms |
|---|---:|---:|---:|---:|
| A | 21.1470 | 38.2088 | 39.3938 | 83.8383 |
| B | 20.8370 | 38.0440 | 39.0501 | 84.8422 |
| C | 21.0258 | 38.1040 | 39.5904 | 83.1218 |
| D | 21.2443 | 37.8461 | 39.5439 | 84.5273 |

The median of the repetition-wise four-pair sums was **84.4107 output tok/s
at c1** and **158.2688 output tok/s at c4**.

What stands out to me is the balance across the cluster:

- all **480 of 480** official measured requests completed;
- every official request recorded exactly 2,048 input tokens and 128 output
  tokens;
- pair spread was **1.9337% at c1** and **1.3715% at c4**;
- the four pairs ran concurrently, with no more than three seconds of recorded
  start skew.

That is useful because it gives me four closely matched starting points. When
I change one pair, I can compare it against three others that began in nearly
the same place.

## How I tested it

The primary lane used the deployed vLLM build's official `vllm bench serve`
interface. Each two-Spark replica used tensor parallelism `2`, expert
parallelism, FP8 KV cache, prefix caching, eager execution, and DSpark
speculative decoding.

I also ran a secondary `llama-benchy` lane for directional comparison with a
community result. I keep those client metrics separate because the model
revision, runtime, serving profile, and client behavior are not
apples-to-apples.

The complete setup, seeds, metric definitions, ordering, telemetry gates, and
known limitations are in [Methodology](docs/METHODOLOGY.md).

## Where I am taking it next

The next profiles will test changes to the runtime, scheduling, cache behavior,
speculative decoding, concurrency, and pair-specific tuning. Those are planned
experiments, not results yet.

I will keep the original profile frozen. A faster configuration becomes a new
profile with its own inputs, measurements, and evidence instead of quietly
rewriting the starting point.

## Verify the numbers yourself

Only Python's standard library is required:

```bash
python3 scripts/recompute_results.py
python3 scripts/verify_public_bundle.py
```

The first command rebuilds every headline figure from the sanitized numeric
runs. The second checks the publication manifest, JSON documents, local links,
privacy rules, and symbolic-link boundary.

## Repository map

| Path | Contents |
|---|---|
| [docs/METHODOLOGY.md](docs/METHODOLOGY.md) | Frozen profile, request design, seeds, ordering, and metric definitions |
| [docs/RESULTS.md](docs/RESULTS.md) | Complete results and telemetry summary |
| [docs/CONTEXTUAL-COMPARISON.md](docs/CONTEXTUAL-COMPARISON.md) | Directional community comparison and its limits |
| [docs/VERIFICATION.md](docs/VERIFICATION.md) | What the public evidence proves and what it does not |
| [docs/VERIFICATION-REPORT.md](docs/VERIFICATION-REPORT.md) | Publication-gate receipt |
| [docs/PRIVACY.md](docs/PRIVACY.md) | Sanitization method and private/public boundary |
| [docs/GROK-EXPOSE-HANDOFF.md](docs/GROK-EXPOSE-HANDOFF.md) | Fact sheet and guardrails for the public write-up |
| [data/README.md](data/README.md) | Sanitized data dictionary |
| [media/README.md](media/README.md) | Graphic provenance and acceptance record |
| [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) | Upstream projects, revisions, and terms |

## How I treat the evidence

- A completed request is not automatically a comparable benchmark.
- A one-off peak is not a stable profile.
- Two benchmark clients do not become equivalent because both report tokens
  per second.
- A private route observation is not packet-capture proof.
- A clean baseline is not a speed record.
- Unknown stays unknown. I do not turn it green for convenience.

The custom runtime image is pinned by digest, but the image and build recipe
are not distributed here. The public bundle can reproduce the arithmetic and
the method; it cannot produce a bit-for-bit rebuild of that private image.

Raw operational logs, generated model text, account paths, hostnames,
addresses, ports, and topology remain private. The public data uses anonymous
pair labels and publishes only the measurements needed to audit the result.

## Credits and scope

DeepSeek, vLLM, llama-benchy, NVIDIA product names, and their trademarks belong
to their respective owners. This is an independently maintained Gumbii Digital
engineering record. It is not an official NVIDIA, DeepSeek, vLLM, or
llama-benchy result, and no endorsement is implied.

No model weights, serving-engine source, comparison-client source, or container
image are redistributed here.

## Copyright

Copyright (c) 2026 Gumbii Digital. All rights reserved. See
[COPYRIGHT.md](COPYRIGHT.md) for the publication and reuse terms.
