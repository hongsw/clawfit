# Research Watch: PicoMQ — S3-Based Real-Time Data Stream for Agent Conversations

- Repo/Link: https://news.hada.io/ (GeekNews, 2026-10-05)
- Source: GeekNews

## Why this is worth watching
PicoMQ is a stream server that stores and delivers chat messages, device events, tasks, and agent conversations using S3 as its durable backing store. It targets the specific challenge of durable, replayable agent conversation streams — a gap between ephemeral in-process agent memory (lost on restart) and full database storage (high operational overhead). S3-backed stream semantics provide a middle path: cheap durable storage with real-time delivery.

## What stands out immediately
- S3 as primary storage: low operational cost, high durability, cloud-native
- Explicit agent conversation delivery as a named use case
- Real-time stream semantics: subscribe to live events, not just batch replay
- Covers: chat, device events, tasks, and agent conversations in one system
- Positions as infrastructure below the harness layer (no agent logic included)

## Why clawfit should care
Agent state management is a recurring theme in the ecosystem: clawfit already tracks OpenMemory, GBrain, claude-mem, and Supermemory. PicoMQ is structurally different — it is a **conversation stream transport**, not a memory retrieval system. It enables audit trails, replay, and multi-consumer access to agent conversation history at infrastructure cost. This may become relevant to `statefulness` scoring: agents operating in `session` statefulness mode could use PicoMQ as the durable backing layer, enabling resumability without dedicated memory infra.

## Preliminary interpretation
Current best reading:
- **L7 — Infrastructure / Substrate layer** (primary: durable stream transport for agent conversations)
- **L4 — Capability layer** (secondary: provides agent-readable state access surface)

## Status
- First signal for "S3-backed real-time stream server purpose-built for agent conversation delivery"
- No GitHub repo confirmed; GeekNews 8 points; monitoring for open-source release
- Pattern adjacent to: earendil Pi Durable (L2 durable execution) and SnapState (L2 persistent workflow state) — but distinct as infrastructure-layer transport vs. harness-layer persistence
