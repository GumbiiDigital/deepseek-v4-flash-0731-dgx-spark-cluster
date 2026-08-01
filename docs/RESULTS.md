# Results

## Initial official-vLLM profile

These are three-repetition medians from exact server-observed 2,048-input and
128-output-token requests.

| Pair | c1 output tok/s | c1 TPOT ms | c4 output tok/s | c4 TPOT ms |
|---|---:|---:|---:|---:|
| A | 21.1470 | 38.2088 | 39.3938 | 83.8383 |
| B | 20.8370 | 38.0440 | 39.0501 | 84.8422 |
| C | 21.0258 | 38.1040 | 39.5904 | 83.1218 |
| D | 21.2443 | 37.8461 | 39.5439 | 84.5273 |

| Cross-pair statistic | c1 | c4 |
|---|---:|---:|
| Mean pair median, output tok/s | 21.0636 | 39.3946 |
| Four-pair aggregate median, output tok/s | 84.4107 | 158.2688 |
| Range-over-mean pair spread | 1.9337% | 1.3715% |

The c1 mean is calculated from the full-precision raw pair medians before final
rounding. The four-pair aggregate is not four times the rounded mean; it is the
median of the three repetition-wise sums.

## Request integrity

- Raw official result files: 24
- Measured requests: 480
- Completed requests: 480
- Failed requests: 0
- Server-observed input tokens: 2,048 for every request
- Output tokens: 128 for every request
- Maximum observed start skew across the four pairs: three seconds

## Telemetry integrity

- Full-campaign collector samples: 409
- Devices monitored: 8
- Swap use: zero
- OOM records: zero
- Container lifecycle identity changes: zero
- Software/hardware thermal-slowdown records: zero
- Minimum available memory: 6.019%
- Official measured lane: 8/8 healthy, minimum T.Limit margin 10 C
- Public measured request windows: 8/8 healthy, minimum T.Limit margin 6 C
- Retained idle exception: one inter-condition sample at exactly 5 C T.Limit margin

T.Limit is the remaining margin to the device's thermal limit, not an absolute
temperature.

## Public-method lane disclosure

The secondary llama-benchy lane recorded 240 measured requests and zero errors.
It requested `tg128` with `--exact-tg`, but client-observed completion counts
ranged from 125 through 128 tokens:

| Measure | Value |
|---|---:|
| Requests | 240 |
| Exactly 128 observed tokens | 179 |
| Other observed counts | 61 |
| Minimum | 125 |
| Maximum | 128 |
| Mean | 127.7 |

The complete sanitized numeric records are under [data](../data/README.md).
