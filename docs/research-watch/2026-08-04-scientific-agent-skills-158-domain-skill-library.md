# Research Watch: K-Dense-AI/scientific-agent-skills — 158-Skill Scientific Domain Library

- Repo: https://github.com/K-Dense-AI/scientific-agent-skills (⭐32,625)
- Source: GitHub Trending Python #15 (126 stars/day, 2026-08-04)

## Why this is worth watching

scientific-agent-skills is a 158-skill library spanning 18+ scientific domains — bioinformatics, drug discovery, proteomics, medical imaging, materials science, geospatial science, laboratory automation, multi-omics — packaged as agent-ready skills for Claude Code, Codex, Cursor, Hermes, and NemoClaw. It also integrates 100+ scientific databases via a unified database-lookup skill interface.

The prior L4b signals in the corpus are domain-specialized but narrow: Trail of Bits skills covers 7 security categories; k-skill covers Korean-language workflows; NVIDIA SkillSpector covers hardware benchmarking; SimpleEnglish covers one documentation standard. scientific-agent-skills is different in scope: 158 skills across a full scientific research stack (from data ingestion through analysis to scientific communication) from a single coordinated source. The 32k star count suggests it is already established in the research community, not an emerging signal — the trending position today may reflect discovery lag rather than launch.

## What stands out immediately

- **158 skills across 18+ scientific domains:** most L4b entries in the corpus cover 5–20 tools or skills; 158 is an order-of-magnitude scale difference
- **100+ scientific database integrations via a unified interface:** eliminates the need for per-database API connectors; the unified lookup skill routes to the appropriate database for the query
- **Domain coverage depth:** bioinformatics (26 skills), scientific communication (27 skills), data analysis (22 skills), ML/AI (14 skills), clinical research (8 skills), laboratory automation (6 skills) — coverage extends from wet-lab workflow to paper drafting
- **Supports NemoClaw:** named compatibility with NemoClaw signals awareness of NVIDIA's agent ecosystem — this is the first L4b entry explicitly declaring NemoClaw compatibility
- **MIT license:** unrestricted commercial use; 3.2k forks (9.8% fork ratio) suggests active downstream customization
- **Each skill includes documentation, code examples, and test suites:** structured for reliability, not just listing

## Why clawfit should care

OpenScience (2026-07-29) was tracked as the first signal for scientific research agent orchestration at the L3 layer (full research loop orchestration). scientific-agent-skills operates at the L4b layer one level above: the skills that an OpenScience-type orchestrator would call to execute domain-specific steps.

These two signals together constitute a two-signal confirmation of the scientific AI tooling stack as an emerging sub-category:
- L3 layer: OpenScience (orchestration — literature review → hypothesis → code → experiment → analysis)
- L4b layer: scientific-agent-skills (skill pack — 158 domain-specific capability units)

The two signals are cross-day (2026-07-29 + 2026-08-04) and describe different layers, not the same sub-type, so the canonical two-signal same-day promotion rule is not triggered. However, the pattern — scientific research as a coherent agent use case with dedicated orchestration AND dedicated skills — now has independent representation at two levels of the stack.

For clawfit scoring, the `task: research` dimension is underspecified for scientific research:
- General research (literature lookup + summarization) is covered by existing registry entries
- Scientific research (code execution, experimental data processing, multi-omics analysis, lab automation integration) has different compute requirements, latency tolerances, and tool dependencies
- A `task: scientific-research` filter extension would enable recommendations that route to the appropriate (scientific-agent-skills + OpenScience) combination

Schema gap: `task: scientific-research` (distinct from `task: research`); `skill_domain: [general | security | scientific | finance | locale-specific]`; `database_coverage: int` (number of integrated data sources).

## Preliminary interpretation

- **Level 4b — Agent skill pack / plugin layer** (primary: domain-specific skills packaged for agent consumption)
- No secondary: this is purely a skill library; no MCP server layer, no memory layer
- Cross-watch: OpenScience (2026-07-29, L3 scientific research orchestration) — complementary stack signal; Trail of Bits skills (2026-07-31, L4b institutional security skills) — same layer, different domain; k-skill (2026-08-02, L4b locale-specific skills) — same layer, different specialization axis

## Claims to verify

- **32,625 stars:** verify repo age — if the repo is older than 6 months, today's trending position is organic discovery rather than a new release; the primary research-watch value is the scale and structure, not launch freshness
- **158 skill count:** verify against the repo's skill index; counts like this frequently include draft or placeholder entries
- **100+ scientific databases:** verify which databases are real integrations vs. listed aspirationally; PubMed, UniProt, ChEMBL are plausible; verify that the unified interface actually routes correctly
- **NemoClaw compatibility:** NemoClaw is a newer entry in the agent ecosystem; verify that compatibility claims are tested against a real NemoClaw release, not just declared
- **Test suite coverage:** "each skill includes a test suite" is a meaningful quality claim; verify whether tests are functional (pass/fail against real APIs) or structural (schema validation only)

## Status

- First dedicated signal for scientific domain skill pack at this scale (158 skills, 18+ domains)
- Pairs cross-day with OpenScience (2026-07-29, L3) to form a two-layer scientific AI tooling signal — different layers, not same sub-type
- No registry entry: skill packs populate a future `skills_registry`, not agents.json; no cost/latency data for skill execution
- Schema watch: `task: scientific-research`; `skill_domain`; `database_coverage: int`
- If `task: scientific-research` is added as a filter dimension, scientific-agent-skills would be a strong candidate for the first `skills_registry` entry
