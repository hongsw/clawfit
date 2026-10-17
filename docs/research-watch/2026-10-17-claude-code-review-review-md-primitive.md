# Research Watch: Claude Code Team Code Review — REVIEW.md Primitive and Risk-Tiered Merges

- Repo/Link: https://claude.dev/blog/solving-code-review-at-anthropic/
- Source: Hacker News front page

## Why this is worth watching
The team that builds Claude Code describes their own production code-review workflow: 90% of code written by Claude Code, automated review on every PR, and merged PRs doubling while revert share fell 40%+ from June to September. The post introduces REVIEW.md as a distinct config primitive alongside CLAUDE.md, and a risk-tier classifier that sets human approval requirements from the diff itself rather than the author's identity.

## What stands out immediately
- **REVIEW.md**: a per-codebase file written by code owners that tells the reviewer what failure looks like, which paths to skip, how many nits are allowed, and what evidence format to require. Complements CLAUDE.md (author-side context) with reviewer-side context.
- **Risk-tiered approvals from the diff**: a classifier reads the change, not the author, and assigns Low/Medium/High. Low-tier changes (docs, flagged additive) merge with no human once automated checks pass; High-tier requires two humans.
- **Incident-driven eval set**: past incidents and reverts become daily test cases; reviewer prompt/tool/model changes are kept only if the score improves.
- **Quantified outcomes**: substantive review comments coverage 16% → 54%; mean review rounds 2.08 → 1.32; rounds ≥5 fell from 8.9% to 1.5%.
- **Convergence controls**: round cap at three, diff-only re-review after first passes, no repeat findings across turns — directly address the agent-review runaway failure mode.
- **Noted gap**: no circuit breakers yet that tighten approval thresholds when revert/incident rates rise.

## Why clawfit should care
REVIEW.md is a new reviewer-side config primitive distinct from CLAUDE.md — first signal for a two-file harness config pattern (CLAUDE.md = what to build, REVIEW.md = how to evaluate). The risk-tier-by-diff classifier is the first published description of automated governance tiering in a production AI-first codebase at scale. Both patterns are directly relevant to `governance_need: hard` profiles in the registry. The Postgres 19 delay signal (2026-10-16) showed AI review raising the quality bar enough to delay a major release; this signal shows what an intentional, instrumented AI review system looks like from the inside.

## Preliminary interpretation
Current best reading:
- **Level 3 — Governance / Workflow Config** (primary): REVIEW.md, risk-tier classifier, and incident-driven evals are governance-layer primitives
- **Level 2 — Harness / SDK** (secondary): the parallel-agent review pipeline is a harness-layer pattern

## Status
- First signal for "REVIEW.md as reviewer-side harness config primitive" (distinct from CLAUDE.md)
- First signal for "diff-driven risk-tier classifier replacing author-identity approvals"
- Second signal for "AI code review at scale at a production org" (after Postgres 19 delay governance signal, 2026-10-16)
- Two-signal rule met for "AI code review as a governance-layer workflow change" — candidate for canonical L3 sub-section addition
- Monitor for REVIEW.md adoption outside Anthropic (other teams adding reviewer-side config files)
