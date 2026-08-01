# Methodology

## Claim boundary

This is the first frozen, pre-optimization deployment profile. It is the
project baseline, not a record claim, an official vendor result, or evidence
that another runtime would produce the same numbers.

## Frozen identity

- Model: `deepseek-ai/DeepSeek-V4-Flash-0731`
- Revision: `9e165c30e2704aec5d9d593cce3eebd58bbef1cb`
- Hardware: eight NVIDIA DGX Spark systems
- Topology: four independent replicas, each using tensor parallelism `2`
- Expert parallelism: enabled
- KV cache: FP8
- Context limit: 65,536 tokens
- Maximum sequences: 4
- Maximum batched tokens: 8,192
- Prefix caching: enabled in the service
- Execution: eager
- Speculative decoding: DSpark with seven greedy proposal tokens

The exact custom image digest and software versions are retained in
[run-identity.json](../data/run-identity.json). Changing any runtime field makes
the result a different profile rather than another repetition of this baseline.

## Lane A: primary official-vLLM measurement

The primary lane used the deployed build's `vllm bench serve` interface:

| Parameter | Value |
|---|---|
| Backend | `openai-chat` |
| Dataset | synthetic random prompts |
| Server-observed input length | exactly 2,048 tokens |
| Output length | exactly 128 tokens, EOS ignored |
| Concurrency | 1 and 4 |
| Measured requests | 20 per run |
| Excluded warmups | 4 per run |
| Independent repetitions | 3 |
| Seeds at c1 | 6201, 6202, 6203 |
| Seeds at c4 | 6401, 6402, 6403 |
| Request rate | unbounded, limited by maximum concurrency |
| Sampling | temperature 0 |

Every repetition used a disjoint seed. The same seed was used across anonymous
pairs within a repetition so that pair comparison retained matched prompts.
Each condition ran across all four pairs concurrently. Condition ordering was
alternated across repetitions to reduce time-order bias.

The benchmark client was co-located with each pair head and addressed the
service through loopback. Management-path latency therefore was not part of the
primary throughput measurements.

## Lane B: public-method comparison

The secondary lane used `eugr/llama-benchy` pinned to commit
`e9be344578cec17745066b220798b80a0d2686d3`:

| Parameter | Value |
|---|---|
| Prompt processing | `pp2048` |
| Requested generation | `tg128` with `--exact-tg` |
| Context depths | 0, 4,096, 16,384, 32,768 |
| Concurrency | 1 and 4 |
| Measured runs | 3 |
| Excluded warmups | 1 |
| Cache request | `--no-cache` |
| Latency mode | API |

Important disclosure: although `tg128` was requested with the exact-generation
flag, the client observed 125–128 completion tokens, with a mean of 127.7.
llama-benchy calculated generation throughput from observed token timestamps.
The lane remains useful, but it must be described as “requested tg128,” not as
240 responses that were all exactly 128 tokens.

The four public-method sweeps ran concurrently through four route-equivalent
private paths. The retained evidence supports “configured and observed private
paths”; no packet capture was retained, so the publication does not claim
packet-by-packet proof.

## Integrity monitoring

A five-second collector monitored all eight devices. Stage gates required fresh
and advancing samples, full device health, zero swap, no OOM state, stable
container lifecycle identity, more than five percent available memory, more
than 5 C GPU T.Limit margin, and inactive software/hardware thermal-slowdown
flags.

All measured official and public request windows passed. One retained sample in
an inter-condition idle cooldown reached exactly 5 C T.Limit margin and reduced
the full-campaign healthy count to seven for that sample. It did not overlap a
measured request and is disclosed rather than discarded.

## Metric definitions

- `output tok/s`: aggregate generated-token throughput reported by the selected client.
- `TPOT`: time per output token reported by vLLM.
- Pair result: median of three independent run values.
- Four-pair aggregate: median of the three repetition-wise sums.
- Pair spread: `(maximum pair median - minimum pair median) / mean pair median`.

Metrics from the two client implementations have different definitions and are
never merged into a single aggregate.
