# Research Watch: dotnet/skills — Official .NET Agent Skill Pack

- Repo: https://github.com/dotnet/skills
- Also see: https://devblogs.microsoft.com/dotnet/extend-your-coding-agent-with-dotnet-skills/ · https://microsoft.github.io/skills/ · docs/research-watch/2026-05-22-stitch-skills-google-labs-agent-skills.md

## Why this is worth watching

At 389 stars today on GitHub Trending (#6 C#), dotnet/skills ships from the `dotnet` org — Microsoft's official .NET engineering GitHub organization, not a Labs or community proxy. This is structurally distinct from stitch-skills (Google Labs, with a "not an officially supported Google product" disclaimer): dotnet/skills is authored by the team building the runtime itself. That provenance raises the continuity confidence materially. The repo follows the agentskills.io open standard, making it a fifth corroborating SKILL.md cross-vendor portability signal — one past the threshold already met by the 2026-05-22 stitch-skills entry.

## What stands out immediately

- 12 named plugin suites covering the .NET development lifecycle end-to-end: core, data/EF, diagnostics, MSBuild, NuGet, upgrade/migration, MAUI, AI/ML, template engine, testing, ASP.NET, and .NET 11 features
- Follows the agentskills.io open standard — same format as stitch-skills and agency-agents; compatible with Claude Code, Copilot CLI, VS Code (preview), Cursor, and Codex CLI
- MIT license — no commercial-use friction, no SaaS restriction
- Plugin marketplace distribution: `/plugin install <plugin>@dotnet-agent-skills` — same installation UX as the andrej-karpathy-skills L3 entry
- Lightweight per-skill evaluation metrics included: the team measures improvement over a no-skill baseline using model-specific scoring — claim to inspect whether methodology and data are public
- No hard MCP server dependency documented (contrast: stitch-skills is inert without the Stitch MCP server running)
- Star count is low at time of capture (2.5k on repo page, 389 today) — still below the 5k registry threshold; velocity on day one is the signal, not raw count

## Why clawfit should care

Two convergence signals matter here. First, a second major first-party non-Anthropic model-vendor skill pack has now surfaced: stitch-skills (Google Labs, 2026-05-22) and dotnet/skills (Microsoft/.NET, 2026-05-23) both occupy the "first-party non-Anthropic model-vendor skill pack" cell in the L4b provenance matrix. The stitch-skills research-watch doc set the promotion threshold for that sub-type at a second signal — this entry meets it. Second, dotnet/skills adds SKILL.md cross-vendor portability confirmation (five signals total), reinforcing the stable-axis status already conferred on 2026-05-22. For clawfit scoring, the absence of a hard MCP server dependency (unlike stitch-skills) means dotnet/skills could serve `network: online` and potentially `network: offline` profiles if skills are local-only at runtime — this needs verification.

## Preliminary interpretation

Current best reading:
- **Level 4b — Domain skill pack** (primary): 12 installable plugin suites for the .NET vertical, authored by the official .NET engineering team, following the agentskills.io open standard; closest prior art is stitch-skills (Google Labs, UI/design vertical) and anthropics/financial-services (Anthropic, regulated financial vertical). dotnet/skills fills a new (1st-party non-Anthropic model-vendor) × (developer-runtime vertical) cell.
- No MCP server dependency documented — does not carry the L5-secondary coupling that stitch-skills carries

Flag: the "first-party non-Anthropic model-vendor skill pack" L4b sub-type now has two signals (stitch-skills + dotnet/skills). Per the single-signal-promotion rule established in the 2026-05 patterns section, this sub-type is at the two-signal threshold and should be evaluated for promotion in the next scoring audit.

## Status

- 2.5k stars (at repo snapshot), 389 stars today, MIT, official `dotnet` Microsoft org — below the 5k registry threshold but above the provenance-signal threshold for sub-type counting. Hold for registry entry pending 5k stars. Flag for immediate L4b sub-type promotion audit: "first-party non-Anthropic model-vendor skill pack" now at two signals (stitch-skills + dotnet/skills) — promotion criterion from 2026-05-22 scan note is met.
