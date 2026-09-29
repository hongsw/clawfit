# Research Watch: OpenAI Dots — Always-On Persistent Agentic Assistants

- Repo/Link: https://openai.com/index/introducing-dots/ (product announcement)
- Source: Hacker News (197 points), OpenAI DevDay 2026

## Why this is worth watching

OpenAI Dots is the first major commercial deployment of persistent, autonomous agentic assistants at consumer scale — each user gets a "dot" that runs continuously, maintains context across sessions, and acts proactively without per-prompt invocation. This is distinct from both API-based agents (you invoke them) and scheduled automations (they run at intervals). Dots are always on, learn from feedback, have their own compute (browser + computer), and integrate with 4,000+ apps. That architecture represents a direct test of whether persistent autonomous agent execution is commercially viable at scale.

## What stands out immediately

- Always-on execution model: not a chatbot, not a scheduled job — a persistent process that works between sessions
- Proactive goal pursuit: you assign an objective, the dot pursues it across tools and time without re-prompting
- Multimodal actions: makes phone calls, answers Slack/email, can make purchases on the user's behalf (approval-gated)
- 4,000+ app integrations built into the platform
- Underlying model: powered by GPT-6 Astra (top-tier reasoning model), not a smaller model
- Pricing: included in Pro plan (no per-action drawdown), which is $20/month — zero marginal cost for existing Pro users
- Initial rollout: one dot per user; multi-dot or org-level allocation not confirmed at launch
- Workplace integrations confirmed: Slack, Microsoft Teams, Codex
- Explicitly positioned against Meta's Muse agent — this is a competitive product move, not a research preview
- New $500/month ChatGPT Pro 500 tier announced alongside, implying higher-usage consumers exist as a segment

## Why clawfit should care

Dots defines a new agent deployment pattern: the persistent autonomous assistant vs. the on-demand API agent. Clawfit's current statefulness axis (`stateless`, `session`, `persistent`) now has a first-party commercial reference for `persistent` — OpenAI's own implementation. The "4,000+ app integrations" layer is structurally important for the L4 (capabilities/skills/MCP) taxonomy: if OpenAI's connector ecosystem becomes the de facto integration substrate, agent harnesses that want to compete must either support it or offer a compelling alternative. Registry implications are limited (no per-token cost for this product), but the L6 and L2 taxonomy are directly affected.

## Preliminary interpretation

Current best reading:
- **Level 6 — Human Interface** (primary): Dots is where the persistent agent meets the end user — chat, calls, email, purchasing
- Secondary L2 (harness): the "always-on process with memory, browser, tools, 4,000 integrations" is functionally a harness layer operating on the user's behalf
- Secondary L4 (capabilities/connectors): 4,000 app integrations constitute a substantial capability graph

## Claims to verify

- "Always-on" execution: what actually keeps the dot running — a long-polling process, event-driven triggers, or a scheduled heartbeat? Architectural details not disclosed
- "Learns from feedback": vague; may mean preference tuning on user correction vs. genuine online learning vs. just storing context
- Purchase authorization: approval-gated, but the approval UX and audit trail are not described
- 4,000 integrations: no full list; likely a claim based on Zapier/workflow tool integrations rather than direct API calls to each service
- GPT-6 Astra as the underlying model: stated in the announcement but may change per-feature or per-workload

## Status

- Official OpenAI product, DevDay 2026 (2026-09-29); rolling out to Pro users starting today
- Registry ineligible: product subscription, not a per-token API; no deterministic per-action cost
- Taxonomy action: update reference-levels.md L6 section to note Dots as first commercial persistent-assistant reference; note L2/L4 secondary classification; check if `persistent` statefulness in clawfit's filter axis needs a new reference example
