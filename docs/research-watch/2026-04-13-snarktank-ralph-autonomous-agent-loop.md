# Research Watch: snarktank/ralph — Autonomous Agent Loop for PRD Execution

- Repo/Link: https://github.com/snarktank/ralph
- Source: GitHub Trending (+463 stars today, 15,908 total)

## Why this is worth watching
snarktank/ralph is an autonomous AI agent loop written in TypeScript that **executes PRD (Product Requirements Document) items iteratively** — 15k+ stars with daily momentum on GitHub Trending. This is distinct from frankbria/ralph-claude-code (Claude-specific wrapper) and Th0rgal/open-ralph-wiggum (multi-backend loop controller): snarktank/ralph appears to be the highest-starred independent implementation of the Ralph autonomous loop pattern.

## What stands out immediately
- TypeScript (modern, IDE-compatible), 15.9k stars — well beyond the existing ralph ecosystem entries
- PRD-first execution model: structured requirements documents drive the agent loop
- "Iterative execution" framing emphasizes loop discipline over one-shot generation
- Connects the Ralph methodology (planning → iterative execution → backpressure) to a mainstream tool adoption
- Positioned as an autonomous loop, not just a Claude Code wrapper

## Why clawfit should care
The ralph methodology family now has three distinct implementations tracked in the registry (ralph-claude-code, open-ralph-wiggum, plus the methodology signal). snarktank/ralph at 15k+ stars is now the dominant star count in this family — larger than both existing entries combined. It represents validation that PRD-driven autonomous loops are crossing mainstream developer adoption. For clawfit, this reinforces the Level 2 "harness / autonomous loop" category and may warrant its own registry entry given the star count signal.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrapper / autonomous agent loop**
- PRD-first execution; solo-to-small-team developer target

## Status
- High-traction signal — evaluate for registry addition alongside existing ralph entries
