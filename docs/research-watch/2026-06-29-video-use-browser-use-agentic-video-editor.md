# Research Watch: video-use — Agentic Video Editing Skill from browser-use

- Repo/Link: https://github.com/browser-use/video-use
- Source: GitHub Trending

## Why this is worth watching
The browser-use team — already canonical in the agent harness space for browser automation — has shipped a video editing skill designed to be called by coding agents like Claude Code. With 11k stars and 1.5k forks on debut day, it signals that domain-specific agent skills (not just code/browser/data) are reaching production-quality adoption velocity. This is the clearest signal yet that agentic video production is graduating from research demos to developer tooling.

## What stands out immediately
- **Text-first pipeline**: transcribes audio via ElevenLabs for word-level timestamps, then edits on the transcript — no frame-dumping, minimal token usage
- **Autonomous editing operations**: filler-word removal, color grading, audio fade at cuts, subtitle burn-in, animation overlays (HyperFrames/Remotion/Manim/PIL)
- **Self-evaluation loop**: renders cuts, evaluates boundaries, retries — a mini-agent loop baked into the skill
- **Session memory**: persists project state in files across agent sessions
- **12k★ / 1.5k forks**: fastest-growing agent skill in this scan cycle

## Why clawfit should care
video-use extends the browser-use lineage (browser automation → video editing) and demonstrates that L4 agent skills are consolidating around established harness brands. The multi-modal pipeline (voice → transcript → edit → render) is a template clawfit should track when scoring tools for `summarization`, `content-creation`, or multimedia output tasks. HyperFrames (already tracked 2026-04-29) is now a dependency in another high-signal tool.

## Preliminary interpretation
Current best reading:
- **Level 4b — Agent Skill / Domain Capability Layer** (primary)
- **Level 2 secondary** — designed to drop into a coding agent (Claude Code) as a first-class plugin

## Status
- First signal — 2026-06-29
- Promote to registry when: 20k★ OR second major video-agent harness adopts the same text-first transcript architecture
- Registry candidate: `tasks: [summarization, content-creation]`, `roles: [developer, pm]`, `network: online`, `setup_complexity: medium`
