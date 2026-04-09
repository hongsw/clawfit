# Research Watch: obra/superpowers — Agentic Skills Framework

- Repo/Link: https://github.com/obra/superpowers
- Source: GitHub Trending

## Why this is worth watching
`superpowers` is a composable, cross-platform agentic skills framework with 141k stars and 2,028 daily trending gains — one of the highest-velocity signals on GitHub today. It wraps the full software development workflow (spec → plan → execute → test → review) into auto-activating skills that work across Claude Code, Cursor, Codex, OpenCode, GitHub Copilot CLI, and Gemini CLI. Its cross-platform portability is novel: the same skill pack runs on any major coding agent.

## What stands out immediately
- **Platform reach**: Available in Claude Code marketplace, Cursor, Codex, OpenCode, Copilot CLI, Gemini CLI — first skill pack explicitly listed for 6+ runtimes
- **Auto-activation by context**: Skills fire based on task context (brainstorm → plan → execute), not manual invocation
- **TDD-enforced workflow**: Built-in RED-GREEN-REFACTOR cycles; agents cannot self-certify completion
- **Multi-agent dispatch**: Subagent-driven parallel implementation with plan-based checkpoints
- **Philosophy**: "Work autonomously for a couple hours without deviating from the plan" — harness reliability as primary design goal

## Why clawfit should care
`superpowers` exemplifies the emerging Level 3 pattern: an **executable SSOT** that simultaneously reads as a workflow guide (for humans) and executable constraints (for agents). Its cross-runtime portability is a new signal: skill packs are decoupling from specific base agents, which changes how clawfit should weight `level` and `category` dimensions. The 141k star count also makes it a strong candidate for the registry as a workflow benchmark reference.

## Preliminary interpretation
Current best reading:
- **Level 3 — Team harness / executable SSOT** (primary: structured workflow methodology)
- **Level 4b — Skill pack** (secondary: distributed via Claude marketplace and Cursor plugin system)

## Status
- New — added to registry as `superpowers` (Level 3/4b dual classification)
- Added to reference-levels.md Level 3 section
