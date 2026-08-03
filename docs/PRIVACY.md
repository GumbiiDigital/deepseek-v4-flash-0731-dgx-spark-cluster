# Privacy review

The public bundle was generated from an allowlist, not by copying the private
run and trying to redact it afterward.

## Kept private

- usernames and account paths;
- local filesystem locations;
- machine names and per-host lifecycle records;
- private and overlay network addresses;
- ports, routes, forwarding details, and SSH configuration;
- command transcripts and operational logs;
- full generated model responses and raw streamed-text files;
- request identifiers;
- per-host telemetry and infrastructure topology.

The source audit found 95 private-run files with operator-path or key-location
references, 125 files with internal address literals, 24 result files containing
generated text, and four progress files containing streamed snippets. A
high-confidence secret-shape scan found no credential values, but the source was
still treated as private.

## Published instead

- anonymous pair labels A–D;
- numeric measurements and token-length arrays;
- aggregate health and telemetry facts;
- exact upstream revisions and non-personal content hashes;
- an integrity hash for the sealed private archive;
- deterministic scripts that recompute and verify the claims;
- sanitized agent-run summaries and hashes;
- run-level and group-level replication statistics with anonymous pair labels;
- live-wall stills with anonymous pair/cell labels and bounded output snippets
  from the synthetic offline showcase corpus.

The publication verifier rejects user-home paths, private address ranges,
per-host labels, SSH material, common credential shapes, generated-text fields,
and symbolic links.

The repository hero is a deterministic browser composition using an official
NVIDIA product-photo crop and the official DeepSeek avatar. It contains no live
labels, addresses, host identities, account details, or operational topology.

The agent-wall stills are real terminal captures. They were reviewed for
personal and infrastructure details before publication. The visible task
content is limited to bounded snippets produced from the synthetic offline
showcase corpus; full responses, prompts, event ledgers, raw films, host data,
and network data remain private.

The six-run replication record is built from an explicit allowlist. It omits
campaign identifiers, run identifiers, aliases, hostnames, commands, private
addresses, paths, raw event ledgers, generated text, and per-host samples. It
publishes anonymous run labels, aggregate timing/token/queue/safety values,
normalized runtime-identity hashes, and receipt hashes. Those hashes bind the
public arithmetic to retained private receipts; they do not make the private
receipts public.

The planned Hermes audit record follows the same allowlist rule. The public
pre-run dossier contains the upstream repository identity, pinned commit and
tree, deterministic inventory counts, document hashes, workflow allocation,
controls, validation ladder, and disclosure rules. It contains no audit model
output, candidate detail, exploit sequence, private source-unit payload,
operational endpoint, or result.

If the audit runs, raw prompts, responses, event ledgers, detailed runtime
records, generated tests, and unpatched security candidates remain private.
Only sanitized aggregate counts, evidence hashes, control outcomes, and fixed
or disclosure-cleared findings are eligible for publication.
