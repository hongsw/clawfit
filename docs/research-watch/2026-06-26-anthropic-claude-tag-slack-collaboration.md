# Research Watch: Anthropic Claude Tag — Claude as a Slack Team Member

- Repo/Link: https://anthropic.com
- Source: GeekNews

## Why this is worth watching
Anthropic published "Claude Tag," a feature allowing Claude to be added to Slack channels as a named team member and receive task delegation via @mentions. This is Anthropic's first integration that places Claude inside an existing asynchronous team communication workflow rather than requiring users to navigate to a dedicated interface. It makes the agent a persistent ambient presence in team coordination, not just a point-of-need query tool.

## What stands out immediately
- Claude appears as a team member (@Claude), not a bot widget — social framing of agent identity
- Task delegation via mention: `@Claude summarize this thread`, `@Claude draft a follow-up`
- Asynchronous by default — fits Slack's async-first workflow model
- Directly comparable to the 2026-05-22 Multica signal (team agent platform) and Microsoft Teams BYOA (2026-04-23)

## Why clawfit should care
The L7 human interface layer currently covers IDEs, terminals, desktop apps, and voice. Slack (persistent async team channel) is a distinct interface sub-type that is not currently represented. Claude Tag is the first first-party Anthropic signal for this L7 sub-type. For enterprise profiles with `team_size: large` and `governance_need: hard`, the recommendation of "agent in the team communication surface" vs. "dedicated agent IDE" is a meaningful axis. The `output_destination: internal_product` dimension in clawfit is the closest existing proxy, but doesn't capture the ambient-async usage pattern.

## Preliminary interpretation
Current best reading:
- **Level 7 — Human interface** (async team communication channel sub-type; Slack-native)
- **Level 2 secondary** (task delegation pattern resembles harness routing, but at the L7 surface)

## Status
- First signal; proprietary feature (no public repo or star count). Held.
- Watch: whether other frontier model providers (OpenAI, Google) ship equivalent Slack integrations (would confirm the sub-type, not just one product).
- Promotion criterion: second major agent provider ships a Slack-native team-member integration OR Anthropic publishes an API for the delegation protocol.
