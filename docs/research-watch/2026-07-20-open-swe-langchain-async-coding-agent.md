# Research Watch: open-swe — Open-Source Async SWE Agent Platform

- Repo: https://github.com/langchain-ai/open-swe (⭐10,400)
- Source: GitHub Trending Python (rank 14, +18 today, 2026-07-20)

## Why this is worth watching

Open-SWE is LangChain's reference implementation of the production async SWE agent architecture used internally at Stripe, Ramp, and Coinbase. It is not a demo or prototype — it is the open-source version of how leading engineering orgs deploy coding agents as background workers that operate in isolated cloud sandboxes, triggered by Slack mentions, Linear comments, or GitHub PR reviews. At 10.4k stars with no formal versioned releases (tracked via commits only), it is growing on developer interest alone. The explicit design goal is that organizations fork or extend it to build their own internal agents rather than buy a commercial product.

## What stands out immediately

- **Background-async execution model**: agent tasks are not interactive (no terminal session); they are dispatched to a cloud sandbox (Modal, Daytona, Runloop, E2B, or custom), run to completion, then surface results as a drafted PR — an architectural complement to session-bound agents like Claude Code
- **Sandbox isolation as a hard design constraint**: the project's philosophy is "isolate first, grant full permissions inside the boundary" — each task gets a fresh container, short-lived credentials brokered by the control plane, and scoped repository access
- **Multi-channel invocation**: triggered via Slack (repo: syntax mentions), Linear (@ comments), or GitHub PR review comments — the agent lives in existing developer workflow surfaces, not a dedicated UI
- **Context engineering via AGENTS.md**: ingests structured per-repo convention documents alongside Linear issues or Slack threads to build task context — a pattern derived from Claude Code's CLAUDE.md mechanism
- **LangGraph stateful graph foundation**: agent control flow is defined as a LangGraph graph, giving deterministic resumability, mid-run message injection, and step-limit notification hooks
- **Curated minimal toolset**: 3 execution tools (execute, fetch_url, http_request) + 4 integration tools (linear, slack) + file ops (read, write, edit, ls, glob, grep) — deliberately smaller than general-purpose agent toolkits to reduce blast radius
- **Corridor guardrails via MCP**: optional integration with Corridor policy enforcement at the sandbox boundary — an agent cannot act outside its declared policy envelope even with full container permissions

## Why clawfit should care

Open-SWE exposes a structural gap in clawfit's `statefulness` filter. Current options (`stateless` and `session`) do not represent the background-async execution model — a task is dispatched, the agent runs unsupervised for hours, results surface later. This is distinct from interactive session-bound agents in three material ways: (1) latency profile: not milliseconds but minutes-to-hours per task cycle; (2) rollback requirements: the agent must produce a reviewable artifact (PR) before human acceptance, not execute changes directly; (3) trust model: human review happens after completion, not during. These differences affect scoring: `reliability_signal` and `auditability` matter more than `latency: low`.

Additionally, open-swe is built on the Deep Agents framework (LangChain's emerging harness layer), making it a second observable deployment of Deep Agents in the wild after Ramp's production system. This is a meaningful cross-signal for the harness layer taxonomy.

## Preliminary interpretation

Current best reading:
- **Level 2 primary — Agent harness**: wraps Deep Agents (itself a harness), orchestrates sandboxes, manages credential brokering, handles multi-channel dispatch
- **Level 1 secondary — Base runtime**: acts as the agent execution substrate for orgs that fork and deploy it internally
- **Level 3 tertiary — Governance**: Corridor MCP integration and the scoped-credential design add a policy enforcement layer that is structurally L3

Comparable to: background-agents (ColeMurray, tracked 2026-07-13, Cloudflare Durable Objects control plane) and devin (commercial SWE agent) — but open-swe is explicitly designed as an org-forkable internal platform rather than a black-box service.

## Claims to verify

- "Used at Stripe, Ramp, and Coinbase": README framing is "open-source version of systems used at" — does not confirm these orgs use open-swe specifically or that Ramp (which uses OpenCode) uses this exact architecture. Attribution may be aspirational or based on pattern-matching.
- LangGraph stateful graph design: repo uses LangGraph but no public architecture diagram was surfaced; mid-run message injection and resumability claims need hands-on verification.
- Corridor guardrails via MCP: listed as optional integration; no live Corridor MCP server link or API reference confirmed in the subagent fetch.
- Sandbox provider compatibility: Modal, Daytona, Runloop, E2B listed; pluggability claim needs independent integration testing across providers.

## Status

- No registry entry: `agents.json` has no field for `execution_model: [interactive | background-async | batch]` or `sandbox_provider: [modal | daytona | e2b | runloop | custom]`. Current schema cannot represent open-swe's core distinguishing property.
- Schema gap: `execution_model: [interactive | background-async | batch]`; `sandbox_provider: [none | modal | daytona | e2b | runloop | custom]`; `audit_trail: [none | pr-draft | structured-log]`.
- Statefulness filter watch: the current `statefulness: [stateless | session]` binary misses background-async workflows. Adding `background` as a third option would surface this class of agent correctly.
- Two-signal check for "background-async coding agent harness": background-agents (2026-07-13, Cloudflare DO + Modal) and open-swe (2026-07-20, LangGraph + Daytona/Modal) are two independent implementations of the same pattern: async coding tasks dispatched to cloud sandboxes, results as PRs, no interactive session. **Two signals confirmed.** Pattern name: "background-async SWE agent." No canonical section change this run — both tools are below the 5,000-star registry threshold or lack deterministic cost data; "when in doubt" rule applied. Discovery log note only.
