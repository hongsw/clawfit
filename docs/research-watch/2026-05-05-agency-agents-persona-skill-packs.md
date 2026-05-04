# Research Watch: agency-agents — 144-Agent Cross-Tool Persona Pack

- Repo: https://github.com/msitarzewski/agency-agents
- Also see: obra/superpowers (L3/L4b, 169k★), marketingskills (L4b, 25k★), Claude-Code-Game-Studios (L3, 16k★), Donchitos (domain harness framing)

## Why this is worth watching
At 92,398 stars it is the third-largest starred repo in this entire taxonomy after superpowers (169k★) and everything-claude-code (168k★), and it reached that height organically from a Reddit thread rather than via vendor launch or institutional provenance. The combination of 144 agents across 12 professional divisions with automated conversion to seven distinct coding tools (Claude Code, Cursor, Copilot, Aider, Windsurf, OpenCode, Gemini CLI) makes it the most cross-tool-compatible persona pack yet tracked. Its organizational scope — covering not just engineering but sales, marketing, legal, healthcare, spatial computing, and finance — pushes L4b domain fragmentation further than any prior single signal.

## What stands out immediately
- 144 agents in 12 divisions: Engineering (28), Specialized (33), Game Development (20+), Marketing (23), Sales (8), Testing (8), Support (6), Design (7), Paid Media (7), Product (5), Project Management (5), Finance (5), Academic (4) — claim to inspect, division totals sourced from README as of 2026-05-03
- File format is Markdown with standardized sections: identity, core mission, critical domain rules, technical deliverables with code examples, workflow processes, success metrics — significantly more structured than prior L4b entries
- Automated conversion pipeline (`./scripts/convert.sh`, `./scripts/install.sh`) generates tool-specific formats from a single Markdown SSOT; Cursor gets `.mdc` rule files, Aider gets a single `CONVENTIONS.md`, Windsurf gets `.windsurfrules`
- Seven confirmed target tools documented with install paths: Claude Code, GitHub Copilot, Cursor, Aider, Windsurf, Antigravity, Gemini CLI; per the WebFetch scan also OpenCode, OpenClaw, Qwen Code, Kimi Code — claim to inspect for the extended list
- MIT license — commercially usable without restriction
- Community origin: explicitly grew from Reddit discussions; 15.2k forks; no single corporate sponsor
- "Learning memory" listed as an agent feature in the README — claim to inspect; actual memory implementation is not confirmed as a runtime mechanism vs. behavioral instruction text
- No agent orchestration runtime included; agents are definition files only, not an execution harness

## Why clawfit should care
Two distinct implications for the recommendation engine and ecosystem map:

**L4b density and promotion:** With 92k stars, agency-agents is approximately 3.7x the current largest confirmed L4b entry by star count (caveman at 48k★). It is also the first L4b pack that spans domains beyond software engineering, knowledge work, and marketing simultaneously. If clawfit's recommendation engine evaluates agent surface by task (code-gen, qa, research, writing, data-analysis), this is the first single source where a team can cover all five task types plus sales, legal, and healthcare from one install. The cross-tool conversion pipeline also directly addresses the `vendor_lock_in` axis surfaced by the multi-vendor anti-lockin meta-pattern (2026-04-28).

**L3 secondary read:** The automated conversion pipeline with a Markdown SSOT at the repo root, standardized YAML frontmatter, and synchronized tool-specific outputs is structurally similar to gitagent's "Git-native agent definition" and AGENTS.md's "cross-platform SSOT spec." The 12-division org chart mirrors a real team structure, which is exactly what Claude-Code-Game-Studios did at Level 3. The difference: agency-agents does not prescribe a governance workflow, approval chain, or sprint lifecycle — it defines agent personas only. That places the structural weight at L4b, not L3. The L3 secondary read is plausible but weaker than the L4b primary read.

## Preliminary interpretation
Current best reading:
- **Level 4b — Domain skill packs (primary):** Largest-starred persona skill pack in the taxonomy; cross-tool conversion pipeline distinguishes it from static dotfile packs; multi-domain (not single-vertical) scope exceeds all prior L4b entries
- **Level 3 — Team harness / executable SSOT (secondary, weak):** Division-organized 144-agent structure resembles an org chart SSOT, but no execution harness, no governance workflow, and no sprint lifecycle are present; the L3 read is a structural analog, not a confirmed classification

Notable subcategories within L4b this entry clarifies:
- Confirms "cross-tool-portable skill pack" as a distinct sub-type (alongside static practitioner dotfiles and platform-native plugin systems)
- Is the first L4b entry with explicit professional non-technical divisions (sales, marketing, legal, spatial computing, finance) at high star count — extends the domain-fragmentation trend beyond software and knowledge work

## Status
- High signal. Star count alone (92k, +828 in a single day) meets promotion threshold. MIT license, multi-tool compatibility, and division breadth are all promotion-positive factors. Deferred from registry today pending one verification: confirm that the Markdown agents are actually functional as skill files in Claude Code (i.e., install to `.claude/agents/` or equivalent) rather than being prompt templates that happen to be stored as `.md` files. If functional install is confirmed, this is a registry entry at L4b. Re-evaluate at next scan cycle or when a second source independently reviews the install path.
