# Research Watch: HiClaw — Matrix-protocol multi-agent OS with human-in-the-loop

- Repo: <https://github.com/agentscope-ai/HiClaw>
- Site: <https://hiclaw.io/>
- Mirrors / forks: `alibaba/hiclaw`, `higress-group/hiclaw` (same codebase, multiple org-affiliated mirrors)
- Source: GitHub Trending Daily (Go), 2026-04-28
- Stars: ~4,300 total / +29 today
- Language: Go 40% / Shell 37% / Python 13%
- License: Apache-2.0

## Why this is worth watching
HiClaw is the first high-signal entry in this taxonomy that uses **Matrix** — a federated, open chat protocol — as the substrate for multi-agent task coordination. The dominant pattern for "agents in a chat room" so far has been closed enterprise platforms (Microsoft Teams BYOA on 2026-04-23, Slack-bot-style integrations). HiClaw inverts that: same problem (multi-agent coordination with humans visible in the loop), opposite distribution choice (open protocol, self-hosted server, zero SaaS dependency).

It is also notable for being **multi-runtime by design** — OpenClaw, QwenPaw, and Hermes Workers coexist in the same Matrix room — which makes it structurally a coordination layer rather than a wrapper around any one base agent.

## What stands out immediately
- **Matrix protocol as the agent bus.** Self-hosts a Tuwunel Matrix server + Element web client; no DingTalk / Lark / Slack / Teams integration needed.
- **Manager-Workers architecture.** A Manager agent orchestrates Worker agents inside a Matrix room; humans are first-class participants in the same room, not observers reading logs after the fact.
- **Heterogeneous runtime support claimed:** OpenClaw + QwenPaw + Hermes Workers in one room (claim to inspect — needs validation that all three actually interop in production, not just demoware).
- **Higress AI Gateway** centralizes credential routing — Workers carry only a consumer token ("badge"), never raw API keys or GitHub PATs. Compromised Worker cannot exfiltrate credentials. (Claim to inspect.)
- **MinIO shared object store** for inter-agent file exchange, framed as a token-cost reduction mechanism vs. passing files through chat messages.
- **v1.1.0 ships a K8s-native control plane** and a `hiclaw` CLI replacing shell scripts — productization signal, not just research code.
- **No explicit Slack/Teams competitive framing in the README.** Positioning is "self-hosted, zero vendor lock-in," not direct rivalry — which is itself a tell about the open-protocol vs. enterprise-platform fork.

## Why clawfit should care
clawfit's Level 3 already distinguishes harness/SSOT (Paperclip-style closed company orchestration) from team-workflow tooling. HiClaw forces a finer distinction inside Level 3:

- **Closed-SSOT orchestration** (Paperclip): proprietary org chart, single-vendor governance plane, opinionated stack.
- **Open-protocol federated orchestration** (HiClaw): Matrix as the coordination bus, multi-runtime by construction, governance enforced via gateway + room visibility rather than via a single SSOT.

This matches the Microsoft Teams BYOA signal (2026-04-23) on the **enterprise/closed** side and provides a missing **opensource/open-protocol** counterpart on the same problem. For `governance_need: hard` + `data_sensitivity: confidential` + `network: self-hosted` profiles, HiClaw fills a slot that closed enterprise integrations cannot — agent coordination without surrendering chat history to a SaaS vendor.

It also reinforces the human-in-the-loop axis as a Level 3 differentiator. HiClaw's "no hidden agent-to-agent calls — everything is visible and intervenable" is a stronger governance stance than orchestrators that surface only summaries to humans.

## Preliminary interpretation
Current best reading:
- **Level 3 — Team harness / executable SSOT / governance layer**, sub-pattern **open-protocol federated multi-agent coordination**
- Adjacent to Level 4c on the **credential-broker / gateway** axis (Higress component overlaps kontext-cli / Agent Vault territory) — but the gateway is a component, not the product
- Not a Level 1 base runtime — HiClaw does not ship its own agent; it coordinates other runtimes (OpenClaw, QwenPaw, Hermes)

Comparison axis to track:
- **Closed SSOT** (Paperclip) vs. **open-protocol federated** (HiClaw) as two viable Level 3 architectures
- **Enterprise chat-platform integration** (Teams BYOA) vs. **self-hosted open-protocol coordination** (HiClaw) as two distribution surfaces for the same multi-agent + human-in-the-loop problem

## What to validate later
- Does the three-runtime interop (OpenClaw + QwenPaw + Hermes) actually work cross-runtime, or is it parallel single-runtime support inside one UI?
- Real-world Matrix federation usage — are deployments using federation across orgs, or single self-hosted homeservers in practice?
- Higress credential-broker claim: badge-token isolation in production traffic, not just architecture diagrams.
- Adoption velocity beyond the +29/day signal — currently below registry threshold (5k stars).

## Status
- Research-watch entry only. No registry addition (team-OS coordination layer, schema-incompatible with agent/llm/hardware triples).
- No `docs/reference-levels.md` mutation today — single-vendor signal; revisit when a second open-protocol federated coordinator appears or HiClaw crosses 10k stars.
- Flag for re-evaluation as the open-protocol vs. closed-platform fork in Level 3 if a second high-signal Matrix-based or federated agent-coordination tool surfaces in the next ~30 days.
