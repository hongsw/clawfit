# Research Watch: Jeeves — Reasoning-Enhanced Jev-Compatible Decision Classifier

- Repo: https://github.com/PostHog/jeeves (⭐211)
- Source: Hacker News (187 points), item #11 on front page

## Why this is worth watching

Jeeves is a second independently-developed Jev-compatible decision model appearing on the same day as Jeff (firelex/jeff, HN 202 pts). Where Jeff is 0.8B and optimized for consumer-hardware training, Jeeves is 9B with integrated chain-of-thought reasoning built on Qwen3.5-9B — the two tools together constitute a two-signal confirmation of "Jev-compatible local classification model" as a distinct emerging sub-type. That PostHog — a commercially-significant product analytics company — built this signals that the pattern is being adopted beyond individual experimenters.

## What stands out immediately

- 9B parameters fine-tuned from Qwen3.5-9B via LoRA; not a scratch-trained model — LoRA on a frontier base
- CISPO reinforcement learning in training pipeline: supervised fine-tuning → CISPO RL → temperature calibration
- Diffusion drafter for speculative decoding — accelerates inference alongside the main model
- Dual-latency profile: ~0.3s without reasoning, ~3.3s median with reasoning on H100 — explicit reasoning budget exposed to callers
- Pointer head mechanism: produces Jev-compatible output (probabilities/scores, not generated text)
- JevBench public tier: 0.935 vs. Jev's 0.866 — outperforms on structured decision tasks, trails on MMLU knowledge (0.793 vs. 0.900)
- PostHog authored this: a product analytics company with production user bases is building classification infrastructure, not a research lab demo

## Why clawfit should care

Jeff + Jeeves on the same day from two independent organizations confirms "Jev-compatible decision model" as an emergent sub-type at the L1/L2 boundary. Clawfit's scoring.py uses heuristic weights for latency, cost, and task type; a reasoning-capable classifier in this tier could replace those heuristics with a learned signal. More practically, clawfit's `low-latency` + `offline` org profile has limited registry coverage — this sub-type directly addresses that gap. The two-signal rule for ecosystem-mapper is met today (jeff + jeeves = same pattern, different orgs). Phase 3 action warranted.

## Preliminary interpretation

Current best reading:
- **Level 1 — Specialist Decision Model** (primary): sits in the scoring/routing sub-layer of the LLM stack — not a generative base model, not an agent harness
- Secondary L5 characteristic: built using RL (CISPO), so it touches the training/evaluation layer during development

## Claims to verify

- JevBench score (0.935 vs. 0.866): self-reported, no independent audit; need external reproduction
- CISPO RL improvement vs. baseline SFT: claimed benefit, not separated out in public benchmarks
- Diffusion drafter speedup: speculative decoding gains depend heavily on hardware configuration — H100 numbers may not transfer to consumer GPUs
- PostHog's production use case: unclear if this is an internal tool or intended for public product use

## Status

- 211 stars; 187 HN points — above threshold, active community
- Registry ineligible: Jeeves has no public API with deterministic per-request pricing; it's a self-hosted model
- Two-signal confirmation (jeff + jeeves today): recommend Phase 3 ecosystem-mapper review for `jev_compatible_decision_model` canonical L1 sub-type entry
