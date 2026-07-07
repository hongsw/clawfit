# Research Watch: OpenTag — Self-Hosted Agent for Team Chat Surfaces

- Repo: https://github.com/CopilotKit/OpenTag
- Also see: https://www.copilotkit.ai/opentag-managed (managed variant), docs/research-watch/2026-06-06-copilotkit-ag-ui-protocol-agent-frontend.md (distinct product — AG-UI Protocol)

## Why this is worth watching
OpenTag is a reference implementation from the CopilotKit org that deploys an AI agent directly into Slack, with Discord, Telegram, and WhatsApp listed as targets on the same SDK. It is the first CopilotKit-org artifact aimed at team communication surfaces rather than web app UIs, which makes it architecturally distinct from CopilotKit's core React/Angular SDK. The GeekNews signal (8 points, 2026-07-07) is weak on its own, but the backing org — $27M raised, May 2026 — gives it institutional weight.

## What stands out immediately
- Self-hosted: "you own the runtime, bring your own model" — no per-seat pricing or vendor lock-in claim
- Built on `@copilotkit/bot`, `@copilotkit/runtime`, and platform adapter packages; OpenTag is a reference impl, not a standalone runtime
- Reads Slack threads, executes tool calls, renders generative UI (tables, charts) inline in conversation
- Human-in-the-loop approval gate is surfaced natively inside the chat thread — approval happens where the work happens
- Optional Redis for thread-state persistence; stateless by default
- Multi-LLM: OpenAI, Anthropic, and others via the CopilotKit runtime abstraction
- Distinct from CopilotKit's AG-UI Protocol, which targets React/Angular web UIs; OpenTag targets chat-platform surfaces

## Why clawfit should care
This is the first observed pattern of a well-funded agent SDK org shipping a dedicated Slack-surface deployment artifact. If this pattern spreads, "which chat surface does this agent run on?" becomes a filter axis in clawfit alongside `task`, `network`, and `statefulness`. OpenTag also reinforces the `statefulness: session` profile — thread state via Redis is optional, meaning many deployments will be stateless-by-accident in a context (Slack threads) where continuity is expected.

## Preliminary interpretation
Current best reading:
- **Level 6 primary — Human interface / team communication surface**: OpenTag's purpose is to embed agent capability inside Slack/Discord/Teams conversations; the interface layer is the product, not incidental
- **Level 2 secondary — Harness/wrapper**: orchestrates tool calls, threading, and HIL gates on top of CopilotKit's bot SDK; not a base runtime in its own right

## Status
- New signal, low community traction (8 GeekNews points). Reference impl status limits registry candidacy. Monitor for standalone adoption outside CopilotKit ecosystem. Flag if chat-surface becomes a scoreable axis.
