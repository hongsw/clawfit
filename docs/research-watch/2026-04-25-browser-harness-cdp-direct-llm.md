# Research Watch: Browser Harness — Direct CDP Browser Automation

- Repo/Link: https://github.com/browser-use/browser-harness
- Source: Hacker News (Show HN, 77 pts, 33 comments)

## Why this is worth watching
Browser Harness is from the team behind `browser-use` (the original browser-use framework), but this time they reversed direction: instead of wrapping CDP with Playwright-style APIs, they give the LLM a raw Chrome DevTools Protocol connection plus a `helpers.py`. When steps fail, the agent reads the errors, self-edits helpers.py, and retries mid-task — no framework, no recipes, no rails.

## What stands out immediately
- **Self-healing by design**: failures are recovery signals, not hard stops — the LLM writes what's missing
- **Anti-framework stance**: explicit rejection of framework-mediated browser control in favor of raw CDP access
- **From browser-use**: provenance from the team that built the most-watched open-source browser agent layer gives this credibility
- **LLM freedom over predictability**: explicitly trades determinism (Libretto pattern) for maximum task range

## Why clawfit should care
This is a direct complement to `chrome-devtools-mcp` (Level 4c, 35k★) and a competitor to Libretto (deterministic automation) and Playwright-over-MCP patterns. For profiles with `qa` or `research` tasks and `online` network where full LLM autonomy over browser state is acceptable, this is a candidate Level 4c entry. It also anchors a new sub-type axis: **deterministic vs. self-healing browser automation** — relevant when scoring governance-heavy vs. velocity-heavy profiles.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infrastructure** (browser automation sub-type, self-healing variant)

## Status
- Tracking. 77 HN pts at launch (2026-04-17). Revisit when star count is available.
