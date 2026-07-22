# Research Watch: Poolside Laguna S 2.1

- Repo: https://huggingface.co/poolside/Laguna-S-2.1
- Also see: https://poolside.ai/blog/introducing-laguna-s-2-1 | https://trajectories.poolside.ai | https://openrouter.ai/poolside/laguna-s-2.1

## Why this is worth watching

Laguna S 2.1 is a 118B/8B-active MoE model whose RL post-training ran across multiple harnesses simultaneously — a deliberate choice to prevent evaluation overfitting to Poolside's own pool scaffold. Poolside releases pool (terminal-based coding agent, up to 500 steps per task, sandboxed) alongside the weights, making this a model-plus-harness pair rather than a standalone LLM drop. At $0.10/$0.20 per 1M tokens on OpenRouter with a 1M-token context window, it is the first Western open-weight coding model at this claimed capability tier with public API pricing below frontier model rates.

## What stands out immediately

- **MoE architecture**: 256 routed experts (top-10) + 1 shared; 8B active per token — inference cost approximates an 8B dense model despite 118B total parameters
- **Dual thinking modes**: off or max-adaptive; no medium tier — same structural gap as Kimi K2.6 Thinking mode, which was flagged as a `latency: low` disqualifier in this cycle
- **pool harness**: ships as both eval scaffold and user-facing product; L2 companion to a L1 model — the eval environment and the user-facing product are the same artifact
- **RL trained across multiple harnesses**: post-training explicitly ran on multiple scaffolds to resist architecture-specific benchmark overfitting; claim to inspect: pool-run evals cannot fully confirm harness-agnostic capability without third-party reproduction
- **Self-reported benchmarks via pool**: Terminal-Bench 2.1 70.2%, SWE-Bench Pro 59.4%, DeepSWE 40.4%. Trajectories published at trajectories.poolside.ai — more transparent than typical lab releases, but independent replication is pending
- **Hardware floor**: ~236GB BF16 at 4x tensor-parallel for vLLM serving; "runs on a single DGX Spark" is single-node data-center hardware, not consumer deployment
- **OpenMDW-1.1 license**: permits commercial use and modification; integrations with Hermes Agent, Cline, OpenCode, Kilo, and pi.dev listed in official docs

## Why clawfit should care

Poolside benchmarks the model inside pool and ships pool with the weights — the current `llms.json` / `agents.json` separation does not accommodate this coupling. A `recommended_harness` linking field is absent from the registry schema. OpenRouter pricing ($0.10/$0.20 per 1M) makes Laguna S 2.1 viable for `budget: medium` + `task: code-gen` profiles without self-hosting — the first open-weight model in this apparent capability tier at that price point. Schema gaps also include `active_params_b` and `total_params_b` for MoE cost disambiguation, flagged previously for Qwen3-Coder-Next.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base LLM** (primary: open-weight MoE backend; maps to `llms.json`)
- **Level 2 — Harness / Wrapper** (secondary: pool ships alongside as the official eval scaffold and user-facing agent; not embedded in the model weights — a separable L2 companion)

## Status

- First signal; `llms.json` candidate pending: (a) independent benchmark replication outside pool harness, (b) OpenRouter pricing stability. Schema gaps: `active_params_b`, `total_params_b`, `recommended_harness`. ref-levels.md: simultaneous model-plus-harness release is a new L1/L2 coupling pattern — flag for next review cycle, no modification this run.
