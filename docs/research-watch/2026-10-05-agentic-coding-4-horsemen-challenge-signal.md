# Research Watch: 에이전트 코딩의 묵시록 4기사 (4 Horsemen of Agentic Coding)

- Repo/Link: https://news.hada.io/ (GeekNews front page, 2026-10-05)
- Source: GeekNews

## Why this is worth watching
A GeekNews post titles "에이전트 코딩의 묵시록 4기사" (4 Horsemen of the Agentic Coding Apocalypse) catalogs four organizational failure modes emerging from AI-assisted coding at scale: sloppiness, alienation, skill degradation, and weakened team dynamics. These are not technical but social and process signals — and they directly bear on when and whether organizations can effectively adopt agent-first coding workflows.

## What stands out immediately
- Four named failure modes: **sloppiness** (AI-generated code merged without review), **alienation** (developers disconnected from their own codebase), **skill degradation** (junior engineers not building foundational skills), **weakened team dynamics** (pair programming and knowledge transfer eroding)
- The analysis comes from the Korean developer community — a high-adoption early-mover population for agentic coding tools
- This is a "second-order effects" signal: not about capability but about org-readiness constraints

## Why clawfit should care
clawfit's 10-dimension org_fit scoring includes `governance_need`, `min_maturity`, and `primary_role` — all of which should reflect whether a team has the readiness to use agentic tools safely. This signal suggests that `min_maturity` for high-autonomy coding agents may be systematically under-set in current registry metadata: teams with `governance_need: none` but low maturity may be exactly the risk population described here.

## Preliminary interpretation
Current best reading:
- **L2 — Harness/Wrapper layer** (affects how harnesses should manage autonomy guardrails)
- Also relevant to **L5 — Evaluation/Learning** (skill degradation as a longitudinal eval signal)

## Status
- First signal for "organizational failure modes from agentic coding at scale" — analytical, no repo
- Monitoring: watch for follow-on posts, empirical studies, or tooling responses to these failure modes
