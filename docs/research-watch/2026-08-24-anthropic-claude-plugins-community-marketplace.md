# Research Watch: claude-plugins-community — Official Community Plugin Marketplace for Claude Cowork and Claude Code

- Repo: https://github.com/anthropics/claude-plugins-community (⭐1,275)
- Source: GitHub Trending Python (August 24, 2026)

## Why this is worth watching

Anthropic is operating a curated, security-screened community plugin marketplace for both Claude Cowork and Claude Code. The read-only mirror (synced nightly from an internal review pipeline) establishes a formal approval and distribution channel for third-party capabilities. With 1,275 stars and +490 in a single day, it is drawing immediate attention — the star spike likely reflects developers discovering that the marketplace is real, not experimental.

The companion repositories (`anthropics/claude-plugins-official`, `anthropics/knowledge-work-plugins`) establish a three-tier structure: official Anthropic plugins, role-specific knowledge-work plugins, and community plugins. This mirrors the Chrome Extension / VS Code Extension marketplace architecture but is specific to Claude's harness layer.

## What stands out immediately

- **Security-screened before distribution**: automated security scanning is a gate before any community plugin reaches the nightly mirror — explicit curation policy distinguishes this from npm or a raw GitHub topic
- **Dual target**: Claude Cowork (team collaboration) and Claude Code (developer coding agent) share the same marketplace, implying plugins must satisfy cross-context compatibility or be scoped to one target
- **`claude plugin marketplace add`**: a named CLI command for adding community registries — implies the plugin system is designed for multiple registries, not just Anthropic's; third-party registries could emerge
- **`.claude-plugin/marketplace.json`**: the canonical registry format is a single JSON file with the full plugin list — structured, machine-readable, and inspectable; same approach as KEYWORDS.md or package.json manifests
- **Apache-2.0 license**: permissive license on the repository itself (not necessarily the plugins); signals ecosystem-building intent
- **Submission via web form, not PRs**: `clau.de/plugin-directory-submission` — Anthropic controls the review funnel; community cannot bypass the approval process via pull request

## Why clawfit should care

This is L4 (capabilities/skills layer) infrastructure at the platform level. clawfit's registry currently lists agents as monolithic entries; it does not model the plugin/capability dimension that determines what an agent can actually do after installation. A `plugin_marketplace: [none | official | community | open-registry]` field would let clawfit distinguish agents with curated marketplace support from those with ad-hoc skill packs or no extension story.

**Two-signal context**: Agent Plugins v1.0.0 (tracked 2026-08-22, cross-vendor open standard) + claude-plugins-community (Anthropic's implementation of the marketplace concept) = two signals confirming that plugin marketplaces are becoming a first-class distribution mechanism for agent capabilities, distinct from skill packs in YAML files or GitHub topics. These are different layers (the standard vs. one marketplace implementing it), not identical sub-types — canonical section promotion deferred.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capabilities / Skills / MCP**: primary. Distributes third-party capabilities to Claude harnesses via a curated marketplace.

Contrast with: VoltAgent/awesome-agent-skills (tracked 2026-04-24, community list of 1,000+ skills without security vetting or a nightly sync mechanism); mattpocock/skills (practitioner-authored skill pack, no marketplace infrastructure); Agent Plugins v1.0.0 (the cross-vendor open standard that this marketplace likely implements).

## Claims to verify

- Security scanning methodology — "automated security scanning" is vague; sandbox execution, static analysis, or capability inspection?
- Plugin compatibility scope — whether a single plugin can target both Cowork and Claude Code or must specify a target harness
- Third-party registry support — `claude plugin marketplace add <registry>` implies it, but no documentation confirms that non-Anthropic registries are operational
- Nightly sync delay — content published to `clau.de/plugin-directory-submission` may lag the repo by 24–48 hours; implications for time-sensitive capability rollout

## Status

- Tracking: first signal 2026-08-24
- Stars: 1,275 — below 5k registry threshold; no clean agent/LLM/hardware schema slot (marketplace infrastructure, not an agent)
- No canonical section change: Agent Plugins v1.0.0 (2026-08-22) + this marketplace = two signals for "plugin marketplaces as agent capability distribution," but different sub-types; two-signal rule for same sub-type not met
- Schema watch: `plugin_marketplace: [none | official | community | open-registry]`; `capability_vetting: [none | automated | manual-review]`
- Watch: third-party registries emerging alongside Anthropic's; plugin count growth in marketplace.json as leading indicator of ecosystem health
