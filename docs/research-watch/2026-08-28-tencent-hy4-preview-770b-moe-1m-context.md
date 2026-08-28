# Research Watch: Tencent Hy4-preview — 770B MoE Open-Weight Model with 1M-Token Context

- Repo: https://github.com/Tencent-Hunyuan/Hy4-preview (⭐202 at release, today 2026-08-28)
- HF: https://huggingface.co/tencent/Hy4-preview (220 likes)
- Source: Hugging Face trending models; TechNode; Tencent official press release (2026-08-28)

## Why this is worth watching

Tencent released and open-sourced Hy4-preview today under Apache 2.0. The timing is notable: it drops the same day that GLM-5.3's open weights were expected (and delayed), making this a direct competitive signal in the race for open-weight frontier-class models. Hy4 is Tencent's largest open-weight model to date, and at 770B total parameters with 49B activated per forward pass, it lands in the same tier as DeepSeek V4 and GLM-5.3-Flash.

The 1M-token context window, if it holds quality at full context, has meaningful implications for agent deployments that need to maintain long session state or reason over large codebases in a single pass. The model is co-designed with Tencent product teams, which implies it has undergone task-specific tuning beyond raw benchmark optimization.

Low initial star count reflects launch-day timing. The model's significance is based on Tencent's established track record with Hunyuan and the architectural specifics, not current community adoption numbers.

## What stands out immediately

- **770B total / 49B active MoE**: achieves a 15.7:1 sparsity ratio (activation / total parameters), competitive with DeepSeek V4-class models; inference cost decouples from parameter count
- **256 routed experts + 1 shared expert per MoE layer**: expert count is notably high; finer granularity typically improves routing quality and reduces expert imbalance
- **Gated DeepSeek Sparse Attention (Gated DSA) with IndexCache**: cross-layer sparse index reuse reduces attention compute; the "Gated" modifier and IndexCache are architecture-level additions to the original DSA design from DeepSeek
- **Identity Hyper-Connections (iHC)**: replaces standard residual connections to expand inter-layer information flow; cited as improving scaling efficiency
- **Native MTP (Multi-Token Prediction) layer**: built-in speculative decoding support with 10B total / 0.7B activated parameters; production inference acceleration is first-class, not an add-on
- **1M-token context window**: matches the frontier; claims "precise long-context capabilities" — needs independent evaluation at 4x+ native context
- **Apache 2.0 license**: commercially permissive; directly competes with GLM-5.3-Flash (MIT) for enterprise open-weight adoption
- **Domain co-design**: trained on data tuned for software engineering, office analysis, game development, and scientific research — a broader domain mix than coding-specialist models

## Why clawfit should care

Hy4-preview adds a third major open-weight frontier-class model available since August 2026 alongside DeepSeek Harness (uses DeepSeek V4) and GLM-5.3-Flash. For clawfit's `hardware: local` and `hardware: local-apple-silicon` filters, 49B active parameters is manageable on multi-GPU workstations but not on consumer Apple Silicon. The `budget` filter logic needs to account for open-weight models where compute cost is deployment-dependent rather than a fixed API rate.

The 1M-context claim should influence how clawfit treats `statefulness: session` vs `statefulness: persistent` filters: a model that can hold 1M tokens in context arguably blurs the line between session-scoped and persistent-context deployments.

The simultaneous release with GLM-5.3-Flash (also open-weight, also today) is a two-signal confirmation that open-weight frontier-class models are now a sustained pattern, not a one-time event. This validates the case for adding `weights: [proprietary | open]` as a registry dimension.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Runtime / LLM**: primary. Hy4-preview is a foundation model. It sits at L1 as weights available for local deployment and API access.
- No secondary layer: the iHC and Gated DSA are internal architectural choices; they do not surface at the harness (L2) or skill (L4) layer.

The 256-expert MoE architecture is relevant to L7 (infrastructure) only insofar as routing hardware (e.g., NVLink-connected GPU clusters or Groq) must handle expert dispatch at inference time. This is an operator concern, not a clawfit registry concern yet.

## Claims to verify

- Whether the 1M-context quality holds on a diverse long-context benchmark (the claim is architectural; benchmark results at long range are not yet published independently)
- Whether Gated DSA + IndexCache meaningfully reduces TTFT (time-to-first-token) compared to standard MHA at equal context lengths
- Whether the 256-expert router introduces token-dropping artifacts under load that degrade output quality — high expert count can exacerbate load imbalance
- Whether iHC (identity Hyper-Connections) produces measurable quality improvements vs standard residual, or is primarily a training-efficiency claim
- Whether the "approaching Claude Opus 4.8 on coding" benchmark comparison uses a comparable task split and is not cherry-picked

## Status

- Tracking: first signal 2026-08-28 (launch day)
- Stars: 202 GitHub (launch day); 220 HF likes (launch day)
- Registry decision: hold. Open-weight model; API pricing not yet publicly confirmed for the managed endpoint. Local deployment cost is hardware-dependent. Registry entry requires deterministic public cost/latency data. Watch: z.ai API pricing announcement; independent benchmark results from LMSYS or similar.
- Schema gap reinforced: `weights: [proprietary | open]` — Hy4-preview is the third frontier-class open-weight model tracked this month alongside GLM-5.3-Flash and DeepSeek V4
- Watch: LMSYS Arena ranking; any Unsloth GGUF quantization (which typically signals broad community adoption within days of release)
