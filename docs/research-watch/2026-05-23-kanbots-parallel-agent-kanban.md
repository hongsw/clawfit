# Research Watch: Kanbots — Parallel Agent Kanban Desktop App

- Repo: https://github.com/kanbots-dev/kanbots (MIT) · https://kanbots.dev
- Also see: docs/research-watch/2026-05-22-multica-team-agent-platform.md · docs/research-watch/2026-05-22-runtime-yc-team-agent-sandbox.md · docs/research-watch/2026-04-07-dureclaw-distributed-agent-orchestration.md

## Why this is worth watching

Kanbots collapses three distinct ecosystem layers into a single desktop binary: a Kanban task board (project-management UI), a parallel agent dispatcher (orchestration), and a git-worktree isolation substrate (execution environment). The combination is structurally distinct from existing L2 harnesses that are CLI- or server-first. HN front page at 148 points is a credible organic signal. The local-first, zero-telemetry, no-account stance differentiates it from YC-backed managed platforms (Runtime, Twill) in the same general space.

## What stands out immediately

- Each task card dispatches one agent into its own git worktree (`kanbots/issue-N` branch) — worktree isolation is the core concurrency primitive, not containers or VMs
- Multi-runtime support: Claude Code and OpenAI Codex CLIs at launch; vendor-neutral at the execution layer (same pattern as multica's 11-CLI support, but narrower today)
- Electron + SQLite stack — local-first by design; no external data plane required for core operation
- MCP integration documented, but integration depth is not clear from public materials; claim to inspect whether MCP is used for agent tooling or as a first-class extension surface
- GitHub integration via PAT or managed GitHub Apps — two trust models with meaningfully different security profiles for `governance_need: hard` deployments
- Live board updates and cost accrual visibility as agents run — a governance-adjacent observability feature, not a full audit log
- Free OSS tier (MIT) + Cloud tier ($19/seat/month) — the pricing split implies a managed-sync or team-collaboration layer in the Cloud tier, details not publicly documented
- Zero telemetry, no account required for the desktop tier — relevant for `data_sensitivity: confidential` profiles

## Why clawfit should care

Kanbots sits at the same L2/L3 boundary as multica and Runtime YC but takes a different approach: rather than a server-side task queue or managed sandbox, it uses the git worktree as the isolation unit. This is architecturally interesting because it maps directly to git-native agent patterns (see gitagent, 2026-04-06) and produces a natural audit trail via branch history without requiring a separate governance layer. The worktree-per-card model also implies a `statefulness: session` profile — each card spawns a bounded agent session, not a persistent daemon. For clawfit's recommendation engine, this matters: Kanbots-as-harness presupposes agents that can operate within a branch-scoped context, which is currently not a tracked constraint in the schema. The Cloud tier introduces a `hardware: cloud` / `network: online` deployment variant alongside the baseline `hardware: local` path — another dual-profile pattern the registry does not yet express cleanly.

## Preliminary interpretation

Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layer** (primary): Kanbots wraps and dispatches L1 agent runtimes (Claude Code, Codex) into isolated worktrees, manages concurrency, and provides a human-facing task surface. It does not define agent behavior or impose sprint contracts — it routes and executes.
- **Level 3 secondary (weak)**: Live cost accrual and board state as agents run is a governance-observability surface, but no SSOT, behavioral spec, or formal sprint lifecycle is present. Insufficient for L3 primary.
- The git-worktree-per-task isolation model is a candidate sub-type within L2 distinct from task-queue dispatch (multica), VM sandboxing (Runtime YC, Freestyle), and serverless execution (Claude Code Routines). Closest structural analogy is gitagent (L3 candidate, git-as-distribution-layer), but Kanbots inverts the model — git is the execution substrate, not the distribution format.

## Status

- New signal, 148 HN points, MIT license, public repo. Below enough documented detail to assess star count or production maturity at log time.
- Map mutation deferred: "worktree-per-task parallel dispatch" is a new L2 sub-type candidate with no second independent signal yet; MCP integration depth unverified; Cloud tier architecture undocumented.
- Watch: whether the worktree isolation model gains adoption as a lightweight alternative to VM/container sandboxing in team agent workflows.
