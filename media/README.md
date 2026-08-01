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
| SHA-256 | `a52c91aae663ca3a2f88bde64614b5037ba6b081e5279c8eeb2d5861887e814c` |
| Relationship | Original generated JPEG bytes; not resized, cropped, or recompressed |
| Embedded provenance | C2PA manifest markers identify `Grok Imagine`, `trainedAlgorithmicMedia`, and `SpaceXAI`; the original metadata is preserved byte-for-byte |

The account-scoped asset origin is intentionally not published. The hash above
anchors the exact bytes that are in this repository.

A dedicated `c2patool` verifier was not available locally, so this record does
not claim independent cryptographic validation of the embedded signature.

## Accepted generation path

The final image was produced through a style-and-layout prompt followed by one
focused form-factor repair. The repair used the preceding generated image as a
composition reference, so the text alone is not presented as a deterministic
reproduction recipe.

### Style and layout prompt

```text
Use the image you just generated only as a rough composition reference. Create
a completely new, much more energetic wide 16:9 repository hero graphic for a
real eight-system cluster.

Show exactly eight recognizable NVIDIA DGX Spark desktop systems, not generic
black boxes: compact low square chassis, black front panels, copper-gold
perforated top surfaces, and restrained authentic product-style "DGX SPARK"
identification on the hardware. Arrange them as exactly four clearly separated
two-system pairs. Each pair is connected by one bright cyan data link, and all
four pairs converge toward a central burst of electric cyan and deep-blue
light.

Make the central visual a dramatic lightning-flash / deep-ocean energy surge—
sharp, fast, technical, and unmistakably "Flash"—with a subtle abstract
deep-sea wave silhouette in the energy, but do not copy or invent a DeepSeek
corporate logo. Add only this exact clean headline: "DEEPSEEK V4 FLASH 0731".
Add only this exact smaller line: "8× DGX SPARK • 4× TP=2". Use crisp modern
geometric typography with safe margins.

Premium cinematic product visualization, aggressive high contrast,
graphite-black background, cyan/teal energy, NVIDIA-green accent light, copper
hardware highlights, clean industrial precision, dramatic depth, and enough
negative space to remain readable as a GitHub README hero.

Hard constraints: exactly eight devices, exactly four pairs, no people, no room
or location detail, no rack, no extra devices, no tangled cables, no performance
numbers, no tokens-per-second claims, no "record" claim, no personal
identifiers, no email, no usernames, no extra words, no misspelled text, and no
watermark.
```

### Accepted form-factor repair prompt

```text
Use the most recent generated image as a composition and lighting reference
only. Correct one specific failure: every computer is the wrong form factor.

Replace all eight tall tower/server shapes with exactly eight low-profile
NVIDIA DGX Spark desktop systems sitting flat on the surface. Each DGX Spark
must be a compact square slab approximately three times wider than it is tall,
with a black front edge, dark sidewalls, and a copper-gold perforated top panel—
the real compact desktop DGX Spark silhouette. Show no rear panels, no rack
faces, no tower cases, and absolutely no loose or bundled cables.

Preserve the strong central cyan lightning, graphite background, exact
eight-device count, exact four separated two-device pairs, cyan pair links,
cinematic copper/cyan color palette, safe margins, and the clean centered
typography exactly as written:
"DEEPSEEK V4 FLASH 0731"
"8× DGX SPARK • 4× TP=2"

No people, no room detail, no extra devices, no performance numbers, no record
claim, no personal identifiers, no extra wording, no misspelled text, and no
watermark.
```

The generator returned a 1,248 x 832 image rather than the requested 16:9
canvas. The result was accepted because the repository does not make an aspect
ratio claim and the full image works as the README hero without cropping.

## Acceptance record

- Exactly eight low-profile systems in four visible two-system groups: pass.
- Exact two-line title and configuration label, with no additional wording:
  pass.
- Central cyan flash and one visible cyan link within each pair: pass.
- No extra device, person, room detail, rack, loose cable, performance figure,
  record claim, personal identifier, or watermark: pass.
- Low-profile square silhouette, black sidewalls, and copper perforated tops:
  pass as stylized DGX Spark identification, not as a photographic product
  replica.
- Suitable as conceptual repository artwork: pass.
- Suitable as physical topology or benchmark evidence: no; explicitly out of
  scope.

An intermediate revision with tall tower cases and cable bundles was rejected
and is not included in the public tree. The accepted asset was generated through
Grok chat, downloaded as the original response bytes, and visually reviewed
before inclusion.
