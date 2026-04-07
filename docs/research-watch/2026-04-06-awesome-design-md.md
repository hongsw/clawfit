# Research Watch: awesome-design-md — DESIGN.md as AI Agent UI Specification

- Repo/Link: https://github.com/VoltAgent/awesome-design-md
- Source: GeekNews

## Why this is worth watching
The project proposes DESIGN.md as a structured, plain-text design system document that AI agents read before generating UI — a direct parallel to CLAUDE.md (executable instructions) but applied to visual design. At 15.9k stars at launch (2026-04-06 기준; 2026-04-07 검증: 24.6k, 포크 3k, 커밋 18) and 55+ ready-to-use design systems (검증: 58개) (Claude, Cursor, Linear, Stripe, Vercel…), it has crossed from concept into actual adoption. This is a new sub-pattern of the SSOT layer: not workflow rules, but design-system rules embedded in the repo for agent consumption.

## What stands out immediately
- 55+ curated DESIGN.md files extracted from popular sites' actual design languages
- Each file encodes: color palettes, typography, component specs, layout principles, spacing scales, shadow/elevation, responsive behavior, agent prompt guides
- Paired with preview HTML files for visual validation
- Installs into projects like a skill — copy and reference; no tooling required
- Compatible with Google Stitch and general Claude/Codex agents
- Eliminates the Figma-export step as design system distribution mechanism
- Category coverage: AI platforms, developer tools, infrastructure, consumer products

## Why clawfit should care
DESIGN.md represents a new dimension of the SSOT layer (Level 3). Current Level 3 tracking focuses on workflow and governance rules (CLAUDE.md, AGENTS.md, oh-my-agent). DESIGN.md extends the SSOT pattern into the visual/UI domain: it is executable design documentation that agents read to generate consistent output. If this pattern standardizes, agent configuration may need three SSOT files: CLAUDE.md (workflow), AGENTS.md (cross-platform governance), DESIGN.md (visual output norms). That changes how clawfit models agent suitability for UI-heavy tasks.

## Preliminary interpretation

**Primary: Level 3 — Team harness / executable SSOT / governance layer**

Level 3 is defined as "executable SSOT — humans read it as a workflow or operating guide, agents read it as executable instructions." DESIGN.md satisfies this criterion exactly: a designer reads it as a design system reference, an agent reads it as binding styling constraints before generating UI. The purpose is to govern agent output norms across an entire project, not to add a one-time capability — which is the governance function that defines L3.

**Why not Level 4b (skill packs)?**
L4b tools add a *discrete, invocable capability* to an agent (a command, an action). DESIGN.md does not add a new command — it constrains how the agent produces *all* UI output. The correct analogy is CLAUDE.md (L3 governance), not `/impeccable` (L4b skill command).

**Secondary: Level 4b**
The files *can* be loaded like a skill — copy-and-reference, no tooling required — so the distribution mechanism overlaps with L4b. But the function (persistent design-system governance) is L3.

## Status
- High signal. 15.9k stars at launch → 24.6k (2026-04-07 검증). Tracking for Level 3 expansion and potential reference-levels entry.
