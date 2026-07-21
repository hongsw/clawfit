# Research Watch: MiMo Code — Xiaomi Terminal Coding Agent

- Repo: https://github.com/XiaomiMiMo/MiMo-Code (⭐12,297)
- Source: GitHub Search API — new repos (created 2026-06-10, 41 days old), topics: [ai, ai-agents, cli, mimo, mimo-code], v0.1.7 released 2026-07-20

## Why this is worth watching

MiMo Code is Xiaomi's terminal-based AI coding agent, forked from OpenCode and extended with a persistent memory system, subagent orchestration, and deterministic workflows. At 12,297 stars after 41 days, it is the highest-star new Chinese-origin coding agent framework in the current scan cycle. Its positioning is architecturally interesting: rather than a blank CLI-wrapper (the generic OpenAI-compatible terminal agent pattern), MiMo Code ships with specific agents (build, plan, compose), a multi-LLM provider abstraction, persistent cross-session memory (SQLite FTS5), and a built-in skills system with 30+ named instruction sets. The "where models and agents co-evolve" tagline refers to the self-modification capability: the compose agent can write and register new skills into the running system.

## What stands out immediately

- **Three-agent architecture**: `build` (full read/write permissions), `plan` (read-only inspection), `compose` (orchestration + workflow invocation). Permission scope is enforced by role, not configured per-session — reduces the "agent with root access" problem to a role-selection decision
- **Persistent cross-session memory**: project knowledge stored in `MEMORY.md` with automatic checkpoint management and SQLite FTS5 full-text search index. Unlike session-scoped context (e.g., AGENTS.md, CLAUDE.md), MEMORY.md accumulates observations across task boundaries
- **Deterministic JavaScript workflows**: declarative scripts for compose, deep-research, fact-check, and research-experiment phases. Distinct from natural-language agent chaining: the workflow order is fixed code, not model-driven — trading flexibility for reproducibility
- **Skills system (30+ built-in)**: named instruction sets for arxiv, pdf-official, data-analytics, and others. Skills are composable: the compose agent can invoke multiple skills in a single workflow. Self-modification: new skills can be defined and registered at runtime
- **Voice input**: TenVAD + MiMo ASR for real-time streaming voice commands. Chinese ASR quality claimed to be superior to general Whisper variants — relevant to the Chinese-developer primary audience
- **Multi-provider LLM support**: OpenAI-compatible APIs as the abstraction; any provider that implements the API is supported. No hard dependency on a single vendor
- **Context reconstruction**: automatic detection of approaching token limits with context reconstruction to preserve active task state — a common pain point in long-running coding sessions

## Why clawfit should care

MiMo Code extends the competitive map of terminal coding agents. Before this scan cycle, the field was dominated by Claude Code, Codex CLI, Cursor (IDE), and OpenCode. MiMo Code introduces:

1. **A role-based permission model** (`build`/`plan`/`compose`) that is more granular than the binary `safe-mode`/`full-mode` pattern in most tools. The `plan` (read-only) role maps directly to clawfit's `task: qa` profile where read-access sufficiency is desirable.
2. **Persistent memory as a first-class feature** without an external memory service (mem0, GBrain): SQLite-backed, repo-local, no cloud dependency. This is the `network: offline` × `statefulness: session` × `budget: $0.00` memory path.
3. **Deterministic workflows as reproducibility primitives**: the fixed-order compose/research/fact-check scripts are closer to a task automation framework than an interactive agent. Relevant for `statefulness: stateful` + `task: research` profiles.

Schema implication: `agent_roles: [single | build-plan-compose | specialist-ensemble]`; `memory_backend: [none | in-context | sqlite-local | cloud-vector]`.

Second-signal check for "persistent local memory in coding agents": open-knowledge (inkeep/open-knowledge, 3,055 stars, 2026-06-03, AI-native markdown IDE + LLM wiki) represents a different architectural approach to the same problem (persistent knowledge across sessions). These are two implementations: MiMo Code's MEMORY.md + SQLite FTS5 (agent-native, code-adjacent) vs. open-knowledge's Markdown IDE (human-authored, knowledge-base-adjacent). Pattern emerging: "persistent local memory for coding agents without cloud dependency." Single engineering implementation (SQLite) across two tools is not yet a confirmed pattern — needs a third signal.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/Wrapper** (primary: terminal coding agent harness with multi-agent orchestration and LLM-agnostic abstraction)
- **Level 5 — Memory/Context** (secondary: persistent cross-session memory, context reconstruction, deterministic workflows)

Not L1: MiMo Code does not run inference; it wraps providers via OpenAI-compatible APIs. Not L3: the skills/workflows are per-project conventions, not organization-wide SSOT generation.

Closest comparables: OpenCode (parent fork — MiMo Code adds memory/orchestration to OpenCode's base), Claude Code (L1/L2, Anthropic-native, no persistent memory), Omnigent (meta-harness, multi-runtime routing, less opinionated on memory). MiMo Code occupies the "opinionated single-harness with memory" niche; Omnigent occupies the "flexible multi-harness" niche.

## Claims to verify

- **"Fork of OpenCode"**: the README states this explicitly; it is a fork with significant additions. The fork relationship means MiMo Code inherits OpenCode's 188k-star ecosystem signal but also its breaking-change risk when OpenCode upstream changes.
- **SQLite FTS5 memory performance**: MEMORY.md with automatic checkpointing across long-running projects needs independent verification — how does context reconstruction interact with the FTS5 index at scale (e.g., 6-month project with 10k memory entries)?
- **"Self-modification" via new skills**: the compose agent writing new skills into the running system is a supply-chain risk — arbitrary skill injection by the orchestration layer requires trust boundary documentation that is not yet public.
- **Voice input via MiMo ASR**: Xiaomi's MiMo ASR model availability (cloud vs. on-device, licensing, API access) is not described in the public README.

## Status

- No registry entry: 41 days old (v0.1.7, pre-1.0); no deterministic cost/latency data for the harness layer; schema has no `agent_roles` or `memory_backend` fields.
- Schema gap: `agent_roles: [single | build-plan-compose | specialist-ensemble]`; `memory_backend: [none | in-context | sqlite-local | cloud-vector]`; `workflow_model: [conversational | deterministic-script | hybrid]`.
- Cross-watch: OpenCode upstream (anomalyco/opencode, 188k stars) — MiMo Code's continued divergence from upstream determines whether it becomes an independent entry or a thin wrapper. Monitor for: first incompatible fork divergence, memory backend documentation, MiMo ASR licensing terms.
- Pair with: Omnigent (meta-harness multi-runtime) — together these represent two distinct extensions of the OpenCode base: MiMo Code extends depth (memory, roles, voice); Omnigent extends breadth (multiple runtimes, governance). They are complementary, not competing.
