# Research Watch: turbo-fieldfare — Gemma 4 26B Inference in 2 GB RAM via SSD Expert-Streaming

- Repo: https://github.com/drumih/turbo-fieldfare (⭐571)
- Source: Hacker News front page (326 pts, 2026-07-29) — "Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac"

## Why this is worth watching

turbo-fieldfare is a Swift + Metal runtime that runs Gemma 4 26B-A4B — a 14.3 GB model — on Apple Silicon Macs with as little as 8 GB of RAM by streaming model weights from SSD on demand rather than loading them into memory. The HN engagement (326 pts) is unusually high for a 571-star repo, indicating significant practitioner interest in local inference under hardware constraints. It is a first signal for "sub-2GB RAM inference via MoE expert-streaming on consumer Apple Silicon," a pattern distinct from prior local-inference signals (colibri used disk streaming for larger MoE models; ktransformers used CPU offloading). If this approach generalises, it resets the minimum hardware bar for running capable local models.

## What stands out immediately

- **Expert-streaming at inference time:** weights for a given MoE expert are loaded from SSD only when selected by the router, and evicted after use — steady-state RAM is bounded by the active expert set, not the full parameter count. This is the core architectural claim.
- **Benchmark numbers from 12 committed audit experiments:** 5.1–6.3 tokens/second on M2 MacBook Air (8 GB), 31–35 tokens/second on M5 Pro — a 5–6× throughput gap attributable to memory bandwidth differences between generations.
- **Custom Metal kernels:** inference uses Apple's Metal GPU shader language rather than a general ML framework, giving precise control over memory transfer timing from SSD to GPU.
- **OpenAI-compatible server endpoint:** exposes a local HTTP API, making it drop-in compatible with agent harnesses (Hermes, Claude Code, Codex) that support OpenAI-format tool calls.
- **Tool function calling supported:** not just completion — agent-usable. Functionally positions it as an offline L1 base runtime.
- **Swift + Metal, macOS-only:** tight coupling to Apple's ecosystem narrows deployment scope, but also means zero dependency on CUDA or Python inference stacks.
- **103 documented experiments committed:** reproducibility is baked in; benchmarks are not marketing claims but committed artifacts.

## Why clawfit should care

clawfit's hardware registry treats "offline / local" inference as a monolith. turbo-fieldfare demonstrates that the relevant distinction is not just "offline vs. cloud" but "memory-resident vs. SSD-streamed." A 8GB Mac is currently classified as unable to run capable models; if expert-streaming matures, that assumption breaks.

Two concrete implications:
1. The `hardware` dimension may need a new tier: `ssd-streamed` or `memory-constrained` — distinct from `edge` (which implies dedicated inference hardware) and `cloud`.
2. The `latency: low` filter would need to account for SSD I/O latency: 5 tokens/second on M2 is below what most agents need for interactive use, but may be acceptable for batch tasks.

The Gemma 4 architecture is specifically MoE (Mixture of Experts), which makes expert-streaming feasible; dense models cannot benefit from this pattern. This is therefore a Gemma-family-specific technique that may generalise only to other large MoE models.

## Preliminary interpretation

Current best reading:
- **Level 7 — Infrastructure / inference substrate** (primary): this is a specialized inference runtime for a specific hardware class
- **Level 1 secondary:** functions as a base runtime for agents via its OpenAI-compatible server

Not L2+: turbo-fieldfare provides no harness features, orchestration, or skills — it is the inference engine only.

Cross-watch: colibri (2026-07-21) — consumer-hardware MoE inference via C; ktransformers (2026-07-19) — CPU-GPU heterogeneous inference. turbo-fieldfare is the Apple-native variant of the same pressure: "run big models where they weren't supposed to run."

## Claims to verify

- Whether the 2 GB RAM figure is steady-state during inference or peak-at-load; the distinction matters for 8 GB hardware with macOS overhead
- Whether tool function calling passes standard agent benchmark suites (not just single-call accuracy)
- Whether the expert-streaming approach introduces meaningful prompt-processing latency beyond the per-token generation numbers
- Whether Gemma 4 26B-A4B (4-billion activated) quality is degraded by quantization applied during streaming vs. full-weight FP16

## Status

- First signal. 571 stars is above threshold; 326 HN points is strong independent validation. Early-stage repo (12 commits).
- Registry consideration: too early — no deterministic cost/latency data across hardware classes; throughput numbers vary 5× between M2 and M5 Pro. Monitor for: stable throughput benchmarks; whether the pattern is adopted by other runtimes; whether Apple Silicon hardware tier needs explicit modelling in clawfit.
- Open question: does expert-streaming on NVMe SSDs degrade token quality through partial-weight access patterns, or is this purely a latency/RAM trade-off?
