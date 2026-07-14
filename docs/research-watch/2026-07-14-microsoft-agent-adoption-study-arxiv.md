# Research Watch: Microsoft Claude Code + Copilot CLI Adoption Study (arXiv 2607.01418)

- Repo/Link: https://arxiv.org/abs/2607.01418
- Source: Hacker News front page (2026-07-14)

## Why this is worth watching
This is the first peer-reviewed field study using developer-level telemetry to measure both the *adoption* and *output impact* of agentic CLI tools at enterprise scale (tens of thousands of Microsoft engineers, four-month window). It directly validates — with real data — the organizational fit signals clawfit uses for recommendation scoring.

## What stands out immediately
- **+24% PR merge rate** for adopters vs. non-adopters; lift persists across the full four-month measurement window — not a novelty effect
- **Social network is the primary adoption vector**: first use spread via peer visibility, not top-down mandates — organizational maturity and peer density matter for rollout
- **Retention correlates with coding activity, not demographics**: engineers who code more retain; role/seniority/team-size are poor predictors of retention
- **CLI coding agents are not uniformly adopted**: adoption follows a social diffusion curve, reinforcing that rollout strategy (peer visibility, champions) is as important as tool quality
- The study specifically covers Claude Code and GitHub Copilot CLI under a single Microsoft enterprise umbrella

## Why clawfit should care
The study empirically grounds two clawfit scoring axes: (1) **org maturity** — enterprise-scale adoption follows social diffusion, meaning mid/large orgs need different rollout conditions than solo/small; (2) **output proxy validity** — merged PRs as a productivity proxy is measurable and does show real signal. Clawfit's `frequency: daily` and `team_size: large` scoring dimensions map directly to the study's cohort structure. The +24% PR lift is a concrete ROI anchor for the `large_exec` profile.

## Preliminary interpretation
Current best reading:
- **Ecosystem signal, not a tool** — no level assignment; this is evidence for clawfit's scoring model

## Status
- High-confidence field study; arXiv 2607.01418; Emerson Murphy-Hill et al.; watching for follow-up studies from other large enterprises
