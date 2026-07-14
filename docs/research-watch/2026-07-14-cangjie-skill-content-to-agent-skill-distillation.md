# Research Watch: Cangjie-Skill — Distilling Books and Long-Form Content Into Executable Agent Skills

- Repo: https://github.com/kangarooking/cangjie-skill (⭐2,894)
- Source: GitHub Trending Python (daily), 2026-07-14

## Why this is worth watching
Cangjie-skill is a pipeline that converts high-value long-form content — books, video transcripts, podcasts — into structured `SKILL.md` files deployable directly to Claude Code or Cursor skill directories. The framing is not "generate a summary" but "generate a skill you can invoke during agent tasks." The distinction matters: a summary is passive retrieval; a skill is an executable trigger with structured activation conditions. With 2,900+ stars and 20+ generated skill repositories covering business and classical texts, this is the first tracked tool in the ecosystem explicitly positioned at content-to-skill as a production pipeline, not a demo.

## What stands out immediately
- **Seven-stage RIA-TV++ pipeline**: Content analysis (Adler reading method) → parallel extraction via 5 specialized extractors (frameworks, principles, cases, counter-examples, terminology) → triple verification filtering (originality, predictive power, uniqueness) → RIA++ structuring (Reference/Interpretation/Application/Execution/Boundary) → Zettelkasten linking → adversarial stress testing → deployment
- **Output format**: `SKILL.md` (executable skill body), `INDEX.md` (cross-skill navigation map), `DIGEST.md` (compressed overview), test prompts — not raw summaries
- **Adversarial stress testing included**: each generated skill includes test cases designed to probe failure boundaries; this is a quality gate on generated skills, not just on source content
- **Triple-verification filter**: three independent checks (originality, predictive power, uniqueness) before content graduates to a skill; this is a signal that the authors are aware of quality noise in LLM-generated distillation
- **Source breadth**: books (Buffett letters, business texts, classical literature), long videos with transcripts, podcasts — multi-modal input with transcript-as-text normalization for audio/video
- **Zettelkasten linking**: generated skills are cross-linked in a knowledge graph rather than isolated files, enabling skill-to-skill navigation during agent workflows
- **Claude Code/Cursor deployment target**: skills drop directly into `.claude/` or `.cursor/` skill directories — zero harness modification required

## Why clawfit should care
This is a direct L4 capability-layer signal. Cangjie-skill generates the artifact type that the L4b canonical section already tracks (agent skill packs). The distinction from mattpocock/skills or addyosmani/agent-skills: those are engineer-authored, curated over time; cangjie-skill generates skills programmatically from content corpus input. This opens a new L4b sub-type: **content-distilled auto-generated skill packs** — not manually authored, not fine-tuned weights, but a structured extraction pipeline producing executable skill artifacts. Clawfit's current registry has no entry for skill generation tooling. If cangjie-skill is the first significant signal, registry consideration should wait for a second confirming project doing the same thing.

## Preliminary interpretation
Current best reading:
- **L4b primary** (agent skill generation pipeline) — produces the same artifact type as the canonical L4b section entries, but via automated content distillation rather than human authorship
- **L3 secondary** (workflow/SSOT) — the RIA-TV++ pipeline is a governance mechanism for knowledge capture, sitting between content source and the deployed skill

## Claims to verify
- Whether generated skills are actually invoked by agents during real tasks vs. acting as context injection (trigger semantics vs. RAG semantics)
- Adversarial stress test quality: who evaluates the test cases, and what is the pass threshold?
- Cross-harness compatibility: tested against Claude Code and Cursor; behavior in other skill-compatible harnesses (Codex, Windsurf, Continue.dev) not confirmed
- The Zettelkasten linking mechanism: is the skill graph queryable during agent runtime, or is it only for human navigation of the generated corpus?
- Language support: README is in Chinese; English-language source corpus support needs confirmation

## Status
- **Registry eligibility**: no — cangjie-skill is a skill generation tool, not an agent/LLM/hardware; does not map to current registry schemas
- **Schema watch**: first signal for "content-distilled auto-generated skill packs" as a new L4b sub-type; promote to canonical taxonomy only if a second independent tool appears with the same content-to-skill pipeline model
- **Open questions**: Does the quality of generated skills degrade for non-book content (unstructured podcast audio with noisy transcripts)? Is there a quality floor below which content should not be distilled?
