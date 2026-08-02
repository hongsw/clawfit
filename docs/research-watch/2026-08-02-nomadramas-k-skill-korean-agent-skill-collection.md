# Research Watch: NomaDamas/k-skill — Korean Agent Skill Collection

- Repo/Link: https://github.com/NomaDamas/k-skill
- Source: GitHub Trending (2026-08-02, +53 stars today, 6,726 total)

## Why this is worth watching
A curated, community-maintained skill collection targeting Korean-language agent workflows. At 6,726 stars with active daily velocity, it is the first geographically-localized L4b skill library signal in this corpus — distinct from all prior entries which are English-first. This matters for clawfit because skill compatibility with local-language use cases is a dimension not currently modeled.

## What stands out immediately
- JavaScript implementation, cross-agent compatible (Claude Code, Cursor, etc.)
- Korean-language skill targets: document summarization, legal research, Korean API connectors
- Community-contributed structure resembling `awesome-claude-skills` but locale-specific
- No MCP dependency — pure skill-manifest format for agent skill invocation
- 6,726 stars at +53/day trajectory suggests consistent organic growth, not a trending spike

## Why clawfit should care
This is the third-signal for "locale-specific domain skill packs" (after `korean-law-mcp` tracked 2026-04-07 and `NomaDamas` k-skill appearing today). It signals that the L4b skill layer is fracturing by language/locale as well as by domain. The `tasks` dimension in clawfit currently has no `locale` axis — recommending skill packs to Korean-language orgs without this would produce incorrect results. Schema gap candidate: `locale: [global | ko | ja | zh | ...]`.

## Preliminary interpretation
Current best reading:
- **Level 4b — Domain/Locale Skill Pack** (locale-specific community skill aggregator for Korean-language agent workflows)

## Status
- First dedicated signal; monitoring for second non-Korean locale-specific pack to confirm the pattern
