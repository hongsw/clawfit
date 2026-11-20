# Research Watch: Gemini 4 Neon — Cost-Efficient Coding and Analysis Model

- Repo/Link: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
- Source: GeekNews front page

## Why this is worth watching
Gemini 4 Neon is Google's cost-efficient companion to Gemini 4 Hydrogen (tracked 2026-11-13). It targets complex coding and analysis tasks at substantially lower cost — continuing the two-tier frontier model pattern (deep/flash split) now observed across Google, Microsoft (MAI Code 2 Flash), and Anthropic (Sonnet/Haiku). Neon's availability in the Gemini API and Gemini CLI makes it a direct competitor for cost-sensitive coding agent workloads.

## What stands out immediately
- Explicitly positioned for "complex coding and analysis" at efficient cost
- Part of the Gemini 4 family alongside Hydrogen (orchestrator) and Carbon (deep reasoning)
- Available through the Gemini API, Gemini CLI, and AI Studio
- Extends the Hydrogen/Carbon two-tier model into a three-tier family
- Pricing not fully confirmed at time of scan

## Why clawfit should care
Neon adds a third Gemini 4 tier, completing the family tracked since 2026-11-13. The LLM registry entry for Gemini 4 Hydrogen should be audited to reflect the full three-tier family. For the `solo_dev_codegen` profile (medium budget), Neon may be the preferred Gemini recommendation over Hydrogen. Registry entry deferred until pricing is confirmed.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Model / LLM** (cost-efficient coding model, part of Gemini 4 family)

## Status
- First scan 2026-11-20 (GeekNews)
- Registry entry deferred: pricing not confirmed; Hydrogen already tracked
- 📡 Watch: once pricing confirmed, add registry entry as `gemini-4-neon` with latency: low, cost positioning below Hydrogen
