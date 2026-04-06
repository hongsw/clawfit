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
- 100% Python, MIT licensed, 11 stars

## Why clawfit should care
mdarena is a Level 5 evaluation tool (benchmark / autoresearch pattern), but it is specifically calibrated to the Level 3 SSOT layer — it evaluates CLAUDE.md quality, which is the primary governance artifact in the Level 3 pattern. This creates a feedback loop between Level 3 (instruction definition) and Level 5 (evaluation). The empirical finding that file placement and specificity matter significantly is directly relevant to any team using clawfit to configure agent workflows — it suggests that a well-placed, task-specific CLAUDE.md is worth more than a comprehensive monolithic one.

## Preliminary interpretation
Current best reading:
- **Level 5 — Research / evaluation / benchmark** (empirical grading of instruction file quality)
- Cross-level: evaluates Level 3 SSOT artifacts using Level 5 methods

## Status
- Low stars but structurally novel. The only known tool of this type. Track for adoption.
