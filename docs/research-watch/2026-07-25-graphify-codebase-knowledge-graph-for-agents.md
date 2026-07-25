# Research Watch: Graphify — Codebase Knowledge Graph for AI Agents

- Repo/Link: https://github.com/Graphify-Labs/graphify
- Source: GeekNews front page (2026-07-25)
- Stars: ⭐ 95,300 (9.2k forks, YC S26)

## Why this is worth watching

Graphify converts codebases — plus documentation, SQL schemas, configs, and PDFs — into a queryable knowledge graph that agents can traverse in natural language. At 95.3k stars and YC S26 backing, it is the second-highest-starred tracked tool in the corpus after mattpocock/skills (186k) and the largest single-signal code-intelligence tool observed in this scan series. Its graph-traversal approach (real edges, not vector embeddings) is architecturally distinct from every prior code-intelligence signal tracked.

## What stands out immediately

- **Local AST parsing via tree-sitter** — deterministic, no LLM required for graph construction; 40+ languages supported
- **"Every edge is explained"** — edges tagged `EXTRACTED` (explicit) or `INFERRED` (resolved), making graph decisions auditable
- **No vector embeddings** — real graph traversal with community detection and "god node" identification (highly-connected concepts)
- **Multi-format ingestion** — code, docs, PDFs, images, video/audio in a unified graph; semantic extraction of non-code assets routes through configured LLM backends
- **Skill packaging** — ships as an installable skill for Claude Code, Cursor, Codex, Gemini CLI, and 15+ agents; `graphify query` CLI for natural language traversal
- **Three outputs** — `graph.html` (visual), `GRAPH_REPORT.md` (markdown summary), `graph.json` (machine-readable); all local, no source files sent to external APIs
- **Dual license** Apache 2.0 / MIT; YC S26 company (Graphify Labs)
- **Cross-file relationship resolution** across ~40 languages; Terraform, SQL, and Salesforce Apex included

## Why clawfit should care

Code intelligence for agents is the fastest-growing L4c sub-category in the scan corpus. Serena (26.8k★, 2026-07-23) and code-review-graph (19.7k★, 2026-07-18) are the prior signals; Graphify at 95.3k★ is 3.5× larger than serena and introduces a fundamentally different retrieval model. The graph approach is significant for clawfit's `task: qa` and `task: code-gen` profiles where understanding cross-file dependencies (not just token proximity) is the bottleneck. The offline-first architecture (no API calls for source files) is relevant for `data_sensitivity: confidential` profiles. The skill-packaging pattern (same tool installable across 15+ agent runtimes) reinforces the L4b/L4c convergence trend.

**Schema gap exposed:** the current `tools_registry.json` has no `task: knowledge-graph` or `task: code-intelligence` category. Graphify does not fit cleanly into existing task categories; adding it would require either a new task type or classifying it under `research + code-gen`, which undersells the distinction.

## Preliminary interpretation

Current best reading:
- **Level 5 — Knowledge/memory substrate (primary):** Graphify builds and persists a structured knowledge representation of a codebase that survives across agent sessions. Unlike screenpipe (ambient context capture, L5) or codebase-memory-mcp (conversation-fact persistence, L5), Graphify's graph is deterministic, AST-derived, and queryable via graph traversal — a distinct L5 sub-type: **static deterministic code knowledge graph**.
- **Level 4c — Capability/skill layer (secondary):** Ships as an installable skill for coding agents; `graphify query` is a tool call abstraction. The skill packaging across 15+ runtimes reinforces L4c secondary.

Closest tracked neighbor: serena (L4c primary, code-navigation MCP server). Key distinction: serena uses LSP/tree-sitter for real-time navigation; Graphify builds a persistent offline graph structure. They operate at different points in the agent session: serena answers "where is this symbol right now?" and Graphify answers "how does this concept connect to everything else in the codebase?"

## Status
- First signal. High-confidence classification (L5 primary / L4c secondary).
- **Star count (95.3k) well exceeds the 5k registry threshold.** Registry entry deferred this run: `task: knowledge-graph` or `task: code-intelligence` absent from current schema; adding Graphify without a proper task category would produce misleading recommendation scores. Flag for next schema revision cycle.
- **Canonical section change candidate:** with serena (2026-07-23) as a second independent L4c code-intelligence signal and Graphify as a third, the "code-intelligence MCP/skill" sub-type now has three signals. "When in doubt" rule applied — Graphify's graph-traversal approach is architecturally distinct enough from serena's LSP approach that they represent different L5/L4c sub-types, not a single merged category. Deferred to next review cycle.
- **Schema watch additions:** `task: knowledge-graph`; `task: code-intelligence`; `retrieval_model: [vector | graph | lsp | hybrid]`; `knowledge_persistence: [session | persistent | exported]`.
