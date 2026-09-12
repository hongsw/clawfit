# Research Watch: Google ARTEMIS — Android Natural Language Agent Automation

- Repo/Link: https://github.com/google/ARTEMIS
- Source: GeekNews front page (2026-09-12)

## Why this is worth watching
ARTEMIS is Google's official open-source tool for executing natural-language instructions on Android devices — "turn natural-language instructions into reliable Android automation." Built by the Pixel Test Engineering Fusion team and licensed Apache-2.0. It extends the browser-automation signal cluster (browser-use, camofox, coding-tools-mcp) to native mobile, making it the first Google-official mobile agent automation tool in this log.

## What stands out immediately
- Two execution modes: **Flash Profile** (reactive, ~3–5s/step) for routine tasks; **Pro Profile** (plan-and-verify, ~15–40s/step) for complex scenarios
- Multimodal targeting: accessibility hierarchy + OCR + visual model with element-index/coordinate/visual-detection fallback chain
- Installs a small accessibility service ("Artemis Accessibility Helper") on target Android device via ADB
- Dependencies: ADB, scrcpy, FFmpeg, Python `uv`; auto-detected at startup
- 2,500 stars, 223 forks; active Discord; Apache-2.0; Python 3.12+
- Supports real devices and emulators with USB debugging

## Why clawfit should care
Mobile UI is the surface area not covered by any currently tracked tool. Browser-use/camofox handle web; coding-tools-mcp handles file-system; ARTEMIS handles Android apps. A `surface: [web | desktop | mobile | filesystem | api]` axis would let clawfit surface ARTEMIS for QA professionals automating mobile regression tests. The Flash/Pro dual-mode is architecturally identical to the "efficient draft, frontier escalate" cascade pattern seen in HydraFusion (2026-09-04) — confirming that tiered execution speed is now a recognized design pattern across surface types.

## Preliminary interpretation
Current best reading:
- **Level 4 primary — Capability Layer** (Android automation MCP-compatible tool for agents)
- **Level 6 secondary — Human Interface / Surface** (acts on the native UI layer agents would otherwise be blind to)

## Status
- 2,500 stars — below 5k registry threshold; no per-call pricing model
- Not registry-eligible today; revisit at 5k stars or if Google adds MCP server interface
- Extends the tracked mobile/voice surface cluster (VoiceStudio 2026-08-31, hyperframes 2026-04-29)
