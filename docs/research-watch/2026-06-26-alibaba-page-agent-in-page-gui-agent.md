# Research Watch: alibaba/page-agent — In-Page JavaScript GUI Agent

- Repo/Link: https://github.com/alibaba/page-agent
- Source: GitHub Trending — 19,791★

## Why this is worth watching
Alibaba's `page-agent` is a JavaScript-native, in-page GUI agent that controls web interfaces through natural language. Unlike Playwright-based agents (which drive a browser from the outside), page-agent runs *inside* the page as a JavaScript module, giving it direct DOM access without a separate browser automation process. At 19.8k★ it is one of the highest-starred browser-control agent libraries tracked this cycle.

## What stands out immediately
- In-page execution model: no external browser driver or CDP connection required
- Natural language → DOM action translation happening inside the page context
- TypeScript; works in any JavaScript-compatible environment
- Architecturally distinct from existing L1 computer-use agents (trycua/cua, chrome-devtools-mcp)
- From Alibaba, same team behind open-code-review (already tracked 2026-06-22)

## Why clawfit should care
Current registry has computer-use as an implicit axis but no dedicated in-page browser agent category. page-agent proposes a third computer-use deployment sub-type: (1) OS-level computer use (Claude Computer Use), (2) external browser automation (chrome-devtools-mcp, trycua/cua), and (3) in-page embedded agent. The in-page model has lower latency and no browser driver dependency, making it viable for `network: online` + `latency: low` profiles that current computer-use tools can't satisfy. Relevant to clawfit's QA and research task scoring.

## Preliminary interpretation
Current best reading:
- **Level 1 — Specialized base agent** (in-page web control sub-type)
- **Level 4c secondary** (tool-use/action layer: DOM manipulation as the action surface)

## Status
- 19,791★ — exceeds registry threshold. Second signal for in-page browser automation sub-type needed before map entry.
- Registry candidate: `tasks: [qa, research]`, `roles: [developer, pm]`, `network: online`, `setup_complexity: low`.
- Promotion criterion: second independent in-page browser agent project OR confirmed adoption as a Claude Code/Codex skill.
