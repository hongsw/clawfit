# Research Watch: Kev — Tiny Jev-like Decision Models on Qwen3.5

- Repo/Link: https://github.com/jaredpalmer/kev
- Source: Hacker News (398 points, front page 2026-09-22)

## Why this is worth watching
Kev is an open-source family of compact decision models built on top of Qwen3.5, explicitly positioned as a "tiny Jev-like" structured output alternative to autoregressive LLM generation. It targets agent action production — returning probabilities and ranked choices instead of free text — at significantly lower latency and cost than a full LLM call. This is the fourth signal for the "structured / non-autoregressive agent decision output" pattern after TypeSafe Jev (2026-09-16), OpenJev (2026-09-19), and ConvAI RL-NAR (2026-09-20).

## What stands out immediately
- Built on Qwen3.5 base — open weights, self-hostable, no API vendor dependency
- "Tiny" framing: compact model family implies CPU-friendly or edge-suitable inference
- 398 HN points and front-page placement signals meaningful developer interest
- `jaredpalmer` — creator of Formik, Tsdx, and other widely-used open-source TypeScript tools; practitioner credibility
- Qwen3.5 base means the technique is reproducible on any Qwen-family fine-tune

## Why clawfit should care
This pattern is building toward canonical: four signals across four independent organizations/approaches in one week (TypeSafe Jev, OpenJev, ConvAI RL-NAR, Kev). If "structured decision output" becomes a recognized architecture class, clawfit's `latency` and `network` scoring for agent runtimes will need a new dimension — decision models (sub-100ms, offline-capable) vs. autoregressive LLM calls (300ms+, online). The `tasks` field in the registry currently assumes all agents use full LLM inference; structured decision models at the action layer would change scoring for time-sensitive workflows.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Agent Runtime** (L1 primary: model as decision engine)
- **Level 5 — Evaluation / Fine-tuning** (L5 secondary: specialized training technique)

## Status
- First research-watch doc for Kev specifically
- Fourth signal for "structured/non-autoregressive agent decision output" cross-date pattern
- Pattern is approaching canonical promotion threshold (four independent signals, multiple architectural approaches)
- Not yet in registry — awaiting confirmed star count, confirmed GitHub URL, licensing details
- Monitor: if star count crosses 5k threshold in next scan, registry entry warranted
