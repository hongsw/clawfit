# Research Watch: Firecrawl — Agent Data Infrastructure

- Repo/Link: https://github.com/firecrawl/firecrawl
- Source: GitHub Trending

## Why this is worth watching
Firecrawl positions itself as purpose-built data infrastructure for AI agents: a single API surface covering web search, scraping, and 550+ data providers at 204k stars. Its agent-first framing (rate-limiting, retries, structured output) distinguishes it from general scraping libraries. At 204k stars it has crossed the threshold from experiment to infrastructure dependency.

## What stands out immediately
- 204k total stars, 825 gained today — consistently high adoption
- One API key routes to 550+ data providers (news, finance, weather, public records, search)
- Structured output mode: returns JSON rather than raw HTML, reducing agent token overhead
- Explicit agent-mode: handles retries, pagination, and de-duplication
- Self-hostable; also available as a managed API

## Why clawfit should care
Agents that need real-world data (research, QA, monitoring) depend on a capability tool like Firecrawl. It sits squarely in the L4 capability layer (tools the agent uses) and directly maps to `task: research`, `task: data-analysis`. Its `network: online` requirement and managed/self-hosted split are relevant to the `network` and `governance_need` scoring axes. Registry entry should be evaluated: 204k stars confirms adoption; schema needs `capability_type: data-access` annotation.

## Preliminary interpretation
Current best reading:
- **Level 4 — Agent Capability Infrastructure** (data access / scraping layer)

## Status
- First scan at this star count (204k) on GitHub Trending 2026-11-20
- Registry entry deferred: schema needs `capability_type` field; no deterministic per-task latency data
- 📡 Watch: if a second major agent-data-infrastructure tool crosses 100k stars with similar structured-output framing, a canonical L4 "agent data access" sub-type is justified
