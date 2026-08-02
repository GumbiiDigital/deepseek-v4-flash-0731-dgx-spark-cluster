# Graphic provenance

## Published asset

| Field | Value |
|---|---|
| Path | `media/deepseek-v4-flash-0731-dgx-spark-cluster-hero.jpg` |
| Production method | Deterministic HTML/CSS composition captured from a local browser |
| Generated | 2026-08-02 UTC |
| Dimensions | 1,264 x 712 pixels |
| Format | JPEG, sRGB |
| File size | 87,408 bytes |
| SHA-256 | `268467bbc3b6ed669cc260208bce93be15d70b7fdf177949534af23d8788215f` |
| Relationship | Original browser-capture bytes; not resized or recompressed after capture |

This revision contains no AI-generated hardware and no desktop or monitor. Each
of the eight visible units is a repeated crop of the same official NVIDIA
product photograph, used to make the requested four two-Spark pairs legible.
The repeated crops are a visual summary, not eight independent photographic
captures or proof of physical inventory.

## Embedded-source record

| Source | Public origin | Downloaded source SHA-256 | Use in the final graphic |
|---|---|---|---|
| NVIDIA DGX Spark product photograph | [Official DGX Spark product page](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) / [direct official image](https://www.nvidia.com/content/dam/en-zz/Solutions/dgx-spark/DGX-Spark-og.jpg) | `e1ebbda8aa122a77e2d2bc150c02efa223c9ce328f8a9e7017ba734f86f9c6bc` | A 320 x 200 crop at source coordinates `x=775,y=420` is repeated eight times; the crop isolates the real Spark chassis and reflection, with no repainting, regeneration, or content replacement; visible `Courtesy of NVIDIA` attribution |
| DeepSeek organization avatar | [Official DeepSeek GitHub organization](https://github.com/deepseek-ai) / [avatar image](https://avatars.githubusercontent.com/u/148330874?v=4) | `55e6e0c1ba0c453749211368b8a26e00f470b4ab696ce1fed539d70777d4aab1` | Full source image scaled into the identity tile; no redrawing or generated substitute |

The source files are not separately redistributed in this repository. Their
pixels appear only inside the flattened hero composite. The NVIDIA photograph
and DeepSeek mark remain third-party material and are excluded from Gumbii
Digital's reuse rights.

## Composition record

The final layout was rendered at a fixed 1,264 x 712 viewport. It combines:

1. the exact title `V4 FLASH 0731`;
2. the exact configuration labels `8× DGX SPARK` and `4× TP=2`;
3. eight repeated crops of the official NVIDIA product photograph, each visibly showing the Spark chassis;
4. the official DeepSeek avatar in an identity tile; and
5. four labeled rows, each containing exactly two photo crops connected by one
   `TP=2` link.

No generative image model was used for this revision. HTML/CSS supplied only
the background, typography, borders, pair connectors, and labels; the visible
Spark units are all derived from the official NVIDIA source photo.

## Acceptance record

- Eight actual NVIDIA DGX Spark product-photo crops are visibly present: pass.
- The photograph's Spark retains the official chassis, textured front, NVIDIA
  identification, proportions, and product-photo lighting in every crop: pass.
- Exactly four rows and eight visible units communicate four two-Spark pairs,
  without desktop or monitor clutter: pass.
- Exact model and configuration text: pass.
- Official DeepSeek whale identity is visibly present: pass.
- `Courtesy of NVIDIA` is visible beside the photo: pass.
- No person, private room detail, rack photograph, host label, address,
  performance figure, record claim, personal identifier, account URL, or
  watermark: pass.
- Suitable as a repository hero and configuration summary: pass.
- Suitable as physical-topology, inventory, or benchmark evidence: no;
  explicitly out of scope. The eight units are repeated crops of one official
  source photograph.

The generated-hardware hero published at commit `f745a17` was superseded after
visual review found that its chassis were not actual DGX Spark photographs.
That historical asset remains recoverable through Git history but is no longer
in the current publication tree.

## Six-run comparison graphic

The separate [`agent-showcase/replicated-512-vs-1024.jpg`](agent-showcase/replicated-512-vs-1024.jpg)
is a 1,600 x 900 evidence-derived comparison, SHA-256
`223066e5e352a026660b331e4a75fa3f8b019ef319f8de66bce29b07d9bec93f`.
Its hardware and identity tiles use the same official NVIDIA crop and DeepSeek
avatar described above. Its values come only from the independently verified
public six-run JSON.

Grok generated the abstract cyan light/whale background. The accepted source
hash is `8525ec39f79b2b040f02e36424240c2c014b6c549903494750a6cbb9939f0ee6`.
It is used at reduced opacity and contributes no hardware, topology, mark,
label, or measurement. Full source and render hashes are recorded in the
[agent-showcase media record](agent-showcase/README.md).

## Rights and trademark boundary

The NVIDIA photograph is used for editorial product identification in this
independent engineering record and is visibly attributed. The source is cropped
and repeated for a visual cluster summary; that does not grant a right to use
the image outside the applicable source terms. Refer to
[NVIDIA's terms](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/)
for rights governing the source photograph. NVIDIA, DGX, DGX Spark, DeepSeek,
and their associated marks belong to their respective owners. No endorsement,
partnership, or official benchmark status is claimed.
