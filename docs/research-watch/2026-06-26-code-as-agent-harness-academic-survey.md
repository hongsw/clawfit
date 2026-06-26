# Research Watch: Code as Agent Harness — Academic Survey

- Repo/Link: https://code-as-harness.github.io
- Source: GeekNews

## Why this is worth watching
A 102-page survey from UIUC, Meta, and Stanford frames code as an *execution platform* for agents rather than merely their output. This is the first peer-reviewed, multi-institution treatment of the harness-as-code paradigm that clawfit's ecosystem map is built on. It joins the 2026-06-10 arxiv harness-search paper as a second academic confirmation that harness selection outweighs model selection as a design variable.

## What stands out immediately
- Authors from Meta AI and Stanford alongside UIUC — not a single-lab perspective
- 102 pages suggests a comprehensive taxonomy of code-execution patterns for agents
- Appears on GeekNews front page, indicating practitioner traction beyond academic circles
- Complements the arxiv 2605.15184 paper (already tracked) which showed harness > retrieval strategy for accuracy

## Why clawfit should care
The survey directly legitimizes clawfit's architectural frame: recommending on the harness + runtime axis first, model second. If it proposes a formal taxonomy of code-execution harness patterns, that taxonomy is a candidate for upgrading the L1–L2 taxonomy definitions in `docs/reference-levels.md`. Monitor for whether it names patterns that map to existing L2 sub-types (orchestrator, state machine, looped CLI, etc.).

## Preliminary interpretation
Current best reading:
- **L2 — Ecosystem Meta-Signal** (academic validation of harness-centric architecture)

## Status
- First signal; no formal star count (site-hosted survey). Held pending review of taxonomy contents.
- Promotion criterion: identified taxonomy elements that require map revision OR a clawfit maintainer reads and annotates the paper.
