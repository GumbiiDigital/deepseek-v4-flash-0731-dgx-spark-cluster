# Methodology

## Claim boundary

This is the first frozen, pre-optimization deployment profile. It is a starting
measurement, not a record claim, an official vendor result, or evidence that
another runtime would produce the same numbers.

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
the result a different profile rather than another repetition of this starting
profile.

## Agent-concurrency replication campaign

The original 512- and 1,024-workflow tmux films are one-off visual showcase
runs. They are not the replication dataset. After the first comparison looked
unusually close to linear in elapsed time, I froze a separate six-run protocol
before collecting the replacement result.

The experimental unit is one complete campaign across all four TP=2 replicas.
Individual workflows inside a campaign share the same services, queues,
hardware, and time window, so I do not count them as independent replicates.
The fixed order was:

```text
512, 1024, 1024, 512, 512, 1024
```

That gives three experimental units at each load and counterbalances early,
middle, and late campaign position. Three units per load support a descriptive
replication, not a stable confidence interval or a universal scaling law. The
public record therefore reports run-level values, ranges, sample standard
deviations, and coefficients of variation, but no p-value or confidence
interval.

Each synthetic offline workflow made three serial expected-model requests:
`PLAN`, `BUILD`, and `CHECK`. All workflows were launched asynchronously. The
application-side high-water mark and the model-engine running/waiting
high-water marks are reported separately.

The primary endpoint is workflow duration, measured from that workflow's
`agent_started` epoch to its `agent_completed` epoch. The group headline is the
median of the three run-level workflow medians. Secondary endpoints include:

- active span from the earliest `PLAN` request start to the last workflow
  completion;
- completed model requests per active second;
- completion tokens per active second;
- TTFT and end-to-end distributions;
- anonymous pair distributions;
- queue high-water marks, token totals, memory, temperature, and safety state.

Control and receipt collection used the local LAN. Each runner executed on its
pair head and called the inference API through that pair head's loopback
interface. Tailscale was not the workload-data path, and management-path
latency was not included in inference timing.

Before the replacement campaign, the collector had to pass 60 consecutive
8-of-8 LAN samples at five-second spacing. Any failed sample reset the
consecutive count. Before every measured run, two consecutive samples 15
seconds apart had to show all eight systems healthy, four pair-head APIs,
exactly one compute application per system, zero engine work, no swap, no OOM
or thermal-slowdown state, no probe error, at most 60 C, and at least 5.8%
available memory.

The frozen stop gate aborted a campaign on any collector/probe failure,
runtime-identity change, OOM, restart, thermal-slowdown flag, missing receipt,
or workflow/request failure. There were no retries or post-hoc exclusions
inside an eligible campaign.

Two prior attempts are retained and disclosed:

1. A pre-work harness attempt failed on a Python import before any workload run
   or model request began. It is not an experimental unit.
2. A later campaign completed one 512 run, then a live collector SSH probe
   failed during its second run. The frozen gate stopped all runners. That
   entire campaign, including its clean first run, is excluded from the
   replacement analysis.

The replacement campaign used a new immutable campaign identifier, LAN
control, the continuity soak above, and the same model/workload contract. The
sanitized public JSON includes hashes that bind its aggregates to retained
private receipts without publishing operational identity or generated text.

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
