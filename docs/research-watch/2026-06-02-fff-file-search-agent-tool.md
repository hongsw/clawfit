# Research Watch: fff — In-Memory File Search for AI Agents

- Repo/Link: https://github.com/dmtrKovalenko/fff
- Source: GitHub Trending (Daily #16, 7,160 stars, Rust)

## Why this is worth watching
fff is not a CLI search tool — it is a persistent in-memory index with background file watching that keeps frecency-ranked, SIMD-accelerated fuzzy search available to agents without the process-spawn overhead of invoking ripgrep or fd on each query. It ships an MCP server and a Pi framework extension as first-class delivery vectors, positioning itself explicitly as agent-native infrastructure rather than a developer productivity utility.

## What stands out immediately
- Sub-10ms query latency via in-memory index maintained by a background file watcher — no cold-start per query
- Frecency ranking (recency + frequency combined) biases results toward files the user or agent actually works with
- Smith-Waterman fuzzy matching — algorithm borrowed from bioinformatics, claimed to outperform standard edit-distance for partial symbol queries
- SIMD-accelerated regex and Aho-Corasick multi-pattern OR search for throughput on large repos
- Git status awareness: untracked, modified, and ignored files are distinguishable in results
- Definition classifier: marks files containing struct/fn/class declarations — allows agents to scope searches to definition sites
- Delivery: MCP server (Claude/Cursor), Pi framework plugin, Neovim plugin (fff.nvim), Node/Bun SDK, C FFI library
- The MCP server and Pi extension are not afterthoughts; the README frames agent use as the primary use case

## Why clawfit should care
fff introduces a file-search capability that is qualitatively different from shell-out approaches: persistent process, frecency signal, definition awareness, and multi-delivery SDK surface. For clawfit's recommendation engine, agents doing code-gen or QA tasks in large repos currently have no scored option for low-latency file navigation. fff is a registry candidate for the tool-use layer and could influence scoring on `task: code-gen` and `task: qa` profiles where file-context retrieval is a bottleneck. It also extends the MCP cluster tracked at L5 — the MCP server is a context-injection path, but the core capability lives at L4.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability / Tool-Use Layer** (agent-facing search capability with native MCP and Pi delivery; the MCP server is a transport, not the primary classification)

## Status
- Tracking: first-signal for agent-native in-memory file search sub-type; 7.1k stars is a strong early velocity — monitor for registry inclusion at next scoring cycle
