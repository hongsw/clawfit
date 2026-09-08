# Research Watch: Claude Fable 5.1 / Mythos 5.1 — 75% Cache-Read Price Cut and Restricted Security Tier

- Repo/Link: https://anthropic.com/news/claude-fable-5-1
- Source: Anthropic newsroom 2026-09-01; VentureBeat 2026-09-01; gHacks 2026-09-01; MarkTechPost 2026-09-01
- See prior signals: `2026-06-10-claude-fable-5-async-agent-model-tier.md`, `2026-06-16-fable5-mythos5-us-export-restriction.md`

## Why this is worth watching

Fable 5.1 cuts prompt cache-read pricing from $1.00 to $0.25 per million tokens — a 75% reduction — while leaving base input ($10/M) and output ($50/M) prices unchanged. For agentic workflows that return repeatedly to the same system prompt, tool schema, or document corpus, this is not a cosmetic discount: it changes the break-even math for whether prompt caching is worth implementing and, when it is, substantially alters the effective per-task cost of Fable 5.1 relative to alternatives.

The simultaneous introduction of a named restricted tier — Mythos 5.1, available only to vetted cybersecurity and life-sciences organizations — is the third signal (after Mythos 5 June 2026 and the June export-control event) pointing to specialized access controls for frontier-capability models. This pattern is worth tracking independently of the pricing change.

Released 2026-09-01. No star count; not a GitHub repo. Ecosystem signal.

## What stands out immediately

- **75% cache-read cut, base unchanged**: cache-read drops $1.00 → $0.25/M tokens; base input remains $10/M, output $50/M; cache-write remains at the base-input rate. This is the first time Anthropic has cut per-class token pricing without a general model downgrade.
- **Effective cost reduction is workload-dependent**: for a heavily agentic workflow with 80% cached context, effective per-token cost drops ~45%; for a workflow with 30% cached context, the reduction is ~22%. Neither is a fixed headline number — it depends on cache hit rate.
- **Terminal-Bench-Science benchmark 52.6%**: reported score on a terminal-environment scientific reasoning benchmark; no prior Fable 5 score published on this benchmark for direct comparison.
- **Mythos 5.1 restricted access**: same model weights, different API access tier; limited to vetted cybersecurity researchers and life-sciences organizations; access is application-gated, not subscription-gated.
- **Third access-control signal**: Mythos 5 (June 2026, export restriction), Mythos 5 (June 2026, restricted security tier), Mythos 5.1 (September 2026, same dual restriction) — a pattern of frontier-capability models with non-public access paths is accumulating.
- **No new API parameters**: the release does not introduce `execution_mode`, `max_task_duration`, or other API parameters proposed for tracking after the Fable 5 signal (June 2026); the model tier is still selected by model ID only.
- **Export control status unclear**: the June 2026 export restriction applied to Fable 5 and Mythos 5; whether it extends to 5.1 is not stated in the release announcement.

## Why clawfit should care

1. **Cache-read price cut directly changes cost scoring for Fable 5.1 configurations**: clawfit's current scoring uses input token price as the cost proxy. For any (agent, Fable 5.1, hardware) triple where the agent's typical workload has >50% cached context (e.g., Claude Code with a large persistent system prompt, or a document-analysis agent with a fixed corpus), the effective per-task cost at cache-read $0.25/M is meaningfully below what the $10/M base input price suggests. The scoring model needs either a cache-adjusted effective price or a workload-profile field that adjusts cost scoring when caching is active.

2. **Mythos 5.1 restricted access creates a new `access_tier` dimension gap**: clawfit's `network: online` filter assumes that any named LLM is publicly accessible to all users. Mythos 5.1 is online but not publicly accessible — it requires application approval and domain affiliation. A `task: security` profile that would nominally recommend Mythos 5.1 would give incorrect results for users who are not vetted. An `access_tier: public | restricted | vetted` field on LLM registry entries would prevent this.

3. **Effective cost reduction of ~25-45% for agentic workloads shifts relative scoring between Fable 5.1 and cost-competitive alternatives**: the cache cut narrows the cost gap between Fable 5.1 and cheaper models (GPT-4o mini, Claude Haiku) for workloads that cache aggressively. Some configurations that previously scored poorly on cost at Fable 5.1 base prices may score acceptably when cache-adjusted cost is used.

4. **"Restricted security tier" is now a repeating L1 pattern, not a one-off**: two models (Mythos 5, Mythos 5.1) with the same restricted-access pattern confirm this is intentional product architecture. The `task: security` registry gap identified after June 2026 still has no resolution — no security-focused tool has cleared the 5k-star registry threshold — but the LLM layer now has a named model for that task that is inaccessible to most users.

## Preliminary interpretation

Current best reading:
- **L1 — Base Runtime / Model Tier (primary)**: Fable 5.1 / Mythos 5.1 are LLM updates; the cache-read price change affects cost scoring at L1
- **Ecosystem signal (secondary)**: the Mythos 5.1 restricted-access pattern is a governance/access signal, not a new architectural layer

## Claims to verify

- Whether the 75% cache-read cut applies retroactively to existing cached content or only to new cache writes after the pricing change
- Whether the Terminal-Bench-Science 52.6% result is measured against a fixed test set with external validators, or is Anthropic-internal benchmarking with no third-party reproduction
- Whether the Mythos 5.1 restricted-access program accepts rolling applications or has a fixed cohort; the release announcement language is vague on this
- Whether the June 2026 export control directive that blocked Fable 5 / Mythos 5 access in certain regions applies to 5.1; the announcement is silent on this
- Whether prompt cache write-through still incurs base-input pricing, or whether the cache-write rate has also changed (release copy is ambiguous — "cache-read" is explicit but "cache-write" rate is unspecified in secondary coverage)

## Status

- Ecosystem / LLM signal. No GitHub repo. No star count.
- Released 2026-09-01. Qualifies as recent signal.
- LLM registry candidate: if `llms.json` gains an `effective_cached_price_per_mtok` field or a `workload_cache_adjusted_cost` field, Fable 5.1 is the first entry to populate it. Blocked on schema design decision.
- `access_tier` field needed in `llms.json` for Mythos 5.1. Blocked on schema design decision.
- Watch: (a) whether cache-read pricing drop is extended to Haiku 4.5 / Sonnet 5 in a follow-on announcement, (b) whether Mythos 5.1 access expands beyond current restricted cohort, (c) whether the export control status for 5.1 is clarified.
