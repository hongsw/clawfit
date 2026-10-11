# Research Watch: Vercel Eve — Filesystem-First Durable Agent Framework

- Repo: https://github.com/vercel/eve (⭐~3,500+)
- Link: https://vercel.com/eve
- Source: GeekNews front page (6 pts); New Stack coverage of Vercel Ship 2026 (London, June 17 2026)

## Why this is worth watching
Vercel is applying its "convention over configuration" playbook — the same logic that made Next.js the default React framework — to agent definition and deployment. Eve defines an agent as a directory: `instructions.md` for behavior, `.ts` files for tools, optional `agent.ts` for model selection, `sandbox/` for execution config. This mirrors Next.js's file-based routing (pages = routes, here files = agent capabilities). Vercel has a proven track record of making infrastructure primitives accessible to frontend and full-stack developers; if Eve achieves similar adoption, it could shift how a large segment of the developer population reaches for their first agent framework — not LangChain, not CrewAI, but Eve.

## What stands out immediately
- **Filesystem-as-agent-definition**: agent = directory with `instructions.md` + `.ts` tool files; tool's filename becomes its callable name — zero boilerplate wiring
- **Durable by default**: steps checkpointed via Vercel Workflows; agents survive process restarts without external state management bolted on separately
- **Human-in-the-loop gates**: approval gates are a first-class primitive, not a third-party integration
- **Subagents and evals** built into the same directory convention — a subdirectory is a subagent
- **Vercel Sandbox**: isolated compute per tool execution (distinct from the agent process)
- **Vercel Drives**: persistent agent workspaces for cross-session file storage
- **Vercel Connect**: MCP server integration via the same directory config
- **Init command**: `npx eve@latest init my-agent` — time-to-first-agent measured in minutes
- **Apache 2.0**: no license friction for commercial adoption
- **Prior art**: `@vercel/ai` SDK (tracked 2026-09-20 via JSON Render signal); Eve sits one layer above, wrapping it into a deployment unit

## Why clawfit should care
Eve occupies the L1/L2 boundary: it is a full base runtime (deploys and executes agents) but also a wrapper harness (filesystem conventions abstract away the runtime details). The critical signal for clawfit is the **target user**: frontend and full-stack developers reaching for Next.js-style conventions, not Python ML engineers. This is a different `primary_role` profile than most tracked L2 harnesses (which target ML engineers or DevOps). If Eve achieves Next.js-level adoption, `solo_dev_codegen` and `small_team_codegen` personas will encounter it as their default entry point — the `data.agents.json` recommendation surface for those profiles should account for it. Additionally, Eve's filesystem-first approach makes it structurally compatible with clawfit's `task: code-gen` profiles (agents as directories can be version-controlled, diffed, and reviewed like code).

## Preliminary interpretation
Current best reading:
- **Level 1 — Base agent runtime** (primary): Eve executes agents, manages their durable lifecycle, and provides the execution substrate
- **Level 2 — Harness/wrapper** (co-primary): the filesystem conventions, durable execution abstraction, and MCP integration layer operate at the harness level

This is the clearest "L1+L2 co-primary" signal in the corpus — neither layer description fits alone.

## Claims to verify
- Actual star count (background agent estimated ~3,500+ from July 2026 aggregator; live count may differ)
- Whether durable execution via Vercel Workflows imposes vendor lock-in or has a local/self-hosted path
- Pricing for Vercel Workflows and Vercel Sandbox at production scale (the "less than 60 seconds to deploy" claim is a DX metric, not a cost signal)
- Whether `defineAgent` / `defineTool` / `defineSandbox` API primitives are stable at v0.37+ or still pre-stable

## Status
- First signal for "filesystem-first durable agent framework" with a major platform backing
- Not a registry entry yet: star count likely above 5k threshold by now but deterministic cost/latency data for Vercel Workflows per-step pricing not confirmed
- Next trigger: Eve reaching 10k+ stars, Vercel publishing benchmark comparisons against LangGraph/CrewAI, or self-hosted/local-run path confirmed
