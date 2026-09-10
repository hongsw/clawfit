# Research Watch: DeepSeek V4.1 Flash — Official Release Confirms $0.003/M Input Pricing

- Repo/Link: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash (⭐1,170 HF likes)
- Source: Hacker News (801 pts, 447 comments) + API changelog

## Why this is worth watching
DeepSeek V4.1 Flash launched officially on September 10, 2026, with confirmed pricing at $0.003 per million input tokens. The previous scan (2026-09-09) flagged this as "limited beta, planned Sept 10 — no confirmed pricing or benchmarks yet." Today's official release resolves that uncertainty: pricing is now deterministic and publicly documented. At $0.003/M input, this is among the lowest confirmed pricing for a frontier-class multimodal MoE model. The announced transition (all deepseek-v4-pro traffic rerouted to V4.1 Flash at V4.1 Flash pricing from September 14) makes this the de facto DeepSeek Pro replacement.

## What stands out immediately
- $0.003 per million input tokens — confirmed public pricing on launch day; this is the primary registry-relevant data point
- 552B backbone MoE parameters; native multimodal (text + image + speech in a single architecture, not separate towers)
- 1M-token context window
- KV Cache HBM requirement reduced to 1/4 vs. previous generation; SSD requirement reduced to 1/8 — significant self-hosted inference efficiency improvement
- "Comprehensively surpassed V4 Pro in performance, cost, speed, and total time" per internal + external testing — benchmarks not publicly listed in the announcement
- Effective from Sept 14: all `deepseek-v4-pro` API requests routed to V4.1 Flash and billed at V4.1 Flash pricing — this is a deprecation, not a parallel offering
- HF model page updated Sept 10 at 08:18 UTC; 1,170 HF likes at the time of capture
- 427 tokens/second throughput reported in earlier limited-beta coverage (Sept 9)

## Why clawfit should care
The confirmed pricing at $0.003/M input tokens is directly actionable for the registry and for `budget` dimension scoring. The existing `deepseek-v4-flash` registry entry (representing V4 Flash, the prior generation) carries a different cost basis. V4.1 Flash at $0.003/M input is meaningfully cheaper than V4 Pro on a per-token basis and is now the official replacement for that slot.

The Sept 14 rerouting announcement also means any existing recommendation that routes to `deepseek-v4-pro` will transparently switch model behavior — a compatibility consideration for `statefulness: session` profiles where model personality consistency matters. clawfit's registry currently lists both `deepseek-v4-pro` and `deepseek-v4-flash` as separate entries; the V4.1 Flash launch effectively deprecates V4 Pro and updates the cost floor for the Flash tier.

The native multimodal architecture (single model handling text, image, speech) is also relevant: it signals that the `modality` gap in `llms.json` will become more pressing as multimodal becomes the default rather than the exception across frontier MoE models.

## Preliminary interpretation
- **Level 1 — Base Model** (primary: LLM substrate for agentic inference, now confirmed multimodal)
- No harness layer from DeepSeek directly; third-party harnesses at L2

## Claims to verify
- "$0.003 per million input tokens" — confirm output token pricing; the announcement mentions input pricing specifically; output pricing not yet confirmed in the sources reviewed
- "Comprehensively surpassed V4 Pro" — no benchmark table published in the announcement; independent SWE-bench / Terminal-Bench results pending
- 427 tok/s throughput — was from limited-beta coverage; confirm on production infrastructure
- KV Cache 1/4 HBM claim — relevant for self-hosted inference capacity planning; no independent hardware validation yet
- Sept 14 rerouting — confirm whether this applies to all regions and whether output pricing changes simultaneously

## Status
- Signal strength: very high — HN 801 pts, confirmed launch, confirmed pricing
- Registry eligibility: CONDITIONAL — pricing confirmed ($0.003/M input tokens); however V4.1 Flash is not a standalone GitHub repo (HF model page only, 1,170 likes, below 5k threshold); output pricing not yet confirmed; full benchmark table absent; decision deferred until output pricing and independent benchmarks land
- Immediate action: update reference-levels.md with confirmed pricing; monitor Sept 14 V4 Pro rerouting confirmation; watch for independent benchmark results
- Context: existing `deepseek-v4-flash` and `deepseek-v4-pro` registry entries are now the prior generation; neither entry needs changes today — V4.1 Flash is a separate model
