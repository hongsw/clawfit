# Research Watch: ViMax — Agentic Video Generation

- Repo/Link: https://github.com/HKUDS/ViMax
- Source: GitHub Trending (#17, 6,044★, Python)

## Why this is worth watching

ViMax is a multi-agent video generation framework from HKUDS (same team as DeepTutor, already tracked at L6). It orchestrates specialized agents — Director, Screenwriter, Producer, and Video Generator — to transform narrative input (ideas, scripts, novels) into complete video output with storyboard planning, character consistency, and sequential image synthesis. At 6k★ it exceeds the 5k registry threshold.

## What stands out immediately

- MIT, Python 100%, from HKUDS research lab
- Domain-specialized multi-agent pipeline with 6+ distinct agents (script, storyboard, visual, reference image, consistency, synthesis)
- Accepts long-form narrative input (novels → video); targets episodic content production
- No coding agent or developer workflow integration — pure creative/production vertical
- No MCP server, no Claude Code plugin interface documented
- Closely related to the domain-specialized agent cluster (security: Shannon/Strix; game dev: Claude-Code-Game-Studios; finance: Dexter/TradingAgents)

## Why clawfit should care

ViMax expands the domain-specialized agent cluster into **creative content production** — a new vertical alongside security, game development, and finance. However, it targets an end-user creative audience (independent creators, writers) rather than developers or knowledge workers, which is outside the current clawfit org persona set. The workflow is isolated from the agent tooling ecosystem (no Claude Code, no MCP, no harness integration). The HKUDS research lab provenance (also DeepTutor) is notable — second tool from this team.

## Preliminary interpretation

Current best reading:
- **Level 1 — Domain-Specialized Base Agent** (creative/video production vertical)
- No secondary level: no harness, no memory, no capability extension

## Status

- 6,044★, MIT, Python — meets star threshold
- Map mutation deferred: creative/video production is outside clawfit's current org persona scope (developer, researcher, PM, exec); `task: video-gen` does not exist in current schema; no developer-workflow integration documented
- Would require adding a `content-creation` or `video-gen` task type to clawfit schema before registry entry is actionable
- Watch: whether HKUDS adds Claude Code plugin or MCP integration; whether a developer-oriented use case (e.g., automated explainer video from code) emerges
