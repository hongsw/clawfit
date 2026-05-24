# Research Watch: ClawMem — On-Device Memory Layer for AI Agents

- Repo/Link: https://github.com/yoloshii/ClawMem
- Source: hongsw GitHub stars (curated by clawfit project owner)

## Why this is worth watching
ClawMem occupies the intersection of two active sub-tracks in the L5 memory cluster: SQLite+MCP-native structured memory (Engram sub-track) and on-device inference (no cloud dependency, GGUF models via node-llama-cpp). At 170 stars it is well below the promotion threshold, but its combination of 31 MCP tools, seven Claude Code lifecycle hooks, and a hybrid retrieval stack (BM25 + vector + reciprocal rank fusion + cross-encoder + multi-graph traversal) is architecturally denser than most single-track entries. It also introduces causal-graph traversal and configurable decay half-lives — two features previously seen only in separate tools (hippo-memory for decay, cognee for graph).

## What stands out immediately
- SQLite single file at `~/.cache/clawmem/index.sqlite` with FTS5 and sqlite-vec; no separate vector DB service required
- Seven Claude Code lifecycle hooks covering ~90% of retrieval automatically — hooks are the primary interface, not manual calls
- 31 MCP tools exposed as secondary interface for any MCP-compatible client
- Local GGUF model inference via `node-llama-cpp` (auto-downloaded, ~2GB); cloud embedding providers (Jina, OpenAI, Voyage, Cohere) are optional fallbacks, not requirements
- Multi-graph traversal: semantic, temporal, and causal graphs — causal inference traces decision chains across sessions
- A-MEM (Adaptive Memory Evolution) enriches stored fragments with evolving keywords and metadata
- Decay half-lives configurable per content type — explicit lifecycle management, not pure persistence
- Beads integration for syncing issue-tracker data as memory graph edges (cross-tool composability signal)
- Prompt injection filtering across five detection layers — security-aware design
- Star count 170 / 26 forks, MIT, TypeScript 98.5% on Bun; no independent benchmarks provided (vendor claims zembed-1 outperforms Cohere rerank-3.5 — claim to inspect)

## Why clawfit should care
ClawMem synthesizes features previously distributed across three separate L5 signals: decay (hippo-memory), causal/graph traversal (cognee), and MCP-native structured access (Engram). If those capabilities hold under independent validation, it is a meaningful architectural consolidation for `network: offline` + `statefulness: persistent` profiles. The seven-hook model also introduces a new integration pattern: Claude Code lifecycle events as first-class memory triggers, rather than explicit agent calls. This is relevant to clawfit's scoring model — agents that support lifecycle hooks could be rated higher for persistent-memory compatibility than agents that require explicit MCP calls.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / MCP / context layer** (primary; SQLite-backed, hook-triggered, MCP-exposed persistent agent memory)
- **Level 7 — Infrastructure / hardware / edge layer** (secondary overlay; on-device GGUF inference, no cloud dependency, explicit offline-first design)
- Sub-track fit: closest to 5c portable-binary (single SQLite file, no infra) but with an MCP-native interface layer that overlaps 5b SQLite+MCP-native (Engram). Neither sub-track is a clean fit — this may warrant a 5d note if a second tool combines on-device inference with hybrid RAG at the memory layer.

## Status
- Tracking: early signal, below 5k-star threshold. Hold for registry action. Architecture is notably dense for a 170-star repo; watch for star velocity increase or community adoption signals in Claude Code hook ecosystem. Causal graph and decay combination warrants a follow-up read of the causal inference implementation once it stabilizes.
