# Graphic provenance

## Published asset

| Field | Value |
|---|---|
| Path | `media/deepseek-v4-flash-0731-dgx-spark-cluster-hero.jpg` |
| Generator | Grok image generation through the Grok chat interface |
| Attribution | [Created with Grok](https://x.ai/legal/brand-guidelines) |
| Generated | 2026-08-01 UTC |
| Dimensions | 1,168 x 784 pixels |
| Format | JPEG, sRGB |
| SHA-256 | `97aca3bb7098e3803da34e598787c1e209813d55b5d0cb5de94cb0b959c84fe8` |
| Relationship | Original generated JPEG bytes; not resized, cropped, or recompressed |
| Embedded provenance | C2PA manifest markers identify `Grok Imagine`, `trainedAlgorithmicMedia`, and `SpaceXAI`; the original metadata is preserved byte-for-byte |

The account-scoped asset origin is intentionally not published. The hash above
anchors the exact bytes that are in this repository.

A dedicated `c2patool` verifier was not available locally, so this record does
not claim independent cryptographic validation of the embedded signature.

## Accepted prompt

```text
Create a wide 16:9 conceptual technology illustration. Show exactly eight
compact matte-black square compute nodes, arranged as four clearly separated
two-node pairs on a dark graphite surface. Connect each pair with one glowing
teal line. Warm amber data particles flow from all four pairs toward the
center. Premium cinematic product visualization, clean precise industrial
geometry, high contrast, dramatic studio lighting, and safe margins. No
people, no text, no letters, no numerals, no logos, no labels, no watermarks,
no extra devices, no server rack, and no tangled cables.
```

The generator returned a 1,168 x 784 image rather than the requested 16:9
canvas. The result was accepted because the repository does not make an aspect
ratio claim and the full image works as the README hero without cropping.

## Acceptance record

- Exactly eight discrete compute nodes: pass.
- No extra node, person, room detail, text, numeral, label, logo, or watermark:
  pass.
- Teal and amber paired-data visual language: pass.
- Suitable as conceptual repository artwork: pass.
- Suitable as physical topology or benchmark evidence: no; explicitly out of
  scope.

The direct Imagine-page attempts remained unresolved placeholders and were not
published. The accepted asset was generated through Grok chat, downloaded as
the original response bytes, and visually reviewed before inclusion.
