# Research Watch: "Why Are Coding Agents So Dumb?" — Agent-Layer Bottleneck Discourse

- Repo/Link: https://mtlynch.io/why-are-coding-agents-so-dumb/
- Source: GeekNews front page

## Why this is worth watching
Michael Lynch's post reached the GeekNews front page as a high-signal practitioner critique: it argues that the *model* is no longer the bottleneck in coding agents, the *orchestration and planning layer* is. The list of failure modes is unusually specific and directly maps to the current clawfit scoring dimensions. This kind of high-visibility practitioner discourse often precedes product pivots by major harness vendors.

## What stands out immediately
- **Orchestration failures:** sequential execution of parallelizable subtasks; no sub-model delegation by cost/capability
- **Self-ignorance:** agents search the web for documentation about their own features
- **Planning quality:** unstructured, low-level lists instead of hierarchical plans with diagrams and mockups
- **Security gap:** instructions to avoid files are advisory, not enforced; sandbox bypasses are real
- **AFK failure mode:** agent halted overnight waiting for a branch name — no autonomous fallback decision
- **Principal-agent hypothesis:** author's leading explanation — AI lab incentives point to benchmark scores (model quality) not daily developer experience (agent quality)
- **"Dream agent" spec:** multi-model selection per subtask, real OS sandboxing, self-knowledge, unified dashboard, ETA estimates, quota-aware routing

## Why clawfit should care
- The specific failure modes map directly to clawfit dimensions: `setup_complexity`, `network`, `governance_need`, `statefulness`, `primary_task`
- "AFK fallback autonomy" is an unmodeled axis — current `growth_horizon` doesn't capture *autonomous continuation without human* vs. *blocks waiting for human*
- The "dream agent" spec items (multi-model routing, enforced sandboxing, quota-aware model selection) are near-term differentiators between harnesses — worth tracking as org_fit metadata signals
- Post confirms `solo_dev_codegen` profiles are underserved by the current generation of tools; clawfit top-5 for this profile (Claude Code, OpenCode, Goose, Crush, Cline) are exactly the tools the author critiques

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Orchestration weakness signal** (discourse that maps to L2/L3 gaps)
- Secondary: practitioner evidence for a `planning_quality` sub-dimension at L3

## Status
- Ongoing discourse signal; monitoring: author follow-ups, HN/GeekNews comment threads, harness vendor responses
- No code/repo; classification is a discourse/trend signal, not a tool entry
