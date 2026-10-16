# Research Watch: xerj — Search Engine for AI Agents

- Repo/Link: https://github.com/xerj-org/xerj
- Source: GitHub Trending
- Stars today: 715 (total: 5,617)

## Why this is worth watching
Most AI agent tool discovery today relies on vector similarity (pgvector, Chroma, Weaviate) or manual tool manifests. xerj positions itself as a search engine built specifically for agents: autoindexing of tool registries and capability endpoints, with an Elasticsearch-compatible query API written in Rust. This occupies a distinct infrastructure niche that sits between L4c (tool/MCP surfaces) and L1 (base runtime) — a routing and discovery layer agents can query at runtime.

## What stands out immediately
- Elasticsearch-compatible API lowers adoption barrier; existing agent frameworks can use it as a drop-in
- Autoindexing design suggests tools/skills register themselves, inverting the manual-manifest model
- Rust implementation implies low-latency response suitable for hot-path agent tool selection
- 715 stars today on a 5.6K total base signals a genuine community discovery moment, not an established project
- No LLM dependency in the core — purely a search/index infrastructure layer

## Why clawfit should care
clawfit currently recommends static (agent, LLM, hardware) triples from a fixed registry. xerj represents a dynamic counterpart: a live index agents query to discover available tools at runtime rather than at config time. If xerj's model gains traction, clawfit's scoring engine may need to account for "tool discovery capability" as a dimension — specifically whether an agent runtime supports dynamic tool indexing vs. static manifest loading.

Also relevant: xerj's Elasticsearch-compatible interface means any agent with web search or HTTP tool-use can index and query it, making it a potential capability layer (L4c) for agent runtimes that currently lack structured tool discovery.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / MCP / capability surface**: xerj provides the search infrastructure that surfaces tools to agents at runtime; this is squarely in the capability-access layer rather than the harness or runtime layer.
- Secondary: **Level 1** (runtime infrastructure) — the index service itself is infrastructure that a base runtime consumes.

## Status
- Tracking: new entry, early signal (day-1 trending)
- Action: watch for harness adoption (ruflo, ECC, Claude Code integration mentions)
- Registry: not added yet; insufficient maturity data for org_fit scoring
