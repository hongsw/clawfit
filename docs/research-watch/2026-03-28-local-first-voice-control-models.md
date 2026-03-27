# Research Watch: local-first voice control as a model split pattern

## Source
- LinkedIn post by Pau Labarta Bajo
- Source URL: <https://www.linkedin.com/posts/pau-labarta-bajo-4432074b_most-voice-assistants-send-your-audio-to-ugcPost-7443231277161504768-tRJQ>

## Why this is worth watching
This is an important voice-control signal because it highlights a strong alternative to cloud-first assistants:

> local-first voice control with a split model architecture.

The post specifically points to:
- **LFM2.5-Audio-1.5B** for speech recognition
- **LFM2-1.2B-Tool** for action dispatch
- both running locally on-device

This is important because it turns “voice assistant” into a more modular systems question.

## Why clawfit should care
clawfit has already been tracking voice as more than dictation:
- talk mode
- realtime interaction
- business voice workflows
- interface commercialization

This signal adds another key pattern:

> voice systems may increasingly split into separate local models for:
> 1. audio understanding
> 2. tool / action dispatch

That is a useful architecture pattern to watch.

## Key interpretation
This is not only a privacy story.
It is also a product architecture story.

The important emerging properties are:
- local-first operation
- no cloud dependency
- no API-key requirement
- lower privacy risk
- voice control as an on-device action layer
- modular separation between perception and action routing

## Why this matters strategically
If this pattern matures, there may be a distinct class of voice systems optimized for:
- in-car assistants
- edge devices
- privacy-sensitive workflows
- offline-capable controls
- embedded or always-on voice interfaces

This would connect strongly to:
- edge/runtime trends
- talk-mode commercialization
- local assistant deployment
- capability routing under hardware constraints

## Working classification
Current best reading:
- **research watch subject**
- voice-control architecture signal
- local-first / on-device interface pattern
- model-split design worth tracking

## Status
- Added as a research watch subject
- Useful for future Level 7 refinement around voice/runtime architectures
