# Research Watch: OpenAI GPT-5.6 — Sol/Terra/Luna Three-Tier Model Family GA

- Repo/Link: https://openai.com/index/gpt-5-6/
- Source: OpenAI announcement / Hacker News front page (1444 pts)

## Why this is worth watching
GPT-5.6 is OpenAI's first model family structured as three named tiers (Sol/Terra/Luna) with explicit per-tier pricing and a shared 1.05M context window. The pricing discipline is notable: Luna and Terra are direct competitors for Claude Sonnet and Haiku in the cost-sensitive midrange. More structurally important: MCP is listed as a first-class built-in capability alongside hosted shell, apply patch, code interpreter, and Skills — meaning GPT-5.6 agents natively consume the same protocol ecosystem that clawfit already tracks.

## What stands out immediately
- Three-tier structure: Sol (flagship, $5/$30/1M), Terra (balanced, $2.50/$15/1M), Luna (fast/cheap, $1/$6/1M) input/output
- Shared 1.05M context window and 128K max output across all three tiers — no trade-off on context for cost
- API model IDs: `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`; bare `gpt-5.6` routes to Sol
- Knowledge cutoff February 16, 2026 (same across all three)
- MCP, Skills, hosted shell, apply patch, code interpreter, computer use, tool search: listed as supported by all three — not Sol-only
- Launched July 9, 2026 with GitHub Copilot integration same day; global rollout in 24h
- ChatGPT Work agent launched simultaneously on same model family (separate signal)
- Luna pricing ($0.001/1k input) undercuts gpt-4o-mini ($0.00015) by 6.6× at quality parity claims — unverified

## Why clawfit should care
The clawfit LLM registry currently has gpt-4o ($0.0025/1k) and gpt-4o-mini ($0.00015/1k) as the sole OpenAI entries. GPT-5.6 introduces three directly registerable tiers that map cleanly to the existing latency/cost axes. Terra ($0.0025/1k) matches gpt-4o's input price at claimed superior quality. Luna ($0.001/1k) fills a medium-cost tier currently absent from the OpenAI column in clawfit's scoring. Sol ($0.005/1k) is a high-end flagship tier between claude-sonnet ($0.003) and claude-opus ($0.015). The 1.05M context window is the largest in the registry — relevant for profiles with `tasks: research` + `data-analysis`. MCP native support means any `network: online` agent in the registry can call these models as MCP tool providers.

## Preliminary interpretation
- **LLM base layer** (primary) — below the L1–L7 taxonomy but foundational to all layers
- **L4c secondary** (MCP-native tool consumer/provider capability built in, not via third-party wrapper)
- Three distinct scoring tiers; Luna and Terra are mid-range registry gaps currently

## Claims to verify
- Luna's claimed quality parity with GPT-4o mini has not been independently benchmarked at time of writing
- MCP depth: whether all three tiers support MCP equally or Sol gets privileged MCP features (release notes ambiguous)
- `gpt-5.6` bare alias: confirm routing behavior before using in production pipelines

## Status
- Registry candidate: **Yes, all three tiers** — public deterministic pricing, schema maps cleanly to llms.json (id, tasks, latency, cost_per_1k_tokens, context_window, network)
  - `gpt-5.6-sol`: latency=high, cost_per_1k_tokens=0.005, context_window=1050000
  - `gpt-5.6-terra`: latency=medium, cost_per_1k_tokens=0.0025, context_window=1050000
  - `gpt-5.6-luna`: latency=low, cost_per_1k_tokens=0.001, context_window=1050000
- Phase 4 decision: add all three to llms.json (official GA, deterministic pricing, no prior entries)
