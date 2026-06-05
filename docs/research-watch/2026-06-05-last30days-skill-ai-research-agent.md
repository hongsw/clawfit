# Research Watch: last30days-skill

- Repo/Link: https://github.com/mvanhorn/last30days-skill
- Source: GitHub Trending

## Why this is worth watching
`last30days-skill` is an AI agent skill that researches any topic across Reddit, X (Twitter), YouTube, and web sources, synthesizing what has happened in the last 30 days. At 27,555 stars, it is one of the highest-starred L4b skill pack entries by star count alone, signaling strong demand for time-windowed research synthesis as a standalone agent capability.

## What stands out immediately
- Multi-source research synthesis: Reddit, X, YouTube, web — covers the full informal knowledge surface
- Time-bounded retrieval: "last 30 days" framing makes it a standing query skill, not a one-shot lookup
- Pure Python skill; installs as a single SKILL.md or command pack
- High star velocity on day of trending suggests this fills a real workflow gap (staying current on a topic without manual browsing)
- Complements existing L4b domain packs (obsidian-skills, academic-research-skills) by covering informal/social sources the academic pack excludes

## Why clawfit should care
This is a strong confirming signal for the `task: research` + `role: researcher/exec` intersection in the skill-pack layer. It's architecturally simple (no orchestration, no governance), so it's an L4b primary. More importantly, the star count puts it above several existing registry entries — if confirmed, it's a registry candidate for `task: research` profiles where `data_sensitivity` is `public` or `internal` (social media research implies public-facing data). Also notable: the multi-source design (Reddit + X + YouTube) makes it `network: online` only and not `data_sensitivity: confidential` compatible.

## Preliminary interpretation
Current best reading:
- **Level 4b — Domain/capability skill pack (primary)**: Time-windowed multi-source research synthesis skill

## Status
- 27,555 stars exceeds registry promotion threshold. Hold pending: (1) verification that stars are genuine and not trending-day spike; (2) confirmation that the skill pack installs cleanly via SKILL.md; (3) confirm it doesn't duplicate `anthropic-knowledge-work-plugins` research capability.
- Registry candidate for `task: research` + `role: researcher` + `network: online` profiles.
