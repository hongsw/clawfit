# Research Watch: MiniMax-M3 — Low-Cost Frontier LLM

- Repo/Link: https://www.minimax.io/blog/minimax-m3
- Source: GeekNews ("MiniMax-M3 데뷔") — venturebeat.com article

## Why this is worth watching
MiniMax-M3 (released 2026-06-01) claims frontier-tier coding performance at 5–10% of comparable closed-model cost: $0.60/$2.40 per million input/output tokens vs. Claude Opus 4.7 at $5/$25 — an 8–10x price gap on list rates. Open weights are committed for release within 10 days of launch, which would make it the first open-weight model combining a 1M-token context window, native multimodality, and frontier-competitive code benchmarks in a single artifact. If open weights land and independent evaluations hold up, this is a meaningful shift in the cost curve for any `task: code-gen` profile.

## What stands out immediately
- Architecture: MSA (MiniMax Sparse Attention) — reduces per-token compute at 1M context to 1/20th of the prior generation; 9x faster prefill, 15x faster decoding vs. M2
- Context window: 1,000,000 tokens — matches DeepSeek V4-Pro/Flash already in `llms.json`; exceeds GPT-4o (128k) and Claude Opus/Sonnet (200k)
- Benchmark claims (vendor-authored, not independently verified at time of capture): SWE-Bench Pro 59.0% (above GPT-5.5 and Gemini 3.1 Pro; below Opus 4.8 69.2%); BrowseComp 83.5% (above Opus 4.7 79.3%); Claw-Eval #1 among tested models; Terminal-Bench 2.1 66.0% (trails Opus 4.8 74.6%)
- Pricing confirmed via API: $0.60/M input (≤512K context), higher rate above 512K; $2.40/M output; ~$0.30/$1.20 promotional rate on OpenRouter at launch
- Native multimodality: text, image, video input plus desktop computer operation
- Delivery: API + monthly token subscription plans ($20/$50/$120); open weights pending on Hugging Face/GitHub
- TechTimes flagged benchmark methodology as unverified — the SWE-Bench Pro and BrowseComp results are vendor-self-reported comparisons

## Why clawfit should care
The current `llms.json` has one low-cost frontier-adjacent entry for code-gen at 1M context: DeepSeek V4-Pro (`cost_per_1k_tokens: 0.000435`). MiniMax-M3 at $0.00060/1k tokens input lands between DeepSeek V4-Pro and claude-sonnet in cost, but claims substantially higher coding benchmark scores. For `task: code-gen` + `latency: medium` + `budget: 0.001` profiles, M3 would score differently from any current entry: the cost weight (0.25) would favor it over claude-opus and claude-sonnet, while the LLM preference weight (0.15) cannot yet be set without stable benchmark evidence. The open-weight release also opens a `network: offline` classification path that no current high-capability code-gen LLM in the registry supports — that would be a new cell in the recommendation matrix.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtimes / primary agent surfaces** (LLM-axis sub-entry; note: the suggested "Level 0" in the source signal does not exist in the reference taxonomy — the closest home for base LLMs is L1, where prior frontier model entries such as Kronos/financial models appear on the LLM axis)

## Status
- Registry candidate, conditional: open weights not yet released; benchmark scores are vendor-self-reported and flagged as unverified by independent press. Hold for registry entry until (1) open weights land on Hugging Face and latency data is independently measurable, and (2) at least one third-party SWE-Bench Pro evaluation confirms the 59.0% figure. Cost data ($0.60/$2.40 per million tokens) is API-confirmed and meets the registry bar. Revisit within 2 weeks of open-weight release.
