# Research Watch: google-labs-code/design.md — Official Format Specification with Tooling

- Repo: https://github.com/google-labs-code/design.md
- Also see: docs/research-watch/2026-04-06-awesome-design-md.md, docs/research-watch/2026-05-22-stitch-skills-google-labs-agent-skills.md

## Why this is worth watching
This is the specification layer that the awesome-design-md watch (2026-04-06) assumed existed but couldn't point to: a Google Labs-authored canonical format definition for DESIGN.md, with a validating CLI and multi-format export pipeline. The distinction matters — awesome-design-md is a curated library of DESIGN.md instances; this repo defines what a valid instance is. With 17.3k stars at v0.3.0 alpha, adoption is running ahead of format stability.

## What stands out immediately
- Format combines YAML front matter (color tokens, typography, spacing) with Markdown prose (design rationale) — agents can parse both layers independently
- CLI ships three distinct functions: validation, file-to-file comparison, and export; not a single monolithic command
- Linter enforces token-reference integrity, WCAG contrast ratios, and structural completeness — these are machine-checkable constraints, not style guidance
- Export targets: Tailwind v3, Tailwind v4, W3C Design Tokens Format Module; v4 and DTFM targets indicate the spec is tracking active upstream format churn
- Google Labs authorship — not an officially supported Google product; claim to inspect whether this is a stepping-stone toward formal standardization or a research artifact
- MIT-equivalent license; v0.3.0 alpha signals the schema is not yet stable

## Why clawfit should care
The 2026-04-06 watch established DESIGN.md as an L3 SSOT pattern. This repo adds something new: a validation and export toolchain that can run in CI. That shifts the artifact from a convention (copy a file, agents read it) toward enforced infrastructure (lint fails the build if tokens are invalid). If the export pipeline normalizes, clawfit's registry may need to distinguish between agents that consume raw DESIGN.md prose versus those that consume compiled Tailwind/DTFM output — a capability distinction relevant to scoring UI-heavy task profiles.

## Preliminary interpretation
Current best reading:
- **Level 3 — Team harness / executable SSOT / governance layer** — the format specification itself is governance infrastructure; the linter enforces it mechanically
- **Level 4 secondary (weak)** — the export CLI functions as a capability tool: it transforms a design spec into a framework-consumable artifact, which is skill-adjacent
- The Level 3 classification aligns with the prior awesome-design-md ruling; the difference is this repo owns the grammar, not just instances of it

## Status
- First signal for google-labs-code/design.md as distinct from the awesome-design-md library; tracked separately
- Schema stability concern: v0.3.0 alpha — format may shift before any registry entry would be appropriate
- Watch trigger: v1.0 release or W3C DTFM export reaching stable parity would warrant promotion to reference consideration
