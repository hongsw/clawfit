# Research Watch: DeepSeek Search & Fetch API — First-Party LLM Provider Grounding API at $0.75/1000

- Repo/Link: https://api-docs.deepseek.com/guides/search/
- Source: Hacker News front page (443pts, 214 comments, 2026-10-18)
- Stars: N/A (API product, not an OSS repo)

## Why this is worth watching

DeepSeek has launched a paid search+fetch grounding API directly within its own LLM API surface. At 443pts and 214 HN comments, this is one of the highest-traction API announcements of the week. The architectural novelty is that grounding is now a **first-party LLM provider service** — the same credential, the same billing, the same endpoint family — rather than a third-party retrieval pipeline the developer must wire up separately. This creates a new category distinct from both RAG architectures (developer-managed vector stores + retrieval) and general-purpose web search APIs (Google Custom Search, Bing, Tavily, Exa) that are stitched in at the application layer.

## What stands out immediately

- Two raw JSON endpoints: `POST /v1/tools/search` (structured results with relevance scores, authority tiers, dual snippets) and `POST /v1/tools/fetch` (URL → Markdown)
- Pricing: $0.75 per 1,000 successful requests — only HTTP 200 responses with results are billed; failures and empty results are free
- Free for server-side tool calls made through DeepSeek Harness, Claude Code, and Codex until November 1, 2026 (Beijing time) — the three primary harness clients already emit these calls
- Each result carries two distinct summaries: a `snippet` for UI display and a separate `summary` for model consumption — rare design choice that separates human-facing and model-facing content
- Supports standard search operators (`site:`, `-site:`, exact phrases, `lang:`, `after:`/`before:`) — retrieval precision stays under caller control
- Relevance score (`rerank_score`, 0–3) blends relevance, authority, and freshness; authority tier (0–4) is a separate signal

## Why clawfit should care

DeepSeek models are already in `clawfit/registry/llms.json`. The grounding API changes the effective capability of a DeepSeek LLM triple in clawfit recommendations: a (DeepSeek, DeepSeek-V4, cloud) recommendation now implicitly includes native grounding without a third-party tool. This has two implications:

1. **`network: online` + `task: research` recommendations that currently score DeepSeek models lower due to grounding friction need to be re-examined** — the friction gap vs. models with native search (e.g., Claude models with web search plugins) has narrowed.
2. **First-party vs. third-party grounding is a new `org_fit` dimension** — organizations that want to minimize supply-chain complexity (single vendor, single credential, single cost center) now have a viable alternative to multi-vendor retrieval pipelines.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capability layer** (search+fetch as an MCP-callable or API-callable grounding primitive, first-party within the LLM provider)
- **Level 1 secondary** (changes the effective task performance of DeepSeek base models for `network: online` + `research` tasks)

## Claims to verify

- Whether `rerank_score` and authority tier are calibrated well vs. third-party alternatives (Tavily, Exa, Perplexity Sonar)
- Whether the November 1 billing change for Claude Code + Codex server-side calls is confirmed in official communications
- Actual throughput limits at 5 req/s per account — whether this is sufficient for agentic loop patterns (agents that issue 3–5 grounding calls per step)
- Whether `in-house search engine` is DeepSeek's own crawler or a licensed backend

## Status

- New signal: first tracking entry for "LLM provider-native search+fetch grounding API as a first-party capability"
- Registry eligibility: DeepSeek models already tracked; this is a capability signal, not a new model entry
- 📡 note: first-party LLM grounding APIs (DeepSeek today) vs. third-party RAG pipelines — candidate for a new `grounding_complexity` axis in `org_fit` scoring; relevant for `network: online` + `research` task recommendations
