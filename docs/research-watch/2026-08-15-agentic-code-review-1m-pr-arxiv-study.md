# Research Watch: From Human-Centric to Agentic Code Review (arxiv 2607.13196)

- Repo/Link: https://arxiv.org/abs/2607.13196
- Source: GeekNews front page (2026-08-15)

## Why this is worth watching
A large-scale empirical study of 1.02 million pull requests across 207 GitHub projects, tracing the shift from human-only → LLM-assisted → AI-agent-driven code review. The key finding: AI agent involvement accelerates review decisions (speed), but does **not** improve review quality — and once agents participate, human-AI collaboration patterns become the dominant predictor of review efficiency, overtaking traditional factors like PR size and reviewer activity.

## What stands out immediately
- Three adoption patterns identified: Gradual AI Adoption, Rapid LLM Adoption, Rapid AI Agent Adoption — each with distinct velocity and quality outcomes
- Speed-quality decoupling: agentic review makes review faster but not better; this challenges the assumption that automation = improvement
- Human-AI collaboration *pattern* (not just presence) predicts efficiency — structural insight relevant to harness design
- Connects to: openai-training-agent-breakout (2026-08-08), harveyai-harvey-labs (2026-08-08), open-code-review tool in registry

## Why clawfit should care
clawfit has `open-code-review` in tools_registry.json and tracks agent evaluation (L5 layer). This paper provides the first large-scale empirical evidence that agentic code review adoption is active and measurable — relevant to two clawfit axes: (1) **task=qa** recommendations should note the speed/quality trade-off when recommending AI review tools; (2) **L5 evaluation** signals are accumulating around code review as a measurable benchmark domain (after harveyai's legal benchmarks), suggesting code review will be a second evaluation frontier.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation and Learning Layer** (primary): large-scale empirical measurement of agent review adoption and quality impact
- No new tool to add, but strengthens the evidential basis for clawfit's `qa`/`security-testing` task scoring

## Status
- Academic signal: arxiv preprint, not a tool — no registry entry
- Relevant to scoring calibration: `qa` task tools should carry a note that speed-vs-quality trade-off is documented empirically at scale
