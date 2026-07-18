# Research Watch: Kimi K3 (Moonshot AI)

- Repo: https://huggingface.co/moonshotai/Kimi-K3 (weights pending; promised by 2026-07-27)
- Also see: https://simonwillison.net/2026/Jul/16/kimi-k3/ | https://openrouter.ai/moonshotai/kimi-k3 | https://news.ycombinator.com/item?id=48947717

## Why this is worth watching

K3 is Moonshot AI's follow-up to K2.6 at 2.8T total parameters — self-described as the first open 3T-class model — with a 1M token context window that directly addresses the 256K ceiling that was flagged as K2.6's primary structural weakness. Artificial Analysis places it at Elo 1547 on their private long-horizon evaluation, a reported +732-point jump from K2.6, with SWE-Bench FrontierSWE rising to 81.2% (from K2.6's 80.2%) and Terminal-Bench 2.1 at 88.3%. The open-weight release is promised but not yet delivered — weights are expected 2026-07-27.

## What stands out immediately

- **Architecture**: MoE at 2.8T total parameters, 16 of 896 experts active per token (vs K2.6's 8 of 384 experts from 1T total). Parameter count tripled; active compute roughly doubled.
- **Context window**: 1M tokens — closes the gap versus DeepSeek V4-Pro and Grok 4.3 that was explicitly flagged in the K2.6 watch doc.
- **Benchmark claims**: FrontierSWE 81.2%, DeepSWE 67.5%, Terminal-Bench 2.1 88.3%, GPQA Diamond 93.5%, BrowseComp 91.2%. Self-reported; independent confirmation pending.
- **Pricing**: $3/M input, $15/M output — a 3x–4x increase over K2.6 ($0.95/$4). Now priced at Claude Sonnet tier, described as the most expensive Chinese lab release to date.
- **Single reasoning effort only**: K3 exposes only a "max" reasoning mode. K2.6's dual Thinking/Instant modes — which made it a candidate for `latency: low` profiles in clawfit — are absent. Simon Willison's pelican test consumed 13,241 reasoning tokens to produce 3,417 output tokens of SVG, costing $0.25 for a trivial prompt.
- **Pelican benchmark signal**: The benchmark's utility is degrading as a model-quality discriminator — Willison notes it "no longer strongly correlates with model quality" — but it usefully exposed K3's runaway reasoning-token behavior on simple tasks.
- **Open weights status**: API-only at time of writing. Weights promised 2026-07-27; treat as closed until confirmed.

## Why clawfit should care

Two implications for the registry and scoring engine:

1. **Context window gap closed**: K2.6 was held from `llms.json` partly because 256K context ruled out `task: research` profiles. K3's 1M window removes that constraint — but the weights-pending and pricing-tier questions still apply.

2. **Reasoning mode regression matters for filter logic**: K2.6's Instant Mode gave it a `latency: low` slot unavailable to Grok 4.3. K3 loses that. At $15/M output with mandatory max-effort reasoning, K3 cannot satisfy `latency: low` or `budget` profiles below roughly $0.015/task. This is a filter-layer regression relative to K2.6, not an upgrade.

## Preliminary interpretation

Current best reading:
- **Not an ecosystem layer** — same registry slot as K2.6, `deepseek-v4-pro`, `gpt-4o`: a base LLM backend.
- Maps to `llms.json` as a Level 1 frontier open-weight LLM once weights are confirmed.
- If added, suggested profile: `tasks: [code-gen, research]`, `latency: medium` (mandatory max reasoning, no fast mode), `context_k: 1000`, `network: online`, `cost_per_1k_tokens: 0.003`. Not a `latency: low` candidate.
- The +732 Artificial Analysis Elo gain over K2.6 is a strong quality signal, but it is a single private benchmark. Treat as claim to inspect until FrontierSWE and Terminal-Bench scores receive independent replication.

## Status

- Weights pending (2026-07-27 target); hold `llms.json` addition until open-weight release is confirmed, pricing-tier fit is assessed against clawfit budget profiles, and at least one independent benchmark replication is available.
