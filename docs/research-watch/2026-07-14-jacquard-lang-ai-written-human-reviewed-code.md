# Research Watch: Jacquard — Programming Language for AI-Written, Human-Reviewed Code

- Repo/Link: https://github.com/jbwinters/jacquard-lang
- Source: Hacker News (Show HN, 2026-07-14)

## Why this is worth watching
Jacquard is a research programming language designed explicitly for the regime where ML models write most code and humans review it. Its core insight — that reviewers need the language itself to answer "what can this touch, and how sure are we" without reading every line — is the most structurally coherent answer to AI-generated code safety reviewed to date.

## What stands out immediately
- **Explicit effect system in signatures**: `(text) ->{net} text` makes external capabilities visible at function boundaries; reviewers see authority without reading implementations
- **Multi-world execution**: same program runs against real network, scripted fakes, recorded traffic, or probabilistic models by swapping handlers — no code changes
- **Structural hashing**: hashes canonical structure, not source bytes; comments/formatting don't trigger re-runs; enables trustworthy incremental verification
- **Probabilistic programming built-in**: `sample`/`observe` operations enable Bayesian inference as library code; used in the repair demo where agents generate patches and inference finds the most likely correct fix
- **AGENTS.md governance doc**: explicit contract for how AI agents should contribute to the repo

## Why clawfit should care
Jacquard defines a new axis for evaluating coding agents: **code verifiability** — can a human reviewer assess what generated code can touch without reading every line? This is a pre-scoring signal for `governance_need: hard` profiles. Tools paired with Jacquard would benefit from a `verifiable_output` capability flag. Currently 30 stars (research prototype), but the design pattern (effect-explicit codegen languages) could inform how clawfit weights governance-oriented harnesses.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation/Formal layer**: The language's structural hashing and probabilistic semantics function as an agent evaluation substrate — it enforces what the agent can claim about its own output.
- Secondary: **Level 3 — Governance**: the effect system is a governance mechanism that enforces output transparency.

## Status
- First signal; research prototype (30★); watching for adoption by coding agent harnesses as a "safe output language" pattern
