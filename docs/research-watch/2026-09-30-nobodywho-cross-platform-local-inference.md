# Research Watch: NobodyWho — Cross-Platform On-Device AI Inference Engine

- Repo/Link: https://github.com/nobodywho-ooo/nobodywho
- Source: GeekNews front page (2026-09-30)
- Stars: ~1,500

## Why this is worth watching

NobodyWho is an on-device LLM inference engine with first-class support for Android (Kotlin), iOS/macOS/visionOS/watchOS (Swift), Flutter, React Native/Expo, and Godot — platforms almost entirely absent from today's inference runtime landscape (dominated by Python-first tools like Ollama, llama.cpp, vLLM). Its built-in TTS/STT and voice activity detection make it directly relevant to the local voice agent stack, complementing the VoiceStudio and realtime-voice-agents signals already tracked.

## What stands out immediately

- **Mobile-first multi-platform**: Android, iOS, Flutter, React Native, Godot — not just Python/CLI
- **GGUF inference + structured tool calling**: automatic grammar generation means models can call tools without server-side orchestration
- **Built-in voice stack**: TTS + STT + VAD in one package — no separate toolchain needed
- **OpenAI-compatible local server**: drop-in replacement mode for existing API clients
- **EUPL-1.2 license**: requires open-sourcing modifications; unusual for inference tooling
- **Zero API keys**: true offline operation, model downloads from HuggingFace directly
- **Godot support**: first signal for AI inference integration inside a game engine runtime

## Why clawfit should care

The hardware and network filters in clawfit (`offline`, `edge`) currently map primarily to desktop/server runtime substrates (Ollama, llama.cpp, MLX). NobodyWho extends "local execution" to mobile and game-engine contexts — environments where clawfit has no current registry coverage. A future `platform` axis (mobile, desktop, server, embedded, game-engine) would make this tool classifiable; today it sits in a gap. The Godot integration is a first signal for "AI agent in real-time simulation" as a distinct deployment context.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Runtime / Inference Substrate** (primary): on-device GGUF inference across mobile + desktop + game engine platforms
- **Level 4 — Capability Layer** (secondary): structured tool calling + multimodal input (image, audio) available to any model running on it

## Status
- 📡 Tracking: first signal for **mobile-first cross-platform inference engine** sub-type
- No prior clawfit registry entry
- Below single-signal promotion threshold for canonical L1 sub-type; watching for second mobile inference engine signal
