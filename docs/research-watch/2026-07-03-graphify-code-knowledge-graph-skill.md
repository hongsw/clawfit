# Research Watch: graphify — Code-to-Knowledge-Graph Skill for Multi-Agent Coding Assistants

- Repo: https://github.com/safishamsi/graphify (⭐76,900)
- Source: GitHub Trending (Python, +937 today)
- Created: April 3, 2026

## Why this is worth watching

graphify is a 76,900★ Claude Code skill that converts any project directory into a queryable knowledge graph via a single slash command. It reached this star count in roughly 90 days, an extraordinarily fast trajectory that puts it among the top 5 fastest-rising skill-category tools tracked since the project began. However, star velocity alone is not analysis: the project's technical claim — static AST extraction plus LLM-based semantic graph generation as a unified developer tool — sits in a space that clawfit has already tracked at the L5 (memory/graph) layer (codegraph, gitnexus-code-knowledge-graph-mcp) and as a general code-understanding capability. The question is whether graphify's specific cross-modal scope (code + PDFs + images + videos) constitutes a meaningfully new sub-type, or is a feature expansion of an established pattern.

## What stands out immediately

- Covers 36 programming languages via tree-sitter AST extraction for structural analysis
- Local-first for code; uses LLM API calls for docs/PDFs/images/videos (dual-path architecture)
- Outputs three formats: interactive HTML graph visualization, markdown report, queryable JSON graph
- `/graphify .` command integrates into Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and 10+ others
- "God node" detection — identifies highly connected modules via community-detection algorithms
- Went viral 48 hours after Andrej Karpathy referenced LLM Knowledge Bases workflows (external catalyst, not organic)
- 151 releases; v0.9.5 released July 2, 2026; active v8 development branch suggests major revision in progress
- No deterministic pricing listed; LLM API calls for non-code assets incur variable token costs

## Why clawfit should care

graphify has 76k+ stars and is already a de facto dependency for many teams using Claude Code or similar. Failing to track it is a coverage gap regardless of whether it represents a new taxonomy category. The architectural point of interest is the multi-modal input scope: codegraph (2026-05-09) and gitnexus (2026-04-07) both process code and documentation; graphify adds images and video transcripts to the graph. That cross-modal extension is not currently represented in the L5 or L4b taxonomy entries. If a second tool (beyond graphify) expands graph inputs to include visual assets, the two-signal rule for a `multi-modal-knowledge-graph` sub-type would be met.

The `offline` constraint is partial: code graph generation is fully local, but multi-modal processing requires a live LLM API. This creates a hybrid network posture not cleanly captured by the current `network: online/offline` binary.

## Preliminary interpretation

Current best reading:
- **Level 4b — Domain Skill Pack** (cross-agent installable skill, code-understanding sub-type)
- **Level 5 secondary** (knowledge graph generation as a persistent project memory artifact)

The L4b classification is preferred over L5 because graphify installs as a slash-command skill rather than a persistent memory backend; it generates a one-time graph artifact rather than maintaining an active memory store across sessions.

## Claims to verify

- Whether the 76k★ count is organic or significantly boosted by the Karpathy reference and trending algorithms
- Whether the v8 development branch introduces breaking changes to the multi-agent integration interface
- Whether the local-code AST path genuinely runs offline or whether LLM calls are also made for structured code interpretation
- Actual token cost for multi-modal projects (PDF/image/video processing via LLM); no public benchmark

## Status

- 76,900★ above registry threshold; but no deterministic public cost/latency data for multi-modal path → registry hold
- Watch criterion: public pricing page with per-asset cost estimates, OR v8 GA release with documented API surface
- Promotion criterion for taxonomy: second independent multi-modal code-graph tool (beyond graphify) → new `multi-modal-knowledge-graph` L5 sub-type
