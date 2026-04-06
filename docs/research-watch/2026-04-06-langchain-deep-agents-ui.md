---
# Research Watch: langchain-ai/deep-agents-ui — web UI for DeepAgents

- Repo: <https://github.com/langchain-ai/deep-agents-ui>
- Related: <https://github.com/langchain-ai/deepagents>

## Why this is worth watching
The UI layer of a major open-source harness is being developed in parallel with the engine — this is a pattern shift. Previously, open-source agents relied on terminal UIs or third-party GUIs. LangChain shipping a dedicated Next.js UI signals that the **human interface layer is now a first-class concern** for harness projects, not an afterthought.

## What stands out immediately
- **Stack:** Next.js + TypeScript (84%), connects to LangGraph deployment via HTTP
- **Client-server split:** frontend on :3000, agent backend on :2024
- **Debug capabilities:** step-through mode, file operation monitoring, execution trace view
- **LangSmith integration:** optional observability layer
- **1.5k stars, 307 forks** — smaller than the engine but actively adopted
- **Pattern:** mirrors Claude Code's web/desktop companion trend (cf. `deep-agents-ui` ↔ Claude Code desktop app)

## Why clawfit should care
This repo, combined with deepagents, shows a **two-repo harness pattern** emerging: engine + UI shipped separately but designed together. clawfit should track this as an architectural pattern for the Level 6 layer. The web UI + LangGraph backend combination may become a template for future harness projects.

## Preliminary interpretation
- Primary: **Level 6 — Human interface / voice / multimodal layer** (web UI surface)
- Secondary: depends on deepagents (Level 1/2) — this is its interface skin

## Status
- Tracked as companion to deepagents watch.
- No standalone registry entry needed — represents a UI pattern, not an agent/LLM/hardware.
