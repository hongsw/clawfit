# Research Watch: ctx — Agent History Search CLI

- Repo/Link: https://github.com/ctxrs/ctx
- Source: Hacker News (Show HN)

## Why this is worth watching
ctx solves a real pain point for teams using multiple coding agents over time: the inability to search prior session context across Claude Code, Codex, Cursor, Gemini CLI, and others. It indexes all local agent transcripts into SQLite and exposes token-efficient search (claimed 50x more efficient than raw transcript search). It is entirely local with no cloud dependency.

## What stands out immediately
- Multi-agent transcript support: Claude Code, Codex, Cursor, Pi, OpenCode, Gemini CLI, and more
- SQLite-backed local index with read-only SQL access for advanced queries
- `ctx search "failed migration"` pattern for recovering prior debugging context
- Prevents duplicate work across agent sessions; preserves institutional memory

## Why clawfit should care
ctx is a lightweight **session-memory recovery** tool that operates between agent runs rather than within them. It addresses the lack of persistent cross-session memory in most L1 base agents. If the `offline_mid_codegen` or confidential-data profiles grow, tools like ctx (local-only, zero cloud) become increasingly relevant. This also surfaces a gap in clawfit's current taxonomy: there is no clean slot for "agent history indexer" — distinct from an in-session memory system like codebase-memory-mcp.

## Preliminary interpretation
Current best reading:
- **Level 4b — Domain Skill / Developer Tooling** (session history as a searchable capability layer)
- **Level 6 secondary** (persistent memory substrate spanning multiple agent sessions)

## Status
- Low star count (203★ at time of discovery); HN Show HN placement is the signal. Below standard promotion threshold. Monitor for star growth and second independent signal. Promotion criterion: 2K★ OR explicit integration by a tracked L1/L2 agent runtime.
