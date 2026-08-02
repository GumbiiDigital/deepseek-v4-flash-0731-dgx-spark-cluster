# Agent-showcase media

This directory contains two kinds of media: still-image evidence and
contact-sheet QA artifacts from the original live showcase runs, plus one
data-derived comparison graphic for the separate six-run replication.

| Asset | Purpose | SHA-256 |
|---|---|---|
| `512-agent-live-wall.jpg` | 512 labeled workflows during live inference | `da7172cc7e268f5363bbdd0db15622e287288e256fdcbda3622ba42326722049` |
| `512-agent-live-wall-final.jpg` | 512 workflows completed | `7d1c2bf4dc991c85b36e9eb9edf0efac5b8584c681e5ae44445968a86ab0034f` |
| `512-agent-contact-sheet.jpg` | 300-frame publication QA sheet | `5bc01bb1b0e2cb9bbbdd9969bbfad256abd111b7463d526454893a7954376726` |
| `1024-agent-live-wall.jpg` | 1,024 labeled workflows during live inference | `b7e73dd01a00e423200da39a48c63460506e070dc5f18746e8a90018d6c5f6b5` |
| `1024-agent-live-wall-final.jpg` | 1,024 workflows completed | `71f72e884087de3c3090573382b8cef67f563b19feb52da7ae14e50ce77673a3` |
| `1024-agent-contact-sheet.jpg` | 300-frame publication QA sheet | `6575592393000569d13cbee89ceba3a974bae7b74318f001d6748fb9d384e17f` |
| `replicated-512-vs-1024.jpg` | Deterministic 1,600 x 900 comparison built from the verified six-run public JSON | `223066e5e352a026660b331e4a75fa3f8b019ef319f8de66bce29b07d9bec93f` |

The pair numbers are anonymous presentation labels. The images contain no
address, port, account path, credential, physical-location detail, or actual
host identity. Visible task content comes only from the synthetic offline
showcase corpus.

The MP4 files are distributed separately from this repository. Their hashes
and media properties are recorded in the corresponding sanitized JSON files.

## Replication-graphic provenance

`replicated-512-vs-1024.jpg` is not a terminal capture and is not footage of
the six replacement campaigns. Its numerical text was rendered
deterministically from `data/agent-showcase-replication.json` only after the
public recomputation passed.

The hardware tiles use the same official NVIDIA DGX Spark photograph crop
documented in [the repository media record](../README.md), repeated eight times
as four visual TP=2 pairs. The DeepSeek tile uses the official organization
avatar. A Grok-generated abstract light/whale image is used at reduced opacity
as background decoration only; it supplies no hardware, logo, topology, text,
or numeric value.

Source hashes:

- public replication JSON: `3638909684ef42a82335156a566f283665440ff5865d25b2494338562ebb99e1`;
- official Spark crop: `d760612ec01a0d9b9cd8d438e195f492428ad9c02ae8dd65c8f421a6c40e41bc`;
- official DeepSeek avatar: `55e6e0c1ba0c453749211368b8a26e00f470b4ab696ce1fed539d70777d4aab1`;
- accepted Grok decorative background: `8525ec39f79b2b040f02e36424240c2c014b6c549903494750a6cbb9939f0ee6`;
- deterministic SVG before browser rasterization: `194e2d358c2fd778cc467ff58b1d61c7f9889283ddc81562b5787b1c6b5699aa`.

The final JPEG was captured from the reviewed SVG at exactly 1,600 x 900. A
Quick Look raster was rejected because it padded and clipped the layout; its
bytes were not published.
