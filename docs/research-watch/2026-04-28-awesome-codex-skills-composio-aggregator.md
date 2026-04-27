# Research Watch: ComposioHQ/awesome-codex-skills — Skill Aggregator Pattern Crossing into OpenAI Codex Ecosystem

- Repo: https://github.com/ComposioHQ/awesome-codex-skills
- Source: GitHub Trending Daily (Python, +637 today, 2026-04-28)
- Also see:
  - VoltAgent/awesome-agent-skills (1,000+ skill aggregator, 2026-04-24 watch)
  - mattpocock/skills (personal skill directory, 2026-04-26 watch)
  - vercel-labs/skills (platform-vendor skill manager, 2026-04-23 watch)

## Why this is worth watching
The skill aggregator pattern — previously concentrated in the Anthropic Claude Code ecosystem (claudemarketplaces.com, awesome-agent-skills, mattpocock/skills, kepano/obsidian-skills) — now has its first significant non-Anthropic counterpart targeting OpenAI's Codex CLI. Composio (a vendor-neutral integration platform with 1,000+ app connectors) is the curator, which means the aggregator pattern is being driven by a third-party integration layer rather than the model vendor itself. This is the strongest 2026 signal yet that "skills" is shifting from a vendor-specific concept (Anthropic Skills, OpenAI Plugins) toward a cross-vendor distribution pattern.

## What stands out immediately
- **SKILL.md format reused on Codex side.** Each skill has YAML frontmatter (`name`, `description`) plus body — visually identical to the Anthropic Skills format. The schema is being copied across vendors, not redesigned per platform.
- **Install target is `$CODEX_HOME/skills/` (default `~/.codex/skills/`)** — symmetrical to Claude Code's `.claude/skills/`. OpenAI Codex CLI now has a skills directory convention parallel to Anthropic's.
- **50+ curated skills across 5 categories** — Development, Productivity, Communication, Data/Analysis, Meta/Utilities. Smaller catalog than VoltAgent/awesome-agent-skills (1,000+) but materially broader than a personal directory.
- **Composio integration is the differentiator.** Many skills depend on Composio CLI to reach external apps (Slack, GitHub, Notion, Datadog, Stripe). The aggregator is also a funnel into Composio's connector platform.
- **Python installer script (`install-skill-from-github.py`)** as the install vector — distinct from `npx skills` (Vercel) or git-clone-into-`.claude/`. Each ecosystem is settling on its own install affordance.
- **Progressive disclosure pattern documented** — `references/` for long-form content, `scripts/` for deterministic ops, `assets/` for templates. This matches the Anthropic Skills authoring guide, suggesting de facto convergence on skill-pack internal layout.

## Why clawfit should care
1. **First non-Anthropic L4b aggregator with traction.** All prior L4b aggregator entries in this taxonomy are Claude-centric. A Codex-targeted aggregator means clawfit's L4b sub-type "skill aggregator" is no longer Anthropic-only. The runtime axis (Claude Code vs Codex CLI vs Gemini CLI) and the skill-pack axis are partially decoupling.
2. **Cross-vendor schema convergence.** SKILL.md with YAML frontmatter is being used by both Anthropic and Composio/Codex. If this stabilizes, a skill pack could become portable across runtimes — relevant to scoring `skill_portability` and `vendor_lock_in` axes.
3. **Vendor-of-integrations as curator.** Unlike Vercel (deployment platform → skill manager) or mattpocock (personal brand → skill directory), Composio is an integration vendor curating skills as a top-of-funnel for their connector business. This is a third distinct curator archetype for L4b aggregators.
4. **Codex CLI ecosystem maturity signal.** The fact that Codex CLI now has a skills directory convention, an install pipeline, and a 50+ skill catalog means OpenAI's CLI agent has crossed a tooling threshold previously only Claude Code occupied. clawfit recommendations that currently route to Claude Code for skill-heavy workflows may need to consider Codex CLI on the same axis.

## Claim to inspect vs. validated facts
- **Validated:** Repo exists, SKILL.md format with YAML frontmatter, install target `$CODEX_HOME/skills/`, ~50 skills across 5 categories, Composio CLI dependency for many integration skills, Python installer script.
- **Claim to inspect:** Star velocity (+637/day) — needs a few more days of trend data to confirm sustained vs. one-day spike. Cross-vendor portability of SKILL.md schemas — visually similar but not yet verified that an Anthropic skill drops in unmodified to Codex CLI (or vice versa).

## Preliminary interpretation
Current best reading:
- **Level 4b — Skill aggregator / curated catalog** (Codex-targeted sub-type)
- Curator archetype: **integration-vendor-curated** (distinct from platform-vendor like Vercel, community-curated like VoltAgent, practitioner-curated like mattpocock)
- Cross-cutting signal: SKILL.md as a de facto cross-vendor schema — worth flagging but not yet strong enough to mutate `docs/reference-levels.md`

## Status
- Tracking; +637 stars in one day on GitHub Trending Python. Below registry threshold (content catalog, not a runnable tool); confirms L4b skill-aggregator pattern is now cross-vendor, with OpenAI Codex CLI as the second runtime to host an aggregator ecosystem.
