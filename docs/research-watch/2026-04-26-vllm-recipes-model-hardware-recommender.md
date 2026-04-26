# Research Watch: vLLM Recipes — Model + Hardware Configuration Recommender

- Repo/Link: https://recipes.vllm.ai/
- Source: GeekNews front page (2026-04-26)

## Why this is worth watching
vLLM Recipes is an interactive platform that recommends model and hardware configurations for vLLM inference deployments. This is directly adjacent to clawfit's own domain: where clawfit recommends agent + LLM + hardware combos for organizational fit, vLLM Recipes recommends LLM + hardware combos for inference serving. The existence of a standalone recommendation product from the vLLM team signals that model/hardware fit guidance is becoming a product category, not just documentation.

## What stands out immediately
- From the vLLM team (the most widely deployed open-source LLM inference server)
- Interactive recommendation interface — not static docs, but a configuration advisor
- Focus on serving-side hardware selection (GPU type, memory, parallelism) rather than org-fit scoring
- Signals that "hardware+model fit" recommendation is a product surface that users want

## Why clawfit should care
vLLM Recipes and clawfit solve adjacent problems: clawfit's hardware dimension (`network: offline/hybrid`, `budget`) overlaps with vLLM Recipes' serving-side hardware advice. Two implications: (1) clawfit's hardware scoring should stay distinct by emphasizing *org-fit* (governance, team size, task type) rather than raw inference optimization; (2) for `network: offline` + `budget: low` profiles, vLLM Recipes could become a downstream reference that clawfit users consult *after* getting a clawfit recommendation. A potential complementary positioning rather than a competitor.

## Preliminary interpretation
Current best reading:
- **Level 5 — Research / evaluation / benchmark** (serving-side hardware recommendation guide)
- Not a Level 1–4 agent tool; it is infrastructure guidance, not an agent runtime or capability layer

## Status
- Tracking; no registry entry (serving-side, not an agent or agent tool); noteworthy as adjacent recommendation-engine product from a major inference team
