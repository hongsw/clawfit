# Research Watch: Bring Your Own Agent to Microsoft Teams

- Repo/Link: https://microsoft.github.io/teams-sdk/blog/bring-your-agent-to-teams/
- Source: Hacker News front page (2026-04-23)

## Why this is worth watching
Microsoft Teams has ~320M monthly active users. Enabling any existing agent (LangChain, Azure AI Foundry, Slack bots) to plug into Teams via a three-line adapter is enterprise distribution at a scale that dwarfs any developer-focused deployment surface in this taxonomy. This is the enterprise harness entry point, not the developer tooling entry point.

## What stands out immediately
- **Zero-rebuild integration**: wrap existing HTTP agent server with ExpressAdapter, create TeamsApp, handle messages — three lines per the docs
- Supported sources: Slack bots (Bolt), LangChain chains, Azure AI Foundry, any HTTP bot
- Built-in request verification and routing — removes security boilerplate from enterprise integrations
- Dev experience: Teams CLI + Azure AD auto-registration + dev tunnel support
- Target persona: developers who built agents elsewhere and need enterprise Teams reach

## Why clawfit should care
There is currently no enterprise collaboration platform integration entry in the Level 2/4c layer of this taxonomy. Teams BYOA is different from Slack/Discord bots (developer audience) — it targets IT governance, compliance teams, and enterprise executives who approve software through IT procurement. For `team_size: large` + `governance_need: hard` profiles, "does this agent work in Teams?" may be a binary filter. This signals a new enterprise deployment surface worth modeling in the `output_destination` dimension.

## Preliminary interpretation
Current best reading:
- **Level 4c — Enterprise agent distribution / collaboration platform connector**
- Distinct from Level 2 harnesses: BYOA is a distribution adapter, not an orchestration layer

## Status
- Microsoft SDK, production-ready — ecosystem signal; revisit for registry entry when Teams agent marketplace solidifies
