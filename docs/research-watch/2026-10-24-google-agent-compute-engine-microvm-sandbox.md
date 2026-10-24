# Research Watch: Google Agent Compute Engine — MicroVM Sandbox Infrastructure for Agents

- Repo/Link: https://cloud.google.com/blog/topics/ai-infrastructure/agent-compute-engine-deep-dive (⭐N/A — Google Cloud product)
- Source: GeekNews / Google Cloud Blog (2026-10-22)

## Why this is worth watching
Agent Compute Engine (ACE) is Google Cloud's dedicated sandbox substrate for AI agent tool execution. It is not a general-purpose VM service with an "AI" label bolted on — it defines a structural split between *harness* (the model call loop running outside) and *sandbox* (the tool-execution environment inside a microVM) and builds hardware-level isolation around that split. The isolation model is materially different from containers: single-tenant microVMs with hardware roots of trust, no network interface or metadata server access, and zero credentials in the guest. It is targeted for preview "in the coming months" from an October 22, 2026 announcement.

## What stands out immediately
- Each agent session runs in a hardware-isolated single-tenant microVM — not a container with a shared host kernel
- Zero secrets in the sandbox: no API keys, OAuth tokens, or service account credentials inside the guest; a gateway injects credentials on the wire at egress
- No network interface in the microVM: all traffic routes through a virtio-vsock boundary to a local proxy, then through an external Agent Gateway with egress and DLP policy enforcement
- Four identity model: user, delegated on-behalf-of grant, short-lived SPIFFE workload identity (sandbox traffic only), workforce identity (agents acting with their own accounts)
- Idle checkpoint/restore: the runtime knows when an agent waits on a model call and checkpoints the session; restore is fast enough for tool-call round-trips
- DAX + copy-on-write snapshot cloning: VMs sharing the same base OS/library pages pay only for private changes, enabling high-density multi-agent workloads on shared hardware
- Fork semantics: a session can be snapshotted and forked into memory-deduplicated copies for parallel RL rollouts or branching experiments
- Targeted at four workload types: interactive agent surfaces, autonomous software engineering, eval/RL pipelines, and sandbox backends for Google's own services

## Why clawfit should care
ACE defines a new infrastructure tier between "cloud hardware" and "agent harness" that clawfit's current Level 7 does not distinguish clearly. Until now, L7 infrastructure was treated as a background layer (cloud vs. local hardware). ACE shows that sandbox isolation, credential routing, and idle scheduling are architectural choices that meaningfully constrain or enable what a harness can do and how it should be scored. A harness running inside ACE has different security, cost, and latency properties than one running in a generic container or a local VM.

For clawfit scoring: `hardware: cloud` currently treats all cloud deployments as equivalent. ACE suggests a credentialing-isolation axis (sandbox can or cannot exfiltrate secrets) that would matter for `task: code-gen` and `task: security-audit` profiles where sandboxing is a hard constraint.

## Preliminary interpretation
Current best reading:
- **Level 7 — Infrastructure / Execution Substrate** (primary): dedicated microVM compute for agent sandbox isolation, not general cloud compute
- **Level 5 — Observability** (secondary): the Agent Gateway + DLP enforcement layer provides an auditable trail of every tool call and egress event

## Claims to verify
- Whether the "targeted for preview" timeline (coming months from Oct 22, 2026) is still accurate at the time of reading
- Actual pricing: no figures were published; compare against EC2/GCE VM pricing once available
- Whether the SPIFFE identity scheme is compatible with existing harness identity models (Claude Code, Codex)
- Whether fork semantics for RL rollouts have been demonstrated outside of Google's internal use

## Status
- Tracking: new signal, Google Cloud Blog 2026-10-22 / GeekNews 2026-10-24
- Registry eligibility: not a registry candidate in current schema (hardware.json covers user-facing hardware; ACE is a cloud substrate not yet GA); revisit when pricing is available and preview access opens
