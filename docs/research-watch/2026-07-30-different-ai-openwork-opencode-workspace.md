# Research Watch: OpenWork (different-ai)

- Repo/Link: https://github.com/different-ai/openwork
- Source: GitHub Trending (⭐17,881, +97 today)

## Why this is worth watching
OpenWork is positioned as "the open-source alternative to Claude Cowork, powered by opencode" — explicitly naming a commercial Anthropic product as its displacement target. With 17,881 stars it has strong early traction, and different-ai (the team behind File Organizer 2000) has a track record of shipping AI-native productivity tools. The combination of OpenCode's coding-agent layer with a team-workspace shell creates a self-hosted path that bypasses Anthropic subscription lock-in.

## What stands out immediately
- Explicitly markets against a named commercial product (Claude Cowork), positioning as the OSS alternative
- Built on OpenCode as the coding-agent runtime — inherits its task execution capabilities out of the box
- Team workspace framing (not solo-developer): shared sessions, project context, multi-agent coordination
- different-ai's File Organizer 2000 precedent shows team can ship practical user-facing AI products (not just research)
- 17,881 stars on GitHub Trending with only +97 today suggests existing organic traction, not a trending spike

## Why clawfit should care
Reinforces the L6/L2 collapse pattern: workspace interfaces are increasingly built on top of coding agents rather than being separate products. For clawfit's recommendation engine, OpenWork is a strong candidate entry for `governance_need: low` + `team_size: small/mid` + `network: online` profiles who want OpenCode's capabilities wrapped in a shared workspace UX. Direct competitor to oh-my-openagent and oh-my-claudecode at the team workspace layer.

## Preliminary interpretation
Current best reading:
- **Level 2 primary — Harness/Wrapper** (team orchestration shell built on OpenCode)
- **Level 6 secondary — User Interface Layer** (workspace UI for team-shared agent sessions)

## Status
- First signal — registry candidate (exceeds 5k★ threshold; deterministic latency/cost data pending before `tools_registry.json` entry)
- Schema gap: `base_agent_runtime: str` — no field to express that OpenWork requires OpenCode as a dependency
