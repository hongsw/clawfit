# Research Watch: OpenAI Codex Record & Replay

- Repo/Link: https://developers.openai.com/codex/record-and-replay
- Source: GeekNews (OpenAI Codex Record & Replay — 관찰된 워크플로우를 재사용 가능한 스킬로 변환)

## Why this is worth watching
Record & Replay is a new Codex feature that converts demonstrated workflows into reusable skills through observation — the user performs a task once on macOS while Codex records it, then Codex analyzes the sequence and generates a skill with instructions, inputs, and verification steps. This is a new category of skill acquisition: instead of writing skill definitions manually (as Claude Code skills or oh-my-openagent plugins require), the agent learns from observation. It brings "end-user programming by demonstration" into the agent harness layer.

## What stands out immediately
- Observe-once, replay-anywhere: the user demonstrates the workflow naturally; Codex generates skill structure automatically
- Skill output includes: instruction text, parameterized inputs, and verification steps — not just a macro recording
- Targets workflows hard to describe in text: personal preferences, multi-step UI sequences, context-dependent actions
- Currently macOS-only; disabled in EEA/UK/Switzerland (Computer Use dependency)
- Fits into Codex's "plugins" architecture — skill becomes a callable plugin after generation
- Zero manual skill authoring: lowers the skill creation barrier dramatically compared to writing CLAUDE.md or system prompts

## Why clawfit should care
clawfit's skill-layer taxonomy (Level 3–4) currently assumes skills are manually authored by developers or teams. Record & Replay introduces a skill acquisition pathway that bypasses the authoring step. If this pattern generalizes (other harnesses add similar observe-and-replay features), clawfit's `setup_complexity` scoring for skill-enabled harnesses changes — what was `high` becomes `low` once the "demonstrate it" acquisition path exists. This is also a signal that OpenAI is competing with Claude Code's skill ecosystem at the acquisition layer, not just the execution layer.

## Preliminary interpretation
Current best reading:
- **Level 3 — Skill / Plugin / Instruction Layer** (primary; generates and stores reusable skill definitions)
- **Level 4c — Tool-use / action infrastructure** (secondary; relies on Computer Use to observe the underlying OS actions)

## Status
- New feature in active deployment (macOS, non-EEA). No independent star/adoption count available — feature embedded in Codex product. Track whether the observe-and-replay skill acquisition pattern spreads to Claude Code or open-source harnesses.
