# Research Watch: OpenExecutive — Multi-Agent AI Executive Team

- Repo: https://github.com/SenteLabsAI/OpenExecutive (⭐3,000)
- Source: GeekNews ("CEO가 AI를 위해 개발팀을 해고하자, 개발자들은 오픈소스 AI CEO를 만들었다")

## Why this is worth watching

OpenExecutive was built by engineers who were laid off after their company replaced the development team with AI tools. Their response was to build an open-source AI that replaces executive functions instead — the cultural framing explains the project's stated design philosophy. It is a multi-agent system of eight specialist agents (Strategy, Finance, HR, Legal, Operations, Marketing, Product, Board Communications) routed through an orchestrator that maintains "a single coherent executive voice." The GeekNews post received 27 points, a meaningful signal of engagement in a community that trends toward infrastructure and developer tooling.

What makes it technically interesting is not the business metaphor but the architectural choices: dual-layer RAG (built-in MBA-level knowledge base plus user-uploaded company documents), SQLite-backed episodic memory that extracts and recalls past decisions across sessions, and Claude-tier model selection per task (Haiku for memory extraction, Sonnet for primary responses, Opus for strategic reasoning). The multi-channel interface (Web UI, Slack, Email, Telegram, Discord, Google Chat, CLI) reflects a design assumption that executive advice flows through many surfaces.

## What stands out immediately

- **Role-specialized agent routing**: eight agents with distinct knowledge domains; the orchestrator merges outputs rather than exposing raw specialist responses — prevents the "committee of contradictions" failure mode
- **Dual-layer RAG**: static MBA knowledge base (embedded at startup) plus ChromaDB for uploaded company documents; 85% cache hit rate cited for static content separation
- **Cross-session episodic memory**: SQLite stores decision summaries extracted by Claude Haiku; the memory layer recalls relevant prior decisions at query time, not just within a session
- **Model tiering by task**: Claude Haiku 4.5 for memory extraction (cost optimization), Claude Sonnet 4.6 as primary, Claude Opus for strategic reasoning — explicit cost-quality routing at the application layer
- **Multi-channel delivery**: Web UI + Slack + Email + Telegram + Discord + Google Chat + CLI — this is not a chatbot, it is meant to integrate into existing executive communication flows
- **Apache 2.0 license, Fly.io deployment target**: commercially permissive with a batteries-included deployment path; not only a research demo
- **Origin story matters**: built by laid-off developers as a deliberate provocation — the project has activist intent that could drive adoption in communities skeptical of AI-driven workforce displacement

## Why clawfit should care

OpenExecutive is a high-complexity L3 multi-agent system occupying a domain (business advisory) that clawfit's current registry does not cover. It is worth watching because:

1. **L3 occupancy pattern**: the orchestrator-plus-specialists architecture with a unified output voice is a recurring pattern (seen in OpenMAIC, tracked 2026-08-30). Two examples in a short period do not trigger the two-signal taxonomy rule alone, but the pattern is building.
2. **Model selection as application logic**: the tiering of Haiku/Sonnet/Opus within a single application is a design pattern that affects clawfit's `budget` and `latency` dimensions — a system that self-selects model tier per query cannot be classified by a single cost/latency profile.
3. **Statefulness profile**: the cross-session SQLite memory combined with single-session ChromaDB retrieval places this in a hybrid statefulness zone — `stateful: persistent` in the episodic layer, `stateful: session` in the retrieval layer. The registry currently has a single `statefulness` field; this case argues for more granularity.

## Preliminary interpretation

Current best reading:
- **Level 3 — Team / SSOT / Multi-Agent Orchestrator** (primary): eight specialist agents coordinated by an orchestrator with a defined task decomposition model — classic L3 structure
- **Level 5 — Memory / Observability** (secondary): the episodic memory layer is substantive enough to count as a secondary classification; it's not just a session store, it drives recall across executions
- **Level 6 — Human Interface** (tertiary): multi-channel delivery is a first-class design concern, not an afterthought

## Claims to verify

- Whether the 85% cache hit rate figure was measured in production or in a controlled demo environment with static query patterns
- Whether the eight-agent routing is actually specialized or whether all agents are the same base prompt with a role header — the distinction matters for whether "specialist agent" is an architectural claim or a UX one
- Whether Claude Opus usage on strategic decisions is practical at scale (Opus per-query cost is non-trivial; "CEO-level advice" workloads may have unpredictable volume)
- Whether the Fly.io deployment path handles the ChromaDB persistent volume correctly at startup — embedded vector stores and serverless deployment are often incompatible
- The activist origin story is compelling, but it does not guarantee technical soundness; independent review of the routing logic and memory quality is needed

## Status

- Tracking: first signal 2026-08-30
- Stars: 3,000 GitHub (2026-08-30); source: GeekNews (27 points)
- Registry decision: hold. OpenExecutive is a multi-agent application, not an agent or LLM primitive. Its cost profile is a composite of three Claude models with variable per-query routing — no single cost/latency can be assigned. Registry entry is not meaningful until clawfit has an `agent_system` or `application` schema type.
- Watch: whether the activist origin drives sustained community adoption or fades; whether the episodic memory + role routing pattern appears in other projects (would trigger pattern promotion); whether Fly.io deployment proves stable for ChromaDB-backed workloads
