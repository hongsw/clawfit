# Research Watch: QM — Multiplayer Agent Harness

- Repo/Link: https://github.com/yc-software/qm
- Source: Hacker News (393 pts, 89 comments — 2026-08-01)

## Why this is worth watching
QM is a YC-backed team-level agent harness that runs agents inside Slack and a web app simultaneously, with isolated per-employee workspaces and shared organizational channels. At 393 HN points it has strong traction, and multi-model support (Claude Code, OpenCode, Codex, Pi) positions it as a vendor-agnostic workspace layer.

## What stands out immediately
- Dual interface: Slack-native AND web app, both sharing one backend
- Isolated personal workspaces with admin promotion of shared skills
- Three security postures: Strict (approve every call), Auto (content-screened), Dangerous (unrestricted)
- Background job execution via crons and watches (persistent agent tasks)
- Predeclared command policies and audit trails — governance built in

## Why clawfit should care
QM sits squarely in Level 2 (harness layer) and targets the "team" segment that neither solo CLI tools (Claude Code/Aider) nor enterprise platforms (Aperant/OpenHands) serve well. Its governance postures are directly relevant to clawfit's `governance_need` dimension, and the multi-model backend makes it a strong candidate for mid/large teams with hard policy requirements.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Workspace Layer** (team-scoped orchestration with skill sharing and security controls)

## Status
- Tracking — new entry; high-signal (HN front-page, YC-backed). Add to tools_registry.json.
