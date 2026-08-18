# Research Watch: machine0 — Persistent Agent Compute Infrastructure (YC S26)

- Repo/Link: https://machine0.io / https://news.ycombinator.com/item?id=48543245
- Source: Hacker News (Launch HN, 2026-08-18); YC S26 batch

## Why this is worth watching

machine0 provides persistent NixOS virtual machines specifically designed for AI agent workloads, accessible via CLI or MCP. The product premise is that coding agents are increasingly running for 6–24 hours on hard features, auto-research agents running for days, and always-on agents (OpenClaw, Hermes) running 24/7. Standard cloud VMs were not designed for agent-driven lifecycle management; ephemeral sandboxes (e2b, Sandbox Runtime) are designed for short-burst tasks. machine0 occupies the gap: persistent, agent-controlled compute with per-minute billing and native MCP integration.

Founded by Barnaby Malet (previously co-founded Upflow, YC W20), raised $500K in the YC S26 batch. The company is one of the first infrastructure startups explicitly positioning their product around AI agent compute rather than general-purpose developer VMs.

## What stands out immediately

- **Agent-native CLI and MCP interfaces:** all operations use CLI with `--json` output, and a remote MCP server enables agents to provision, start, stop, and configure VMs programmatically. Claude Code and Codex "pick up injected credentials automatically" — machines are provisioned and configured without human intervention.
- **Persistent vs. ephemeral design:** unlike e2b or Anthropic Sandbox Runtime (designed for short bursts), machine0 VMs remain running until explicitly stopped. Suspended VMs incur only storage costs ($0.078/GB/month), enabling cost-efficient long-running workloads.
- **Profile injection for agent configuration:** agents inject credentials, MCP servers, prompts, and environment variables into machines at provisioning time. This creates a reproducible agent environment without manual setup steps between sessions.
- **NixOS reproducibility:** NixOS as the base OS enables deterministic builds and one-command rollbacks. For agent workloads that need consistent environments across sessions (no "works on my machine"), NixOS reproducibility is a structural advantage over Debian/Ubuntu-based sandboxes.
- **Static IP and HTTPS endpoint per VM:** each machine gets a static IP and public HTTPS endpoint, enabling agents to host services, receive webhooks, and maintain persistent network identity across pauses. This is absent from ephemeral sandboxes.
- **GPU options at scale:** H100, H200, L40S, MI300X, RTX 4000/6000 Ada — up to 8×H200 per VM. Per-minute billing from $0.013/hr (small CPU) to $39.336/hr (8×H200). This enables agents to provision GPU compute for inference or training as needed during a run.
- **99.99% uptime SLA:** the uptime guarantee matters for always-on agents (OpenClaw, Hermes) where a provider outage resets multi-day agent runs.

## Why clawfit should care

machine0 introduces a new infrastructure pattern not previously modeled in clawfit: **agent-controlled compute provisioning**. The current scoring model treats hardware as a static recommendation dimension (hardware: local_laptop, local_mac, cloud, on-prem). machine0 changes this: an agent running on a local laptop can dynamically provision a GPU VM for a specific subtask, complete it, and suspend the VM — blurring the line between "local" and "cloud" hardware profiles.

**Cross-signal with e2b (L7 sandbox infrastructure, tracked):** e2b provides ephemeral sandboxes for short-burst agent tasks (seconds to minutes). machine0 provides persistent VMs for long-duration agent tasks (hours to days). Together they define a spectrum: ephemeral (e2b, Anthropic Sandbox Runtime) → persistent (machine0). The "duration" dimension is not currently in the clawfit hardware schema.

**Cross-signal with NemoClaw (L2, always-on, 2026-08-15):** NemoClaw is an always-on NVIDIA-reference agent stack. machine0 is the compute substrate an always-on agent would run on. These are complementary layers, not substitutes.

**Schema gap:** `compute_duration: [ephemeral | session | persistent]`; `agent_self_provisioning: bool`; `vm_persistence: [none | suspend | always-on]`; `gpu_on_demand: bool`.

## Preliminary interpretation

- **Level 7 — Infrastructure / agent compute substrate** (primary): machine0 is agent compute infrastructure — not a harness, not a runtime, not a capability layer. It provides the VM substrate on which agents run and which agents can provision dynamically. Closest structural analogue: e2b (L7, ephemeral sandbox for agents), but on the opposite end of the persistence spectrum.
- **Level 4 secondary (MCP capability):** the MCP server mode makes VM provisioning callable as a tool from within agent sessions — an agent can provision its own compute environment as a tool call. But the primary function is infrastructure.
- Not L2 (harness): machine0 does not orchestrate agent tasks; it provides the VMs on which agent harnesses run.
- Not L1 (base runtime): machine0 does not implement an agent runtime; it is the compute on which runtimes run.

## Claims to verify

- **99.99% uptime SLA:** an uptime guarantee is a commercial commitment, not a technical specification. What is the SLA remediation (credits, refund)? What counts as "downtime" (full VM unavailability vs. degraded performance)?
- **Profile injection compatibility:** "Claude Code and Codex will pick them up automatically" — is this via the standard `~/.claude/settings.json` and environment variable injection, or does it require machine0-specific harness modifications? The claim implies a convention-based injection model.
- **MCP server stability:** MCP server is listed as a feature; is it fully implemented or in preview/beta? How does the MCP server handle VM state transitions (starting, suspending, terminating) in the middle of an agent tool call?
- **NixOS agent compatibility:** NixOS uses the Nix package manager rather than apt/brew. Agents that depend on apt-based workflows (e.g., `sudo apt install`) will fail on NixOS unless the agents are configured for Nix. The claim of "one-command rollbacks" requires agents to use Nix tooling.
- **GPU provisioning latency:** for agents that dynamically provision GPU VMs for a subtask, the provisioning latency (time from MCP `start` call to GPU-accessible VM) affects whether on-demand GPU is practical for short-burst compute.

## Status

- Commercial SaaS product (YC S26); no open-source repository identified
- **No registry entry:** infrastructure compute product; no `agents.json`/`llms.json`/`hardware.json` schema mapping; published pricing available ($0.013/hr–$39.336/hr) but no agent/LLM performance benchmarks to score against
- **No canonical section change:** single signal for "persistent agent compute infrastructure with native MCP provisioning"; two-signal rule applies. e2b covers the ephemeral end of the spectrum; machine0 is the first tracked persistent end
- **Watch for:** open-source release of machine0 CLI tooling; second independent product in "persistent agent-provisioned VMs" category; adoption by OpenClaw/Hermes teams as official recommended compute; GPU benchmarks for agent inference workloads on machine0
