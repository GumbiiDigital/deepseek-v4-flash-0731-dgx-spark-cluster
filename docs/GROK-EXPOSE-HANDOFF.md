# Grok exposé handoff

This is the factual handoff for the public write-up. It is not finished social
copy. The voice can be energetic; the numbers and boundaries cannot move.

## The story

I loaded DeepSeek-V4-Flash-0731 across eight DGX Sparks as four independent
TP=2 replicas. Before tuning anything, I froze one clean profile so I would
have four matched starting points for the optimization work that follows.

The interesting result is not a one-off peak. It is how closely the four pairs
landed while running concurrently.

There is now a second story in the same repository: fresh live 512- and
1,024-workflow concurrency runs with every labeled workflow visible on a tmux
wall. Lead with the 1,024 run if the piece is about the visual showcase.

## Agent showcase facts that can be used

- Fresh live 1,024-workflow run: 1,024 / 1,024 workflows completed, zero failed.
- Each workflow made three model-backed calls: PLAN, BUILD, and CHECK.
- Requests completed: 3,072 / 3,072.
- Maximum client requests in flight: 1,024.
- Maximum model sequences running across the four replicas: 16.
- Maximum model requests waiting: 1,008.
- Event-ledger span: 893.526 seconds.
- Median TTFT: 272.317 seconds; median end-to-end time: 275.761 seconds.
- Peak GPU temperature: 83 C; zero thermal-gate failures in 186 samples.
- Fresh live 512-workflow comparison: 512 / 512 workflows, 1,536 / 1,536
  requests, zero failed, 463.975-second event span, 134.367-second median TTFT,
  and 81 C peak GPU temperature.
- Every one of the 1,024 cells is visible in all 1,857 corrected source frames
  and all 300 selected edit frames.
- Fifteen incomplete tmux repaint frames were removed from the raw capture; no
  synthetic or replayed frames were added.
- The task corpus was synthetic and offline. The inference, queueing, outputs,
  telemetry, and receipts were live.

## Facts that can be used

- Hardware: eight NVIDIA DGX Spark systems.
- Topology: four independent two-Spark replicas with tensor parallelism `2`.
- Primary client: the deployed vLLM build's official `vllm bench serve`
  interface.
- Request shape: exactly 2,048 input tokens and 128 output tokens.
- Repetitions: three, with different seeds.
- Per repetition: four excluded warmups and 20 measured requests per pair and
  concurrency condition.
- Per-pair median throughput: 20.8370-21.2443 output tok/s at c1 and
  39.0501-39.5904 output tok/s at c4.
- Four-pair aggregate median: 84.4107 output tok/s at c1 and 158.2688 output
  tok/s at c4.
- Pair spread: 1.9337% at c1 and 1.3715% at c4, calculated as range divided by
  mean pair median.
- Completion: 480/480 official measured requests, with zero failures.
- Maximum recorded pair-start skew: three seconds.

## Framing that fits the project

- This is the first frozen, pre-optimization profile.
- The repository will follow the deployment and every optimization that earns
  a new measured profile.
- Four balanced pairs make pair-by-pair experimentation useful.
- The public evidence includes sanitized numeric runs, exact revisions,
  hashes, recomputation code, telemetry gates, and explicit limitations.

## Boundaries that must stay intact

- Do not call this a record, world record, fastest result, or official vendor
  result.
- Do not merge the official vLLM lane and the `llama-benchy` lane into one
  number.
- Do not attribute the community comparison delta to the 0731 weights alone.
- Do not say all public-method responses produced exactly 128 observed tokens;
  that lane observed 125-128 with a mean of 127.7.
- Do not claim packet-capture proof or a publicly reproducible custom image.
- Do not publish hostnames, addresses, ports, account paths, generated model
  text, raw logs, or live topology.
- Do not translate “1,024 concurrent agent workflows” into “1,024 simultaneous
  decoding streams.” The measured engine high-water mark was 16 running and
  1,008 waiting.
- Do not call the showcase a record, intelligence evaluation, or general
  benchmark.

The conceptual repository graphic is artwork generated with Grok Imagine. It
is not evidence of the physical cluster or its wiring.
