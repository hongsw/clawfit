# Research Watch: toris-agent — Evidence-Receipt Audit CLI for AI Agents

- Repo/Link: https://www.npmjs.com/package/toris-agent
- Source: GeekNews

## Why this is worth watching
toris-agent is a local CLI that documents AI agent execution through structured plan-run-verify stages and leaves an "evidence receipt" for each completed task. It addresses the auditability gap in agentic workflows: humans commissioning agent work cannot easily confirm *what* the agent actually did, only its outputs. An evidence-receipt layer is an emerging governance primitive.

## What stands out immediately
- Three-stage model: **plan** (what the agent intends to do), **run** (execution trace), **verify** (outcome confirmation)
- Produces a per-task audit artifact ("evidence receipt") that can be stored, shared, or reviewed
- Local CLI — no cloud dependency; fits `network: offline` and `data_sensitivity: confidential` profiles
- npm package suggests Node.js ecosystem; likely composable with existing agent harnesses

## Why clawfit should care
This fills a cross-cutting governance role (L3 candidate) that currently has no entry in the registry: agent execution auditability without requiring a full observability platform like Langfuse. The plan-run-verify receipt pattern is a lightweight alternative to full observability dashboards and maps directly to `governance_need: hard` profiles in clawfit's scoring. The `offline_mid_codegen` and `large_exec_research` profiles both have high governance requirements and would benefit from this kind of tooling.

## Preliminary interpretation
Current best reading:
- **Level 3 — Agent governance / behavior control layer** (execution audit primitive)
- Possible L5 secondary — receipt as ground-truth for agent evaluation

## Status
- First signal — GeekNews mention; npm package exists but details unverifiable (403 at fetch time)
- Registry candidate pending verification of star count, license, and evidence format details
- Schema watch: `audit_trail: bool`; `plan_run_verify: bool`; `receipt_format: [json | markdown | html]`
