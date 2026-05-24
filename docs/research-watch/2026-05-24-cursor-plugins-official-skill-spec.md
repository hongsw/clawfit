# Research Watch: cursor/plugins

- Repo: https://github.com/cursor/plugins
- Also see: docs/research-watch/2026-05-22-claude-plugins-official-anthropic-marketplace.md (structurally parallel — Anthropic's first-party plugin spec for Claude Code)

## Why this is worth watching

At 674 total stars with 95 added today (#8 GitHub Trending TypeScript), this is the official Cursor IDE plugin specification — not a community aggregator or third-party standard. It defines a standardized manifest format and marketplace infrastructure for distributing agent skills, MCP server configs, and IDE rules from a single plugin container. The structural parallel to `anthropics/claude-plugins-official` is immediate: two major IDE/agent vendors are now shipping first-party, incompatible plugin distribution specs within days of each other, establishing competing distribution channels at the same layer.

## What stands out immediately

- Plugin manifest path is `.cursor-plugin/plugin.json` — distinct from Claude Code's `plugin.json` layout; compatibility between the two formats is not claimed
- Three artifact types per plugin: `skills/` directory (agent-executable tasks in SKILL.md format), `mcp.json` (MCP server config), and `rules` (IDE-level behavioral constraints)
- Skills are authored in SKILL.md format — the same cross-vendor portable format now confirmed as a stable axis (five signals as of 2026-05-23)
- Explicit design emphasis on "patterns for designing CLIs that coding agents can run reliably" — the plugin spec is opinionated about agent-callable CLI ergonomics, not just packaging
- Official `cursor` org — first-party to the IDE, not a community proxy or Labs experiment

## Why clawfit should care

The `anthropics/claude-plugins-official` research-watch doc noted the L4b/L4c boundary is softened at the distribution layer because a single plugin container can carry both skill packs (L4b) and MCP server configs (L4c). `cursor/plugins` replicates that exact same collapse pattern — and it does so in a competing first-party format. The practical consequence is that the clawfit ecosystem now has two parallel distribution channels for L4b/L4c capabilities, each anchored to a specific IDE: Claude Code → `claude-plugins-official`; Cursor → `cursor/plugins`. Skill packs that want cross-IDE reach (cf. agency-agents, dotnet/skills, andrej-karpathy-skills) will face a dual-packaging burden unless SKILL.md portability mediates the gap.

The `rules` artifact type inside a Cursor plugin is worth flagging separately: IDE-level behavioral rules are L3 territory (governing how the agent behaves), co-packaged inside what is architecturally a L4 distribution container. This is the same L3/L4 co-packaging pattern seen in `anthropics/claude-plugins-official` (which also carries agent definitions and behavioral constraints). Both specs are blurring the L3/L4 boundary at the distribution layer.

## Preliminary interpretation

Current best reading:
- **Level 4b — Capability / skill / plugin / tool-use layer** (platform-native distribution channel sub-type): Cursor's first-party parallel to `claude-plugins-official`; same sub-type, different IDE anchor. Occupies the `(platform-native × IDE-specific) × (Cursor)` cell in the provenance × domain matrix, which `claude-plugins-official` occupies for the Claude Code IDE.
- Secondary: weak L4c adjacency (`mcp.json` is a first-class plugin artifact, same pattern as `claude-plugins-official`)
- Secondary: weak L3 adjacency (`rules` artifact type co-packages behavioral constraints inside the L4 distribution container)

The "platform-native distribution channel" sub-type at L4b, established by `claude-plugins-official`, now has a second independent instance in `cursor/plugins`. This is the second signal for the sub-type. Per the taxonomy, the sub-type was already named and stable from `claude-plugins-official`; `cursor/plugins` reinforces it and extends its scope from "Claude Code IDE" to a multi-IDE pattern — but does not occupy the same cell. Two cells in the matrix are now occupied by distinct first-party IDE plugin specs.

## Status

- 674 stars total, 95 today, official `cursor` org — below the 5k registry threshold at capture; velocity is the signal
- No map mutation applied: sub-type ("platform-native distribution channel") is already named and stable at L4b; `cursor/plugins` is the second instance but in a distinct IDE cell — no new sub-type definition required
- Flag: if a third major IDE (VS Code / Copilot, Windsurf, Gemini CLI) ships a first-party plugin spec in this format within 4 weeks, the pattern should be noted as a cross-IDE standardization signal and the L4b sub-type entry should record all three anchors explicitly
- Watch: whether SKILL.md portability effectively bridges `cursor/plugins` and `claude-plugins-official` in practice, or whether dual-packaging becomes required for cross-IDE skill packs — this directly affects `setup_complexity` estimates for any L4b entry targeting both IDEs
