# Research Watch: isair/jarvis — Local-First Desktop AI Assistant with MCP, Knowledge Graph, and Voice

- Repo: https://github.com/isair/jarvis (⭐2,312)
- Source: GitHub Trending Python

## Why this is worth watching
Jarvis is a local-first cross-platform desktop AI assistant (macOS, Windows, Linux) that integrates MCP tool servers, a local knowledge-graph memory diary, dictation, and optional on-device speech synthesis. It is designed to run entirely without a cloud AI service — Ollama or any OpenAI-compatible local server supplies the language model. At 2,312 stars it is above the signal threshold and represents a distinct pattern from managed desktop assistants: the sensitive information is redacted before it reaches model context or the diary, and no telemetry is sent. This positions it as the first tracked fully offline-capable personal AI assistant with native MCP connector support in the scan corpus.

## What stands out immediately
- Fully local by default: Ollama integration means LLM, STT, and TTS can all run on-device; cloud services are opt-in, not opt-out
- MCP connector configuration (`config.json` `mcps` section) lets users attach GitHub, browser automation, Home Assistant, database connectors — MCP extensibility without cloud dependency
- Local knowledge graph diary (not vector DB only): structured memory that persists across sessions with a Memory Viewer UI
- Sensitive information redaction before model context and diary storage — privacy-preserving by design, not by policy
- Dictation hotkey (hold-to-dictate, release-to-paste) — first tracked desktop assistant with agent-independent dictation integration
- Wake-name addressing: speaks the assistant's name and it joins the conversation from ambient listening
- Cross-platform (macOS/Windows/Linux) — unlike most local AI tools which are macOS-first
- 552 forks at 2,312 stars suggests active community extension or adaptation

## Why clawfit should care
The `network: offline` profile in clawfit scoring is currently underserved at L6 (human interface). Most tracked L6 tools require cloud connectivity (OpenAI Dots, Ando, Sierra) or have only partial offline capability. Jarvis fills the `network: offline` + `hardware: local` + `statefulness: persistent` combination at the personal assistant interface layer. The MCP extensibility also signals that the "MCP as local tool connector" pattern is reaching non-developer users — the README specifically advises reviewing permissions before enabling each MCP server, suggesting the user base includes people who may not fully understand tool access implications.

## Preliminary interpretation
Current best reading:
- **Level 6 — Human Interface Layer** (local-first personal AI assistant with native MCP)
- Secondary L5 (knowledge graph memory is a first-class feature, not a plugin)

## Claims to verify
- Whether the local knowledge graph is a custom implementation or built on an existing graph DB (affects extensibility and security review)
- Creation date — the repo shows "© 2026" but commit count (870) and fork density (552) suggest earlier origins; a pre-2025 repo would be outside the 6-month threshold for new signals
- Parity of features across macOS/Windows/Linux (cross-platform claims often degrade on Windows)
- Whether sensitive information redaction is rule-based or model-based (rule-based has known gaps; model-based adds inference overhead)

## Status
- First scan: 2026-11-16
- Registry action: deferred — L6 personal assistants do not map cleanly to current registry schema (agents.json, llms.json, hardware.json); no cost/latency profile applicable
- 📡 Note: First tracked fully offline-capable personal AI assistant with native MCP in the corpus; if a second tool appears with the same local+MCP+persistent-memory combination at L6, that would confirm "offline-capable MCP-extensible personal assistant" as a named L6 sub-type; second-signal watch candidates: nobodywho (Sep-30, mobile-first inference with built-in tools), Earendil Pi (recurring tracker — desktop/mobile unified agent runtime)
