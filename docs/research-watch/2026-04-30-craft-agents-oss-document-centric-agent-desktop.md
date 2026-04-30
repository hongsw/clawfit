# Research Watch: craft-agents-oss — Document-Centric Desktop Agent Application

- Repo: https://github.com/lukilabs/craft-agents-oss
- Also see: https://craft.do (parent product), obra/superpowers (L3 methodology, co-trending 2026-04-30), mattpocock/skills (L4b practitioner skill directory, tracked 2026-04-26)

## Why this is worth watching
craft-agents-oss is a document-centric desktop agent application from the team behind craft.do, positioning itself against the dominant code-centric harness pattern (Claude Code, Codex CLI, Cursor) with a workflow framing organized around tasks and documents rather than file trees and terminals. At 5,330 stars on GitHub Trending TypeScript (rank #11) it has above-threshold initial traction. The combination of a built-in skills system, 32+ MCP tools, REST API connections (Gmail, Slack, Microsoft, Google), and headless server mode places it at an unusual cross-layer position — it bundles what clawfit typically tracks as L2 harness, L4b skills, and L5 MCP in a single end-user desktop application.

## What stands out immediately
- **Document-centric workflow model** — task inbox organized as Todo/In Progress/Done; primary unit is a document or task, not a file or terminal session. Explicitly differentiates from code-centric agents.
- **Three-tier permission model** — Explore (read-only), Ask to Edit (human-in-the-loop), Auto (fully autonomous). Matches the governance axis clawfit already scores on (`statefulness` and `governance_need`); an unusual end-user-facing exposure of that dimension.
- **32+ MCP tools shipped in-box** — MCP integration is not a plugin but a first-class feature, including REST API connections to Gmail, Slack, Microsoft (Office 365 family), and Google Workspace. This makes MCP a default connectivity layer for knowledge-worker workflows, not an optional add-on for developer workflows.
- **Skills system for specialized agent instructions** — named sub-agents or instruction profiles invocable per task. Structurally parallel to L4b skills (SKILL.md pattern, Vercel skills, VoltAgent/awesome-agent-skills) but housed within a GUI desktop application rather than a dotfile directory.
- **Multi-provider LLM support** — Anthropic, Google, OpenAI, and GitHub Copilot. Provider-agnostic by design, which aligns with the multi-vendor anti-lockin cluster signal documented 2026-04-28.
- **Headless server mode with thin-client desktop** — separates the agent execution substrate from the UI surface; enables self-hosted or remote deployment with a lightweight client. Claim to inspect: documentation does not yet confirm what auth and deployment requirements headless mode carries in practice.
- **Apache 2.0 license** — permissive; enterprise-friendly. Distinct from AGPL (Warp, 2026-04-29) and PolyForm Noncommercial (GitNexus, 2026-04-28).
- **TypeScript-first** — consistent with the broader TypeScript trend in high-star harness tooling (cc-switch, vercel-labs/skills, GitNexus).

## Why clawfit should care
craft-agents-oss represents a distinct deployment pattern not yet covered by the taxonomy: a **desktop-first, document-native agent harness targeting knowledge workers** (writers, PMs, researchers) rather than developers. Several implications:

1. **`primary_role` axis gap** — clawfit's current role taxonomy skews heavily toward `developer`, `devops`, and `data-scientist`. craft-agents-oss is the most prominent L2-equivalent entry targeting `pm`, `writer`, and `researcher` roles, alongside kepano/obsidian-skills (L4b, knowledge work, 20k★) and coreyhaines31/marketingskills (L4b, marketing, 23.7k★). Those two are content/skill packs; craft-agents-oss is an executable harness for those roles.

2. **`primary_task` axis gap** — the skills system and REST integrations are oriented toward communication tasks (drafting, sending, summarizing email/Slack/docs), which clawfit currently lacks a clean task label for. The existing `writing` task type partially covers this, but the combination of writing + API action (send email, create Slack message) is closer to the `agentic-workflows` category that has no current registry slot.

3. **Scoring dimension for MCP density** — 32+ MCP tools in-box raises the question of whether "ships integrated MCP toolset" should be a scoring signal for `task: research` and `task: writing` profiles where external-service connectivity is a practical prerequisite. Currently MCP integration is treated as a binary yes/no filter, not a quality/density axis.

4. **Headless server mode and `hardware` dimension** — if headless server mode is confirmed to work independently from the desktop client, craft-agents-oss could score in `hardware: cloud` self-hosted profiles as a knowledge-worker harness, not just as a local desktop tool.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrapper / harness / orchestration layer** (primary; end-to-end agent harness with session management, skills, permissions, and multi-provider LLM routing)
- **Level 4b — Capability / skill layer** (secondary; built-in skills system is structurally analogous to the L4b skill patterns already tracked)
- **Level 5 — Memory / MCP / context layer** (cross-cut; 32+ MCP tools are first-class, not plugin. MCP is the connectivity substrate rather than an optional extension)
- Sub-type: **document-native knowledge-worker harness** — distinct from code-native harnesses (Claude Code, Codex CLI, Cursor/Cline/Roo Code) and from terminal-native harnesses (Warp, cmux). First entry in this taxonomy with this shape.

## Status
- New signal. 5,330 stars, Apache 2.0, TypeScript. Above the 5k-star threshold for registry consideration but the agent/llm/hardware schema does not currently accommodate a desktop harness targeting knowledge workers. Flag for schema review: (1) whether `primary_role: writer` or `primary_role: pm` should be added as named roles; (2) whether `primary_task: async-communication` or `primary_task: document-workflows` should be added as task types. If both flags are resolved, craft-agents-oss is a plausible Level 2 registry entry. No docs/reference-levels.md mutation today; document-native harness sub-type note should be incorporated on next reference-levels update cycle.
