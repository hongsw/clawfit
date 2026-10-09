# Research Watch: Whistle — 16.9 MB Speech-to-Text from Cactus Compute

- Repo/Link: https://github.com/cactus-compute/needle · https://cactuscompute.com/blog/whistle
- Source: Hacker News (Show HN: Whistle – Speech to Text in 16.9 MB, front page 2026-10-09)

## Why this is worth watching
Cactus Compute, already tracked for Needle (26M-parameter function-call model, 2026-07-14), has released a second purpose-built model — Whistle — targeting the voice input side of the agent stack. At 16.9 MB, it is 8.6× smaller than Whisper base (145.3 MB) and ships a prebuilt engine for 17 targets including iOS, Android, watchOS, browser (WASM), and WASI. The same organization is now covering both the "hear the user" (Whistle) and the "call a tool" (Needle) sides of an on-device agent loop.

## What stands out immediately
- **16.9 MB total weight** — not a quantized Whisper; custom encoder-decoder architecture (8 Simple Attention encoder + 8 Laddered Simple Attention decoder blocks, width 512)
- **17 prebuilt targets**: macOS, Linux, Android, iOS, watchOS, Windows on ARM, RISC-V, MIPS, browser, WASI component — broader platform coverage than Needle
- **Seven languages**: English, German, French, Spanish, Italian, Dutch, Polish — no multilingual expansion yet
- **11.1 ms to first token, ~1,319 tokens/s decode** (Apple M4 Pro CPU, 10-second clip)
- **Per-word timestamps and speech embeddings** as optional outputs — not just transcript text
- **30-second max clip per pass**; 8,192-token vocabulary
- **Open model** ("open speech recognition model") but license terms not yet confirmed

## Why clawfit should care
Cactus Compute is now building a two-model pair (Needle + Whistle) that covers the tool-dispatch and voice-input ends of an edge agent pipeline without cloud API calls. Whistle adds a voice input capability layer (L4) to the L1 runtime signal Needle represented. Together they represent a minimal on-device agent stack: hear (Whistle) → plan → call (Needle). This has direct implications for `hardware: local`, `network: offline`, and `latency: low` scoring dimensions — particularly for wearable and mobile deployment profiles not yet represented in clawfit's hardware registry.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capabilities** (primary): Whistle is a standalone input-modality capability that any agent harness can integrate; it does not orchestrate or govern agents
- **Level 1 secondary**: as a model that runs on the same Cactus inference runtime as Needle, it also functions as a base runtime component in the Cactus on-device stack

## Status
- Same GitHub repo as Needle (cactus-compute/needle), but Whistle is a distinct model
- Registry eligibility: deferred — deployment cost model unclear (self-hosted = no per-token cost); may warrant a new `capability_type: voice_input` field in the schema
- First signal for "ultra-compact cross-platform STT for on-device agent voice input" at L4
- Cactus two-model pattern (Needle + Whistle) reinforces the micro-device / wearable hardware tier noted in the 2026-07-14 Needle doc
