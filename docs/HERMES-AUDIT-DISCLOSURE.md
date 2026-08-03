# Hermes audit privacy and disclosure boundary

Status: **planned; no finding or vulnerability is claimed**

Pinned source: `a6defd4f1549da3fe1d08d6f746fc645c64543f0`

This independently maintained experiment references the public
`NousResearch/hermes-agent` repository. It is not an official Nous Research
audit, collaboration, certification, or endorsement.

## Upstream policy governs security reporting

The pinned upstream
[security policy](https://github.com/NousResearch/hermes-agent/blob/a6defd4f1549da3fe1d08d6f746fc645c64543f0/SECURITY.md)
defines its trust model, in-scope boundaries, out-of-scope heuristics, and
private reporting channels. This project will follow that policy.

A model-generated candidate is not automatically a security issue. Before any
security label is applied, the candidate must identify the declared boundary,
state its preconditions, survive source verification, reproduce inside the
isolated executor, and pass human review.

Potential unpatched vulnerabilities are reported privately through the
upstream channels named in the security policy. They are not opened as public
issues, included in an X post, embedded in a graphic, or released as raw model
text.

## Public record

The public repository may include:

- pinned upstream commit and tree;
- deterministic source-inventory counts and hashes;
- frozen audit design, prompts, schemas, and validation rules;
- sanitized system and utility aggregates;
- complete candidate-disposition counts;
- positive- and negative-control outcomes;
- methodology corrections and failed-run disposition;
- hashes anchoring private evidence;
- sanitized live-wall media; and
- findings already fixed or explicitly cleared for disclosure.

Public counts must preserve failures, invalid evidence, duplicates,
non-reproductions, and human rejections. A filtered highlight reel cannot be
substituted for the complete outcome table.

## Private evidence

The private archive retains:

- raw prompts and model responses;
- per-request and per-workflow event ledgers;
- detailed runtime and operational records;
- source-unit payloads that exceed the public need;
- generated test and reproduction artifacts;
- unpatched candidate details;
- exploit sequences and sensitive failure paths;
- maintainer correspondence; and
- disclosure status and dates.

Private retention exists to support verification and coordinated disclosure.
It is not a reason to destroy inconvenient failures or publish sensitive data.

## Infrastructure privacy

The public topology is limited to eight DGX Spark systems arranged as four
anonymous TP=2 replicas. The public record may state that payload staging uses
the private LAN and that overlay networking is reserved for control/recovery.

It does not publish addresses, hostnames, usernames, ports, SSH configuration,
switch configuration, route tables, credentials, or per-host operational logs.
Transport, authentication, authorization, service health, and topology are
separate evidence classes.

## Isolated reproduction

The audit does not test candidates against live Hermes users, messaging
platforms, provider accounts, public services, or upstream infrastructure.

Reproduction is restricted to a disposable whole-process sandbox with:

- a read-only pinned source tree;
- a temporary writable overlay;
- no credentials;
- no operator-home mount;
- no outbound network;
- no access to model-serving hosts beyond the inference API contract; and
- bounded time, memory, CPU, and process counts.

The model-serving Spark systems do not execute upstream source or generated
tests.

## Control provenance

Positive-control defects exist only in isolated mutant copies. They are labeled
controls in every receipt and cannot be counted as upstream findings.

Negative controls remain part of the false-positive calculation. They are not
removed after model output.

The exact control mutations may remain private until the run is complete so
they cannot leak into blind model prompts. A sanitized control description and
hash may be published after validation.

## Finding publication states

| State | Public detail allowed |
|---|---|
| Model candidate | Aggregate count only |
| Evidence invalid | Aggregate count and rejection reason class |
| Reproduced pending review | Aggregate count only |
| Human rejected | Aggregate count and non-sensitive reason class |
| Embargoed security | No technical detail |
| Reported upstream | Disclosure status only when safe |
| Fixed and released | Reproducer/fix detail after upstream release and review |
| Non-security correctness finding | Detail after duplicate and maintainer-context review |

## Public-language guardrails

Allowed only after the corresponding evidence exists:

- “1,024 concurrent audit workflows completed”;
- “3,072 model calls completed”;
- “the full disposition table contained these counts”;
- “this many controls were detected or missed”; and
- “this many candidates were reproduced and human-confirmed.”

Disallowed without stronger evidence:

- “1,024 security agents found vulnerabilities”;
- “1,024 simultaneous models audited every line”;
- “Hermes is insecure”;
- “the audit proves the repository is secure”;
- “Nous Research approved this audit”; or
- any vulnerability count based only on model output.

## Current state

The source snapshot and audit plan are documented. The audit harness, canary,
1,024-workflow run, candidate validation, human review, and disclosure phases
remain planned. There are no findings to publish in this revision.
