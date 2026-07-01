# Research Watch: book-to-skill — Technical PDF/Book to Claude Code Skill Converter

- Repo: https://github.com/virgiliojr94/book-to-skill (⭐7,375)
- Source: GitHub Trending Python (daily, 2026-07-01)
- Language: Python (100%)
- Latest release: v1.2.0, June 17, 2026
- License: MIT

## Why this is worth watching

book-to-skill converts technical books and documents into modular agent skills compatible with Claude Code, GitHub Copilot CLI, and Amp — and does so 24–51× more efficiently than dumping raw PDFs into context windows. The efficiency multiple is the structural claim worth examining: if accurate, it represents a qualitatively different approach to knowledge loading than RAG-over-embeddings or raw context stuffing, using LLM-generated structure to compress access rather than search-based retrieval. At 7,375 stars with v1.2.0 released June 17 2026, this is an active project that has found real adoption.

The practical angle: the Claude Code skill ecosystem (tracked across phuryn/pm-skills, google/skills, aws/agent-toolkit, and addyosmani/agent-skills) has so far focused on *behavioral* skill packs — task procedures and tool integrations. book-to-skill occupies a distinct niche: *knowledge* skill packs derived from technical references. These are structurally different objects: behavioral skills define what an agent does, knowledge skills define what the agent knows. The distinction matters for how clawfit should categorize them.

## What stands out immediately

- **24–51× efficiency over raw context loading**: the claim is that chapter-indexed on-demand loading (~1,000 tokens per chapter, loaded only when referenced) beats RAG and full-document injection; the wide range (24–51×) suggests high variance by document type and query pattern — neither endpoint is verified independently
- **Output structure is modular and queryable**: `SKILL.md` contains mental models; per-chapter files are separate, loaded on-demand; a cheatsheet file provides quick reference; a glossary file indexes terms — four distinct access patterns rather than one monolithic text
- **Supported formats**: PDF, EPUB, DOCX, TXT, Markdown, reStructuredText, AsciiDoc, HTML, RTF, MOBI/AZW — broader format coverage than most document ingestion tools in this scan series
- **The conversion uses Claude**: book-to-skill calls the Claude API to identify frameworks, extract chapter structures, and generate the modular output files — so the skill quality is bounded by Claude's summarization accuracy on the source material; hallucinated chapter summaries would be structurally invisible
- **Compatible with Claude Code, Copilot CLI, and Amp**: not Claude Code-exclusive; the skill format appears to be harness-portable enough that at least three runtimes can consume it
- **Query interface is slash-command native**: `/book-name chapter` accesses specific sections at invocation time, not at install time; this is how Claude Code skills work, meaning the integration is architectural, not a workaround
- **v1.2.0 active development**: three releases since initial; not abandoned; 100% Python with no documented external runtime dependencies beyond the Anthropic SDK

## Why clawfit should care

The L4 capability layer (tracked in this taxonomy across multiple sub-types: behavioral skill packs, MCP tool collections, cloud-vendor integrations) has been expanding rapidly. book-to-skill introduces a sub-type not currently represented: **knowledge-base skill packs generated from existing technical documents**. This is distinct from:

- **L4b behavioral skill packs** (phuryn/pm-skills, addyosmani/agent-skills): procedural instructions for what an agent should do
- **L6b knowledge bases** (AnythingLLM, tolaria, open-notebook): document stores with search/retrieval interfaces
- **L5 memory systems** (cognee, Memora, recall): runtime memory captured from agent sessions

book-to-skill occupies the intersection: structured, persistent, on-demand knowledge access formatted specifically for agent consumption via the skills protocol. It is closer to L4b than L6b because it delivers packaged skills that agents invoke via command, not a searchable store the agent queries.

For clawfit's registry: a `knowledge_skill` sub-type of L4b, distinct from `behavioral_skill`, would correctly capture this pattern. The `task` mapping is also non-trivial — unlike pm-skills or agent-skills (which map to specific professional roles), book-to-skill's output depends entirely on the source document. The effective task set is user-defined at generation time.

## Preliminary interpretation

Current best reading:
- **Level 4b — Skills / capabilities layer** (primary): packaged, installable knowledge units accessed via agent slash-command protocol; structurally within the skill distribution model established by addyosmani, phuryn, google/skills, aws/agent-toolkit
- **Level 6b — Knowledge base / LLM-native KB** (secondary): uses LLM to transform source documents into knowledge structures; output could be described as a "structured KB artifact" as much as a "skill pack"

The overlap with L6b is genuine — whether this belongs primarily in L4 or L6 depends on whether the dominant use case is "installing knowledge as an agent capability" (L4) or "creating a queryable knowledge store from documents" (L6). The slash-command access pattern and skills-directory installation path tilt toward L4b.

## Claims to verify

- 24–51× efficiency multiple: the range is wide; the methodology (token count comparison against which baseline? raw PDF injection? RAG?) is not documented in available materials; independent replication needed before treating as a design input
- Hallucination risk during conversion: Claude generates the chapter summaries and mental-model files; if a chapter is mis-summarized, the skill silently contains wrong information with no detection mechanism — this is a known failure mode for any LLM-mediated document transformation, not specific to this tool
- Multi-runtime compatibility: "compatible with GitHub Copilot CLI and Amp" is stated; whether the skill file format is truly portable across runtimes or requires per-runtime configuration is not confirmed
- Token cost of skill generation: converting a full technical book requires non-trivial Claude API calls; the cost per book conversion is not documented

## Status

- First signal — 2026-07-01; 7,375 stars, v1.2.0 June 2026, MIT, Python
- Schema implication: `knowledge_skill` as a named L4b sub-type candidate — distinct from behavioral/procedural skill packs; two-signal threshold for sub-type promotion not yet met
- Registry candidate: `tasks: [research, code-gen]`, `roles: [developer, researcher]`, `network: online` (generation phase) / `offline` (consumption phase), `setup_complexity: low`
- Promotion criterion: 10k★ OR independent user report confirming efficiency claims with reproducible methodology
