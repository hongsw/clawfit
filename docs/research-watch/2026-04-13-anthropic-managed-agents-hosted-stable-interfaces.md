# Research Watch: Anthropic Managed Agents — Long-Running Hosted Agents with Stable Interfaces

- Repo/Link: https://www.anthropic.com/engineering/managed-agents
- Source: GeekNews

## Why this is worth watching
Anthropic published an engineering article describing **Managed Agents** — a hosted agent pattern with stable interfaces that remain consistent independent of underlying model updates. This is architecturally significant: it separates the *agent interface contract* from the *model version lifecycle*, allowing products built on Claude agents to upgrade models without breaking agent behavior.

## What stands out immediately
- Stable interfaces decouple agent behavior specification from model releases
- Long-running hosted execution: agents can run for extended periods without session re-initialization
- Interface stability is a **governance and reliability primitive** — directly relevant to enterprise adoption
- Different from the harness-design-long-running-apps article (which covers sprint contracts + context reset); this covers hosted interface contracts
- Implies a new deployment topology: Anthropic-hosted stateful agents, not just stateless API calls

## Why clawfit should care
This introduces a new infrastructure layer between Level 1 (base agent runtimes) and Level 2 (harnesses): **Anthropic-managed stateful agent hosting**. For orgs with `governance_need: hard`, stable interfaces reduce regression risk from model updates. clawfit's statefulness scoring axis (`session` vs `stateless`) may need a third value: `managed_hosted` to capture this pattern. Also relevant: if managed agents become a first-class product, the "online vs cloud" network distinction matters more.

## Preliminary interpretation
Current best reading:
- **Level 2 — Hosted harness / managed orchestration layer** (Anthropic-first party)
- Governance-relevant: interface stability as a reliability primitive

## Status
- Primary Anthropic source — cite alongside harness-design-long-running-apps in Level 2 notes
- Flag for scoring-analyst: `managed_hosted` statefulness value consideration
