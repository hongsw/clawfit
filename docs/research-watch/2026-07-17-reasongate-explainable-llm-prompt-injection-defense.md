# Research Watch: ReasonGate

- Repo/Link: https://github.com/search?q=ReasonGate+LLM+prompt+injection (Show HN)
- Source: Hacker News Show HN (2026-07-17)

## Why this is worth watching
ReasonGate is an explainable security gate for LLM apps that blocks prompt injection attacks and provides an auditable reason for every blocking decision. The "explainability" angle differentiates it from threshold-based jailbreak filters — every gate decision is transparent and debuggable, which is material for governance-heavy orgs (`governance_need: hard`).

## What stands out immediately
- Written in Python, actively maintained
- Every block produces a human-readable reason, not just a binary flag
- Addresses jailbreak detection, AI safety, and guardrails in a single layer
- Positioned at the input boundary of LLM applications — pre-inference security
- Reflects growing demand for auditable AI governance tooling at L3

## Why clawfit should care
This is a signal that the L3 governance layer is maturing from "prompt engineering rules" toward dedicated security proxy tooling. For clawfit profiles with `governance_need: hard` and `data_sensitivity: confidential`, a tool like ReasonGate represents a companion layer rather than an alternative agent — but clawfit's scoring should distinguish agents that natively support governance hooks from those that require external gates like this.

## Preliminary interpretation
Current best reading:
- **Level 3 — Governance / Security Layer**: sits at the agent API boundary as a pre-inference injection shield; does not execute agent tasks itself

## Status
- Early-stage Show HN; tracking for L3 governance-tooling cluster growth
- Not a registry candidate (not an agent or harness — infrastructure companion layer)
- Watch: Show HN thread and GitHub repo once confirmed
