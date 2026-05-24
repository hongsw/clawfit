# Research Watch: OpenHuman — Personal AI Super Intelligence

- Repo/Link: https://github.com/tinyhumansai/openhuman
- Source: GitHub Trending ALL languages #1
- Stars: ~21k (3,973 stars today at capture)

## Why this is worth watching

OpenHuman reached #1 on GitHub Trending All Languages with nearly 4k stars in a single day, a trajectory that puts it in the same velocity class as Warp's open-source announcement (the prior clawfit all-language high). The architectural thesis — a local-first Memory Tree that auto-ingests from 118+ OAuth integrations every 20 minutes, compressed into SQLite and surfaced as a desktop-native Tauri + Rust application — is a distinct posture compared to every tracked L1 agent: it treats *personal context continuity* as the primary product, and the LLM as a consumer of that context rather than the centrepiece. The GPL-3.0 license and early-beta status make it a watch item rather than an immediate registry candidate.

## What stands out immediately

- **Rust + Tauri (64.6% Rust, 31.2% TypeScript), GPL-3.0, ~21k stars, early Beta.** Tauri provenance distinguishes it from Electron-based desktop agents; binary is smaller and the threat surface for local data handling is narrower.
- **Memory Tree — local SQLite, Obsidian-compatible vault.** Compressed document chunks pulled from connected apps on a 20-minute auto-fetch cycle. Raw data stays on-device; only prompt-included context exits to cloud. This is an L5-adjacent memory primitive embedded directly in an L6 desktop shell — not exposed via MCP, not a standalone server.
- **118+ OAuth integrations via one-click consent.** Gmail, Notion, GitHub, Slack, Stripe, Calendar, and more. Claim to inspect: whether actual data ingestion breadth matches the integration count, and whether OAuth token handling is auditable for `data_sensitivity: confidential` profiles.
- **TokenJuice compression layer.** Vendor claims up to 80% token reduction. Mechanism and independent replication not yet available; treat as claim-to-inspect.
- **Built-in model routing** across reasoning / fast / vision LLM tiers, plus optional local inference via Ollama.
- **Desktop mascot with voice (STT/TTS) and Google Meet participation.** The voice and video meeting surface is the most distinctly L6 element — no other tracked agent has first-party meeting-participation as a feature.
- **GPL-3.0.** Copyleft on the client binary creates friction for `governance_need: hard` enterprise profiles. Same concern flagged for Warp (AGPLv3).

## Why clawfit should care

The embedded Memory Tree collapses L5 memory tooling and L6 desktop interface into a single product — the same multi-layer collapse pattern seen in Warp (L1+L2+L6) and opencode (L1 with proto-L4 model curation). clawfit currently scores memory as a separate capability axis; OpenHuman makes memory inseparable from the agent surface. If this pattern repeats, a `memory_integrated: true` flag on L6 entries may be needed to distinguish agents that bundle context management from those that delegate it to standalone L5 tools.

The 20-minute auto-fetch loop and Obsidian vault design also surface a new `statefulness` sub-dimension: not session-level persistence (what opencode offers via its server process) but *ambient background ingestion* — context is built continuously without user-initiated action. Current clawfit `statefulness` values (`stateless`, `session`, `persistent`) do not express this pattern.

## Preliminary interpretation

Current best reading:
- **Level 6 — Human interface / voice / multimodal layer** (primary — desktop-native ADE with mascot, voice I/O, and meeting participation; the interaction surface is the differentiator)
- **Level 5 — Memory / MCP / context layer** (secondary — embedded Memory Tree with local SQLite and auto-ingestion is a first-class L5 primitive, not an afterthought; operationally closer to cognee or claude-mem than to a session buffer)

Not Level 1: OpenHuman does not expose a general-purpose coding agent runtime or tool-use orchestration loop. The LLM is a consumer of context, not the primary execution surface.

## Status

- 21k stars exceeds the 5k registry threshold on raw count, but early-beta status, GPL-3.0 copyleft, and unverified TokenJuice and integration-breadth claims all argue for a hold. No registry entry today. Revisit at v1.0 stable or when an independent benchmark confirms the 80% token reduction claim. The `ambient background ingestion` statefulness pattern is a candidate new value for the `statefulness` axis — flag for schema review at the next calibration cycle (2026-06).
