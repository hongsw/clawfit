# Research Watch: pocket-tts — CPU-Optimized Neural TTS from Kyutai Labs

- Repo: https://github.com/kyutai-labs/pocket-tts (⭐6,000)
- Source: GitHub Trending Python (2026-07-07)

## Why this is worth watching

pocket-tts is a lightweight, CPU-deployable text-to-speech system from Kyutai Labs — the same French AI research group that shipped Moshi (real-time speech-to-speech LLM, first tracked 2025). The 100-million-parameter model achieves ~200 ms time-to-first-audio-chunk and ~6× faster than real-time throughput on a MacBook Air M4 CPU — without a GPU. This is the third independent local voice/audio AI tool in this scan series: Meetily (tracked 2026-07-04, now at 20,410★) is a meeting assistant; huggingface/speech-to-speech (tracked 2026-07-04) is a composable voice pipeline; pocket-tts adds a standalone CPU TTS component. The previous monitoring note for the voice cluster stated "if a third independent local voice/audio AI tool appears, consider adding `voice-agent` as a named sub-type" — that condition is now met.

## What stands out immediately

- ~200 ms first-audio-chunk latency on CPU; no GPU dependency — directly compatible with `hardware: local_cpu` profiles in clawfit
- ~6× faster than real-time on M4 hardware (no independent benchmark confirmation; Kyutai's own measurement)
- Voice cloning support: custom speaker from a reference audio sample
- Multi-language: English, French, German, Portuguese, Italian, Spanish (6 languages)
- 100M-parameter model — small enough to embed in agent pipelines without memory pressure
- pip-installable with a two-line Python API: no external service dependency
- v2.1.0 (May 4, 2026); 8 releases total — early but maintained
- Kyutai Labs provenance: institutional credibility (INRIA, École polytechnique affiliation) beyond a solo-developer project
- Complements Moshi (real-time STT+LLM+TTS, Kyutai): pocket-tts is TTS-only, offering a narrower and lighter component

## Why clawfit should care

Voice output is not currently a scoreable axis in clawfit's recommendation schema. As AI agents increasingly operate in voice-interface contexts (meeting assistants, voice-enabled workflows, ambient computing), the ability to produce audio output becomes a capability that clawfit should surface. pocket-tts is directly pip-installable and CPU-compatible, meaning it is accessible to `network: offline` + `hardware: local_cpu` profiles — the same profiles that favor Aider and Goose in current scoring. The CPU-only constraint also makes it relevant to `budget: 0.00` profiles where cloud TTS API costs are a barrier. If clawfit adds a `modality.output` dimension (text, voice, multimodal), pocket-tts is the reference entry for CPU-local voice output.

The three-signal voice cluster (Meetily 20k★, speech-to-speech 5.3k★, pocket-tts 6k★) now satisfies the monitoring threshold set in the 2026-07-04 scan notes. Meetily crossing 20k★ (20,410★ as of today) also meets the alternative promotion criterion ("one of these crosses 20k★"). The sub-types within this cluster remain diverse (application, composable pipeline, TTS component), which argues against a single unified sub-type. A more precise framing: "local voice output" (pocket-tts, speech-to-speech TTS stage) vs. "local voice application" (Meetily) — two narrower sub-types within the voice cluster.

## Preliminary interpretation

Current best reading:
- **Level 4b primary — Capability layer** (installable voice synthesis component; directly pip-installed into agent pipelines)
- **Level 6 secondary — Human interface** (voice as an output modality for agent-to-human communication)

Three-signal voice cluster update: the 2026-07-04 monitoring condition ("third independent local voice/audio AI tool") is now met. However, the sub-types within the cluster (TTS component vs. composable pipeline vs. meeting assistant application) are distinct enough that a single named L4b/L6 "local voice" sub-type would be over-broad. A more useful pair: `voice-output-component` (pocket-tts, speech-to-speech TTS stage) and `voice-application` (Meetily). Neither sub-type has reached two-signal confirmation for its specific framing.

## Status

- 6,000★, v2.1.0 (May 4, 2026), Apache-2.0, Python 91.6%
- Above 5k registry threshold; registry hold: no `modality.output` or `task: voice-synthesis` field in current schema; latency figures are Kyutai's own measurements on a single hardware reference
- Schema watch: `modality.output: [text, voice, multimodal]`; `hardware.voice_output: cpu | gpu | cloud` as a new sub-axis
- Promotion criterion: independent third-party benchmark confirming <300ms first-chunk on commodity CPU hardware AND schema gains `modality.output` field
- Three-signal voice cluster: monitoring flag promoted — recommend `docs/reference-levels.md` annotation for voice output component sub-type when a second independently usable CPU TTS pip library appears
