# Research Watch: AWS Labs cli-agent-orchestrator — Multi-CLI Supervisor for AI Coding Agents

- Repo: https://github.com/awslabs/cli-agent-orchestrator (⭐1,597)
- Source: GitHub Trending (Python, daily)

## Why this is worth watching

Amazon Web Services Labs has shipped an orchestration layer that coordinates multiple AI coding CLIs — Claude Code, Kiro CLI, Codex CLI, and others — under a single supervisor agent. The significance is not the technical approach (tmux-isolated sessions, supervisor/worker delegation, Web UI) but the institutional signal: a hyperscaler's official tooling organization has concluded that multi-CLI orchestration is a problem worth formalizing. Community projects (Dodaios, OpenMausBot) have explored similar territory, but AWS Labs carries distribution weight and production-deployment context (Kubernetes/EKS support is in the README). That changes the probability that multi-CLI orchestration becomes a standard deployment pattern rather than a power-user curiosity.

## What stands out immediately

- **Supervisor + worker model**: a supervisor agent receives tools to delegate tasks to specialist workers; workers can run in parallel or sequence; orchestration topology is defined by profiles, not code changes
- **Provider-native authentication**: each CLI runs as a full native process with its own auth (Claude Pro subscription, Codex API key, etc.) — the orchestrator does not proxy credentials; it coordinates, not impersonates
- **tmux isolation per agent**: each worker runs in its own tmux session; the Web UI (localhost:9889) streams live PTY output per agent; isolation means a crashing worker does not stop the supervisor
- **MCP server interface**: an `operations` MCP server exposes orchestration control to other agents or tooling — the orchestrator can itself be a tool called by a higher-level agent
- **Kubernetes deployment path (Amazon EKS)**: devcontainer and EKS deployment options are documented from day one; this is not a local-only tool
- **Tool restrictions per provider**: the profile system can restrict which tools a worker agent is allowed to call, relevant for cost control and security
- **774 commits on main**: the commit count suggests the repo has been in active development for some time before trending — this is not a proof-of-concept drop

## Why clawfit should care

clawfit currently models single-agent deployments: one (agent, llm, hardware) triple per recommendation. awslabs/cli-agent-orchestrator represents a category where the deployment unit is a *fleet of heterogeneous agents*, each with its own CLI, model, and credentials. This creates a new recommendation axis: when a task requires both a deep coding agent and a browser agent running simultaneously, the optimal single-agent recommendation is the wrong output. The supervisor model also surfaces a new filter criterion — which agents support being orchestrated as workers (MCP-compatible, tmux-compatible) versus which only run as top-level processes.

The EKS deployment path suggests AWS expects this pattern in production cloud environments, not just on developer laptops. That is relevant to clawfit's `hardware: cloud` category, which currently assumes a single agent per deployment.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/Wrapper Layer** (primary): wraps multiple L1 CLI runtimes under a supervisor-worker coordination layer; does not replace any individual CLI's base runtime
- **Level 7 — Infrastructure** (secondary): Kubernetes deployment and per-agent tool restrictions touch the production infrastructure axis

## Claims to verify

- Whether Kiro CLI is AWS's own agent CLI or a third-party — the README lists it alongside Claude Code and Codex; confirming its origin matters for understanding whether this is partly an AWS-native agent promotion
- Whether the 774-commit history reflects internal development before public release, or a long public development period — the star count (1,597) is low for the commit depth, suggesting recent public release
- Whether the MCP `operations` server exposes full orchestration state or only task dispatch — the distinction matters for whether this can be supervised by a higher-level orchestration layer
- Whether profile-based tool restrictions are enforced at the orchestrator level or rely on the worker CLI's own tool filtering

## Status

- First scan: 2026-11-19
- Registry action: **deferred** — 1,597 stars is above the 100-star threshold but below the 5,000-star threshold for registry addition; no deterministic per-task cost/latency data available for the orchestration overhead; the product orchestrates agents rather than being an agent itself, so current registry schema (task × latency × budget) does not map cleanly
- 📡 Note: awslabs/cli-agent-orchestrator is the first official hyperscaler tool for multi-CLI AI coding agent orchestration; prior signals in this space were community projects (Dodaios Nov-18, OpenMausBot); watch for a second major vendor (Google Labs, Microsoft) shipping equivalent multi-CLI coordination tooling — that would confirm the pattern and justify a new L2 sub-type "multi-CLI supervisor harness"
