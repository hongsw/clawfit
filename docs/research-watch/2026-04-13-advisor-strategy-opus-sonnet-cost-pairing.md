# Research Watch: Anthropic Advisor Strategy — Opus + Sonnet Cost-Optimal Pairing

- Repo/Link: https://claude.com/blog/the-advisor-strategy
- Source: GeekNews

## Why this is worth watching
Anthropic published a blog post formalizing the "Advisor Strategy" — pairing **Claude Opus as a high-capability advisor** with **Claude Sonnet as a cost-efficient executor**. This is a named, officially endorsed multi-LLM architecture pattern that directly affects how clawfit should recommend LLM combinations for budget-constrained orgs.

## What stands out immediately
- Opus handles strategic reasoning / planning; Sonnet handles iterative execution
- Cost reduction framing: Opus only invoked when high-capability reasoning is required
- Officially published by Anthropic — not a community workaround
- Mirrors the "planner/executor" dual-agent harness design pattern documented earlier
- Complements Anthropic's earlier sprint-contract harness architecture

## Why clawfit should care
clawfit's current LLM scoring uses latency, cost, and task preference as independent axes. The Advisor Strategy shows that **LLM pairing** (not single LLM selection) is becoming a first-class architectural choice. This is a gap in the current recommendation model: recommending a single LLM ignores the cost-optimal pairing pattern. Potential future dimension: `multi_llm_pattern` with values like `advisor_executor`, `single_model`, `cost_tiered`.

## Preliminary interpretation
Current best reading:
- **Level 2/3 — Harness architecture pattern (multi-LLM orchestration layer)**
- Not a tool itself, but a named architecture pattern from a primary source

## Status
- Named pattern from official Anthropic blog — should be cited in reference-levels.md Level 2 notes
- Flag for scoring-analyst: LLM pairing as a future scoring dimension
