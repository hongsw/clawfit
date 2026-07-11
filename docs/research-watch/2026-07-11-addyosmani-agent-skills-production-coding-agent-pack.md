# Research Watch: addyosmani/agent-skills — Production-Grade Coding Agent Skills

- Repo/Link: https://github.com/addyosmani/agent-skills
- Source: GitHub Trending (76,807 ⭐, #4 today)

## Why this is worth watching
Addy Osmani (Google Chrome DevRel) releasing a "production-grade engineering skills" pack for AI coding agents signals mainstream credibility for the skill-layer pattern. At 76k stars this is a top-10 signal by raw star count in the entire tracked ecosystem. It was referenced in passing in the 2026-07-06 awesome-claude-code audit but never received a dedicated research-watch entry.

## What stands out immediately
- "Production-grade" positioning: not a toy/prototype pack, explicitly engineered for real workloads
- Cross-agent design: works with Claude Code, Cursor, Codex and other coding agents
- High-authority author from Google Chrome DevRel community
- JavaScript-dominant (ecosystem targeting front-end / web engineers)
- Now at 76.8k stars, up from 70k referenced in the 2026-07-06 audit — +6.8k in under a week

## Why clawfit should care
Skills packs are a core recommendation axis in clawfit: a developer with `primary_task: code-gen` and `primary_role: developer` should surface high-quality skill packs. `agent-skills` is the highest-star cross-agent skill pack and directly maps to `tasks: code-gen, qa` and `roles: developer`. Registry candidate. The cross-agent portability also matters for scoring: unlike Claude Code–specific skill packs, this tool works across multiple harnesses — relevant to `network: online` + multi-harness organizations.

## Preliminary interpretation
Current best reading:
- **Level 4b — Skill / capability extension layer** (primary)
- Cross-agent portability makes this a reference point for L2/L4b boundary comparisons

## Status
- Previously referenced in 2026-07-06 audit context but without a dedicated doc
- First dedicated signal 2026-07-11 (76.8k stars, well above 50k exceptional threshold)
- Registry candidate: added to `tools_registry.json` as `addyosmani/agent-skills`
- Map mutation: together with mattpocock/skills (164k★), "engineer-authored cross-agent skill pack" is now a two-signal sub-type warranting a canonical L4b entry in reference-levels.md
