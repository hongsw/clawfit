# Research Watch: Starnet — Local-First Desktop Agent Harness

- Repo: https://github.com/androoAGI/starnet (⭐386)
- Source: GitHub Trending
- Language: JavaScript

## Why this is worth watching

Starnet describes itself as "a living pixel-art station where real AI agents do real work." The aesthetic framing is unusual — a pixel-art desktop environment as a harness surface — but the underlying architecture claim is specific: local-first, desktop-native, where AI agents do actual work (file operations, code execution, web access) rather than just generating text in a chat window. At 386 stars it is early-stage by any conventional measure, but the GitHub Trending appearance alongside much larger projects suggests it is drawing attention beyond its current size.

The "living" framing is the analytically interesting part: Starnet positions the agent's workspace as a persistent, observable desktop environment rather than a stateless session. This is a different point in the design space from CLI-based harnesses (Codex, Claude Code) and from browser-based harnesses (browser-use, computer-use) — it is a self-contained, visual, local-first agent operating environment.

## What stands out immediately

- Desktop-native architecture: agents operate inside a self-contained local environment rather than over an API bridge
- Pixel-art visual surface is not merely cosmetic — it makes agent activity observable at a glance (which agent is active, what it is working on, current state)
- Local-first: no cloud dependency by default; agent compute and storage stay on the operator's machine
- JavaScript/TypeScript implementation makes it accessible to a broad contributor base
- "Real work" framing: explicitly not a demo or toy — agents execute actual tasks (files, code, web)
- Early-stage (386★) but active on GitHub Trending — unusual for a repo this size

## Why clawfit should care

Starnet introduces an aesthetic-first approach to agent harness design: the visual metaphor is functional, not decorative. This is the inverse of most agent interfaces, where observability is added as an afterthought. If the pixel-art metaphor successfully lowers the cognitive cost of monitoring multi-agent activity (each agent is a character doing something visible), it could point toward a new class of L6 interface patterns for local-first agent deployments.

For clawfit's scoring, Starnet is a weak additional signal in the emerging "agent-side visualization" cluster (Whiteboard today at L6 is the stronger signal). Both tools address the same underlying gap: humans cannot easily observe what agents are doing. Whiteboard does it through a shared canvas in an IDE; Starnet does it through a local desktop environment with visual agent representations.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/Wrapper Layer** (primary: local-first desktop agent harness with persistent state)
- **Level 6 — Human Interface Layer** (secondary: pixel-art observability surface for agent activity)

## Claims to verify

- What specific task execution capabilities agents have inside Starnet (file access, code execution, web browsing — all claimed but not independently verified)
- Whether the local-first claim means no cloud calls or only no cloud storage (agents likely still call external LLM APIs)
- Whether the pixel-art surface is an aesthetic layer over a standard harness protocol or a custom implementation
- Whether the JavaScript runtime isolates agent execution from the host system (security posture unclear)

## Status

- Above minimum threshold (386★ ≥ 100); below registry threshold (5k)
- Very early-stage; 386 stars with a Trending appearance is a real but thin signal
- **Weak second signal** for "agent-side visual observability" (Whiteboard today is the stronger signal in this cluster); not yet sufficient for canonical sub-type promotion
- Monitor star trajectory; if it passes 1k in 30 days, write a deeper research note
