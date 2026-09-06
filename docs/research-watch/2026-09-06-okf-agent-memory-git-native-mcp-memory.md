# Research Watch: OKF Agent Memory — Git-Native MCP Memory for Coding Agents

- Repo/Link: https://github.com/okf-memory/okf-agent-memory (⭐29)
- Source: Hacker News front page (14 pts, 2026-09-06) — "OKF Agent Memory – Git-native persistent memory for AI coding agents"

## Why this is worth watching

This is the third independent structured-memory architecture to appear in research-watch after Lemmalog (2026-08-30, logic/Datalog) and memoryfield (2026-08-31, portable ZIP + SQLite). OKF uses a different mechanism: Google's Open Knowledge Format (OKF v0.2) as the schema, BM25 keyword search at sub-300μs latency, and a built-in MCP server that exposes memory operations directly to Claude Code and compatible runtimes — no separate retrieval pipeline. The three together bracket a design space that clawfit's current taxonomy doesn't distinguish: logic-inference vs. portable-file vs. keyword-graph.

## What stands out immediately

- **MCP server built-in**: memory is exposed as MCP tools — no custom integration; any Claude Code or MCP-compatible agent can attach without code changes
- **BM25 over embeddings**: keyword search instead of vector search; sub-300μs, no model call needed for retrieval; deterministic and inspectable
- **Google OKF spec**: uses a named, versioned format specification (Open Knowledge Format v0.2); positions the format as a standard rather than a personal convention
- **Hierarchical index files**: reduces context injection by ~80% via progressive disclosure; agents see the index first, fetch pages on demand
- **Go, zero external dependencies**: installable via `go install`; no Python runtime, no API key, no embedding model required
- **Git-native storage**: memory lives as Markdown files in the repository; version-controlled, diffable, reviewable by humans alongside code

## Why clawfit should care

This is the third-signal confirmation the memoryfield doc (2026-08-31) called out explicitly: "deferred until a third independent implementation confirms one of these approaches." Three independent implementations now exist across three distinct design choices — Datalog inference, ZIP+SQLite portable file, and BM25+MCP keyword graph. The design axis is confirmed: `memory_model: [logic | portable-file | keyword-graph | vector]` is a real dimension for `stateful: persistent` agents, not a one-off variant.

The BM25-over-embeddings choice is architecturally significant for clawfit's cost model: keyword retrieval has zero per-query inference cost, making it the natural choice for `monthly_budget: low` or `data_sensitivity: confidential` profiles where sending queries to an embedding endpoint is unacceptable.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory / Observability / Evaluation** (primary): OKF defines how an agent stores and retrieves knowledge between sessions; the OKF spec is a memory architecture choice
- **Level 4 — Capabilities / Skills / MCP** (secondary): the built-in MCP server is an L4 integration surface that makes the L5 memory layer callable by any agent

## Status

- Research signal; no registry entry (29 stars, below threshold; MCP memory is a skill/capability, not a base agent or LLM)
- **Three-signal confirmation for `memory_model` design axis**: Lemmalog (logic-inference, 2026-08-30) + memoryfield (portable-file, 2026-08-31) + OKF (keyword-graph+MCP, 2026-09-06)
- The BM25/keyword-graph variant is the first memory architecture in this log that imposes zero per-query inference cost — relevant for budget-constrained and air-gapped profiles
- Watch: whether OKF v0.2 spec attracts implementations from other authors; whether MCP server integration drives adoption beyond the Go ecosystem
