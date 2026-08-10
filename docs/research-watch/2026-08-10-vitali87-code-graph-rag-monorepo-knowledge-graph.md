# Research Watch: code-graph-rag — Monorepo Knowledge Graph for AI Agents

- Repo/Link: https://github.com/vitali87/code-graph-rag
- Source: GitHub Trending (today, Python, +96 stars, 2,974 total)

## Why this is worth watching
A Python-native code intelligence layer that parses multi-language monorepos with Tree-sitter, builds a structural knowledge graph in Memgraph, and exposes it as an MCP server for coding agents. Unlike embedding-based RAG (which treats code as text), the graph encodes actual call relationships, imports, and dead-code paths — giving agents precise structural answers rather than approximate semantic matches.

## What stands out immediately
- **Memgraph backend**: persistent, queryable graph DB (Cypher-compatible) vs. vector stores that rebuild on each session
- **MCP server surface**: drop-in context for Claude Code, Aider, Gemini CLI and other MCP-compatible agents
- **AST-based edit operations**: `ast-grep` patterns for surgical search-and-replace across 13+ languages
- **Cross-language analysis**: unified schema spanning Python, TypeScript, Rust, Go, Java, C/C++, C#, PHP, Lua, Dart, Ruby
- **Real-time indexing**: continuous updates as files change
- **Star trajectory**: 2,974★, early velocity (96 today), Python ecosystem — different addressable market from the TypeScript-first gitnexus

## Why clawfit should care
This is the second high-signal code-graph-RAG entry after gitnexus (2026-04-28, L4a/L4c). Where gitnexus is WASM-first, zero-server, client-side TypeScript, code-graph-rag is server-side Python with a real graph DB (Memgraph). The architectural difference matters for org recommendations:
- Monorepos with Python CI pipelines fit code-graph-rag (native language, Memgraph container)
- Frontend/TS-heavy shops with no-infra constraints fit gitnexus (WASM, no backend)

The two projects collectively strengthen the case that L4a is bifurcating: **conversation memory** (cognee, mem0) vs. **structural code memory** (gitnexus, code-graph-rag). If a third structurally-similar project appears, the L4a section in reference-levels.md should explicitly name this sub-cluster.

The MCP surface makes this a direct pairing with `task: code-gen` / `task: refactor` and `network: hybrid` profiles. Star count (2,974) is below registry threshold; watch for velocity over the next week.

## Preliminary interpretation
Current best reading:
- **Level 4a — Memory / Persistent Context** (structural code memory, server-side Memgraph variant)
- **Level 4c — Tool-Use / Action Infrastructure** (MCP server for agent tool calls)

Cross-reference: gitnexus (2026-04-28, L4a/L4c — WASM/client-side TS, 31.5k★, PolyForm NC); codebase-memory-mcp (L4c — C-native, 5.2k★, 158 languages). Third tool in the same structural code-memory cluster.

## Status
- Watching; below registry threshold (2,974★ vs. typical 5k+ for inclusion)
- Do NOT modify reference-levels.md on this single signal — the structural-code-memory sub-cluster now has 3 entries (gitnexus, code-graph-rag, codebase-memory-mcp); if one more appears, add a sub-cluster note to L4a
- Open questions: Memgraph licensing (AGPLv3 may affect enterprise deployments), embedding model for semantic search, indexing speed on large monorepos
