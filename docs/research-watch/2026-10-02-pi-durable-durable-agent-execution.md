# Research Watch: Pi Durable

- Repo/Link: https://earendil.com
- Source: Hacker News (187 pts)

## Why this is worth watching
Earendil Engineering is shipping "Pi Durable" as a distinct product alongside Pi 1.0, introducing first-party durable execution semantics directly into an agent runtime rather than relying on external orchestration frameworks (Temporal, Prefect, DBOS). This is the first signal of a major agent runtime vendor treating durable execution as a core product feature rather than an integration concern.

## What stands out immediately
- Ships alongside Pi 1.0 as a sibling product (same-day HN launch, 187 pts)
- "Durable" implies agent-native checkpointing, resumption across failures, and long-running task continuity
- Structurally distinct from pydantic-ai's durable execution (which adapts to 8 external engines) — Pi Durable appears to be a native runtime feature
- Earendil already shipping Codemode (harness-side MCP sandbox) and Pi 1.0 (unified LLM API + agent loop) — Pi Durable extends the stack downward into execution substrate

## Why clawfit should care
Pi Durable strengthens the case that `statefulness: session` and `statefulness: persistent` are meaningful registry axes: tools with native durable execution can make different guarantees about long-running tasks than harnesses that depend on external orchestration. A future `durability_model` field in org_fit metadata could distinguish tools that natively checkpoint vs. those that delegate. The earendil product family is now spanning L1 (Pi inference) + L2 (Pi Durable execution) + L3 (Pi harness) + L4 (Codemode MCP sandbox) across four levels simultaneously.

## Preliminary interpretation
Current best reading:
- **Level 2 — Agent Harness / SDK (durable execution sub-type)**
- Secondary: Level 1 (inference runtime integration)

## Status
- First signal for "agent-native first-party durable execution" as distinct from "external-framework durable execution"
- Cross-org condition: needs one more independent agent runtime vendor shipping native durable execution to confirm as a canonical sub-type
- Earendil Pi already tracked; this is a new architectural dimension of the same product family
- Monitoring
