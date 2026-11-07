# Research Watch: Waymark — Workflow Engine That Compiles Jobs

- Repo/Link: https://github.com/piercefreeman/waymark
- Source: Hacker News front page (Show HN)

## Why this is worth watching
Waymark is a workflow engine for agentic pipelines that *compiles* job graphs rather than replaying them. Standard workflow engines (Temporal, Prefect, LangGraph) checkpoint state and replay from the last saved position on failure. Waymark instead statically analyzes the job DAG at definition time, produces a compiled execution plan, and executes deterministically from that plan. The claim is elimination of replay-induced side effects and cheaper reruns.

## What stands out immediately
- Compile-time rather than runtime graph resolution — unusual in agent workflow tooling
- Targets agentic pipelines where replay side effects (duplicate LLM calls, duplicate writes) are costly
- Python library, MIT license, Show HN — early stage, 33 points/9 comments
- Directly comparable to LangGraph, Prefect, and to the DeerFlow/AutoResearch harnesses already in registry
- No star count included in HN snippet — appears new/small

## Why clawfit should care
clawfit currently scores orchestration tools on `statefulness` and `latency`. A compile-time workflow model changes the latency profile (predictable, no replay overhead) but introduces a constraint: job graphs must be statically analyzable. This would be a new scoring dimension — `execution_model: compiled | replayed | streaming`. First signal for this sub-type in the orchestration layer.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Orchestration Layer** (workflow engine sub-type)

## Status
- First signal for compile-time workflow engines in the agent orchestration layer
- Registry action: deferred (no star count / adoption data; check back in 2–4 weeks)
