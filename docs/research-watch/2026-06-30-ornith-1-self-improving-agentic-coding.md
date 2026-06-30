# Research Watch: Ornith-1.0 — Self-Scaffolding LLMs for Agentic Coding

- Repo/Link: https://github.com/deepreinforce-ai/Ornith-1
- Source: Hacker News (140 + 52 pts, 30 + 7 comments)

## Why this is worth watching
Ornith-1.0 is the first open-source model family trained to jointly optimize *both* solution trajectories *and* the scaffolds that guide them — a qualitatively different approach from fine-tuning on SWE-Bench solutions. If the "scaffold RL" mechanism generalizes, it could shift the base model tier from commoditized coding LLMs to self-improving agentic substrates. Available in 9B-Dense, 31B-Dense, 35B-MoE, and 397B-MoE variants under MIT license.

## What stands out immediately
- **Dual RL loop**: RL optimizes the solution trajectory AND the guiding scaffold simultaneously; models "discover better search strategies" without human-designed prompts
- **Top benchmark results**: SWE-Bench, Terminal-Bench 2.1, NL2Repo top-tier at time of release
- **256K context window** across all size variants
- **OpenAI-compatible API**: drops in as a vLLM / SGLang backend without agent-framework changes
- **511★, 48 forks** — early but gaining traction (HN front page)

## Why clawfit should care
Ornith challenges the assumption that base model choice is decoupled from agentic scaffolding. A model that optimizes its own scaffolds blurs the L1/L2 boundary: the model itself absorbs some harness responsibility. If this pattern matures, clawfit may need a new `self_scaffolding` capability flag to distinguish these models from passively fine-tuned coding LLMs.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Agent Runtime** (model serving as its own scaffold optimizer)
- Secondary: **L5 — Evaluation / Self-improvement** (RL-driven trajectory discovery)

## Status
- First signal — 2026-06-30; 511★; hold for promotion until 3k★ or second independent self-scaffolding model appears
