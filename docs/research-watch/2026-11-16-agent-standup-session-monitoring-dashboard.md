# Research Watch: Agent Standup

- Repo/Link: https://agent-standup.com (GeekNews topic page)
- Source: GeekNews (Show GN)

## Why this is worth watching
Agent Standup is a tool that displays Claude Code and Codex sessions as a Korean video-meeting-style view, letting developers track the status of multiple agent sessions at a glance. It is the first signal for an **agent session monitoring dashboard** as a distinct product category — separate from the agents themselves, separate from fleet managers (Orca, OpenMausBot), and separate from inline approval prompts. The video-meeting metaphor is a novel UX framing for multi-agent visibility.

## What stands out immediately
- Video-meeting-style UI for agent sessions (novel presentation metaphor)
- Supports Claude Code and Codex simultaneously in one view
- Korean-originated (GeekNews front page, Show GN post)
- Positioned as observability, not control — you watch, not approve
- No star count available (hosted product, not purely OSS)

## Why clawfit should care
clawfit currently has no L6 (Human Interface Layer) tools focused specifically on agent session monitoring. This is a different category from chat UIs (claudecodeui), plan review workspaces (plannotator), and fleet managers (OpenMausBot). As users run more concurrent agent sessions, a lightweight session-status dashboard becomes a recommendation-worthy tool type. The `team_size: mid | large` profiles that currently recommend Claude Squad or LoopForge for multi-agent coordination might also benefit from a passive monitoring layer.

## Preliminary interpretation
Current best reading:
- **Level 6 — Human Interface Layer** (passive agent session monitor / observability dashboard)
- Secondary L2 (wraps agent session state without controlling it)

## Status
- First scan: 2026-11-16
- Registry action: deferred — no star count / OSS repo confirmed; hosted product with unclear pricing
- 📡 Note: first signal for "passive agent session monitoring dashboard" as a distinct L6 sub-type; watch for a second tool (OSS or commercial) that positions itself as a session-level observability layer without an approval/control mechanism; would confirm this as a canonical L6 sub-type
