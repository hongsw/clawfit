# Research Watch: OpenRig — Declarative Multi-Agent Team Orchestrator

- Repo: https://github.com/mvschwarz/openrig (⭐804)
- Source: GitHub Trending daily (+114 today)

## Why this is worth watching

OpenRig treats a team of coding agents as a declared topology, not as individually-launched processes. Its `RigSpec` YAML describes which agents exist, how they relate, and what happens if one fails — and a single `rig up` materializes the whole fleet. This is a structurally different abstraction than existing L2 harnesses (which wrap a single agent) or L3 SSOT files (which govern a single agent's behavior): OpenRig's unit of management is a *named agent team*, not an agent instance.

## What stands out immediately

- `RigSpec` YAML defines pods (agent instances), topology (relationships), and continuity policies (restart behavior) as a first-class config file — declarative, not imperative
- Supports both Claude Code and Codex CLI as first-class agent types within the same rig
- Cross-agent messaging built in: `rig send`, `rig broadcast`, `rig chatroom` — agents can communicate without leaving the abstraction
- `rig snapshot` / `rig restore` for team-state persistence: entire agent team configs are named and re-loadable
- Discovery mode: detects running agent sessions and brings them under management retroactively
- Implementation: Node.js daemon with Hono HTTP, SQLite control plane, tmux runtime adapters; MCP server exposed at the top layer
- 804 stars in what appears to be early development; +114 in one day suggests landing on GitHub Trending is recent viral momentum

## Why clawfit should care

OpenRig is the second signal (after TencentCloud/Octop, same scan) for a pattern that can be called "declarative agent team topology configuration" — distinct from governance SSOT (AGENTS.md, CLAUDE.md define *what* an agent should do) and from orchestration SDKs (CrewAI, LangGraph define *workflows*). RigSpec defines *who exists and how they're related*. For clawfit, this changes the selection question: not just "which agent?" but "which team topology for this org's workflow?" A multi-model shop running both Claude Code and Codex would benefit from tools that normalize their interface — but that introduces a new dimension (topology management) not yet in clawfit's scoring.

## Preliminary interpretation

Current best reading:
- **Level 2/3 — Harness + Team Topology Layer**: primary L2 (multi-agent orchestration harness) with L3 characteristics (team-level SSOT for agent team configuration)
- The `RigSpec` file is closer to a Kubernetes pod spec than to CLAUDE.md — it's a runtime topology declaration, not a behavior governance file

## Claims to verify

- Whether `RigSpec` supports heterogeneous model configurations (different LLMs per pod)
- Maturity of the MCP server layer — whether it can be used to manage rigs from other agents
- Whether "continuity policies" include failure recovery or just restart behavior
- 804 stars may include GitHub Trending inflation — worth checking age and organic growth rate

## Status

- Tracking; 804 stars on GitHub Trending 2026-09-27
- Below registry threshold (no deterministic cost/latency data; no MCP server direct inference costs)
- **Second signal for "declarative agent team topology" pattern** alongside TencentCloud/Octop (same scan day) — cross-day confirmation pending before canonical sub-type consideration
