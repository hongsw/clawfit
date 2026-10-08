# Research Watch: Trigger.dev — Durable Execution Platform for AI Agents

- Repo: https://github.com/triggerdotdev/trigger.dev (⭐16.2k)
- Source: GitHub Trending, October 2026; GitHub Topics `ai-agents`, `mcp`

## Why this is worth watching
Trigger.dev occupies a narrow but load-bearing position in the agent stack: it guarantees that long-running agent tasks survive page refreshes, network failures, process restarts, and arbitrary waits without developer-managed checkpointing. The v4.5.0 release elevated this from a generic background job platform to a first-class durable agent runtime, shipping `chat.agent` — a construct that maps one conversational session to one long-lived task keyed by `chatId`. At 16.2k stars and reported 30,000+ developers executing hundreds of millions of agents monthly (as of December 2025), it has crossed from experimental to production-scale infrastructure.

## What stands out immediately
- **chat.agent construct**: runs Vercel AI SDK chat completions as a durable Trigger.dev task; survives redeploys and crashes with conversation state intact via `chatId` key
- **Container checkpointing via CRIU**: leverages the Linux kernel's CRIU (Checkpoint/Restore In Userspace) tool to freeze and resume ordinary async code at any `await` — no special state-management API needed, no cold-restart cost during waits
- **Human-in-the-loop built in**: a tool flagged as requiring approval causes the long-running task to pause mid-execution; the process sleeps cheaply while a human reviews, then resumes
- **headStart optimization**: runs first LLM turn server-side while the agent boots; measured cold-start cut from 2,801ms to 1,218ms in their own benchmarks
- **AI SDK v7 support**: ESM-only v7 alongside v4, v5, and v6 — unusually broad SDK compatibility; indicates it tracks the Vercel AI SDK release cycle closely
- **Model-agnostic**: the platform doesn't pick the LLM; any provider surfaced through the AI SDK works
- **Apache 2.0 license**: permissive; cloud-hosted and self-hosted options available
- **YC W23 company**: $16M Series A (December 2025), Standard Capital lead, Y Combinator participation

## Why clawfit should care
Trigger.dev sits between L2 (harness) and L7 (infrastructure) in a way the current registry does not model: it is specifically a **durable execution substrate** for agents rather than an orchestration framework. The distinction matters because `statefulness` in clawfit's filter is currently binary (stateless / session / long-term), but the CRIU checkpoint model represents a fourth mode — process-level durable state that persists across machine boundaries without an external store. A `durable_execution` axis in the hardware or harness registry would differentiate this from ordinary stateful agents. The human approval gate also directly maps to an emerging `human_oversight` variable that clawfit's scoring model does not currently capture.

## Preliminary interpretation
- **L2 — Harness / Wrapper** (primary): provides the execution loop, tool dispatch, conversation keying, and approval gates that constitute an agent harness
- **L7 — Infrastructure** (secondary): CRIU checkpointing is kernel-level execution infrastructure, not harness logic

## Claims to verify
- Cold-start improvement (2,801ms → 1,218ms with `headStart`): self-reported in release notes; no independent benchmark; methodology not specified (model, hardware, network)
- "Hundreds of millions of agents monthly" (December 2025 self-report): not independently verified; reflects submitted job count, not successful completions
- CRIU checkpoint fidelity under network file system or shared state: CRIU is well-established for process migration but can fail on open network sockets and certain file descriptor types; behavior under real agent workloads with active MCP connections is not documented

## Status
- v4.5.16 last confirmed stable release (~September 2026)
- Actively maintained: YC-backed, Series A funded, production-scale adoption
- **First dedicated signal for "CRIU-checkpoint durable execution as an agent runtime substrate"** in clawfit's research-watch corpus
- Registry candidacy: eligible for a hardware/execution-environment entry if `durable_execution` axis is added; pricing is published; no registry entry warranted under current schema
- Monitor: v5 roadmap (if any), MCP server integration, CRIU failure modes under real agent workloads
