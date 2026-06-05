# Research Watch: Google Agent Executor (AX)

- Repo/Link: https://github.com/google/ax
- Source: GeekNews

## Why this is worth watching
Google released AX as an open-source distributed agent runtime emphasizing reliability, safety, and customizability over raw performance. It is Kubernetes-native and ships with first-class support for MCP, A2A, and other agentic protocols — positioning it as a vendor-backed harness substrate for production multi-agent deployments.

## What stands out immediately
- Kubernetes-native execution via Agent Substrate — not a shell script wrapper but a k8s-first deployment model
- Protocol-agnostic: MCP, A2A, and "other agentic protocols" supported as first-class citizens
- Automatic recovery and resumability across distributed deployments
- Model and harness agnostic — handles execution, durability, and coordination independently of LLM choice
- Go-based CLI: `go install github.com/google/ax/cmd/ax@latest`
- Comprehensive audit trails and observability built-in

## Why clawfit should care
AX is the second major hyperscaler (after Microsoft's agent framework signals) to ship an open-source production-grade agent runtime, and the first to lead with Kubernetes-native orchestration rather than a Python SDK. It directly occupies L2 (harness/orchestration) with L3 secondary characteristics (audit trails = governance signal). For clawfit, this is a counterpoint to `claude_code_routines` and `openai_agents_python` — it serves teams that already run Kubernetes and want protocol-standard interop over vendor-native convenience. The `network: online`, `setup_complexity: high`, `governance_need: hard` profile intersection is currently underserved in the registry.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness/Orchestration layer (primary)**: Kubernetes-native multi-agent dispatch and coordination
- **Level 3 — SSOT/Governance layer (secondary candidate)**: Audit trails and observability suggest governance characteristics pending confirmation of blocking vs. logging behavior

## Status
- First signal. Hold pending: (1) confirmed star count / adoption evidence beyond launch; (2) whether audit trail enforcement is blocking or advisory; (3) whether A2A integration is production-grade or declared intent.
- Registry candidate for `task: orchestration` + `governance_need: hard` + `team_size: mid/large` profiles once above 5k stars.
