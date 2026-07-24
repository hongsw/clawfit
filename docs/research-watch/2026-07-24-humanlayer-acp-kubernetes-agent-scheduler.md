# Research Watch: HumanLayer ACP — Kubernetes-Native Distributed Agent Scheduler

- Repo/Link: https://github.com/humanlayer/acp
- Source: Hacker News front page (146pts, "Why Software Factories Fail (or: harness engineering is not enough)", 2026-07-24)

## Why this is worth watching
HumanLayer's Agent Control Plane (ACP) is a Kubernetes operator for long-lived autonomous agents. Rather than polling or callback-based orchestration, it uses CRDs (Custom Resource Definitions) to model agents, tools, tasks, and tool-calls as first-class Kubernetes objects — giving DevOps teams the same cluster-observable control loop they use for other production workloads. The 146-point HN thread linked to an essay ("Why Software Factories Fail") arguing that harness engineering alone is insufficient without durable execution and human-in-the-loop primitives baked into the control plane.

## What stands out immediately
- **Kubernetes-native**: agents, tools, tasks are CRDs — visible via `kubectl`, alertable via standard monitoring
- **Durable async execution**: checkpoints at each tool call; task resumes from checkpoint after restart/failure
- **Human-in-the-loop native**: approval gates and expert-contact channels are first-class tool types, not afterthoughts
- **MCP integration**: tools are MCP servers, human contact channels, or delegated sub-agents
- **Multi-provider LLM**: OpenAI, Anthropic, Vertex AI, Mistral supported
- **OpenTelemetry**: observability built in; spans exported to standard collectors

## Why clawfit should care
ACP represents a structurally distinct pattern from existing L2 harnesses: it targets **DevOps/platform teams** building production agent infrastructure, not individual developers running local agents. The Kubernetes substrate means governance, access control, and observability are inherited from cluster policy — not implemented ad hoc in application code. The `governance_need: hard` + `large` team profile currently has no candidate in the registry that matches this deployment model. HumanLayer also frames this as a counterpoint to "software factory" patterns (pure automation without durable execution), which aligns with clawfit's interest in distinguishing harness types.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Orchestration** (Kubernetes-native agent control plane)
- **Level 5 secondary** (human-in-the-loop feedback loop)

## Status
- First signal. Novel Kubernetes-native deployment model; no comparable tool currently in the registry.
- "When in doubt" rule applied — first signal, single source. No canonical section change.
- Key claim to verify: durable checkpoint behavior under LLM API failures vs. Kubernetes node failures.
- Schema gap exposed: `deployment_substrate: [local | cloud-managed | kubernetes-operator]` — clawfit cannot currently distinguish between agent harnesses that run on a developer's laptop vs. those that require cluster infrastructure.
