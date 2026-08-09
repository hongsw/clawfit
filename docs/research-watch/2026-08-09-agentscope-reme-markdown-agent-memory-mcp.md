# Research Watch: agentscope-ai/ReMe — Markdown-Native Agent Memory with Auto-Consolidation

- Repo: https://github.com/agentscope-ai/ReMe (⭐3,300)
- Source: Web search signal (agentscope ecosystem expansion, 2026-08-09); also cited at ACL 2026 Findings
- License: Not confirmed; agentscope family is typically Apache-2.0
- Language: Python

## Why this is worth watching

ReMe (Remember Me) is a distinct project from the AgentScope framework (tracked 2026-07-10) despite sharing the `agentscope-ai` organization. Where AgentScope is a multi-agent coordination framework, ReMe is a **local-first Markdown memory system** — the only L4a/L5 memory tool in the current corpus that uses Markdown files with frontmatter and wikilinks as the primary storage format and exposes them via an MCP server to Claude Code.

The architectural claim is that memory should be **human-readable, human-editable, and machine-traversable** simultaneously. A ReMe memory node is a `.md` file with frontmatter metadata, wikilinks for relationship traversal, and plain text for content — any human can open it in an editor; any agent can retrieve it via the MCP server; hybrid retrieval (wikilinks + BM25 + embeddings) covers graph, keyword, and semantic access from the same underlying file format.

The three "Auto" background processes — **Auto Memory** (conversation → daily summaries), **Auto Resource** (external source indexing), **Auto Dream** (background consolidation into long-term digest nodes) — automate the memory lifecycle without requiring explicit agent action. "Auto Dream" is explicitly framed as analogous to REM sleep consolidation: the system runs background passes over accumulated memories to identify patterns, collapse redundant entries, and elevate recurring themes to permanent digest status.

## What stands out immediately

- **Memory as Markdown files:** storage is `.md` files with YAML frontmatter and `[[wikilink]]` syntax — human-readable and directly editable by humans; no proprietary binary format, no database dependency for reading; version-controllable via standard git
- **Auto Memory:** automatic daily summarization of raw conversation logs into structured memory nodes — agents don't need to explicitly call "save memory"; the system observes and indexes continuously
- **Auto Resource:** indexes external sources (documents, web pages, files) into the same Markdown node format — agents can retrieve information from past-ingested external content alongside past conversations
- **Auto Dream:** background consolidation process that reviews accumulated memory nodes, eliminates redundancy, extracts patterns, and promotes stable themes to long-term "digest" nodes — the REM sleep analogy is accurate: this is not just archiving but structural reorganization
- **Hybrid search (three paths):** wikilink graph traversal (relationship-aware), BM25 keyword matching (exact/near-exact), embeddings (semantic); three paths hit different parts of the retrieval space; graph traversal via wikilinks is unusual — most vector stores lack relationship traversal at the link level
- **MCP server for Claude Code:** agents consuming memory via standard MCP tool calls without SDK coupling; compatible with QwenPaw and CLI-based agents in addition to Claude Code
- **ACL 2026 Findings publication:** academic backing for the methodology — "Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution"; publication in ACL Findings indicates peer review, not just preprint; cite-tracking useful for gauging research uptake
- **946 commits, 3.3k stars:** strong commit depth relative to star count — suggests production use by a dedicated team, not just demo traction
- **Progressive pipeline architecture:** raw conversations → daily summaries (Auto Memory) → background indexing → Auto Dream consolidation → long-term digest nodes; each stage is inspectable as Markdown files

## Why clawfit should care

ReMe is the third entry in the **inspectable agent memory** sub-track alongside wuphf (agent-maintained markdown wiki, L6b/L5) and GBrain (markdown + PGLite, L6b/L4a). However, it adds two capabilities the wuphf/GBrain cluster lacks: (1) an explicit **consolidation process** (Auto Dream) that is background-automated rather than requiring human curation, and (2) **hybrid retrieval** (wikilinks + BM25 + embeddings) that spans three retrieval modalities rather than relying on flat text search.

The MCP integration for Claude Code is directly relevant to clawfit's target user. A `statefulness: persistent` + `network: offline` + `task: code-gen` profile would benefit from a local-first Markdown memory with MCP integration — exactly what ReMe provides. The current registry lacks any entry that combines all three of these characteristics.

Auto Dream is architecturally significant: it is the first background-automated consolidation process in the inspectable memory cluster. Existing tools (wuphf, GBrain, Engram) require the agent or user to explicitly trigger consolidation or archiving. ReMe eliminates this manual step, which reduces the memory hygiene burden for long-running agent sessions.

The Apache-2.0 (likely) license and local-first architecture make ReMe compatible with `governance_need: hard` + `network: offline` profiles where cloud memory APIs (mem0, Supermemory) are unavailable.

## Preliminary interpretation

- **Level 4a — Agent Memory Layer** (primary): local-first Markdown-native persistent memory system consumed by agents via MCP or SDK; Retain/Recall operations over stored facts and experiences
- **Level 5 — Evaluation / Learning Layer** (secondary): Auto Dream consolidation generates new memory organization from accumulated entries, creating an experience-learning loop; ACL 2026 academic backing positions it in the research-backed evaluation cluster

## Claims to verify

- **Auto Dream consolidation quality:** verify whether the background consolidation produces semantically coherent digest nodes or just keyword-proximity clusters; quality depends on the LLM used internally and the consolidation prompt design
- **Wikilink traversal implementation:** confirm whether wikilinks create bidirectional graph edges or only forward references; bidirectional graph traversal is the richer capability and the less obvious default
- **Claude Code MCP server stability:** verify which Claude Code versions are tested and whether the MCP integration covers the full memory lifecycle (Auto Memory, Auto Resource, Auto Dream) or only on-demand Recall
- **License:** Apache-2.0 assumed from agentscope-ai organization default; confirm whether ReMe carries a separate license file
- **ACL 2026 citation vs. implementation alignment:** the academic paper may describe a research prototype that differs from the production repo in 3.3k stars; verify which version the paper evaluates and whether the GitHub implementation matches

## Status

- Active; 3.3k stars, 946 commits
- Registry eligibility: below 5k-star threshold; no schema match for `memory_format: markdown-wikilink` or `memory_backend: local-first-markdown`; local-first architecture means no deterministic cost data
- Schema watch: `memory_format: [sqlite | json | markdown-wikilink | binary-container]`; `memory_consolidation: [manual | background-auto]`; `memory_delivery: [in-process | mcp-server | rest-service]`; `memory_inspectable: true/false`
- Cross-reference: wuphf (L6b/L5, agent-maintained markdown wiki), GBrain (L6b/L4a, markdown + PGLite), Engram (L4a/L5, SQLite + MCP-native), hindsight (2026-08-09, L4a/L5 — REST service, biomimetic schema), AgentScope framework (2026-07-10, same org, L2/L5 — different project)
