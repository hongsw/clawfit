# Research Watch: google-labs-code/stitch-skills

- Repo/Link: https://github.com/google-labs-code/stitch-skills
- Source: GitHub Trending

## Why this is worth watching
Google Labs Code has published a curated skill library for the Stitch MCP server, explicitly designed for compatibility across multiple coding agents (Claude Code, Gemini CLI, OpenCode, Codex). With 9,280 stars it has established significant traction outside the Google-owned agent ecosystem. It represents a second data point for a "platform-agnostic Google-authored skill library" after `google/skills` (Jun 2026), but with an MCP-first architecture rather than a Workspace/Cloud API first architecture.

## What stands out immediately
- Targets the Stitch MCP server as the primary delivery channel, not a standalone CLI
- Explicitly lists multi-agent compatibility (not Google-agent-only)
- TypeScript-first, 247 stars gained in a single day
- Distinct from `google/skills` (Workspace/Cloud/Maps-focused, tracked 2026-06-09) — Stitch Skills focuses on dev workflow tasks (testing, refactoring, scaffold generation)
- 9.2k total stars vs. google/skills at ~23k — still a significant standalone repo

## Why clawfit should care
Stitch Skills is a second major skill library from Google Labs aimed at developer agents, but oriented to MCP delivery rather than direct API invocation. It strengthens the signal for a `delivery_model: mcp | direct-api | slash-command` dimension on skill pack entries in the registry. As the number of multi-compatible skill libraries grows, the recommendation engine needs to map skill packs to the agent harnesses that can consume them.

## Preliminary interpretation
Current best reading:
- **Level 4b — Skill/Plugin Layer** (MCP-delivered skill library for coding agents)
- Secondary L4c (MCP server as delivery substrate)

## Status
- First scan: 2026-11-16
- Registry action: deferred — no deterministic latency/cost per skill invocation; schema needs `delivery_model` field before this category is fully scoreable
- 📡 Two-signal check: `google/skills` (Jun-09) is first signal for "major-vendor agent skill library"; Stitch Skills (today) is **second signal** — two-signal rule met for a canonical `domain_skill_pack` entry from a major vendor; consider adding `delivery_model: mcp` as a schema annotation
