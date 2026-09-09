# Research Watch: context-mode — MCP Context Window Optimizer

- Repo/Link: https://github.com/mksglu/context-mode
- Source: GitHub Trending

## Why this is worth watching
context-mode sandboxes tool output to achieve 98% context window reduction, persists session memory, and enforces routing across 17 platforms via MCP + hooks. 21k stars with +651 today. This directly addresses the #1 practical pain point in long coding-agent sessions: context exhaustion.

## What stands out immediately
- 98% context size reduction claim via tool output sandboxing
- Persists session memory across context resets
- Enforces MCP routing across 17 platforms from one config
- TypeScript, 21k stars
- "Ask HN: How Do You Manage Skill Files?" (GeekNews today) is the community-level signal for the same pain point

## Why clawfit should care
context-mode is a meta-layer above individual coding agents — it wraps MCP + hooks to normalize behavior. This is analogous to the harness layer but specifically solves context management rather than task orchestration. clawfit's org_fit scoring has no "context_management" capability field, and this tool would rank unexpectedly low under current scoring for profiles that need long sessions.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Wrapper Layer** (context + routing management)

## Status
- New — strong candidate for registry addition; addresses gap in current tool taxonomy
