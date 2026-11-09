# Research Watch: Anthropic — Components of Agent Memory

- Repo/Link: https://www.anthropic.com/research/components-of-agent-memory
- Source: GeekNews

## Why this is worth watching
Anthropic published a detailed research paper on how agents should structure memory across sessions, moving from ad-hoc note-taking to a disciplined four-layer architecture. The findings are based on live experiments with Claude on game and document-corpus tasks, making them actionable rather than theoretical.

## What stands out immediately
- **Four-layer stack:** transcript logs → memory notes → structured representations (wikis) → injected always-on context
- **Dreaming/consolidation:** offline review passes that check notes against transcripts, fix errors, and repair broken links lifted wiki-only accuracy from 13% to 48%
- **Salience > volume:** Fable 5 wrote 10 focused files and earned four badges; Sonnet 3.7 wrote 413 redundant files and earned one — quality of memory notes matters more than quantity
- **Guidance beats prescription:** telling the agent what memory is *for* works better than fixed rules like "record only failures"
- **Concurrency hazard:** shared-file writes cause agents to overwrite each other; one-owner-per-file preserved all 57 contract facts vs. 41 with shared writes

## Why clawfit should care
Memory architecture is a key differentiator for long-running and session-persistent agents. clawfit's registry currently tracks `OpenMemory`, `Supermemory`, and `codebase-memory-mcp`; this paper gives a framework for evaluating *how well* each implements layered memory. The `statefulness` dimension in clawfit filters (session vs. persistent) maps directly to the distinction between injected context and wiki-based consolidation.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness/Memory layer** (consolidation and retrieval belong between base agent and task execution)

## Status
- Tracking: Anthropic research signal — informs scoring criteria for memory-capable tools
