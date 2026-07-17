# Research Watch: Sourcebot — Self-Hosted Codebase Intelligence for Humans and Agents

- Repo: https://github.com/sourcebot-dev/sourcebot (⭐3,592)
- Source: GitHub Trending TypeScript (2026-07-17); v5.1.2 released July 16, 2026

## Why this is worth watching

Sourcebot is a self-hosted code intelligence platform explicitly designed for both human developers and AI agents — the dual-audience framing ("helps humans and agents understand your codebase") is architecturally significant. Most code indexing tools in the agent ecosystem are designed with humans as the primary consumer and agents as second-class integration targets (e.g., tree-sitter grammars, semantic search via embeddings). Sourcebot inverts this by treating agents as a first-class query interface: natural language Q&A with inline citations, regex code search, and IDE-level cross-repo navigation are all reachable programmatically. The v5.1.2 release on July 16, 2026 (yesterday) and 154 total releases indicate sustained active development, and the 3.6k star count exceeds the 100-star tracking threshold.

## What stands out immediately

- **Explicit dual-audience design**: "helps humans AND agents understand your codebase" — not retrofitted AI integration but stated primary design target
- **Natural language Q&A with citations**: "Ask Sourcebot" returns detailed codebase answers grounded with inline source citations — citation grounding reduces hallucination risk for agent consumers
- **Cross-repo search**: fast regex search across all connected repositories from a single query surface, relevant for multi-repo monorepo migrations and large org codebases
- **IDE-level goto-definition and find-references across all repos**: symbol intelligence spanning repository boundaries — not just file-level grep
- **Self-hosted via Docker Compose**: no cloud dependency; fully compatible with `data_sensitivity: confidential` profiles
- **v5.1.2 released July 16, 2026**: active major version series (5.x), 154 total releases — not a prototype
- **TypeScript 97.8%**: well-typed codebase, low-friction contribution and extension path

## Why clawfit should care

Sourcebot occupies a gap in the clawfit L5 landscape: it is a persistent code intelligence layer that agents can query at runtime rather than re-indexing at session start. Existing L5 entries (mem0, TencentDB-Agent-Memory, cognee, GBrain) focus on general conversation memory or structured fact storage; Sourcebot is specialized for code structure — the dominant knowledge type in coding agent tasks. For profiles with `task: code-gen` or `task: qa` and large or multi-repo codebases, a tool like Sourcebot as a backing service would reduce per-session context window pressure significantly. The `data_sensitivity: confidential` + `network: offline` compatibility is a direct fit for the `offline_mid_codegen` profile segment that currently has limited options. Additionally, the cross-repo navigation capability (goto-definition across repo boundaries) addresses a concrete gap in existing coding agents that operate within single-repo context windows.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory / Context** (primary): persistent code intelligence store that agents query at runtime; acts as external codebase working memory
- **Level 4 — Capability** (secondary): the "Ask Sourcebot" natural language interface functions as an agent tool or MCP server endpoint in practice

## Claims to verify

- MCP server interface: whether Sourcebot exposes an MCP-compatible endpoint for agent tool-calling, or requires custom integration code
- Latency at scale: cross-repo goto-definition and NL Q&A response times on large multi-repo setups not benchmarked
- Offline completeness: whether Docker Compose deployment can run fully air-gapped (no external model API for the NL Q&A layer) or requires a cloud LLM endpoint
- Citation grounding accuracy: "grounded with inline citations" — whether citations are code-location references or summarized paraphrases
- Agent SDK: programmatic access API for agent tool integration vs. human UI only

## Status

- 3,592 stars (above 100-star threshold); v5.1.2 released 2026-07-16 — active, timely
- Registry ineligible: no direct schema match in agents.json/llms.json/hardware.json (code intelligence infrastructure, not an agent type or hardware tier)
- Schema watch: `code_intelligence_backend: true/false`; `cross_repo_navigation: true/false`; `agent_query_api: [none | rest | mcp]`
- Watch: MCP integration and offline LLM backend support would make this a strong L5 registry candidate
