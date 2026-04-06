---
# Research Watch: Claude Code marketplace ecosystem — skill discovery infrastructure matures

- claudemarketplaces.com: <https://claudemarketplaces.com/>
- Claude Code Skills Hub: <https://claudecodeplugins.io/>
- claude-code-plugins-plus-skills: <https://github.com/jeremylongshore/claude-code-plugins-plus-skills>

## Why this is worth watching
A **skill discovery infrastructure layer** has emerged around Claude Code: dedicated marketplaces, directories, and curated collections with ratings and install counts. This mirrors the trajectory of npm, VSCode extensions, and Homebrew — when a plugin ecosystem gets its own discovery layer, it has crossed a maturity threshold.

## What stands out immediately
- **claudemarketplaces.com:** 150+ skills with ratings (March 2026) — unofficial but structured marketplace
- **claudecodeplugins.io:** dedicated skills hub/directory
- **claude-code-plugins-plus-skills:** GitHub repo cataloging 340 plugins + 1,367 agent skills — largest known collection
- **Anthropic Frontend-Design Skill:** 277,000+ installs (March 2026) — single skill at app-store scale
- **Google gws:** Workspace API harness skill with built-in MCP server (March 2026)
- Security note: claude-mem audit flagged unauthenticated HTTP on port 37777 as HIGH risk — marketplace maturity requires security review norms

## Why clawfit should care
The discovery infrastructure layer is a new emergent category that doesn't fit neatly into clawfit's current Level 4 taxonomy:
- It is not a skill pack (Level 4b)
- It is not a tool-use extension (Level 4c)
- It functions more like a **Level 4 meta-layer**: enabling discoverability and governance for the skill ecosystem

clawfit should track this as an early signal of **skill ecosystem formalization** — the same transition npm made from scripts to package registry.

Also notable: 277k installs on a single skill proves that skill distribution at scale is already happening, not just a future possibility.

## Preliminary interpretation
- **Level 4b — Skill packs & skill managers** (discovery/registry infrastructure variant)
- Emerging subtype: **skill marketplaces / discovery registries** (distinct from skill managers like Chops)

## Status
- Medium-high priority. Marketplace maturity = ecosystem health signal.
- Security hygiene for skills (e.g., claude-mem port risk) may become a ranking criterion for clawfit.
