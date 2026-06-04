# Research Watch: pi-subagents — Async Subagent Delegation for Pi

- Repo/Link: https://github.com/nicobailon/pi-subagents
- Source: GitHub Trending

## Why this is worth watching
pi-subagents is a Pi framework extension (1.8k stars) that adds async background subagent delegation, parallel execution, worktree isolation, and mid-task intercom to Pi sessions. It is the clearest productization yet of a pattern emerging across multiple frameworks: the parent agent as orchestrator that spawns, monitors, and merges focused child agents.

## What stands out immediately
- Foreground (streaming) and background (fire-and-forget with status check) execution modes
- Six built-in specialist agents: Scout, Reviewer, Worker, Planner, Oracle, Researcher — named by function, not implementation
- Worktree isolation: parallel workers use separate git branches to prevent conflicts
- Intercom bridge: child agents can ask parent for decisions mid-task, preserving human-in-the-loop
- Sequential chains with per-step visibility and live progress tracking
- Natural language invocation: "Use reviewer to review this diff" — no special syntax

## Why clawfit should care
The async delegation pattern in pi-subagents mirrors the orchestration patterns in Claude Squad, DureClaw, and multica but wrapped inside a lightweight Pi-specific plugin. Three signals confirm this pattern is not Pi-specific: Claude Squad (clone-and-delegate), DureClaw (distributed orchestration), and now pi-subagents (session-fork delegation). This is evidence that `task: orchestration` and `statefulness: session` are becoming entangled dimensions — a user who wants subagent delegation needs both orchestration capabilities and persistent session context. Relevant to clawfit's `statefulness` filter axis.

## Preliminary interpretation
Current best reading:
- **Level 3 — Orchestration Primitives** (session-fork delegation, parallel subagent coordination within a single framework)

## Status
- Tracking: third signal confirming parent-orchestrates-child pattern; relevant to statefulness × orchestration axis in scoring
