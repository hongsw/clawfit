# Research Watch: mdarena — Empirical Benchmarking of CLAUDE.md Instruction Files

- Repo/Link: https://github.com/HudsonGri/mdarena
- Source: Hacker News (Show HN, 11 points)

## Why this is worth watching
mdarena is the first observed tool that treats CLAUDE.md as a variable to be optimized empirically rather than written intuitively. It benchmarks instruction file variants against real merged PRs from the target repo, grading by test pass rate and diff overlap — the same methodology as SWE-bench. This closes a feedback loop that has been open since CLAUDE.md became a standard: developers write instructions but have no way to measure whether they help or hurt.

## What stands out immediately
- Three-stage pipeline: mine merged PRs → run agent with/without instruction variants → compare test pass rates and diff overlap
- Uses `git archive` history-free checkouts to prevent agents from seeing future commits — benchmark integrity is explicitly addressed
- Supports monorepo structures with per-directory instruction files
- SWE-bench-compatible export (JSONL) and import — connects to existing benchmark ecosystems
- Real-world finding documented in README: targeted per-directory instructions improved test resolution by ~27% over no-instruction baseline; single consolidated file performed no better than baseline
- 100% Python, MIT licensed, 11 stars at 2026-04-06 기록; 2026-04-07 검증: 44 (포크 1, 커밋 5)

## Why clawfit should care
mdarena is a Level 5 evaluation tool (benchmark / autoresearch pattern), but it is specifically calibrated to the Level 3 SSOT layer — it evaluates CLAUDE.md quality, which is the primary governance artifact in the Level 3 pattern. This creates a feedback loop between Level 3 (instruction definition) and Level 5 (evaluation). The empirical finding that file placement and specificity matter significantly is directly relevant to any team using clawfit to configure agent workflows — it suggests that a well-placed, task-specific CLAUDE.md is worth more than a comprehensive monolithic one.

## Preliminary interpretation

**Primary: Level 5 — Research / evaluation / benchmark**

Level 5 is defined as "evaluation harnesses, benchmark references, autonomous research loops." mdarena's core function is evaluation: it runs a controlled experiment (with/without CLAUDE.md variants) against a ground-truth dataset (merged PRs), scores each variant by test pass rate and diff overlap, and outputs a ranked comparison. This is a benchmark harness — the defining L5 function.

**Why not Level 3 (SSOT / governance)?**
L3 is about *creating and maintaining* SSOT files (CLAUDE.md, AGENTS.md, DESIGN.md). mdarena does not help create CLAUDE.md — it evaluates *existing* ones. The subject of the study is L3, but the function is L5. The distinction: L3 asks "what should the instruction file say?"; L5 asks "does this instruction file actually improve outcomes?"

**Cross-level relationship**
mdarena creates a feedback loop between L3 (instruction authoring) and L5 (evaluation). This is structurally significant: most L5 tools evaluate model or agent capability; mdarena evaluates the *configuration artifact* (CLAUDE.md). That makes it a novel sub-type within L5 — "SSOT evaluation" — not previously represented in the taxonomy.

## Status
- 11 stars → 44 (2026-04-07 검증). Structurally novel — only known tool of this type. Track for adoption.
