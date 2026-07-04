# Research Watch: alirezarezvani/claude-skills — Cross-Agent Skill Pack Aggregator

- Repo: https://github.com/alirezarezvani/claude-skills (⭐20,052)
- Source: GitHub Trending Python (2026-07-04); cross-listed in all-language trending

## Why this is worth watching

alirezarezvani/claude-skills is a community-authored aggregator of 337 skills for Claude Code, Codex, Gemini CLI, Cursor, and 8 other coding agents. The star count (20k+) places it among the highest-rated community skill packs in this scan series, behind mattpocock/skills (156k★, tracked 2026-04-26) and hesreallyhim/awesome-claude-code (48k★). The distinguishing claim is explicit cross-agent portability: while most tracked skill packs are Claude Code-specific, this one claims first-class support for Codex, Gemini CLI, and Cursor. It was last pushed 2026-07-03 (yesterday) and covers functional areas that most skill packs do not address: marketing, compliance, C-level advisory, and commercial/finance operations.

## What stands out immediately

- **Cross-agent portability:** Explicitly targets 10+ coding agents (Claude Code, Codex, Gemini CLI, Cursor among named ones); most tracked skill repos are single-runtime
- **337 skills across non-engineering domains:** Marketing, compliance, C-level advisory, business operations, commercial/finance — extends skills into professional workflows beyond development
- **30+ bundled agents and 70+ custom commands:** The distinction between "skill" and "agent" in the repo's own terms suggests a richer packaging model than a flat skill list
- **Published GitHub Pages site:** `has_pages: true` indicates documentation investment beyond a raw markdown dump
- **2,747 forks:** High fork count relative to stars (1:7 ratio) suggests users are customizing rather than just starring; active consumer pattern
- **Created Oct 2025:** 9 months of development; recent push (July 3, 2026) indicates live maintenance
- **Categorically broader than most skill packs:** The business/compliance framing overlaps with the "org_fit" metadata axis in clawfit's current registry — potentially more enterprise-relevant than typical engineering-focused packs

## Why clawfit should care

This is the third large-scale community skill pack tracked (after mattpocock/skills and hesreallyhim/awesome-claude-code). Together they confirm a pattern: the skills layer (L4b) is accumulating community-built aggregators with 10k–150k stars, all growing rapidly. This is structurally different from official/vendor skill packs (dotnet/skills, microsoft/skills-for-fabric, anthropic cybersecurity pack).

The cross-agent claim is architecturally significant for clawfit: if skills are portable across agents, then clawfit's recommendations could theoretically decouple skill selection from agent selection — recommending `(agent=X, skills_pack=Y)` where Y is not agent-specific. This is a schema design question: should clawfit track skill packs as first-class registry entries with their own compatibility matrix?

The non-engineering domain coverage (marketing, finance, C-level) is the most distinctive differentiator here. No tracked skill pack has reached this breadth of professional scope. Whether the quality of compliance or C-level advisory skills holds up to scrutiny is a separate question, but the framing suggests a user population beyond developer teams.

## Preliminary interpretation

Current best reading:
- **Level 4b primary — Skill / capability / tool-use layer** (multi-agent, cross-runtime skills aggregator)
- **Level 6 secondary** (non-engineering professional workflow skills, extends into human-facing advisory domains)
- Not L2: does not orchestrate agents; provides installable skills that agents consume

## Claims to verify

- Cross-agent compatibility claim: verify that skills are structurally portable (YAML/markdown format without Claude Code-specific tooling hooks) versus just stated as compatible
- Skill quality in compliance/legal/finance domains — high error cost in these categories
- Whether the "30+ agents" claim refers to packaged agent configurations or templates
- Active maintenance pace: is the July 3 push a content addition or only a README update?

## Status

- 20,052★ above registry threshold; schema would need a "skills_pack" entry type to include this class of entry — different from agent, LLM, and hardware categories
- Third large community skill aggregator tracked (after mattpocock/skills, hesreallyhim/awesome-claude-code); cross-agent portability and non-engineering domain coverage are the differentiators
- Promotion criterion: clawfit registry schema gains a `skill_pack` or `capability_pack` entry type with cross-agent compatibility fields
