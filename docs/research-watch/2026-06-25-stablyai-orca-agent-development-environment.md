# Research Watch: stablyai/orca

- Repo: https://github.com/stablyai/orca
- Also see: https://orca.stablyai.com (product site, claim to inspect)

## Why this is worth watching
Orca is the highest-starred ADE (Agent Development Environment) signal in this watch log at 6,754 stars, with a daily shipping cadence and 490 forks suggesting active adoption rather than curiosity traffic. Its core bet — running 40+ heterogeneous CLI agents in parallel across isolated git worktrees for head-to-head comparison — is structurally distinct from single-agent IDEs and from orchestration layers that route tasks to one agent at a time. The addition of mobile companion apps and a visual Design Mode positions it as a cross-layer harness rather than a thin wrapper.

## What stands out immediately
- Parallel worktree fan-out: a single prompt is dispatched to multiple agents simultaneously, each working in its own isolated git branch — comparison is first-class, not an afterthought
- Agent roster claims 40+ supported CLI agents (Claude Code, Codex, OpenCode, Pi, others) — breadth is a claim to inspect; compatibility depends on whether each agent honors the worktree working directory
- Design Mode: click a UI element in a real Chromium window; Orca injects the element's HTML/CSS and a screenshot into the active agent's prompt — this is a visual-grounding capability at the harness level, not the agent level
- Mobile (iOS/Android): remote monitoring and prompt steering from a companion app — delegates human-in-the-loop control to a separate surface
- WebGL-rendered terminal splits with persistent infinite scrollback — infrastructure investment suggesting desktop-native rather than web-wrapped
- GitHub and Linear integrations listed as native — issue-to-agent and PR-to-review flows implied, not independently verified
- TypeScript 97%, MIT license, v1.4.97 — versioning cadence consistent with active production use

## Why clawfit should care
Orca is the first ADE signal in this watch log where the harness itself is the product rather than a plugin layered on an existing IDE. clawfit's scoring model evaluates individual (agent, llm, hardware) triples; Orca introduces a new composition unit — a parallel fleet of agents on the same task — that the current cartesian product cannot score. The Design Mode capability also signals a convergence between L2 harness behavior and L6 multimodal/UI interaction that the taxonomy currently treats as separate layers. The mobile steering surface adds a latency and availability dimension not present in any current registry entry.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrapper / harness / orchestration layer** (primary classification: it wraps and parallelizes multiple L1 agent runtimes, coordinates their execution, and surfaces comparison across them)
- **Level 6 secondary** — Design Mode and mobile companion apps introduce multimodal UI capture and cross-device human interface elements that span into L6; these are features of the harness, not separate products
- Not L1: Orca does not execute agent logic itself; it routes, isolates, and compares agents that do

## Status
- 6,754 stars, daily shipping cadence — above threshold for active tracking
- First ADE-class signal where parallel comparison is the core primitive, not a feature
- Promotion criterion: independent confirmation that worktree isolation holds across 3+ agents simultaneously, and that Design Mode prompt injection works with non-Claude CLI agents
