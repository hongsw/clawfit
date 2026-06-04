# Research Watch: Mnemo — Local-First AI Memory Layer with Knowledge Graph

- Repo/Link: https://github.com/zaydmulani09/mnemo
- Source: Hacker News (Show HN, 22 pts, 2026-06-04)

## Why this is worth watching
Mnemo ships a graph-backed, fully offline memory sidecar with a sub-50ms retrieval benchmark — a combination that distinguishes it from the cloud-API memory cluster (Supermemory, OpenMemory) already in view. More significant than the repo itself is the cluster context: at least three other independently authored projects with overlapping names and goals appeared on HN the same day (mnemon-dev/mnemon, DharmaDhillon/mnemo, GuyMannDude/mnemo-cortex), which suggests the local-first knowledge-graph memory pattern is arriving as a moment, not an isolated project.

## What stands out immediately
- Ships as a single static Rust binary with zero runtime dependencies; SQLite in WAL mode is the only persistence layer
- Entity extraction is LLM-delegated — the sidecar calls back to whichever LLM is configured (Ollama, OpenAI, Anthropic, any OpenAI-compatible endpoint) to extract named entities and relationships; no embedded ML model
- petgraph is held in-process for fast traversal; the SQLite store and in-memory graph are updated atomically, so reads never see a partial write
- 6-stage retrieval: full-text chunk search → entity name search → BFS graph expansion → relation filter → score/rank → assembled context_prompt injection
- Test surface is non-trivial for an early-stage project: 122 Rust unit tests, 21 Python integration tests, 12 benchmarks — suggests engineering-first authorship
- Same-day HN cluster of at least 4 similar repos is a pattern signal; the individual project's 22 pts is weak on its own, but the cluster is not

## Why clawfit should care
clawfit's current L5 memory candidates are differentiated primarily on cloud vs. self-hosted deployment axis (Supermemory as cloud-API anchor; headroom as local context-compression middleware). Mnemo introduces a third axis: topology of the memory store. Flat vector retrieval (Supermemory, most RAG stacks) vs. graph-traversal retrieval (Mnemo's BFS expansion) produces different recall characteristics for multi-hop relational queries. For clawfit profiles with `statefulness: persistent` and `network: offline` or `data_sensitivity: internal`, a graph-memory option with no cloud dependency would be a scoring-relevant distinction that the current registry cannot represent. No registry field currently captures memory topology (flat vs. graph), and no hardware profile captures the sidecar-process resource footprint that a Rust binary adds to edge deployments.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / MCP / context layer** (local-first, graph-topology sub-type; operates as a sidecar that intercepts conversations and injects retrieved context, not as a plugin or skill the agent calls explicitly)
- The LLM-delegated entity extraction step creates a secondary dependency on Level 1 (base runtime / Ollama), which is architecturally notable — memory quality is bounded by the extraction LLM's capability, not just retrieval latency

## Status
- Watching: early signal, low individual traction (22 HN pts, no star count); same-day cluster of parallel projects elevates category priority; registry gap identified for memory-topology and sidecar-footprint dimensions; no map mutation warranted yet; revisit if any cluster project crosses 500 GitHub stars or gains MCP server integration
