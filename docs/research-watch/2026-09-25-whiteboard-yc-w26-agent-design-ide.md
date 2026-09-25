# Research Watch: Whiteboard — Open-Source IDE for Agent-Human Design Collaboration

- Repo: https://github.com/devdotfast/whiteboard (⭐1,100)
- Source: Hacker News "Show HN" front page (374 pts, 202 comments, Sept 25, 2026)
- Backing: YC W26

## Why this is worth watching

Whiteboard (YC W26) is an open-source desktop IDE built on CodeOSS that gives AI coding agents an SDK to draw on a shared canvas alongside human developers — sequence diagrams, ERDs, and agent decision traces that link directly to source code. The 374 HN points (a top-3 story today) reflects genuine practitioner interest, not just novelty. The YC W26 batch backing indicates this received institutional validation during the recent cohort.

The target problem is well-defined: when a coding agent makes 400 autonomous decisions across 200 files, there is currently no surface that lets a human understand what it was *thinking* — only what it did. Whiteboard attempts to solve the observability gap at the agent-human interface layer, not through logs or traces in a monitoring dashboard, but through a first-class design canvas embedded in the IDE itself.

## What stands out immediately

- Agents write to a shared canvas via an SDK — they can draw diagrams, annotate reasoning, and signal decision points; humans can click diagram elements to jump to source code
- Semantic diff viewer built in Rust that filters noise from agent-generated changes, surfacing only semantically meaningful diffs rather than reformatting or whitespace changes
- Decision logging captures agent reasoning at decision points — not just tool calls, not just file diffs, but the decision rationale
- Built on CodeOSS (VSCode fork) with LSP support — not a standalone tool but a full editor replacement
- WASM-based plugin system for extensibility — third-party plugins can add custom visualization types
- Local-first architecture: no cloud sync of agent reasoning or canvas state
- Explicitly multi-harness: connects to Claude Code, Codex, and other harnesses via their respective SDKs

## Why clawfit should care

The Whiteboard signal is primarily an L6 (Human Interface) observation, but its implications are cross-layer. It introduces a new interface category: **agent-side visualization** — not a dashboard for humans to inspect past agent actions, but a live shared surface that agents write to as they work. This is structurally different from agent observability tools (L5) and from agent IDEs that merely display agent output.

For clawfit's scoring model, Whiteboard suggests the `statefulness: session` dimension should include a sub-type for "agent-legible session context" — shared workspaces where agents can express reasoning state in a form the human can interrogate. If this pattern proliferates, `task: code-gen` profiles may benefit from a `collaboration_surface` axis.

The WASM plugin system and multi-harness SDK are indicators this is designed as infrastructure rather than a point product.

## Preliminary interpretation

Current best reading:
- **Level 6 — Human Interface Layer** (primary: agent-human design canvas embedded in IDE)
- **Level 2 — Harness/Wrapper Layer** (secondary: agent SDK for writing to shared visualization surface)
- **Level 5 — Observability/Evaluation Layer** (weak secondary: decision logging and semantic diff)

## Claims to verify

- Whether the agent SDK is available standalone or only through the Whiteboard IDE
- Whether decision logging is retroactive (log replay) or real-time (live agent writing)
- Whether the Rust semantic diff viewer is open-source separately or only accessible via Whiteboard
- Whether WASM plugins can be shared as a marketplace or are local-only
- Actual star count trajectory — 1,100 stars on launch day could plateau or continue growing

## Status

- Above 100-star threshold (1,100★); below 5k registry threshold
- YC W26 backing; 374 HN points on Show HN is strong practitioner signal
- **First tracked tool** in "agent-side visualization canvas embedded in IDE" sub-category
- Complements pbakaus/impeccable (2026-09-24, L6 design language for harnesses) — both are L6 signals about making agent interaction surfaces legible and intentional; two signals from different organizations; watch for a third to confirm "agent interface legibility" as a canonical L6 sub-type
- No deterministic cost/latency data; no registry entry warranted yet
