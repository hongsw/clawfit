# Research Watch: OpenMAIC — Multi-Agent Interactive Classroom

- Repo/Link: https://github.com/THU-MAIC/OpenMAIC
- Source: GitHub Trending

## Why this is worth watching
OpenMAIC deploys a coordinated swarm of specialized agents (teacher, coach, evaluator, peer) into a single learning session, making it one of the clearest real-world demonstrations of multi-agent orchestration for a non-coding task. It earned 3,128 GitHub stars in a single day, signaling rapid adoption. The pattern — heterogeneous roles collaborating in one context — is directly analogous to enterprise agent-of-agents architectures.

## What stands out immediately
- Single-click deployment of a full multi-agent classroom session
- Distinct agent roles (instructor, evaluator, peer learner) communicating within one harness
- TypeScript implementation, suggesting browser/server deployment is the primary target
- No specialized hardware required — runs cloud-hosted

## Why clawfit should care
This is a live example of Level 3–4 orchestration (agent harness + multi-agent coordination) applied to education rather than code. It validates that the multi-agent pattern generalizes beyond dev tooling. Any org-fit scoring that treats "orchestration" as a rare/advanced use case should account for how accessible this pattern is becoming.

## Preliminary interpretation
Current best reading:
- **Level 3 — Harness/Wrapper Layer** (orchestrates multiple specialist agents under one session)
- Secondary signal: **Level 4 — Research-Loop / Multi-Agent Systems** (agents interact and evaluate each other)

## Status
- Follow-up signal — first noted in reference-levels.md 2026-08-30 at 22k stars; today earned +3,128 stars in one day (now 29k+), indicating accelerating adoption rather than plateau. Watching for whether educational orgs begin forking for internal training.
