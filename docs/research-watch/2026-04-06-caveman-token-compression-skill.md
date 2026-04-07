# Research Watch: Caveman — Output Token Compression as a Claude Skill

- Repo/Link: https://github.com/JuliusBrussee/caveman
- Source: GeekNews, Hacker News (716 points, 313 comments)

## Why this is worth watching
Caveman achieves 65–75% output token reduction by constraining how Claude responds — not by filtering its inputs (rtk's approach) but by modifying its output style. The HN traction is strong (716 points, 313 comments), indicating this resonates with developers managing API cost at scale. It also introduces a structural claim: brevity constraints may improve benchmark accuracy on certain tasks, not just reduce cost.

## What stands out immediately
- Three intensity levels: Lite (removes filler, keeps grammar), Full (drops articles and connectives), Ultra (telegraphic, maximum compression)
- Activated via `/caveman` command or natural language; no CLI shim or shell hook required
- Technical terminology and code blocks are preserved exactly — compression targets prose, not data
- Eliminates high-frequency padding: "I'd be happy to help", "The reason this is happening is because", "Certainly!"
- Cited research suggests constrained brevity can improve accuracy on some benchmarks (claim to inspect — no direct benchmark link in README observed)
- Installs via `npx skills add JuliusBrussee/caveman` — confirms Level 4b skill distribution model
- 1.7k stars at 2026-04-06 기록; 2026-04-07 검증: 4.4k (포크 142, 커밋 32) — genuine adoption signal

## Why clawfit should care
Together with rtk, caveman represents a second vector on the token-cost axis: rtk compresses agent inputs (shell output); caveman compresses agent outputs (response prose). Both are economic interventions that reduce effective cost without changing the LLM or the task. clawfit's scoring model currently treats output token volume as fixed per task type. If both tools become common defaults, there is a case for a "session token efficiency modifier" that adjusts cost scores when these tools are in use. This also reinforces the Level 4b skill-pack pattern: cost-reduction behaviors packaged as installable skills.

## Preliminary interpretation

**Primary: Level 4b — Skill packs**

Level 4b is defined as tools that "add capabilities to agents rather than replacing the base runtime." Three criteria confirm L4b:
1. **Distribution mechanism**: installs via `npx skills add JuliusBrussee/caveman` — the canonical skill distribution channel, not a harness install or CLI tool.
2. **Activation pattern**: invoked via `/caveman` slash command per session — discrete, invocable, not a persistent wrapper.
3. **Scope**: adds one capability (output compression) without touching the model, the harness, or the base runtime. The agent can function identically without it.

**Why not Level 4c (tool-use infrastructure)?**
L4c tools mediate how agents *call external systems* (MCP servers, shell proxies, browser connectors). Caveman does not connect to external systems or wrap tool calls — it modifies the LLM's own prose output style via prompt convention. No external transport is involved.

**Why not Level 2 (meta wrapper / harness)?**
L2 tools sit on top of the base runtime and change *how the agent operates overall* (routing, multi-agent orchestration, lifecycle management). Caveman is a single-function skill, not a comprehensive operational wrapper.

## Status
- Medium-high priority. Strong HN reception. Watch whether this becomes a default in oh-my-* harnesses or recommended defaults in Level 2 systems.
