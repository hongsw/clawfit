# Research Watch: pingdotgg/t3code — Cross-Platform Control Surface for AI Coding Agents

- Repo: https://github.com/pingdotgg/t3code (⭐17,940)
- Source: GitHub Trending (2026-08-10, +388 today)
- License: not specified (very early stage — check repo)
- Language: TypeScript / Node.js

## Why this is worth watching

t3code is Theo's (Ping Labs, creator of the T3 Stack) approach to the agent control surface problem: as AI coding agents (Claude Code, Codex, Cursor, Grok Build, OpenCode) multiply, developers increasingly need a unified way to issue instructions, monitor progress, and grant permissions across agents from whatever device they are using. t3code provides a mobile app (iOS/Android), web app, and Electron desktop client that all connect to the same agent session on a developer's machine.

The 17.9k stars reached within the first days of being listed as "very very early" are Theo's audience effect — not independent discovery. The practical question is whether the problem it solves (cross-device agent control) is architecturally significant enough to survive the early-adopter spike and establish a stable user base. Given that paseo (2026-08-08, 12.8k stars, L2/L6) solved a subset of this problem for OpenCode specifically, and openchamber (2026-08-09, 7.8k, L2/L6) added a cross-device surface for OpenCode, t3code is the first attempt at a vendor-agnostic cross-device control surface.

## What stands out immediately

- **Vendor-agnostic multi-agent support:** works with Claude Code, Codex, Cursor, Grok Build, and OpenCode — this is the widest agent support surface in the tracked corpus for a UI-layer tool; paseo and openchamber both require OpenCode as the backend
- **Cross-device control surface:** iOS app, Android app, Electron desktop client, and web app — four interfaces for a single agent session; a developer on mobile can approve permissions, review diffs, and issue commands to an agent running on their workstation
- **Permission modes and keyboard shortcuts:** explicit permission delegation — the mobile app can grant or deny permissions requested by the agent without requiring the developer to be at their workstation; keyboard shortcuts in the desktop client suggest a keyboard-driven workflow philosophy
- **Remote access built-in:** "remote-ready" framing; developers can control agents running on a home machine from their phone or from a different computer without setting up SSH tunnels or VPNs
- **Very early stage:** developers state "we are very very early in this project" and expect bugs; contributions limited to small fixes; this is a seed-stage signal, not a production-ready tool
- **npx t3@latest:** zero-install test path for quick evaluation — same pattern as OpenCode's install ergonomics
- **Package manager distribution:** Homebrew (macOS), winget (Windows), AUR (Arch Linux) — all three major developer package managers, which suggests infrastructure investment ahead of feature completeness
- **17.9k stars on first trending day:** high-signal for problem resonance, not for product maturity; Theo's prior projects (T3 Stack, T3 OSS) have 20k–60k stars; this is audience transfer, not organic discovery

## Why clawfit should care

t3code occupies a position in the taxonomy that clawfit currently does not model: the **harness control surface** — the UI through which humans interact with the harness, distinct from the harness itself. paseo and openchamber both package the harness and the control surface together; t3code is an attempt to decouple the control surface from the harness entirely.

If this decoupling succeeds, it would suggest a pattern where harnesses (prime-agent, openchamber, LifeOS) expose a standard control API, and control surfaces (t3code, paseo's mobile UI, openchamber's web app) consume it. A `control_surface_api: true/false` axis in the harness schema would capture whether a harness is designed to expose control to external interfaces, or whether it is a closed system.

The vendor-agnostic multi-agent support is the structural differentiator from paseo and openchamber. If t3code can maintain parity with five or more agent backends without becoming a lowest-common-denominator interface, it would establish the L6 control surface as a distinct architectural layer from the L2 harness — currently the two are conflated in openchamber and paseo.

The mobile-first interaction model (approve permissions from your phone) is a new interaction pattern not previously tracked. It implies asynchronous agent supervision: the agent runs unattended, requests permission, and the human responds from wherever they are. This is architecturally similar to humanlayer (2026-07-24, L6 — async human approval layer for agents) but at the harness UI level rather than the orchestration API level.

## Preliminary interpretation

- **Level 6 — Human Interface** (primary): cross-platform UI layer for issuing instructions to, monitoring, and granting permissions to AI coding agents; not a harness, not a capability layer, but the interface surface between human and harness
- **Level 2 — Agent Harness** (secondary): if t3code evolves to schedule tasks, manage sessions, or store state across agent runs, it will creep into L2 territory; currently it is a control surface, not an orchestrator

Cross-reference: paseo (2026-08-08, L2/L6 — cross-device control for OpenCode, 12.8k★), openchamber (2026-08-09, L2/L6 — cross-device for OpenCode + Fusion synthesis, 7.8k★), humanlayer (2026-07-24, L6 — async human approval API for agents). t3code is closest to humanlayer in intent (asynchronous human-in-the-loop) but operates at the UI layer rather than the orchestration API layer.

## Claims to verify

- **Vendor-agnostic agent protocol:** whether t3code connects to each agent via a common protocol (stdin/stdout control plane, a t3 agent SDK, or agent-specific adapters); if it requires agent-specific integrations for each of the five supported agents, it may become a maintenance burden as agents change APIs
- **Permission delegation security model:** verify what credentials or authentication the mobile app uses to grant permissions to an agent running on a separate machine; a compromised phone could potentially approve dangerous agent actions if the permission model is not carefully bounded
- **Remote access transport:** what relay or tunnel infrastructure t3code uses for cross-device remote access (Theo-hosted relay, P2P, self-hosted relay); privacy and data routing depend on whether agent instructions transit a Ping Labs server
- **Early-stage stability:** the project is explicitly pre-stable; check whether core interfaces (agent connection, permission delegation) are documented as stable or subject to breaking changes
- **Stars vs. active users:** Theo's audience effect inflates initial star counts; watch weekly active user metrics (if published) as a more reliable adoption signal than star trajectory

## Status

- Active development, explicitly very early stage; TypeScript / Node.js
- 17,940★ at time of scan; Theo's audience-driven star count — watch for stabilization
- Registry eligibility: no — does not map to agents.json, llms.json, or hardware.json schema; would require a new `interfaces.json` registry category; also blocked by no deterministic cost/latency data (it is a free control surface, not an inference provider)
- Schema watch: `control_surface_api: true/false`; `device_targets: [desktop | mobile | web | electron]`; `agent_backends: [claude-code | opencode | codex | cursor | grok-build | multi]`; `approval_model: [synchronous | asynchronous | autonomous]`
- Cross-reference: paseo (2026-08-08, L6 — OpenCode mobile control), openchamber (2026-08-09, L6 — OpenCode cross-device), humanlayer (2026-07-24, L6 — async approval API)
