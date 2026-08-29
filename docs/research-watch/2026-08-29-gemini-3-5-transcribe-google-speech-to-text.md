# Research Watch: Gemini 3.5 Transcribe — Google's Precision Speech-to-Text Foundation Model

- Repo/Link: https://deepmind.google/models/gemini/3-5-transcribe/ (no public GitHub repo; official Google product)
- Source: GeekNews front page; 9to5Google (2026-08-26); Engadget; Dataconomy

## Why this is worth watching

Google announced Gemini 3.5 Transcribe on August 26, 2026, positioning it as a dedicated, production-grade speech-to-text foundation model replacing Chirp 3. The significance for the agent ecosystem is not the transcription accuracy alone but the deployment surface: the model is rolling out into Search Live, Gemini Live, Docs, Keep, Gmail, and the Gemini app, while also being exposed as a developer API. This makes it a plausible input layer for voice-capable agent pipelines.

The reported 4.0% word error rate for streaming audio and 2.6% for non-streaming audio, combined with a 70% improvement in time-to-final-transcription vs Chirp 3, would represent a meaningful capability jump for real-time agent interaction scenarios if independently confirmed. The claim of handling background noise, domain-specific vocabulary (order IDs, postal codes, file names), and speaker self-corrections goes beyond generic ASR — these are agent-relevant edge cases.

This is a Google product announcement, not a community project. Promotional framing should be discounted accordingly; independent benchmark comparisons against Whisper, Deepgram Nova 3, and AssemblyAI Universal are necessary before treating the WER figures as settled.

## What stands out immediately

- **4.0% WER streaming / 2.6% WER non-streaming**: better than Chirp 3's claimed performance; where these numbers land on industry benchmarks against Whisper v3-large and Deepgram Nova 3 is not yet public
- **70% reduction in time-to-final-transcription vs Chirp 3**: this is a latency claim for agent pipelines where ASR is on the critical path; "time-to-final" (vs interim) matters for downstream tool invocation
- **Custom vocabulary support** (order IDs, postal codes, file names): suggests fine-grained recognition tuning rather than pure general ASR — useful for domain-specific agent deployments
- **Self-correction and filler-word handling**: the model reportedly cleans transcript output in a post-pass, not just raw STT; this changes the format of input an agent's text processing layer receives
- **Gboard Rambler integration**: powers a consumer product feature (turning "ramblings" into structured text); signals productionized deployment at scale, not a research preview
- **API access for developers**: coming to Google Cloud AI; pricing not yet published
- **No open weights**: proprietary model with no open-source release announced; competes with Whisper (open-weight) and paid services like Deepgram

## Why clawfit should care

Gemini 3.5 Transcribe sits at L1 as a foundation model specialized for speech. For clawfit's current taxonomy, it is most relevant as an input-layer dependency for voice-capable agents (L6 — human interface) rather than as a directly scoreable LLM entry.

However, its API exposure raises a practical question: can clawfit's `task: qa` or `task: research` workflows incorporate a voice input layer, and if so, should ASR providers appear in the registry alongside LLMs? The current schema has no entry type for ASR models — only for LLMs, agents, and hardware. Gemini 3.5 Transcribe is the clearest signal yet that voice-input routing is becoming a distinct infrastructure concern for agent deployments.

The lack of open weights also reinforces the schema gap identified with Hy4-preview and GLM-5.3: `weights: [proprietary | open]` as a registry dimension would allow clawfit to surface build-vs-buy tradeoffs when users specify `hardware: local`.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Runtime / Foundation Model** (primary): Gemini 3.5 Transcribe is a foundation model layer for audio. It is not an agent or harness; it is a capability that agents call.
- **Level 6 — Human Interface** (secondary): the model's primary consumer-visible deployment is in conversational interfaces (Gemini Live, Search Live) and document editors — L6 territory where agents interact with humans

This model is a closer analog to Whisper or Deepgram than to a general-purpose LLM. It doesn't fit cleanly into clawfit's existing LLM registry schema, which assumes text-in/text-out models.

## Claims to verify

- Whether the 4.0% streaming WER and 2.6% non-streaming WER hold on standard open benchmarks (LibriSpeech clean/other, FLEURS, TED-LIUM) or are measured on a proprietary Google test set
- Whether the 70% time-to-final-transcription improvement represents wall-clock improvement at typical 5–30 second utterance lengths, or is measured on specific utterance characteristics
- Whether the custom vocabulary feature requires fine-tuning or is prompt-configurable at inference time
- Whether the API pricing (not yet published) is competitive with Deepgram Nova 3 ($0.0059/minute) or Whisper API ($0.006/minute) for agent pipeline use cases
- Whether the model generalizes across accents and technical jargon, or whether "custom vocabulary" is the primary mechanism for non-standard domain coverage

## Status

- Tracking: first signal 2026-08-29 (product launched 2026-08-26)
- Stars: N/A — no public GitHub repo; proprietary Google product
- Registry decision: skip. Gemini 3.5 Transcribe is an ASR model, not an LLM or agent runtime. The current registry schema (`llms.json`) assumes text-generation models with token-based pricing. ASR pricing is per-minute or per-audio-second. No schema mapping exists today.
- Schema gap: `modality: [text | audio | vision | multimodal]` — the registry currently implicitly assumes `modality: text`; Gemini 3.5 Transcribe is the strongest evidence yet for an explicit modality field in `llms.json`
- Watch: API pricing announcement on Google Cloud AI; independent WER benchmarks from the community; whether livekit/agents (already tracked 2026-07-10) adds native Gemini 3.5 Transcribe support
