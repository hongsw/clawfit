# Research Watch: Supermemory — Memory API for the AI Era

- Repo/Link: https://github.com/supermemoryai/supermemory
- Source: GitHub Trending

## Why this is worth watching
Supermemory is a production-grade memory API for AI agents that ranked #1 on three benchmarks: LongMemEval (81.6%), LoCoMo, and ConvoMem. With 23.3k stars it has crossed from research prototype into mainstream adoption, directly challenging custom vector-DB setups as the default memory backend for agent developers.

## What stands out immediately
- Hybrid search combining RAG (document retrieval) with personalized user-profile memory in a single query (~50ms retrieval)
- Automatic contradiction resolution and "forgetting" of outdated facts — not just append-only storage
- Real-time connectors for Google Drive, Gmail, Notion, OneDrive, GitHub
- Native MCP server for Claude, Cursor, and other AI tools
- npm + pip packages with Vercel AI SDK and LangChain adapters
- Benchmarked #1 on LongMemEval (81.6%) — first major benchmark comparison across memory architectures

## Why clawfit should care
Supermemory occupies the L4a memory layer but distinguishes itself from tracked tools (OpenMemory, cognee, Honcho, Hippo) through its benchmark-anchored positioning and cloud-API-first delivery model. It signals that the L4a memory cluster is bifurcating: self-hosted/process-boundary tools (Engram, Beads, wuphf) vs. cloud-API memory platforms (supermemory). For `data_sensitivity: internal` profiles with `network: online`, supermemory is now the leading evidence-backed memory option and should be considered for registry inclusion.

## Preliminary interpretation
Current best reading:
- **Level 4a — Agent Memory Systems** (cloud-API sub-type, benchmark-anchored)

## Status
- Tracking: strong adoption signal, L4a benchmark anchor, registry candidate at next scoring cycle
