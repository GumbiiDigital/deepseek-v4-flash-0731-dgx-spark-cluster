# Watching 1,024 agent workflows hit DeepSeek V4 Flash at once

I wanted something more honest than a dashboard animation. I wanted to see the
work happen.

I started with 512 distinct agent workflows against the four DeepSeek V4 Flash
replicas already running across my eight DGX Sparks. Then I doubled it to
1,024. Every workflow had three model-backed stages: `PLAN`, `BUILD`, and
`CHECK`. I put every labeled agent cell on one tmux wall and captured the real
pane buffers while both runs were in flight.

![All 1,024 labeled workflows visible during live inference](../media/agent-showcase/1024-agent-live-wall.jpg)

## The 1,024-workflow run

| Measured result | Value |
|---|---:|
| Agent workflows requested | 1,024 |
| Agent workflows completed | 1,024 |
| Failed workflows | 0 |
| Live model requests completed | 3,072 / 3,072 |
| Maximum live workflows | 1,024 |
| Maximum client requests in flight | 1,024 |
| Maximum model sequences running | 16 |
| Maximum requests waiting in the model queues | 1,008 |
| Event-ledger span | 893.526 seconds |
| Peak GPU temperature | 83 C |
| Thermal-gate failures | 0 / 186 samples |

All 1,024 workflows reached `DONE`. The harness issued all 1,024 first-stage
requests before the engines completed the wave, and the observed client-side
high-water mark reached 1,024 requests in flight.

The queue is the important distinction. The four deployed TP=2 replicas were
configured for four model sequences each, so 16 sequences could decode at
once. The other requests waited inside the model queues. This is 1,024
concurrent agent workflows, not 1,024 simultaneous decoding streams.

## What changed when I doubled it

| Measured result | 512 workflows | 1,024 workflows | Change |
|---|---:|---:|---:|
| Completed workflows | 512 / 512 | 1,024 / 1,024 | 2.00x |
| Completed model requests | 1,536 / 1,536 | 3,072 / 3,072 | 2.00x |
| Max client requests in flight | 512 | 1,024 | 2.00x |
| Max model sequences running | 16 | 16 | unchanged |
| Max model requests waiting | 496 | 1,008 | 2.03x |
| Event-ledger span | 463.975 s | 893.526 s | 1.93x |
| Median TTFT | 134.367 s | 272.317 s | 2.03x |
| Median end-to-end time | 137.940 s | 275.761 s | 2.00x |
| Peak GPU temperature | 81 C | 83 C | +2 C |
| Failed workflows | 0 | 0 | unchanged |

That is what I expected from a saturated fixed-capacity serving profile. The
harness and APIs accepted twice the concurrent application load, but the model
sequence ceiling stayed at 16. Queue depth roughly doubled, median latency
roughly doubled, and the total campaign took 1.93x as long. This is not a
throughput-scaling claim; it is one bounded concurrency and observability run.

## What the wall shows

The five-pane tmux layout contains one cluster overview and four pair panes.
Each pair pane contains 256 individually labeled cells:

- `A001` through `A256`
- `B001` through `B256`
- `C001` through `C256`
- `D001` through `D256`

Cell state changes are driven by the live event ledger:

- `P` — PLAN
- `B` — BUILD
- `C` — CHECK
- `✓` — DONE
- `!` — ERROR
- `·` — waiting to start

The corrected 1,024-agent capture contains 1,857 original live frames. An
automated visibility check found all 1,024 unique labeled cells in every
retained frame. A separate 300-frame edit was validated the same way before
the 60-second social cut was encoded.

Fifteen of the 1,872 raw frames caught tmux between a clear and repaint
operation and did not contain the complete cell set. I excluded those 15
frames. No synthetic or replayed frames were added. A contact-sheet review then
caught five browser screenshots taken before paint completed; I re-rendered
those exact edit frames with a paint-readiness gate before encoding the final
movie.

![All 1,024 workflows in the completed state](../media/agent-showcase/1024-agent-live-wall-final.jpg)

## The first 512-workflow run

The first fresh live run also completed cleanly:

| Measured result | Value |
|---|---:|
| Agent workflows completed | 512 / 512 |
| Failed workflows | 0 |
| Live model requests completed | 1,536 / 1,536 |
| Maximum client requests in flight | 512 |
| Maximum model sequences running | 16 |
| Maximum model requests waiting | 496 |
| Event-ledger span | 463.975 seconds |

That wall used 128 labeled cells per pair. All 512 labels were present in each
of the 665 corrected source frames and each of the 300 selected edit frames.

![All 512 labeled workflows visible during live inference](../media/agent-showcase/512-agent-live-wall.jpg)

## Verification boundary

Both campaigns were fresh live inference runs, not replays of sealed receipts.
Each capture is hash-bound to its run contract, summary, event ledger, and
before/after runtime-identity receipts.

The prompts were synthetic offline tasks. The inference, queueing, model
responses, concurrency, telemetry, and completion receipts were real.

The 1,024-workflow run recorded four PLAN marker-format mismatches. The
512-workflow run recorded three. All seven responses were HTTP 200, came from
the expected model, contained nonempty uniquely hashed output, and passed the
semantic receipt check. The recorded campaign contract reports marker
formatting as a note rather than a failed workflow.

The sanitized numeric records are in
[`agent-showcase-512.json`](../data/agent-showcase-512.json) and
[`agent-showcase-1024.json`](../data/agent-showcase-1024.json).

## What this does not claim

This is a concurrency and observability demonstration. It is not a speed
record, a quality evaluation, an agent intelligence score, or a claim that
1,024 model sequences decoded simultaneously.

The frozen performance profile elsewhere in this repository uses a different
request contract and remains the comparable throughput reference. I am not
mixing those numbers with this showcase.

## Media integrity

The 1,024-agent X-ready movie is a 60-second, 1920x1080 H.264 edit,
time-compressed 16.412x from the 935.504-second corrected tmux capture. It is
silent by design and is distributed separately from the Git repository.

- Movie SHA-256: `88cf11bc750cdba38a544b402bbae93b6625a6bc36b4f537b637b6b4a94e7faf`
- Corrected source-film SHA-256: `7d3a7414deef74953d35ad28289552981353559cc275f82cf1c44e87fcd4a802`
- 300-frame contact-sheet SHA-256: `6575592393000569d13cbee89ceba3a974bae7b74318f001d6748fb9d384e17f`

The dense contact sheet is retained as a publication QA artifact:
[1,024-agent contact sheet](../media/agent-showcase/1024-agent-contact-sheet.jpg).

For the 512-agent edit:

- Movie SHA-256: `1b3157e4d05bd3fe4b08c66a892d4dbe52c21cd6689cc4587b67c748df0b21d7`
- Corrected source-film SHA-256: `369d0374f3e3ec577af8cff6c7a0552d20523130d2df64d8cd33a54d4fe22806`
- 300-frame contact-sheet SHA-256: `5bc01bb1b0e2cb9bbbdd9969bbfad256abd111b7463d526454893a7954376726`

The raw operational captures remain private because they include live model
output and infrastructure receipts beyond the public disclosure boundary.
