---
# Research Watch: Skill layer consolidation — Chops, skills-cleaner, Impeccable, K-Skill

- Chops: <https://github.com/Shpigford/chops>
- skills-cleaner: <https://github.com/amebahead/skills-cleaner>
- Impeccable: <https://github.com/pbakaus/impeccable>
- K-Skill: <https://github.com/NomaDamas/k-skill>

## Why this is worth watching
Four separate projects appeared in the same weekly digest, all targeting the **skill/plugin management layer**. This cluster is evidence that Level 4 (capability/skill/plugin layer) is rapidly maturing from individual skill packs into a managed ecosystem requiring discovery, deduplication, and lifecycle tooling.

## What stands out immediately

**Chops** (macOS app):
- Manages skills across Claude Code, Cursor, Codex, Windsurf, Amp simultaneously
- Single UI for cross-agent skill lifecycle — boilerplate gen, full-text search
- First multi-agent skill manager with a native desktop UI

**skills-cleaner** (Claude plugin):
- Lists, searches, and removes duplicate skills in `.claude/plugin/`
- Interactive comparison and deduplication
- Addresses skill sprawl — a problem that only exists because skill adoption is high

**Impeccable** (design skill pack):
- 20 design commands across 7 domains (layout, spacing, color, typography, etc.)
- Workflow-oriented: check → align → refine
- Domain-specific skill vocabulary — "design language for AI assistants"

**K-Skill** (Korean-localized skills):
- SRT reservations, Seoul subway info, KBO baseball, lottery — Korean service automation
- Shows skill packs becoming **locale/culture-specific**

## Why clawfit should care
The skill layer is fragmenting into subtypes that clawfit's Level 4 doesn't yet distinguish:
1. **Skill managers** (Chops, skills-cleaner) — lifecycle/discovery tools
2. **Domain skill packs** (Impeccable — design; K-Skill — Korean services)
3. **Tool-use extensions** (Expect, cq) — capability augmentation

This cluster warrants a Level 4 taxonomy refinement in `docs/reference-levels.md`.

## Preliminary interpretation
- All four: **Level 4 — Capability / skill / plugin / tool-use layer**
- Emerging subtypes within Level 4 need explicit naming

## Status
- Medium-high priority as a cluster signal.
- Recommend ecosystem-mapper update Level 4 in reference-levels.md to distinguish skill managers from skill packs.
