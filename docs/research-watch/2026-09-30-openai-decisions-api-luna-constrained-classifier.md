# Research Watch: OpenAI Decisions API — Luna-Based Constrained Classification Endpoint

- Repo/Link: https://thenewstack.io/openai-decision-api-luna/
- Source: GeekNews front page (3 points, "OpenAI, Jev와 경쟁할 Luna 기반 Decision API 공개"); OpenAI DevDay 2026-09-29

## Why this is worth watching

OpenAI's Decisions API is a product-level operationalization of the "Jev-compatible decision model" pattern that emerged last month (jeff, PostHog/jeeves, 2026-09-29). It provides a constrained classification endpoint — developer supplies a question, a fixed set of allowed answers, and optional context; the API returns one answer with a confidence score. The key claim: 150ms response time vs 1.6s for a standard Luna call. That 10× latency reduction on a constrained output space mirrors exactly what TypeSafe/Jev and PostHog/Jeeves documented at the open-source layer. OpenAI shipping a first-party version of this pattern confirms it as a stable architectural primitive, not an experimental sub-community trend.

## What stands out immediately

- **150ms response time**: 10× faster than standard GPT-6 Luna calls (1.6s) on the same underlying model — constraint on the output space enables significant compute reduction
- **Confidence scores on a closed answer set**: unlike standard chat completions, returns probability distributions over developer-defined answers — addresses a known reliability gap in using chat models for routing/classification
- **Constrained output format**: developer specifies the complete set of valid answers at call time; the API cannot hallucinate outside that set
- **Multimodal context support**: accepts text and image context, consistent with Luna's base capabilities
- **Use cases explicitly named**: content classification, request routing, agent next-action selection from a limited menu
- **Limited preview status at DevDay**: not yet broadly available; pricing not yet published — this limits registry eligibility immediately
- **Third independent signal for the Jev-compatible pattern**: jeff (0.8B local, 2026-09-29), jeeves (9B local, 2026-09-29), Decisions API (cloud, 2026-09-30) — three orgs, three implementations, same architectural primitive

## Why clawfit should care

clawfit currently has no "decision model" or "classification endpoint" category in the LLM registry. The scoring system uses `task` filters to match agents to workloads, but the underlying LLM entries assume general-purpose completion models. The Jev-compatible decision model pattern — now confirmed by three independent implementations — represents a distinct LLM sub-type with a different latency/cost/accuracy profile: ~150ms, constrained output, reliability > general chat. A future `task: routing` or `task: classification` profile in clawfit would need this sub-type represented. The OpenAI Decisions API is the first cloud-hosted entry in this pattern, which makes it structurally different from jeff/jeeves (both self-hosted). When pricing is announced, it may be the first directly registerable entry in a new "classification endpoint" LLM category.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base LLM / Constrained Inference** (primary): constrained classification endpoint built on Luna; a distinct model-serving mode, not a new model
- **Level 4 — Capability API** (secondary): accessible as an API call in agent decision loops — functions as an agent capability/tool for routing and classification steps

This is the third cross-organization signal for the "Jev-compatible decision model" pattern. The two-signal rule was met on 2026-09-29 (jeff + jeeves). Today's Decisions API adds cross-tier confirmation (cloud-hosted, from the dominant API provider), which strengthens the case for canonical promotion.

## Claims to verify

- 150ms latency: stated in the DevDay announcement but not independently benchmarked; p50 vs p99 distinction not specified — relevant for agent decision loops that call this in sequence
- Confidence score calibration: decision models are described as providing "more realistic confidence scores" than chat models, but the calibration methodology is not disclosed
- Pricing: not yet published at time of tracking (limited preview); without cost data the entry cannot be added to the LLM registry
- Relationship to `gpt-6-luna` base model: unclear whether Decisions API runs the same weights or a fine-tuned variant optimized for constrained output

## Status

- 📡 Tracking: **third cross-org signal** for `jev_compatible_decision_model` pattern (cross-tier confirmation: open-source local → cloud API)
- No prior research-watch doc specifically for the Decisions API (Luna model tracked separately: 2026-07-11-openai-gpt-5-6-sol-terra-luna-model-family.md)
- Registry eligibility: PENDING — pricing not yet public; once announced, cost + 150ms latency would satisfy deterministic data requirement for a new `classification_endpoint` sub-type entry
- Canonical section: approaching promotion threshold for `jev_compatible_decision_model` as a stable L1 sub-type — see Phase 3 note below
