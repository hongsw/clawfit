# Research Watch: moonshine-ai/moonshine micro — Sub-500KB On-Device Speech+TTS

- Repo/Link: https://github.com/moonshine-ai/moonshine/tree/main/micro
- Source: Hacker News (200 points, 2026-07-19)

## Why this is worth watching
moonshine-micro is an on-device speech recognition and TTS model family that fits in under 500KB — a 100–1000× footprint reduction vs. tracked alternatives (Whisper-tiny ≈ 75MB; Coqui TTS ≈ 200MB). It targets browser WASM, embedded devices, and edge MCUs, enabling a fully offline voice interface to an AI agent with no server round-trips and no cloud dependency.

## What stands out immediately
- Sub-500KB total size including both STT and TTS in a single model artifact
- Designed for WASM and ARM microcontrollers — not just desktop/mobile
- Inference in-browser without any network hop, enabling true offline voice agent interaction
- Separate from the main moonshine project (Whisper-class accuracy); micro trades accuracy for extreme compactness
- 200 HN points on day of post — organic, not self-promotion

## Why clawfit should care
Current L7 voice agent frameworks (pipecat ⭐13k, livekit/agents ⭐11k) handle pipeline orchestration but depend on a cloud-hosted or locally-running STT/TTS provider. moonshine-micro would let an `network: offline` agent profile gain voice I/O without any backend service. This fills the last gap in a fully-local voice coding agent stack: local LLM (ollama/Goose) + local voice (moonshine-micro). It also opens the `hardware: phone-class` + `voice` profile slice that currently has no viable offering at this footprint.

## Preliminary interpretation
Current best reading:
- **Level 7 — On-device voice interface infrastructure** (sub-500KB STT+TTS model layer)
- Secondary: supports L1 voice-driven agent runtimes as a drop-in component

## Status
- First signal; 200 HN points organic.
- No registry entry: model artifact, not agent/LLM/hardware schema match; `voice_footprint_kb` field does not exist in current schema.
- Schema watch: `voice_footprint_kb: int`; `wasm_compatible: true/false`; `voice_offline_capable: true/false`.
- Two-signal condition: needs a second deployable tool demonstrating sub-1MB on-device speech for tracking-threshold upgrade.
