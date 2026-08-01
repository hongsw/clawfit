# Research Watch: LLM Router Anti-Pattern — Manifest Post-Mortem

- Repo/Link: https://manifest.build/blog/why-we-deprecated-our-llm-router/
- Source: Hacker News (82 pts, 39 comments — 2026-08-01)

## Why this is worth watching
Manifest ran an LLM router for 7,000 users over four months and then shut it down — one of the first production post-mortems on the routing pattern. The reasons they cite are structural, not operational, making this a durable counter-signal to the "intelligent model routing" trend clawfit currently tracks.

## What stands out immediately
- **Prompt-alone routing is unreliable**: context emerges through tool calls, making pre-routing decisions stale by the time they matter
- **Cache coherence beats routing savings**: switching models breaks prompt-cache locality; staying on one model is 75–90% cheaper on repeat calls
- **Consistency has hidden value**: engineers need stable tool behavior; model-switching degrades quality and raises eval burden
- **Total cost of routing complexity** often exceeds the savings — the paper trail is now public

## Why clawfit should care
clawfit's multi-layer scoring does NOT recommend routing as a pattern, so this validates the current design. However, any new tools in the registry claiming "smart model routing" as a key feature should be flagged with lower `task_fit` and higher `setup_complexity`. The scoring analyst should also review whether latency/cost weights inadvertently reward routing-heavy architectures.

## Preliminary interpretation
Current best reading:
- **Cross-layer signal** — affects how Level 1 (base runtime) and Level 2 (harness) tools with routing features are evaluated
- No new registry entry needed; signals that existing routing-oriented entries may need downgraded notes

## Status
- Tracking — anti-pattern signal. Note in scoring review. manifest.build already tracked (2026-05-05); this is a distinct deprecation post-mortem.
