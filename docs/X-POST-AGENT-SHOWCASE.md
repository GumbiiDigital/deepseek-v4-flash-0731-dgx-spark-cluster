# X post: 1,024 live agent workflows

## Recommended post

Okay, this got ridiculous.

I pushed DeepSeek V4 Flash to 1,024 concurrent agent workflows across eight DGX Sparks—and put every agent on one live tmux wall.

1,024/1,024 finished. 3,072/3,072 model calls. 0 failed workflows.

Real inference. Synthetic tasks. Receipts below.

## Suggested follow-up thread

**Post 2**

The important distinction: this is 1,024 concurrent agent workflows, not 1,024 simultaneous decoding streams.

All 1,024 client requests were in flight. The four vLLM replicas decoded 16 model sequences at once and queued up to 1,008 requests.

**Post 3**

I ran the same harness at 512 first, then doubled it.

- event span: 463.975s → 893.526s
- median TTFT: 134.367s → 272.317s
- peak GPU temperature: 81 C → 83 C
- failed workflows: 0 → 0

The fixed 16-sequence ceiling stayed unchanged, so the queue and latency roughly doubled.

**Post 4**

I wanted to show the actual work, not animate a dashboard after the fact.

Every cell is one labeled workflow moving through PLAN → BUILD → CHECK → DONE. The final 60-second edit is built from the captured tmux pane buffers and keeps all 1,024 cells visible.

**Post 5**

The prompts were synthetic. The inference, queueing, model responses, telemetry, and completion receipts were real.

This is a concurrency/observability demo—not a speed record or an “1,024 simultaneous decodes” claim.

Method + sanitized evidence:
https://github.com/GumbiiDigital/deepseek-v4-flash-0731-dgx-spark-cluster

## Short version

1,024 DeepSeek V4 Flash agent workflows on eight DGX Sparks. One live tmux wall.

1,024/1,024 finished. 3,072/3,072 calls. 0 failed.

Real inference. Synthetic tasks.
https://github.com/GumbiiDigital/deepseek-v4-flash-0731-dgx-spark-cluster

## Claim guardrail

Use “1,024 concurrent agent workflows” or “1,024 client requests in flight.”
Do not say “1,024 simultaneous decoding streams.” The observed model-engine
high-water mark was 16 running sequences and 1,008 waiting requests.
