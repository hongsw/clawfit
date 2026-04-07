# Research Watch: claude-peers-mcp

- Repo/Link: https://github.com/louislva/claude-peers-mcp
- Source: hongsw GitHub stars

## Why this is worth watching
claude-peers-mcp gives separate Claude Code instances running on the same machine the ability to discover each other and exchange messages in real time via a local broker daemon (SQLite + localhost:7899). With 1,763 stars it has clear traction for a narrow but important use case: ad-hoc multi-agent coordination without a dedicated orchestrator process. It is one of the first MCP servers that treats Claude-to-Claude messaging as a first-class primitive.

## What stands out immediately
- Broker daemon runs on localhost:7899; each Claude Code session is a peer that registers on startup
- `list_peers`, `send_message`, `set_summary`, `check_messages` — four clean tool verbs
- Uses the official `claude/channel` push protocol — messages arrive instantly rather than via polling
- Scope is currently machine-local; no cross-machine relay (contrast with DureClaw which does cross-machine)
- Single dependency: Bun runtime. Setup is two commands.
- TypeScript, MIT license

## Why clawfit should care
This is a textbook L4c MCP server that enables a new coordination topology: peer-mesh rather than orchestrator-worker. clawfit currently has no registry entry for Claude-to-Claude communication infrastructure. The `network=online` tag is slightly misleading here — the actual message passing is local, but the LLM calls remain online. Latency is low for the coordination layer itself. Relevant for teams running parallel Claude Code sessions on the same dev box.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infra / MCP server (Claude Code peer mesh messaging)**

## Status
- Tracking: new entry, high signal. 1,763 stars. Monitor for cross-machine support, authentication model, and whether Anthropic adopts the pattern officially.
