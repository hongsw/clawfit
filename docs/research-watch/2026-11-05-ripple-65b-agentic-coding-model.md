# Research Watch: Ripple-65B — Agentic Coding Model Preview

- Repo/Link: https://www.ricursive.com/ripple
- Source: Hacker News front page (2026-11-05)

## Why this is worth watching
Ricursive is previewing Ripple-65B with claims of state-of-the-art results on agentic coding benchmarks. The model appears to target the coding-agent backend use case specifically — not general reasoning — which would make it a narrow-scope competitor to Claude Opus 5.5 and Gemini 4 Carbon in clawfit's `task: code-gen` profile. At 65B parameters it sits below frontier-class MoE models (Kimi K3, DeepSeek V5) and above mid-class models (Qwen 2.5 72B), suggesting a compute/cost tradeoff optimized for coding-agent workflows.

## What stands out immediately
- Headline claim: SOTA on agentic coding (benchmark name and methodology not confirmed in preview announcement)
- 65B parameters: positioned below trillion-parameter MoE models; potentially more cost-efficient per coding task
- Company name "Ricursive" and URL structure suggest this is a startup, not an incumbent lab
- No open weights mentioned; no pricing published at preview stage
- Preview URL implies early access / waitlist model, not GA

## Why clawfit should care
If Ripple-65B's benchmark claims survive independent verification, it would be the first purpose-built agentic coding model in the 65B-class (non-MoE) tracked by clawfit. That would affect `task: code-gen` scoring by introducing a cost/quality tradeoff option between frontier models ($3-4/1M tokens) and open/local models. The `llms.json` schema has no `specialization` field; if purpose-built coding models proliferate, the registry may need to distinguish general-purpose LLMs from coding-optimized ones for accurate score weighting.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base LLM** (purpose-built coding model candidate for agent backends)
- clawfit category: `llms.json` candidate, pending pricing, public weights or API, and independent benchmark verification

## Claims to verify
- Benchmark name and methodology for the SOTA claim
- Pricing (startup model — likely premium API, not self-hostable at preview)
- Whether open weights are planned or API-only
- Whether "agentic coding" benchmark is the same framework as SWE-Bench, Parsimony Code Volume, or a proprietary suite

## Status
- Tracking: first signal (HN front page 2026-11-05)
- Registry action: deferred — preview only; no pricing, weights, or independent benchmark
