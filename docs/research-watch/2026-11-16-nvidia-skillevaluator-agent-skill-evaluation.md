# Research Watch: NVIDIA/SkillEvaluator

- Repo/Link: https://github.com/NVIDIA/SkillEvaluator
- Source: GitHub Trending

## Why this is worth watching
NVIDIA has released SkillEvaluator, a multi-tier framework for evaluating AI agent skills including automated quality gates and live agent evaluation loops. At 1,657 stars with 122 gained today, it appears distinct from NVIDIA/SkillSpector (tracked previously — benchmark visualization). SkillEvaluator positions itself as an active evaluation harness rather than a passive scorecard: it gates skill deployment through quality tiers before skills reach production agents.

## What stands out immediately
- Multi-tier evaluation model: draft → quality-gate → live-agent eval before skill deployment
- Python-first; 1,657 total stars, 122 today
- NVIDIA provenance signals hardware-aware evaluation (GPU-specific skill benchmarking is likely)
- Different from SkillSpector: SkillEvaluator is about gating new skills; SkillSpector appears to be about inspecting deployed skill behavior
- Evaluation loop is live (runs the skill against a real agent), not static assertion-based

## Why clawfit should care
Agent skill evaluation is becoming a production concern as skill libraries grow (google/skills, stitch-skills, anthropics/skills). SkillEvaluator formalizes a quality-gate pattern that clawfit doesn't yet have a scoring axis for. The `governance_need: hard` profile in clawfit scoring should care about whether a recommended tool has associated evaluation infrastructure. This is the second evaluation-focused signal from NVIDIA (after SkillSpector), suggesting NVIDIA is positioning at the L5 evaluation layer for the agent ecosystem.

## Preliminary interpretation
Current best reading:
- **Level 5 — Agent Evaluation Layer** (multi-tier skill quality gating framework)
- Secondary L4b (interacts with the skill/plugin layer as evaluator)

## Status
- First scan: 2026-11-16
- Registry action: deferred — evaluation frameworks don't have cost/latency dimensions; no current registry schema for L5 entries
- 📡 Note: If SkillEvaluator and SkillSpector are both confirmed to be standalone NVIDIA tools at L5, that would be the second major-vendor push into the agent evaluation layer alongside maxxbench (HN, Nov-08) — three-signal threshold for a canonical L5 sub-type
