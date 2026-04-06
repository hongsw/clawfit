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
- 1.7k stars; not a one-off meme — genuine adoption signal

## Why clawfit should care
Together with rtk, caveman represents a second vector on the token-cost axis: rtk compresses agent inputs (shell output); caveman compresses agent outputs (response prose). Both are economic interventions that reduce effective cost without changing the LLM or the task. clawfit's scoring model currently treats output token volume as fixed per task type. If both tools become common defaults, there is a case for a "session token efficiency modifier" that adjusts cost scores when these tools are in use. This also reinforces the Level 4b skill-pack pattern: cost-reduction behaviors packaged as installable skills.

## Preliminary interpretation
Current best reading:
- **Level 4b — Skill packs** (output-style modifier packaged as an installable Claude skill)
- Adjacent to Level 4c (tool-use infrastructure) but operates via prompt convention, not a tool call

## Status
- Medium-high priority. Strong HN reception. Watch whether this becomes a default in oh-my-* harnesses or recommended defaults in Level 2 systems.
