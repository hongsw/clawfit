# Research Watch: PaperOrchestra — Google Research Multi-Agent System for Automated Paper Writing

- Repo: https://github.com/google-research/paper-orchestra (⭐116)
- Source: Web search; arXiv preprint 2604.05018 (April 2026); MarkTechPost coverage
- Note: Star count is below the 100-star general threshold but above it; qualifies as official Google Research output bypassing the star floor.

## Why this is worth watching

PaperOrchestra is a multi-agent system from Google Cloud AI Research that converts unstructured pre-writing materials (research ideas, experimental logs) into submission-ready LaTeX manuscripts, using a team of five specialized agents coordinating in sequence and parallel. The architectural interest is not the document output, but the decomposition pattern: domain-specific agents with narrow mandates (Outline, Literature Review, Section Writing, Content Refinement, Plotting) coordinating through a defined handoff protocol rather than a monolithic LLM prompted to "write a paper." The associated benchmark, PaperWritingBench, reverse-engineers raw materials from 200 top-tier AI conference papers — making evaluation structurally sound.

## What stands out immediately

- **Five specialized agents with narrow mandates**: Outline agent, Literature Review agent, Section Writing agent, Content Refinement agent, Plotting agent — each operates on a scoped task, not a general "write this section" prompt
- **Handles unstructured inputs**: accepts research ideas and experimental logs in raw form; the orchestrator decomposes and routes these before specialized agents process them
- **Full LaTeX output**: not markdown or prose summary — the system targets actual conference submission format including generated figures and diagrams
- **PaperWritingBench**: first benchmark for automated paper writing; 200 papers from top AI venues, reverse-engineered to recover the raw pre-writing materials; enables reproducible evaluation rather than impressionistic human review
- **Human evaluation win rates**: 50–68% absolute margin over autonomous baselines for literature review quality; 14–38% for overall manuscript quality — margins are meaningful but not overwhelming, signaling current limitations
- **Google Cloud AI Research authorship**: not a research intern project; co-authors include Tomas Pfister and Jinsung Yoon, established researchers

## Why clawfit should care

PaperOrchestra demonstrates a *specialized multi-agent team* pattern: a fixed set of domain-expert agents coordinated by an orchestrator for a single defined output type. This is distinct from general-purpose multi-agent frameworks (CrewAI, AutoGen) where agent roles are user-defined at runtime. clawfit currently tracks agents by general `task` categories (code-gen, qa, research); PaperOrchestra suggests a sub-category: `task: specialized-document-generation` with a distinct agent architecture (fixed specialist team vs. dynamic crew). The benchmark methodology (PaperWritingBench) is also a model for how clawfit could evaluate document-generation agent quality in future scoring dimensions.

## Preliminary interpretation

Current best reading:
- **Level 3 — Team / SSOT Generator**: primary. Five named agents with defined roles, coordinated handoffs, and a specific workflow producing a structured artifact.
- **Level 2 — Harness**: secondary. The orchestrator layer that routes inputs to specialists and assembles the final output operates as a thin harness.

Contrast with: hermes-agent (general-purpose self-improving L1/L2), deer-flow (long-horizon SuperAgent, general research), AutoGen (dynamic multi-agent, user-defined roles). PaperOrchestra is more constrained than any of these — the roles are hardcoded, the output type is fixed.

## Claims to verify

- Whether the five specialist agents are independent model calls or a single model prompted differently each time — architectural distinction matters for latency and cost
- Reproducibility of PaperWritingBench — is the evaluation dataset and scoring code included in the repo?
- Whether the system runs on a single Google Cloud API dependency or is provider-agnostic
- Human evaluation methodology — annotator background, agreement rates, and whether evaluators knew which output was system-generated

## Status

- Tracking: first signal 2026-08-23
- Stars: 116 — marginal, but official Google Research repository with peer-reviewed arXiv preprint
- Registry hold: no per-call cost/latency data; academic release without pricing documentation
- Watch: whether the "fixed specialist team" pattern for document generation spreads beyond academic research; PaperWritingBench adoption as an evaluation standard
