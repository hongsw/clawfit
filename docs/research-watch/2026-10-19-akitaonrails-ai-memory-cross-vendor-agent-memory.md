# Research Watch: akitaonrails/ai-memory — Cross-Vendor Long-Term Memory for Agent CLIs

- Repo/Link: https://github.com/akitaonrails/ai-memory
- Source: GitHub Trending (10,463 stars, +512 today)

## Why this is worth watching
A Rust library that gives coding agent CLIs persistent long-term memory, with an explicit goal of enabling handoff between different agent vendors (Claude Code, Codex, Cursor, etc.). As developers switch agents or split work across tools, shared persistent memory becomes a coordination layer.

## What stands out immediately
- Written in Rust — low-latency, low-overhead memory backend for CLI-adjacent use
- Explicitly targets cross-vendor portability, not single-agent lock-in
- Stores agent context across sessions, enabling continuity that most CLIs lack today
- +512 stars in a single day suggests strong developer resonance

## Why clawfit should care
clawfit's recommendation logic currently treats each agent as stateless at selection time. If persistent cross-vendor memory becomes standard infra, it changes filter logic: agents running against a shared memory layer are substitutable in new ways. This is also a direct complement to clawfit's harness-layer (Level 2) tracking.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Wrapper Layer** (memory infrastructure bolted onto coding agent CLIs)
- Adjacent to Level 3 (Research-Loop / State) given cross-session persistence semantics

## Status
- Tracking: new, high star velocity, monitor for integration into major harnesses
