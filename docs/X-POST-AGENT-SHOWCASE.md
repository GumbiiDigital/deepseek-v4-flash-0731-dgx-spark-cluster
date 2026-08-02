# X post: six-run DeepSeek V4 Flash agent-concurrency replication

## Recommended post

Okay, the first result looked too clean, so I did not believe it.

I froze six fresh DeepSeek V4 Flash campaigns across eight DGX Sparks:

512, 1024, 1024, 512, 512, 1024.

2x the workflows produced:

- 1.985424x median workflow time
- 1.999551x median active span
- 1.002549x completion-token rate

4,608/4,608 workflows. 13,824/13,824 live model calls. Zero failed workflows.

Method, failures, sanitized data, and recomputation code:
https://github.com/GumbiiDigital/deepseek-v4-flash-0731-dgx-spark-cluster

## Suggested follow-up thread

**Post 2**

The experimental unit is one complete four-pair campaign—not every agent
inside it. That gives n=3 per load.

Median workflow time across the three runs:

- 512: 373.914s (range 373.799–377.733)
- 1,024: 742.378s (range 742.065–745.353)

No confidence interval. No universal scaling claim.

**Post 3**

Why the result makes sense:

The four TP=2 engines stayed capped at 16 simultaneous model sequences.

At the application layer I had 512 or 1,024 client workflows in flight. The
engine queues reached 496 or 1,008 waiting requests.

Double the queued work behind the same saturated capacity; nearly double the
time; nearly flat token rate.

**Post 4**

The ugly parts are in the receipts too.

- one pre-work import failure before any model call;
- one later campaign stopped by the frozen collector gate and excluded as a
  whole—even its clean first run;
- 20 outputs in the final six runs missed the unique marker gate.

“Completed” means transport/orchestration completion, not perfect instruction
following or model quality.

**Post 5**

I used LAN control and pair-head loopback inference. Before the replacement
campaign, the fleet passed a 60-sample continuity soak. Every run then had to
pass two cooldown samples plus 8/8 health, identity, probe, queue, swap, OOM,
memory, and thermal gates.

No retries or exclusions inside the eligible six-run campaign.

**Post 6**

Important boundary: this is 1,024 concurrent client workflows—not 1,024
simultaneous decoding streams.

The observed engine high-water mark was 16 running and 1,008 waiting.

This is a descriptive replication under one fixed contract. It is not a speed
record, vendor benchmark, model-quality score, or universal hardware law.

**Post 7**

The old tmux wall shows the original live 1,024-workflow run. It is not footage
of the six replacement campaigns.

The new comparison graphic is built from the verified public JSON. Official
DGX Spark photography and the DeepSeek avatar identify the hardware/model; the
Grok whale/light background is decoration only.

Recompute it yourself:

```bash
python3 scripts/recompute_replication.py
python3 scripts/verify_public_bundle.py
```

## Short version

The first result looked too clean, so I ran six fresh campaigns.

DeepSeek V4 Flash on eight DGX Sparks:

2x workflows → 1.985424x median workflow time, 1.999551x active span, 1.002549x
completion-token rate.

4,608/4,608 workflows. 13,824/13,824 calls. Zero failed.

n=3 campaigns per load. Descriptive result, not a record claim.

https://github.com/GumbiiDigital/deepseek-v4-flash-0731-dgx-spark-cluster

## Claim guardrail

Use “1,024 concurrent client workflows” or “1,024 client requests in flight.”
Do not say “1,024 simultaneous decoding streams.” Do not turn six campaign
runs into thousands of independent replicates. Do not omit the 20 marker
findings or the two retained failed-attempt disclosures.
