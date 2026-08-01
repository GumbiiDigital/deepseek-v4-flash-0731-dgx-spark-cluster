# Third-party notices and provenance

This bundle records versions and links; it does not redistribute the model,
serving engine, comparison client, or container image.

| Component | Pinned identity | Source | Terms |
|---|---|---|---|
| DeepSeek-V4-Flash-0731 | `9e165c30e2704aec5d9d593cce3eebd58bbef1cb` | [Model revision](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731/tree/9e165c30e2704aec5d9d593cce3eebd58bbef1cb) | [Upstream MIT license](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731/blob/9e165c30e2704aec5d9d593cce3eebd58bbef1cb/LICENSE) |
| vLLM | upstream commit `264bce1da81e27d638e7cf265b4cbd125d023c38` embedded in the tested custom build version | [Upstream source](https://github.com/vllm-project/vllm/tree/264bce1da81e27d638e7cf265b4cbd125d023c38) | [Apache-2.0](https://github.com/vllm-project/vllm/blob/264bce1da81e27d638e7cf265b4cbd125d023c38/LICENSE) |
| vLLM serving benchmark | deployed build's `vllm bench serve` interface | [Official documentation](https://docs.vllm.ai/en/stable/cli/bench/serve/) | Same vLLM terms |
| llama-benchy | `e9be344578cec17745066b220798b80a0d2686d3` | [Pinned source commit](https://github.com/eugr/llama-benchy/commit/e9be344578cec17745066b220798b80a0d2686d3) | [MIT](https://github.com/eugr/llama-benchy/blob/e9be344578cec17745066b220798b80a0d2686d3/LICENSE) |

The repository hero is a deterministic photo-and-diagram composite, not a
generated hardware scene. It embeds the complete frame of an official
[NVIDIA DGX Spark product photograph](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
from this [direct NVIDIA asset](https://www.nvidia.com/content/dam/en-zz/Solutions/dgx-spark/DGX-Spark-og.jpg).
The source frame is scaled inside the composition without a subject crop,
repainting, regeneration, or content replacement, and the graphic visibly says
`Courtesy of NVIDIA`. The NVIDIA photograph remains NVIDIA copyright and is
not licensed under Gumbii Digital's repository terms; use of the source material
is subject to [NVIDIA's terms](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/).

The hero also embeds the complete official
[DeepSeek GitHub organization avatar](https://github.com/deepseek-ai) as its
model-identity tile. That mark remains DeepSeek property and is likewise
excluded from Gumbii Digital's reuse rights. The four two-node pair cards are
original schematic shapes and are not presented as product photographs.

NVIDIA, DGX, DGX Spark, DeepSeek, and their associated marks belong to their
respective owners. Names, the product photograph, and the DeepSeek identity
mark are used only to identify the independently tested hardware and
model. No endorsement, partnership, or official benchmark status is implied.

The tested container is identified in [run-identity.json](data/run-identity.json)
by an exact image digest. The custom image and its build recipe are not included,
so the digest proves runtime identity within the retained evidence rather than
public image availability.
