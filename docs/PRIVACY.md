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
- generated model responses and streamed text snippets;
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

The publication verifier rejects user-home paths, private address ranges,
per-host labels, SSH material, common credential shapes, generated-text fields,
and symbolic links.

The repository hero image is conceptual artwork generated through Grok
Imagine. It was reviewed as an image asset, not exported from an account screen
or captured from the physical environment. It contains no live labels,
addresses, host identities, account details, or operational topology.
