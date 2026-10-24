# Research Watch: Dessa — Full-Duplex Speech Model

- Repo/Link: https://block.xyz/dessa
- Source: Hacker News

## Why this is worth watching
Dessa (from Block) claims to be the first publicly available full-duplex speech model, meaning it listens and speaks at the same time rather than taking turns. This is the architecture needed for natural real-time voice interfaces for AI agents, where latency and barge-in behavior have historically been broken by turn-based models.

## What stands out immediately
- Full-duplex: simultaneous listen and speak, not half-duplex turn-taking
- Built by Block (the payments/fintech company behind Square and Cash App)
- Positioned for authentic conversation rather than assistant-style Q&A latency
- Relevant to voice interface layers for autonomous agents

## Why clawfit should care
Voice/multimodal agent interfaces are a tracked dimension in clawfit's ecosystem. Full-duplex speech is the key missing primitive for truly conversational agents — the difference between a voice assistant that waits for you to stop talking and one that can genuinely interrupt or be interrupted. Dessa's public availability from a non-traditional AI lab signals that voice agent infra is moving beyond the LLM incumbents.

## Preliminary interpretation
Current best reading:
- **Level 6 — Interface / Voice layer** (multimodal input/output surface for agents, below harness, above model)

## Status
- Tracking: new signal, HN front page 2026-10-24
- Registry candidate: possible if a voice interface tier is added to the recommendation engine
