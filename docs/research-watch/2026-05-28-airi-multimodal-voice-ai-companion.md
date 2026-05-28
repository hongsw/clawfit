# Research Watch: airi — Open-Source Multimodal Voice AI Companion / VTuber Runtime

- Repo: https://github.com/moeru-ai/airi
- Also see: https://github.com/moeru-ai/airi (Neuro-sama, the proprietary VTuber this competes with, is not open-source)

## Why this is worth watching
airi combines real-time voice chat, game-playing autonomy (Minecraft, Factorio), live 3D avatar rendering, and a multi-LLM backend in a single open-source TypeScript project. It sits at the intersection of three active taxonomy signals: real-time voice agents, autonomous game-playing, and cross-platform human-AI interface. With ~40,200 total stars and consistent trending presence it has crossed the threshold where dismissing it as a novelty demo is no longer defensible.

## What stands out immediately
- Real-time voice pipeline: browser-based STT (WebSpeech / WebAssembly) + TTS (ElevenLabs integration confirmed in docs); not a push-to-talk tool — designed for continuous conversational exchange
- Autonomous game-playing: Minecraft and Factorio are explicitly listed as supported environments; agents parse game state and issue actions, making this a behavioral agent runtime embedded in a consumer entertainment surface
- Avatar layer: VRM and Live2D character model support with expression and animation control — the rendering and emotional-state display are first-class features, not cosmetic overlays
- Memory system: embedded database for persistent cross-session memory; architecture type (vector / key-value / other) is claimed but full implementation depth unverified from public docs
- Multi-LLM backend: OpenAI, Claude, DeepSeek listed; routing depth and fallback logic are undocumented beyond what provider list implies
- Deployment breadth: web app, macOS, Windows desktop, mobile PWA — claimed, cross-platform architecture enabled by TypeScript/Vue.js + WebGPU/WebAssembly
- Social chat integrations: Discord and Telegram; the agent joins channels and participates in conversations — this is an agentic messaging surface, not a simple chatbot connector
- WebGPU/WebAssembly use implies partial on-device inference is architecturally possible, though the primary inference path is API-based (multi-LLM backends)
- Codebase is TypeScript-primary with Vue.js frontend; no Python dependency chain — unusual for an agent framework of this scope

## Why clawfit should care
airi is the most architecturally ambitious open-source entry in the voice/multimodal human-interface layer (Level 6) currently tracked. The Level 6 entries in this taxonomy — Ghost Pepper (offline STT), Superwhisper (dictation), omi (ambient passive monitoring) — are all single-modality or single-direction tools. airi integrates bidirectional voice, visual avatar output, persistent memory, and autonomous environmental action (game-playing) into one runtime. That combination positions it as the first L6 entry that also bleeds into L1 (the game-playing agents are a base runtime behavior, not just an interface) and L5 (the memory system is a structural component, not an add-on).

For clawfit's recommendation engine, the primary relevance is: if a `task: companionship` or `task: interactive-agent` persona type is ever added, airi is the immediate anchor. More immediately, airi's multi-LLM backend architecture and real-time voice latency requirements are a direct test of whether clawfit's latency filter (`low`, `medium`, `high`) is granular enough for voice-interactive workloads — sub-second voice turn-taking is categorically different from the `latency: low` clawfit applies to coding agents.

The game-playing capability (Minecraft, Factorio) is the most unusual dimension. These are not toy grid environments — they are open-ended, long-horizon planning contexts. This aligns with the `statefulness: session` and `statefulness: persistent` axis in clawfit's filter layer, but at a level of environmental complexity that the current registry does not represent.

## Preliminary interpretation
Current best reading:
- **Level 6 — Human interface / voice / multimodal layer** (primary)

The bidirectional real-time voice pipeline and avatar rendering are unambiguously L6. The consumer entertainment framing (VTuber, companion) does not reduce the architectural significance — it is the deployment context, not the layer.

Secondary classifications worth flagging:
- **Level 1 secondary** — the Minecraft/Factorio game-playing agents are autonomous base-runtime behaviors embedded in the same project; this is a Level 1 pattern executing inside a Level 6 shell
- **Level 5 secondary** — embedded database memory with cross-session persistence is a structural L5 component; implementation depth unverified

Notable: airi is not a Level 2 harness (it does not orchestrate other agents) and not a Level 4 plugin (it is a self-contained runtime). The closest analog in the current taxonomy is omi (BasedHardware, L6 passive ambient input) but airi inverts the passivity assumption — it speaks, renders, acts, and plays games rather than monitoring quietly.

Sub-type candidate: "active multimodal companion runtime" — distinct from passive ambient monitoring (omi), push-to-talk STT (Ghost Pepper), dictation (Superwhisper), and realtime business voice agents (tracked in `2026-03-28-realtime-voice-agents-signal.md`). Single signal; sub-type naming deferred per single-sample rule.

## Status
- Held: not a current registry candidate — no `task: companionship` or `task: interactive-agent` type exists in the clawfit schema; game-playing environments are outside the current org persona scope
- Map mutation deferred: single signal for "active multimodal companion runtime" L6 sub-type; promotion criterion is a second open-source project combining bidirectional voice + avatar rendering + autonomous environment interaction at ≥10k★
- Flag for schema-analyst: the real-time voice latency requirement (sub-second turn-taking) exposes a gap in clawfit's current `latency` filter — `low` / `medium` / `high` do not distinguish interactive voice latency from code-completion latency; worth a companion-axis note if a second voice-interactive agent runtime surfaces at this signal level
- Watch: if airi adds a developer-workflow integration (MCP connector, Claude Code plugin, SDK) that enables the voice pipeline outside the companion context, the classification should be revisited — a voice/multimodal SDK wrapper would shift the primary classification toward L2
