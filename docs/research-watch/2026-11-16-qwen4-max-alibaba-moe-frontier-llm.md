# Research Watch: Qwen4-Max — Alibaba Frontier MoE Release (2.4T/71B, Native Vision, 1M Context)

- Repo/Link: https://qwen.ai/blog?id=qwen4-max
- Source: Hacker News front page (800 pts, 2026-11-16)
- Stars: N/A (hosted model; released today)

## Why this is worth watching
Alibaba released Qwen4-Max today with 2.4 trillion total parameters, 71B active parameters per token, native vision encoding, and a one-million-token context window. At $1.50/$4.50 per million tokens, it undercuts many equivalent-tier models by over 60% on a claimed cost-per-task basis. The DeepSWE v1.1 score (75.7%) places it in the same tier as Claude Opus 5.5 (74.2%) and GPT-6.1 Sol (75.2%) on the leading agentic coding benchmark. This is the full release after the August 2026 preview tracked at `2026-08-26-qwen3-8-flash-next-qwen4-preview-moe.md`.

## What stands out immediately
- MoE architecture: 2.4T total / 71B active — sparse activation means billing and latency scale to active params, not total
- Native vision encoder (not a bolted-on multimodal wrapper): understands images natively, relevant for computer-use and UI-automation agents
- 1M-token context confirmed in production (not just benchmark-claimed); relevant for long-running agents over large codebases
- DeepSWE 75.7% puts it at parity with Opus 5.5 (74.2%) and GPT-6.1 Sol (75.2%) on the most credible agentic coding benchmark
- Specific weaknesses confirmed: Terminal-Bench 4.0 at 48.5% (vs Kimi K3.1 at 67.2%) and ProgramBench at 31.5% (vs Opus 5.5 at 65.0%) — these are not minor gaps
- Work360 benchmark (Alibaba's own): 52.69 vs 47.74 for Qwen3.8-Max — relative improvement notable but benchmark is vendor-designed
- Pricing: $1.50/M input, $4.50/M output — below Opus 5.5 and GPT-6.1 Sol at similar DeepSWE tiers
- Multiple independent speed reports describe it as slow per step compared to Opus 5.5; Artificial Analysis index score 43 vs Kimi K3.1 Pro 46

## Why clawfit should care
Qwen4-Max enters the registry-eligible tier at input pricing comparable to or below current mid-tier entries. At $1.50/M input, it falls within reach of the `budget: medium` filter axis. The native vision capability directly expands its surface for `task: ui-automation` and `task: computer-use` recommendation paths, which currently have limited LLM options. The Terminal-Bench weakness (48.5%) is a concern for `task: code-gen` profiles that heavily use shell interaction. This is the fourth frontier MoE entry within two months (Reflection Beam, Mistral Large 4, Kimi K3.1 Pro previously) — the sub-10B-active-params pattern is becoming a parallel track distinct from the 71B-active-params frontier tier.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base LLM** (MoE frontier model with explicit agentic benchmark scores)
- No secondary layer: this is a pure model entry

## Claims to verify
- $1.50/$4.50 pricing confirmed as GA pricing, not preview discounts
- 1M-token context in practice (not just advertised maximum) — test with actual agent sessions
- Terminal-Bench 4.0 scores from multiple independent testers (currently only Vals and MarkTechPost reporting)
- ProgramBench gap (31.5% vs Opus 5.5 65.0%) is very large — verify this isn't a benchmarking artifact
- Whether native vision is genuinely fused (vs. separate vision prefix encoding that degrades on mixed image-text reasoning)

## Status
- First scan: 2026-11-16
- Registry action: **eligible for review** — pricing publicly available ($1.50/$4.50), context window confirmed (1M), DeepSWE benchmark published; active parameter count (71B) maps to `latency: medium` scoring; `task: ui-automation` capability adds a new recommendation path
- Open question: Terminal-Bench weakness may warrant a `task_exclusion: terminal-intensive` annotation if the gap is confirmed by third-party testing
- 📡 Note: Qwen4-Max is the third frontier-class open-weight MoE with explicit agentic benchmarks in Nov 2026 (Kimi K3.1 Pro Nov-14 is prior) — if a fourth appears this month, that would constitute a signal for a November 2026 frontier MoE cohort entry in the L1 canonical section, parallel to the October 2026 cohort (Reflection Beam + Mistral Large 4)
