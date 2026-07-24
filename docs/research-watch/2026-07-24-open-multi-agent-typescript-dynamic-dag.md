# Research Watch: open-multi-agent — TypeScript Multi-Agent Orchestration with Runtime DAG Planning

- Repo: https://github.com/open-multi-agent/open-multi-agent (⭐6,700)
- Source: GitHub Trending TypeScript; web search for AI agent frameworks 2026

## Why this is worth watching
Most multi-agent frameworks require developers to define the task graph at authoring time: which agents run, in what order, with what dependencies. open-multi-agent inverts this: a coordinator agent receives the goal and constructs the task DAG dynamically at runtime, then a deterministic scheduler executes it. The practical consequence is that the developer describes what they want (the goal), not how to get it (the graph). This is a meaningful architectural position in a field where the dominant pattern (LangGraph, CrewAI, custom orchestration) still requires hand-drawn graphs. Whether the dynamic planning approach is reliable or merely aspirational is the key claim to verify.

## What stands out immediately
- **Runtime DAG construction**: coordinator agent turns a goal into a task DAG; no graph authoring required from the developer
- **Deterministic scheduler**: once the DAG is constructed, execution is deterministic — agents don't re-plan mid-run without an explicit re-planning gate
- **Plan approval gate**: developers can require human or automated approval of the generated plan before execution begins — bridges the gap between autonomous planning and human oversight
- **Checkpoint-based recovery**: execution state is checkpointed at task boundaries; failed or interrupted runs resume from the last successful checkpoint without re-running completed tasks
- **Token/cost budgets**: per-run budget caps with enforcement — the framework stops execution rather than silently exceeding limits
- **Stable run identity**: each run has a persistent ID; execution receipts and span waterfalls are replayable in the offline Run Viewer
- **Multi-model teams**: individual agents within a run can use different LLMs (Claude, ChatGPT, Gemini, DeepSeek, local models)
- **Loop detection**: detects runaway agent cycles and halts — a basic safety primitive often absent in framework-level orchestration
- **6.7k stars, launched 2026-04-01 under MIT**: 3+ months of community adoption; not a one-week-old prototype

## Why clawfit should care
open-multi-agent is at the intersection of two patterns clawfit has been tracking separately: (1) dynamic task decomposition (previously seen in DeerFlow, OpenHuman v0.2) and (2) durable execution with checkpoint recovery (previously seen in HumanLayer ACP, also written up today). The combination in a TypeScript-native, MIT-licensed package is notable because it targets the largest developer population in the ecosystem (JS/TS) without requiring a Kubernetes cluster or cloud provider dependency.

For clawfit's recommendation engine, open-multi-agent raises a classification question: is a framework that dynamically plans its own task graph an L2 harness (it wraps and coordinates agents) or an L3 team/SSOT generator (it generates the coordination structure at runtime)? The line between "orchestrator" and "plan generator" is meaningful for scoring profiles with `statefulness: session` and multi-step task requirements.

The `statefulness` axis in clawfit's filters may also need a `multi-step-durable` sub-mode: the framework's checkpoint-resume pattern isn't captured by either `stateless` or `session` — it's closer to "persistent workflow state across failures."

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Agent Orchestrator** (primary: coordinates multiple agents, handles scheduling, manages execution flow)
- **Level 3** has a secondary claim — the runtime DAG generation from a goal description is a form of SSOT/plan generation; depends on whether the coordinator agent's planning is treated as a capability or a structural layer
- Closer to L2 than L3: the "coordinator" is itself an agent call, not a separate architectural layer with governance authority

## Claims to verify
- "Describe the goal, not the graph" usability claim: real-world task decomposition quality depends on the coordinator model choice; Claude vs. GPT-5.6-Sol as coordinator likely produces very different DAG quality — not yet benchmarked
- Checkpoint recovery reliability: documented as a feature; no published failure/recovery rate or success metrics under adversarial conditions
- Loop detection robustness: described but not specified — detection threshold, max iterations, and halt behavior under complex dependency graphs need independent testing
- Multi-model agent teams: mixing providers within a run introduces per-provider auth, rate limiting, and context-format differences — integration complexity may exceed the documented "just configure" framing

## Status
- Research watch: appropriate (6.7k stars, 3 months of growth, MIT, TypeScript-native)
- Registry candidate: **No** — open-multi-agent is an orchestration framework, not an LLM or hardware entry; clawfit's current registry has no agents.json category for orchestration frameworks (only for specific agent runtimes like Claude Code)
- reference-levels.md: potential L2 canonical entry candidate — but single signal; watch for a second confirming signal that validates the "runtime DAG planning as distinct L2 sub-type" pattern before promoting
- Monitor for: adoption by Claude Code Routines users; comparison benchmarks vs. CrewAI and LangGraph on real task sets; whether the coordinator planning step is open-sourced or depends on a proprietary model call
