# Research Watch: Yorishiro — A macOS Terminal Where AI Agents Live

- Repo/Link: https://github.com/sktkkoo/yorishiro
- Source: Hacker News Show HN (31 points, 8 comments, 2026-07-26)

## Why this is worth watching
Yorishiro positions itself not as a terminal *with* AI features bolted on, but as a terminal *designed for* AI agents as first-class residents. This is a different philosophy from tools like Warp or iTerm AI integrations — agents are the primary user, humans are observers.

## What stands out immediately
- macOS-native (Swift/AppKit likely), not Electron
- Explicit "agents live here" framing vs "humans get AI assistance"
- Complements harness-era tooling: if agents need their own terminal context, this fills a gap
- 31 HN points on launch day suggests niche but engaged early audience
- Distinct from existing tracked tools: Grok Build TUI, deepseek-tui, Terax are coding agent TUIs; this is an agent *host*

## Why clawfit should care
The Level 1 (base runtime) layer is expanding beyond CLI coding agents into dedicated agent-native environments. If yorishiro gains traction it would be a Level 1 entry — a terminal OS substrate for agents. Could affect how `statefulness=session` tools are evaluated when the execution environment itself is agent-aware.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Agent Runtime** — macOS terminal designed as agent-native execution host

## Status
- Early-stage (31 HN points on launch). Monitor for GitHub star growth and usage reports.
