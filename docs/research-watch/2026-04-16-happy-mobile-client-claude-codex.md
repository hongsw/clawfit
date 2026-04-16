# Research Watch: Happy — Mobile Client for Claude Code + Codex

- Repo/Link: (GitHub, username not confirmed)
- Source: GeekNews (2026-04-16)
- Tag line: "Open-source remote control client for Claude Code and Codex on iOS, Android, and web"

## Why this is worth watching
The first open-source cross-platform mobile client explicitly targeting both Claude Code and Codex via a CLI wrapper. Mobile access to coding agents has been locked behind proprietary apps (claudecodeui, etc.). A free open-source alternative that works on iOS, Android, and web simultaneously lowers the barrier for exec/PM roles who need to monitor or trigger agent work without terminal access.

## What stands out immediately
- Targets three platforms simultaneously: iOS, Android, web
- CLI wrapper approach — no backend changes needed to agent runtimes
- Open-source + free, distinct from claudecodeui (repo-only)
- Explicit dual-agent support (Claude Code + Codex) from day one signals cross-platform design intent

## Why clawfit should care
This extends Level 7 (human interface layer) for mobile form factors. Currently claudecodeui and pi-generative-ui cover web/desktop. Happy adds mobile as a separate interface category. For `exec` and `pm` roles, mobile access to agent status and trigger is the practical interface. This may warrant a new sub-type in Level 7: mobile-native vs. desktop-native vs. web-based agent interfaces.

## Preliminary interpretation
Current best reading:
- **Level 7 — Mobile interface for agent sessions (new sub-type)**

## Status
- Early stage — track, no stars count available at time of write
