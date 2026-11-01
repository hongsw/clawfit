# Research Watch: Memdoor — Multi-Agent Ensemble Beats Frontier Model on LiveCodeBench Hard

- Repo/Link: https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve
- Source: Hacker News (#6, 22 points)

## Why this is worth watching

A team of 5 Qwen 3.8B–27B models coordinated through Memdoor's workflow layer outperforms Fable 5 on LiveCodeBench Hard — a challenging coding benchmark. This is a concrete benchmark result showing that a multi-agent ensemble of smaller open-weight models can surpass a top-tier frontier model on hard coding tasks, with the implication that cost, latency, and data-sovereignty concerns need not mean accepting lower quality.

## What stands out immediately

- Benchmark: LiveCodeBench Hard — the hardest tier of a widely-respected coding evaluation
- Ensemble of 5 agents, each specializing in a sub-task or providing a candidate solution for majority-vote
- Uses Qwen3.8B–27B, a smaller model family, not a frontier-class model
- Workflow orchestration handles task decomposition and vote aggregation
- Memdoor is an open-source project; the team-solve workflow is provided as a reusable example

## Why clawfit should care

clawfit's scoring currently weights LLM choice heavily through `scoring.py` (LLM preference at 0.15). A result like this challenges the implicit assumption that a single high-capability model is the optimal recommendation for a hard code-gen task. Two implications:

1. **Multi-agent agent entries** (e.g., rowboat, Claude Squad) may deserve higher code-gen task scores when paired with capable open-weight LLMs under budget constraints.
2. The `offline_mid_codegen` profile — which today ranks Goose/Aider/Continue — could benefit from a "multi-agent ensemble" option in the registry.

## Preliminary interpretation

Current best reading:
- **Level 5 — Evaluation / Benchmark layer** (primary): demonstrates a measurable quality ceiling for multi-agent approaches
- **Level 2 — Harness / Orchestration layer** (secondary): the team-solve workflow pattern is a reusable L2 harness artifact

## Status

- Early signal (22 HN points); benchmark claim not independently replicated yet
- Track: does the result hold for other hard coding tasks? Does a Memdoor registry entry make sense, or is the signal primarily about the ensemble *pattern*?
- Deferred: wait for star count / replication before adding Memdoor to tools_registry.json
