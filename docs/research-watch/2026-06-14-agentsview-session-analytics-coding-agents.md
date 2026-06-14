# Research Watch: AgentsView — Session Intelligence Analytics for Coding Agents

- Repo/Link: https://github.com/kenn-io/agentsview
- Source: GitHub Trending (190 stars today, 2,356 total)

## Why this is worth watching
AgentsView is a local-first analytics platform that auto-discovers sessions from 30+ coding agents (Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Cursor, OpenHands, and others) and provides cost tracking, token usage dashboards, and activity heatmaps — without any cloud account or external dependency. It targets the operational blind spot that emerges when teams run multiple agents concurrently: you can't govern what you can't measure.

## What stands out immediately
- Auto-discovers sessions from 30+ agents via standard local paths; zero configuration
- Full-text search (FTS5) across session message content
- Per-session and per-model token cost breakdown with live updates via SSE
- PostgreSQL backend option for team-level dashboards (vs. SQLite for local solo use)
- Self-described as "100x faster cost tracking than ccusage"
- MIT license, Go + TypeScript + Svelte, 2.4k stars

## Why clawfit should care
This is a first signal for **session-scoped cost and performance analytics** as a distinct L5 sub-type — distinct from Spanlens (L5, full LLM-call tracing + eval, Docker-deployed) and NVIDIA SkillSpector (L4, pre-admission static skill scanning). AgentsView operates *after* sessions run, reading artifact traces rather than intercepting API calls; the offline/local posture distinguishes it from cloud observability platforms. Directly relevant to clawfit's `monthly_budget` scoring dimension: a tool that surfaces per-agent cost granularity helps organizations enforce budget constraints without changing their agent selection.

## Preliminary interpretation
Current best reading:
- **Level 5 — Observability / Session-scope analytics sub-type (first signal)**

L5 secondary weak: the team dashboard mode (PostgreSQL backend) introduces a cross-session governance layer that approaches L3 characteristics; treat as unconfirmed.

## Status
- First signal; 2.4k stars below the 5k registry threshold
- No map mutation applied; single-signal rule applies
- Registry candidate for `task: code-gen`, `role: developer`, `network: offline`, `governance_need: hard` profiles (budget tracking is a hard-governance feature)
- Promotion threshold: 5k stars OR confirmed team-dashboard adoption by a second independent project report
