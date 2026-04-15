# Research Watch: Claude Code Routines — Serverless Agent Execution

- Repo/Link: https://code.claude.com/docs/en/routines
- Source: Hacker News

## Why this is worth watching
Anthropic has launched Claude Code Routines (research preview) — saved agent configurations that run autonomously on Anthropic-managed cloud infrastructure, triggered by schedule, HTTP API, or GitHub events. This is the first first-party "serverless agent execution as a service" offering from Anthropic, removing the local-machine dependency entirely and turning Claude Code from an interactive tool into an always-on background automation layer.

## What stands out immediately
- Three trigger types: **schedule** (cron-style, min 1h interval), **API** (HTTP POST with bearer token + optional `text` payload), **GitHub** (PRs, pushes, issues, CI runs, 18 event types)
- Routines run as full Claude Code cloud sessions: shell commands, Skills, MCP connectors — no permission prompts
- Per-run sessions are accessible in the web UI for review, PR creation, or manual continuation
- `/schedule` CLI command creates routines conversationally; `/schedule list`, `/schedule update`, `/schedule run` for management
- Supported on Pro, Max, Team, Enterprise plans; counts against daily run allowance
- GitHub App install required for GitHub triggers; Anthropic-managed cloud environment with configurable network access and env vars

## Why clawfit should care
This directly introduces a new statefulness value — effectively `managed_hosted` + `event_driven` — that the current scoring model doesn't distinguish from "session" or "persistent." Orgs considering routines for CI/CD automation need different latency, governance, and network criteria than interactive sessions. Additionally, the trigger-by-GitHub-event pattern means agentic coding work can now be provoked entirely outside the developer's terminal, which changes the `roles` scoring dimension (PM, exec can now initiate agent runs via GitHub issues without touching a CLI).

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layers** (managed cloud runner on top of Claude Code base agent)
- *Also* spans **Level 3 — Team workflow / executable SSOT** (GitHub event triggers encode org workflow as automation)

## Status
- Research preview (April 2026); breaking changes expected; track `/schedule` CLI evolution and GitHub App adoption
