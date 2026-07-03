# Research Watch: Chrome DevTools MCP

- Repo/Link: https://github.com/ChromeDevTools/chrome-devtools-mcp
- Source: GitHub Trending

## Why this is worth watching
The official Chrome DevTools team has shipped an MCP server that exposes 40+ browser inspection and automation tools to coding agents. With 45.1K stars and 2.9K forks, this is the first authoritative (Google-originated) capability layer for browser-native agent tasks — agents can now run performance traces, capture network traffic, and automate DOM interactions without a bespoke integration.

## What stands out immediately
- 40+ MCP tools across input automation, navigation, performance, network inspection, and memory debugging
- Puppeteer-backed reliable automation with automatic result waiting (no flaky polling)
- Explicit named support for Claude, Cursor, and GitHub Copilot as consumers
- Auto-starts Chrome or attaches to an existing instance; zero manual browser setup
- Source-mapped stack traces available to agents via the DevTools protocol

## Why clawfit should care
This adds a credible **browser-debugging** capability axis that clawfit's current tool taxonomy does not model. It is an L4c tool-integration artifact produced by the Chrome team itself — not a third-party wrapper — which changes the trust and stability calculus significantly. Agents recommending Playwright-based tooling for web tasks should be compared against this as an alternative. A `browser_debug` task type (or an `automation` sub-tag under `code-gen`) would surface this in recommendations.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool Integration / Capability Layer** (MCP server surface, official browser tooling for agents)

## Status
- First signal; 45.1K★ (above threshold). Promotion criterion: ≥1 L1/L2 base agent or harness documents chrome-devtools-mcp as a default browser-inspection integration, OR a `browser-debug` task type is added to the clawfit schema and this tool is a natural fit candidate.
