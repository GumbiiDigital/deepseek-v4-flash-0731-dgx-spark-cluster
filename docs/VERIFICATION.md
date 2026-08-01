# Verification and evidence boundary

## Publicly verifiable

The public bundle permits a reader to verify:

- the 24 official numeric run records;
- 480 completed and zero failed official requests;
- exact official input/output token-length arrays;
- per-pair medians and coefficient of variation;
- four-pair repetition sums and aggregate medians;
- the explicit range-over-mean spread calculation;
- the public-method request-count and observed-token disclosure;
- all 20 stage-gate outcomes;
- aggregate telemetry and the retained idle exception;
- model, runtime, benchmark-client, and private-evidence hashes;
- every public file through the publication manifest.

Run:

```bash
python3 scripts/recompute_results.py
python3 scripts/verify_public_bundle.py
```

An additional publication-policy verifier can be run with:

```bash
python3 /path/to/verify_publication.py \
  --root . \
  --policy publication-policy.json \
  --pdf-tools off
```

## Integrity anchors

| Artifact | SHA-256 or count |
|---|---|
| Sealed private run manifest | `2efa0d711aed8e383dd58014ae30d45aa285201f9f1e103e8c374d12725df558` |
| Sealed private run entries | 331 |
| Full private model-source manifest | `1579d788beb7c9e759e717ade14e7c8a232d08a8db598f3a19dc2d0e3dcc43f2` |
| Full private model-source entries | 151 |
| Public model-file hash entries | 75 |
| Model weight shards | 48 |

The public [model-files manifest](../data/model-files.sha256) omits local cache
metadata entries while preserving hashes for the 75 checkpoint-directory files,
including all 48 weight shards.

## Not publicly proven by this bundle

- A bit-for-bit rebuild of the custom runtime image; its digest is recorded, but
  its build recipe and image are not distributed here.
- Packet-by-packet transport exclusion; route and socket evidence was retained
  privately, but no packet capture was retained.
- An exact reproduction of any external community table.
- A performance record or universal hardware expectation.

These are explicit limitations, not implied passes.

## Private archive retention

The sealed private archive remains unchanged. It contains the original commands,
logs, detailed telemetry, management-path evidence, generated outputs, and stage
receipts. Those materials are useful for a private audit but exceed the public
disclosure needed to recompute the benchmark.
