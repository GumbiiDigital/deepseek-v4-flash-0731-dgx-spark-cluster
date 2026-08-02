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
- deterministic scripts that recompute and verify the claims.
- sanitized agent-run summaries and hashes;
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
