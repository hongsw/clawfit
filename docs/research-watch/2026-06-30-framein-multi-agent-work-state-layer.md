# Research Watch: Framein — Work State Layer for Multi-Agent Transitions

- Repo/Link: https://github.com/framein-dev/framein
- Source: GeekNews front page (2 pts, posted by chunbak)

## Why this is worth watching
Framein solves a specific gap: when a developer switches between Claude Code, OpenAI Codex, and Gemini CLI mid-task, context and decisions are lost and must be re-explained. Framein introduces "task contracts" — shared structured state that any agent can read and write — enabling lossless model handoffs. The framing ("Better prompts help. They do not keep the work intact.") directly challenges the prevailing assumption that prompt engineering is the solution to multi-agent coordination.

## What stands out immediately
- **Four phases**: Start (task contracts) → Challenge (independent model review + structured verdicts) → Switch (model transition via local facts) → Validate (deterministic build/test/risk gates)
- **Universal agent integration**: `/fr:*` slash commands for Claude/Gemini; `$fr-*` project skills for Codex; CLI+JSON for terminal/CI/MCP
- **Local-first, zero deps**: Node 22.5+, 249 tests, Git-friendly JSON snapshots + local SQLite — no cloud relay
- **Pre-release v0.0.6** — early but architecturally complete enough to be meaningful
- **Challenge phase is novel**: invokes independent model review as a built-in quality gate, not an afterthought

## Why clawfit should care
Framein occupies a new sub-layer between L1 (base runtime) and L2 (orchestration harness): a *work state persistence layer* specifically for multi-agent handoffs. The existing registry has no entry capturing this pattern. If Framein or a successor gains adoption, clawfit would need to recommend it alongside (not instead of) the primary agent — a "pairing recommendation" pattern not currently modeled. Also relevant: the Challenge phase is an embedded evaluation gate, intersecting L5.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness/Wrapper** (coordinates across agent runtimes via shared state)
- Secondary: **L5 — Evaluation** (structured model review as built-in quality gate)

## Status
- First signal — 2026-06-30; v0.0.6 pre-release; hold for promotion until public GitHub stars visible and at least one independent review
