# Research Watch: DureClaw

- Repo/Link: https://github.com/DureClaw/dureclaw
- Source: hongsw GitHub stars

## Why this is worth watching
DureClaw orchestrates AI agents across physically separate machines using Claude Code as the orchestrator and a Phoenix WebSocket server as the message bus. Workers on remote machines (Mac, Linux, Windows) run any AI backend — Claude, OpenCode, Gemini, Aider — and receive tasks via `task.assign`, returning results via `task.result`. The name references the Korean cooperative farming tradition (두레/dure), signaling a philosophy of distributed-but-unified effort. At 1 star it is brand new and authored by hongsw, making it a direct insight into the owner's own tooling direction.

## What stands out immediately
- Three-tier architecture: Claude Code orchestrator → Phoenix WebSocket server → oah-agent workers on each machine
- MCP plugin via `@dureclaw/mcp` (npm + MCP Registry + Smithery listed) — formal distribution path already in place
- Agent backend is heterogeneous: worker can run claude / opencode / gemini / aider — not Claude-locked
- Phoenix server runs via Docker with no Elixir requirement; Tailscale integration for networking
- Slash commands `/setup-team` and `/team-status` — natural language alternatives also accepted
- Shell as primary language; multilingual README (Korean, English, Chinese, Japanese)
- Contrast with claude-peers-mcp: that tool is machine-local peer mesh; DureClaw is cross-machine crew orchestration

## Why clawfit should care
DureClaw is a direct L2/L4c hybrid from the repo owner — it is both an orchestration harness (L2) and an MCP server enabling cross-machine tool use (L4c). It is the most architecturally ambitious of this batch. Even at 1 star it warrants tracking because it comes from hongsw directly and may shape future clawfit registry categories (heterogeneous-backend orchestration, cross-machine agent crews).

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrapper / orchestration harness (cross-machine multi-agent crew via MCP + Phoenix)**

## Status
- Tracking: new entry, personal project signal. 1 star (hongsw is the author). High relevance despite low stars. Monitor for community adoption and MCP Registry listing status.
