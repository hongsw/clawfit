# Research Watch: Procedural Graphs — Self-Evolving Execution Structures for LLM Agents

- Repo/Link: https://arxiv.org/abs/2609.09153
- Source: Hacker News (40 pts, 12 comments)

## Why this is worth watching
An arXiv paper introducing "Procedural Graphs" — execution structures that self-modify at runtime based on LLM agent output. This is distinct from static DAG orchestration (LangGraph, Apache Maka): the graph topology itself evolves during a run, enabling adaptive agent workflows.

## What stands out immediately
- Self-evolving graph topology: edges and nodes are added/removed mid-execution by the agent
- Targets long-horizon tasks where static plans fail (research loops, debugging cycles)
- Benchmarked against ReAct and fixed-graph baselines — claims 18-32% improvement on multi-step tasks
- Academic stage: no production implementation linked yet

## Why clawfit should care
Procedural Graphs represent an emerging Level 3 paradigm (research-loop / adaptive orchestration). If this pattern is adopted by mainstream harnesses (LangGraph, Maka, etc.), clawfit's taxonomy will need to distinguish "adaptive-graph" harnesses from "static-DAG" ones. Relevant to future scoring dimensions around task complexity headroom.

## Preliminary interpretation
Current best reading:
- **Level 3 — Research-Loop / Adaptive Orchestration** (not yet a product, but a formative architecture signal)

## Status
- Signal strength: medium-academic (40 HN pts, arxiv only)
- Next: Watch for implementation in open-source harnesses over next 60 days
