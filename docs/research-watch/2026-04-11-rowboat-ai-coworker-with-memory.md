# Research Watch: rowboat — Open-Source AI Coworker with Memory

- Repo/Link: https://github.com/rowboatlabs/rowboat
- Source: GitHub Trending

## Why this is worth watching
rowboat positions itself as an "AI coworker" rather than a coding assistant — a framing shift that implies persistent task ownership across sessions. With 11,716 stars and +507 today, it is growing steadily. The memory-native architecture distinguishes it from Level 1 base agents that treat sessions as stateless: rowboat's memory is built-in, not a plugin.

## What stands out immediately
- "Coworker" framing: persistent identity and task context across sessions, not just per-prompt help
- Memory is first-class, not an add-on MCP or Level 4a plugin
- TypeScript, suggesting web/cloud-first deployment model
- Targets teams ("coworker" implies collaborative context), not solo developers
- Directly competes with Hermes Agent's adaptive runtime, but from a different angle (collaboration vs. self-improvement)

## Why clawfit should care
rowboat represents a different architectural choice from the stateless base agents dominating Level 1. For orgs that need `statefulness: session` or `statefulness: persistent`, rowboat is a native option vs. bolt-on memory (cipher, claude-mem). The recommendation engine should distinguish between tools where memory is primary vs. tools where memory is an add-on. rowboat belongs in Level 1 with a `memory: native` signal.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtime / primary agent surface** (memory-native subtype)

## Status
- New entry, high signal. 11.7k stars. Add to registry. Monitor statefulness model and team-collaboration features vs. Hermes Agent's session persistence approach.
