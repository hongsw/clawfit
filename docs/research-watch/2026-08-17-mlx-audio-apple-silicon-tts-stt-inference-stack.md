# Research Watch: mlx-audio — Unified TTS/STT/Music Inference Stack for Apple Silicon

- Repo: https://github.com/Blaizzy/mlx-audio (⭐7,746)
- Source: GitHub Trending (Python, daily) 2026-08-17
- License: MIT
- Language: Python (MLX backend)
- Author: Blaizzy (community)

## Why this is worth watching

mlx-audio is the most comprehensive audio inference library for Apple Silicon that has appeared on GitHub Trending. It unifies text-to-speech (TTS), speech-to-text (STT), speech-to-speech (STS), and music generation in a single framework built on Apple's MLX — running quantized audio models entirely on M-series chips without cloud round-trips. At 7.7k stars it is above the 5k signal threshold.

The significance for clawfit is not audio as an entertainment feature — it is audio as a voice interface layer for local agents. TTS/STT running locally on the same hardware that runs the inference model closes the latency and privacy loop for voice-driven agent interactions on Apple Silicon. oMLX (tracked 2026-08-16) addressed the LLM inference side; mlx-audio addresses the voice interface side on the same hardware platform.

## What stands out immediately

- **30+ TTS models, 15+ STT models in one library:** the model catalog is unusually wide for a single inference library. Notable implementations: Kokoro (82M parameters, 54 voices), Qwen3-TTS (multilingual with voice cloning), OmniVoice (646+ language support). The breadth signals that mlx-audio is positioning as a registry/router for audio models, not just a wrapper for one.
- **Four quantization levels (3-bit through 8-bit):** MLX quantization support across the full model catalog enables fitting larger TTS models into M-series unified memory at different quality/size tradeoffs — the same tradeoff space that LLM inference offers for language models.
- **OpenAI-compatible REST API server:** exposes TTS and STT endpoints using the OpenAI audio API protocol (`/v1/audio/speech`, `/v1/audio/transcriptions`). Frameworks and agents that use OpenAI's TTS/STT can switch base URL to a local mlx-audio server — same integration pattern as oMLX's OpenAI-compatible LLM endpoint.
- **Streaming TTS support:** real-time audio streaming enables low-latency voice output for interactive agent conversations — relevant for voice-driven agent interfaces where waiting for full audio synthesis before playback is a user experience problem.
- **Speech-to-speech (STS) pipeline:** transcribe (STT) → process (LLM/agent) → synthesize (TTS) as a unified pipeline, not three separate tool invocations. Reduces integration overhead for voice agent loops.
- **941 commits on main, 70 open issues:** active development trajectory; not a one-person hobby project with low maintenance expectation.
- **3D audio visualization in web UI:** a web UI with 3D audio visualization is an unusually polished interface for an inference library — may indicate intent to be an end-user-facing tool as well as a developer library.

## Why clawfit should care

mlx-audio is infrastructure for an agent interface mode not yet profiled in clawfit: **local voice I/O on Apple Silicon**. The current clawfit hardware profiles cover `local_mac` for LLM inference but do not model TTS/STT as a separate capability dimension. Two emerging signals now converge on Apple Silicon as a complete local agent runtime:

1. **oMLX (2026-08-16):** multi-model LLM inference server on Apple Silicon with SSD KV cache tiering and OpenAI-compatible endpoint
2. **mlx-audio (2026-08-17):** TTS/STT/music inference stack on Apple Silicon with OpenAI-compatible endpoint

Together they describe a `hardware: local_mac` profile where the full agent pipeline — LLM reasoning (oMLX) + voice I/O (mlx-audio) — runs locally on a single M-series device without cloud dependencies. This combination is relevant to `data_sensitivity: confidential` and `network: offline` profiles where cloud voice APIs (ElevenLabs, OpenAI TTS, Azure TTS) are not acceptable.

**Two-signal note on Apple Silicon complete-agent-stack:** oMLX (2026-08-16) + mlx-audio (2026-08-17) together represent a "local Apple Silicon full-stack" pattern: one provides the LLM layer, the other provides the voice I/O layer. Both use OpenAI-compatible API protocols and MLX as the backend. This is a candidate for a two-signal pattern, but the two signals cover *different layers* (L1 inference vs. L7 interface) rather than confirming the *same sub-type*. One-signal caution: no canonical section change warranted yet.

**Schema gap:** `voice_io: [none | cloud-tts | cloud-stt | local-mlx-audio | local-other]`; `tts_provider: [elevenlabs | openai | azure | local-kokoro | local-qwen3-tts | ...]`; the current schema has no audio I/O dimension at all.

## Preliminary interpretation

- **Level 7 — Infrastructure** (primary): mlx-audio is audio inference infrastructure — it provides the compute layer for TTS/STT workloads on Apple Silicon hardware. Closest L7 analogues: oMLX (L1/L7, LLM inference on Apple Silicon), h3.c (tracked 2026-08-11, native video diffusion inference).
- **Level 6 secondary (voice interface layer):** the speech-to-speech pipeline and streaming TTS make mlx-audio a direct enabler of voice-driven human-agent interaction — the boundary between "audio inference infrastructure" (L7) and "voice human-agent interface" (L6) is blurry here. Primary classification is L7 because mlx-audio does not itself provide a conversation or agent loop — it is a library consumed by L6 interfaces.
- Not L2 (harness): mlx-audio does not orchestrate agent tasks; it provides audio I/O primitives.
- Not L4 (MCP server): no MCP interface documented; integration is via REST API or Python SDK.

## Claims to verify

- **646+ language support in OmniVoice:** this is an extraordinary claim for a TTS model. What is the definition of "language support" — full fluency, phoneme coverage, or accent support for language-tagged text?
- **Quantization quality floor at 3-bit:** 3-bit quantization is aggressive for TTS models (where audio artifacts accumulate from weight errors in ways that are perceptually obvious). What is the measured audio quality degradation at 3-bit vs. 8-bit for Kokoro and Qwen3-TTS?
- **OpenAI protocol completeness:** the REST API claims OpenAI protocol compatibility — does this cover streaming responses, audio format options (mp3, opus, aac, flac), and voice parameters, or only the base endpoint?
- **Star attribution:** 7.7k stars on a Python audio library is high. Is the growth organic from MLX ecosystem community, or amplified by a specific trending event or launch post?

## Status

- 7,746 stars — above 5k threshold; **no registry entry**: mlx-audio is audio inference infrastructure, not an agent, LLM, or hardware entry in clawfit's current schema
- **No canonical section change:** single signal for "unified TTS/STT inference library on Apple MLX"; two-signal rule requires a second independent unified audio library on Apple MLX
- **Two-signal cross-note:** oMLX (2026-08-16) + mlx-audio (2026-08-17) describe a `local_mac` full-stack but cover different architectural layers (L1 LLM vs. L7 audio). Not the same sub-type; no canonical change.
- **Schema watch:** `voice_io` dimension missing from all current clawfit recommendation profiles; hardware profile `local_mac` covers only LLM inference, not audio I/O
- **Watch for:** second tracked unified audio library on Apple MLX (would satisfy two-signal rule for L7 audio sub-section); documented integration with oMLX as co-deployed local-mac stack; MCP server mode added (would elevate to L4 secondary)
