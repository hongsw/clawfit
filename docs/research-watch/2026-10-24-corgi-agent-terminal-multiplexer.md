# Research Watch: Corgi — Agent Terminal Multiplexer

- Repo/Link: https://corgi.computer/
- Source: Hacker News

## Why this is worth watching
Corgi is a terminal multiplexer explicitly designed for running and supervising multiple AI coding agents simultaneously. As agent-heavy workflows become the norm, a dedicated tool for managing agent sessions, monitoring their status, and tracking token/resource usage represents a new layer of infrastructure between raw terminals and full GUI orchestration.

## What stands out immediately
- Works natively with Claude Code, Codex, Pi, and OpenCode using existing accounts
- Per-agent status markers: working, needs you, finished, idle — keeps humans looped in
- `F1` catchup view and per-file diff view to see everything an agent touched
- `top`-style token usage view across agents
- `corgi --skill` teaches agents how to drive Corgi itself (meta-layer)
- Persistent sessions (tmux-style), worktree support, and workspace auto-organization

## Why clawfit should care
This is a new harness category: the **agent supervisor** layer. Clawfit's recommendation engine currently tracks individual coding agents and orchestration frameworks but not session-management / multi-agent-supervision tools. As developers run 3–10 agents in parallel, Corgi-style tools become a prerequisite layer, affecting how agent recommendations are scoped.

## Preliminary interpretation
Current best reading:
- **Level 3 — Harness / Wrapper layer** (sits atop base agents like Claude Code and OpenCode, multiplexing and supervising them)

## Status
- Tracking: new signal, HN front page 2026-10-24
- Registry candidate: no (tool-runner meta-tool, not a direct recommendation target)
