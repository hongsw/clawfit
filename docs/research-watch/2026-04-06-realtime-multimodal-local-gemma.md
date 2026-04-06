# Research Watch: Real-Time Audio/Video-In Voice-Out Agent on M3 Pro (Gemma E2B)

- Repo/Link: https://github.com/fikrikarim/realtime-gemma (via Hacker News Show HN)
- Source: Hacker News (151 pts, 13 comments)

## Why this is worth watching
A Show HN demo of real-time multimodal AI — audio/video input, voice output — running fully locally on an Apple M3 Pro using Google's Gemma E2B (2B parameter efficient model). This is a working proof that the voice agent stack (Level 7 human interface) can now run offline on consumer hardware, not just in the cloud.

## What stands out immediately
- Real-time loop: camera + mic → LLM → TTS, all local, no API calls
- Runs on M3 Pro (not a server) — consumer hardware threshold crossed
- Uses Gemma E2B (2B params) — small enough for edge but capable enough to reason
- Directly parallels what Google AI Edge Gallery is doing on mobile, but for macOS desktop
- HN traction (151 pts) confirms developer interest in offline multimodal agents

## Why clawfit should care
Clawfit's voice agent dimension (Level 7) has been cloud-dominated. This demo collapses the cloud vs. local distinction for voice/multimodal: a developer on M3 hardware can now run a real-time audio+video agent without any cloud dependency. This should affect how clawfit scores `network=offline` profiles when `hardware=apple_silicon` — offline multimodal is now viable.

## Preliminary interpretation
Current best reading:
- **Level 7 — Human interface / computer use** (real-time multimodal, offline)

## Status
- New; added to research-watch 2026-04-06. Signals that Level 7 offline capability has crossed the consumer hardware threshold.
