# Hermes Agent 1,024-workflow audit plan

Status: **planned and frozen before the first audit request**

Results: **none collected**

Upstream: [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent)

Pinned commit: [`a6defd4f1549da3fe1d08d6f746fc645c64543f0`](https://github.com/NousResearch/hermes-agent/commit/a6defd4f1549da3fe1d08d6f746fc645c64543f0)

This is the pre-run contract for turning the earlier synthetic concurrency
showcase into bounded, useful repository work. It records the source, scope,
workflow allocation, validation ladder, controls, stop conditions, and
publication boundary before any audit output exists.

It is not an audit report, vulnerability claim, security certification, or
statement of upstream endorsement.

## Why Hermes Agent

Hermes is a meaningful target because it combines a broad application surface
with explicit engineering invariants. Its public tree includes the core agent
loop, model and tool routing, terminal backends, gateways, plugins, model
providers, memory, scheduled jobs, multi-agent delegation, an Electron desktop
application, a TUI, web surfaces, and editor integration.

The upstream project also publishes detailed
[development rules](https://github.com/NousResearch/hermes-agent/blob/a6defd4f1549da3fe1d08d6f746fc645c64543f0/AGENTS.md),
[architecture documentation](https://github.com/NousResearch/hermes-agent/blob/a6defd4f1549da3fe1d08d6f746fc645c64543f0/website/docs/developer-guide/architecture.md),
and a precise
[security policy](https://github.com/NousResearch/hermes-agent/blob/a6defd4f1549da3fe1d08d6f746fc645c64543f0/SECURITY.md).
Those upstream statements become part of the audit evidence contract rather
than being replaced by generic model judgment.

## Frozen source snapshot

The public inventory was computed from the pinned Git tree, not a search-engine
summary or a moving branch head.

| Field | Frozen value |
|---|---:|
| Commit | `a6defd4f1549da3fe1d08d6f746fc645c64543f0` |
| Tree | `d056cf8ee585f28a5e90085ab6fb31b73f31c834` |
| Tracked files | 8,345 |
| Tracked bytes | 138,840,634 |
| Text files | 8,248 |
| Text lines | 2,554,893 |
| Binary files | 97 |
| Python files | 3,787 |
| Runtime Python files | 955 |
| Runtime Python function definitions | 21,059 |
| Runtime Python classes | 1,127 |
| Python test files | 2,685 |
| Python test functions | 22,823 |
| TypeScript test/spec files | 632 |
| Python parse errors during inventory | 0 |

The complete extension and top-level-directory counts, key upstream document
hashes, and audit contract are in
[`data/hermes-audit-plan.json`](../data/hermes-audit-plan.json). The inventory
can be independently recomputed with
[`scripts/inventory_hermes_snapshot.py`](../scripts/inventory_hermes_snapshot.py).

## What the 1,024 workflows mean

One workflow is an isolated, client-side state machine with a unique audit
unit, input hash, three serial model requests, and a final receipt. It is not an
independent model process, container, operating-system user, or simultaneous
decoding stream.

The planned run contains 1,024 workflows and 3,072 expected model calls:

1. `PLAN_TRACE`: identify the governing invariant and trace the relevant path.
2. `BUILD_ATTACK`: construct a concrete failure sequence or explain why the
   evidence does not support one.
3. `CHECK_FALSIFY`: attempt to disprove the candidate and emit strict JSON.

The previous cluster run observed no more than 16 decoding sequences at once.
That number is retained as a configuration reference, not assumed current.
A fresh live preflight is mandatory before launch.

## Complete-machine coverage plus bounded semantic review

The repository is too large for 1,024 model workflows to justify an exhaustive
human-equivalent review claim. The experiment therefore separates two kinds of
coverage:

- deterministic scanners and official project checks cover the complete pinned
  public tree; and
- 1,024 model workflows perform deep semantic review of a frozen,
  risk-stratified set of units.

The semantic units are selected before model output. Selection uses named risk
lanes, immutable source slices, call context, and SHA-256 ordering for ties.
Open issues, pull requests, and prior findings stay outside the model input
during the blind pass. They are compared only after candidates exist.

## Frozen workflow allocation

| Lane | Workflows |
|---|---:|
| Core agent, model routing, and tool execution | 192 |
| Gateways, authorization, sessions, and external surfaces | 160 |
| Configuration, credentials, profiles, memory, and isolation | 128 |
| Plugins, providers, MCP, discovery, and dependencies | 128 |
| Cron, kanban, delegation, and background durability | 96 |
| Desktop, TUI, web, ACP, IPC, and state reconciliation | 160 |
| Tests, CI, installers, updates, and supply chain | 96 |
| Seeded positive controls in isolated mutant copies | 32 |
| Negative controls | 32 |
| **Total** | **1,024** |

The 960 real units test useful repository work. The 32 positive controls measure
whether the method can detect known, privately seeded defects without altering
the pinned upstream tree. The 32 negative controls measure unsupported finding
generation. Controls are reported separately from real-source candidates.

## Per-workflow input contract

Every workflow receives only the material necessary for its unit:

- exact repository commit and tree;
- immutable source slice plus bounded adjacent caller/callee context;
- applicable upstream engineering and security invariants;
- file, line, and content hashes;
- lane and unit identifiers; and
- a unique response receipt.

It receives no credentials, private infrastructure details, live-account data,
upstream issue answers, or authority to browse, message, publish, or mutate a
repository.

## Per-workflow output contract

Every final response must parse against a versioned JSON schema and contain:

- `NO_FINDING` or `CANDIDATE`;
- exact path and line evidence when a candidate is asserted;
- the claimed invariant and trust boundary;
- preconditions and reachability path;
- a bounded behavioral-test proposal;
- an attempted falsification; and
- uncertainty.

Malformed output is retained as a failure record. It is not repaired silently
or counted as a successful audit finding.

## A model candidate is not a finding

The required evidence ladder is:

```text
model candidate
  -> schema valid
  -> source path and line valid
  -> quoted evidence hash valid
  -> claimed path reachable
  -> upstream intent checked
  -> isolated reproducer or behavioral test
  -> duplicate and existing-issue comparison
  -> human review
  -> confirmed finding or rejection
```

Severity and vulnerability language are withheld until the relevant evidence
and human-review gates pass. A high-confidence model score cannot bypass the
ladder.

## Execution architecture

The planned public topology statement is deliberately anonymous:

- eight NVIDIA DGX Spark systems;
- four independent tensor-parallel replicas;
- two Spark systems per replica;
- model requests issued through each replica's local serving endpoint;
- private LAN preferred for staging and receipts; and
- overlay networking limited to control and recovery.

The source repository and generated tests do not execute on the model-serving
nodes. Any reproducer runs in a disposable whole-process sandbox with read-only
source, no secrets, no operator-home mount, no outbound network, and bounded
CPU, memory, process, and time limits.

This topology is **previously measured/configured context**, not a current
health claim. Current transport, authorization, service identity, temperature,
memory, queue, and restart state must pass a fresh read-only preflight before a
live run.

## Staged launch

### Stage 0: contract freeze

- Freeze the pinned source, inventory, unit generator, prompts, schemas,
  validators, model revision, serving identity, and source hashes.
- Record every exclusion before model output.
- Accept when the public plan verifier and private source/unit manifests agree.

### Stage 1: offline schema test

- Run 16 workflows without issuing model requests.
- Exercise unit loading, receipts, schema enforcement, event accounting, and
  sanitization.
- Accept when every expected artifact exists and all counters close at zero.

### Stage 2: live canary

- Run 64 workflows, balanced as 16 per replica.
- Expect 192 model calls.
- Stop if two or more final outputs violate the structured-output contract.
- Stop immediately on service-identity drift, collector failure, OOM, restart,
  thermal slowdown, or failed functional probe.
- Accept when all model calls and workflow receipts exist and the safety gates
  remain green.

### Stage 3: 1,024-workflow campaign

- Launch only after reviewing the live canary.
- Keep the unit set and ordering frozen.
- Retain failures; do not replace or exclude them after seeing results.
- Accept the campaign only when all infrastructure, request, counter, receipt,
  and validation-accounting gates close cleanly.

### Stage 4: candidate validation

- Validate evidence mechanically.
- Run bounded reproductions only in the isolated executor.
- Compare surviving candidates with upstream issues and pull requests.
- Deduplicate before human review.
- Keep unpatched security candidates private.

## Metrics that matter

The practical result is not the largest number of green cells. Primary utility
metrics are:

- structured-output validity;
- evidence-valid candidate rate;
- reproduction rate;
- negative-control false-positive rate;
- positive-control detection rate;
- duplicate rate;
- unique human-confirmed findings; and
- verified useful findings per active hour.

System metrics remain important but secondary: workflow completion, model-call
completion, prompt/completion tokens, latency, request rate, completion-token
rate, queue depth, temperature, memory, OOM, restart, collector, and functional
probe outcomes.

## Timing boundary

The earlier synthetic 1,024-workflow result does not predict this audit's
duration. Audit prompts and outputs are materially larger. No audit runtime is
claimed until the 64-workflow live canary measures actual prompt length,
prefill behavior, output length, and completion rate.

## Planned 2,048-workflow follow-up

If the 1,024-workflow campaign and validation pipeline are sound, the next
planned experiment assigns two independent workflows to each of the same 1,024
units:

- one correctness/invariant reviewer; and
- one adversarial/trust-boundary reviewer.

They work independently. Agreement, disagreement, incremental validated yield,
and control performance are measured after completion. The purpose is to test
whether additional workflow capacity improves evidence quality, not to imply
twice the model throughput.

## Claim limits

Even a clean campaign will not establish:

- comprehensive coverage of every possible defect;
- security certification;
- 1,024 simultaneous decoding sequences;
- that every model candidate is a vulnerability;
- upstream approval or endorsement; or
- a universal audit-performance law.

The machine-readable contract is authoritative if a summary sentence and the
contract ever disagree.
