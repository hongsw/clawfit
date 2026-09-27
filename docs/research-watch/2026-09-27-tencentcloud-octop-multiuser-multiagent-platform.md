# Research Watch: TencentCloud Octop — Self-Hosted Multi-User Multi-Agent AI Platform

- Repo: https://github.com/TencentCloud/Octop (⭐5,240)
- Source: GitHub Trending weekly (+951 this week)

## Why this is worth watching

Octop targets a gap between personal agent tools (Claude Code, Codex — single user) and enterprise orchestration platforms (CrewAI — developer-configured pipelines): team-level, self-hosted agent deployment where each user maintains a personal "expert team" and coordination happens through a shared control plane. The `AgentTeams (Beta)` feature — where a coordinator schedules multiple domain specialists for complex tasks — is the most structurally interesting piece, as it represents a bottom-up org-topology model rather than top-down workflow design.

## What stands out immediately

- Per-user "expert team" model: each user configures their own specialists rather than sharing a global agent pool — reduces configuration coupling between team members
- `AgentTeams (Beta)`: a coordinator agent schedules expert agents; task complexity determines whether single-expert or multi-expert path is taken
- Expert sharing/publishing: users can publish agent configurations for reuse within the deployment — a lightweight "agent marketplace" within an org's own instance
- ACP (Agent Client Protocol) for IDE integration — compatible with Claude Code's protocol layer
- IM channel normalization via Octop Gateway: Feishu, DingTalk, WeChat, Telegram, Discord, WeCom — single agent backend serves all channels
- 16 MBTI personality templates for system prompt defaults — unusual; signals consumer/household target market alongside enterprise
- Full local data storage (`~/.octop/` default): privacy-first posture against SaaS alternatives
- Supports OpenAI-compatible, DashScope (Qwen), and Ollama backends — China-ecosystem model support is explicit

## Why clawfit should care

Octop represents the **second signal** (alongside OpenRig, same scan day) for "declarative agent team topology configuration" — the pattern where team structure is defined as a first-class config artifact, not assembled imperatively in code. The distinctive axis here is **multi-user shared deployment**: Octop is explicitly designed for teams, not solo use, while most L2 harnesses assume a single developer instance. For clawfit scoring, this introduces an `org_deployment_model` axis: some tools are personal agents, others are team platforms — and recommendation quality depends on the org scale. A 10-person team deploying a self-hosted agent platform has different requirements than a solo developer choosing a base agent.

## Preliminary interpretation

Current best reading:
- **Level 2/3 — Harness + Team Platform**: primary L3 (team-scale deployment, multi-user control plane) with L2 characteristics (wraps underlying model providers without being a base runtime)
- The `AgentTeams` coordinator-specialist model is L3 governance at the task level — not just configuration, but runtime task decomposition

## Claims to verify

- `AgentTeams` is marked Beta — maturity and stability unknown; coordinator scheduling logic not yet public
- Expert sharing within deployments sounds useful but sharing scope (within-team vs. cross-org) is unclear
- MBTI personality templates as default system prompts suggests consumer-facing product thinking that may conflict with enterprise hardening requirements
- DashScope (Qwen) as a first-class backend confirms China-domestic market targeting; validate whether international model support is maintained consistently
- 5,240 stars with 635 forks is healthy but jump (+951 this week) may reflect GitHub Trending amplification rather than organic adoption

## Status

- Tracking; 5,240 stars — above registry threshold but no deterministic cost/latency data (delegates to user-configured backend)
- Registry ineligible: backend-agnostic platform; cost/latency depends on org's model configuration
- **Second signal for "declarative agent team topology" pattern** alongside OpenRig (same scan day) — cross-date confirmation pending for canonical sub-type consideration
- `AgentTeams` coordinator-specialist model is a genuine signal for coordinator-topology sub-type in L3, distinct from workflow-based orchestration (CrewAI, LangGraph)
