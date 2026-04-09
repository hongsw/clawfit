# Research Watch: From Prompts to Harness — 4 Years of AI Agentic Patterns

- Repo/Link: https://bits-bytes-nn.github.io/insights/agentic-ai/2026/04/05/evolution-of-ai-agentic-patterns.html
- Source: GeekNews

## Why this is worth watching
This post offers the clearest single-document synthesis of the 2022–2026 AI engineering paradigm shift: from **prompt engineering** (2022–2024) → **context engineering** (2025) → **harness engineering** (2026+). It maps each shift to concrete tooling milestones and explains why the locus of precision moved from words to context to systems. It's a reference-quality conceptual frame for how clawfit's taxonomy maps to practitioner priorities.

## What stands out immediately
- **Three-phase model**: Prompt → Context → Harness, with dated milestones (Copilot 2022, Karpathy vibe-coding 2025, Hashimoto harness principles 2026)
- **Harness defined as a 2×2**: deterministic feedforward (AGENTS.md/linting), deterministic feedback (compilers/tests), non-deterministic feedforward (system prompts), non-deterministic feedback (LLM-as-judge)
- **Anthropic 3-agent architecture** (planner/generator/evaluator) cited as canonical reference
- **Rule of Two (Meta AI)**: agents can hold untrusted input OR sensitive data OR perform state changes — never two simultaneously without human approval
- **KV-cache optimization** and Ralph pattern (clean resets) as harness reliability primitives

## Why clawfit should care
The blog frames harness engineering as the key discriminator for 2026 production AI. Clawfit's Level 2 taxonomy (meta wrappers/harnesses) now has a theoretical backbone: the 2×2 deterministic/non-deterministic split. "Harness reliability" as an evaluation axis (vs. pure latency/cost) aligns with recent signals from oh-my-pi Hashline, Anthropic sprint-contracts, and superpowers methodology.

## Preliminary interpretation
Current best reading:
- **Reference / Level 5** — conceptual framework for clawfit taxonomy evolution; not a tool but an important architecture reference

## Status
- Tracked as reference signal; informs Level 2 harness evaluation criteria
