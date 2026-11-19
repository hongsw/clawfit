# Research Watch: Stitch Skills (Google Labs)

- Repo/Link: https://github.com/google-labs-code/stitch-skills
- Source: GitHub Trending

## Why this is worth watching
Google Labs has shipped a first-party skills library for the Stitch MCP server. With 10,391 stars, it signals that Google is building a parallel skill ecosystem to Anthropic's Claude Code skills layer, using the MCP protocol as the interoperability layer. This is the first major hyperscaler-backed MCP skill library.

## What stands out immediately
- First-party from Google Labs, not a community contribution
- Targets the Stitch MCP server as the runtime host
- TypeScript skills library — implies composability with other MCP hosts
- Competitive response to Anthropic's skills ecosystem

## Why clawfit should care
clawfit tracks MCP servers and agent skills layers. Stitch Skills adds a new entry in the Level 4 (Plugin/Skill) layer, backed by a major provider. It may also affect how clawfit scores Gemini CLI — agents using Gemini models now have a first-party skills library, which improves their "extensibility" dimension.

## Preliminary interpretation
Current best reading:
- **Level 4 — Plugin/Skill Layer**: First-party MCP-based skill library, sitting above the Gemini CLI/Stitch harness and providing reusable agent capabilities.

## Status
- Tracking: new, high-signal (Google first-party)
