# Research Watch: Domain Expert Adoption of Coding Agents — Terence Tao Signal

- Repo/Link: https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/
- Source: Hacker News (#10, 399 points, 114 comments)

## Why this is worth watching

Terence Tao (Fields Medal 2006, UCLA) documented using Claude Code to port ~24 Java 1.0 applets from 1999 to modern JavaScript in hours and to build new mathematical visualization tools. The signal is the persona, not the tool: a research scientist — not a software engineer — applying a Level 2 harness with an explicit, articulable risk tolerance framework.

## What stands out immediately

- Tool named: Claude Code — terminal-based agent reading full codebases, executing shell, iterating on observations
- Task type 1 — legacy code porting: 24 applets ported in hours; one output bug found; agent identified two bugs in Tao's original 1999 Java code that Tao had missed
- Task type 2 — domain-specific visualization: new apps built from scratch (Lorentz transformation drawing tool, Gilbreath conjecture visualizer)
- Risk tolerance stated explicitly: applets are "secondary visual aids rather than critical components of a mathematical argument" — acceptable risk calibrated by function, not by blind trust
- Development pattern: "vibe coding" across multi-hour iterative sessions; Tao retains design and domain judgment; "lower-level implementation details largely automated away"

## Why clawfit should care

Clawfit's task taxonomy (`qa`, `code-gen`, `summarization`, `data-analysis`, `research`) has no entry for `legacy-porting` or `domain-visualization`. Both have distinct scoring profiles: legacy porting prioritizes correctness over speed; visualization prioritizes iteration velocity over production stability. Tao's risk stratification ("secondary aid" vs. "critical argument") directly maps to a `fault_tolerance` or `criticality` axis absent from current scoring. Most structurally: `roles: researcher` is in the schema but its evidence base is thin — this is the strongest single-author adoption signal for that persona in the tracked ecosystem. Clawfit should treat `researcher` as a first-class role with its own filter logic, not a synonym for `developer` on research tasks.

## Preliminary interpretation

Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layers** (adoption signal for L2 harness tools by a research-scientist persona)
- Secondary: task taxonomy gaps (`legacy-porting`, `domain-visualization`) and scoring axis gap (`fault_tolerance`)

## Status

- Adoption signal only; no registry entry warranted
- Flag: `roles: researcher` warrants a dedicated user-persona note; `task: legacy-porting` is a candidate for the next schema revision
