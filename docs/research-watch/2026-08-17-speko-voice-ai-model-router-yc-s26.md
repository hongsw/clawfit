# Research Watch: Speko — Voice AI Model Router (YC S26)

- Repo/Link: https://speko.ai / https://speko.dev
- YC: https://www.ycombinator.com/companies/speko (S26 batch)
- Source: Hacker News (Launch HN, 54 points, 2026-08-17)
- Prior tracking: OpenRouter routing architecture tracked 2026-05-31; voice model category tracked via pipecat (2026-07-10), LiveKit (2026-07-10), Moonshine Micro (2026-07-19)

## Why this is worth watching

Speko is an inference-routing layer specialized for voice AI models, positioned as "OpenRouter for voice AI." It routes speech-to-text (STT) and text-to-speech (TTS) requests across 21+ models from OpenAI, Google, AssemblyAI, Deepgram, and others — choosing the best model per request based on language and measured accuracy rather than vendor default. The comparison to OpenRouter is structural: Speko does for voice models what OpenRouter does for LLMs — abstracts the provider surface behind one API, routes based on performance data, and provides failover.

The YC S26 backing signals that routing infrastructure for specialized model categories (voice, vision, code) is perceived as a standalone market, not just a feature of a larger platform. Speko's founding story — the founder previously consulted for frontier labs on voice model quality evaluation before they shipped — indicates domain depth that is rare at the pre-product stage.

## What stands out immediately

- **Language-specific routing:** benchmarks across 9 languages reveal that "4 different models win across 9 languages" — no single speech model is universally optimal. Routing by detected language is a measurable accuracy improvement over provider-default model selection. This is empirically grounded, not a marketing claim — the measurements are published.
- **21+ STT model coverage, 9 language benchmarks:** includes OpenAI Whisper family, Google Speech-to-Text, AssemblyAI Universal, Deepgram Nova, and others. Coverage is wide enough to be practically useful for multilingual applications; benchmark scope is narrow enough (9 languages) to be verifiable.
- **Pricing transparency:** model costs published ($0.001/min–$0.016/min range depending on accuracy). This makes Speko suitable for cost-aware routing decisions — cheaper at lower WER requirements, more expensive at higher accuracy requirements — analogous to budget-based LLM routing.
- **<500ms failover:** mid-conversation failover under 500ms is the key real-time voice reliability claim. Whether this holds under load and across provider API latency is the key claim to verify.
- **OpenAI-protocol API:** clients change only the base URL and API key. Integration with LiveKit and Pipecat (both tracked L2 voice agent frameworks) confirmed with base-URL-only change. This is the same integration strategy oMLX uses for LLM endpoints.
- **MCP server support:** Speko exposes an MCP server interface, making it callable as a tool from Claude Code and other MCP-compatible agents. This is notable for a voice routing service — it means an agent can programmatically select and invoke voice models through Speko as a capability.
- **Founder domain pedigree:** Beknazar Abdikamalov previously co-founded Hupo (backed by DST Global, Meta, Goodwater Capital). The frontier-lab consulting history on voice model quality is cited as the source of the routing methodology.

## Why clawfit should care

Speko is a direct structural analogue of OpenRouter at the voice-model layer. The Stripe/OpenRouter acquisition (tracked 2026-08-17) raises the question of whether OpenRouter's LLM routing model will remain neutral or become commercial infrastructure — Speko is positioned at the same routing layer for a different modality at a moment when that question is live.

For clawfit's recommendation model, Speko introduces a pattern not yet modeled: **modality-specialized routing infrastructure** as a layer between the agent harness and the model provider. The current clawfit schema assumes agent harnesses call LLM providers directly (with possible routing via OpenRouter or LiteLLM). Speko extends this to voice models — a modality increasingly relevant to L6 human interface recommendations (LiveKit, Pipecat, Moon shine Micro, kyutai-pocket-tts — all tracked in the voice-agent space).

**Cross-signal with OpenRouter acquisition (2026-08-17):** Stripe acquiring OpenRouter at $7B+ for LLM routing; Speko launching for voice routing at seed/S26. Same architectural pattern applied to two different modalities. Whether "modality-specialized routing" is the winning architecture or whether a general-purpose router (OpenRouter expanding to voice) wins is an open question — Speko's launch is the voice-specialist bet.

**Cross-signal with pipecat (2026-07-10) and LiveKit (2026-07-10):** both tracked as L2 voice agent frameworks with multi-provider STT/TTS support. Speko is explicitly documented as compatible with both via base-URL change. This is the first tracked L7 infrastructure piece that sits *below* pipecat/LiveKit as a routing/reliability layer rather than above them as an orchestration harness.

**Schema gap:** `voice_routing: bool`; `stt_provider_routing: [direct | speko | openrouter-voice]`; `voice_failover_sla_ms: int`; the current schema does not model voice routing as a dimension.

## Preliminary interpretation

- **Level 7 — Infrastructure / routing layer** (primary): Speko is voice model routing infrastructure — not a harness, not a skills layer, not a voice agent. It sits at the same architectural position as OpenRouter (L7 LLM routing) but for the voice-model modality.
- **Level 4 secondary (MCP capability):** the MCP server mode makes Speko callable as a tool from within agent sessions — agents can programmatically invoke voice synthesis or transcription via MCP tool call. But the primary function is infrastructure.
- Not L2 (harness): Speko does not orchestrate agent tasks; it routes voice model calls.
- Not L6 (human interface): Speko is not an end-user interface — it is middleware consumed by L6 interface frameworks.
- Closest structural analogue: **OpenRouter** (L7, LLM routing, tracked 2026-05-31, now Stripe-subsidiary); same architectural role, voice modality.

## Claims to verify

- **<500ms failover under real-world load:** latency claim is for the routing decision and reconnect — what is the end-to-end audio gap from provider failure to first audio byte from the backup provider?
- **Benchmark methodology:** "published measurements instead of vendor English leaderboard" — are the benchmarks independently reproducible, and what is the test set (proprietary recordings, public datasets, or user-provided data)?
- **11 of 23 models measured in English only:** acknowledged coverage gap — for non-English deployments, what is the fallback behavior when the optimal model for a language is unmeasured?
- **MCP server stability:** MCP is listed as a feature — is it a fully implemented server or a beta/experimental capability with known gaps?
- **Pricing parity:** Speko charges a platform fee on top of provider costs (analogous to OpenRouter's 5.5%) — what is the markup structure, and does it make high-accuracy STT (Universal-3.5 Pro at $0.0075/min + markup) non-competitive with direct provider pricing?

## Status

- No public GitHub repository (SaaS product, not open-source)
- YC S26 batch — seed-stage; no deterministic throughput or latency SLA published beyond the <500ms failover claim
- **No registry entry:** SaaS routing service, no `agents.json`/`llms.json`/`hardware.json` schema mapping; no deterministic cost data (markup not published)
- **No canonical section change:** single signal for "modality-specialized voice model routing" sub-type; two-signal rule requires a second independent voice routing layer
- **Watch for:** second tracked dedicated voice model router (would trigger L7 routing sub-section for modality-specialized routing); Speko adds open-source self-hosted option; OpenRouter announces voice routing parity (would threaten Speko's positioning); pricing structure published
