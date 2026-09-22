# Research Watch: Drop — Rootless Linux Sandbox Explicitly for Coding Agents

- Repo: https://github.com/wrr/drop (⭐137)
- Source: Hacker News Show HN (109 pts, 37 comments, 2026-09-22)

## Why this is worth watching
Drop is a rootless Linux sandboxing tool built in Go that explicitly lists "coding agents" as a primary target use case alongside individual programs. It frames the problem as: agents running in a user's environment have access to credentials, SSH keys, and sensitive files — Drop enforces OS-level permissions to contain what the agent can read or write, defending against prompt injection that results in accidental deletion or credential theft. This is the first tracked tool whose README positions sandboxing as an agent-safety primitive rather than a generic developer-tool convenience.

## What stands out immediately
- Explicitly calls out **coding agents** as a target: "isolate programs and coding agents without leaving your familiar work environment"
- **Rootless** — no elevated privileges required to create or enter the sandbox; this is a deployment blocker eliminated vs. Docker
- Optional **gVisor** integration for user-space kernel protection — higher isolation for agents with broader tool access
- **TOML configuration** for granularly exposing specific files and services to the sandbox (allow-list model, not deny-list)
- **Isolated home directory** — agent cannot see the user's full `$HOME`, only what is explicitly allowed in
- Built on **Linux namespaces** (user, mount, PID, IPC, cgroup, network) — standard kernel primitives, no proprietary shim
- **Pasta** for isolated networking — can restrict agent outbound network access at the OS layer
- 137 stars and Show HN format: early-stage, not production-hardened, seeking developer feedback
- Written in Go (consistent with agent-substrate, google/ax — Go is converging as the language for agent infrastructure)

## Why clawfit should care
The current registry has no `sandbox_model` field for agent entries. CubeSandbox (tracked 2026-07-01) is the nearest prior signal but it is a hosted multi-tenant execution environment, not a user-deployable per-process sandbox. Drop occupies a different slot: a local-first, per-agent sandbox that a developer runs on their own machine without a cloud dependency. The `hardware: local` + `governance_need: hard` profile in clawfit has no sandboxing recommendation today. Drop is the first explicit supply to that gap, though at 137 stars it is too early to register. More structurally: the fact that a developer tool is describing agents as a threat to reason about (alongside regular programs) is an ecosystem signal — agent sandboxing is becoming a recognized developer concern, not just an enterprise compliance item.

## Preliminary interpretation
- **Level 7 — Infrastructure / Hardware layer (primary)**: execution sandboxing for agent processes; operating at the OS/kernel level, not the agent framework level
- **Level 4 — Capability layer (secondary candidate)**: if positioned as a deployable skill or plugin for Claude Code / Codex, it would serve as an L4 security capability

## Claims to verify
- Whether gVisor integration is stable or experimental (the README calls it "optional" — confirm it works with standard agent CLIs)
- Whether the isolated network mode (Pasta) prevents agent LLM API calls or only restricts outbound connections to non-allow-listed hosts
- Whether Drop has been tested against Claude Code, Codex CLI, Cline, or other tracked agents specifically
- Star trajectory — 137 is very early; need confirmation of developer uptake over the next 30 days

## Status
- **First signal for "user-deployable, rootless, agent-native Linux sandbox"** as a named tool category
- 137 stars — below registry threshold (5k); below the stronger monitoring threshold (1k); Show HN engagement (109 pts) is the primary signal quality indicator
- Not a registry candidate yet
- Monitor: if star count reaches 1k in the next scan, write a follow-up; if a second independent tool in the same category appears, evaluate canonical promotion for a `sandbox_model: [none | hosted | local-rootless]` axis
