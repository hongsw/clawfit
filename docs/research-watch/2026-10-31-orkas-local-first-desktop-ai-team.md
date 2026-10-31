# Research Watch: Orkas — Local-First Desktop AI Team Platform

- Repo: https://github.com/Orkas-AI/Orkas (⭐6,018)
- Source: GitHub Trending (all languages, daily, 2026-10-31)

## Why this is worth watching

Orkas is a local-first desktop app (Electron, TypeScript) that runs a team of 16 specialist AI agents plus a Commander agent on the user's machine. Rather than replacing external coding agents, it coordinates them: Claude Code, Codex, OpenCode, OpenClaw, and Hermes-Agent can each be assigned to a project alongside Orkas's own specialists. The structure is a Commander-plus-specialists delegation model, not a flat multi-agent network.

The local-first stance is a design choice with concrete consequences: API keys and project data stay on disk by default, models can be served from a local OpenAI-compatible endpoint, and the architecture does not require cloud sync to function. This positions Orkas differently from cloud-hosted multi-agent platforms (OpenBot, Lobehub CAO) while sharing their agent-coordination ambition.

## What stands out immediately

- **Three-tool delegation model**: Commander uses `dispatch_to` (named agent, returns result), `hand_off_to` (transfers remaining work), and `run_worker` (isolated anonymous sub-task) — a small, typed coordination API rather than a message-bus or DAG scheduler
- **Per-agent memory scopes**: each specialist has private skills and memory separate from the project scope and other agents' memories; memory isolation is structural, not a convention
- **Library with SQLite vector index**: local document store uses sqlite-vec for semantic search over ingested codebases, docs, and PDFs — no external vector service dependency
- **Background self-assessment**: when idle, agents run reviews that can update their own skill and self-assessment records — a lightweight in-process skill-learning loop (adjacent to but distinct from the Sakana MASS / ASPIRE agentic skill-discovery signals from Oct 2026)
- **Scheduled automations and connectors**: Gmail, Notion, Slack connectors enable ongoing workflows beyond single-prompt sessions; to-dos with Auto-advance support multi-step task chains
- **CLI agent coordination**: accepts Claude Code, Codex, and other CLI agents as external workers alongside built-in specialists — treats coding agents as a capability, not a competitor
- **Platforms**: packaged installers for macOS and Windows; Linux from source; TypeScript with Node.js 22.12+ minimum

## Why clawfit should care

Orkas occupies a gap in the current registry: a local-first desktop multi-agent host that is not a coding-agent harness (Cursor, Windsurf, Claude Code) and not a cloud coworker platform (OpenBot). Its CLI agent coordination feature means it is the first tracked tool to use other registered clawfit agents (Claude Code, Codex) as sub-workers inside a broader orchestration layer — a meta-harness pattern.

The `statefulness: session` and `statefulness: persistent` scoring distinction gains relevance here: Orkas projects carry goals, rules, memory, and files across sessions, which is closer to `persistent` than session-scoped agents, but the underlying coding agents it delegates to are session-scoped. A recommendation profile that needs persistent project memory plus coding agent execution would now have a local-first option.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness / Wrapper** (primary): Commander + specialist orchestration model, local agent host with structured delegation
- **Level 6 — Human Interface** (secondary): packaged desktop app with task management, connectors, and coworker-style UX analogous to OpenBot but local

## Claims to verify

- Whether the background self-assessment reviews are genuinely skill-updating (write back to a skill record) or advisory only (display only); the distinction matters for the "memory and learning" L5 classification
- Whether CLI agent coordination (Claude Code, Codex) runs in isolated processes or shares the Orkas process namespace
- Whether sqlite-vec usage is embedded (bundled) or requires a separate install; affects offline score
- Creation date of the repository: "© 2026" and 820 commits visible, but no first-release date confirmed; age matters for the `genuinely new` assessment

## Status

- New signal; not previously tracked
- Registry eligibility: below 5k threshold — wait (6,018 is above 5k — barely qualifies for consideration); however, schema fit is ambiguous (Orkas is a meta-harness host, not an agent itself) and deterministic cost/latency data is not publicly available — no registry addition at this time
- Watch for: whether CLI agent coordination pattern (using coding agents as sub-workers) appears in other L2 platforms — would be a two-signal candidate for a companion axis note on "coding agent as capability primitive"
