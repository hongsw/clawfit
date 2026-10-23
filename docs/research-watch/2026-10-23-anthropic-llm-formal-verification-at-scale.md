# Research Watch: Anthropic — LLMs Make Formal Software Verification Feasible at Scale

- Repo/Link: https://www.anthropic.com/research/formal-verification
- Source: Hacker News

## Why this is worth watching
Anthropic published research showing LLMs can generate formal proofs for software at a scale that was previously impractical — bridging the gap between property-based testing and mathematical correctness guarantees. This has direct implications for how coding agents validate their own output, moving beyond "does the test pass?" toward "is this provably correct?"

## What stands out immediately
- Targets the correctness-validation step that currently happens *after* code generation, not during
- Positions LLMs as proof-assistant co-pilots rather than raw code generators
- Could transform agent evaluation from benchmark-pass/fail to formal correctness checking
- Relevant to harness-level tooling that wraps agents with post-generation verification

## Why clawfit should care
If formal verification becomes a standard harness component, clawfit's scoring may need a new axis for "verification capability" or "output correctness guarantees." Tools that pair code generation with formal proof generation would score significantly higher for high-governance, high-data-sensitivity profiles. This is a Level 1→2 boundary signal: base LLM capability enabling new harness-layer features.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base LLM Capability** (formal reasoning over code) with **Level 2 — Harness integration potential** (verification-as-a-harness-step)

## Status
- Research publication 2026-10-23 — tracking (potential scoring dimension)
