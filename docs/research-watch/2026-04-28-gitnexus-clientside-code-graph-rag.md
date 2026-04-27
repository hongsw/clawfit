# Research Watch: GitNexus — Client-Side Code Intelligence with Graph RAG

- Repo: https://github.com/abhigyanpatwari/GitNexus
- Hosted Web UI: https://gitnexus.vercel.app
- Source: GitHub Trending Daily (TypeScript) — 2026-04-28, +1,074 stars in 24h (claim to inspect)
- Headline numbers (claim to inspect): 31.5k stars, 3.6k forks, 789 commits, latest release v1.6.3 (2026-04-24)

## Why this is worth watching
A high-velocity (+1,074★/day) TypeScript project that fuses two layers clawfit currently tracks separately: code-intelligence indexing (4a-style persistent context) and an MCP tool surface (4c). Unlike most Graph RAG projects, GitNexus runs the entire indexer — Tree-sitter, embeddings, and graph DB — fully client-side via WASM/WebGPU, with no backend service required for either the Web UI or the local CLI. This collapses the typical "indexer service + agent" deployment model into a zero-infra primitive.

## What stands out immediately
- **Two delivery modes from one codebase**: (1) browser Web UI where "code never leaves the browser" via WASM, and (2) a `gitnexus` CLI + MCP server for local persistent indexing.
- **Graph storage**: LadybugDB — a native embedded graph database with vector support — runs as native bindings in CLI and WASM in browser. Same DB, two runtimes.
- **Hybrid retrieval**: BM25 (keyword) + semantic vectors + Reciprocal Rank Fusion. Embeddings via HuggingFace `transformers.js` with WebGPU acceleration in browser, falling back to WASM.
- **Graph schema is code-aware, not generic RAG**: nodes are functions/classes/interfaces; edges are CALLS, IMPORTS, EXTENDS, IMPLEMENTS. Community detection (Graphology) groups related symbols into functional clusters.
- **Precomputed at index time, not query time**: confidence-scored relationships, process traces, and "blast-radius" impact analysis are baked in. README claim: tools return complete context in one call rather than chained LLM exploration.
- **16 MCP tools exposed**: `query`, `context`, `impact`, `detect_changes`, `rename`, `cypher`, plus 5 multi-repo `group_*` tools. Claude Code hook integration (PreToolUse enrichment, PostToolUse staleness detection).
- **14 language parsers** via Tree-sitter (TS/JS/Python/Java/Kotlin/C#/Go/Rust/PHP/Ruby/Swift/C/C++/Dart) with varying depth.
- **Licensing caveat**: PolyForm Noncommercial — commercial use routes through akonlabs.com. This affects registry inclusion criteria for enterprise users.
- **Positioning quote (verbatim)**: "Like DeepWiki, but deeper. DeepWiki helps you understand code. GitNexus lets you analyze it."

## Why clawfit should care
Most Level 4a memory tools (cognee, claude-mem, GBrain) treat memory as generic key-value or semantic store. GitNexus is **structurally specialized for code** — its graph schema encodes the semantics a coding agent actually needs (call chains, blast radius, dependency cycles), not just "things the user said before." For clawfit's recommendation engine, this means a candidate that:

- Pairs cleanly with `task: code-gen` / `task: refactor` workloads
- Fits `network: offline` and on-device hardware profiles (WASM-only mode is genuinely client-side)
- Bridges 4a (graph memory) and 4c (MCP tool surface) — reinforcing the case that L4 sub-layers are not strictly orthogonal

Differentiation vs. existing 4a entries:
- **vs. cognee**: cognee is a general graph-memory engine for any domain; GitNexus is opinionated for source code with code-specific edge types and impact analysis.
- **vs. claude-mem**: claude-mem persists conversational/session context; GitNexus persists structural code facts derived from AST parsing.
- **vs. mem0**: mem0 emphasizes user/agent memory across sessions; GitNexus emphasizes repository structure across queries.
- **vs. DeepWiki**: explicitly positioned against — DeepWiki produces narrative documentation, GitNexus produces queryable graph relationships.

## Preliminary interpretation
Current best reading:
- **Primary: Level 4a — Memory / Persistent Context** (code-specialized graph memory subtype)
- **Secondary: Level 4c — Tool-Use / Action Infrastructure** (16-tool MCP server surface)
- Notable cross-cut: zero-server / WASM-first deployment reinforces emerging pattern alongside Libretto's deterministic browser automation — client-side capability layers are becoming a recognizable cluster within L4c.

## Status
- Strong velocity signal (+1,074★/day) on an already-mature project (31.5k★, v1.6.3); monitor for 1 week before registry inclusion. Do NOT modify reference-levels.md on this single signal — flag for aggregation if 2+ more code-graph-RAG entries appear in L4a.
- Open questions to validate: actual creation date (claim of 31.5k★ + 789 commits suggests >6 months old, but trending velocity is anomalous for a mature repo — possible re-discovery event); license compatibility with clawfit registry inclusion criteria; embedding model size and offline-install footprint.
