# Research Watch: Uber's Agent-Native Software Factory at Scale

- Repo/Link: https://www.uber.com/us/en/blog/efficient-software-factory/
- Source: GeekNews (news.hada.io)

## Why this is worth watching
Uber reports that over 70% of their pull requests are now handled by agents, with 3,600+ agent skills executing more than 30,000 times daily. This is the largest confirmed public deployment of coding agents at a major engineering organization — not a pilot, but a production operating posture.

## What stands out immediately
- 70%+ of PRs by agents at Uber's engineering scale (~5,000+ engineers) is a step-change
- 3,600 named agent skills — skills are the unit of automation, not monolithic agents
- 30,000+ daily skill executions implies near-continuous agent activity across the codebase
- Framed as "efficient software factory" — process language, not infrastructure language

## Why clawfit should care
This is a major adoption-signal data point for the `large` team_size segment in the registry. Uber's posture — skill-based agent decomposition, high cadence, multi-agent at enterprise scale — validates the registry's treatment of large-org profiles needing governance and orchestration. It also suggests that "number of named skills" may be a meaningful maturity proxy: organizations running thousands of skills are at maturity 9–10 on our scale, not the 6–7 currently modeled.

## Preliminary interpretation
Current best reading:
- **Level 3 — Orchestration / Multi-Agent** (enterprise-scale skill-based agent orchestration pattern)
- This is an organizational posture, not a tool — but it's a strong ecosystem signal for L3 pattern adoption

## Status
- Published ~2026-09-02; first observation in clawfit scan
