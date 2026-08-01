# Graphic provenance

## Published asset

| Field | Value |
|---|---|
| Path | `media/deepseek-v4-flash-0731-dgx-spark-cluster-hero.jpg` |
| Generator | Grok image generation through the Grok chat interface |
| Attribution | [Created with Grok](https://x.ai/legal/brand-guidelines) |
| Generated | 2026-08-01 UTC |
| Dimensions | 1,248 x 832 pixels |
| Format | JPEG, sRGB |
| File size | 237,300 bytes |
| SHA-256 | `b71298f90d391eeb8ddeebc0196c246260effde7f5eda577639647e8e4bcbb66` |
| Relationship | Original generated JPEG bytes; not resized, cropped, or recompressed |
| Embedded provenance | C2PA manifest markers identify `Grok Imagine`, `trainedAlgorithmicMedia`, and `SpaceXAI`; the original metadata is preserved byte-for-byte |

The account-scoped generation URL is intentionally not published. The hash
above anchors the exact bytes in this repository.

A dedicated `c2patool` verifier was not available locally, so this record does
not claim independent cryptographic validation of the embedded signature.

## Visual-reference record

The final image was grounded with official public references so the systems
would read as DGX Sparks rather than generic computers. The references were
used only as visual inputs and are not redistributed in this repository.

| Reference | Public source | Downloaded reference SHA-256 | Relationship to final image |
|---|---|---|---|
| NVIDIA DGX Spark product photography | [NVIDIA Local AI](https://developer.nvidia.com/local-ai) / [official image](https://developer.download.nvidia.com/images/local-ai/nvidia-dgx-spark-panels-ari.jpg) | `5d1ffa3ab5c6ce82e6890651a6af554b264b46c1f3cada4bcec82973c5d148c9` | Form-factor reference only; the source photograph is not included |
| Device-only crop made from that NVIDIA image | Derived locally from the reference above | `f034b6153e20e36fba4c4af239225c4ad8e329bf0e0b6e248d10f8480d2723e7` | Prompt reference only; not included |
| DeepSeek organization avatar | [Official DeepSeek GitHub organization](https://github.com/deepseek-ai) / [avatar image](https://avatars.githubusercontent.com/u/148330874?v=4) | `55e6e0c1ba0c453749211368b8a26e00f470b4ab696ce1fed539d70777d4aab1` | Identity reference only; the generated whale is not a copy of the avatar bytes |

## Accepted generation path

The accepted image came from a bounded three-stage correction sequence in the
same Grok conversation:

1. A hardware-only pass used the official NVIDIA device crop as the form-factor
   reference and asked for eight compact, horizontal Spark-style systems in
   four separated pairs.
2. A count-only repair locked the composition to exactly eight systems, exactly
   four two-system groups, and exactly one cyan link inside each pair.
3. A branding-only pass preserved the accepted hardware and count while adding
   the exact title, exact configuration line, and one whale emblem visually
   grounded by the official DeepSeek organization avatar.

The shared hard constraints were: no people, no room or location detail, no
extra systems, no performance number, no record claim, no personal identifier,
no extra text, and no watermark. The generator returned a 1,248 x 832 image.
The repository makes no 16:9 claim, and the full image is used without cropping.

## Acceptance record

- Exactly eight Spark-style systems arranged as four visible two-system groups:
  pass.
- One visible cyan connection inside each pair: pass.
- Solid champagne-metal horizontal chassis, textured dark front, and twin tall
  rounded front recesses derived from the official product reference: pass as
  stylized identification, not as a photographic replica.
- Exact title `DEEPSEEK V4 FLASH 0731`: pass.
- Exact configuration line `8× DGX SPARK • 4× TP=2`: pass.
- One blue whale emblem, generated from the official DeepSeek avatar reference:
  pass as an identification motif, not as a byte-identical upstream logo asset.
- No person, room detail, rack, extra device, performance figure, record claim,
  personal identifier, account URL, or watermark: pass.
- Suitable as conceptual repository artwork: pass.
- Suitable as physical-topology or benchmark evidence: no; explicitly out of
  scope.

Drafts with six tower-like systems, four oversized systems, a distorted animal
mark, or corrupted subtitle text were rejected and are not included in the
public tree. The previous public hero at commit `e9ea41a` was superseded because
its generic low-profile chassis were not a defensible DGX Spark depiction; that
historical asset remains recoverable through Git history.

## Trademark boundary

NVIDIA, DGX, DGX Spark, DeepSeek, and their associated marks belong to their
respective owners. Their names and the generated visual identifiers are used
only to describe the independently run system and model. No endorsement,
partnership, or official benchmark status is claimed.
