# Research Watch: OzBrain — Cross-Agent Shared Knowledge Base via MCP

- Repo/Link: https://ozbrain.com
- Source: Hacker News front page (Show HN, 75 points, 2026-08-23)

## Why this is worth watching

OzBrain provides a shared, structured knowledge base that multiple AI agents — across different platforms (Claude, ChatGPT, Cursor) — can read and write simultaneously via MCP connectors. Unlike per-platform memory APIs, it creates a single source of truth for projects, decisions, and research that persists across agent sessions and tool switches.

## What stands out immediately

- **Cross-platform via MCP**: connects to Claude, ChatGPT, Cursor, and others without code changes; uses MCP as the integration layer
- **Conflict detection**: flags when a write contradicts existing knowledge; version history attributes changes to the agent that made them
- **Structured articles, not raw logs**: organizes content into focused, auto-refactored articles rather than conversation history dumps
- **Explicitly not memory**: positions itself against `memory_api`-style systems (thin daily summaries); claims to hold "projects, decisions, research, and thinking already done"
- **Proprietary SaaS**: free tier (50 articles), Pro ($20/mo), Max ($99/mo); no open-source repository

## Why clawfit should care

clawfit has no dimension for cross-agent shared knowledge. `statefulness` currently captures "ephemeral / session / persistent" within a single tool — but OzBrain introduces a new axis: **cross-tool knowledge sharing**. A `shared_knowledge_store` dimension (none / proprietary-SaaS / self-hosted / MCP-native) could help orgs that run multiple coding agents in parallel (e.g., Claude Code + Cursor on the same codebase). This is a distinct pattern from TencentDB team memory (which is team-scoped within one platform) and from codebase-memory-mcp (which indexes code, not decisions and research).

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory and Knowledge**: primary. Persistent structured knowledge layer across agent sessions and platforms.
- **Level 4 secondary**: MCP as the capability/integration mechanism for agent read/write access.

## Status

- Tracking: early commercial SaaS signal, no public GitHub
- 75 HN points on Show HN debut; concept well-differentiated from existing tracked L5 tools
- Schema watch: `shared_knowledge_store: [none | proprietary-saas | self-hosted | mcp-native]`; `cross_platform_memory: bool`
- No canonical section change: first signal for "MCP-mediated cross-agent shared knowledge" pattern
