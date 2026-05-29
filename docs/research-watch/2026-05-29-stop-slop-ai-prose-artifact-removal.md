# Research Watch: stop-slop — AI Prose Artifact Removal Skill

- Repo/Link: https://github.com/hardikpandya/stop-slop
- Source: GitHub Trending #4 (all languages, 2026-05-29), 6,395 stars, +761 today

## Why this is worth watching
stop-slop reached 6,395 stars on its first trending day — above the 5k registry threshold — with a narrow, executable contract: a SKILL.md file that eliminates identifiable AI-prose artifacts from agent output. The velocity is notable given the repo is a behavioral-spec file rather than runnable software, placing it in the same tier as `andrej-karpathy-skills` (25k★, L3) and other high-star CLAUDE.md/SKILL.md repos. A parallel signal (taste-skill, 26k★) surfaced the same day, making this the first two-signal day for output-quality governance as a distinct L4b sub-type candidate.

## What stands out immediately
- **SKILL.md delivery:** Standard format; installable into Claude Code, Claude Projects, Cursor, and API system prompts without modification
- **Reactive, not proactive framing:** Operates as a named removal pass over existing text — distinct from taste-skill, which proactively enforces stylistic identity at generation time
- **Concrete artifact taxonomy:** Three reference files enumerate banned phrases, structural clichés, and sentence-level rules (no Wh- starters, no em dashes, active voice required); operationally specific, not vague style advice
- **Scoring rubric embedded:** Five-dimension quality gate (directness, rhythm, trust, authenticity, density) rated 1–10; scores below 35/50 trigger a revision pass — gives the skill a programmatic trigger condition rather than leaving invocation to the user's discretion
- **MIT license:** No governance blockers
- **469 forks:** Community signal of active adaptation, not passive starring

## Why clawfit should care
stop-slop and taste-skill together form the first two-signal cluster for output-quality governance at L4b. The structural distinction matters for clawfit's recommendation logic: taste-skill shapes what the agent writes; stop-slop audits and rewrites what the agent already produced. These are architecturally different invocation patterns — proactive style constraint vs. reactive artifact removal pass. If clawfit tracks both as a single "output quality" category, it will underfit profiles that need reactive post-processing (e.g., content-heavy publishing workflows) vs. those that need proactive stylistic identity (e.g., brand voice enforcement).

A `task: content-writing` or `task: prose-qa` task type is implicated. Neither currently exists in the clawfit schema.

## Preliminary interpretation
Current best reading:
- **Level 4b — Skill / behavioral spec, output-quality governance sub-type (reactive artifact removal)**
- Distinct from taste-skill's proactive variant; together these two signals establish a two-cell matrix within the sub-type: `reactive removal` vs. `proactive enforcement`
- No L3 signal: stop-slop does not govern agent workflow or session lifecycle; it governs a single output artifact

## Status
- New — first observed 2026-05-29; above 5k registry threshold; registry entry held pending: (1) second scan confirming star count is not trending-amplified; (2) schema addition of a prose/content-writing task type; (3) paired analysis against taste-skill to determine whether these belong as a single registry entry or two
