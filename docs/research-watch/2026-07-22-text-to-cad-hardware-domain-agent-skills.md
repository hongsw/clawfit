# Research Watch: text-to-cad — Vertical Domain Agent Skill Pack for CAD and Hardware Design

- Repo: https://github.com/earthtojake/text-to-cad (⭐9,090)
- Also see: https://github.com/addyosmani/agent-skills (general coding skill pack, tracked 2026-04-08)

## Why this is worth watching
text-to-cad is a structured library of agent skills targeting CAD generation, robot kinematics, and hardware fabrication workflows — the first physical-world-domain skill pack in the clawfit scan corpus. At 9,090 stars with 1k forks and an active Discord, adoption is confirmed beyond curiosity-phase. Provider-native plugin installation for Claude Code and Codex is documented in the README, making this a runtime-integration signal rather than an isolated prompt library.

## What stands out immediately
- Ten discrete skill categories: text/image-to-CAD (STEP, STL, 3MF, GLB export), DXF 2D drawings, URDF/SRDF robot structure files, SDF simulation environments, G-code with real slicer CLI integration, Bambu Labs 3D printer control, SendCutSend fabrication validation, and Implicit CAD via GLSL raymarching (experimental)
- Built on Build123d + OpenCASCADE — the same geometry kernel used in professional FreeCAD pipelines; output is production-grade geometry, not simplified shapes
- Fabrication handoff is first-class: SendCutSend skill validates parts against manufacturing constraints before service submission; G-code generation invokes actual slicer executables, not wrappers
- Install path documented as "Skills CLI or provider-native plugins (Codex, Claude Code)" — integration mechanism (MCP server vs. plugin manifest vs. prompt injection) is unspecified and a claim to inspect
- 10 benchmark CAD models (gears, impellers, stairs) ship with the repo for regression testing agent output quality

## Why clawfit should care
addyosmani/agent-skills (tracked 2026-04-08, 76k stars) established the L4 agent skill pack pattern for the software development domain. text-to-cad is the second independent signal at this layer but covers an entirely non-overlapping capability space: physical hardware design. These are not expansions of a single general skill set — they are separate domain skill packs targeting the same runtime host class. The two-signal condition for **vertical domain agent skill packs** as an L4 sub-pattern is now met.

For clawfit's recommendation engine, this exposes `task: cad-design` / `task: hardware-design` as task dimensions absent from agents.json. The fabrication handoff skills (G-code, Bambu, SendCutSend) are also the first observed case of an L4 skill pack producing outputs consumed directly by physical manufacturing infrastructure — an L4→L7 handoff pattern not previously tracked in the scan corpus.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability / Skill / Plugin layer** (primary: agent skill pack extending coding agent runtimes into CAD, robotics, and fabrication domains)
- Fabrication output targets (G-code, printer APIs, cutting services) reach into **Level 7** as downstream consumers, not as the tool's architectural home

## Claims to inspect
- "Provider-native plugins (Codex, Claude Code)": integration mechanism unspecified — MCP server, plugin manifest, or prompt injection each carries different runtime-version coupling risk; needs verification

## Status
- First signal; 9,090 stars with 1k forks and active Discord confirm adoption traction above noise threshold
- Two-signal condition met for "vertical domain agent skill packs" alongside addyosmani/agent-skills; "when in doubt" rule applies given star-count asymmetry (9k vs. 76k) — flag for reference-levels.md next update cycle, no canonical change this run
- Schema gap: `task: cad-design`; no registry entry until hardware/CAD task dimension is added to agents.json taxonomy
