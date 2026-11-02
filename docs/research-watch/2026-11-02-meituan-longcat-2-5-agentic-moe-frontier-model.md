# Research Watch: LongCat-2.5 — Meituan's Natively Multimodal Agentic MoE

- Repo/Link: https://longcat.ai/blog/longcat-2.5/ (API-only, no public weights; model ID: meituan/longcat-2-5-preview)
- Source: Hacker News (#14, 45 points, 2026-11-02)

## Why this is worth watching

LongCat-2.5 is an agentic frontier model from Meituan — a Chinese tech company known primarily for food delivery and local commerce, not AI research. Its entry into the frontier model space is notable not because it is the most capable model announced this week, but because of what it signals: a major consumer platform operator building a model explicitly designed for the agent use case (terminals, browsers, GUIs, spreadsheets) rather than general chat. The model is natively multimodal, uses a mixture-of-experts architecture with 1.6T total and ~48B active parameters, and supports a 1M-token context window.

The "preview" label and API-only availability suggest the weights are not public yet. Third-party listings show limited-time pricing at $0.30/1M input tokens and $1.20/1M output tokens, which is competitive with mid-tier frontier models.

## What stands out immediately

- **MoE architecture at 1.6T/48B active**: follows the sparse-activation pattern established by Mixtral and DeepSeek-V2; the 48B active parameters give frontier-class reasoning without paying full-density inference cost per token
- **1M-token context window**: one of the longer publicly available contexts; positions it for long-session agentic workflows where earlier models would truncate or summarize
- **Natively multimodal**: text + image inputs; "native" implies the multimodal capability is trained into the base model rather than added as a post-hoc visual adapter
- **Agentic task targeting**: the announcement explicitly lists terminals, browsers, GUIs, and spreadsheets as target surfaces — a narrower framing than general chat, with implications for tool-use benchmarks
- **Competitive pricing**: $0.30/$1.20 per 1M input/output puts it in the same cost band as Claude Haiku 5.5 and Gemini Flash, below Opus and GPT-5 tier
- **Chinese origin, international API**: served through international API providers (Vercel AI Gateway, OpenCode); no geo-restriction on API access in available listings
- **LongCat-2.0 predecessor was open-weight** (per one listing); the 2.5 preview may be a weights-withheld commercial step while the open-weight pipeline continues
- Release date: approximately 2026-09-25 per OpenCode data

## Why clawfit should care

LongCat-2.5 is the first Meituan-origin model in the tracker. Its architectural combination — MoE, 1M context, natively multimodal, agentic-first — is relevant to three open questions in clawfit's registry:

1. **Cost-to-context tradeoff**: the registry currently lacks a `context_window` field. A 1M-token model at $0.30/1M input changes the calculus for long-session agentic workflows (deep-research, document processing) relative to shorter-context models at similar cost.
2. **Chinese frontier model coverage**: the registry tracks DeepSeek, Qwen, and Kronos (financial domain); LongCat-2.5 is a different organization and a different product philosophy (consumer platform company, not AI-first lab or academic group).
3. **"Agentic-first" framing**: multiple models now frame themselves as agentic-first rather than general-purpose. Whether this is architectural (different training regime) or marketing (same base model, different prompt engineering advice) is worth verifying.

For registry: pricing data is available ($0.30/$1.20), the model is API-accessible, and it is a general-purpose (non-domain-specific) LLM-class entry. Star count doesn't apply to models. A registry entry is possible if `context_window` and `origin` (or `provider`) fields are added. No addition today — weights are unverified as public, and benchmark performance against existing registry LLMs is not confirmed.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Model** (primary): a pre-trained frontier model that provides the inference foundation for agent workflows
- **Level 6 — Human Interface** (secondary): the explicit targeting of browser, GUI, and spreadsheet surfaces implies embedded interface affordances beyond pure text API

## Claims to verify

- Meituan's actual involvement: whether Meituan built this internally or acquired/partnered with an AI lab is not clear from the announcement; the model family name (LongCat) appears on the longcat.ai domain, not meituan.com
- 1M context correctness: "1M-token context" must be verified against a primary source; third-party listing sites frequently copy unverified specs
- Whether LongCat-2.0 open weights still exist and are compatible with 2.5 fine-tuning pipelines
- Benchmark performance: no independent evaluation confirmed at time of this note; the announcement cites no public leaderboard results
- API availability stability: "limited-time pricing" language suggests the preview tier may change; long-term commercial access terms are unknown

## Status

- New signal; not previously tracked
- Registry eligibility: LLM-class model; pricing data available; registry addition deferred pending (a) independent benchmark confirmation against existing registry LLMs, (b) verification of API stability, (c) a `context_window` schema field for meaningful representation
- Watch for: HuggingFace model weights release; MMLU/LiveCodeBench/agent-eval benchmark result from a neutral third party; a second Chinese consumer-platform company releasing an agentic model
- 📡 note: first signal for "consumer platform company origin" frontier model (Meituan is food delivery / local services, not an AI lab); watch for platform operators in other regions (delivery, e-commerce) releasing agent-optimized models
