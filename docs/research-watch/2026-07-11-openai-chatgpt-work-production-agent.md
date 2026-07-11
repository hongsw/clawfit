# Research Watch: ChatGPT Work — OpenAI's Hours-Long Production Agent

- Repo/Link: https://openai.com/chatgpt/work/
- Source: Bloomberg, MacRumors, The Next Web (July 9, 2026)

## Why this is worth watching
ChatGPT Work is the first OpenAI product that competes directly in the L1 "production agent runtime" category that clawfit tracks. Prior OpenAI products (ChatGPT, DALL-E, Codex CLI) are either conversational, generative, or developer-facing. ChatGPT Work is a deployed autonomous agent marketed to enterprise users as a task executor: it breaks goals into steps, runs them independently for hours, and returns finished artifacts — not conversation.

## What stands out immediately
- Runs on GPT-5.6; multi-step task execution lasting hours without continuous user input
- Output is finished work: spreadsheets, slides, documents, interactive web apps — not chat
- Plan mode: shows a step-by-step plan the user approves before work starts
- Configurable check-ins and action approvals: explicit autonomy dial, from fully supervised to fire-and-forget
- Built-in browser: accesses URLs, online files, and tools directly
- Connected apps: pulls context from local files and external services
- Codex technology built in: code execution as a first-class capability
- Available to Pro, Enterprise, Edu at launch; Plus and Business within days
- Cross-device continuity: start on mobile, review on web, resume at desk

## Why clawfit should care
ChatGPT Work is a direct commercial competitor to the agent patterns clawfit currently recommends. It targets the same profiles: `task: research | code-gen | data-analysis`, `statefulness: session | persistent`, `team_size: mid`. Compared to open-source L1 runtimes (Claude Code, Goose, Pi), ChatGPT Work bundles runtime, model, execution environment, and enterprise integrations as a single managed product — the tradeoff is control vs. out-of-box completeness. The autonomy dial (Plan mode, configurable check-ins) maps directly to the `governance_need` axis clawfit is evaluating for schema expansion. This is also the clearest signal yet that "hours-long task execution" is a named product feature, not just an architecture property.

## Preliminary interpretation
- **Level 1 — Base agent runtime** (primary, managed cloud runner)
- **Level 6 — Human interface layer** (secondary, enterprise UI with approval surfaces)
- No self-hosted path (fully managed): relevant to `network: online`, `hardware: cloud` profiles only
- Statefulness: persistent (cross-device session continuity)

## Claims to verify
- "Works for hours" — actual session limits and timeout behavior not published at launch
- Connected apps depth: which app integrations are available and whether enterprise SSO is supported
- Whether the autonomy dial actually gates outbound actions (writes, sends, publishes) or only informs the user post-hoc
- Pricing structure: currently implied as included in Pro/Enterprise subscriptions, per-task pricing not confirmed

## Status
- First signal 2026-07-11 (commercial product, no GitHub repo)
- No registry entry: agents.json covers pattern-based agent types, not SaaS products; schema mismatch
- Schema watch: `autonomy_mode: supervised | configurable | autonomous` as a future `org_fit` axis
- Monitor: whether Anthropic or Google ship analogous named products ("hours-long task execution" as product category)
