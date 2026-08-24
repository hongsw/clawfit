# Research Watch: TryCaspian/caspian-sdk — Multi-Channel Agent Communication SDK with Single Identity

- Repo: https://github.com/TryCaspian/caspian-sdk (⭐871)
- Source: Hacker News Show HN (August 21, 2026)

## Why this is worth watching

Caspian gives an AI agent one identity across Slack, Discord, Telegram, WhatsApp, Instagram, email, SMS, X, and Linear via a single `on_message` handler. The engineering goal is deterministic channel routing without the agent needing to know which platform the human is using — the agent writes output once; Caspian renders it natively per channel (Slack Block Kit, Discord embeds, Telegram keyboards).

The "Talk to Human Tool for AI Agents" framing positions this as infrastructure for the agent escalation moment — when the agent needs human input, it routes the message to wherever the human actually is, not just to one platform. This is a different problem from deploying a chatbot on multiple channels; it is an agent-to-human communication primitive.

## What stands out immediately

- **Single `on_message` handler across 9+ channels**: the integration abstraction hides platform-specific API differences from the agent runtime — channel proliferation does not add code complexity
- **Native rendering per channel**: messages are not plain-text forwarded; they are re-encoded as Slack blocks, Discord embeds, Telegram keyboards — preserving the structural meaning of agent output in the target channel's UI model
- **Declarative overlap policies**: `queue`, `debounce`, `drop`, `parallel` — the agent specifies what should happen if a human message arrives while the agent is processing; this is race-condition handling as a first-class API
- **Hosted or self-hosted**: Caspian's own gateway or self-hosted adapters with the agent's own tokens — a deployment choice that matters for enterprise data-sovereignty requirements
- **Webhook verification built-in**: Slack, Meta, Telegram, X, and email signature verification — removes a common implementation-error source when agents receive inbound messages from humans
- **650+ tests with platform-specific payload validation**: coverage across platform event schemas signals that the library is designed for production reliability, not demo-quality integration
- **Python and TypeScript**: two SDK languages matching the primary languages of the agent frameworks it targets (Claude Code is TypeScript; most ML harnesses are Python)

## Why clawfit should care

CopilotKit/channels-sdk (tracked 2026-08-06, 558 stars, L6) established the pattern of agent-to-channel routing. Caspian adds a distinct architectural element: **persistent agent identity across channels**. CopilotKit routes from a copilot's output to a channel; Caspian routes to wherever the human currently is, treating the human's location as dynamic and the agent's identity as stable.

This distinction matters for clawfit's task taxonomy. A `task: customer-support` or `task: async-coordination` profile needs the agent to follow the human across channels, not to pick one. clawfit has no `channel_identity: [single | multi-channel]` or `human_escalation_protocol: [none | platform-specific | cross-platform]` dimension — these would capture a meaningful capability gap between agents that can escalate to one fixed channel vs. ones that can reach a human wherever they are.

**Two-signal note**: CopilotKit/channels-sdk (2026-08-06) + Caspian (2026-08-24) = two signals for "agent multi-channel communication SDK," but different architectural sub-types (copilot embedding vs. agent identity persistence). Not the same sub-type; canonical section promotion deferred.

## Preliminary interpretation

Current best reading:
- **Level 6 — Human Interface Layer**: primary. Manages agent-to-human communication across channels, channel identity, and escalation routing.
- **Level 4 secondary**: the declarative overlap policies and webhook verification are capability infrastructure the agent runtime calls into.

Contrast with: CopilotKit/channels-sdk (tracked 2026-08-06, copilot-centric channel routing); munder-difflin (tracked 2026-08-18, desktop Electron harness for multi-agent coordination, not agent-to-human multi-channel messaging); Speko (tracked 2026-08-17, agent-native voice/messaging interface — single identity, fewer channel types).

## Claims to verify

- "One identity across channels" — whether this means a single agent user object that platforms associate with the same entity, or just a shared message-dispatch surface without persistent cross-platform identity
- Overlap policy behavior — `queue`, `debounce`, `drop`, `parallel` need concrete example scenarios; `debounce` in particular needs to specify time window behavior
- Self-hosted deployment — whether the self-hosted adapters require the user to provision and manage channel-specific app registrations (Slack App, Meta Business Account) independently
- Enterprise data sovereignty — does the hosted gateway see message content, or is routing metadata-only?
- 871 stars on August 21 Show HN — verify this reflects organic adoption, not a launch spike from the HN front page that will regress

## Status

- Tracking: first signal 2026-08-24
- Stars: 871 — below 5k registry threshold; channel SDK, no clean agent/LLM/hardware schema slot
- No canonical section change: CopilotKit/channels-sdk + Caspian = two signals in L6 channel routing space, but different sub-types (embedding vs. identity persistence); two-signal rule for same sub-type not met
- Schema watch: `channel_identity: [single | multi-channel]`; `human_escalation_protocol: [none | platform-specific | cross-platform]`; `overlap_policy: [none | queue | debounce | drop]`
- Watch: whether agent harnesses (Claude Code, Hermes, OpenClaw) ship native Caspian integration as a first-class escalation primitive
