# Research Watch: Untrivial Agent Orchestrator — Fleet-Management IDE for Coding Agents

- Repo: https://github.com/Untrivial-ai/agent-orchestrator (⭐9,900)
- Source: GitHub Trending (TypeScript, via web search)

## Why this is worth watching

Agent Orchestrator is a desktop IDE that coordinates multiple coding agents — Claude Code, GitHub Copilot, Cursor, Aider, and 23 others — working on the same codebase simultaneously. Rather than replacing a coding agent, it operates one layer above: planning tasks, delegating to agents via isolated worktrees, then autonomously resolving the output integration problems (CI failures, merge conflicts, review threads) that arise when agents run in parallel. The 9,900-star count and 26+ agent integrations suggest this has moved past proof-of-concept.

## What stands out immediately

- **26+ agent integrations**: Claude Code, GitHub Copilot, Cursor, Aider, Goose, Codex, and others; all treated as interchangeable workers beneath the orchestrator
- **Autonomous integration handling**: CI fix loops, merge conflict resolution, and pull request code review run without human intervention per task — the orchestrator escalates only on genuine decision points
- **Isolated worktrees per task**: each agent gets its own git worktree, preventing state bleed between concurrent work streams; a pattern distinct from sequential task dispatch
- **Live Kanban board**: tracks every agent's assigned work, PR status, and CI run in a single view — explicit artifact of the fleet model, not just a dashboard
- **Project-aware planning**: orchestrator decomposes a large outcome into appropriately-sized work units before delegation; this is scope-setting, not just task routing
- **Electron desktop app with Nix dev environment**: desktop distribution (.dmg, .exe, AppImage) signals a product aimed at individual power users and small teams, not an enterprise SaaS
- **Apache 2.0 license**: permissive, not dual-licensed; suggests community growth priority over lock-in

## Why clawfit should care

clawfit currently models (agent, llm, hardware) triples without any concept of a *fleet controller* above individual agents. Agent Orchestrator represents a pattern where the agent is a *commodity worker* and the orchestration layer is the differentiator — inverting the assumption that the user selects one agent and configures it. A `fleet_controller` or `orchestration_layer` dimension in clawfit's registry would let it distinguish recommending a single agent vs. recommending an orchestrator that spans many agents. Also relevant: the isolation model (`per_task_worktree: bool`) is a verifiable registry field with concrete scoring implications for multi-agent org profiles.

## Preliminary interpretation

Current best reading:
- **Level 2 — Agent Harness / Meta-Wrapper**: primary. Sits above individual agents, managing their lifecycle, dispatch, and output integration.
- **Level 3 — Team / SSOT**: secondary. The project-level decomposition and PR-centric workflow place it in the team coordination layer when used at scale.

Contrast with: apache/maka (log-as-runtime, single-agent), Claude Code (direct user↔agent), ruflo (multi-agent swarm with built-in runtime), ECC (harness optimization, not fleet management).

## Claims to verify

- "26+ coding agents supported" — need to confirm list covers all claimed integrations, or if some are placeholder stubs
- Autonomous merge conflict resolution — the approach matters (rebase vs. merge, conflict resolution strategy); current description is high-level
- Star count trajectory — 9,900 could reflect rapid recent spike; check star history for organic vs. viral growth
- CI fix loop — whether this calls external CI APIs or parses CI output locally; important for air-gapped / on-prem environments

## Status

- Tracking: first signal 2026-08-23
- Stars: 9,900 — above 5k registry threshold, but cost/latency data for the orchestrator layer itself is not applicable (it's a client app, not a priced API)
- Registry hold: no per-call pricing to model; registry addition deferred until a `fleet_controller` dimension exists in the schema
- Watch: adoption among power users running 3+ agents in parallel; whether Apache Maka, ruflo, or Untrivial converge on similar patterns (three-signal rule for "fleet management IDE" taxonomy entry)
