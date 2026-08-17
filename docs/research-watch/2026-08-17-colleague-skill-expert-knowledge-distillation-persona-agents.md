# Research Watch: colleague-skill — Expert Knowledge Distillation into Deployable Persona Agents

- Repo: https://github.com/titanwings/colleague-skill (⭐23,124)
- Source: GitHub Trending (Python, daily) 2026-08-17
- License: MIT
- Author: titanwings (community, Shanghai AI Lab research backing)
- Language: Python / multi-harness skill format

## Why this is worth watching

colleague-skill is a structured framework for distilling a specific person's expertise, communication style, and decision patterns into a deployable AI skill that runs inside existing coding agent harnesses. The core claim: rather than general-purpose personas or RAG over documents, colleague-skill extracts a two-layer (Persona + Work) structured profile — then compiles it into a skill bundle that Claude Code, Hermes Agent, OpenClaw, Codex, and DeepSeek Harness can load and invoke.

At 23k stars it is one of the higher-star entries in the L4 skills space. The research backing is a peer-reviewed arXiv paper (arXiv:2605.31264, Shanghai AI Lab): "COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation." The combination of high community adoption and academic validation is unusual in the skills-pack category.

## What stands out immediately

- **Two-layer persona model:** Persona Layer (six dimensions: identity, expression, decisions, interpersonal dynamics, correction mechanisms, and a sixth) plus Work Layer (scope, workflows, expertise, output preferences) — separates "how they think and communicate" from "how they do the job." Most persona tools flatten these into a single prompt blob.
- **Three character families:** `colleague` (coworker with full Persona + Work), `relationship` (close connection emphasizing emotional/conflict dynamics), `celebrity` (public figure with six-dimension research dossier from works, interviews, decisions, timeline, mental models, external evaluations). Structurally different persona types require structurally different extraction pipelines.
- **Multi-source data ingestion:** Feishu/DingTalk/Slack via APIs, WeChat chat histories, PDFs, emails, markdown, direct text, and video subtitles with AI transcription — the persona is built from actual interaction artifacts, not from a single prompt-engineering session.
- **Multi-harness deployment:** one compiled skill format runs on Claude Code (native slash-commands), Hermes Agent, OpenClaw, Codex, and DeepSeek Harness (filesystem-based skill discovery). Harness-agnostic persona skill format is a distribution pattern not yet tracked in other L4 skill entries.
- **Community skill gallery:** 100+ pre-built skills and 165+ contributors — indicates the format is reusable and shareable, not just a per-org private tool.
- **Published benchmark:** arXiv:2605.31264 reports measurable similarity between the distilled persona's outputs and the original person's documented responses — the paper provides a peer-reviewed evaluation framework, not just qualitative claims.
- **23.1k stars / 2.1k forks:** significant adoption velocity for a skills-layer tool; the only L4 skills-pack entry with comparable community scale is the Anthropic cybersecurity skills pack (tracked 2026-05-24, 28k★) and last30days-skill (tracked 2026-06-05, 58k★), though those serve different use cases.

## Why clawfit should care

The core pattern — person → structured extraction → compiled skill → multi-harness deployment — is a new L4 sub-type: **expert knowledge distillation as a skill distribution format.** Prior L4 skill entries fall into categories: domain-skill packs (security, research, code-review), capability wrappers (MCP servers), and harness-specific slash-commands. colleague-skill is the first tracked entry where the skill content itself is a specific person's modeled expertise, not a task category.

For clawfit's scoring model, this introduces a use case not currently profiled: `task: expert-delegation` — delegating a domain-expert consultation to an AI persona skill rather than to a full RAG pipeline over documents or a fine-tuned model. The multi-harness portability of the skill format means a single knowledge distillation output runs on whichever agent harness the org uses, which is directly relevant to clawfit's `statefulness: session` and `network: offline` profiles (skills load locally without cloud round-trips).

**Cross-signal with last30days-skill (2026-06-05):** last30days-skill aggregates recent AI research from public sources into a temporal skill format. colleague-skill distills individual expertise into a persona skill format. Both are "skill-as-specialized-knowledge" patterns — but the persona format is bounded by data from one person, while the research-aggregator is unbounded by topic. Different extraction pipelines, same harness distribution mechanism.

**Schema gap:** `task: expert-delegation`; `skill_content_type: [domain-task | persona | research-aggregator | capability-wrapper]`; `multi_harness_portable: bool`.

## Preliminary interpretation

- **Level 4 — Skills / capabilities layer** (primary): colleague-skill produces deployable skill artifacts — compiled persona bundles invoked via slash-commands or filesystem-discovery by existing harnesses. It does not run an agent loop, does not provide inference, and does not orchestrate workflows; it provides a callable knowledge artifact.
- **Level 2 secondary (skill compilation pipeline):** the extraction process (ingesting multi-source data → structuring into Persona + Work layers → compiling a harness-compatible skill) is a pipeline with LLM-powered extraction steps — structurally a harness for building other skills. But the primary artifact is L4.
- Not L5 (memory/observability): colleague-skill stores persona data statically at build time, not as a running memory system. The persona does not update from interactions — it is compiled and deployed.
- Not L3 (team workflow): colleague-skill skills represent individual expertise, not organizational SSOT or executable workflow documents.

## Claims to verify

- **Peer-review validity:** arXiv:2605.31264 cites Shanghai AI Lab — is the paper peer-reviewed and published in a recognized venue, or a preprint with no external validation?
- **Similarity evaluation methodology:** the paper claims measurable similarity between distilled-persona outputs and original-person outputs — what is the evaluation metric, ground truth, and human evaluation protocol? Self-reported similarity without blind evaluation is weak evidence.
- **Harness compatibility claim:** five harnesses listed (Claude Code, Hermes Agent, OpenClaw, Codex, DeepSeek Harness) — are all five maintained and tested by the repo, or are some community-contributed with unknown compatibility state?
- **Privacy and data governance:** ingesting WeChat histories, Slack, DingTalk for knowledge distillation raises data ownership questions — is there documented consent model, data handling policy, or local-only processing guarantee?
- **Star velocity source:** 23.1k stars is high for a skills-layer tool — is this organic from HN/trending, or seeded by a coordinated launch from a large Chinese tech community?

## Status

- 23,124 stars — above 5k threshold; below registry threshold for `agents.json`/`llms.json`/`hardware.json` (schema does not map to current registry entries)
- **No registry entry:** colleague-skill is a skill compilation framework, not an agent, LLM, or hardware entry. No deterministic cost/latency data for the compilation pipeline (depends on LLM provider used).
- **No canonical section change:** single signal for "expert knowledge distillation as persona skill" sub-type; two-signal rule requires a second independent tool in the same category.
- **Watch for:** second tracked tool doing structured persona distillation to multi-harness skill format (would trigger L4 skills sub-section "persona skill" in reference-levels.md); privacy incident or data governance flag that would disqualify from certain org profiles; arXiv paper acceptance at a peer-reviewed venue.
