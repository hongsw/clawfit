# Research Watch: Superset — Desktop IDE for Parallel Coding Agents

- Repo: https://github.com/superset-sh/superset
- Also see: Launch HN thread 2026-05-23; docs/research-watch/2026-05-22-multica-team-agent-platform.md; docs/research-watch/2026-05-22-runtime-yc-team-agent-sandbox.md

## Why this is worth watching

Superset targets the same developer pain point as multica and Runtime YC — managing multiple coding agents simultaneously — but solves it via a local desktop IDE rather than a managed cloud service or daemon. Running 10+ parallel agents in isolated git worktrees on a single developer machine is a structurally different topology from cloud-hosted multi-agent platforms. YC P26 institutional backing and HN front page placement (74 pts) establish early but real signal.

## What stands out immediately

- Git worktree isolation: each agent task runs in its own worktree, preventing file-level interference between parallel agents — this is an OS-primitive approach rather than a sandbox VM or container approach
- Multi-runtime agnosticism: supports Claude Code, OpenAI Codex, Cursor Agent, Gemini CLI, and GitHub Copilot simultaneously from one UI — five vendors, same pane of glass
- Unified monitoring surface: agent status notifications and a built-in diff viewer allow the developer to triage results across parallel runs without switching terminal contexts
- Built-in terminal and editor integration: positions itself as a self-contained IDE rather than a wrapper around an existing editor (contrast with multica's separate task board)
- Workspace presets: implies saved topologies (agent count, task templates) — persistence mechanism undocumented; claim to inspect
- License: Elastic License 2.0 (ELv2) — source-available, not OSI-compliant; a hard blocker for any profile requiring open-source governance compliance
- YC P26 means pre-launch cohort: feature set and stability claims are founder-stage assertions; no independent production case study available

## Why clawfit should care

Superset sits squarely in the L2 layer alongside multica and Runtime YC, but its desktop-native, git-worktree approach represents a third distinct sub-type candidate within L2. Where multica = project-management + harness collapse (daemon + task board) and Runtime YC = sandboxed team platform with governance observability (cloud-managed, audit log), Superset = local parallel-execution IDE (desktop process, worktree isolation, diff-first UX). A developer who selects multiple agents via `clawfit recommend` would use Superset to run them concurrently — the recommendation output feeds directly into the tool's agent-selection surface. The ELv2 license is a material filter signal: profiles with `governance_need: hard` or `open_source: required` cannot use Superset.

## Preliminary interpretation

Current best reading:

- **Level 2 — Meta wrappers / harnesses / orchestration layer** (primary): Superset wraps and dispatches to multiple L1 agent runtimes, manages their parallel lifecycle via git worktrees, and provides a unified monitoring surface. It does not define agent behavior (no SSOT, no behavioral spec), impose governance contracts, or add memory/context primitives.
- No credible secondary classification: the diff viewer and agent status monitoring are execution-layer observability, not L3 governance primitives. The workspace presets are a UX affordance, not an executable SSOT artifact.
- Candidate sub-type within L2: "local parallel-execution IDE" — distinct from cloud harnesses (Runtime YC), daemon-based task boards (multica), and raw VM substrates (Freestyle). Git worktree as the isolation primitive is not used by any prior L2 entry in this taxonomy.

## Status

- YC P26, Launch HN 74 pts, ELv2 license; no star count confirmed from public repo at time of writing
- Hold for registry: ELv2 source-available license, YC P26 pre-launch stage, no independent benchmark or production case study
- Promotion threshold: public star count crossing 5k OR one independent user case study validating 10+ parallel agent stability; ELv2 license review required for any enterprise profile
- Three L2 sub-type candidates now visible in one week (multica, Runtime YC, Superset) — none has a second corroborating signal; sub-type formalization remains deferred for all three
