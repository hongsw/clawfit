# Research Watch: Ghost Pepper — Local Hold-to-Talk STT for macOS

- Repo/Link: https://github.com/matthartman/ghost-pepper
- Source: Hacker News

## Why this is worth watching
Ghost Pepper provides a hold-to-talk speech-to-text input layer for macOS that runs fully locally — no cloud dependency, no audio leaves the device. This positions it as a privacy-first alternative to Superwhisper for developers who need voice input with confidential codebases. The HN front page placement signals practitioner interest in offline voice workflows, especially as local LLM and STT quality converges with cloud quality.

## What stands out immediately
- Hold-to-talk model reduces accidental transcription — more precise than always-on voice
- Fully local: Whisper-based inference, no network call
- macOS-native, lightweight — low friction to add to any development workflow
- Directly complementary to coding agents: voice-to-terminal rather than voice-to-cloud
- Distinct from Superwhisper (commercial, cloud optional) and claude-code-voice (Claude-specific wrapper)

## Why clawfit should care
This is a Level 7 (human interface / voice / input layer) tool that is meaningfully different from Superwhisper in one dimension: `network: offline`. For the `offline_mid_codegen` and any `data_sensitivity: confidential` profile, a local voice input layer matters. Clawfit's current Level 7 voice tools (Superwhisper, claude-code-voice) are both `network: online`. Ghost Pepper fills the offline voice input slot.

## Preliminary interpretation
Current best reading:
- **Level 7 — Human interface / voice / input-output layer (offline STT, macOS)**

## Status
- Tracking: new entry, medium signal. Front page HN. Niche but fills a gap in the offline voice tooling map.
