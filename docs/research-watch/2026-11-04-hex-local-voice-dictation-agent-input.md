# Research Watch: Hex — Local Voice Dictation with Agent Skills Layer

- Repo/Link: https://github.com/anomalyco/hex
- Source: GitHub Trending (4,567 ⭐, 410 today, 2026-11-04)

## Why this is worth watching

Hex is a cross-platform local voice dictation tool (Mac, Windows, Linux) that runs the speech model fully on-device and pastes transcribed text into any app. With 4,567 stars and 410 stars gained today, it's on a steep adoption curve. The repository includes an `AGENTS.md` file and a `skills/` directory, indicating the project is actively integrating with the agent ecosystem rather than remaining a standalone transcription utility.

## What stands out immediately

- **Full local transcription**: speech model runs on-device, nothing leaves the machine — zero cloud dependency and zero latency to external APIs
- **Cross-platform**: macOS (Apple silicon), Windows x64/ARM64, Linux x86_64/ARM64 — covers all major developer platforms
- **Multiple install paths**: Homebrew, AUR, Nix, .deb, .rpm, installer scripts — unusually broad Linux support suggests a developer-first focus
- **AGENTS.md + skills/ directory**: the project is building out agent skill integration; exact capabilities not yet documented publicly but the structure matches the L4b pattern
- **Hold-to-dictate UX**: voice input as a low-friction alternative to typing, relevant for developers who direct agents with natural language prompts

## Why clawfit should care

Voice input is an increasingly important agent interface layer, particularly for developers who want to direct agents hands-free or during code review. Hex sits at the intersection of the voice agent interface trend and the local-first execution preference. Its `AGENTS.md` and skills layer suggest it wants to become a voice front-end for coding agents (Claude Code, Codex, Cursor). If the skills layer matures, Hex could be classified as a Level 4b input surface tool that pairs with any L1–L2 coding agent. The local execution model aligns with `network: offline` and `data_sensitivity: confidential` profiles in clawfit.

## Preliminary interpretation

Current best reading:
- **Level 4b — Capability / skill layer**: voice dictation as an agent input surface; skills directory suggests intent to integrate as an agent capability

## Status

- 4,567 ⭐, strong growth trajectory
- AGENTS.md and skills/ directory exist but content not yet publicly documented
- Watch for: skills/ documentation; named integrations with Claude Code or Codex; registry entry once agent capabilities are confirmed
