# Research Watch: Mistral Large 4 — 1T-Parameter Open-Weight Multimodal MoE

- Repo/Link: https://mistral.ai/news/mistral-large-4
- Source: Hacker News front page (1,022 pts)

## Why this is worth watching
Mistral Large 4 is a 1 trillion-parameter MoE model with 49B active parameters, slated for open-weight release before end of October 2026 at $1.36/$4.18 per million tokens. It is natively multimodal and benchmarks at 61.7% on DeepSWE v1.1 — approaching Reflection Beam (77.2% on SWE Bench Pro v2-Hard) but from a different architecture lineage. The open-weight release at frontier-class performance continues the October 2026 pattern of open-weight models closing the capability gap on closed API models, now with multimodal support included.

## What stands out immediately
- 1T total / 49B active MoE — larger active parameter count than Beam (23B active) but still inference-efficient
- Natively multimodal: visual grounding, outperforming GPT-6-Astra on Dense 200 (42% vs. 41%)
- 59.9% on AutomationBench — direct agentic workflow benchmark score
- 59.4% on SWE-Atlas-QnA — coding agent tool-use benchmark
- 82% on vulnerability reproduction tasks — cybersecurity-capable
- SciCode-Verified SOTA among open-weight models — science/research loop eligible
- Trained on 3,800 NVIDIA Grace Blackwell GPUs in European datacenters — AI sovereignty angle
- $1.36/$4.18 per million tokens with planned open weights — undercuts closed frontier pricing

## Why clawfit should care
Mistral Large 4 is the second frontier-class open-weight model announced for October 2026 (alongside Reflection Beam). Together they represent a pattern that directly affects clawfit's `hardware: self-hosted` scoring: if open-weight models reach 60–77% coding benchmark scores, the cost/governance tradeoff argument for self-hosted inference strengthens considerably. ML4's multimodal capability also extends agent applicability beyond pure code tasks. The AutomationBench score is directly clawfit-relevant for `task: automation` queries. The European training provenance addresses `governance_need: data-sovereignty` in GDPR-sensitive contexts.

## Preliminary interpretation
Current best reading:
- **L1 — Base Agent Runtime / LLM** (primary: frontier-class LLM with agentic and multimodal benchmarks)

## Claims to verify
- AutomationBench 59.9% — benchmark definition and scoring methodology not confirmed independently
- Open-weight release confirmed for October 2026 but weights not yet published at time of tracking
- Multimodal benchmark comparisons use internal Mistral benchmarks (Dense 200) not industry-standard

## Status
- New signal 2026-10-06 — weights pending; benchmarks self-reported; registry-eligible pending open weight confirmation and deterministic latency/cost data verification
