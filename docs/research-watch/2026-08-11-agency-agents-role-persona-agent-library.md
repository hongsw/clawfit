# Research Watch: agency-agents — 230+ Role-Specific Agent Persona Library

- Repo/Link: https://github.com/msitarzewski/agency-agents
- Source: GitHub Trending (2026-08-11, 142k stars, Shell)

## Why this is worth watching
agency-agents is a collection of 230+ AI agent persona definitions covering 18+ professional divisions (engineering, design, marketing, sales, product, legal, etc.), each with distinct personality traits, domain expertise, specific workflows, and measurable success metrics. Works natively with Claude Code, GitHub Copilot, Cursor, Aider, Windsurf, and 8+ other platforms via a desktop app installer. At 142k stars it is one of the most-starred AI agent configuration projects on GitHub.

## What stands out immediately
- **230+ agent personas** across 18+ divisions — role-driven rather than task-driven (contrast with addyosmani/agent-skills, which is task-driven)
- Native desktop installer app (macOS, Linux, Windows) for low-friction onboarding
- Harness-agnostic: works across 8+ coding platforms, not locked to one agent runtime
- Each persona includes explicit success metrics and deliverable specs — structured enough to score against org profiles
- MIT license; open for fork and customization

## Why clawfit should care
clawfit currently tracks task-oriented skill packs (mattpocock, addyosmani, phuryn, stitch). agency-agents introduces a **role-persona** axis: instead of giving an agent a skill, you give it an identity that spans multiple tasks. This is architecturally different from skill packs — the persona persists across tasks and shapes defaults, tone, and workflow order. **Schema exposure:** `skill_orientation: [task | role-persona | domain]`; `persona_count: N`; `platform_compatibility: [list of supported runtimes]`. The 142k star count and cross-platform support make this a strong candidate for the L4b skill section.

## Preliminary interpretation
Current best reading:
- **Level 4b — Skill packs & managers (role-persona sub-cluster)**

## Status
- Added to `tools_registry.json` as L4b agent_persona_library
- High-signal: 142k stars, cross-platform, desktop installer
