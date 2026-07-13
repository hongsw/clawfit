# Research Watch: background-agents — Async Coding Agent Harness

- Repo/Link: https://github.com/ColeMurray/background-agents
- Source: GitHub Trending Daily #7 (2.3k stars)

## Why this is worth watching
background-agents is an open-source reference implementation of a three-layer async agent dispatch system that explicitly separates orchestration (Cloudflare Workers/Durable Objects) from execution (Modal/Daytona/Vercel sandboxes) from client surface (Slack/GitHub/Linear). This control-plane vs. data-plane split is a recurring production pattern in internal engineering tools but rarely published as open source. At 2.3k stars and trending, it is one of the cleaner open examples of background/async coding delegation as opposed to interactive, session-bound agents.

## What stands out immediately
- Control plane runs on Cloudflare Durable Objects with per-session SQLite and WebSocket hubs — persistent orchestration state without a dedicated server
- Data plane is provider-agnostic: Modal, Daytona, Vercel Sandbox, and OpenComputer are all documented backends; the runtime (OpenCode) is the same across providers
- Async execution model: sessions trigger via cron, Sentry alerts, webhooks, or @mentions — no interactive user session required
- `spawn-task` call allows agents to decompose work into parallel child sessions in separate sandboxes
- Browser automation (headless Chromium) included in sandbox spec — this is not just code execution, it is full agent environment
- Explicitly single-tenant by design: all users must be trusted org members; multi-tenant use requires per-tenant GitHub App installations and access validation
- Credentials brokered short-lived by the control plane; AES-256-GCM encryption with repo-scoped secret scoping

## Why clawfit should care
This is architecturally distinct from interactive coding agents (Devin, OpenCode in interactive mode, Claude Code). It represents **background work delegation** — a task is handed off, the agent runs unsupervised, results surface via PR or Slack thread. The distinction matters for clawfit's `statefulness` filter axis: current options are `stateless` and `session`; this pattern implies a third mode — `background-async`. Any org profiling with `statefulness: background` would need different scoring weights (reliability, rollback, auditability) over interactive-latency. Also notable: the pluggable sandbox backend layer is a direct implementation of what Freestyle, Daytona, and Modal each claim independently.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrapper / harness / orchestration layer** (async agent dispatch harness over a pluggable sandbox data plane)
- Secondary: **Level 7** — Cloudflare Workers control plane and Modal/Daytona backends are infrastructure, not harness logic

## Status
- Active signal: 2.3k stars, GitHub Trending daily. Flag for registry evaluation; priority is resolving whether `statefulness: background` warrants a new filter value in `filters.py`.
