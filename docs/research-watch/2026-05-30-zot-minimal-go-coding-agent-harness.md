# Research Watch: Zot — Minimal Go Coding Agent Harness

- Repo/Link: https://github.com/patriceckhart/zot — https://zot.sh
- Source: Hacker News — Show HN: "Zot – Yet another coding agent harness" (56 pts)

## Why this is worth watching

Zot is a single static Go binary terminal coding agent self-described as "in beta forever," which is an honest signal about maturity. At 83 stars it is far below any registry threshold, but the architectural decisions — zero external runtime dependencies, 20+ provider integrations, subscription OAuth support for Claude Pro and ChatGPT Plus, a JSON-RPC extension protocol, and a parallel swarm dispatcher — pack an unusual breadth of harness concerns into a minimal distribution unit. The Show HN appearance and active release cadence (203 releases, v0.2.3 on 2026-05-29) are enough to log as a signal.

## What stands out immediately

- **Single static Go binary:** drop on `$PATH`, no Docker, no plugin manager, no Node, no Python — the lowest possible bootstrap cost of any harness tracked in this taxonomy
- **20+ provider integrations** (Anthropic, OpenAI/Codex, DeepSeek, Gemini/Vertex, Bedrock, Azure OpenAI, GitHub Copilot, Groq, Mistral, Ollama, OpenRouter, and others including Xiaomi/MiniMax/Fireworks/Vercel AI Gateway/Cloudflare AI) — multicloud coverage comparable to Aider
- **Subscription OAuth:** authenticates against Claude Pro/Max, ChatGPT Plus/Pro, Kimi Code, and GitHub Copilot subscriptions alongside API-key flows — the first harness in this taxonomy explicitly targeting subscription-tier users rather than API-key users only (claim to inspect — OAuth implementation depth unverified)
- **Swarm subagents:** `/swarm new <task>` launches background agents sharing the working directory; an `auto-swarm` mode lets the main agent spawn sub-agents via a `swarm_spawn` tool; a `/swarm` dashboard surfaces logs and status — this is a parallel dispatch mechanism, not just multi-turn conversation
- **SKILL.md loading:** discovers skill files from `.zot/skills/`, `$ZOT_HOME/skills/`, `.claude/skills/`, and `.agents/skills/` paths — compatible with the broader SKILL.md cross-vendor portability pattern now confirmed at four+ signals in this taxonomy
- **Session branching:** `/session fork` creates a new branch from any past message with parent lineage preserved; sessions export as `.zotsession` files
- **JSON-RPC extension protocol:** extensions in any language register slash commands, expose model tools, gate permissions, and open TUI panels — a plugin surface analogous to what ECC provides via subagent delegation, but at the single-binary level
- **Telegram integration:** remote prompting via bot (in-TUI or headless daemon); photo forwarding to vision-capable models
- **MIT license:** no governance blockers
- **Author's stated motivation:** "to understand coding agents from the inside" — the repo self-describes as vibe-slopped ("written (vibe-slopped) in go"), which is an honest provenance note rather than a production claim

## Why clawfit should care

Zot's subscription OAuth feature is structurally novel for this taxonomy. Every harness currently tracked assumes API-key access; Zot explicitly targets users with Claude Pro or ChatGPT Plus subscriptions who want a terminal agent without a separate API billing relationship. If this pattern spreads, it implies a `budget: subscription` dimension that clawfit's current `budget` filter (which operates on per-token cost) does not represent.

The SKILL.md search paths deliberately include `.claude/skills/` alongside `.zot/skills/` — Zot treats Claude Code skill directories as first-class discovery sources, which reinforces the cross-vendor SKILL.md portability axis already at stable-axis status in the taxonomy.

The swarm dispatcher is a lightweight parallel-dispatch mechanism at L2, but without a task queue, Kanban state, or worktree isolation — structurally simpler than Kanbots, routa, or ECC's subagent delegation. It is closer to a "fire-and-monitor background agent" primitive than a full orchestration layer.

At 83 stars, Zot is not a registry candidate and does not trigger any taxonomy mutation. It is worth logging because the subscription-OAuth and multi-provider breadth in a minimal binary is a distinct pattern from everything currently at L2.

## Preliminary interpretation

Current best reading:
- **Level 2 — Meta wrapper / harness** (primary: single-binary multi-provider harness with session management, extension protocol, and swarm dispatch)
- No credible Level 3 secondary: Zot has no behavioral spec layer, no governance SSOT, no sprint-contract enforcement — SKILL.md loading is capability delegation, not behavioral governance
- No credible Level 4 secondary: the JSON-RPC extension protocol is a plugin surface, but extensions are not the product; the harness is

Nearest comparators: OpenHarness (L2, Python, stdlib-only) and the Aider model-agnostic positioning — but Zot adds subscription auth and swarm dispatch that neither offers. Distinct from ECC (total operator stack), multica (project-management collapse), and Kanbots/routa (Kanban + worktree isolation).

## Status

- New signal — first observed 2026-05-30; 83 stars, far below the 5k registry threshold
- No registry entry; no map mutation; no reference-levels.md change warranted
- Flag for schema-analyst: subscription-tier OAuth as a `budget` dimension (`budget: subscription`) is not representable in the current clawfit filter schema; Zot is the first harness that makes this gap concrete
- Watch criterion: if star count crosses 2k or a second harness adopts subscription-OAuth as a primary authentication path, revisit for sub-type formalization at L2
