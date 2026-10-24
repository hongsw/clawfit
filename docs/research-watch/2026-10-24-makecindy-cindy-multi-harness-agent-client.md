# Research Watch: Cindy — Multi-Harness Open-Source Agent Client

- Repo: https://github.com/makecindy/cindy (⭐4k)
- Source: GitHub Trending (all languages, 2026-10-24)

## Why this is worth watching
Cindy positions itself as the "single client" that switches between Claude Code and Codex mid-task while keeping memory, skills, and tools persistent across harness changes. This addresses a practical pain point: developers lock themselves to one agent harness per project even when a different harness might handle a specific subtask better. The multi-harness client pattern is architecturally distinct from both multi-agent orchestration frameworks (like crewAI or AutoGen) and terminal multiplexers (like Corgi): it maintains task-level continuity across harness boundaries rather than running parallel agents or parallelizing session management.

## What stands out immediately
- Supports Claude Code and Codex as first harnesses; architecture is designed for additional harness plugins
- Memory, skills, and MCP integrations persist when switching harnesses mid-task — no context loss at the boundary
- Desktop Electron client and mobile Expo/React Native client — cross-platform from day one
- Browser, computer, and phone control built in: desktop-class tool use without per-harness setup
- IM and schedule integration: the agent picks up work from Slack, calendar, and task systems
- Apache-2.0 license with no sign-in requirement: runs on user accounts only
- 573 forks and active PR count suggest community-driven harness additions are already in progress

## Why clawfit should care
Cindy is a direct consumer of clawfit's recommendation output: a user running Cindy would want to know which harness to invoke *for a given task profile*, which is exactly what clawfit recommends. As multi-harness clients become common, clawfit's recommendations shift from "which agent should I use for this project?" to "which agent should this task call right now?" This is a scoping change, not just a new entry.

Registry implication: Cindy itself is not a registry candidate (it is a client, not a harness or model), but it is a strong signal that clawfit should model harness-switching as a first-class use case.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Wrapper** (primary): wraps and routes between existing coding agent harnesses with persistent task context
- **Level 6 — Human Interface** (secondary): desktop and mobile client surfaces for agent task management

## Claims to verify
- Whether harness-switching mid-task is genuinely stateful or whether it is session restart with context replay
- How the memory/skill persistence layer is implemented — local files, SQLite, or a cloud sync service
- Whether the Codex and Claude Code integrations use official APIs or screen scraping
- Age of the repository (creation date not surfaced from the trending page)

## Status
- Tracking: new signal, GitHub trending 2026-10-24
- Registry eligibility: not a candidate (client-layer tool); watch for a harness-comparison report citing clawfit
