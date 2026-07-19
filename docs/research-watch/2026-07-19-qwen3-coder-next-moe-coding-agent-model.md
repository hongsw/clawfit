# Research Watch: Qwen3-Coder-Next — MoE Coding-Specialized Open-Weight Model

- Repo: https://github.com/QwenLM/Qwen3-Coder (⭐~5k est.)
- HuggingFace: https://huggingface.co/Qwen/Qwen3-Coder-Next
- AWS Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-qwen-qwen3-coder-next
- Source: WebSearch discovery via "Qwen3-Coder-Next coding agent" (2026-07-19); arXiv 2603.00729; also listed in DEV Community "complete 2026 guide" articles

## Why this is worth watching

Qwen3-Coder-Next is Alibaba's open-weight coding-specialized model: 80B total parameters, 3B active per token (MoE), 256K context window, 70.6% SWE-Bench Verified — the highest tracked open-weight score on SWE-Bench among models with deterministic public API pricing. Released February 4, 2026 (within the 6-month tracking window), it has not previously appeared in clawfit's research-watch series. Its architecture — hybrid attention + MoE — is described in a published arXiv paper (2603.00729). AWS Bedrock availability provides a deterministic cost anchor.

## What stands out immediately

- **70.6% SWE-Bench Verified**: self-reported in the technical report (arXiv 2603.00729); AWS Bedrock documentation confirms the figure — providing one layer of institutional validation beyond the lab's own README
- **80B total / 3B active (MoE)**: same parameter efficiency principle as DeepSeek-R1 (671B total / 37B active) and Kimi K3 (2.8T / ~32B active), but at a consumer-friendly serving scale — 3B active parameters per token means inference cost approaches a 3B-class model despite 80B-class reasoning capacity
- **Hybrid attention architecture**: the base model (Qwen3-Next-80B-A3B-Base) combines standard attention with a variant attention mechanism not specified in the README; the arXiv paper is the primary technical source
- **Agentic training at scale**: the paper describes "executable task synthesis, environment interaction, and reinforcement learning" — not just next-token pretraining on code, but RL-trained on agent-executed tasks
- **AWS Bedrock availability**: provides a managed API path with deterministic pricing, distinct from self-hosting the open weights
- **Explicit coding-agent ecosystem integrations**: OpenClaw, Qwen Code, Claude Code, Web dev, browser use, Cline — the showcase list covers the major tracked coding agent harnesses
- **Context: same announcement day as Qwen3.8**: Qwen3-Coder-Next is a separate product from the just-announced Qwen3.8 flagship. The Coder line addresses the coding-task vertical; the 3.8 flagship addresses general frontier capability.

## Why clawfit should care

Qwen3-Coder-Next is the strongest candidate for a new `llms.json` entry since DeepSeek-V4-Flash:

1. **SWE-Bench coverage**: 70.6% is the highest tracked open-weight score on the primary coding-agent evaluation benchmark. The existing top coding model in `llms.json` (if any) would need to be evaluated against this baseline.

2. **Cost profile**: 3B active parameters at inference means serving cost is effectively a 3B-class model. If AWS Bedrock pricing is in the range of $0.20–$0.60/1M input tokens (typical for small-model API calls), Qwen3-Coder-Next could satisfy `budget: 0.01` profiles at `task: code-gen` quality exceeding current `llms.json` entries.

3. **MoE active-parameter efficiency**: the `cost_per_1k_tokens` field in `llms.json` currently does not distinguish between dense and MoE models of the same active-parameter count. Qwen3-Coder-Next would be the first MoE model in the registry if added, requiring a schema note about cost-at-inference vs. cost-at-serving.

4. **Offline deployment**: open weights under Apache 2.0 enable `network: offline` + `hardware: local` deployment — but serving 80B total parameters locally requires substantial RAM (even if 3B active), potentially requiring ktransformers-style heterogeneous routing (also tracked today).

## Preliminary interpretation

Current best reading:
- **Level 1 — Coding-specialized open-weight LLM backend** (maps to `llms.json`, not a standalone agent or harness)
- Registry profile estimate: `tasks: [code-gen]`, `latency: low` (3B active → fast inference), `context_k: 256`, `network: [online, offline]`, `statefulness: stateless`
- Cost estimate via AWS Bedrock: needs verification from current Bedrock pricing page — do not add to registry until confirmed

## Claims to verify

- **70.6% SWE-Bench Verified**: arXiv 2603.00729 and AWS Bedrock card are two sources. Third-party reproduction (e.g., LiveSWE, independent lab reproduction) needed before registry addition.
- **AWS Bedrock cost_per_1k_tokens**: Bedrock pricing pages must be checked directly. Estimate only; may have changed since the technical report.
- **"Hybrid attention"**: the arXiv paper (2603.00729) describes the architecture; the exact attention mechanism name and its performance implications are not in the README alone.
- **Context window**: 256K is the declared limit; effective context (where quality degrades) is typically lower for MoE models and is not reported.
- **Self-hosted serving requirements**: 80B total parameters in FP16 requires ~160GB RAM. Most consumer hardware cannot host this; ktransformers-style quantization + expert offloading would be needed. The "offline" use case is real but hardware-constrained.

## Status

- Registry eligibility: **PENDING**. Apache 2.0, open weights confirmed, AWS Bedrock pricing available (needs current value pull). SWE-Bench score has institutional validation (Bedrock card). This is closer to registry-ready than any other signal in today's scan.
- Blocking item: pull current AWS Bedrock price for `us.qwen.qwen3-coder-next` (or equivalent endpoint). If `cost_per_1k_tokens` is deterministic and public, proceed to `llms.json` addition.
- Schema note if added: include `active_params_b: 3.0` and `total_params_b: 80.0` to distinguish MoE serving cost from dense equivalent; existing `cost_per_1k_tokens` field covers the API cost.
- Watch trigger: AWS Bedrock pricing confirmation; third-party SWE-Bench reproduction.
