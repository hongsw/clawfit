# Research Watch: Kimi K2.6 (Moonshot AI)

- Repo: https://huggingface.co/moonshotai/Kimi-K2.6
- Also see: https://www.kimi.com/blog/kimi-k2-6.html | https://platform.moonshot.ai | https://arxiv.org/abs/2602.02276

## Why this is worth watching

Kimi K2.6 enters the open-weight frontier coding tier with SWE-Bench Verified 80.2% — above Grok 4.3 (unconfirmed independent score at time of writing) and just below DeepSeek V4-Pro (80.6%), in a cluster where a 0.4-point gap is within noise. At $0.95/M input and $4.00/M output it is priced higher than V4-Pro ($0.435/M) but carries open weights under a Modified MIT license and introduces a documented 300-agent horizontal swarm that scales to 4,000 coordinated steps — a claim not present in either V4-Pro or Grok 4.3. The combination of frontier-tier coding benchmark, open weights, and a natively specified multi-agent architecture at release makes this the most structurally distinct entry in the current SWE-Bench cluster.

## What stands out immediately

- **Architecture**: 1T total / 32B active MoE. 61 layers (1 dense + 60 MoE), 384 total experts, 8 selected per token, 1 shared expert. MLA attention (Multi-head Latent Attention), same architecture family as K2.5 — confirmed by HuggingFace model card.
- **Vision encoder**: MoonViT (400M params). Image, video, and text input; text output. First in this watch cluster with a named dedicated vision encoder at open-weight release.
- **Context window**: 256K tokens. Lower than DeepSeek V4-Pro (1M) and Grok 4.3 (1M); this is a confirmed architectural limit, not a retrieval approximation.
- **SWE-Bench Verified 80.2%**: Confirmed from HuggingFace model card. Positions K2.6 between DeepSeek V4-Pro (80.6%) and the mid-tier below 65%. SWE-Bench Pro 58.6% is the strongest verified figure in the current frontier cluster on that benchmark; V4-Pro and Grok 4.3 do not yet have confirmed SWE-Bench Pro scores at time of writing.
- **Terminal-Bench 2.0: 66.7%**: Agentic terminal task benchmark. No comparable figure exists in V4-Pro or Grok 4.3 watch docs — this is a distinct evaluation axis.
- **AIME 2026: 96.4%, GPQA-Diamond: 90.5%**: Math and science reasoning scores are competitive with frontier closed models (GPT-5.4, Claude Opus 4.6 are cited in Moonshot's own comparisons). Treat as internal benchmark claims; independent confirmation pending.
- **300-agent swarm / 4,000 coordinated steps**: The blog post specifies horizontal scaling to 300 sub-agents executing 4,000 steps simultaneously. This is 3x the sub-agent count and ~2.7x the step depth vs K2.5 (100 agents / 1,500 steps). This is a claim to inspect: the swarm architecture is described at the product layer (Kimi API / "Claw Groups"), not the open-weight checkpoint level. The HuggingFace weights themselves do not include scheduler code.
- **Two inference modes**: Thinking Mode (CoT, temperature 1.0) and Instant Mode (no CoT, temperature 0.6, `thinking: disabled` via extra_body param). Unlike Grok 4.3's always-on reasoning, the mode is user-selectable — relevant for latency-sensitive clawfit profiles.
- **Inference backends**: vLLM, SGLang, KTransformers recommended. Transformers >=4.57.1 required.
- **License**: Modified MIT. The modification terms are not spelled out in the HuggingFace model card at time of writing; treat as open-weight with possible usage-scope carve-outs until the full license text is reviewed. Not the same as plain MIT as shipped by DeepSeek V4-Pro.
- **Pricing (API)**: $0.95/M input, $4.00/M output on platform.moonshot.ai. At 3:1 input:output ratio, blended cost ~$1.80/M — higher than V4-Pro ($0.435/M) and Grok 4.3 ($1.56/M blended), but open weights enable self-hosted deployment that bypasses API pricing entirely.

## Why clawfit should care

clawfit's llms.json has no entry for any Moonshot AI model. K2.6 occupies a position in the SWE-Bench cluster (80.2%) that is currently held only by V4-Pro (80.6%) among open-weight candidates logged in research-watch. Two differences matter for the recommendation engine:

1. **Selectable reasoning mode**: Unlike Grok 4.3's mandatory reasoning overhead, K2.6 can run in Instant Mode, making it a candidate for `latency: low` profiles — a slot Grok 4.3 cannot fill. This is a direct filter-layer implication in `filters.py`.

2. **256K vs 1M context**: K2.6's context ceiling is lower than V4-Pro and Grok 4.3. For tasks requiring long-context retrieval (research, document analysis), this is a hard constraint. The scoring model should reflect this differential before any llms.json addition.

The agent swarm claim (300 agents / 4,000 steps) is product-layer behavior available via Moonshot's hosted API, not a capability that transfers to self-hosted open-weight deployments. It is relevant to Level 2 harness evaluation but should not inflate the base LLM score in the registry.

The Modified MIT license warrants a close read before marking K2.6 as unrestricted open-weight. Until the exact carve-out terms are confirmed, classify conservatively.

## Preliminary interpretation

Current best reading:
- **Not an ecosystem layer** — this is an LLM backend, same registry slot as `deepseek-v4-pro`, `gpt-4o`, `claude-sonnet`.
- Maps to `llms.json`, not to any of the 7 ecosystem layers in reference-levels.md.
- If added, suggested registry profile: `tasks: [code-gen, qa, research]`, `latency: low` (Instant Mode) or `latency: medium` (Thinking Mode), `context_k: 256`, `network: online`, `cost_per_1k_tokens: 0.00095`.
- The 300-agent swarm scheduler is a separate product signal: primary **Level 2 — Meta wrappers / harnesses / orchestration layers**, worth a dedicated watch doc when Claw Groups API specs are public.

## Status

- Registry threshold: open weights on HuggingFace, active commercial API, Modified MIT license pending full text review. Benchmark position (SWE-Bench 80.2%) verified from model card. Recommend holding for (1) full Modified MIT license text review, (2) one independent SWE-Bench confirmation, and (3) context window limitation (256K) factored into scoring weights before adding to llms.json. Flag for 2026-05 calibration cycle alongside V4-Pro and Grok 4.3.
