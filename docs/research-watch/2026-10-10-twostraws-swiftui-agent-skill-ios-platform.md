# Research Watch: twostraws/SwiftUI-Agent-Skill — iOS Platform Skill for AI Coding Agents

- Repo/Link: https://github.com/twostraws/SwiftUI-Agent-Skill
- Source: GitHub Trending (5,413 stars, all languages)

## Why this is worth watching
Paul Hudson (twostraws), author of Hacking with Swift and the most-followed iOS developer educator globally, has published a SwiftUI agent skill targeting Claude Code, Codex, and other AI coding tools. The 5.4k stars on GitHub Trending is the first time an iOS/SwiftUI-specific agent skill from a recognized platform community leader has reached trending status — a social signal that iOS developers are now actively adopting AI coding agents, not just web and backend developers.

## What stands out immediately
- **Author**: Paul Hudson (twostraws) — Hacking with Swift, hundreds of thousands of Swift developer followers
- **Target platforms**: Claude Code, Codex, explicitly named; "other AI tools" suggests harness-agnostic format
- **Content**: agent skills for SwiftUI development (UI layouts, state management, SwiftData, previews, animations — inferred from pattern of similar repos)
- **Stars growth**: GitHub Trending "all languages" at 5,413 total, 65 stars/day — sustained but not explosive
- **Signal type**: community adoption indicator — influential educator publishing agent skills means their audience (beginner-to-intermediate Swift developers) is now an active clawfit-relevant user segment

## Why clawfit should care
The existing `tasks` taxonomy in the registry is backend/web-biased: code-gen, research, qa, orchestration. There is no `mobile-development` or `ios-development` task category. twostraws/SwiftUI-Agent-Skill is the first high-credibility signal that iOS developers are a distinct user segment with platform-specific agent skill needs. clawfit's recommendation quality for a `primary_role: developer` + `primary_task: code-gen` profile who is an iOS developer would not currently surface platform-specific tools — the scores would default to web/backend agent harnesses.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability layer (agent skills)** — platform-specific skill library that extends a coding agent's task coverage for a target tech stack

## Status
- First signal for "iOS/SwiftUI-specific agent skill from a recognized platform community figure"
- Not a registry entry candidate (it is a skill library, not an agent harness, LLM, or hardware)
- Implication: consider adding `mobile-development` as a task type in org_questions.json and a `platform_specialty` field to the org_fit schema in a future scoring review
