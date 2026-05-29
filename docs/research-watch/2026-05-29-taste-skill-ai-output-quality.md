# Research Watch: Taste-Skill — Proactive Stylistic Governance for AI-Generated Frontend

- Repo/Link: https://github.com/Leonxlnx/taste-skill
- Source: GitHub Trending #3 (all languages, 2026-05-29)

## Why this is worth watching

Taste-skill packages a dense set of frontend design constraints into a portable SKILL.md file that instructs the agent *before* output is generated — a proactive stylistic governance approach that differs structurally from reactive artifact-removal tools like stop-slop. Trending position and velocity on the same day as a parallel anti-slop signal suggest the "output quality enforcement" concern is crossing into mainstream adoption pressure. The SKILL.md distribution mechanism confirms it as an L4b skill pack rather than a harness or runtime modification.

## What stands out immediately

- Distributed via `npx skills add` — canonical L4b distribution path, same as caveman and dotnet/skills
- Core mechanism is a 50+ item pre-flight checklist the agent must run before emitting any code; failures are blocking ("the page is not done")
- Three tunable dials (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY, each 1–10) encode stylistic intent in the brief — not post-hoc filters
- Specific forbidden-pattern lists target "AI tells": generic placeholder names, startup-slop brand names, filler verbs ("elevate," "seamless"), em-dash usage (zero tolerance, most critical constraint)
- Hard layout bans encoded explicitly: no three-column equal feature cards, max one marquee per page, hero headline ≤2 lines — rules derived from observed AI repetition patterns (claim to inspect — "dedicated research" cited but not linked)
- Six aesthetic variants (soft-skill, minimalist-skill, brutalist-skill, gpt-taste, image-to-code-skill, redesign-skill) rather than a single style prescription; framework agnostic
- Technical constraints co-packaged: bans `window.addEventListener('scroll')`, mandates `useMotionValue` over `useState` for pointer values, restricts icon libraries to named sets (Phosphor, HugeIcons, Radix, Tabler)
- Reduced-motion accessibility (`prefers-reduced-motion`) required for any MOTION_INTENSITY > 3

## Why clawfit should care

Taste-skill represents a new L4b sub-type not yet named in the taxonomy: **output-quality governance skill pack** — proactive stylistic constraints on what the agent produces, as distinct from domain skill packs (which add capabilities) or compression skills (which reduce verbosity). The distinction from stop-slop matters: taste-skill is forward-prescriptive (sets design intent at brief time), while stop-slop is understood to be backward-corrective (removes artifacts post-generation). If both converge in adoption, the clawfit task taxonomy may need a `task: frontend-codegen` sub-type — distinct from `task: code-gen` — given the frontend-specific scope of these tools. The cross-vendor installation path (Cursor, Claude Code, Codex, Copilot, Windsurf all listed) confirms L4b SKILL.md portability remains the dominant distribution pattern at this layer.

## Preliminary interpretation

Current best reading:
- **Level 4b — Skill packs** (output-quality governance sub-type, proactive/stylistic variant)
- Frontend-specific scope; does not modify the agent runtime, harness, or base model
- SKILL.md distribution model confirmed; three-dial parameterization is notable as it encodes intent rather than just constraints

The "output-quality governance" L4b sub-type is a single-signal candidate (taste-skill). Stop-slop (tracked separately today) may constitute a second signal, but only if its mechanism is structurally distinct enough to confirm the same category rather than a different one. Sub-type formalization should wait for both research-watch docs to be complete before assessing whether the two-signal threshold is met.

## Status

- New entry. Hold for registry pending: (1) verification that "dedicated research" behind forbidden-pattern lists has identifiable sources; (2) confirmation that pre-flight checklist is enforced by agent parsing vs. agent honor-system; (3) second signal for "output-quality governance skill pack" sub-type (see stop-slop parallel). Monitor for harness-level adoption (oh-my-* systems picking this up as a default).
