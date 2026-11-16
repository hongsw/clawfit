# Research Watch: elementalsouls/Claude-BugHunter

- Repo/Link: https://github.com/elementalsouls/Claude-BugHunter
- Source: GitHub Trending

## Why this is worth watching
Claude-BugHunter is a Claude Code skill bundle specifically for bug hunting and external red-team work, with 6,417 total stars and 98 stars today. It represents the first confirmed example of a **security-domain skill pack** in the L4b category — extending the domain_skill_pack taxonomy (pm-skills Jun-10, scientific-agent-skills Aug-04, claude-trading-skills Nov-15) with a fourth vertical: security/red-team. The red-team framing is explicit in the description ("external red-team work"), which raises distinct governance questions.

## What stands out immediately
- Security and bug-hunting framing, not general QA
- "External red-team work" language implies use against targets beyond the user's own codebase
- Python-based skill bundle for Claude Code; 6,417 stars — highest-starred security skill pack seen
- Explicit red-team positioning distinguishes it from generic `qa` or `security-testing` task tags
- No governance or scope-limiting mechanism mentioned in the description

## Why clawfit should care
clawfit currently has `security-testing` as a task type but no nuanced distinction between internal testing (owns the target) and external red-team work (may not own the target). Claude-BugHunter is the first signal that security skill packs are fragmenting along that axis. The `governance_need` scoring dimension should distinguish these: `security-testing` with `governance_need: none` is a different risk profile from red-team skill packs. Additionally, the recent Lovable credential exposure signal (Nov-15) makes security-aware scoring more urgent.

## Preliminary interpretation
Current best reading:
- **Level 4b — Domain Skill Pack** (security/red-team vertical, fourth confirmed domain)
- Security tool governance signal crosses L3 (policy layer)

## Status
- First scan: 2026-11-16
- Registry action: deferred — security skill packs require a `scope` or `target_model` annotation not yet in registry schema; adding without it would produce misleading recommendations for `governance_need: hard` profiles
- 📡 Note: fourth domain_skill_pack signal (pm, scientific, finance, security); canonical L4b sub-type now has four domain confirmations; recommend adding `skill_domain: [pm | scientific | finance | security | locale-specific | general]` field to registry schema
- 📡 Note: `security-testing` task tag likely needs a sub-type annotation (`scope: internal | red-team`) to avoid recommending red-team tools to `governance_need: hard` orgs for internal QA
