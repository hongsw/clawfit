# Research Watch: NeoGraph — C++ Graph Agent Engine

- Repo/Link: https://github.com/fox1245/NeoGraph
- Source: GeekNews
- Stars: 6 (at time of capture)

## Why this is worth watching

NeoGraph describes itself as "C++ Graph Agent Engine Library — LangGraph for C++", attempting to bring LangGraph's graph-based agent orchestration model to C++17. LangGraph is the dominant substrate for complex multi-agent workflows at L2; a C++ port would open agentic patterns to embedded, systems-programming, and high-performance contexts that Python's runtime overhead forecloses.

## What stands out immediately

- C++17-based agent orchestration, stated as analogous to LangGraph
- Target niche: systems software and high-performance environments where Python is impractical
- Very early — 6 stars at time of capture; no release, no documentation depth confirmed
- Author profile (`fox1245`) has minimal prior activity — provenance is thin

## Why clawfit should care

If LangGraph-style graph orchestration spreads to C++ environments it represents a new class of L2 harness sub-type: compiled-language agent orchestration, distinct from all current L2 entries (Python, TypeScript, Go, Shell). This would open `network: offline` + `latency: low` cells for high-governance/embedded deployments that currently have no harness option. Single signal, 6 stars — apply single-signal rule strictly.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/Orchestration sub-type candidate**

Architectural analogue to LangGraph but targeting compiled-language execution environments. No L3 or L4 signals detected. L1 secondary is possible if NeoGraph ships a base runtime alongside the graph layer.

## Status
- First signal for C++ agent orchestration harness sub-type
- Too early for map mutation: 6★, no functional verification, thin provenance
- Promotion threshold: 500★ OR confirmed functional parity with a LangGraph workflow; independent usage by a non-author project
- Revisit at 2026-07-08 or when star count exceeds 500
