# Research Watch: Meta HyperAgents — Self-Referential Agent Improvement

- Repo/Link: https://cobusgreyling.medium.com/hyperagents-by-meta-892580e14f5b
- Source: GeekNews

## Why this is worth watching
Meta's HyperAgents framework introduces **self-referential agents that modify their own improvement mechanisms** — not just their task outputs, but the meta-process by which they improve. This is qualitatively different from tool-use agents or even adaptive runtimes like Hermes Agent: the modification loop targets the agent's *learning and improvement loop*, not the task code itself.

## What stands out immediately
- Agents can rewrite their own improvement heuristics, not just execute tasks
- Self-modification targets the improvement *process*, making this a recursive meta-agent
- Framework from Meta Research, adding institutional weight to the concept
- Conceptually distinct from reinforcement-style self-improvement: operates at reasoning-process level
- Unclear open-source status; originated as a research publication

## Why clawfit should care
This represents a new sub-type at the boundary of Level 1 (base runtime) and Level 5 (research / evaluation): an agent that autonomously tunes its own evaluation criteria. If this pattern productizes, clawfit's maturity dimension will need a new top-end stage. It also challenges LLM-selection logic — if the agent improves its own prompts, static capability scores become less meaningful over time.

## Preliminary interpretation
Current best reading:
- **Level 1/5 — Adaptive base runtime with self-modifying evaluation loop**
- Research-stage; not yet a recommendation endpoint — track as ecosystem signal

## Status
- Early signal — watching for open-source release or engineering blog follow-up
