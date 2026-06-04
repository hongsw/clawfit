# Research Watch: Hermes WebUI — Browser and Mobile Interface for Hermes Agent

- Repo/Link: https://github.com/nesquena/hermes-webui
- Source: GitHub Trending

## Why this is worth watching
Hermes WebUI brings the Hermes Agent (tracked 2026-04-06, now ~27k stars) to browser and mobile with near-1:1 CLI parity: 9.9k stars, 1.4k forks, 5,303 tests across 488 test files. Its appearance on GitHub Trending signals that the Hermes ecosystem is maturing from a CLI-only tool into a multi-surface system — a pattern seen with Warp (terminal → agent-native client) and cmux (terminal multiplexer → agent UX layer).

## What stands out immediately
- No build step required (Python + vanilla JS) — low deployment friction
- Tool call visualization inline with chat — transparency into agent actions
- Session management: pinning, projects, tagging, archiving
- Cron job scheduling via Tasks panel — persistent autonomous behavior from a browser tab
- Mobile-responsive, voice input via Web Speech API
- Profile switching without server restart

## Why clawfit should care
This is an L6 interface-layer maturation signal for an L1 base runtime. The Hermes ecosystem now covers CLI (L1), WebUI (L6), and the paperclip adapter bridge (L4c). For clawfit scoring: tools with multi-surface interfaces should receive higher `setup_complexity` credit for their low-friction access modes. The WebUI makes Hermes accessible to `primary_role: exec` and `primary_role: pm` profiles who would not install a CLI agent — a persona shift worth tracking in the registry entry for `Hermes Agent`.

## Preliminary interpretation
Current best reading:
- **Level 6 — User Interface Layer** (browser + mobile front-end for L1 Hermes Agent runtime)

## Status
- Tracking: L6 maturation signal for Hermes ecosystem; no separate registry entry needed — update existing Hermes Agent entry if exec/pm roles are confirmed
