# Research Watch: SimpleEnglish — Agent Skill for ASD-STE100 Documentation Quality

- Repo/Link: https://github.com/AminBlg/SimpleEnglish
- Source: Hacker News ("Agent Skill to Force Docs in ASD-STE100 Simplified Technical English")

## Why this is worth watching
First agent skill specifically targeting documentation quality via a structured constraint set (ASD-STE100, 1983 aerospace standard). Reduces STE violations by 72.9% across six Claude models in benchmarks. Ships as a cross-agent pluggable skill with no external dependencies, compatible with Claude Code, Cursor, Copilot, Codex, and Gemini CLI — representing the first published "style standards enforcement" skill category.

## What stands out immediately
- Targets technical writing artifacts agents frequently produce badly: error messages, runbooks, release notes, incident reports
- Constraint-based approach (max sentence length, active voice, no hedging language) outperforms prompt-softening attempts
- MIT license, no dependencies — installable via skill CLI or direct system prompt paste
- Benchmarked evaluation methodology (before/after examples across 6 models) distinguishes it from most undocumented skills
- Addresses localization cost reduction and clarity for non-native English readers — real enterprise value driver

## Why clawfit should care
Extends the L4 skill taxonomy: `code-gen` and `research` skills are well-covered; documentation quality skills are not. `governance_need: hard` organizations (regulated industries, aerospace, defense) have existing compliance requirements around technical writing — this skill directly serves that persona. Could inform a new `documentation_standard` dimension in org_fit or a `compliance` task tag.

## Preliminary interpretation
- **Level 4b — Agent Skill** (documentation quality / style enforcement layer)

## Status
- First signal; small repo but benchmarked claims and HN pickup. Monitor for star trajectory. No registry entry yet: single-skill, no inference cost or latency data; would fit a future `skills_registry` if one is added.
