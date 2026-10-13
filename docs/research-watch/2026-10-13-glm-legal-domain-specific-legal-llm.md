# Research Watch: GLM-Legal — Domain-Specific Legal LLM

- Repo/Link: https://z.ai/blog/glm-legal
- Source: Hacker News front page (400 points, 2026-10-13)

## Why this is worth watching
GLM-Legal is a domain-specific variant of the GLM model family (Zhipu AI / z.ai) fine-tuned for legal reasoning, case law citation, and contract analysis. With 400 HN points it attracted significant developer and practitioner attention. This is the first GLM variant with explicit legal domain positioning — distinct from GLM 5.1/5.2/5.3 general-purpose releases and from Harvey AI (a legal agent product, not an LLM) and from Korean Law MCP (an API surface, not a model).

## What stands out immediately
- Fine-tuned specifically on legal corpora: case law, statutes, contracts, regulatory filings
- Positioned for legal research, contract review, compliance Q&A
- Published by z.ai, the commercial arm of Zhipu AI (same org as GLM-5.x series)
- Legal domain LLMs have stricter accuracy and hallucination requirements than general coding agents

## Why clawfit should care
This is a third signal for "professional domain primary_task missing from org_questions.json" (after mobile-development 2026-10-10 and industrial datasheets/PartsPlan 2026-10-12). A `primary_task: legal` dimension is now confirmed across three independent signals (Harvey AI benchmark 2026-08-08, Korean Law MCP 2026-04-07, GLM-Legal 2026-10-13). The `org_fit.tasks` taxonomy in tools_registry.json does not yet include `legal`, `compliance`, or `contract-review` as task types. If GLM-Legal gains traction (confirmed star count pending), a registry entry with `tasks: ["research", "qa"]` would be a poor fit — it warrants a purpose-built task dimension.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base LLM** (domain-specialized base model)

## Status
- Third signal for "professional domain primary_task gap" in org_questions.json
- Three-signal rule met: `legal` task type is a confirmed gap; candidate for org_questions.json update
- Monitor: open-weight availability, pricing, self-hosted inference feasibility for `governance_need: hard` legal orgs
- Note: Harvey AI (2026-08-08) covers the agent/product layer; GLM-Legal covers the base model layer — complementary, not duplicate
