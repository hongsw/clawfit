# Research Watch: re_gent — Version Control for AI Coding Agents

- Repo/Link: https://github.com/regent-vcs/regent
- Source: GeekNews front page (2026-06-16, 9 pts)

## Why this is worth watching
re_gent introduces a new sub-type of agent tooling: **provenance tracking at the agent-action level**, analogous to what Git does for developer commits. It captures every tool-using turn (file edits, bash commands, writes) with line-level attribution to the prompt that produced it. This is distinct from API-call tracing (Spanlens) and session-cost analytics (AgentsView) — it is an audit trail built for regulatory and debugging use cases.

## What stands out immediately
- Content-addressed storage with BLAKE3; sub-10ms lookups via SQLite indexing
- Line-level "blame" showing which prompt wrote each line — VSCode inline extension available
- DAG of agent steps survives context clears (session continuity across resets)
- Multi-agent session support: tracks concurrent Claude Code, Codex, and OpenCode runs independently
- Zero-config: `rgt init` drops a `.regent/` directory alongside `.git/`
- 730★ at time of discovery

## Why clawfit should care
Agent provenance is directly relevant to clawfit's `governance_need` scoring dimension. Organizations with `hard` governance requirements have no current tool in the registry that addresses "who/what wrote this code" at the prompt-attribution level. re_gent fills a gap between raw session logging (AgentsView) and runtime enforcement (Claw Patrol). A `governance_need: hard` profile with a `data_sensitivity: confidential` flag should surface this tool. Registry candidate.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation / Audit sub-type** (agent provenance tracker; operates on completed steps, not live sessions)
- Secondary **L3 weak** (governance-adjacent: audit trail enables human review of agent actions before merge)

## Status
- First signal (730★). Single-signal rule applies. Promotion criterion: 2k★ OR confirmed use by a regulated-industry team (finance, healthcare, gov).
