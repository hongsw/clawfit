# Research Watch: Autolith — Programming Agent with a Live Runtime

- Repo/Link: https://lambda-symbolics.com (Lambda Symbolics OÜ)
- Source: Hacker News front page (105 points, 2026-08-23)

## Why this is worth watching

Autolith is a terminal programming agent embedded directly inside a live SBCL (Steel Bank Common Lisp) image rather than running as a separate orchestration layer. The agent owns its tools, memory, self-modification capability, checkpoints, and recovery within the same running Lisp process — making the runtime itself the agent's substrate rather than an external sandbox.

## What stands out immediately

- **Live image architecture**: Agent runs inside a live SBCL process, not as a subprocess driver; code evaluation, tool execution, and memory persistence all happen inside the same image
- **Self-modification**: Agent can redefine its own tools and behavior at runtime without restarting
- **Checkpoint / recovery**: Lisp image snapshots give the agent "save state" and rollback without an external orchestration layer
- **Common Lisp**: Niche language choice with deep interactive development tradition (SLIME, REPL-driven iteration); the "live image" concept is native to Lisp culture

## Why clawfit should care

Most L2 harnesses (Claude Code, Goose, Aider) call external processes or LLM APIs and orchestrate them from outside. Autolith inverts this: the LLM operates *inside* the runtime. If this pattern gains traction it represents a new dimension for `statefulness` — not just "session" vs "persistent" but "embedded-live-image" — where the agent's state is the entire runtime process. Could also inform how `execution_log_mode` is defined: Lisp image snapshots are a form of deterministic checkpoint distinct from append-only event logs (cf. apache/maka).

## Preliminary interpretation

Current best reading:
- **Level 2 — Agent Harness / Runtime**: primary. The live SBCL image is the harness; agent owns all tool registration within it.
- **Level 1 secondary**: the SBCL VM is itself the inference host for non-LLM code execution.

## Status

- Tracking: early signal, personal/small company project, no public GitHub link disclosed
- 105 HN points on first appearance; niche but architecturally distinctive
- Schema watch: `execution_environment: [subprocess | sandbox | live-image]`; `statefulness` extension needed
- No canonical section change: first signal for "live-image agent runtime" pattern
