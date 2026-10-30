# Research Watch: CopilotKit OpenBot — Self-Hosted AI Coworkers with Per-Bot Resource Isolation

- Repo: https://github.com/CopilotKit/OpenBot (⭐8,624)
- Source: GitHub Trending (all languages, daily, 2026-10-30)

## Why this is worth watching

OpenBot is CopilotKit's answer to AI coworker platforms: an open-source, self-hosted stack where each AI "coworker" (Bot) runs with its own isolated browser (Chromium container), its own file space, and only the tools explicitly granted. Every action the Bot proposes is checked by a gateway before execution and logged afterward. This is structurally different from multi-agent frameworks (CrewAI, AutoGen) that orchestrate agents around shared task state — OpenBot prioritizes human oversight of per-agent actions within a persistent coworker metaphor.

The AG-UI compatibility means any agent framework that implements the AG-UI protocol can be deployed as a coworker, independent of the underlying framework. This positions OpenBot as an **agent deployment surface** rather than an agent framework — a layer that hosts agents without prescribing how they are built.

## What stands out immediately

- **Per-Bot Chromium container**: each coworker gets a dedicated browser instance with its own login state; browsers cannot access each other's sessions; this is a hardware-isolated sandbox pattern rather than software-level sandboxing
- **Action gateway**: every Bot action is checked before execution and recorded afterward; the gateway is the human oversight point — not an optional review step but an architectural boundary in the stack
- **AG-UI compatibility**: any AG-UI endpoint (LangGraph, CrewAI, Google ADK, custom) can be deployed as a Bot; CopilotKit-specific implementation is not required
- **Human takeover for auth prompts**: when a Bot hits a login wall or 2FA, a human can take control of the browser session, complete authentication, and hand control back — practical workaround for the web-blocking trend noted 2026-10-20
- **Self-hosted by design**: architecture uses Bun, Docker, PostgreSQL+pgvector, and CopilotKit Intelligence; no mandatory cloud dependency beyond a model API key and CopilotKit Intelligence project
- **Durable threads and memory**: CopilotKit Intelligence provides session persistence and memory across coworker sessions; pgvector for semantic retrieval over Bot memory
- **Example jobs are operations-domain**: expense claim review, ticket triage, release note drafting — not software development tasks; this positions OpenBot as a general enterprise assistant platform, not a coding agent host
- **MIT license**: permissive; enables commercial deployment without AGPL-style disclosure requirements

## Why clawfit should care

CopilotKit has been tracked through multiple lenses: the AG-UI protocol (2026-06-06), CopilotKit Channels SDK (2026-08-06), and Caspian agent communication SDK (2026-08-24). OpenBot is a new product from the same organization but represents a different layer: it is an agent deployment host, not a protocol or SDK.

The per-Bot browser isolation pattern is the most architecturally significant feature for clawfit's taxonomy:
- It implements the `execution_sandbox` pattern at the per-coworker level, using dedicated Chromium containers as the sandbox boundary — the same capability Google ACE (2026-10-24) proposes at cloud infra scale but here implemented as a self-hosted Docker-based stack
- The action gateway pattern implements a per-action human approval step that is distinct from harness-level plan-approval (CLAUDE.md/Codex daemon) — it fires per tool call, not per session or task

Registry implication: OpenBot is not a direct candidate for agents.json (it is a deployment host, not an agent), but it is a signal that self-hosted coworker infrastructure with per-agent sandboxing and action gating is moving from cloud-only products to open-source stacks. The `governance_need: hard` recommendation path should distinguish between agents that run in sandboxed coworker hosts vs. bare harnesses.

Previous CopilotKit org signals tracked: AG-UI protocol (L4, 2026-06-06), Channels SDK (L6 bridge, 2026-08-06). OpenBot is L2 primary with L6 secondary — a different layer than previous CopilotKit signals.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness / Wrapper** (primary): agent deployment host that provides per-coworker resource isolation, action gating, and session memory as infrastructure for arbitrary AG-UI-compatible agents
- **Level 6 — Human Interface** (secondary): coworker dashboard interface for managing Bot assignments, monitoring actions, and handling human takeover flows

## Claims to verify

- Whether the per-Bot Chromium container is truly isolated (no shared kernel state, network namespace separation) or shares a host OS user namespace in the default Docker-Compose configuration — the level of isolation matters for `governance_need` scoring
- Whether the CopilotKit Intelligence dependency (for durable threads and memory) requires a paid CopilotKit account or can be self-hosted; this affects the "self-hosted" claim if a CopilotKit account is mandatory
- Whether the action gateway is synchronous (blocks until human approves) or asynchronous (queues and proceeds); synchronous gating has latency implications for high-frequency tool-calling tasks
- How the AG-UI compatibility is tested in practice — whether the advertised LangGraph, CrewAI, and Google ADK integrations are tested and maintained or aspirational
- Age of the repository (593 commits, MIT 2026 copyright; creation date not surfaced)

## Status

- Tracking: new signal, GitHub Trending (all languages) 2026-10-30
- Registry eligibility: not a candidate (agent deployment host, not an agent/LLM/hardware registry entry)
- Related CopilotKit signals: AG-UI protocol (2026-06-06), Channels SDK (2026-08-06), Caspian (2026-08-24)
