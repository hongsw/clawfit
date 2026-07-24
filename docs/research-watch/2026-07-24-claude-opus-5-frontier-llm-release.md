# Research Watch: Claude Opus 5 — Anthropic's New Flagship Model at Half the Opus 4 Price

- Repo/Link: https://www.anthropic.com/news/claude-opus-5
- Source: Hacker News front page (446pts + 68pts system card thread, 2026-07-24)

## Why this is worth watching
Claude Opus 5 is a same-day release that directly affects every clawfit recommendation involving Anthropic's flagship tier. The pricing drop is the primary technical fact: Opus 5 inputs at $5/M tokens — one-third the cost of the current registry entry for claude-opus ($15/M, which tracks Opus 4). Anthropic frames Opus 5 as "approaching Fable 5 intelligence at half the price," which suggests the frontier/flagship positioning has bifurcated into two distinct tiers. The SWE-bench and ARC-AGI 3 claims, if confirmed, would move Opus 5 to the top of the code-gen and reasoning categories in the registry, while the pricing makes it competitive with models currently occupying the medium-cost tier.

## What stands out immediately
- **Pricing**: $5/$25 per million input/output tokens ($0.005/$0.025 per 1k) — 67% cheaper than Opus 4's documented $15/M input
- **Fast mode**: 2× base price (~$10/$50/M) for reported 2.5× speed improvement — an explicit latency/cost trade-off lever
- **Software engineering**: claimed "more than doubles Opus 4.8's performance at lower cost per task" on Frontier-Bench
- **ARC-AGI 3**: scores 3× higher than "competing models" on novel problem-solving tasks — specific competitor list not stated in announcement
- **OSWorld 2.0**: claims best-in-class computer use performance at given cost level — "at given cost level" qualifier is significant
- **Scientific tasks**: notable improvements on organic chemistry and protein-related tasks (no benchmark names given)
- **Visual generation**: described as producing stronger artifact and interactive content outputs
- **Verification emphasis**: announcement explicitly calls out improved self-verification — "much stronger at verifying its work and iterating carefully until it succeeds"
- **Availability**: released on all platforms simultaneously (Claude.ai, API, Claude Code, Claude Cowork)

## Why clawfit should care
The current registry entry `claude-opus` (id) maps to Claude Opus 4 at $0.015/1k input. With Opus 5 entering at $0.005/1k input, the existing entry misrepresents the actual cost of using Anthropic's flagship model. Any recommendation that scores a user profile against `claude-opus` will overestimate cost by 3×. This is a concrete scoring error.

More structurally: if Fable 5 occupies a "superintelligence" tier above Opus 5, the Anthropic lineup now has three meaningful scoring tiers (Haiku/fast, Sonnet/balanced, Opus/flagship) with a potential fourth (Fable/frontier). The current registry covers Haiku, Sonnet, and Opus 4 — Opus 5 is a direct upgrade to the Opus slot, and Fable 5 would be a new tier entirely.

The fast mode pricing also creates a new latency option for Opus-class tasks: at 2.5× speed and 2× cost, it sits between Sonnet-latency and standard-Opus-latency, which doesn't exist in the current registry's `low/medium/high` taxonomy.

## Preliminary interpretation
- **Not an ecosystem layer** — this is an LLM backend, not a harness or capability layer
- Maps directly to `llms.json` as a registry update/addition
- The fast-mode variant raises the question of whether to add a `claude-opus-5-fast` entry or handle it via a latency flag — current schema has no "fast mode" field

## Claims to verify
- ARC-AGI 3 score: "3× higher than competing models" — competitor list not specified; could be cherry-picked comparison set
- Frontier-Bench "doubles Opus 4.8 performance": Frontier-Bench is Anthropic's own benchmark; independent replication needed
- OSWorld 2.0 "best in class at given cost": the qualifier "at given cost level" means this is a Pareto-frontier claim, not a raw-score claim — very different assertion
- Context window: not stated in the July 24 announcement; assumed 1M tokens based on Opus 4.8 precedent — unconfirmed
- Fast mode 2.5× speed: no methodology given; likely measured on Anthropic's own infrastructure under optimal conditions

## Status
- Registry candidate: **Yes** — public deterministic pricing, schema maps cleanly to llms.json
  - `claude-opus-5`: latency=high, cost_per_1k_tokens=0.005, context_window=1000000 (unconfirmed; assumed from Opus 4.8)
  - tasks: research, code-gen, data-analysis, qa (same as claude-opus)
- Phase 4 decision: add `claude-opus-5` to llms.json; keep `claude-opus` entry pointing to Opus 4 for backward compatibility — rename display name to clarify version
- reference-levels.md: no change (single signal; no new structural pattern; LLM releases are below the taxonomy layer)
