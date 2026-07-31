# Research Watch: "2x, not 10x: coding with LLMs in 2026"

- Repo/Link: https://obryant.dev/p/2x-not-10x/
- Source: Hacker News

## Why this is worth watching
A practitioner essay arguing that LLMs deliver roughly 2× coding productivity gains — genuine value but far below the 10× marketing claims. The core finding: a working implementation is now "20% done" (not 80%), because the hard work of refinement, judgment, and maintainability still requires human oversight. Breakthroughs will come from industry retooling around existing model capabilities, not from waiting for the next model generation.

## What stands out immediately
- Concrete heuristic: LLMs excel at tasks with objective, verifiable acceptance criteria (click button, check behavior); struggle with subjective judgment (maintainability, documentation scope, design tradeoffs)
- Counterintuitive finding: explicitly instructing agents to skip documentation ("never write READMEs, docstrings, or comments") measurably improves output quality
- Reframing the productivity ladder: "20% done" when it compiles, not 80% — aligns with the growing consensus that agentic loops need human-in-the-loop at quality gates
- Forecast: industry-level retooling of workflows and tooling, not model improvement, will unlock higher multipliers

## Why clawfit should care
Directly affects how clawfit should weight recommendations for solo developers versus team contexts. A 2× frame suggests that `setup_complexity: high` tools may not be worth the overhead for solo users. Also reinforces that `governance_need` and `output_destination` dimensions matter: teams investing in review loops around agent output will see higher effective gains.

## Preliminary interpretation
Cross-cutting signal — ecosystem maturation thesis. Not a tool; informs scoring calibration:
- **Level 7 — Practitioner signal** (productivity expectation baseline for the agentic era)

## Status
- First signal; high HN engagement; no registry action needed. Informational calibration signal for scoring weights.
