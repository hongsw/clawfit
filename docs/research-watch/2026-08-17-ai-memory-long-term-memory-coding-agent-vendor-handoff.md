# Research Watch: ai-memory — Long-Term Memory and Vendor Handoff for Coding Agent CLIs

- Repo: https://github.com/akitaonrails/ai-memory (⭐1,904)
- Source: GitHub Trending (all languages, daily) 2026-08-17
- License: MIT
- Language: Rust
- Author: akitaonrails (community)

## Why this is worth watching

ai-memory is a Rust binary that provides persistent, cross-session, cross-vendor memory for coding agent CLIs. The core innovation is not just session summarization (many tools do this) — it is a documented **vendor handoff** mechanism: a developer can stop Claude Code mid-task, start OpenAI Codex in the same directory, and pick up with full context continuity. The system supports 20+ agent CLIs including Claude Code, Codex, Command Code, Devin CLI, Cursor, Gemini CLI, Kimi Code, Kiro CLI, Grok Build CLI, Antigravity CLI, and others.

At 1,904 stars it is above the 100-star tracking threshold. The multi-vendor handoff problem — moving unfinished work across agent CLI vendors without re-explaining architecture — is an unresolved pain point that grows as agent CLI fragmentation increases. This is the first dedicated Rust implementation of a solution to this problem tracked in the corpus.

## What stands out immediately

- **Wiki-as-memory-source-of-truth:** memory is stored as markdown files in a `wiki/` directory under git version control — making the memory layer inspectable, diffable, and committable. Not a proprietary format or opaque vector database. Developers own the data.
- **Hybrid retrieval stack:** FTS5 (SQLite full-text search), entity matching (extracted technologies and nouns), graph-neighbor relationships, optional vector similarity, and source-authority weighting (decision/procedure pages rank higher). Multi-strategy retrieval reduces the failure modes of any single approach.
- **Session-end compilation:** at end-of-session, raw transcript segments in `raw/` are compiled into coherent summary pages in `wiki/` — optionally via LLM consolidation or via rule-based summaries. The LLM consolidation step is optional, not required, which preserves function in offline or budget-constrained environments.
- **SessionStart hook architecture:** handoffs are delivered via SessionStart hooks before the first prompt in a new session. This matches Claude Code's hook model — the handoff arrives as structured context, not as a prefixed system message that competes with the user's first message.
- **MCP server mode:** runs as an MCP daemon, allowing coding agents to query and write memory via MCP tool calls rather than file-system hooks. Both integration paths (hook + MCP) supported simultaneously.
- **20+ CLI vendors documented:** coverage spans all major coding agent CLIs as of mid-2026, including Devin CLI, OpenCode, and Kiro CLI — not just the top three. Range of integration depth: some CLIs get full lifecycle-hook integration; others get MCP-only mode.
- **Rust binary, single-process:** no external services required. The binary manages `wiki/` (markdown), `raw/` (transcript segments), `db/` (SQLite with FTS5 and embeddings), and `models/` (local embeddings) — full offline operation without cloud dependencies.

## Why clawfit should care

The vendor handoff use case is directly relevant to clawfit's recommendation model: clawfit recommends a specific (agent, LLM, hardware) triple, but in practice developers use multiple tools across the same project. ai-memory is infrastructure that makes agent-switching less costly — which has two implications:

1. **Reduces lock-in penalty of any single recommendation:** if a user can switch from clawfit's recommended agent to a different one without losing context, the switching cost that currently keeps users on their first choice is reduced. This softens the "winner-take-all" dynamic in agent CLI adoption.
2. **Makes multi-agent session patterns addressable:** clawfit's current `statefulness` dimension is binary (`none | session | persistent`). ai-memory introduces a `cross-vendor persistent` statefulness sub-type that does not correspond to any current category.

**Cross-signal with hubble.md (2026-08-16):** hubble.md is a shared filesystem where both human and agent write simultaneously (L6 human interface). ai-memory is a shared memory layer that bridges multiple agent sessions sequentially (L5 memory). Both use local markdown files as the coordination primitive — "local-first markdown as cross-system coordination medium" is an emerging pattern across two different layers.

**Cross-signal with honcho (2026-05-24):** honcho (tracked L5) is a stateful memory service for deployed agents with a cloud API. ai-memory is a local-first alternative for individual developer CLI workflows. Same layer (L5), different deployment model (cloud service vs. local Rust binary). Together they confirm L5 memory is being addressed at both enterprise-SaaS scale (honcho) and individual-developer scale (ai-memory).

**Schema gap:** `statefulness: cross-vendor-persistent` (beyond current `none | session | persistent` trichotomy); `memory_backend: [sqlite-fts5 | vector | hybrid]`; `vendor_handoff: bool`.

## Preliminary interpretation

- **Level 5 — Memory / observability layer** (primary): ai-memory stores session history, compiles summaries, and retrieves relevant context for subsequent sessions — squarely an L5 tool. It does not provide inference, orchestrate workflows, or act as a harness.
- **Level 4 secondary (MCP server):** the MCP daemon mode makes ai-memory callable as an L4 capability tool from within agent sessions — agents can query and write memory during a session, not only between sessions.
- Not L2 (harness): ai-memory is not an agent runner; it provides memory infrastructure consumed by other agents.
- Closest structural analogues: **honcho** (L5, cloud, multi-user agent memory, tracked 2026-05-24) at the enterprise end; **mem0** (not yet tracked, cloud, Python SDK) at the developer-facing end.

## Claims to verify

- **Vendor handoff end-to-end:** does the SessionStart hook mechanism actually deliver cross-session context in all 20+ documented CLIs, or are some documented only as "MCP-only mode" (which requires the agent to actively query memory, not automatically receive a handoff)?
- **FTS5 + graph retrieval quality:** the multi-strategy retrieval stack is architecturally sound; what is the actual retrieval precision in realistic coding session contexts (large codebases, multiple parallel tasks)?
- **LLM consolidation quality:** optional LLM-based wiki page compilation — which LLM, what prompt, and is the compilation quality sufficient for handoff context without additional summarization by the receiving agent?
- **Rust binary build portability:** single-binary distribution simplifies deployment, but does it cross-compile cleanly for Windows/Linux/macOS, or are there platform-specific SQLite or embedding library dependencies?

## Status

- 1,904 stars — above 100-star tracking threshold; below 5k registry threshold
- **No registry entry:** memory infrastructure tool, no `agents.json`/`llms.json`/`hardware.json` schema mapping; no deterministic inference cost/latency data
- **No canonical section change:** single signal for "cross-vendor coding-agent memory with SessionStart handoff"; two-signal rule requires a second tool in the same specific sub-type
- **Watch for:** second tool implementing vendor-agnostic coding-agent memory with structured handoff (would trigger L5 sub-section consideration); star velocity reaching 5k (registry threshold); adoption documented by a tracked L2 harness as their official memory layer
