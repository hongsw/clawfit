# Research Watch: GenericAgent — Self-Evolving Agent with Skill Tree

- Repo/Link: https://github.com/lsdefine/GenericAgent
- Source: GitHub Trending (2026-04-17, +872 stars today, 2,753★ total)

## Why this is worth watching
GenericAgent seeds itself with a 3,300-line Python codebase and grows a skill tree autonomously — the agent writes new tools, tests them, and persists them across sessions. Claims full system control with 6× less token consumption than comparable agents. This is a concrete implementation of the "self-modifying skill acquisition" pattern that Meta HyperAgents explored at the research level (2026-04-13 research-watch).

## What stands out immediately
- Skill tree: agent builds new capabilities incrementally from a minimal seed
- 6× token efficiency claim vs. comparable autonomous agents
- Python; minimal dependencies; ships as a single runnable module
- "Full system control" framing — agent operates filesystem, shell, network
- Rapid growth (+872 stars in one day) suggests practitioner curiosity is high

## Why clawfit should care
GenericAgent represents a new Level 1 sub-type: an agent that grows its own skill library rather than consuming pre-packaged ones. This sits between rowboat (memory-native) and Hermes Agent (adaptive runtime) — it is tool-acquisition-native. If this pattern stabilizes, clawfit's Level 1 taxonomy may need a `self-evolving_runtime` sub-type. The 6× token efficiency claim, if substantiated, is also directly relevant to cost scoring. Low star count (2,753★) means this is early-signal; revisit at 10k★ before registry entry.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtimes** (self-evolving / skill-acquisition sub-type)

## Status
- Early signal: 2,753★, impressive concept; watch for 10k★ threshold before registry
