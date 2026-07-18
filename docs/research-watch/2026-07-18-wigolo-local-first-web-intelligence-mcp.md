# Research Watch: wigolo — Local-First Web Intelligence MCP Server

- Repo: https://github.com/KnockOutEZ/wigolo (⭐1,111)
- Also see: `docs/research-watch/2026-06-26-aws-agent-toolkit-official-mcp-servers.md` (L4c, cloud-native MCP counterpart); `docs/research-watch/2026-07-04-gitnexus-code-intelligence-mcp.md` (L4c, code search MCP); `docs/research-watch/2026-07-18-browser-rs-mcp-multi-agent-stealth-browser.md` (today's L4c browser signal)
- Source: GitHub Trending (All Languages, rank 9), 2026-07-18

## Why this is worth watching

Most web search MCP servers for AI agents (Tavily, Exa, Serper) require a paid API key and route queries through a cloud provider. wigolo routes 18 direct search-engine adapters through the user's local hardware with no API key and $0/query cost. The practical implication for clawfit: for agent profiles where `network: offline` or `budget: $0.00` are filters — research tasks on air-gapped machines or cost-constrained deployments — the cloud-search MCP tier returns no results. wigolo is the first tracked tool that directly fills this gap in the L4c research capability cluster.

## What stands out immediately

- **10 MCP tools covering the full research workflow:** search, fetch, crawl, extract, cache, find_similar, research (multi-step synthesis), agent (autonomous loop), diff, watch — the only comparable tool with comparable breadth is the AWS agent toolkit, which is cloud-native and requires AWS credentials
- **18 direct search engine adapters with rank fusion:** not a single-endpoint wrapper; combines results across engines with ML-based reranking and per-result explainable scores (semantic + lexical + engine-consensus components) — the explainability claim is architecturally non-trivial and requires independent verification
- **Tiered fetch escalation:** lightweight HTTP first, escalates to in-process headless browser pool for JS-heavy pages without user configuration — removes manual tool-selection overhead that other fetch MCP tools place on the agent
- **~1.5 GB disk footprint:** on-device ML models for reranking; this is not a zero-footprint lightweight server; the disk requirement may be prohibitive for memory-constrained local hardware profiles
- **`robots.txt` compliance and per-domain rate limiting:** built-in; most crawl/scrape MCP tools defer this to the agent; enforcement at the server layer reduces agent policy-violation risk
- **AGPL-3.0-only license:** free to use and self-host commercially, BUT: copyleft obligation triggers if modified and run as a network service (published changes must be AGPL-licensed). For enterprise or commercial deployments that modify and serve, this is a meaningful legal constraint not present in MIT/Apache-2.0 alternatives.
- **Available via npm, PyPI, Docker, Homebrew, MCP Registry:** widest distribution surface in the L4c research cluster; reduces setup friction
- **Created Apr 2026, pushed Jul 18, 2026:** active 3-month project with sustained development; public beta status

## Why clawfit should care

For the `network: offline` + `task: research` profile intersection, clawfit currently has no capable MCP search tool in the L4c cluster (cloud tools require internet; browser MCP servers are not search tools). wigolo is the first clean match. However, the AGPL license and ~1.5 GB on-device footprint introduce constraints that do not exist for cloud-search alternatives:

- `governance_need: standard` profiles (enterprise) may exclude AGPL due to copyleft risk on modification
- Hardware profiles below the local workstation tier (e.g., constrained local) may not accommodate 1.5 GB for MCP server alone on top of model weights and agent runtime

The `research` tool (multi-step question decomposition + synthesis) and `agent` tool (autonomous search loop) also represent a capability level above what most L4c MCP servers expose — these are closer to L2 (harness behavior) packaged as MCP tools, which is architecturally interesting and potentially confusing to classify.

## Preliminary interpretation

Current best reading:
- **Level 4c — Web intelligence MCP server (primary):** 10-tool MCP server exposing web search, crawl, fetch, and research as named capabilities; agents consume these as standard MCP tool calls; same layer as chrome-devtools-mcp, GitNexus, AWS agent toolkit
- **Weak Level 2 secondary (research and agent tools only):** the `research` and `agent` MCP tools internalize multi-step planning and sub-query decomposition — behaviors that belong at L2 — but wrapped inside a single MCP call from the agent's perspective; the harness behavior is internal, not exposed as an orchestration API

## Claims to verify

- The 18-engine rank fusion and ML reranking quality versus single-engine cloud alternatives (Tavily, Exa) on research-task recall — the "explainable" scoring claim specifically requires independent benchmarking
- The AGPL copyleft scope in practice: whether running wigolo via Docker as a shared MCP server for a commercial team constitutes "running as a network service" for AGPL purposes (likely yes, which matters for enterprise profiles)
- Whether the on-device ML reranking models add latency that makes `latency: low` profiles impractical
- robots.txt enforcement: whether it is configurable off for legitimate scraping use cases

## Status

- 1,111 stars, public beta — below the 5,000 registry threshold; AGPL license constraint and unverified performance versus cloud alternatives preclude registry addition. Two-signal watch: this is the first local-first web intelligence MCP server in the tracking log; a second independent tool filling the same (`network: offline`, `task: research`) slot would confirm the sub-type for L4c. Schema watch: `search_backend: [cloud-api | local-engine-adapters | hybrid]`; `license_copyleft: [none | agpl | gpl]`; `offline_capable: true/false`.
