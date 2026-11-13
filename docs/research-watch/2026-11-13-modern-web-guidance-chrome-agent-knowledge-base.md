# Research Watch: GoogleChrome/modern-web-guidance-src — Browser-Team Agent Knowledge Base

- Repo: https://github.com/GoogleChrome/modern-web-guidance-src (⭐4,525)
- Source: GitHub Trending (all languages, daily, 2026-11-13 — 1,875 stars gained today)

## Why this is worth watching

The Chrome, Edge, Firefox, and MDN teams jointly maintain a structured library of modern web platform guidance, explicitly designed to be injected into coding agents' context windows. The 1,875 stars gained in a single day suggests a recent announcement or milestone. Unlike ad-hoc RAG pipelines over MDN docs, this is an official first-party source with curated token-efficient entries, a CLI for retrieval, and built-in evals to prune content that models already handle correctly without it. The stewardship breadth — four browser and documentation teams — is unusual for a developer-tools signal.

## What stands out immediately

- **Purpose-built for agent context:** Guides are explicitly written and pruned for token efficiency, with evals to remove content that the model already handles well — a curation model distinct from documentation scrapers or RAG pipelines
- **Multi-organization stewardship:** Chrome, Edge, Firefox, and MDN teams co-maintaining a single repo is structurally different from a single vendor's SDK — it carries cross-browser consensus weight
- **250 modern web feature entries** organized across CSS/Layout (140), JavaScript/APIs (74), HTML/DOM (36) — covering the most hallucination-prone areas for coding agents working on web projects
- **203 real-world developer use cases** structured for retrieval against agent-generated code
- **CLI tool:** `npx modern-web-guidance@latest install` with `search`, `retrieve`, and `legacy-scan` commands — agents can call this via tool use or the harness can inject relevant entries pre-turn
- **Legacy-scan command:** Scans a codebase and returns a list of outdated patterns with modern replacements — directly actionable for coding-agent code review workflows
- **Apache-2.0 license** with 1,600 commits, suggesting sustained maintenance rather than a one-time release

## Why clawfit should care

clawfit's `task: code-gen` and `task: qa` profiles currently do not account for web platform knowledge currency as a scoring dimension. A coding agent that injects modern-web-guidance entries will produce fewer deprecated API calls on web projects. This is a capability multiplier for browser-targeting use cases: Aider, Continue, OpenCode, and other general-purpose coding agents could all benefit. The `legacy-scan` command is also relevant to the `task: code-review` workflow that openqodex (2026-11-02) opened. This is not a new agent — it is infrastructure for making existing agents more accurate on a large and commonly requested task domain.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capabilities / Skills / MCP** (primary) — a knowledge base and CLI that extends any agent's grounded understanding of the web platform; functions as a skill-like capability injection layer
- **Level 3 — Team Workflow / SSOT Governance** (secondary) — the eval loop and pruning discipline, plus the multi-organization authorship, give it a governance dimension beyond a typical knowledge base

## Claims to verify

- Whether the CLI is MCP-server-compatible or requires harness-level tool definition
- Whether the eval methodology for pruning is published — "models already handle well" needs an evaluation benchmark reference
- Whether the 1,875 stars today reflect a formal announcement (Chrome Developer blog post, conference talk, etc.)
- Star count vs. actual adoption by major harnesses (Cursor rules, Claude Code knowledge files, Windsurf Cascade etc.)

## Status

- New signal — tracking; registry action deferred (not an agent/LLM/hardware entry; potential `knowledge_base: web-platform` capability annotation)
- **First signal for "official browser-team agent knowledge base"** — distinct from individual MDN documentation scraping, community knowledge files (like `.cursorrules`), and commercial RAG-over-docs services
