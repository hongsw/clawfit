# Research Watch: Agent.md — Persistent Context Injection Pattern

- Repo/Link: https://fabiensanglard.net/agent.md/index.html
- Source: Hacker News (123 pts, 21 Aug 2026)

## Why this is worth watching
Agent.md is a practitioner-documented pattern: a structured markdown file injected by coding harnesses at session start to encode persistent coding style, architecture rules, and commit standards. It directly addresses "context dilution" — the LLM attention problem where middle-of-prompt instructions get underweighted. The HN traction (123 pts) suggests broad adoption interest beyond the specific author.

## What stands out immediately
- **Session-start injection**: harnesses (Claude Code, Goose, Cline, etc.) consume the file automatically via CLAUDE.md / .agents / system prompt hooks
- **Layered content**: writing style, code quality rules, architectural boundaries, commit message standards — all in one file
- **Context dilution mitigation**: placing invariant guidance upfront to maintain LLM attention weight on the constraints that matter most
- **Codebase-specific**: intended as a committed repo artifact, not a global config — ties agent behavior to project context
- **Complements CLAUDE.md**: agent.md is the public-facing pattern name; CLAUDE.md is Anthropic's named variant; functionally equivalent

## Why clawfit should care
This pattern sits at Level 5 (prompt/skill augmentation) and is increasingly assumed infrastructure for any serious coding agent workflow. clawfit's own CLAUDE.md already implements this pattern. The signal matters for scoring: tools that natively support session-start context injection (CLAUDE.md, .agents dir, system prompt slots) gain an edge in the `code-gen` task dimension for developer profiles. Scoring criteria could eventually reward harness-level context injection support as a capability dimension.

## Preliminary interpretation
Current best reading:
- **Level 5 — Context/Skill Augmentation Pattern** (persistent per-repo agent instruction layer)

## Status
- Established pattern being documented and diffused; watch for harness-level support becoming a differentiator
