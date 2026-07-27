# Research Watch: telepty — Multi-Machine AI Agent Session Control Plane

- Repo/Link: https://github.com/dmsdc-ai (Show GN, exact repo slug unconfirmed)
- Source: GeekNews (Show GN, 2026-07-27)

## Why this is worth watching
As AI coding agents (Claude Code, etc.) proliferate across developer workstations, the problem of managing sessions across multiple machines becomes real infrastructure. Telepty positions itself as a lightweight control plane for AI CLI sessions distributed across machines — a session-management layer sitting above individual agent runtimes. If the pattern holds, this represents an emerging L2–L3 gap between single-machine harnesses (oh-my-pi, Hermes) and full multi-agent platforms (rowboat, multica).

## What stands out immediately
- Targets distributed AI CLI session management specifically (not general SSH multiplexing)
- Named use case: Claude Code sessions across multiple developer machines
- "Control plane" framing suggests centralized visibility + routing, not just SSH relay
- Show GN (community-submitted, early stage) — low star signal, high concept clarity

## Why clawfit should care
The registry currently has no tool addressing cross-machine agent session management. If telepty (or a competing tool) matures, it would slot between L1 single-machine runtimes and L3 team harnesses — a currently untracked architectural tier. A `deployment_scope: [single-machine | multi-machine | kubernetes]` field would be needed to differentiate this class.

## Preliminary interpretation
Current best reading:
- **Level 2–3 — Meta wrapper / Team harness** (session routing across machines, not just local CLI orchestration)

## Status
- First signal. Show GN with no star count visible. Tracking for second signal.
- Schema gap identified: `deployment_scope: [single-machine | multi-machine | kubernetes]`
