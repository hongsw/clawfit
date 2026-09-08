# Research Watch: MiniCPM5-2B — 2B-Class On-Device Agent Model with Tool-Calling

- Repo: https://github.com/OpenBMB/MiniCPM (⭐10,600)
- Source: HuggingFace model hub — openbmb/MiniCPM5-2B (602 likes, 2,879 downloads, 2026-09-07); GitHub Topics: on-device-ai, edge-ai, tool-calling, agent
- License: Apache-2.0

## Why this is worth watching

MiniCPM5-2B is a 2B-parameter dense Transformer explicitly trained for agentic tool-calling on-device. It is not a quantized reduction of a larger model — it is trained from scratch on agent-specific SFT data (UltraData-SFT-Agent-2609) alongside general instruction and reasoning data. The model reports 2B-class SOTA on coding, math, tool use, and agentic benchmarks, with competitive scores against 4B-class models on several tasks.

The combination of a small parameter count (2B), Apache-2.0 license, and explicit support for SGLang's tool-calling interface means this can run on consumer hardware (a MacBook M3 or a mid-range Android device with an appropriate quantization) and be deployed without an API key. For clawfit configurations that target `network: offline` or `data_sensitivity: confidential`, this is a candidate L1 entry that did not exist before September 2026.

Released 2026-09-07; 497 GitHub commits; 10,600 GitHub stars on the parent MiniCPM repository.

## What stands out immediately

- **2B parameters, on-device design target**: the model is explicitly positioned for edge and mobile deployment, not cloud API; Ollama and llama.cpp are listed as supported runtimes alongside SGLang and vLLM
- **UltraData-SFT-Agent-2609 training data**: a named agent-specific SFT dataset used in training; suggests the tool-calling capability is not post-hoc fine-tuning but part of the base training recipe
- **SGLang recommended for tool-calling**: SGLang's structured generation interface is listed as the primary tool-calling runtime; vLLM and Transformers are supported but the recommendation for tool-calling tasks is explicit
- **Long-context support**: the release documentation references long-context handling (specific context window size not confirmed in secondary sources at research time)
- **Benchmark competitive with 4B-class models on tool use and agentic tasks**: the reported result is self-reported by OpenBMB; the specific benchmarks and comparison baselines are not independently verified in secondary coverage reviewed
- **Ollama support listed**: direct implication that deployment via `ollama run openbmb/minicpm5-2b` is intended, which is the lowest-friction local deployment path for Claude Code users currently using Ollama-backed models
- **Apache-2.0 license**: commercially permissive; no network-copyleft (AGPL) or non-commercial clause; the model weights can be integrated into proprietary products

## Why clawfit should care

1. **First 2B-class model with native tool-calling in the research log**: prior L1 entries for local/offline deployment (Ollama-backed Llama 3, Phi-3) are not trained specifically for agent tool-calling workflows. MiniCPM5-2B's training recipe is explicitly agent-oriented. For `task: code-gen` or `task: qa` profiles with `network: offline`, the recommendation engine currently has no sub-7B model that was trained for tool-calling as a primary capability. This would be the first.

2. **On-device AI confirms a new L1 sub-type**: the L1 layer in reference-levels.md currently distinguishes models primarily by provider (Anthropic, OpenAI, local Ollama) and by capability tier (frontier vs. capable vs. fast). MiniCPM5-2B introduces a third distinguishing axis: deployment target (cloud API vs. on-device/edge). A `deployment_target: cloud | local | edge` field on LLM registry entries would let clawfit surface the right model for `hardware: local` + `network: offline` configurations without requiring the user to know specific model names.

3. **Ollama support means low-friction integration with existing clawfit agent stack**: Claude Code, Goose, Aider, Continue — multiple registry agents already support Ollama-backed model selection. MiniCPM5-2B being Ollama-compatible means a `(Goose, MiniCPM5-2B, local)` triple is already technically viable without code changes, pending only a registry entry.

4. **SGLang tool-calling interface is a new runtime dependency signal**: the recommendation to use SGLang for tool-calling — rather than raw Transformers or vLLM — introduces a runtime dependency that is not currently modeled in clawfit's hardware or capability layers. A harness that routes tool calls through SGLang's structured generation API is different from one that relies on JSON extraction from free-form output. This is a practical compatibility concern for any agent that expects OpenAI-format tool-calling JSON.

## Preliminary interpretation

Current best reading:
- **L1 — Base Runtime / Model Tier (primary)**: MiniCPM5-2B is an LLM that runs locally; it belongs in `llms.json` as an offline-capable, tool-calling model
- **L7 — Infrastructure / Deployment (secondary)**: the on-device deployment target and Ollama/llama.cpp runtime support are infrastructure-layer concerns; the model requires specific runtimes and hardware profiles to perform at its reported benchmarks

## Claims to verify

- Whether the "competitive with 4B-class models on agentic tasks" claim holds on benchmarks with external validators (BFCL, τ-Bench, ToolBench), or only on OpenBMB-internal evaluation sets
- Whether the long-context claim has a specific context length and whether the full context length performs comparably to the reported short-context benchmark scores
- Whether Ollama support is officially published as an Ollama library model (searchable in `ollama search`) or requires manual Modelfile setup
- Whether the SGLang tool-calling interface is compatible with Claude Code's current tool-call format (Anthropic JSON) or requires an adapter layer
- Whether the Apache-2.0 license applies to both model weights and training code, or whether the training dataset (UltraData-SFT-Agent-2609) carries a different license that constrains derivative works

## Status

- 10,600 stars on the parent OpenBMB/MiniCPM repo (above registry threshold 5k★); Apache-2.0; released 2026-09-07 (within 6-month window ✓)
- Registry consideration: blocked on (a) deterministic public cost/latency data — self-hosted model has no fixed API cost; (b) schema gap — no `deployment_target` field in `llms.json`; (c) hardware compatibility — no entry for consumer GPU or mobile hardware in `hardware.json`
- Watch: whether the Ollama library publishes an official openbmb/minicpm5-2b model; whether a third-party benchmark reproduces the "4B-class competitive" claim; whether a clawfit-compatible harness agent (Goose, Continue) publishes MiniCPM5-2B as a tested configuration
- This is the first on-device/edge model explicitly trained for tool-calling in this research log; two independent signals for the on-device agent model sub-type would justify a new L1 sub-section in reference-levels.md
