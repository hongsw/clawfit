# Research Watch: codebase-memory-mcp — C-Native Code Intelligence MCP Server

- Repo/Link: https://github.com/DeusData/codebase-memory-mcp
- Source: GitHub Trending (today, all languages)

## Why this is worth watching
A C-native MCP server that indexes codebases into a persistent knowledge graph, claiming 99.2% token reduction versus file-by-file reading (3,400 vs 412,000 tokens on real queries). At 5.2k stars with v0.8.1 released June 2026, it's gaining adoption fast across 11 coding platforms. The performance claims (sub-ms queries, Linux kernel indexed in 3 minutes) are unusual for a newcomer.

## What stands out immediately
- Written in C (88%) with tree-sitter grammars — unusual for an MCP server, but explains the performance
- 158 supported languages; 14 MCP tools: call-chain tracing, dead-code detection, Cypher-like graph queries
- Claims 99.2% token reduction vs file-by-file approaches — directly reduces agent cost
- Compatible with Claude Code, Codex CLI, Gemini CLI, Zed, Aider, VS Code
- 5,221 stars, 484 forks, 35 releases (v0.8.1 June 2026)

## Why clawfit should care
This is a direct Level 4c (tool-use/action infra) addition to the ecosystem. It slots between cipher (memory MCP) and serena (semantic toolkit) but targets a different layer — structural understanding of codebases rather than memory recall. For developer profiles doing code-gen, this is a force multiplier that pairs with any Level 1 agent. The token-reduction claim also affects cost profiles in `clawfit recommend` scenarios.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infra (code intelligence MCP)**

## Status
- New — first observed 2026-06-18. Adding to tools_registry.json as L4c entry.
