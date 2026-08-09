# Research Watch: Claude Code Cross-Session Messaging

- Repo/Link: https://code.claude.com/docs/en/cross-session-messaging
- Source: Hacker News front page ("Message your other Claude Code sessions", 2026-08-09)

## Why this is worth watching
Built-in peer-to-peer messaging between independent Claude Code sessions is now an official Anthropic feature (requires v2.1.224+). Previously this required third-party bridges like claude-peers-mcp (2026-04-07); now it is native. This shifts multi-agent coordination from an MCP-add-on concern to a first-class harness capability.

## What stands out immediately

- Two tools: `ListAgents` (discover reachable sessions) and `SendMessage` (deliver plain-text messages)
- Three scopes: same machine (socket, never through Anthropic), cross-machine via Remote Control, Claude Code on the web
- Cross-machine direction is reply-only; Claude can't initiate to a remote session
- Messages are plain text only — not conversation history or files
- Inbound controls: `accept` / `hold` / `refuse` per session; configurable in settings.json
- Permission isolation: a received message cannot approve permissions or change configuration on the receiving session
- Availability: macOS + Linux; not available on Bedrock, GCP Agent Platform, or Microsoft Foundry
- 50-message backlog cap per session; deduplication window prevents tight loops

## Why clawfit should care
Multi-agent coordination is moving from orchestrator-mediated (L2 harness) to native peer topology. The `claude_code_routines` and `oh-my-claudecode` registry entries gain a first-class coordination primitive that changes their competitive position — background agents can now route status updates without requiring a shared MCP server. The `crossSessionInbound: refuse` + deny rules for `SendMessage`/`ListAgents` give enterprise `governance_need: hard` profiles a control surface that was absent before.

## Preliminary interpretation
Current best reading:
- **Level 4c — Capability Layer** (primary: native agent-to-agent tool calls via ListAgents/SendMessage)
- **Level 2 — Harness Layer** (secondary: part of Claude Code's session management and coordination substrate)

## Status
- Active feature as of CC v2.1.224; stable enough for tracking
- Complements: agent teams (supervised multi-session), background agents, Remote Control
- Distinct from: claude-peers-mcp (2026-04-07, third-party SQLite broker), oh-my-claudecode (2026-03-28, orchestration wrapper)
