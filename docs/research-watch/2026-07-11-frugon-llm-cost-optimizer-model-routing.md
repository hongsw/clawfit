# Research Watch: Frugon — Local LLM Cost Optimizer / Model Router

- Repo/Link: https://github.com/Rodiun/frugon
- Source: Hacker News (Show HN, front page)

## Why this is worth watching
Frugon directly addresses the problem clawfit's scoring system models: which LLM to use for which task at what cost. It operates from the opposite direction — instead of recommending upfront, it analyzes your actual usage logs and identifies retroactively which calls could have used a cheaper model. The local, MIT-licensed, proxy-shim architecture is directly usable in agent pipelines.

## What stands out immediately
- Analyzes JSONL request/response logs entirely locally (no data leaves machine)
- Captures API calls via proxy shim or pre-formatted logs
- `frugon analyze` outputs: current spend, potential savings, routing recommendation
- `--measure` flag validates with real traffic samples using user's own API keys
- Concrete output: "move 64% of easy calls to a cheaper model, save $205/month"
- MIT license; 109 stars (early, but high conceptual relevance)

## Why clawfit should care
Frugon is a complementary tool to clawfit's recommendation engine: clawfit recommends which LLM to use upfront by profile; Frugon validates whether the recommendation was correct in production. For scoring, this reinforces the `monthly_budget: low/medium/high` axis and the value of the cost dimension in clawfit's fit scoring. Also a potential L5 reference implementation for "empirical model routing" as opposed to clawfit's "profile-based recommendation" approach. Schema watch: `cost_analysis_mode: predictive (clawfit) | empirical (frugon)`.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation and learning layer** (primary, retroactive cost analysis)
- **Level 7 — Infrastructure** (secondary, proxy-shim deployment model)

## Status
- First signal 2026-07-11 (109 stars, below 5k registry threshold — no registry entry)
- Monitor: star velocity; whether proxy-shim adoption becomes common in agent cost benchmarking
- Schema watch: `cost_analysis_mode: predictive | empirical`
