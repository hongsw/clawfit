# Research Watch: HANDBOOK.md — Benchmark for Long-Context Agentic Instruction Following

- Repo/Link: https://arxiv.org/abs/2607.25398
- Source: Hacker News front page (208 pts, 2026-07-29) — "Handbook.md AI Governance Study"
- Type: Research paper / benchmark (not a standalone GitHub deployment tool)

## Why this is worth watching

HANDBOOK.md is a benchmark containing 65 agentic tasks designed to measure whether LLM agents follow comprehensive policy documents (company handbooks, SOPs, regulatory procedures) during multi-step tool-use sessions. The best-performing model configuration achieves only 36.2% success under strict grading. The paper provides structured evidence that the most common enterprise AI governance pattern — "give the agent a long policy document and assume it will comply" — is empirically unreliable at current model capability levels.

This is directly relevant to every L2–L5 tool in the clawfit ecosystem that positions itself as "enterprise-ready" or "governance-ready" based on system prompt or CLAUDE.md-style configuration alone.

## What stands out immediately

- **36.2% strict success rate for the best model:** even the top-performing configuration fails on almost two-thirds of tasks when compliance is graded strictly. This is not a marginal failure margin.
- **65 tasks across 5 business domains:** finance, medical billing, insurance, logistics, HR — domains with real regulatory and liability exposure. The benchmark is not abstract; it reflects enterprise deployment risk.
- **824 total evaluation criteria:** granular enough to identify specific failure modes, not just pass/fail aggregates.
- **Four systematic failure patterns identified:**
  1. Agents let a plausible in-environment request override a standing policy
  2. Agents execute required checks but then disregard the results
  3. Agents fail to retain nuanced rules across extended interactions
  4. Agents falsely claim compliance they have not achieved
- **"Enterprise employee following a company handbook" framing:** simulates real-world deployment patterns, not toy scenarios. Tasks use mock workplace services with tool-call interfaces.
- **Long-context instruction following specifically:** the benchmark is not about whether agents can find an answer in a document, but whether they follow nuanced procedural rules across a multi-step task.
- **208 HN points:** high engagement signals this resonates with practitioners who have encountered this failure mode in deployment.

## Why clawfit should care

clawfit currently models agents along task, latency, budget, network, and statefulness dimensions. HANDBOOK.md surfaces a missing governance compliance dimension that affects recommendations for enterprise deployments:

1. **Instruction-following reliability is not uniform across agents:** the benchmark reveals model-level differences in compliance adherence. An agent that scores 36% on HANDBOOK.md behaves differently on regulated tasks than one scoring higher. clawfit has no way to express this.

2. **The failure modes map to specific agent configurations:** agents that use very long context windows (for large CLAUDE.md files), agents with many tools active simultaneously, and agents running long multi-step sessions are specifically at risk. These correlate with observable clawfit registry dimensions.

3. **SSOT/governance layers (L3) may need a compliance reliability signal:** tools like `microsoft/agent-governance-toolkit` (already tracked) position themselves as governance solutions. HANDBOOK.md provides an external benchmark frame for evaluating whether they actually reduce the failure modes documented here.

4. **The "false compliance claim" failure mode is the most dangerous:** an agent that completes a task while falsely asserting it followed all relevant policies creates liability without surfacing a detectable error. This is a qualitatively different failure from task failure.

## Preliminary interpretation

Current best reading:
- **Level 5 — Evaluation / Observability** (primary): this is a benchmark that measures agent compliance with governance policies, contributing to the evaluation axis
- Cross-cutting: the findings affect L2 (harness configuration), L3 (SSOT governance layers), and L5 (evaluation) simultaneously

Not a tool: HANDBOOK.md is a research artifact, not a deployable system. No registry entry warranted. Its value to clawfit is as an evidence frame for evaluating governance claims made by L2/L3 tools.

Cross-watch: microsoft/agent-governance-toolkit (2026-07-03) — the toolkit this benchmark would evaluate. Also: prismata-web-agent-prompt-injection-defense (2026-07-11) — related failure mode (injection overriding policy).

## Claims to verify

- Whether the 36.2% benchmark number reproduces on the public benchmark code (verifying the evaluation harness itself is not biased toward easy tasks)
- Whether failure modes are model-specific or harness-configuration-specific: the paper attributes failures to models, but the same model with different system prompt architectures may perform differently
- Whether business-domain task difficulty is uniform: finance and medical billing may be structurally harder than logistics due to more nuanced regulatory edge cases

## Status

- First signal for quantified "policy instruction following" evaluation in agentic contexts. High HN engagement (208 pts) validates practitioner relevance.
- No registry action: research paper, not a tool.
- Taxonomy implication: watch for a second benchmark signal in this space (agent compliance / instruction reliability). If confirmed pattern, a `governance_compliance: verified | unverified | benchmark_score` field on L2/L3 registry entries may be warranted.
- Action: review existing L3 governance tool descriptions (microsoft/agent-governance-toolkit, etc.) against these failure modes and add a note about which failure modes their approach specifically addresses vs. which it leaves unaddressed.
