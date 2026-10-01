# Research Watch: iFixAi — AI Agent Compliance Auditing Platform

- Repo: https://github.com/ifixai-ai/iFixAi (⭐18,254)
- Source: GitHub Trending Python (2026-10-01)

## Why this is worth watching

iFixAi occupies a specific gap that none of the currently tracked L5 tools address: **compliance-oriented agent auditing** as opposed to capability evaluation or performance benchmarking. Where tools like LiveNeRF (tracked 2026-09-30) measure model performance drift over time, and LatticeDB (tracked 2026-09-30) provides the memory substrate, iFixAi asks whether an agent is doing what it was deployed to do — and whether that behavior is defensible against EU AI Act, ISO 42001, and NIST AI RMF requirements. The 60-inspection framework (5 core pillars × 25+ categories) is structured around organizational risk vectors — Fabrication, Manipulation, Deception, Unpredictability, Opacity — not technical metrics. At 18,254 stars with a plugin integration path (runs inside Claude Code, Codex, and other agent environments), this is not a niche compliance checklist; it is embedding auditing capability directly into development workflows. That development-time audit integration is a structural change from post-deployment compliance scanning.

## What stands out immediately

- **60 inspections across 25 categories** organized into five core pillars: Fabrication, Manipulation, Deception, Unpredictability, Opacity — plus 20 premium categories for advanced risk surfaces
- **Sub-120-second complete audit**: full assessment completes in under two minutes; this makes it practical as a CI gate, not just a periodic review
- **Three execution modes**: guided CLI wizard (for first-time use), flag-based CLI (for automation/scripting), and plugin/skill integration (for Claude Code, Codex, and other in-harness execution)
- **Multi-judge evaluation modes**: uses independent graders for adversarial robustness — not a single-LLM self-assessment loop
- **Provider-agnostic**: works against OpenAI, Anthropic, Google Gemini, Azure OpenAI, Bedrock, and any HTTP-compatible endpoint
- **Regulatory framework alignment**: outputs map to EU AI Act Article 9 (risk management), ISO 42001 clause structure, and NIST AI RMF core functions — gives legal/compliance teams a structured artifact, not just pass/fail
- **Graded output format**: letter grades A–F with weighted scoring; JSON, Markdown, and interactive scorecard outputs — designed for both automated processing and human review
- **Apache 2.0, Python 3.10+**: permissive, embeddable in commercial tooling

## Why clawfit should care

The L5 taxonomy in clawfit currently has entries for evaluation frameworks (LiveNeRF, Pydantic Evals), memory stores (LatticeDB, mem0), and observability. iFixAi introduces a distinct L5 sub-type that none of the existing entries cover: **compliance-gated agent auditing**. The distinction matters for clawfit's recommendation engine because organizations subject to EU AI Act obligations (which entered full enforcement in August 2026) have a hard requirement for auditable AI system documentation that capability benchmarks alone cannot satisfy. An agent recommendation workflow that surfaces iFixAi alongside coding-agent tooling would be a qualitatively different recommendation for a regulated enterprise than one that omits it. The development-time plugin integration also creates an L4/L5 boundary question for the taxonomy: when auditing capability runs inside the agent harness, it stops being a post-hoc evaluation tool and becomes an inline safety check — a structural change in how the evaluation layer is positioned.

## Preliminary interpretation

Current best reading:
- **Level 5 — Evaluation / Governance** (primary): compliance-oriented auditing of agent behavior against regulatory requirements and risk vectors; produces structured compliance artifacts
- **Level 4 — Capability Layer** (secondary): plugin/skill integration means it operates as an in-harness capability when embedded in Claude Code or Codex; the audit runs as part of the agent workflow, not separately

## Claims to verify

- **"Independent verification within 120 seconds"**: the 120-second bound needs verification on agents with external API dependencies where response times vary; complex multi-tool agent traces may exceed this
- **Multi-judge independence**: the multi-judge evaluation mode is listed as a feature, but the specific judge configuration (same model family vs. different providers) affects how meaningful the independence claim is
- **Regulatory mapping accuracy**: the EU AI Act / ISO 42001 / NIST RMF alignments are self-reported; independent legal review of whether the inspection categories actually map to specific article requirements has not been confirmed
- **Adversarial robustness of the inspector itself**: any tool that evaluates whether an agent "manipulates" or "deceives" needs to be robust against an evaluated agent that probes inspection mechanisms — no documentation of this found

## Status

- 📡 Tracking: **first signal for "compliance-oriented AI agent auditing"** as a distinct L5 sub-type — differentiated from capability evaluation (LiveNeRF), memory observability (LatticeDB), and performance benchmarking
- 18,254★ at first tracking; trending on GitHub Python
- Registry eligibility: not applicable — auditing tool, no cost/latency profile that maps to the inference registry schema
- Open questions: depth of EU AI Act mapping (self-reported vs. legally reviewed); behavior on complex multi-step agents with long traces
