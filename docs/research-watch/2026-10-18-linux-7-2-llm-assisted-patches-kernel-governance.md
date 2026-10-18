# Research Watch: Linux 7.2 Development Statistics — LLM-Assisted Patches at 7%, Kernel AI Policy Crystallizing

- Repo/Link: https://lwn.net/Articles/1088776/
- Source: GeekNews front page (2026-10-18, 6pts) + LKML Linus policy post (GeekNews, 13pts)
- Related: https://lore.kernel.org/lkml/CAHk-=whTs09_ozN+e09GU68N1wPP56MUzDjrg9rnKxQUa0A_4Q@mail.gmail.com/

## Why this is worth watching

The Linux 7.2 LWN development statistics article gives the **first structured, LWN-quality quantitative evidence for AI-assisted contributions at scale in the Linux kernel**. 1,111 Assisted-by-tagged changes (nearly 7%) in a single release cycle, up from 301 in 7.1 (+269%). The LWN author explicitly flags that the true number is likely higher — maintainers rarely ask, many devs omit the tag, and at least one maintainer strips them on apply. Simultaneously, Torvalds has posted a LKML policy statement: "Linux is not one of those anti-AI projects" — formal kernel policy now distinguishes AI contributions (Assisted-by tag) from signed-off human authorship. These two signals together are **the clearest evidence yet that LLM-assisted patch contribution is a normalized, measurable part of Linux development, not a fringe experiment**.

This is a third major open-source project governance signal in three days (Postgres 19 delayed by AI code review quality gate 2026-10-16; claude.dev REVIEW.md as governance primitive 2026-10-17; Linux 7.2 LLM patches today). **Three-signal rule met for "AI in major open-source project governance."**

## What stands out immediately

- 1,111 Assisted-by commits in Linux 7.2 (≈7%), up from 301 in 7.1 (3× growth in one cycle)
- 252 commits carry Reported-by:Sashiko (Google's AI code review system); 568 additional commits mention Sashiko in changelogs — an AI reviewer is now a named contributor class
- Fixes-tag count spiked sharply vs. recent cycles — LWN author directly links to LLM-driven bug hunting
- LWN raises a quality question that mirrors Postgres 19: "whether some submitters understand the patches they send" — the maintainability burden of LLM-authored patches is an open concern
- Kernel documentation added December 2025 bars AI Signed-off-by but defines Assisted-by as the correct tag — formal AI attribution policy predates the volume surge
- Torvalds explicitly won't ban AI use: "if somebody has issues with that, they can do the open-source thing and fork it. Or just walk away." Strongest possible signal for kernel AI policy stability.
- linux-next for 7.3 already has 1,100+ Assisted-by-tagged patches queued — the pattern will accelerate

## Why clawfit should care

This is the first evidence that an AI code review system (Sashiko, Google-internal) is a named contributor in the most security-critical open-source project in the world. For clawfit:

1. **`task: systems-programming` now has quantitative evidence** for AI agent effectiveness, not just the qualitative Linus Claude Code adoption signal (2026-10-14).
2. **`governance_need` scoring for AI coding agents in kernel/systems contexts** now has a real operational model: Assisted-by tagging as the baseline governance contract.
3. **The open question about patch quality** (do submitters understand what they sent?) directly mirrors Sphinx's premise (2026-10-18) — the two signals reinforce each other as a two-signal cluster around "AI code comprehension verification."

## Preliminary interpretation

Current best reading:
- **Level 5 — Evidence/observability layer** (first LWN-quality measurement of AI-assisted open-source contribution at scale)
- **Level 3 secondary** (AI contribution policy formalized in kernel documentation; Torvalds policy statement)

## Claims to verify

- Whether the Sashiko AI review system (Google-internal) is or becomes publicly available
- Whether the 7% Assisted-by rate understates true LLM involvement (LWN author believes it does — no independent confirmation)
- Whether the Fixes-tag spike is causally linked to LLM bug hunting or has other explanations
- Whether patch quality per Assisted-by commit is lower, higher, or equal vs. non-tagged commits (no data cited)

## Status

- New signal: first structured, LWN-quality quantitative evidence for LLM-assisted Linux kernel contributions at scale
- Third governance signal in three days (Postgres 19 2026-10-16, claude.dev REVIEW.md 2026-10-17, Linux 7.2 today) — **three-signal rule met for "AI in major open-source project governance"** as a distinct pattern
- 📡 note: `systems-programming` task type now has quantitative evidence — candidate for a stronger `task_evidence` annotation in the scoring model
- 📡 note: Sashiko (Google AI code review for kernel) is a new tool candidate if made publicly available
