# Research Watch: patent-disclosure-skill

- Repo/Link: https://github.com/handsomestWei/patent-disclosure-skill
- Source: GitHub Trending

## Why this is worth watching
A 5,634-star MIT-licensed Python agent skill that automates the full patent lifecycle — from invention disclosure writing to examination response — using natural language prompts. It integrates with China's patent office database for prior art searches and connects to Obsidian for knowledge management, making it a fully functional professional-workflow skill rather than a toy demo.

## What stands out immediately
- Three distinct workflow modes: disclosure document generation, patent interpretation (with knowledge graphs), and office-action response
- Invoked via natural language or `/patent-disclosure-skill` in Claude Code, Cursor, Copilot, and Gemini CLI
- Produces formal Word documents with embedded diagrams from raw project materials (docs, code, CAD)
- Prior art search powered by direct integration with China's patent office database
- Obsidian integration for personal patent knowledge base construction
- MIT license; Python 3.9+

## Why clawfit should care
This represents a new class of high-expertise-domain skill packs targeting professional users (R&D engineers, inventors, patent practitioners) rather than software developers. It reinforces the `legal-research` task taxonomy already used for `korean-law-mcp` and shows that L4 agent skills are maturing into domain-vertical tools with production-grade document output. The star velocity (5.6k, appearing on GitHub Trending today) suggests the pattern of domain-specific professional skills is accelerating.

## Preliminary interpretation
Current best reading:
- **Level 4 — Agent Skill / Capability Pack** (domain-specific, invocable from any compatible agent runtime)
- Secondary: L6 (produces structured professional documents as output)

## Status
- Research signal only; no registry entry (task type `patent-research` not in current taxonomy; primary user persona is patent professional, not developer; Chinese patent office dependency limits global applicability)
- Cross-signal note: confirms `legal-research` as a distinct emerging task category alongside `korean-law-mcp` (already in registry)
- Registry hold: star count (5.6k) is above 5k threshold but task taxonomy gap and narrow professional scope prevent clean classification
