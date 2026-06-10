# Research Watch: x1xhlol/system-prompts-and-models-of-ai-tools — L3 Governance Reference

- Repo/Link: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
- Source: GitHub Trending (2026-06-10, 139,137★)

## Why this is worth watching
At 139k★ this is the highest-starred item on GitHub Trending today. It is a community-curated collection of reverse-engineered system prompts and internal tool definitions from Claude Code, Cursor, GitHub Copilot, Windsurf, Gemini CLI, Codex CLI, and others. Its extraordinary star count signals that developers actively use it to understand the internal governance layer of competing AI tools — i.e., what is baked into the agent's instruction layer vs. what comes from the user's CLAUDE.md / .cursorrules / etc.

## What stands out immediately
- 139k★ is the highest star count ever observed in this scan for a non-LLM project
- Covers 10+ major AI coding tools, each with extracted system prompts
- Multi-language content (not just English)
- Serves as a de-facto governance comparison dashboard for practitioners choosing between AI tools
- Directly shows how tool builders implement L3 (behavioral governance) in practice

## Why clawfit should care
The L3 layer in the ecosystem map covers specification-first development, behavioral governance, and meta-prompting. This collection is the first high-signal evidence that *the content of the governance layer (system prompt)* is a meaningful differentiator in tool selection — distinct from feature lists or benchmarks. It also confirms that practitioners are willing to do significant research to understand tool-level governance before committing. This aligns with clawfit's `governance_need` dimension in org-fit scoring. A `governance_transparency` field (open prompt / disclosed / opaque) could be a useful future registry axis.

## Preliminary interpretation
Current best reading:
- **Level 3 — Behavioral Governance layer reference artifact (not a tool itself)**

## Status
- Reference signal logged. No registry mutation (not a tool). Consider `governance_transparency` as a future org_fit metadata field.
