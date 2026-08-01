# Third-party notices and provenance

This bundle records versions and links; it does not redistribute the model,
serving engine, comparison client, or container image.

| Component | Pinned identity | Source | Terms |
|---|---|---|---|
| DeepSeek-V4-Flash-0731 | `9e165c30e2704aec5d9d593cce3eebd58bbef1cb` | [Model revision](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731/tree/9e165c30e2704aec5d9d593cce3eebd58bbef1cb) | [Upstream MIT license](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731/blob/9e165c30e2704aec5d9d593cce3eebd58bbef1cb/LICENSE) |
| vLLM | upstream commit `264bce1da81e27d638e7cf265b4cbd125d023c38` embedded in the tested custom build version | [Upstream source](https://github.com/vllm-project/vllm/tree/264bce1da81e27d638e7cf265b4cbd125d023c38) | [Apache-2.0](https://github.com/vllm-project/vllm/blob/264bce1da81e27d638e7cf265b4cbd125d023c38/LICENSE) |
| vLLM serving benchmark | deployed build's `vllm bench serve` interface | [Official documentation](https://docs.vllm.ai/en/stable/cli/bench/serve/) | Same vLLM terms |
| llama-benchy | `e9be344578cec17745066b220798b80a0d2686d3` | [Pinned source commit](https://github.com/eugr/llama-benchy/commit/e9be344578cec17745066b220798b80a0d2686d3) | [MIT](https://github.com/eugr/llama-benchy/blob/e9be344578cec17745066b220798b80a0d2686d3/LICENSE) |

The repository hero image was generated through Grok Imagine and is labeled
“Created with Grok” in accordance with the
[xAI Brand Guidelines](https://x.ai/legal/brand-guidelines). The image is
conceptual artwork, contains no xAI or hardware-vendor logo, and is not used as
benchmark or physical-topology evidence.

The tested container is identified in [run-identity.json](data/run-identity.json)
by an exact image digest. The custom image and its build recipe are not included,
so the digest proves runtime identity within the retained evidence rather than
public image availability.
