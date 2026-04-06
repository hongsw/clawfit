# Research Watch: Modo — Spec-Driven Open-Source AI IDE

- Repo/Link: https://github.com/mohshomis/modo
- Source: Hacker News (Show HN, 15 points)

## Why this is worth watching
Modo enters the crowded AI IDE space (Cursor, Kiro, Windsurf) with a structurally different proposition: specification-first development. Rather than going prompt-to-code, the workflow is prompt → requirements → design → tasks → code. The architectural emphasis on planning artifacts stored in `.modo/specs/` as first-class project files represents a different philosophy than autocomplete-centric tools. Star count is minimal (13), but the architecture is analytically interesting as a signal of where thoughtful developers want AI IDEs to go.

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
Current best reading:
- **Level 1 — Base runtime** (full IDE surface, primary user-facing environment)
- Strong Level 2/3 overlap: steering files (SSOT), Powers (skill packs), hooks (orchestration)

## Status
- Low adoption currently (13 stars). Architecturally notable. Watch for sustained development or absorption by a larger project.
