# Research Watch: GPT-6.1 Sol — Near-Astra Performance at One-Fifth the Cost

- Repo/Link: https://openai.com/index/introducing-gpt-6-1-sol/
- Source: Hacker News (293 points), OpenAI DevDay 2026

## Why this is worth watching

GPT-6.1 Sol lands a new cost-performance point: $2/M input, $10/M output — roughly one-fifth of GPT-6 Astra's price — while approaching Astra's capability on agentic coding, computer use, and multi-step professional workflows. That ratio matters for clawfit's budget-constrained agent profiles: teams priced out of frontier models now have an accessible path that doesn't require stepping down to a substantially weaker model. Cached input at $0.10/M (95% discount) is relevant for agents with shared long prefixes.

## What stands out immediately

- Pricing: $2/M input / $10/M output; $0.10/M cached input — deterministic, public, suitable for registry
- Model ID: `gpt-6.1-sol` in the OpenAI API
- Reasoning effort: low / medium (default) / high / xhigh / max; "none" and "minimal" not supported — this is a reasoning model, not a pure completion model
- Target workloads: agentic coding, computer use, document understanding, multi-step business workflows
- Availability: ChatGPT Work, Codex, API; Plus/Pro/Business/Enterprise/Edu — not available in main ChatGPT chat at launch
- Context and capabilities: no public context window spec in the announcement, but compatible with reasoning.effort API parameter already in use for o3/o4 models
- Positions between GPT-6 Sol (cheaper, less capable) and GPT-6 Astra (more capable, 5x more expensive)
- Timing: DevDay 2026, same event as OpenAI Dots announcement — coordinated positioning of model + agent product

## Why clawfit should care

GPT-6.1 Sol has deterministic public pricing, a clearly described cost tier, and a named task profile (agentic coding, computer use, professional workflows) that maps directly to clawfit's task taxonomy. If benchmark data supports the "near-Astra on coding" claim, this may be the highest-value registry addition of the current quarter. The $2/M input price sits within clawfit's existing `budget: 0.01` filter range for moderate-usage agents. Registry eligibility: borderline — pricing is public and deterministic; need to confirm context window and latency profile before adding.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base LLM** (primary): closed API model, positioned for agentic workloads
- No secondary level; this is infrastructure, not a harness or capability layer
- Competes directly with current registry entries: claude-sonnet-5-5, o3-mini; fills the "reasoning-capable but not top-tier-expensive" bucket

## Claims to verify

- "Near-Astra performance" on agentic coding and computer use: vague claim, no specific benchmark scores in the announcement; need independent evaluation (GAIA, SWE-bench, etc.)
- Context window: not announced publicly; may require API testing or documentation update
- Latency characteristics: reasoning.effort=low may be fast enough for `low-latency` org profiles, but no numbers given
- Cached input at $0.10/M: OpenAI's prompt caching applies automatically on qualifying requests — verify this behaves identically to their existing caching policy

## Status

- Official OpenAI model, DevDay 2026 (2026-09-29); API available as `gpt-6.1-sol`
- Registry eligibility: YES — pricing is deterministic and public ($2/$10/$0.10 per M tokens); task profile is clear
- Pending: context window spec, independent latency benchmark, SWE-bench or equivalent coding score before adding to llms.json
- Action: monitor for third-party benchmarks; add to registry when context/latency data confirmed
