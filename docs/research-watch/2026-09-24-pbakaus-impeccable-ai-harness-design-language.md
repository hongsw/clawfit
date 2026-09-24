# Research Watch: pbakaus/impeccable — Design Language for AI Harness Interfaces

- Repo/Link: https://github.com/pbakaus/impeccable
- Source: GitHub Trending (today, all languages)

## Why this is worth watching
Impeccable is a JavaScript design language specification and component library explicitly targeted at AI harness interfaces — not general UI, but the specific interaction surfaces that sit between a human and an agent harness. With 70,325 stars on GitHub Trending today, it is one of the highest-star harness-adjacent projects to appear in this scan. A design language that wins this kind of adoption shapes how the harness layer presents itself to users, which has downstream effects on tooling choices.

## What stands out immediately
- Framed as "design language for AI harness interfaces" — explicitly agent-layer scope, not general-purpose UI
- JavaScript (likely web-component-based given the description and language choice)
- 70K+ stars indicates broad practitioner buy-in, not just hype
- Positions the harness interface as a named concern distinct from both the agent runtime and the end-user app
- No dependency on a specific agent runtime — designed to be runtime-agnostic

## Why clawfit should care
clawfit models the agent stack in 7 layers; L6 (human interface / UX layer) has been the least populated canonical level. Impeccable is a signal that the agent harness UX layer is maturing into a separable design discipline with its own standards. If impeccable becomes a de-facto interface contract for harness UIs, it will influence which harnesses are evaluated as "polished enough" for enterprise adoption — a factor clawfit's `setup_complexity` and `roles` metadata would need to reflect. It also raises the question of whether clawfit should add a `ui_design_system` field to its scoring axes.

## Preliminary interpretation
Current best reading:
- **Level 6 — Human Interface / UX Layer** (primary)
- **Level 2 — Harness/SDK** (secondary, as a harness UI contract)

## Status
- First signal — monitoring
- Star count above 5k registry threshold; registry entry deferred pending confirmation of license, npm/install story, and deterministic cost/latency data (not applicable; tracking at ecosystem level)
- Pattern: first dedicated "harness interface design language" as a named category
