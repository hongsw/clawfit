# Research Watch: DeepSeek V4.1 Flash — Native Multimodal MoE, Official Release Sept 10

- Repo/Link: https://deepseek.com (API: `deepseek-v4.1-flash-expires-on-0910` → official on Sept 10)
- Source: Hacker News front page (351 points); TechNode; PANews; DigitalApplied

## Why this is worth watching
DeepSeek V4.1 Flash is described as "the largest architecture-level update to the V4 series since its release in April 2026." The previous entry in this log (2026-07-31-deepseek-v4-flash-agent-optimized-moe.md) covered V4 Flash, an agent-optimized MoE. V4.1 Flash introduces native multimodal capabilities (text, image, speech) in a unified model architecture — a structural change, not an incremental parameter increase. Official launch is planned for September 10, 2026.

## What stands out immediately
- Native multimodal: text, image, and speech processed in a unified architecture (not adapter-based)
- 427 tok/s throughput; TTFT approximately 178ms (160ms for short Q&A)
- "Comprehensively surpasses V4 Pro" across performance, cost, speed metrics
- Beta pricing identical to V4 Flash — suggesting price parity at higher capability
- API ID `deepseek-v4.1-flash-expires-on-0910` has been open to API users since Sept 8
- Official launch Sept 10, 2026 — within 24 hours of this scan
- No public benchmarks or model card yet (beta test conditions); architecture details not fully disclosed

## Why clawfit should care
DeepSeek V4.1 Flash displaces V4 Pro in performance while (per DeepSeek's claims) maintaining V4 Flash pricing. If confirmed, this breaks the current latency-cost tradeoff assumption embedded in clawfit's scoring: V4.1 Flash would be Pareto-dominant over V4 Pro on cost and performance simultaneously.

More importantly, native multimodal in a Flash-tier model means agents handling image or speech inputs no longer need a dedicated vision or ASR model — the routing logic simplifies. clawfit's current registry has no `modality` field on `llms.json`; this is the third signal (after Gemini 3.5 Transcribe 2026-08-29 and Qwen3.8 2026-08-26) for that gap. A `native_modality: [text-only | text+vision | text+voice | text+vision+voice]` field would let clawfit score V4.1 Flash as a higher-preference choice for multimodal agent profiles.

## Preliminary interpretation
- **Level 1 — Base Agent Runtime / LLM** (primary: model inference substrate)

The native multimodal capability is L1 (model architecture), not L7 (user interface), because it affects what inputs the model natively processes rather than what the user sees.

## Claims to verify
- Official Sept 10 release — as of Sept 9 the model is still beta-expiry only; confirm launch and permanent API ID
- "Comprehensively surpasses V4 Pro" — benchmark methodology not published; this is DeepSeek's internal claim
- Pricing at official launch — beta pricing is not necessarily launch pricing
- Architecture details — "new architecture" described as natively multimodal, but MoE vs. dense and expert count unconfirmed
- Cost per million tokens — required before registry entry

## Status
- New — tracking as major LLM update with direct scoring implications
- No GitHub repo; source is DeepSeek API + news coverage
- Registry eligibility: blocked until Sept 10 official launch confirms pricing, API ID, and benchmarks
