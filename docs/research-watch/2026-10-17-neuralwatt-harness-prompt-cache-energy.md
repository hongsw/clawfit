# Research Watch: Neuralwatt — Harness Prompt-Cache Management as Energy/Token Efficiency Dimension

- Repo/Link: https://neuralwatt.com/news/why-harnesses-matter-for-energy-efficiency
- Source: Hacker News front page

## Why this is worth watching
Neuralwatt publishes the first quantified, production-scale analysis showing that harness design—not model or hardware—determines prompt-cache hit rates and therefore inference energy costs. Cache hit rates varied from 1.6% to 11.1% across popular open-source clients; a request with under 10% cached prompt used roughly 2× the energy of a fully-cached one.

## What stands out immediately
- **Harness is the independent variable**: all 65 cache breaks identified across 539 scripted follow-up requests originated in the harness, not the chat template or the model.
- **Specific harness bugs quantified**: OpenCode 1.x plan-mode reminder caused per-turn re-reads; omp pruning and MCP server insertion mid-list each broke cache; reasoning-effort changes near the prompt start caused 61% cache-miss rates.
- **Energy costs**: 140% prefill overhead on GLM-5.3 and 91% on DeepSeek V4.1 Flash for low-cache sessions; deep sessions (128k+) can produce a single turn costing as much as ~600 normal turns.
- **Production-confirmed at 2.8%**: 2.8% of production turns broke the cache when nothing visible changed; the rate jumped to 67% when tool count changed.
- **Session Insights dashboard**: per-turn cache and energy visibility, a first-party inference observability product aimed at harness authors.

## Why clawfit should care
Prompt-cache management is now a measurable harness quality dimension with direct cost implications; clawfit's (agent, llm, hardware) triple scoring currently has no harness-efficiency axis. This is the third harness economics signal (Four Horsemen 2026-10-05: failure patterns; Martin Fowler 2026-10-16: cost/quality crossover by model tier; Neuralwatt 2026-10-17: energy/token footprint) — three signals now converge on harness economics as a missing scoring dimension. The `setup_complexity` metadata field is a poor proxy; a `cache_efficiency` or `harness_quality` dimension would better capture this. The specific harness bugs named (OpenCode, omp, date-in-system-prompt) directly affect tools already in the registry.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / SDK** (primary): prompt-cache management is a harness-layer responsibility
- **Level 7 — Inference Substrate** (secondary): inference energy footprint is substrate-side, but harness behavior drives it

## Status
- First signal for "prompt-cache management as harness quality metric"
- Third harness economics signal overall — three-signal threshold met for candidate `harness_cache_quality` dimension in scoring
- Specific fixes named for OpenCode and omp should be cross-referenced against their registry entries
- Monitor for upstream patches to tracked harnesses (OpenCode, Goose, Cline)
