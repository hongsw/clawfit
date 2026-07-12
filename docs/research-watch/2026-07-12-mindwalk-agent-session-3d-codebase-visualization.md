# Research Watch: Mindwalk — Agent session replay as 3D codebase map

- Repo: https://github.com/cosmtrek/mindwalk (⭐268)
- Source: Hacker News (135 points, Show HN — July 12, 2026)

## Why this is worth watching
Mindwalk addresses a concrete gap in the coding-agent toolchain: understanding *where* an agent actually looked before it responded. Agent sessions produce linear logs (tool calls, edits, outputs), but the spatial structure of which files were searched, read, and modified is not visible. Mindwalk replays that footprint as a 3D map of the codebase, animated as light traversing the repository graph. This is a novel angle on agent interpretability that sits in the human-interface layer rather than the model or harness layer.

## What stands out immediately
- v0.1.0 released July 11, 2026 — less than 24 hours old at time of this note; 135 HN upvotes suggest early traction
- Sessions are imported from Claude Code and Codex; session data is stored locally and never transmitted
- Built in Go (backend) + TypeScript/React + Three.js (3D frontend) — stack is web-native but locally hosted
- Visualization distinguishes file operations: search (dim glow), read (steady illumination), edit (bright pulse)
- Scope drift becomes visible: if the agent read files outside the plausible scope of a task, it shows spatially
- Designed as a debugging tool for prompt engineers and team leads auditing agent behavior
- No server component; runs as a local binary — privacy-preserving by architecture

## Why clawfit should care
This is a pure L6 signal — human-interface tooling for coding agents. It does not change *what* the agent does, only *how operators understand* what it did. The clawfit taxonomy currently does not have a strong entry for session observability / visualization at the interaction layer. If this pattern scales (multi-session diffs, cross-agent comparison), it could influence how clawfit surfaces trust/auditability signals in recommendations.

## Preliminary interpretation
Current best reading:
- **Level 6 — Human Interface Layer** (session visualization, agent observability from the user's perspective)
- Secondary: **Level 5 — Memory / Observability** (session log replay, footprint analysis)

## Claims to verify
- Whether the Claude Code session log format is stable enough to be reliably parsed across versions
- Whether "light traversal" animation conveys actionable signal or is primarily aesthetic
- Author activity and whether maintenance will continue past v0.1.0
- Whether scope drift detection is explicit (flagged) or only implicit (visible to trained eye)

## Status
- Too new and too low-starred for registry eligibility today (268 stars, v0.1.0)
- Worth re-evaluating at 1k stars; the HN response suggests genuine developer need
- No clawfit taxonomy changes warranted on this signal alone
