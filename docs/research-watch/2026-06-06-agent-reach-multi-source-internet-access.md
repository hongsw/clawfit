# Research Watch: Agent-Reach — Give AI Agents Eyes to See the Internet

- Repo/Link: https://github.com/Panniantong/Agent-Reach
- Source: GitHub Trending
- Stars: ~21,500

## Why this is worth watching
Agent-Reach gives any MCP-compatible AI agent read access to Twitter/X, Reddit, YouTube, GitHub, Bilibili, and XiaoHongShu (Little Red Book) via a unified tool interface. At 21k stars it is well past the registry threshold, and targeting social platforms (not just the open web) is structurally distinct from browser-use tools that automate Chrome.

## What stands out immediately
- Six platform integrations: Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu
- MCP server interface — any MCP-compatible agent (Claude Code, Cline, Cursor) gets these as native tools
- Python backend; stateless search-and-fetch (no login/oauth for most endpoints)
- Read-only by design: no posting, commenting, or write actions
- Especially significant for non-Western markets: Bilibili and XiaoHongShu coverage is rare in Western agent tooling
- 21.5k stars in trending — suggests strong community pickup

## Why clawfit should care
For `role: researcher` and `task: research` profiles, access to social platforms is often required alongside web search. Agent-Reach is a first-class L4 capability that a researcher-profile recommendation should flag. The non-Western platform coverage (Bilibili, XiaoHongShu) matters for clawfit's global scoring ambitions. Second independent signal (after `last30days-skill`) for cross-platform social media research as an L4 capability sub-type.

## Preliminary interpretation
Current best reading:
- **Level 4 primary — Tool-use / Capability layer**: Agent-Reach adds discrete social-platform read tools to any agent's tool-call surface; does not orchestrate agents or manage memory.
- Sub-type: **multi-platform social media reader** (distinct from open-web browsing at L4c).

## Status
- **Held for registry promotion**: 21k★ exceeds threshold; MCP integration needs installation verification (does `pip install agent-reach && mcp install` work cleanly?); read-only design claim needs verification for Twitter/X. Registry candidate for `task: research` + `role: researcher` + `network: online` + `data_sensitivity: internal/public`.
