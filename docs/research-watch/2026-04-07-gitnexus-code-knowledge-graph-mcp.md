# Research Watch: GitNexus — Code Knowledge Graph + MCP Server

- Repo/Link: https://github.com/abhigyanpatwari/GitNexus
- Source: GitHub Trending

## Why this is worth watching
GitNexus indexes any codebase into a persistent knowledge graph (dependencies, call chains, execution flows) and exposes it through 16 MCP tools, giving AI coding agents structural awareness they currently lack. With 23,408 stars and +857 today, it is the fastest-rising TypeScript repo on trending and addresses a recognized gap in how Claude Code, Cursor, and Copilot miss cross-file impact. The dual interface (CLI+MCP for editors, browser-based graph UI with zero install) lowers adoption friction significantly.

## What stands out immediately
- 16 MCP tools: hybrid search (BM25 + semantic), blast-radius impact analysis, multi-repo dependency tracking, Cypher graph queries, git-diff change detection
- Precomputes structural analysis at index time — smaller models can work reliably, less token burn
- Fully client-side browser mode (Tree-sitter WASM + LadybugDB WASM): no server needed
- Language coverage: JS, TS, Python, Java, Go, Rust, C/C++
- Positions as "AI agents never miss code" — direct response to broken-refactor complaints

## Why clawfit should care
This is a Level 4c tool-use / action infrastructure entry: it is not an agent, it is a MCP capability layer that any base agent can call. It directly upgrades the `code-gen` and `qa` task scores for agents that support MCP. Clawfit's scoring model does not yet account for MCP-augmented capability lift; GitNexus is a concrete case where `setup_complexity` investment pays off in task coverage.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infrastructure (MCP server + code intelligence layer)**

## Status
- Tracking: new entry, high signal. 23k stars day-one trending. Consider adding to registry as L4c if growth sustains.
