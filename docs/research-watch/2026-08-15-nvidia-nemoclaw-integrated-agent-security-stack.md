# Research Watch: NVIDIA/NemoClaw — Integrated secure agent execution stack on OpenShell

- Repo: https://github.com/NVIDIA/NemoClaw (⭐22,200)
- Source: NVIDIA GTC Taipei announcement March 2026; NVIDIA Developer Blog; confirmed via WebSearch 2026-08-15

## Why this is worth watching
NemoClaw is NVIDIA's open-source reference stack for deploying supported AI agents (OpenClaw, Hermes, LangChain Deep Agents) inside NVIDIA OpenShell sandboxes with managed inference, network policy, and lifecycle operations in a single CLI-installable package. NVIDIA OpenShell (tracked 2026-04-30: `docs/research-watch/2026-04-30-nvidia-openshell-agent-sandbox-runtime.md`) provides the underlying Rust-core K3s-in-Docker sandbox runtime; NemoClaw is the application layer on top — Nemotron model weights + OpenShell runtime + Privacy Router + NemoClaw CLI — installed and managed together.

The architectural significance is that NemoClaw is the first vendor-packaged "complete agent security stack" in the tracked corpus: one install command delivers a sandboxed runtime, a local open-weight model, an inference policy layer, and a network privacy router as a coordinated unit. Prior signals either deliver the sandbox runtime alone (OpenShell, sandbox-runtime, Docker Sandboxes) or the agent harness alone (OpenClaw, Hermes); NemoClaw is the first to bundle both layers with a local model under a single managed lifecycle.

## What stands out immediately
- Single-command install deploys: NVIDIA Nemotron model weights (local inference for privacy), NVIDIA OpenShell runtime (Rust-core K3s-in-Docker), NemoClaw CLI (lifecycle: start, stop, snapshot, update), Privacy Router (routes inference requests local vs. cloud based on data policy)
- Supported agents: OpenClaw, Hermes, LangChain Deep Agents Code — three distinct harness families in one managed environment; agent does not change its own configuration to gain sandboxed access
- Blueprint system: predefined sandbox configurations covering filesystem, network, and inference policy constraints; operators can define custom blueprints
- Network policy engine: baseline egress rules with explicit "operator approval flows" for exceptions — not a static allow-list but a managed policy-with-exceptions model
- Privacy Router is the novel component absent from OpenShell standalone: it determines per-request whether data can be sent to a cloud LLM API or must stay local (Nemotron); logic is configurable, not hard-coded
- 22.2k stars at 5 months from launch — far above both the 100-star tracking threshold and the 5,000-star registry threshold; velocity suggests broad adoption from NVIDIA's developer community
- Apache 2.0 license; community examples in separate NVIDIA/nemoclaw-community repo

## Why clawfit should care
clawfit's OpenShell entry (2026-04-30) tracked NVIDIA's first L1 move. NemoClaw shows what NVIDIA is building on top of that substrate: a vertically integrated agent deployment unit targeting privacy-sensitive and governance-constrained enterprise profiles. The combination of local model fallback + network policy + managed sandbox lifecycle is the engineering implementation of the `governance_need: hard` + `data_sensitivity: confidential` profile that clawfit currently has the thinnest coverage for.

The Privacy Router introduces a new axis absent from clawfit's current schema: per-request inference routing based on content classification, not just session-level provider selection. This is qualitatively different from `hardware: local` vs. `hardware: cloud` — it's a routing decision made at inference time based on what the prompt contains.

**Schema exposure:** `inference_routing: [fixed | privacy-router | manual]`; `model_bundled: bool`; `agent_lifecycle: [manual | managed-cli]`; `sandbox_policy: [static | blueprint | operator-approval]`; `privacy_router: bool`.

**Two-signal convergence with sandbox-runtime (also 2026-08-15):** sandbox-runtime (Anthropic, OS-native syscall filtering) + NemoClaw (NVIDIA, K3s-in-Docker + Privacy Router) — two same-day signals from different vendors targeting the same gap: AI agent process isolation with policy enforcement. Distinct mechanisms (OS-native vs. containerized K3s), distinct integration models (bare-process wrapping vs. full agent lifecycle management), and distinct inference strategies (passthrough vs. local-model fallback) — not the same architectural sub-type, but a strong same-day convergence pattern. **Two-signal rule note:** the existing Docker Sandboxes (2026-08-10) + sandbox-runtime (2026-08-15) + NemoClaw (2026-08-15) constitute a three-signal cluster across three vendors (Docker, Anthropic, NVIDIA) all shipping agent-process isolation infrastructure within one week. This is the strongest convergence signal on this sub-type since the ADE parallel-execution cluster (paseo + openchamber + t3code, 2026-08-08–10). Canonical section change deferred: these three are architecturally distinct sub-types (microVM, OS-native, K3s-in-Docker) — they confirm a category ("agent process isolation") but each is a different approach; a stable "agent isolation substrate" sub-cluster in L1 or L7 would require two instances of the *same* architectural sub-type. Discovery log entry only.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base runtimes** (primary): NemoClaw installs and manages the runtime environment in which the agent executes — it is the deployment substrate, not an orchestration harness
- **Level 7 — Infrastructure layer** (security / governance sub-type, secondary): Privacy Router and network policy enforcement operate at the infrastructure layer beneath the agent harness

OpenShell alone was L1 primary / L4c secondary; NemoClaw's Privacy Router and managed lifecycle push it distinctly into L7 infrastructure territory as a second layer.

## Claims to verify
- Star count: 22.2k reported by search; verify against GitHub directly — NVIDIA community amplification can cause rapid spikes that don't reflect sustained adoption
- Privacy Router implementation: is local routing enforcement documented at the source level, or is it a configured proxy behavior that could be bypassed by an agent that constructs raw HTTP requests?
- OpenShell dependency: NemoClaw is built on OpenShell v0.0.36 (April 2026, "alpha/proof-of-life"); NemoClaw's stability is tied to OpenShell's alpha label
- Supported agent list: OpenClaw, Hermes, LangChain Deep Agents are listed; Claude Code is listed as OpenShell-compatible but is it NemoClaw-compatible?

## Status
- Registry eligibility: **Potentially eligible** (22.2k stars above 5k threshold; Apache 2.0; public documentation exists) — blocked by: no deterministic cost/latency data for Nemotron local inference (throughput varies by hardware profile); OpenShell alpha label; NemoClaw itself has no explicit version tags in the search results
- Open questions: What is NemoClaw's own version/release status? Is the Privacy Router's routing logic user-configurable or NVIDIA-controlled? Is Nemotron (local inference model) open-weight, and what are the VRAM requirements?
- Watch trigger: first stable NemoClaw release tag OR deterministic Nemotron inference benchmarks published by NVIDIA
