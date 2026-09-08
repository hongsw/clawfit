# Research Watch: agentic-awesome-skills v17.0.0 — Agent-First Skill Control Plane with Portable Bundles

- Repo: https://github.com/sickn33/agentic-awesome-skills (⭐46,200)
- Source: GitHub Release v17.0.0 "Evidence, Portable Bundles, and Grounded Profiles" (2026-09-08); GitHub Topics: claude-code, agent-skills, skill-catalog, mcp
- License: MIT

## Why this is worth watching

At 46,200 stars, agentic-awesome-skills is the highest-star skill catalog in this research log. v17.0.0 (released today, 2026-09-08) ships three structural changes that are qualitatively different from prior version increments: evidence linking (skills declare what external artifacts they depend on), portable bundle format (a single distributable unit that includes skill, schema, and declared dependencies), and grounded profiles (agent-constructed profiles that reference evidence rather than summarizing it). Together these three changes describe a different operational model than a static skill list — one where the agent assembles and validates a skill configuration before execution, rather than executing skills on trust.

The AAS Core orchestration layer (introduced in prior versions, extended in v17) is the part most relevant to clawfit: agent inspects the project, agent selects from a local catalog, human approves an `aas-stack.json` manifest, the manifest becomes immutable for the execution run. This is an explicit human-in-the-loop gate at skill selection time, which is architecturally distinct from both fully autonomous skill invocation and fully manual skill invocation.

2,115+ skills, 2,719 commits; MIT license; CLI, local MCP, and Workbench interfaces.

## What stands out immediately

- **v17.0.0 release today (2026-09-08)**: the "Evidence, Portable Bundles, and Grounded Profiles" release is a major version with structural format changes, not an incremental skill addition
- **AAS Core orchestration**: agent-driven skill inspection → agent skill selection from local catalog → human approval of `aas-stack.json` manifest → immutable execution plan; the human gate is at selection time, not at invocation time
- **Portable bundle format**: a single distributable unit containing skill definition, schema, declared external dependencies (evidence links), and version metadata; enables reproducible skill deployments across environments
- **Evidence linking**: skills declare which external artifacts (documents, APIs, data schemas) they depend on; the evidence link is structural metadata, not documentation; the bundle validator checks evidence reference integrity at install time
- **Grounded profiles**: agent-constructed configuration profiles that cite evidence rather than describing it; the profile is invalid if its evidence links are broken
- **Validation is structural, not semantic**: AAS Core validates bundle integrity and evidence reference links; it does not validate whether the selected skills are appropriate for the task, compatible with the agent, or safe to run
- **No remote uploads**: the entire system runs locally; skill bundles do not require a central registry (though the public AAS catalog at the GitHub repo serves as a reference source); this is consistent with the offline/local profile
- **Prior version milestones for context**: v16.2.0 (Aug 26) — 43 security and reverse-engineering skills; v16.3.0 — delegation workflow skills; v16.8.0 — public-web research via parallel-search-mcp integration

## Why clawfit should care

1. **AAS Core's agent-first selection with human approval is a new L4/L3 hybrid pattern**: prior L4 (capability/skill) signals describe skills that are either fully autonomous (invoked by the agent without human review) or fully manual (selected by the user from a menu). AAS Core introduces a third mode: agent proposes, human approves, then the agent executes an immutable plan. This is closer to the HITL gates in Dr. Claw (2026-09-07) than to typical skill invocation, but it operates at L4 (skill selection) rather than L2 (harness constraint enforcement). Two signals (Dr. Claw, AAS Core) now describe human approval gates at different layers — this is the beginning of a pattern.

2. **Portable bundle format is an implicit registry data model**: AAS Core's bundle format (skill + schema + evidence links + version) is a local implementation of what a clawfit registry entry represents for the wider ecosystem. The structural parallel is worth noting: if the portable bundle format becomes a de facto standard for distributing Claude Code skills, clawfit's registry could eventually describe bundles rather than individual skills. This is not actionable today but is relevant to long-term registry schema design.

3. **46,200 stars confirms skill catalogs are a real user-facing product category**: the prior highest-star skill catalog in this log was OpenClaw (~12k stars, tracked earlier). AAS at 46k stars, with 2,715+ skills, confirms that curated skill catalogs are a distinct product category with significant adoption, not a niche tool. This reinforces the case for a dedicated skill-catalog category in the registry distinct from individual agent skills.

4. **Structural validation gap is a scoring consideration**: AAS Core validates bundle integrity and evidence links but explicitly does not validate semantic fit, safety, or agent compatibility. A harness that uses AAS Core to select skills still bears the full responsibility for determining whether the selected skills are appropriate. This is relevant to any clawfit scoring that assigns quality weight based on "skill catalog management" — the catalog is large and curated, but the selection validator is structural-only.

5. **Security and RE skill additions (v16.2.0, 43 skills)**: the third `task: security` skill signal in six months (after Mythos 5 access controls and coding-tools-mcp's permission tiers). None of these have cleared registry threshold for the security task category, but the accumulation confirms the demand signal.

## Preliminary interpretation

Current best reading:
- **L4 — Capabilities / Skills / MCP (primary)**: AAS is a skill catalog and AAS Core is a skill selection and validation orchestrator; skills are L4 capabilities consumed by agents at inference time
- **L3 — Team Workflow / Executable SSOT (secondary)**: the `aas-stack.json` manifest, immutable execution plans, and portable bundle format describe a version-controlled, shareable workflow specification — this is L3 territory even in a single-user deployment

## Claims to verify

- Whether the portable bundle format has a published spec or is defined only by the AAS Core validator implementation; an implementation-only spec is harder to interoperate with
- Whether the human approval gate in AAS Core is enforced technically (e.g., the CLI refuses to execute without a signed manifest) or only procedurally (the documentation says to approve, but nothing stops skipping it)
- Whether the 46,200 star count represents broad general interest or concentration among a specific developer community; star velocity over the past 90 days would indicate whether the tool is growing or plateauing
- Whether the "structural validation only" disclaimer in AAS Core's documentation is correct — specifically, whether any semantic checks (task-type compatibility, known-incompatible skill combinations) have been added in v16.x or v17.0

## Status

- 46,200 stars (well above registry threshold 5k★); MIT; v17.0.0 released today (within 6-month window ✓)
- Registry consideration: blocked on schema gap — no `skill_catalog` entry type in `agents.json`; no deterministic per-execution cost (locally hosted, cost is agent LLM cost); no agent-level spec (AAS Core is a skill manager, not an agent)
- Two-signal check: AAS Core (L4/L3 hybrid, human-approval gate at skill selection) + Dr. Claw (L2, human-approval gate at harness operations) = two signals for HITL gates at different layers. This is one pattern (HITL at capability selection vs. HITL at harness operation) expressed in two different layers. Not yet sufficient for a new canonical taxonomy section — one more signal confirming the HITL-at-skill-selection mode specifically would justify adding it.
- Watch: whether v17.0.0 attracts usage of portable bundles across different agent runtimes (Claude Code, Cursor, Gemini CLI), confirming cross-runtime portability; whether the security and RE skill additions generate follow-on tool coverage
