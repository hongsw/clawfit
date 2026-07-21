# Research Watch: Omnigent — Meta-Harness for Multi-Agent Orchestration

- Repo: https://github.com/omnigent-ai/omnigent (⭐7,576)
- Source: GitHub Search API — new Python repos (created 2026-06-11, 40 days old), v0.6.0 released 2026-07-21

## Why this is worth watching

Omnigent frames itself as a "meta-harness" — a layer above agent harnesses that orchestrates Claude Code, Codex, Cursor, OpenCode, Hermes, and Pi through a unified interface. At 7,576 stars after 40 days (still alpha), it is the most-starred new meta-orchestration framework in the current scan cycle. The positioning is conceptually similar to what Omnigent calls "meta-harness engineering" visible in `loop-engineering` (tracked 2026-07-05): the premise that the unit of work is not "which agent to use" but "which combination of agents, in what topology, with what governance." The difference from loop-engineering is implementation depth: Omnigent ships a working orchestrator with YAML agent definitions, cross-device session sync, and cloud sandbox deployment — not just a methodology.

## What stands out immediately

- **Multi-agent topology in YAML**: agents are declared via YAML files specifying prompts, tools, and sub-agents. The `harness:` field accepts `claude-sdk`, `codex`, `cursor`, etc., making agent runtimes interchangeable without rewriting the agent definition
- **Supervisor pattern native**: one agent reviews another's output before acceptance — the review loop is a first-class concept in the YAML schema, not a post-hoc script
- **Cross-device session continuity**: sessions follow the user across terminal, browser, and mobile — messages, sub-agents, terminals, and files stay in sync. This is an L6 feature (human interface persistence) surfacing inside an L2 meta-harness
- **Cloud sandbox delegation**: agents can delegate to Modal, Daytona, E2B, Kubernetes, or Databricks without requiring the user's machine to remain online. The local session is a control plane; compute runs elsewhere
- **Governance layer**: shell command approval policies, per-agent spend caps, tool access restrictions — enforced at the meta-harness level, not inside individual agent processes. Server-wide, agent-level, and session-specific policy scopes
- **Apache 2.0, Python + TypeScript**: Python for the orchestration core; TypeScript for the browser/mobile interface. Multi-language runtime surface is a maintenance risk signal for an alpha project
- **v0.6.0 on day 40**: 6 minor releases in 40 days suggests active iteration; also signals API instability. YAML schema breaking changes are a known risk for early-stage declarative orchestrators

## Why clawfit should care

Omnigent directly addresses the multi-agent coordination gap in clawfit's current recommendation logic. Clawfit recommends `(agent, llm, hardware)` triples for single-agent tasks. Omnigent's user profile is explicitly: "I have three tasks that benefit from Claude Code's context depth, Codex's cost efficiency, and Cursor's IDE integration — I want to run them in a topology where a supervisor verifies output before surfacing results." This is a qualitatively different recommendation need.

The governance-at-meta-harness pattern is particularly significant: spend caps and command approval implemented at the orchestration layer, not inside each agent harness, is a security and cost-control pattern that enterprises require. It separates Omnigent from peer projects like open-swe (which implements governance inside a single LangGraph harness).

Schema implication: `orchestration_model: [single-agent | multi-agent | meta-harness]`; `agent_runtimes: [claude-code | codex | cursor | custom]` as a multi-value field in the registry.

Two-signal check for "meta-harness" pattern: `cobusgreyling/loop-engineering` (tracked 2026-07-05, methodology + CLI tools, 8,939 stars) + Omnigent (working orchestrator, 7,576 stars) are two independent approaches to the same problem: orchestrating multiple AI coding agent runtimes in a unified control layer. Pattern confirmed: **"meta-harness for multi-agent coding agent orchestration."** "When in doubt" rule applies — both are pre-1.0/alpha; no canonical section change this run.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/Wrapper** (primary: orchestrates multiple agent runtimes under a unified session model)
- **Level 3 — Team/SSOT Generator** (secondary: YAML agent definitions function as a team-level SSOT for multi-agent policies)

Not L1: Omnigent does not run inference directly; it delegates to underlying runtimes. Not L5: observability features exist (session sync, audit) but are secondary to the orchestration primary.

Closest comparables: open-swe (L2 async SWE agent, single LangGraph harness), loop-engineering (methodology for multi-agent loop design, no runtime), AOS-CE (OS-level substrate, different abstraction level). Omnigent is the first working runtime-switching meta-harness in the scan corpus.

## Claims to verify

- **"Cursor integration"**: Cursor does not expose a public programmatic API; integration may depend on scripting the Cursor desktop app or an unofficial interface. The claim needs technical verification — if Cursor integration is simulated rather than native, it may break on Cursor updates.
- **"Cross-device session sync"**: architecture of the sync layer (cloud-hosted relay vs. P2P vs. local server) is not described in public documentation. Data residency implications for enterprise users are unspecified.
- **7,576 stars in 40 days**: impressive rate; Omnigent's meta-harness positioning likely attracted attention from developers frustrated by tool fragmentation. Verify organic vs. directed growth.
- **Governance policies at v0.6.0 alpha**: shell command approval and spend caps at alpha stage are typically implemented as best-effort, not enforced. Real enforcement requirements would need code inspection.

## Status

- No registry entry: alpha (v0.6.0, 40 days); schema has no multi-agent orchestration category; no deterministic cost/latency data for the meta-harness layer.
- Schema gap: `orchestration_model: [single-agent | multi-agent | meta-harness]`; `session_persistence: [none | local | cloud-synced]`; `agent_runtimes: list[str]`.
- Two-signal condition: loop-engineering (methodology) + Omnigent (runtime) confirm the "meta-harness for multi-agent coding orchestration" pattern. Deferred from canonical section: both pre-1.0; "when in doubt" rule applied. Re-evaluate when either reaches 1.0 or a third implementation appears.
- Registry candidate when: (a) API stabilizes at 1.0, (b) deterministic latency data is available for the orchestration overhead (not just the underlying runtimes), (c) Cursor integration is independently verified.
