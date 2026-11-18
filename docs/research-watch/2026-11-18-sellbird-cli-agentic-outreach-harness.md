# Research Watch: Sellbird — CLI-Based Agentic Sales Outreach Harness

- Repo: https://github.com/ethanplusai/sellbird (⭐6,400)
- Source: GitHub Trending Python (358 stars today, 2026-11-18)

## Why this is worth watching

Sellbird (formerly Harvey through v0.3.x) is an open-source agentic outreach platform that runs the full cold-outreach pipeline — prospect discovery, email verification, copy generation, sending, and reply handling — as an agentic workflow. Its architecture is structurally unusual: it does not use API keys but requires a Claude Pro/Max subscription with the Claude Code CLI, or a ChatGPT subscription with the Codex CLI. This design routes the full workflow through a coding agent harness rather than through a direct model API, which means the billing model, rate limits, and execution context are entirely different from API-based automation tools.

## What stands out immediately

- **No API key required**: needs Claude Pro/Max + `claude` CLI OR ChatGPT plan + `codex` CLI — the billing is subscription-based, not token-based; this is structurally different from every other agent harness in the current registry that uses API pricing
- **Full outreach pipeline as agentic loop**: find companies (OpenStreetMap by default) → read websites for buying signals → find owner/manager → verify email address → write personalized cold email sequence → send (Gmail, M365, SMTP) → read replies → draft responses — each step uses the coding agent as the execution context
- **Human-in-the-loop by default**: holds every email for approval before sending; autopilot mode is opt-in; a `sellbird sending pause` command stops all sending — this is a explicit trust architecture, not an afterthought
- **AGPL-3.0 relicensed from MIT**: Harvey v0.3.x was MIT; v0.4.0 (the Sellbird rename) moved to AGPL; existing users of Harvey must review license implications
- **6,400 total stars, 1,300 forks**: meaningful traction for a business-automation tool; not a showcase project
- **External data dependencies**: uses OpenStreetMap for prospect finding by default; suggests a paid source for higher-quality leads — this means the tool's output quality depends on data source selection, not just model quality
- **Python 3.11+ only**: constrains deployment environment; not deployable on systems running older Python versions

## Why clawfit should care

Sellbird is a first signal for "subscription-CLI-based business process automation" as a distinct architectural pattern. The existing registry tracks harnesses that consume model APIs (OpenAI, Anthropic, etc.) and hardware that hosts those APIs. Sellbird consumes a subscription product (Claude Pro, ChatGPT) through its CLI interface — a billing model that falls entirely outside clawfit's current `budget` filter, which is denominated in cost-per-token or cost-per-request. If this architecture generalizes (other automation tools routing workflows through coding agent CLIs rather than direct APIs), clawfit may need a `billing_model: subscription | api | hybrid` field to represent the distinction.

The outreach domain also expands the `task` taxonomy: Sellbird's tasks (prospect discovery, cold email, reply management) do not map cleanly to existing types (`code-gen`, `qa`, `research`, `data-analysis`, `summarization`). A `task: business-automation` or `task: outreach` classification would be needed for registry inclusion.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/Wrapper** (primary): Sellbird orchestrates a multi-step agentic workflow using a coding agent CLI as the execution substrate
- **Level 6 — Human Interface** (secondary): the approval-hold model and `sending pause` command position it as a supervised automation tool, not a fully autonomous agent

## Claims to verify

- Whether the subscription-CLI architecture actually routes through Claude Code's agentic loop or simply calls `claude` as a command-line LLM without tool use — the distinction matters for how to classify its harness model
- Whether AGPL-3.0 licensing creates compliance issues for enterprise users running it on internal sales pipelines — not addressed in the README
- Whether the 64% paid send rate (every email held for approval) is intentional UX or a bug in autopilot mode detection
- Whether the OpenStreetMap-based prospect finding is accurate enough for real outreach use, or whether it functions only with a paid prospect source

## Status

- First scan: 2026-11-18
- Registry action: **deferred** — `task: outreach` not in current taxonomy; `billing_model: subscription` not in current schema; would require schema changes before registry entry
- 📡 Note: Sellbird is the first signal for "coding-agent-CLI-based business automation harness" (subscription billing, not API billing); watch for a second tool routing a business process workflow through a coding agent CLI — would justify adding `billing_model` as a registry field and a canonical L2 "subscription-CLI harness" sub-type
