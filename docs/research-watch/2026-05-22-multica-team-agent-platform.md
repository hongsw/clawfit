# Research Watch: multica-ai/multica

- Repo: https://github.com/multica-ai/multica
- Also see: https://multica.ai/ · docs/research-watch/2026-05-21-andrej-karpathy-skills-behavioral-spec.md (same org)

## Why this is worth watching

At 30.7k stars (+534 in a single day, GitHub Trending #7 all languages), multica is the highest-starred open-source managed-agents platform in this taxonomy by a significant margin. It addresses a structural gap between L1 base runtimes (which execute tasks) and L3 behavioral specs (which govern how): there is no canonical open-source tool for coordinating multiple agents as persistent team members across a shared task board. Multica occupies that gap. The same org (multica-ai) also ships the `andrej-karpathy-skills` behavioral spec (tracked 2026-05-21 as L3), which suggests a deliberate platform + spec strategy.

## What stands out immediately

- Local daemon model: agents run on the operator's machine or a self-hosted VPS; the Multica server is coordination-only (issue routing, WebSocket streaming, activity feed) — user data never leaves the network
- Multi-runtime abstraction: supports 11 named agent CLIs (Claude Code, Codex, OpenCode, Hermes, Pi, Gemini, OpenClaw, GitHub Copilot CLI, Cursor Agent, Kimi, Kiro CLI) — vendor-neutral at the execution layer
- Squad routing: a leader agent delegates subtasks to team members; squad is a stable named group, not a one-shot orchestration
- Task state machine: enqueue → claim → start → complete/fail lifecycle with proactive blocker reporting from agents
- Skill library: solutions become reusable, org-scoped capabilities over time (persistence mechanism not documented in public docs — claim to inspect)
- Stack: Go backend (Chi + sqlc), Next.js frontend, PostgreSQL + pgvector, v0.3.1 released 2026-05-15, modified Apache 2.0 (SaaS hosting restrictions apply)
- No workflow definition format documented — task routing is pull-based (agents claim from queue), not declarative spec-driven

## Why clawfit should care

Multica is the first high-signal tool in this taxonomy that embeds project-management infrastructure directly into the agent orchestration layer. The multi-runtime abstraction (11 CLIs) means clawfit's recommendation output could feed directly into a Multica workspace — an agent a user selects via `clawfit recommend` would operate as a Multica team member without rebinding. The squad routing pattern is architecturally new: it is not a single-agent harness (L2) nor a governance spec (L3), but a persistent team topology with role assignment. The modified Apache 2.0 license carries a SaaS hosting restriction that is a hard blocker for managed-hosting profiles.

## Preliminary interpretation

Current best reading:

- **Level 2 — Meta wrappers / harnesses / orchestration layer** (primary): Multica wraps and dispatches to L1 agent runtimes, manages their lifecycle, and provides the coordination substrate. It does not define agent behavior, impose workflow governance, or maintain a spec document — it executes. The task queue, squad routing, and WebSocket streaming are harness-layer primitives, not governance-layer primitives.
- **Weak Level 3 adjacency** (not sufficient for secondary classification): The activity feed and skill library could be read as SSOT-adjacent, but there is no evidence of sprint contracts, behavioral specs, or lifecycle governance. The skill library persistence mechanism is undocumented — it is a claim, not a validated SSOT primitive. Without a workflow definition format or governance artifact, L3 secondary does not apply.
- The "project management + harness collapse" is a new sub-type within L2 — distinct from pure execution harnesses (deepagents, Anthropic sprint-contracts) and distinct from multi-agent research loops (TradingAgents). Closest prior art is Claude Code Routines (L2, serverless execution substrate) and DureClaw (L2, distributed agent orchestration), but neither adds a human-facing task board with agent profiles and squad delegation.

## Status

- 30.7k stars, v0.3.1 stable, modified Apache 2.0 (SaaS restriction flag)
- Exceeds 5k-star registry threshold; deferred per new L2 sub-type rule — "project-management + harness collapse" has no second independent signal yet
- Promotion threshold: a second independent tool combining agent task queue management with multi-runtime abstraction at ≥5k stars, OR independent validation of the skill library persistence claim
- License review required before registry entry: confirm whether modified Apache 2.0 SaaS restriction affects self-hosted enterprise profiles
- Watch: whether squad routing displaces one-shot orchestration as the dominant multi-agent coordination pattern
