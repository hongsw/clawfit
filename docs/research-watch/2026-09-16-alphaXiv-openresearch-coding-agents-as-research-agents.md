# Research Watch: OpenResearch — Coding Agents as Research Agents

- Repo/Link: https://github.com/alphaXiv/OpenResearch
- Stars: ⭐ 3,325
- Source: GitHub Trending (2026-09-16)

## Why this is worth watching

OpenResearch, from the alphaXiv research preprint platform, adapts the coding-agent loop — plan, act, observe, revise — for scientific literature research tasks. Rather than building a new agent framework, it wraps existing coding agents (Claude Code, Goose, OpenHands) with domain-specific research primitives: paper retrieval, citation traversal, claim verification, and structured note synthesis. The provenance (alphaXiv, which hosts arXiv papers with annotation) gives it credibility as a research-domain-specific wrapper rather than a general capability claim.

## What stands out immediately

- **Coding-agent loop reuse**: does not reinvent the agent loop; adds a research skill layer on top of agents already in the registry.
- **alphaXiv provenance**: the same org that built annotation infrastructure for arXiv preprints — domain authenticity, not a general-purpose demo.
- **Rust implementation**: suggests performance-oriented design rather than rapid prototyping; unusual for a research tool.
- **Primitives**: paper retrieval, citation graph traversal, claim verification — maps directly to `research` and `summarization` task types in clawfit's schema.
- **3.3k stars**: smaller than colibri/VoiceStudio but meaningful for a domain-specific Rust tool targeting researchers.

## Why clawfit should care

This is a concrete example of the L2 harness pattern applied to a specific domain (scientific research) by domain experts rather than general AI tooling builders. The pattern — take an existing coding agent, add domain-specific skills, score as a research harness — is exactly what clawfit should be able to recommend when `primary_task=research` and `primary_role=researcher`. It reinforces the need for role-specific scoring beyond generic task matching.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/wrapper layer**: a domain-specific skill harness built on top of L1 coding agents, analogous to DeerFlow and OpenHands for research domains.

## Status
- Tracking: new signal; watching for harness compatibility list and adoption by academic orgs.
