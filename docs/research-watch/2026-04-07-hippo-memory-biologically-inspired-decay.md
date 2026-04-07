# Research Watch: Hippo — Biologically-Inspired Memory for AI Agents

- Repo/Link: https://github.com/kitfunso/hippo-memory
- Source: Hacker News (31 points)

## Why this is worth watching
Hippo implements decay, recall-strengthening, and consolidation for agent memory — mimicking human hippocampal memory rather than storing everything indefinitely. This is architecturally distinct from existing tools (claude-mem, cipher, OpenMemory) which are primarily persistence layers. Hippo introduces selective forgetting as a first-class design principle, with configurable half-lives, confidence tiers, and cross-tool memory portability (Claude, ChatGPT, Cursor import).

## What stands out immediately
- Three-layer architecture: buffer (working), episodic (decaying), semantic (compressed patterns)
- Half-life decay (7-day default); recall boosts half-life by 2 days — use-it-or-lose-it
- Error memories get double decay period to persist critical lessons longer
- Hybrid recall: BM25 + embedding similarity with explainable match reasons
- Cross-tool portability: import from CLAUDE.md, ChatGPT exports, Cursor — addresses vendor lock-in
- Git-based auto-learning from commits
- Zero runtime dependencies

## Why clawfit should care
This is a Level 4a memory entry that introduces a new quality axis: memory selectivity and decay. Clawfit's current L4a entries (claude-mem, cipher, OpenMemory) all assume persistence; none model forgetting. For `large_exec_research` profiles dealing with long-running research loops, selective forgetting may matter more than raw storage. The cross-tool portability angle is directly relevant to clawfit's multi-agent recommendation scenarios.

## Preliminary interpretation
Current best reading:
- **Level 4a — Memory / persistent context (biologically-inspired decay memory layer)**

## Status
- Tracking: new entry, medium signal. Low star count but architecturally distinctive. Monitor for adoption.
