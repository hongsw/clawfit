# Research Watch: HarnessTax — Coding Agent Harness Cost Benchmark

- Repo/Link: https://harnesstax.github.io/
- Source: GeekNews

## Why this is worth watching
HarnessTax is the first published benchmark explicitly measuring how much the *harness layer* inflates token usage across identical underlying models. Seven models were compared, with results showing up to a 5x token cost difference driven entirely by harness choices — not model capability. This directly challenges the assumption that model selection alone drives cost.

## What stands out immediately
- Success rates were similar across harnesses for the same model
- Token cost varied by up to 5x across harness configurations
- The study isolates harness overhead as a primary cost driver
- Static site hosted on GitHub Pages — suggests academic/independent research
- GeekNews featured (Korean developer community) — strong signal for Korean enterprise AI adoption context

## Why clawfit should care
clawfit's scoring engine treats cost as a function of LLM pricing tiers. HarnessTax demonstrates that harness selection is a multiplicative cost factor of the same order of magnitude as model price differences. The current scoring schema has no `harness_overhead: [low | medium | high]` dimension. A recommendation of a cheap LLM through an expensive harness could cost more than a premium LLM through an efficient one. This is the strongest external evidence yet that harness cost efficiency should be a first-class scoring axis.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation / Benchmarking** (primary)
- Harness overhead is empirically measurable and should be modelable in org_fit scoring

## Status
- Monitoring — no GitHub repo found, static site; author identity unclear
- High relevance to clawfit scoring roadmap; single signal
