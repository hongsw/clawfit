# Research Watch: PartsPlan — Industrial Hardware Datasheet MCP Server

- Repo/Link: https://news.hada.io/topic?id=35201
- Source: GeekNews front page (Show GN)

## Why this is worth watching
PartsPlan is an MCP server that grounds AI answers in manufacturer datasheet pages rather than parametric training data, targeting electronics/hardware engineers who query component specifications. It is the first observed MCP server specifically targeting the hardware manufacturing / industrial electronics domain — an underrepresented vertical in the current agent tooling landscape that predominantly addresses software development and knowledge work.

## What stands out immediately
- **Source grounding:** answers cite the exact datasheet page they came from (model references, not hallucinations)
- **Domain:** manufacturer datasheets for electronic components — ICs, sensors, modules, connectors
- **MCP integration:** standard MCP server protocol; plugs into Claude Code, Cursor, and other MCP-compatible harnesses
- **Vertical specificity:** industrial electronics / embedded hardware domain is almost entirely absent from current agent tool directories

## Why clawfit should care
- Extends the `primary_task` axis: `hardware-design` and `embedded-development` are missing task types in `org_questions.json` — this is the third signal for that gap (after TwoStraws SwiftUI Skill 2026-10-10 for mobile, and Text-to-CAD 2026-07-22 for mechanical)
- Pattern: domain-specific MCP servers for professional technical domains (legal, medical, hardware) are compounding — each represents a user segment whose `primary_task` is not captured by current filters
- For `governance_need: hard` industrial orgs (aerospace, medical devices, defense), a datasheet-grounded MCP reduces hallucination risk for compliance-sensitive component selection
- Low star count at listing time (Show GN); below 5k registry threshold; monitor for adoption

## Preliminary interpretation
Current best reading:
- **Level 4 — Domain-specific MCP capability tool** (hardware/datasheet domain)

## Status
- First signal for "industrial electronics MCP server with datasheet grounding"
- Third signal for "professional domain-specific primary_task not in org_questions.json" (mobile dev 2026-10-10, CAD 2026-07-22, hardware datasheets today)
- Monitor: star count, whether industrial/embedded community adopts
