# Research Watch: worktrunk — Git Worktree CLI for Parallel AI Agent Workflows

- Repo: https://github.com/max-sixty/worktrunk (⭐7,136)
- Source: GitHub Trending all languages (2026-09-12)

## Why this is worth watching
worktrunk is a Rust CLI that wraps git worktrees specifically to support running multiple AI agents in parallel on separate branches simultaneously. Native git worktree management requires composing several commands and tracking computed paths manually; worktrunk collapses this to branch-name addressing with a shared build cache, per-worktree dev servers, and automation hooks. Its README is explicit that it emerged from the practical problem of managing 5–10+ concurrent coding agents — not from general git UX concerns. This makes it a category-specific tool, not a general git improvement.

## What stands out immediately
- Core commands are `switch`, `list`, `remove` — explicitly branch-centric, hiding worktree path computation
- LLM-generated commit messages built in (not as a plugin) — tight integration with the workflow, not an afterthought
- Shared build cache across worktrees: avoids redundant dependency builds when many agents share a monorepo
- Per-worktree dev server configuration with per-branch environment variables — each agent gets its own runtime context
- Interactive branch picker with live diff/log previews: human-readable inspection of in-progress agent work
- PR/MR checkout support: agents can materialize review branches directly
- Automation hooks: pre/post switch, pre-commit, merge triggers — composable agent lifecycle callbacks
- Released September 2026; Rust binary; MIT OR Apache-2.0; GitHub Actions CI

## Why clawfit should care
clawfit currently has no harness-level concept of "running N agents in parallel on the same repo." worktrunk exposes that pattern as a concrete infrastructure choice — choose a CLI that treats worktrees as the unit of agent isolation. This is a direct answer to the `parallel_agent_support` axis sketched in `docs/reference-notes/missing-recommendation-axes.md`. If a team is coordinating five coding agents on a monorepo, the harness recommendation changes depending on whether their git tooling supports it. The shared build cache is specifically notable: without it, parallel agents on a monorepo incur quadratic install overhead.

## Preliminary interpretation
Current best reading:
- **Level 2 primary — Harness / Wrapper** (wraps base agent execution with git-level isolation, lifecycle hooks, and build coordination)
- **Level 7 secondary — Infrastructure** (git worktree management as infrastructure for agent compute isolation)

The hook system (pre/post switch, merge triggers) is structurally analogous to the hooks mechanism in Claude Code's `settings.json` — both are lifecycle event systems that let external tools coordinate around agent transitions.

## Claims to verify
- Actual performance of shared build cache across worktrees vs. `npm install` / `pip install` per worktree baseline
- Whether `switch` is atomic or can leave a partial state if the agent is mid-task
- Hook contract documentation: what arguments are passed, error handling on hook failure
- Whether LLM commit messages are locally generated or require an API call — and which provider

## Status
- 7,136 stars; Rust; MIT OR Apache-2.0; September 2026
- Not registry-eligible: git worktrees are infrastructure, not an agent/LLM/hardware entry in the current schema
- Worth watching for a future `parallel_agent_support` or `worktree_isolation` axis in org_fit scoring
- Strongest signal yet of parallel-agent git coordination as a recognized operational need
