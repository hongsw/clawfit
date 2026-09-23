# Research Watch: NobodyWho — On-Device LLM Inference Engine for Mobile and Game Dev

- Repo: https://github.com/nobodywho-ooo/nobodywho (⭐~1,200)
- Source: GitHub search ("Jev in 25 Lines of Python" HN 513 pts → nobodywho.ai → nobodywho-ooo/nobodywho)

## Why this is worth watching
NobodyWho is a Rust-based inference engine that runs GGUF chat models locally on any device, shipping as a first-party package for Flutter, React Native, Swift, Kotlin, Python, and Godot. The delivery surface is unusual: game engines and cross-platform mobile frameworks are not addressed by any other L1 runtime tracked in the registry. The "Jev in 25 Lines of Python" blog post (HN 513 pts, today) used NobodyWho specifically to demonstrate local decision model inference without TypeSafe's hosted API — which positions NobodyWho not just as a mobile inference substrate but as a platform for the Jev-class typed decision model pattern that has accumulated six cross-date signals this month.

## What stands out immediately
- **Cross-platform packaging**: first tracked inference engine shipping native packages for Godot (game engine), Flutter, and React Native alongside Python — runtime reaches GPU-accelerated inference on phones and in games
- **Hardware auto-selection**: Metal (macOS), Vulkan (Linux/Windows), CPU fallback — no per-target configuration required
- **Capability completeness**: tool calling, speech-to-text, text-to-speech, and RAG in one engine — comparable to full-featured server-side inference stacks, running on-device
- **GGUF model compatibility**: runs any GGUF chat model, giving access to the entire llama.cpp model ecosystem without conversion
- **EUPL-1.2 license**: commercial use permitted; less permissive than Apache-2.0 but compatible with standard commercial build pipelines
- **Rust core**: consistent with the Rust-native inference trend (colibri 2026-07-21, CUDA Rust 2026-09-17) — Rust as language of on-device agent substrates is pattern-building
- **Jev demonstration context**: NobodyWho's own blog post showing Jev in 25 lines of Python gives an explicit signal that the team is tracking the typed decision model space; if agent-jev (malevrigns, Apache-2.0) runs on NobodyWho, the combination constitutes a fully local, zero-cloud-dependency decision agent substrate

## Why clawfit should care
The registry's `hardware` field currently spans `local`, `cloud`, and `edge` but has no sub-type for **mobile-native** or **game-engine-embedded** deployment. NobodyWho targets exactly those gaps. The current registry has no tool that runs natively inside a Flutter or React Native app or in a Godot scene. If on-device agent primitives (inference + decision model) reach phones through mainstream cross-platform frameworks, clawfit's `hardware: local` recommendations need to distinguish between desktop-local and mobile-local. NobodyWho is the first explicit supply to the mobile-local slot. Additionally, the Jev pattern (now six signals) is gaining an on-device implementation surface here — if the Jev pattern reaches canonical promotion, NobodyWho's role as its mobile deployment vehicle becomes a secondary registry criterion.

## Preliminary interpretation
- **Level 1 — Base Runtime (primary)**: runs GGUF models locally; complete inference substrate for mobile, desktop, and embedded
- **Level 7 — Infrastructure (secondary)**: edge/mobile-first hardware deployment extending agent reach outside server and local-desktop contexts

## Claims to verify
- Confirmed star count: ~1.2k estimated from issue references; need direct GitHub count to confirm registry threshold eligibility (5k needed for registry)
- Whether tool calling works correctly on all platforms (mobile GPU scheduling can introduce timing issues that break tool-call round trips)
- Whether STT and TTS run on-device or delegate to cloud APIs (the readme implies on-device but this should be confirmed for `network: offline` classification)
- Whether the Godot package supports GDScript or requires C# bindings (relevant to game-agent developer surface)
- Whether NobodyWho has been tested with the Jev decision model pattern specifically (the blog post demonstrates viability but not production readiness)

## Status
- **First signal for "mobile-native + game-engine LLM inference engine"** as a distinct delivery category
- ~1,200 stars — below registry threshold (5k); above monitoring threshold (1k)
- The Jev blog post (513 HN pts today) creates an organic integration signal: watch for combined NobodyWho + decision-model deployment tutorials
- Monitor: if star count crosses 5k or a game studio announces production use, write follow-up and evaluate registry entry under a `hardware: mobile` category
