# Hermes audit verification contract

Status: **planned; no audit run has started**

Pinned source: `a6defd4f1549da3fe1d08d6f746fc645c64543f0`

This document defines how a future Hermes audit campaign becomes eligible for
analysis and publication. It does not record a pass.

## Truth labels

Every statement uses one of these labels:

| Label | Meaning |
|---|---|
| Observed | Directly inspected source or runtime state |
| Measured | Reproducible count, hash, duration, or rate |
| Automated pass | A named check completed on a named artifact |
| Human-reviewed | A person inspected the evidence and recorded a disposition |
| Planned | Not yet implemented or executed |
| Unknown | Available evidence is insufficient |

`Planned`, `unknown`, and `candidate` never become `passed` by implication.

## Frozen evidence objects

Before the first model request, the private run contract must record:

- upstream commit and tree;
- complete tracked-file manifest;
- source-unit manifest and every source-slice hash;
- unit-selection code and hash;
- prompt templates and hashes;
- response JSON schema and hash;
- validator source and hash;
- model revision and serving-image identity;
- four-replica assignment and common release epoch;
- live preflight and cooldown policy;
- stop rules; and
- public/private field allowlists.

The public source identity is already frozen at
`a6defd4f1549da3fe1d08d6f746fc645c64543f0`. The audit-unit and runtime
objects remain planned.

## Source-inventory verification

Clone the exact upstream commit, then run:

```bash
python3 scripts/inventory_hermes_snapshot.py \
  --repo /path/to/hermes-agent \
  --verify data/hermes-audit-plan.json
```

This recomputes tracked file/byte counts, text/binary counts, line counts,
extension counts, top-level counts, Python AST counts, test-file counts, and
key upstream document hashes. It does not execute Hermes source.

The plan itself is checked with:

```bash
python3 scripts/verify_hermes_audit_plan.py
```

## Whole-tree deterministic checks

The final tool list and versions must be frozen before execution. At minimum,
the evidence record must distinguish:

- upstream official tests and linters;
- dependency and lockfile checks;
- known-pattern static analysis;
- secret-pattern review;
- source-unit generation; and
- model-assisted semantic review.

One green class cannot substitute for another. A static-analysis pass does not
prove behavior. A model candidate does not prove a defect. A unit test does not
prove absence of a security issue.

For Python tests, the audit must use the upstream project's official wrapper
rather than calling the test runner directly. JavaScript checks must run in the
workspace that owns the changed or inspected surface.

## Workflow receipt requirements

Each of the 1,024 planned workflows requires:

- unique workflow and unit identifiers;
- unit-input SHA-256;
- three named stage-start and stage-finish records;
- expected model identity on every response;
- prompt and completion token counts when supplied by the server;
- response-body SHA-256;
- structured-output parse result;
- final workflow disposition; and
- closed live/request counters.

Raw response bodies remain private. Public summaries contain counts and hashes,
not generated text.

## Candidate evidence requirements

A `CANDIDATE` is automatically rejected from the confirmed set when any of the
following is missing or false:

- pinned source path exists;
- line range exists;
- quoted evidence matches the pinned bytes;
- claimed symbol or boundary exists;
- preconditions are stated;
- reachability is supported;
- upstream design intent was considered;
- the behavioral-test proposal is bounded; and
- the final stage attempted falsification.

Rejection is retained as data. It is not deleted to improve the apparent
success rate.

## Control interpretation

Positive controls are isolated modified copies with known seeded defects. They
are not changes to upstream source and never count as real findings.

Negative controls are slices designed to test unsupported finding generation.
Their false-positive outcomes remain in the denominator even when the prose
sounds plausible.

Control counts are descriptive. Thirty-two examples in each control class do
not establish a universal detection or false-positive rate.

## Live canary acceptance

The planned 64-workflow canary is accepted only when:

- 64 workflows start and finish;
- 192 model calls receive complete receipts;
- no workflow/request counters remain open;
- fewer than two final outputs violate the structured schema;
- all four replica APIs pass before and after probes;
- model and runtime identity remain fixed;
- no collector, OOM, restart, or thermal-slowdown gate fails; and
- raw/private artifacts remain outside the public tree.

A canary failure stops the launch. It is not merged into a replacement run.

## Full-campaign eligibility

The 1,024-workflow campaign becomes eligible for utility analysis only when:

- requested and completed workflows both equal 1,024;
- failed model transports equal zero or are explicitly retained as campaign
  failures under the frozen contract;
- expected and received model calls both equal 3,072;
- every unit ID is unique and belongs to the frozen manifest;
- the 960/32/32 real/positive/negative allocation is exact;
- every final response has a parse disposition;
- all counter, identity, collector, health, and functional gates pass; and
- no post-hoc unit replacement occurred.

Campaign completion is not candidate validation. Those are separate gates.

## Candidate dispositions

| Disposition | Meaning |
|---|---|
| `NO_FINDING` | Workflow did not support a candidate |
| `MODEL_CANDIDATE` | Model asserted a candidate; evidence not yet checked |
| `EVIDENCE_INVALID` | Path, line, quote, hash, or reachability gate failed |
| `DUPLICATE_OR_KNOWN` | Matches an existing issue, pull request, or prior fix |
| `NOT_REPRODUCED` | Bounded behavioral validation did not reproduce |
| `REPRODUCED_PENDING_REVIEW` | Isolated validation reproduced; human review pending |
| `HUMAN_CONFIRMED` | Human review accepted the evidence |
| `HUMAN_REJECTED` | Human review rejected or reclassified the candidate |
| `EMBARGOED_SECURITY` | Potential security issue retained privately for disclosure |
| `DISCLOSURE_CLEARED` | Safe to describe publicly under the recorded disclosure state |

Counts must be published for the complete disposition table, not only the
successful rows.

## Public reproducibility bundle

After a successful, disclosure-reviewed run, the candidate public bundle may
contain:

- frozen source and unit identities;
- sanitized run contract;
- run-level aggregate counters and distributions;
- control outcomes;
- candidate-disposition totals;
- fixed or disclosure-cleared finding summaries;
- deterministic graphics derived from validated aggregates; and
- hashes anchoring private receipts.

It must not contain unpatched vulnerability details, raw model text, operator
identity, private network data, live credentials, or secret-bearing logs.

## Current verification state

| Gate | State |
|---|---|
| Upstream repository resolved | Observed |
| Source commit and tree frozen | Observed |
| Public source inventory computed | Measured |
| Public plan structure verified | Planned until repository checks run |
| Audit-unit manifest | Planned |
| Audit harness implementation | Planned |
| Offline schema test | Not run |
| 64-workflow live canary | Not run |
| 1,024-workflow audit campaign | Not run |
| Candidate reproduction | Not run |
| Human finding review | Not run |
| Coordinated disclosure | Not applicable yet |

There are no audit results in this revision.
