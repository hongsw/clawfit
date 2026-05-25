# Research Watch: MiroFish

- Repo/Link: https://github.com/666ghj/MiroFish
- Source: GitHub Trending (#12, 62.1k★)

## Why this is worth watching
At 62k stars, MiroFish is one of the highest-starred multi-agent frameworks in this taxonomy. It is a swarm simulation engine for prediction — not a coding agent — but its architecture (GraphRAG + thousands of autonomous agents interacting in a simulated environment + ReportAgent) represents a distinct multi-agent orchestration pattern not currently represented in the clawfit ecosystem map.

## What stands out immediately
- Creates a "high-fidelity parallel digital world" from seed data (news, reports, narratives)
- Thousands of autonomous agents interact and evolve; users inject variables to deduce future trajectories
- Architecture: graph building (seed extraction + memory injection + GraphRAG) → environment setup → dual-platform simulation → ReportAgent output → interactive agent chat
- Use cases: policy/PR testing, political/financial prediction, creative scenario exploration
- 62.1k★, 9.7k forks, Python + Vue, AGPL-3.0, Shanda Group strategic backing

## Why clawfit should care
MiroFish is out-of-scope for the current clawfit registry (not a coding agent, LLM harness, or hardware option). However, its architecture is directly relevant to two future concerns: (1) as a reference for multi-agent orchestration at scale, and (2) as a signal that the "prediction/simulation" use-case for agents is reaching mainstream star counts. The AGPL-3.0 license is a hard blocker for `governance_need: hard` enterprise profiles. If clawfit ever adds a `task: simulation` or `task: research-loop` type, MiroFish would be the anchor entry.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base agent runtime (domain-specialized, prediction/simulation vertical)**

Secondary: **Level 6a** (GraphRAG knowledge layer — seed extraction pipeline is a retrieval-native L6a pattern). Not a Level 2 harness because it is not wrapping other agents; it IS the runtime.

## Status
- Held: out-of-scope for current clawfit schema (no `task: simulation` type exists)
- AGPL-3.0 hard blocker for enterprise governance profiles
- Watch: if `task: simulation` or `task: prediction` is added to the schema, MiroFish is the immediate anchor entry; very high star count (62k) would make it a top-ranked entry in its category
