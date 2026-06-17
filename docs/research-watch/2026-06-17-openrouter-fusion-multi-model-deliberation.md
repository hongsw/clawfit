# Research Watch: OpenRouter Fusion — Multi-Model Deliberation Panel

- Repo/Link: https://openrouter.ai/openrouter/fusion
- Source: GeekNews (news.hada.io)

## Why this is worth watching
OpenRouter Fusion turns a single prompt into a small multi-model deliberation: a panel of expert models run in parallel (with web search/fetch enabled), then a judge model synthesizes consensus, contradictions, partial coverage, unique insights, and blind spots into a final answer. This is a new LLM routing primitive that sits above simple load-balancing or cost-routing.

## What stands out immediately
- Panel members + judge are configurable (Quality preset vs. Budget preset, or custom)
- Pricing is additive: each panel member's tokens billed separately — not a flat routing fee
- Recommended for "research, expert critique, or anywhere the cost of being wrong outweighs a few extra completions"
- No custom infrastructure required; drop-in via OpenRouter API

## Why clawfit should care
OpenRouter Fusion adds a new effective LLM category: ensemble/deliberation APIs that aren't a single model. clawfit's current LLM registry assumes one-model-per-call; Fusion's cost model (n × tokens) and latency profile (parallel + synthesis round) need a distinct scoring treatment. Any org scoring "medium budget + high governance need + research task" should surface ensemble options.

## Preliminary interpretation
Current best reading:
- **Level 5 — LLM Evaluation & Benchmarking / Routing Infrastructure** (hybrid: sits between routing and eval)
- Closer to a managed judge-panel than a bare model; may need its own sub-layer tag

## Status
- Newly launched feature on OpenRouter, publicly available via API
- Tracking: observe pricing dynamics and adoption as ensemble-calls become a standard pattern
