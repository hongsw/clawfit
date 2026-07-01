# Research Watch: OmniRoute — Multi-Provider LLM Gateway with MCP/A2A

- Repo: https://github.com/diegosouzapw/OmniRoute
- Also see: docs/research-watch/2026-04-06-rtk-token-proxy.md (RTK compression engine, now bundled inside OmniRoute's 9-engine stack)

## Why this is worth watching
OmniRoute aggregates 231+ AI providers behind a single OpenAI-compatible endpoint, couples that with 17 routing strategies and a 9-engine token compression stack, and now exposes both MCP and A2A protocol surfaces — making it a candidate for the infrastructure layer that sits *beneath* tools like Claude Code, Cursor, and Cline rather than alongside them. At 8,500 stars with 271 releases and v3.8.42 shipping June 30, 2026, this is an actively maintained project at practitioner scale, not an experimental proof-of-concept. The explicit, first-class integration with coding agents (one-command `omniroute setup-cursor` style bootstrapping) marks it as infrastructure-layer tooling with a strong pull toward becoming a default routing substrate.

## What stands out immediately
- **Single local endpoint** at `http://localhost:20128/v1` with OpenAI-compatible API translation — any conforming tool redirects without code changes
- **17 routing strategies** including Auto-Combo (9-factor scoring: health, quota, cost, latency, success rate), context-relay for long-context handoffs, and Fusion fan-out/synthesis — this is not simple round-robin
- **9-engine token compression pipeline**: Session-Dedup, CCR, RTK, Caveman, LLMLingua-2, Headroom, Lite, Aggressive, Ultra — stacked RTK+Caveman achieves 78–95% savings; code blocks and structured data preserved byte-exact
- **MCP support**: 87 built-in tools across stdio/HTTP/SSE transports, 30 permission scopes with audit trail — works as an MCP server for Claude Desktop and Cursor
- **A2A support**: JSON-RPC 2.0 over SSE with 6 skills for autonomous gateway control; agents can programmatically manage routing, cache, and memory through the gateway
- **~1.6B free tokens/month** aggregated across 50+ free-tier providers; compression doubles effective quota
- **Zero telemetry, local credential encryption** — credentials never leave the host; security posture is an explicit product decision
- **16+ explicit coding-agent integrations**: Claude Code, Cursor, Copilot, Cline, Continue, OpenCode, Kilo Code — per-tool setup guides documented
- **Cross-platform delivery**: npm, Docker, Electron desktop, Android Termux, PWA — deployment surface is unusually wide for a local proxy

## Why clawfit should care
OmniRoute represents a new structural position in the ecosystem: a *local routing substrate* that sits between the user's AI tools and the LLM providers, invisibly reshaping both cost and reliability. clawfit's scoring model treats (agent, llm, hardware) as the three axes of a recommendation, and assumes the LLM endpoint is a direct, static binding. A gateway like OmniRoute decouples those axes — the "LLM" a user actually hits becomes a runtime decision made by the gateway, not a configuration choice made at recommendation time. This has two concrete consequences: first, the cost axis in clawfit's scoring becomes a floor estimate rather than a fixed value, since compression and free-tier stacking can reduce effective cost dramatically; second, the hardware axis gains a new variant (local-gateway) that is distinct from both cloud and fully-local inference. The RTK engine (previously tracked as a standalone tool in docs/research-watch/2026-04-06-rtk-token-proxy.md) is now bundled inside OmniRoute — a consolidation signal worth noting for registry hygiene.

## Preliminary interpretation
Current best reading:
- **Level 7 — Infrastructure / hardware / edge** (local proxy substrate that mediates all LLM traffic below the agent layer, with explicit cross-platform and edge-deployment targets)
- Secondary: **Level 5 — Memory / MCP / context layer** (MCP server with 87 tools, A2A protocol surface, and session-level context compression/deduplication)
- The Level 2 (harness/orchestration) framing the preliminary signal suggested is plausible but too shallow: OmniRoute does not orchestrate agents — it routes and compresses the traffic *underneath* them, which is structurally Level 7

## Status
- First signal — 2026-07-01; 8,500 stars, active release cadence (271 releases), explicit clawfit-adjacent integrations; promote to registry evaluation when team confirms whether local-gateway should be a distinct hardware axis value
