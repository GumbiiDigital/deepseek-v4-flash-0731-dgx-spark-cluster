# Directional community comparison

This comparison is contextual only. It is not evidence of a speed record, a
regression caused by the 0731 weights, or an exact reproduction.

The nearest public table found during the 2026-08-01 review was a community post
on the [NVIDIA Developer Forum](https://forums.developer.nvidia.com/t/deepseek-v4-flash-official-fp8-running-across-2x-dgx-spark-tp-2-mtp-200k-ctx-recipe-numbers/370309?page=3).
That table used the older `DeepSeek-V4-Flash` checkpoint and a different vLLM
build, serving profile, and benchmark-client version.

| Depth | This 0731 four-pair mean, c1 tg tok/s | Community single-pair c1 tg tok/s | Directional delta |
|---:|---:|---:|---:|
| 0 | 26.2856 | 38.35 | -31.46% |
| 4,096 | 25.6242 | 38.95 | -34.21% |
| 16,384 | 27.9291 | 35.44 | -21.19% |
| 32,768 | 26.3903 | 31.86 | -17.17% |

Reasons this is not apples-to-apples:

- different model revision;
- different vLLM code/build and launch flags;
- different llama-benchy revision;
- different client path and transport conditions;
- four-pair mean here versus one reported pair there;
- three repetitions are too few for a record-level statistical claim.

The external percentages should not lead a social post. They are retained to
show where the first unoptimized profile sits relative to a useful community report,
with the incompatibilities stated next to the values.
