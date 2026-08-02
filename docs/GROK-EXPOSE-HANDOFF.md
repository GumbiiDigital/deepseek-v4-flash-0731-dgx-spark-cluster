# Grok exposé handoff

This is the factual handoff for the public write-up. It is not finished social
copy. The voice can be energetic; the numbers and boundaries cannot move.

## The story

I loaded DeepSeek-V4-Flash-0731 across eight DGX Sparks as four independent
TP=2 replicas. Before tuning anything, I froze one clean profile so I would
have four matched starting points for the optimization work that follows.

The interesting result is not a one-off peak. It is how closely the four pairs
landed while running concurrently.

There is now a second story in the same repository: the original live tmux-wall
showcase plus a separate six-run replacement campaign. Lead with the
replication if the piece is about the timing result. Use the original wall only
as original-run visual evidence, not as replication footage.

## Replication facts that can be used

- Six fresh live campaigns in frozen order: 512, 1024, 1024, 512, 512, 1024.
- Experimental unit: one complete four-pair campaign; `n=3` per load.
- Each workflow made three serial model-backed calls: PLAN, BUILD, and CHECK.
- Total: 4,608 / 4,608 workflows and 13,824 / 13,824 model calls, zero failed
  workflows.
- Median of three run-level workflow medians: 373.914 seconds at 512 and
  742.378 seconds at 1,024; ratio 1.985424x.
- Median active span: 439.067 seconds at 512 and 877.937 seconds at 1,024;
  ratio 1.999551x.
- Median completion-token rate: 218.690 versus 219.247 tok/s; ratio 1.002549x.
- Run-level workflow-median ranges: 373.799–377.733 seconds and
  742.065–745.353 seconds.
- Maximum engine state: 16 running sequences; 496 waiting at 512 and 1,008
  waiting at 1,024.
- All six runs passed fleet, probe, lifecycle, identity, OOM, swap, memory, and
  thermal-slowdown gates.
- Twenty unique-marker findings are disclosed. They are not model-quality
  passes.
- One pre-work import failure and one collector-interrupted campaign are
  retained and excluded under the published rules.
- LAN carried control/receipts; each runner called its pair-head inference API
  through loopback.
- No confidence interval or universal scaling claim is reported.

## Original visual-run facts that can be used

- The original 1,024 run completed 1,024 / 1,024 workflows and 3,072 / 3,072
  calls with zero failed workflows.
- Every one of its 1,024 cells is visible in all 1,857 corrected source frames
  and all 300 selected edit frames.
- Fifteen incomplete tmux repaint frames were removed; no synthetic or replayed
  frames were added.
- The original wall is not footage of the six-run replacement campaign.

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

The repository hero uses official NVIDIA DGX Spark photography and the official
DeepSeek avatar; it contains no AI-generated hardware. The six-run comparison
also uses those official identity sources. Grok generated only its abstract
cyan whale/light background. That layer is decorative and contributes no
hardware, topology, label, or measurement.
