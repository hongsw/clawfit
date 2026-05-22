# Research Watch: anthropics/claude-plugins-official

- Repo: https://github.com/anthropics/claude-plugins-official
- Also see: docs/research-watch/2026-05-21-andrej-karpathy-skills-behavioral-spec.md (first documented plugin-marketplace-distributed L3 entry); docs/research-watch/2026-05-06-anthropics-financial-services.md (1st-party Anthropic domain skill pack, candidate L4b sub-type)

## Why this is worth watching

This is the first official Anthropic-curated plugin marketplace integrated directly into the Claude Code CLI — not a third-party aggregator or community list. At #1 on GitHub Trending All Languages with 682 stars added in a single day and 22,355 total, it signals that Anthropic is taking direct ownership of the plugin distribution layer at scale. The scope is broader than any prior single skill pack: one repo aggregates internal Anthropic plugins alongside vetted external/community contributions, covering skills, MCP configs, slash commands, and agent definitions in a unified container format.

## What stands out immediately

- Plugin format is a composite container: `plugin.json` manifest plus optional `.mcp.json`, `commands/`, `agents/`, and `skills/` subdirectories — skills are a sub-component, not the top-level unit
- Install surface is first-class CLI: `/plugin install {name}@claude-plugins-official` and `/plugin > Discover` are native Claude Code commands, not external tooling
- Two-tier provenance model: Anthropic-internal plugins and `external_plugins` (third-party/community) coexist in the same repo under different trust lanes
- The repo is from the `anthropics` org directly — not a mirror, community fork, or affiliated vendor

## Why clawfit should care

The existing clawfit L4b classification handles individual domain skill packs (agency-agents, academic-research-skills, obsidian-skills). This repo is a layer above that — it is the distribution infrastructure that any of those packs can register into. The practical consequence is that clawfit's `setup_complexity` estimates for plugin-distributed tools (currently `low` by convention) are now anchored to a first-party channel rather than an informal community convention. Any future L4b entry that ships via this marketplace inherits a new provenance signal: Anthropic-curated vs. external-listed.

A secondary implication: the `.mcp.json` component inside the plugin format means L4c MCP servers and L4b skill packs can now share a single install path — the L4b/L4c boundary is softened at the distribution layer even if architectural roles remain distinct.

## Preliminary interpretation

Current best reading:
- **Level 4b — Capability / skill / plugin / tool-use layer** (platform-native distribution channel sub-type; not a skill pack itself but the marketplace container for skill packs and capability plugins)
- Secondary: weak L4c adjacency (`.mcp.json` support means MCP server configs are a first-class plugin artifact)
- This is the platform-native × general cell in the provenance × domain matrix noted in the `2026-05-06-anthropics-financial-services.md` entry — that doc flagged it as "already occupied by claude-plugins-official"; this research-watch doc gives it a standalone entry

## Status

- 22,355 stars, #1 GitHub Trending All Languages, official Anthropic org — exceeds registry threshold by star count and provenance
- Map mutation deferred: this repo is the distribution channel, not a runnable agent/LLM/hardware option fitting the current clawfit registry schema; same disposition as `anthropic-harness-link-map` and `anthropics/financial-services`
- Flag for reference-levels.md: the L4b section should note "platform-native distribution channel" as a named sub-type distinct from domain skill packs, skill managers, and generative skill synthesizers — single-sample rule does not block a note since the sub-type was already mentioned (without its own named entry) in the 2026-05-06 financial-services scan note
- Watch: whether third-party registry entries (academic-research-skills, agency-agents, CLI-Anything, obsidian-skills) list themselves here; adoption breadth would confirm this as the dominant Claude Code distribution channel
