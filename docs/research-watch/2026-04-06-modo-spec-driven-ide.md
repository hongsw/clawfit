# Research Watch: Modo — Spec-Driven Open-Source AI IDE

- Repo/Link: https://github.com/mohshomis/modo
- Source: Hacker News (Show HN, 15 points)

## Why this is worth watching
Modo enters the crowded AI IDE space (Cursor, Kiro, Windsurf) with a structurally different proposition: specification-first development. Rather than going prompt-to-code, the workflow is prompt → requirements → design → tasks → code. The architectural emphasis on planning artifacts stored in `.modo/specs/` as first-class project files represents a different philosophy than autocomplete-centric tools. Star count is minimal at observation (13; 2026-04-07 검증: 114, 포크 11, 커밋 2,781), but the architecture is analytically interesting as a signal of where thoughtful developers want AI IDEs to go.

## What stands out immediately
- Built on Void editor (VS Code fork), adding ~15 TypeScript services on top
- `.modo/specs/` stores structured planning documents: requirements, design, task checklists
- `.modo/steering/` files auto-inject project context into every agent interaction — similar to CLAUDE.md but IDE-native
- "Powers" system: bundled domain knowledge packs (TypeScript, React, testing, APIs, Docker)
- Agent hooks: JSON-based automation around lifecycle events (file change, tool use, task execution) with 10 event types
- Autopilot/Supervised toggle for autonomy control per session
- Subagent spawning for parallel subtask execution
- Inline "Run Task" buttons with persistent task state across sessions

## Why clawfit should care
Modo is a Level 1 candidate, but its spec-driven model is closer to Level 2/3 behavior packaged as an IDE. The "Powers" system mirrors the Level 4b skill-pack pattern. The steering files are a project-local SSOT variant (Level 3). This is a synthesis product — one tool trying to occupy Levels 1–3 simultaneously — which is worth tracking as a pattern. If the spec-driven workflow resonates, expect larger tools (Cursor, Kiro) to absorb it. clawfit may need a "workflow philosophy" axis (autocomplete-first vs. spec-first) in future agent evaluations.

## Preliminary interpretation

**Primary: Level 1 — Base runtime**

Level 1 is defined as "the main user-facing agent runtimes or primary product choices — the tools users most directly choose as their base environment." Modo is a full IDE (VS Code fork) that users install as their *primary* development environment. The user chooses Modo the way they choose Cursor or Claude Code — as the base surface from which all other agent activity occurs. No separate L1 tool is required underneath it.

**Why not Level 2 (meta wrapper / harness)?**
L2 tools *sit on top of an existing base agent* — they require a separate L1 underneath (e.g., oh-my-claudecode wraps Claude Code; deepagents SDK wraps an LLM runtime). Modo is self-contained: it IS the base agent. There is no prior L1 tool it orchestrates.

**Why not Level 3 (SSOT / governance)?**
L3 defines patterns for *sharing workflow rules across a team*, layered on top of existing runtimes. Modo's steering files and spec system are SSOT features *embedded within* a L1 surface — they are features of the product, not a standalone SSOT layer that works across multiple base runtimes.

**L2/L3 overlap (features, not classification)**
Modo embeds L2 behavior (subagent spawning, lifecycle hooks) and L3 behavior (steering files as per-project SSOT, Powers as skill packs) inside the IDE shell. These are features *within* a L1 surface. This "synthesis product" pattern — one tool trying to occupy L1–L3 simultaneously — is itself worth tracking as a potential signal that the levels are collapsing at the product layer.

## Status
- 13 stars → 114 (2026-04-07 검증, 커밋 2,781). Architecturally notable. Watch for sustained development or absorption by a larger project.
