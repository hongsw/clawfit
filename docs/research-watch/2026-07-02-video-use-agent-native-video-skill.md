# Research Watch: browser-use/video-use — Agent-Native Video Editing Skill

- Repo/Link: https://github.com/browser-use/video-use
- Source: GitHub Trending (July 2026, +693 today)

## Why this is worth watching
video-use is a 13,204★ skill module that lets AI agents (Claude Code primary target) edit video through natural language — without ever processing raw video frames. It reached this star count from approximately 8–9k on June 30 (+5k in roughly 48 hours), which explains why it was held at the June 30 scan ("domain-specific, below threshold") and now clearly crosses the threshold. It is part of the browser-use ecosystem (same GitHub org) but is architecturally a standalone skill, not an orchestration harness.

## What stands out immediately
- Text-first architecture: LLM reads audio transcripts + visual composites, never raw frames — token-efficient by design
- Covers: filler-word removal, silence cutting, color grading, audio fades, subtitle burning, animation overlays
- Self-evaluation loop: agent renders, checks output, re-renders if needed
- Installs as a skill module alongside an existing agent runtime
- 13,204★, 1,700 forks; MIT license; Python

## Why clawfit should care
This is the second high-signal creative-production L4 tool (after OpenMontage, L2, tracked 2026-06-21). It is architecturally distinct: OpenMontage is an L2 harness orchestrating 14 video providers; video-use is a standalone L4b skill installed into any existing agent. The two together confirm that `content-creation` is becoming a stable clawfit task type with tools at multiple layers. Schema watch: `content-creation` task type now has four independent signals (ViMax, HyperFrames, OpenMontage, video-use).

## Preliminary interpretation
Current best reading:
- **Level 4b — Domain Skill Pack** (video/creative-production sub-type; skill module, not a runtime)
- Secondary: **Level 4c weak** (integrates FFmpeg as an action surface)

## Status
- Second signal for agent-native video editing (after OpenMontage which is L2 harness, not L4 skill)
- Registry candidate pending `content-creation` task type schema addition
- Promotion criterion: `content-creation` added to schema AND 15k★ (current trajectory: 2–3 days)
