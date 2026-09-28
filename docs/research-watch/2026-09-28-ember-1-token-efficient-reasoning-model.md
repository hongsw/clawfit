# Research Watch: Ember-1 — Token-Efficient Reasoning Model on Kimi K3

- Repo/Link: https://fireworks.ai/models/fireworks/ember-1 (no GitHub repo; API-hosted)
- Source: Hacker News front page (561 points, 2026-09-28)

## Why this is worth watching

Ember-1 is a distillation-optimized variant of Kimi K3 (itself one of the leading open-weight reasoning models) trained by Fireworks Research to eliminate unnecessary internal reasoning tokens while preserving answer quality. The claim: 40% fewer tokens on average at comparable quality to Kimi K3 maximum. For agentic workloads — where reasoning chains often span dozens of turns and tool calls — a 40% token reduction at the same quality level is not a minor optimization; it's a cost and latency halving at the inference layer. The 561 HN points in one day suggests this landed as a credible result, not a marketing claim.

## What stands out immediately

- **40% token reduction vs. Kimi K3**: measured via live A/B testing by Fireworks, with "approximately 35% fewer tokens per task at comparable quality" confirmed in controlled conditions — two separate measurement methods both support the claim
- **Kimi K3 base**: Kimi K3 is a state-of-the-art open-weight reasoning model; this isn't a weaker base with a compressed top — it's a full-capability model trained to reason more efficiently
- **Coding workload focus**: the primary use case cited is "agentic tasks and code assistance at lower cost" — aligns directly with clawfit's target audience
- **Clinical benchmark result**: Doximity Bedside Bench (clinical cases) shows a new Pareto frontier vs. GPT-5.6 Sol and Claude Opus 5 — quality is verified on a task requiring extended reasoning, not just short-answer benchmarks
- **Multi-turn efficiency**: "maintains efficiency across extended conversations" — the token reduction compounds in multi-turn agent sessions
- **Research Preview on Serverless**: two-week free tier removes cost barrier for evaluation; serverless deployment removes infrastructure barrier
- **Token reduction range 5.9–51.9% across benchmarks**: the variance is wide — the 40% average is real but workload-dependent; some tasks see minimal reduction, others see near-halving
- **Built on Kimi K3 API pricing**: cost is transparent (public Kimi K3 pricing as baseline) — this is unusually explicit for a preview-stage model

## Why clawfit should care

Ember-1 belongs in clawfit's LLM registry (llms.json) if its quality-efficiency Pareto frontier holds up at GA. The current registry covers 7 LLMs; none are explicitly optimized for token efficiency in the way Ember-1 claims. For clawfit's scoring, token efficiency per task is more relevant than raw benchmark scores — an agent that completes a code-gen task in 60% of the tokens at the same quality is strictly better for any cost-sensitive recommendation.

More broadly, Ember-1 signals a product pattern: model providers are not just competing on capability, but on reasoning token economy. This is a different axis than the quality-vs-cost tradeoff clawfit currently scores (via budget filter and LLM preference weight). The efficiency dimension — reasoning tokens per task completion — is not captured in any current scoring weight. If this pattern holds (K3→Ember-1, likely K3.1→Ember-2 etc.), clawfit's LLM scoring will need an efficiency axis beyond $/million tokens.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base LLM / Model** (primary): a hosted model API, not an agent framework or orchestration layer
- The token efficiency optimization is a training innovation, not an inference or harness innovation — it belongs in the LLM layer
- Relevant to clawfit's `llms.json` registry entry criteria (cost, latency, quality profile), not to the agent or hardware registries

## Claims to verify

- "40% fewer tokens" is a Fireworks-internal A/B test result — independent replication needed; the 5.9–51.9% range suggests the average is sensitive to task distribution
- The Doximity clinical benchmark is a niche evaluation; transfer to general coding/QA tasks is not demonstrated in the announcement
- "At comparable quality" — quality parity with Kimi K3 maximum is the specific claim; check whether standard benchmarks (HumanEval, MATH, etc.) confirm or contradict this
- Serverless pricing at GA may differ from the Kimi K3 baseline cited in the preview
- No open-weight release (no GitHub repo, no Hugging Face checkpoint): this is a closed API service, not an auditable model

## Status

- Tracking; no GitHub repo (API-hosted model)
- **Registry candidate for llms.json** once GA pricing and independent benchmark confirmation available
- Token efficiency as a scoring axis is a genuine gap in current clawfit scoring; see `scoring.py` weight review
- The free preview tier expires (2 weeks stated); evaluation window is time-limited
