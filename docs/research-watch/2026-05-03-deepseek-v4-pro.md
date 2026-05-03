# Research Watch: DeepSeek V4-Pro

- Repo: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
- Also see: https://huggingface.co/blog/deepseekv4 | https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash | https://simonwillison.net/2026/Apr/24/deepseek-v4/ | https://openrouter.ai/deepseek/deepseek-v4-pro

## Why this is worth watching

DeepSeek V4-Pro is currently the largest open-weight model by parameter count (1.6T total / 49B active via MoE) and holds the top SWE-Bench Verified score among open-weight models at 80.6 — statistically tied with Claude Opus 4.6 at 80.8. It ships under MIT license and is available via API at $0.435/M input tokens, meaningfully cheaper than comparable closed frontier models. The combination of frontier-tier coding performance, open weights, and aggressive pricing creates direct pressure on the cost/quality tradeoffs in clawfit's current llms.json.

## What stands out immediately

- **Architecture**: MoE with hybrid attention combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA). At 1M-token context, requires only 27% of single-token inference FLOPs and 10% of KV cache compared to V3.2 — a genuine efficiency claim, not marketing rounding.
- **Context window**: 1M tokens natively. This is not a retrieval approximation; MRCR 8-needle retrieval at 256K scores >0.82 accuracy (drops to 0.59 at 1M — degradation is real and documented).
- **Reasoning modes**: Three explicit modes — Non-Think (no chain-of-thought), Think High (explicit `<think>` blocks), Think Max (maximum reasoning effort, requires minimum 384K context). This is a claim to inspect: the token overhead of Think Max at scale is not yet independently benchmarked.
- **Codeforces rating 3,206**: Claimed highest competitive programming score by any model at release, above GPT-5.4's 3,168. Independently reported by multiple sources.
- **SWE-Bench Verified 80.6**: Validated via the HuggingFace blog benchmark table. At parity with Opus 4.6-Max (80.8) and above Sonnet 4.5 (47%) — the gap vs mid-tier models is significant.
- **V4-Flash companion**: 284B total / 13B active, $0.14/M input. Simon Willison notes Unsloth quantized versions will run on M5 MacBook Pro, making this a viable offline-capable candidate.
- **License**: MIT. No usage restrictions documented at time of writing.
- **Training**: 32T+ tokens pre-training, two-stage post-training (SFT+RL with GRPO, then on-policy distillation). Precision: FP4 for MoE experts, FP8 elsewhere.
- **OpenRouter usage signal**: 43.4B prompt tokens processed in tracked periods — early but real adoption signal.
- **Developer survey**: 52% of surveyed developers reported V4-Pro ready to replace primary coding model (source: HuggingFace blog). Methodology not disclosed; treat as directional.

## Why clawfit should care

clawfit's llms.json currently has no open-weight frontier model with a context window above 200K or a competitive code-gen score. V4-Pro fills that gap at a cost point below claude-opus ($0.435/M vs $15/M), with documented SWE-Bench performance that meets or exceeds the current top entry in the registry. The V4-Flash variant is particularly relevant: at $0.14/M input with a quantized path to offline hardware, it could occupy the cost_per_1k_tokens = 0.00014 slot that no current registry entry covers. Both models need scoring weight review — the 1M-token context and agent-optimized training (interleaved reasoning across tool calls, XML tool schemas, RL on real environments) are direct inputs to clawfit's latency and capability scoring.

## Preliminary interpretation

Current best reading:
- **Not an ecosystem layer** — this is an LLM backend, not an agent surface, harness, or infrastructure layer.
- Maps to `llms.json` in the registry, not to any of the 7 ecosystem layers in reference-levels.md.
- If clawfit were to add an "LLM tier" distinction, V4-Pro would sit alongside claude-opus as a frontier-tier entry and V4-Flash alongside mistral-medium-3-5 as a mid-tier entry.

## Status

- Registry threshold met: V4-Pro is in active commercial API use (OpenRouter, DeepInfra, Together AI, DeepSeek own API) with documented large-scale adoption. MIT license removes any open-weight barrier. Recommend adding both `deepseek-v4-pro` and `deepseek-v4-flash` to `llms.json` — schema is fully compatible with existing entries. No reference-levels.md change warranted.
