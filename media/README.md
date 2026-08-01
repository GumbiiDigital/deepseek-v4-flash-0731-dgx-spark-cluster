# Graphic provenance

## Published asset

| Field | Value |
|---|---|
| Path | `media/deepseek-v4-flash-0731-dgx-spark-cluster-hero.jpg` |
| Production method | Deterministic HTML/CSS composition captured from a local browser |
| Generated | 2026-08-01 UTC |
| Dimensions | 1,264 x 712 pixels |
| Format | JPEG, sRGB |
| File size | 72,979 bytes |
| SHA-256 | `2227ed358965aec6935572f24a79cdaa4b902e54fcd03a7688652a0b4c0ed641` |
| Relationship | Original browser-capture bytes; not resized or recompressed after capture |

This revision contains no AI-generated hardware. The Spark visible in the
photographic panel comes from an official NVIDIA product photograph. The eight
nodes in the four pair cards are intentionally abstract schematic symbols, not
computer renderings or photographs.

## Embedded-source record

| Source | Public origin | Downloaded source SHA-256 | Use in the final graphic |
|---|---|---|---|
| NVIDIA DGX Spark product photograph | [Official DGX Spark product page](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) / [direct official image](https://www.nvidia.com/content/dam/en-zz/Solutions/dgx-spark/DGX-Spark-og.jpg) | `e1ebbda8aa122a77e2d2bc150c02efa223c9ce328f8a9e7017ba734f86f9c6bc` | Full 1,200 x 630 source frame scaled into the photo panel; no subject crop, repainting, regeneration, or content replacement; visible `Courtesy of NVIDIA` attribution |
| DeepSeek organization avatar | [Official DeepSeek GitHub organization](https://github.com/deepseek-ai) / [avatar image](https://avatars.githubusercontent.com/u/148330874?v=4) | `55e6e0c1ba0c453749211368b8a26e00f470b4ab696ce1fed539d70777d4aab1` | Full source image scaled into the identity tile; no redrawing or generated substitute |

The source files are not separately redistributed in this repository. Their
pixels appear only inside the flattened hero composite. The NVIDIA photograph
and DeepSeek mark remain third-party material and are excluded from Gumbii
Digital's reuse rights.

## Composition record

The final layout was rendered at a fixed 1,264 x 712 viewport. It combines:

1. the exact title `V4 FLASH 0731`;
2. the exact configuration labels `8× DGX SPARK` and `4× TP=2`;
3. the official NVIDIA product photograph in a visibly attributed panel;
4. the official DeepSeek avatar in an identity tile; and
5. four labeled schematic pair cards, each containing exactly two abstract
   nodes connected by one `TP=2` link.

No generative image model was used for this revision. HTML/CSS supplied only
the background, typography, borders, and schematic pair shapes.

## Acceptance record

- An actual NVIDIA DGX Spark product photograph is visibly present: pass.
- The photograph's Spark retains the official chassis, textured front, NVIDIA
  identification, proportions, and product-photo lighting: pass.
- Exactly four pair cards and eight abstract nodes communicate the cluster
  structure without pretending to be additional hardware photographs: pass.
- Exact model and configuration text: pass.
- Official DeepSeek whale identity is visibly present: pass.
- `Courtesy of NVIDIA` is visible beside the photo: pass.
- No person, private room detail, rack photograph, host label, address,
  performance figure, record claim, personal identifier, account URL, or
  watermark: pass.
- Suitable as a repository hero and configuration summary: pass.
- Suitable as physical-topology or benchmark evidence: no; explicitly out of
  scope.

The generated-hardware hero published at commit `f745a17` was superseded after
visual review found that its chassis were not actual DGX Spark photographs.
That historical asset remains recoverable through Git history but is no longer
in the current publication tree.

## Rights and trademark boundary

The NVIDIA photograph is used for editorial product identification in this
independent engineering record and is visibly attributed. Refer to
[NVIDIA's terms](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/)
for rights governing the source photograph. NVIDIA, DGX, DGX Spark, DeepSeek,
and their associated marks belong to their respective owners. No endorsement,
partnership, or official benchmark status is claimed.
