# Research Watch: cognee — Knowledge Engine for AI Agent Memory

- Repo/Link: https://github.com/topoteretes/cognee
- Source: GitHub Trending (2026-04-17, +170 stars today, 15,788★ total)

## Why this is worth watching
cognee markets itself as "Knowledge Engine for AI Agent Memory in 6 lines of code" — a programmable memory layer that builds knowledge graphs over documents, code, and conversations. At 15,788★ it is already mainstream in the memory-tooling space, and its graph-native approach (rather than pure vector similarity) distinguishes it from claude-mem and OpenMemory.

## What stands out immediately
- 6-line install API: `await cognee.add(data); await cognee.cognify(); results = await cognee.search()`
- Graph-native memory: builds knowledge graphs, not just embeddings — enables reasoning over relationships
- Multi-modal: handles documents, images, code, and unstructured text
- MCP-compatible; integrates with LangChain, LlamaIndex, CrewAI, OpenHands
- Self-hosted; works with any LLM backend (OpenAI, Anthropic, local models)
- Python-first; `pip install cognee` one-liner

## Why clawfit should care
cognee fills a gap in the Level 4a memory taxonomy: where claude-mem is session-centric and GBrain is markdown-native, cognee is graph-native and multi-modal. Orgs doing research or data-analysis workflows (not just code-gen) benefit from graph-structured memory that can answer "what relates to X?" rather than just "what is similar to X?". Its MCP compatibility and multi-LLM support make it a strong recommendation for `research` + `data-analysis` profiles with `data_sensitivity: internal`.

## Preliminary interpretation
Current best reading:
- **Level 4a — Memory / persistent context** (graph-native sub-type)

## Status
- High signal: 15,788★ with cross-framework integrations; add to registry
