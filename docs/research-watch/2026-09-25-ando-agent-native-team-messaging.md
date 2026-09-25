# Research Watch: Ando — Agent-Native Team Messaging Platform

- Repo/Link: https://ando.so (no public GitHub repo)
- Source: TechCrunch / Yahoo Finance / HN front page (Sept 24, 2026)
- Funding: $20M pre-seed + seed (Accel, Index Ventures, Emergence Capital)
- Announced: September 24, 2026

## Why this is worth watching

Ando emerged from stealth on September 24, 2026 as a team messaging platform explicitly designed around AI agents as first-class participants — not bots or integrations, but identity-bearing team members with their own inboxes, channel memberships, and permissions. The $20M raise from tier-1 investors (Accel, Index, Emergence) on launch day is not routine seed activity; it signals institutional conviction that the human-agent collaboration interface layer is about to be rebuilt. The Slack analogy is instructive: Slack displaced email not by being a better email client but by changing the collaboration primitive. Ando is betting the same displacement pattern applies to AI agents at work.

## What stands out immediately

- Agents receive discrete identities with their own inboxes, not shared bot accounts — identity granularity matters for audit and permission scoping
- Agents can proactively initiate messages, join channels, and reach out across workspaces without requiring human tagging or orchestration
- Live "Jams" (voice/video with transcription) include agents as participants, not just observers
- Agent-agnostic runtime: supports Codex, Claude, Grokbot, Devin, and a hosted harness of their own
- Explicitly positioned as a "full Slack replacement," not a plugin or integration layer
- Cross-agent coordination built in: agents can identify when peers' work intersects and consolidate relevant parties
- Initial target: teams of 2–40 humans; enterprise onboarding planned late 2026

## Why clawfit should care

The L6 (Human Interface) layer currently has entries for IDEs, CLI agents, and desktop productivity surfaces. Ando introduces a new sub-type: **agent-native async communication fabric**. This is structurally different from agent dashboards or IDEs — it's a shared workspace where agents operate asynchronously alongside humans without requiring a human to be the bridge. This directly affects how clawfit should model `statefulness: session` vs `statefulness: stateful` for multi-agent work profiles. If teams adopt Ando-style platforms, the "session" boundary disappears — agents operate in persistent, always-on contexts.

The "eliminate meat proxies" framing is analytically useful: it names the current friction precisely. Any harness that requires humans to relay agent outputs to other humans is a meat proxy. Ando's elimination of that pattern, if successful, shifts the scoring weight of `network: online` and `statefulness: stateful` in multi-agent enterprise profiles.

## Preliminary interpretation

Current best reading:
- **Level 6 — Human Interface Layer** (primary: agent-native communication surface)
- **Level 2 — Harness/Wrapper Layer** (secondary: agent identity, permission, and session management infrastructure)

The L6/L2 dual classification reflects the structural reality: Ando is simultaneously an end-user product and infrastructure for agents to operate within persistent shared contexts.

## Claims to verify

- Whether agent identity and permissions are cryptographically scoped or trust-based (significant for enterprise security posture)
- Whether the hosted harness supports custom tool/skill injection or only natively supported agents
- What session persistence model looks like at the protocol level (stored context vs. live agent instance)
- Whether the "your own harness" option means running agents locally or just API-key substitution
- Whether there is a GitHub repo or public SDK under the hood

## Status

- New signal — first tracked tool in "agent-native async communication fabric" sub-type
- No GitHub repo; no deterministic cost/latency data for registry
- Monitor for SDK/API release or GitHub presence; re-evaluate for L6/L2 registry entry if public API with deterministic pricing materializes
- The "full Slack replacement" positioning is ambitious; watch for enterprise adoption signals in the next 60 days
