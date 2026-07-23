# Research Watch: ComposioHQ/awesome-claude-skills

- Repo/Link: https://github.com/ComposioHQ/awesome-claude-skills
- Source: GitHub Trending (all languages, 2026-07-23)

## Why this is worth watching
ComposioHQ/awesome-claude-skills is the highest-starred Composio skills aggregator (68,756 stars, 7.8k forks), cataloging 1,000+ production-ready Claude Skills across 10 categories covering Claude.ai, Claude Code, and cross-agent runtimes (Cursor, Gemini CLI). It is the largest Claude-targeted skill collection in the tracked corpus and part of Composio's pattern of building vendor-specific skill aggregators (previously: awesome-codex-skills for OpenAI Codex, tracked 2026-04-28). The Composio App Automation layer — 78+ SaaS connectors bundled as installable skills — blurs the boundary between static instruction packs and active API integrations.

## What stands out immediately
- 1,000+ skills across 10 functional categories: Document Processing, Development & Code Tools, Data & Analysis, Business & Marketing, Communication & Writing, Creative & Media, Productivity & Organization, Collaboration & Project Management, Security & Systems, App Automation
- 78+ Composio App Automation connectors (Slack, GitHub, Salesforce, Notion, Datadog, Stripe, and others) — these invoke real authenticated APIs at execution time, not static prompts
- Explicitly cross-agent: Claude.ai, Claude Code, Cursor, Gemini CLI all listed
- 7.8k forks with community contribution guidelines — community-maintained at scale
- Largest single-vendor Claude-targeted collection: exceeds hesreallyhim/awesome-claude-code (48.7k★) and alirezarezvani/claude-skills (20k★)
- Previously referenced in passing in the SkillOpt doc (2026-07-09) as "already in the ecosystem" — no dedicated entry until now

## Why clawfit should care
The Composio connector layer constitutes a structural sub-type of L4b: skills that don't just prompt the agent but wire up authenticated SaaS API access. This affects clawfit's `network` and `setup_complexity` scoring for any tool deploying Composio-backed skills — those deployments inherit `network: online` and an OAuth-flow `setup_complexity: medium` dependency that static SKILL.md packs do not carry. A recommendation involving Composio-backed skills needs different network and complexity ratings than one using local SKILL.md files. No current field in `tools_registry.json` captures the `skill_integration_type: [static | composio-connector | mcp-server]` distinction.

## Preliminary interpretation
Current best reading:
- **Level 4b — Skills / Capabilities / Plugin layer (aggregator sub-type)**

Second Composio aggregator (after awesome-codex-skills, tracked 2026-04-28). Fourth large-scale community aggregator overall after mattpocock/skills (156k★), hesreallyhim/awesome-claude-code (48.7k★), and alirezarezvani/claude-skills (20k★). The Composio App Automation layer is a structural differentiator: not pure curation but an integration marketplace bundled as a skill catalog.

## Status
- Established position; first dedicated research-watch entry
- No registry entry: aggregator/catalog; no deployable tool with deterministic cost/latency data
- Schema gap noted: `skill_integration_type: [static | composio-connector | mcp-server]`
- Composio-aggregator sub-type promotion: one more independent Composio aggregator (e.g., awesome-gemini-skills) needed for canonical L4b sub-type entry
