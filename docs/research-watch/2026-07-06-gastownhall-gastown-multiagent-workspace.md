# Research Watch: gastownhall/gastown — Multi-Agent Workspace Manager

- Repo/Link: https://github.com/gastownhall/gastown
- Source: GitHub Trending (2026-07-06, 16,365 stars, Go)

## Why this is worth watching
Gas Town is a multi-agent workspace manager — a Go-based runtime that coordinates multiple coding agents across a shared workspace. With 16k+ stars on trending, it joins a cluster of tools (Claude Squad, Crystal, Superset, herdr) competing in the "multi-agent session orchestration" tier. The Go implementation and "workspace manager" framing distinguish it from tmux-style multiplexers and suggest a more structured approach to agent task routing.

## What stands out immediately
- Go-based (performance-oriented, single binary distribution)
- "Workspace manager" framing — implies project context isolation across agents
- Organic trending without prior research-watch coverage (prior gastownhall entry was for "beads", a separate memory project from the same org)
- 16k stars places it in the same tier as Claude Squad and herdr

## Why clawfit should care
Level 2 (harness/wrapper) is the most crowded and competitive layer in the taxonomy. Gastown adds Go-native workspace routing to a field dominated by TypeScript (Superset, Crystal) and Python (Claude Squad). If it demonstrates a meaningfully different approach (e.g., project-isolated multi-agent sessions without a desktop UI), it may warrant a registry entry. More data needed on feature differentiation.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Multi-Agent Session Manager**

## Status
- Tracking: candidate for registry addition pending feature verification
