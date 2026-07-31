# Research Watch: Trail of Bits Skills — Security-Domain Claude Code Skill Pack

- Repo: https://github.com/trailofbits/skills (⭐6,364)
- Source: GitHub Trending Python (2026-07-31)

## Why this is worth watching

Trail of Bits is a recognized security research firm with a history of producing auditing infrastructure (Slither, Echidna, Manticore) that becomes defacto standard in the security industry. Their `skills` repository is a curated skill pack for Claude Code and Codex targeting the security workflow — smart contract auditing, malware analysis, vulnerability scanning, reverse engineering. The provenance (established vendor, not a hobbyist aggregator) distinguishes this from the many community skill packs already tracked: Trail of Bits has institutional incentive to maintain accuracy in security claims.

## What stands out immediately

- Seven security domain categories: Smart Contract Security, Code Auditing (C/C++/Rust/GitHub Actions), Malware Analysis (YARA rules), Verification/compliance, Reverse Engineering (DWARF), Mobile Security (Android APK scanning), Development Utilities
- Integrates with Claude Code and Codex via marketplace install — not a prompt library; explicitly uses the skills/plugin manifest infrastructure
- CC-BY-SA 4.0 license (requires attribution when redistributing — distinct from MIT skills; affects enterprise redistribution)
- 548 forks relative to 6.4k stars (8.6% fork ratio) — high customization rate, indicating practitioners adapt rather than use wholesale
- 135+ commits — ongoing maintenance, not a one-shot release
- No external model dependencies documented; skills compose with whatever LLM the agent is running
- Scope is deliberately narrow: each skill targets a specific security artifact type, not general "make code secure" prompts

## Why clawfit should care

Trail of Bits Skills is the first institutional (not community-aggregated) security firm publishing a named Claude Code skill pack. Two implications:

1. **Domain-specialized skill packs as a pattern**: Previously tracked security skills (hexstrike-ai L4c/MCP, NVIDIA/skillspector) focus on MCP server integration or hardware verification. Trail of Bits ships pure agent skills with no MCP layer. This is a distinct deployment pattern: `skill_deployment: skills-manifest` vs `skill_deployment: mcp-server`. Schema gap candidate for the existing L4 taxonomy.

2. **Org-fit signal for `governance_need: hard`**: Regulated/security-heavy organizations that already trust Trail of Bits tooling (crypto firms, defense contractors, DeFi) have an existing vendor relationship and will adopt this faster than generic community packs. The `governance_need: hard` profile in clawfit currently surfaces no skills-layer recommendations — this is the first signal that a security-firm-backed skill pack could be a valid recommendation alongside the base agent.

## Preliminary interpretation

- **Level 4b — Agent Skill Pack** (security domain, institutional provenance, multi-category, Claude Code / Codex native)
- Secondary signal for `governance_need: hard` → `task: security-audit` dimension not currently in clawfit task taxonomy

## Claims to verify

- "Claude Code plugin marketplace" framing — confirm whether skills install via `claude skills add trailofbits/skills` or require manual system prompt injection (affects ease-of-use rating)
- CC-BY-SA restriction on enterprise redistribution — legal review needed for any org distributing modified copies internally
- Star trajectory: 6.4k is solid but below the typical threshold for canonical L4b entry (most confirmed L4b entries are 10k+); monitor for 3-month growth

## Status

- First signal; below L4b canonical star threshold (6.4k vs typical 10k+); no registry entry yet
- Cross-watch: hexstrike-ai (`2026-06-04`, MCP-based security automation), NVIDIA/skillspector (`2026-06-09`, hardware-vendor skill provenance) — three-signal cluster on "security-domain agent skills" now forming; two-signal rule for a `security_skill` sub-type not yet formally met (hexstrike is MCP, not pure skill)
- Schema watch: `skill_deployment: [skills-manifest | mcp-server | system-prompt]`, `vendor_provenance: [community | institutional | hardware-vendor]`
