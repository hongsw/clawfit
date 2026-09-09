# Research Watch: openai/plugins — Codex Plugin Ecosystem Reference Repository

- Repo: https://github.com/openai/plugins (⭐6,128)
- Source: GitHub Trending (today, +505 stars)

## Why this is worth watching
`openai/plugins` is OpenAI's official curated example repository for the Codex plugin format. Each plugin ships a `.codex-plugin/plugin.json` manifest alongside skills, agents, and MCP configurations. With plugins already published for Figma, Notion, iOS, macOS, web development, Expo, Netlify, Remotion, and Google Slides, this is OpenAI's answer to the L4 capability layer — and it is structurally distinct from the already-tracked `openai/skills` (which is a flat skills catalog, not a plugin manifest format).

## What stands out immediately
- Official OpenAI repo, not a community fork — signals formal productization of the Codex plugin format
- Plugin structure: `.codex-plugin/plugin.json` manifest + skills + agents + MCP configs in one package
- Platform integrations already present: Figma (design), Notion (productivity), iOS/macOS (Apple platform dev), web, Expo (mobile), Netlify (deploy), Remotion (video), Google Slides (presentations)
- 6.1k stars with +505 today — sustained momentum, not a one-day viral spike
- Each plugin is a self-contained unit combining capability declaration, agent behavior, and MCP tooling

## Why clawfit should care
The `codex-plugin/plugin.json` manifest format is structurally analogous to what `aas-stack.json` is for AAS v17 skills (tracked 2026-09-08) — a machine-readable capability declaration that bundles skills, agents, and MCP configs as a deployable unit. If this format becomes the de facto standard for Codex plugins, it is the L4 capability layer for OpenAI's agent ecosystem in the same way `anthropics/skills` is for Claude Code's.

clawfit currently tracks OpenAI's skill ecosystem via `openai/skills` (tracked 2026-07-02). The plugin format adds a richer composition mechanism: a plugin can contain multiple skills, declare agent behavior, and specify MCP server configs. This is the bundled-capability pattern that AAS v17 (2026-09-08) also promotes, and it is now appearing across both major agent ecosystems (OpenAI Codex + AAS). A `plugin_format: [aas | codex | claude-skill | mcp-only]` axis would help clawfit distinguish capability ecosystems.

## Preliminary interpretation
- **Level 4 — Capabilities / Skills / MCP** (primary: Codex plugin format and reference implementations)
- **Level 2 — Harness / Wrapper** (secondary: agents defined within plugins configure agent behavior)

The format positions Codex as the agent runtime while plugins extend its capabilities — clean L4 primary classification.

## Claims to verify
- Plugin format stability — is `codex-plugin/plugin.json` a versioned, stable spec or an evolving internal format?
- MCP integration — are the MCP configs in each plugin using standard MCP or a Codex-specific dialect?
- License — not mentioned in the content fetched; verify before enterprise adoption guidance
- Plugin community adoption — 6.1k stars on OpenAI's repo doesn't mean the format itself has community plugins; check if third-party plugins exist using the format

## Status
- New — tracking as formal L4 signal for OpenAI's Codex plugin ecosystem
- Star count: 6,128 (above 100-star threshold; below 5k for registry, actually above)
- Registry eligibility: blocked (plugin ecosystem catalog, no agent/LLM/hardware schema slot)
