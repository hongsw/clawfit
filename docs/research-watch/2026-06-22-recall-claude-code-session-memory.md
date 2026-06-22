# Research Watch: recall — Claude Code Session Memory Plugin

- Repo/Link: https://github.com/raiyanyahya/recall
- Source: Hacker News (55 pts, 42 comments)

## Why this is worth watching
recall targets the "cold start" problem in Claude Code — each session begins without context, forcing re-explanation of the project. It logs session activity automatically and summarizes locally using TF-IDF + TextRank with zero LLM calls, zero network traffic, and zero API keys. This positions it distinctly from cloud-based memory solutions and manually maintained CLAUDE.md files.

## What stands out immediately
- Session logging to `history.md` (append-only) + local summarization to `context.md`
- Zero network calls — TF-IDF + TextRank summarization runs entirely offline
- Optional git integration tracking file changes and recent commits
- Commands: `/recall:save`, `/recall:show`, `/recall:log`
- Configurable via `recall.config.json`; best-effort secret redaction before writes
- Claude Code exclusive; no external model dependency for the memory layer

## Why clawfit should care
First Claude Code-native session memory plugin that operates fully offline with no LLM API cost for the memory operation itself. Architecturally distinct from: Supermemory (cloud API), cognee (LLM-backed knowledge graph), agentsview (session analytics), and CLAUDE.md manual context management. Occupies a new sub-cell: offline, zero-cost-per-invocation session memory for a specific agent runtime.

## Preliminary interpretation
Current best reading:
- **Level 4a — Session-scoped offline agent memory plugin** (complementary memory attached to a specific agent runtime without a separate memory API)
- **Level 5 secondary weak** — local summarization pipeline produces a lightweight context artifact (context.md) that functions as an evaluation summary of the session

## Status
- 67★ — well below registry threshold; held
- First signal for "offline zero-cost session memory plugin" as a named L4a sub-type distinct from cloud-API memory platforms
- Promotion criterion: 2k★ OR a second Claude Code-native offline memory plugin with comparable non-LLM summarization architecture
