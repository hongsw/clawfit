# Research Watch: reverse-skill — AI-Powered Security Skill Router Pack

- Repo: https://github.com/zhaoxuya520/reverse-skill (⭐11,681)
- Source: GitHub Trending #4 all languages (2026-08-01, 1,360 stars today)

## Why this is worth watching

reverse-skill is an active skill router pack targeting authorized security research workflows — reverse engineering, penetration testing — across multiple coding agent runtimes (Claude Code, Kiro, Cursor, Cline). With 11,681 stars on a repo created 2026-05-13 and still receiving pushes today, it is the fastest-growing security-domain agent skill pack in the current scan window. This is the fourth security-domain agent skills signal in the corpus: hexstrike-ai (L4c/MCP, 2026-06-04), NVIDIA/skillspector (hardware-vendor skill provenance, 2026-06-09), and Trail of Bits Skills (L4b institutional pure-skill, 2026-07-31). The architectural distinction here is a **router** layer: instead of a static skill collection, this pack routes between specialized security tools on demand, with a self-evolving knowledge base component.

## What stands out immediately

- Explicit "authorized penetration testing" framing in the description — distinguishes from unconstrained offensive tooling; skill docs likely include scoping and authorization language
- AI-powered routing: the pack routes incoming requests to specialized skills based on task (reverse engineering, pen test, vulnerability research), not a flat list the human navigates
- On-demand toolchain bootstrapping — tools required for a specific security task are surfaced as they are needed, not pre-loaded
- Self-evolving knowledge base claim — if verified, means skill quality improves from past execution outcomes (echoes HKUDS/OpenSpace self-improving skill management, 2026-07-28, L4b)
- PowerShell implementation (not Python/JS) — suggests the target environment includes Windows security toolchains where PowerShell is the native automation shell
- Multi-agent runtime support (Claude Code, Kiro, Cursor, Cline) declared explicitly — first security skill pack to name this many runtimes
- MIT license — permissive redistribution, distinct from Trail of Bits CC-BY-SA restriction
- 1,772 forks (15.2% fork ratio) — higher than Trail of Bits (8.6%); practitioners are actively customizing rather than using wholesale

## Why clawfit should care

Trail of Bits Skills (2026-07-31) established the "institutional security firm / static skill collection" pattern. reverse-skill introduces a structurally different architecture: a **router layer** over security skills, not a curated static set. Two implications:

1. **Router + skill pattern vs. static skill pack**: prior L4b signals assume skills are flat, static, and human-selected. reverse-skill routes between skills based on task context. If this becomes a pattern, `skill_deployment` needs a `router-manifest` value to distinguish from `skills-manifest` (flat install) and `mcp-server` (tool-call based). The routing mechanism also links this to the L7 model-routing discussion (Tokenless 2026-07-30, OmniRoute 2026-07-23) — but at the skill level rather than model level.

2. **Self-evolving knowledge base** — if the claim verifies, this is the second signal (after HKUDS/OpenSpace 2026-07-28) for skill-evolution feedback loops in the security domain specifically. Two signals for feedback-loop skill evolution now exist, but they are cross-domain (general vs. security); same-layer rule met for `skill_evolution: feedback-loop` pattern watch.

## Preliminary interpretation

- **Level 4b — Agent Skill Pack with routing layer** (security domain, multi-agent runtime support, MIT, router architecture distinguishes from flat skill collection)
- Secondary: cross-watch with L7 routing signals (Tokenless, OmniRoute) — skill-level routing and model-level routing may converge

## Claims to verify

- "Self-evolving knowledge base" — mechanism unspecified in available README excerpt; could be a user-populated note system or a genuine execution-outcome feedback loop; distinguish before any canonical claim
- "AI-powered routing" specifics — whether routing is LLM-based (prompt → skill selection) or rule-based (keyword → skill); affects reliability at task boundaries
- "Authorized pen testing only" — check whether the README includes scoping gates or relies solely on user attestation
- PowerShell implementation vs. agent ecosystem: verify how skill manifests are interpreted by non-Windows agent runtimes (Kiro/Cline may require adapter layer)

## Status

- First dedicated signal; fourth security-domain agent skills signal overall (hexstrike 2026-06-04, skillspector 2026-06-09, Trail of Bits 2026-07-31, this)
- No registry entry: `tasks` taxonomy lacks `security-audit`/`reverse-engineering` dimension; cost/latency data not available for a pure skill pack
- Schema watch: `skill_deployment: router-manifest` (new value beyond `skills-manifest | mcp-server | system-prompt`); `skill_evolution: feedback-loop` (second signal after OpenSpace 2026-07-28, cross-domain)
- Cross-watch: HKUDS/OpenSpace (2026-07-28, L4b) for self-evolving skill comparison; Trail of Bits Skills (2026-07-31, L4b) for institutional security skill provenance comparison
