# Research Watch: vstorm-co/agenticos — Self-Hosted Enterprise Agent Platform (Pydantic AI + pgvector + Audit)

- Repo: https://github.com/vstorm-co/agenticos (⭐353)
- Source: GitHub Trending Python

## Why this is worth watching
AgenticOS is a self-hosted platform for building and governing company-internal AI agents, with the design principle "code defines, configuration composes." Engineers write typed Python that registers capabilities, connectors, and MCP catalog entries; non-technical users then compose agents in a browser UI from those registered capabilities. The stack is FastAPI + Pydantic AI + PostgreSQL/pgvector + Redis + Next.js, deployed via Docker Compose. At 353 stars, it is above the 100-star threshold but early-stage. It is relevant because it represents a structurally different approach to company agent deployment than managed platforms (Sierra, Voiceflow) or coding harnesses (Claude Code, Codex): an internal governance layer purpose-built for teams that need control without cloud vendor lock-in.

## What stands out immediately
- "Code defines, configuration composes" separation: behavior changes require a PR; non-technical users configure agents without code access — this enforces a governance boundary at the boundary between code and config
- Pydantic AI as the agent runtime (not LangChain or CrewAI) — typed agents, mypy/pyright compatible throughout
- PostgreSQL with pgvector replaces a separate vector database — reduces operational complexity for small teams
- PostgreSQL-backed job queue for background work (no Celery/Redis queuing) — single stateful dependency for async
- Code execution runs in containers started by `sandboxd` — sandboxing is built-in, not an afterthought
- Audit trail, access controls, budget limits, and approvals are first-class features — not plugins
- Single runner serving web, API, and chat channel interfaces — avoids the multi-process deployment pattern common in harness stacks
- 353 stars with 1,534 commits — commit density suggests active development relative to star count

## Why clawfit should care
AgenticOS addresses the `governance_need: hard` profile in a self-hosted, non-vendor-locked way. Current registry entries in this profile (Sierra, Voiceflow, Dust) are managed cloud platforms. AgenticOS is the first tracked self-hosted option that pairs audit trails and budget controls with a typed Python SDK. The `statefulness: session` and `network: online` profile combined with `hardware: self-hosted` and `governance_need: hard` is currently underserved in recommendations. If AgenticOS matures (crosses 5k stars), it would be a registry-eligible entry for teams with data sovereignty requirements. The Pydantic AI dependency also creates an ecosystem affinity signal — Pydantic AI (tracked 2026-09-30) now has at least two downstream products building on it.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness/Wrapper Layer** (self-hosted enterprise agent harness with governance-first design)
- Secondary L5 (audit trail and observability are native, not bolt-on)

## Claims to verify
- Whether `sandboxd` is a custom component or a named open-source project (affects security audit scope)
- Actual MCP catalog support — README mentions it but the implementation maturity is unconfirmed
- Whether the "non-technical user browser composition" UI actually works for non-engineers or is developer-centric with a thin GUI
- Budget enforcement mechanism — whether it's a soft advisory limit or a hard execution block

## Status
- First scan: 2026-11-16
- Registry action: deferred — below 5k star threshold; no deterministic per-call cost data (self-hosted, model backend configurable)
- 📡 Note: First self-hosted L2 harness with governance-first design (audit + budget + approval built-in) in the tracked corpus; second Pydantic AI downstream signal (after a downstream mention in Oct 2026 scan); if a second self-hosted governance-first harness appears, that would constitute a two-signal confirmation for "enterprise-governance-native self-hosted harness" as a distinct L2 sub-type
