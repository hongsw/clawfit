# Research Watch: Engram — Persistent Memory for AI Coding Agents

- Repo: https://github.com/Gentleman-Programming/engram
- Also see: https://github.com/syntax-syndicate/engram-agent-memory (mirror), https://lobehub.com/mcp/gentleman-programming-engram
- Related signals: docs/research-watch/2026-04-27-gastownhall-beads-coding-agent-memory.md, docs/research-watch/2026-04-17-cognee-memory-engine.md (and claude-mem, hippo-memory, GBrain)

## Why this is worth watching
Engram is a Go-native persistent memory system for coding agents that ships as a single binary with SQLite + FTS5 and exposes itself primarily through an MCP server (17 tools). It is the second Go-based agent-memory entrant trending this week — Beads (22.2K stars) and Engram (~2.9K stars, +50/day) are converging on the "compiled, no-runtime, agent-memory infra" pattern. Engram's MCP-first interface model differentiates it from both Python-heavy memory tools (cognee, mem0) and Beads' more workflow-oriented framing.

## What stands out immediately
- 2.9K stars, 61 releases, v1.14.5 published 2026-04-27 — high release cadence (claim to inspect: 205 commits suggests ~1 commit/day baseline)
- Go 93.7% — single binary, zero Node/Python/Docker dependencies (validated from README)
- SQLite + FTS5 as canonical storage at `~/.engram/engram.db`; cloud sync is opt-in replication only, local remains source of truth
- Explicit data schema: `mem_save(title, type, What/Why/Where/Learned)` — opinionated structured memory rather than free-form notes
- 17 MCP tools across 5 categories: save/update, search/retrieve, session lifecycle (`mem_session_start/end/summary`), conflict surfacing (`mem_judge`), and utilities (`mem_capture_passive`, `mem_merge_projects`)
- Multiple parallel interfaces: MCP (stdio), HTTP API (port 7437), CLI (17+ subcommands), TUI (vim-key nav, Catppuccin theme)
- Agent-agnostic positioning: explicitly tested against Claude Code, OpenCode, Gemini CLI, Codex, VS Code Copilot, Antigravity, Cursor, Windsurf
- Self-positions as "inspired by claude-mem — but agent-agnostic, simpler, built different"; no public comparison to Beads or cognee

## Why clawfit should care
Engram is a clean datapoint that the Level 5 memory layer is bifurcating along an interface axis, not just a storage axis. Where cognee bets on graph semantics and Beads bets on workflow-native context retention, Engram bets on **MCP as the universal memory protocol** plus a structured What/Why/Where/Learned schema. For clawfit's recommendation engine, this matters for two reasons: (1) `network: offline` + `setup_complexity: low` profiles now have multiple Go-binary options to recommend, and (2) "MCP-native memory" is emerging as a sub-pattern that may eventually warrant its own scoring axis or sub-category alongside graph-memory and decay-memory.

## Beads vs Engram — core differentiation
Both are Go, both target coding-agent memory, both are stdlib-friendly. Key splits:

- **Interface primacy**: Beads emphasizes workflow/context retention as a runtime concern; Engram's primary surface is MCP (17 tools) with HTTP/CLI/TUI as peers. Engram is built to be a *protocol endpoint*; Beads is built to be a *retention layer*.
- **Schema**: Engram is opinionated (What/Why/Where/Learned + type + topic_key) — claim to inspect. Beads' schema model is less publicly documented.
- **Session model**: Engram exposes explicit lifecycle hooks (`mem_session_start/end/summary`) and passive capture (`mem_capture_passive`) — agent integration is a first-class API. Beads' session story is less explicit from public README.
- **Conflict handling**: Engram ships `mem_judge` for conflict surfacing across saved memories — a deliberate move beyond pure storage into curation.
- **Adoption gap**: Beads 22.2K vs Engram 2.9K — Beads has broader generalist appeal; Engram is more opinionated and likely retains a narrower but stickier audience (MCP-committed teams).

The summary read: Beads is "memory as retention infrastructure," Engram is "memory as MCP-native structured observations with session lifecycle." Different bets, not redundant.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / MCP / context layer** (primary; SQLite-backed persistent agent memory)
- **Level 4 — Capability / plugin / tool-use layer** (secondary; ships an MCP server with 17 tools, functions as a tool-use surface for any MCP client)
- Sub-pattern signal: "MCP-native memory" — Engram + emerging peers (claude-mem influence) form a distinct cluster from graph-memory (cognee) and retention-memory (Beads). Worth tracking but premature to formalize.

## Status
- Tracking: active signal. Star velocity moderate (+50/day) but release cadence and structural opinion (lifecycle tools, judge tool, schema fields) are stronger differentiators than stars alone.
- Registry action: none — memory infrastructure does not fit the agent/llm/hardware schema.
- reference-levels.md action: none yet, but Beads + Engram + cognee + claude-mem cluster is approaching the threshold where Level 5 may need sub-categorization (e.g., 5a graph-memory, 5b retention-memory, 5c MCP-native-memory). Re-evaluate if a 5th distinct entrant appears within 30 days.
