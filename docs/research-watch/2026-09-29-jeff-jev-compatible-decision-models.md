# Research Watch: Jeff — Jev-Compatible 0.8B Decision Models

- Repo/Link: https://github.com/firelex/jeff
- Source: Hacker News (202 points, 63 comments)

## Why this is worth watching
Jeff is a family of 0.8B parameter decision models trained to be Jev-compatible — returning probabilities/scores instead of long-form text. With ~30ms latency and local training, it signals a trend toward tiny, task-specific oracle models that agents call for fast binary or classification decisions rather than full LLM inference.

## What stands out immediately
- 0.8B parameters, trainable on consumer hardware (~home GPU)
- ~30ms latency — fast enough for real-time agentic routing decisions
- Jev-compatible output format: probabilities/scores, not text generation
- Vision model support
- HN traction: 202 points, active 63-comment thread

## Why clawfit should care
Decision models like Jeff sit in the scoring/routing layer of multi-agent pipelines — they'd influence how clawfit itself could be implemented (a tiny classifier replacing the scoring.py heuristics). Also signals growing demand for lightweight, local inference that fits `offline` + `low-latency` org profiles currently underserved in the registry.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base LLM / Specialist Decision Model**
Fits the sub-niche of lightweight classification models used as internal routers in agent harnesses.

## Status
- New signal (2026-09-29), high HN traction; monitor for adoption in agent harness integrations
