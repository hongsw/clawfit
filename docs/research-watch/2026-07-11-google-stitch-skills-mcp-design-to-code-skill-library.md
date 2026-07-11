# Research Watch: google-labs-code/stitch-skills — MCP-Native Design-to-Code Skill Library

- Repo/Link: https://github.com/google-labs-code/stitch-skills
- Source: GitHub Trending (6,735 ⭐, #15 today)

## Why this is worth watching
Google Labs shipping a skill library tied to its Stitch MCP server creates a new "MCP-native skill pack" pattern: skills designed to consume an MCP server's design APIs rather than generic CLI or web calls. This is architecturally distinct from Claude Code skill packs — it demonstrates that MCP servers and skill packs are converging into a single distribution unit, not two separate layers.

## What stands out immediately
- Three skill suites: `stitch-design`, `stitch-build`, `stitch-utilities` — modular by workflow phase
- Follows the Agent Skills open standard (SKILL.md + scripts + knowledge bases + examples)
- Works across multiple coding agents: Claude Code, Cursor, Codex — cross-agent portability
- 929 forks: high contribution velocity for a new Google Labs repo
- Design-to-code coverage: text/image → UI screen → React component → React Native

## Why clawfit should care
The MCP+skill-pack convergence pattern could change how clawfit should score tools. A tool that bundles an MCP capability server with skill definitions is more locked-in (higher `setup_complexity`) but more powerful for its specific task domain. For `primary_task: code-gen` + `primary_role: developer` with a design workflow, stitch-skills would rank above generic skill packs. Registry candidate at 6.7k stars (above 5k threshold). Also signals `task: design-to-code` as a potential new schema value.

## Preliminary interpretation
Current best reading:
- **Level 4b — Skill / capability extension layer** (primary)
- **Level 4c — MCP capability server** (secondary, via Stitch MCP dependency)

## Status
- First signal 2026-07-11 (6.7k stars, above 5k registry threshold)
- Registry candidate: `stitch-skills` — `tasks: code-gen`, `network: online`, `setup_complexity: medium`
- Schema watch: `task: design-to-code`; `mcp_dependent: true/false` for skill packs
- No map mutation: first signal; "MCP-native skill pack" sub-type needs a second signal before promotion
