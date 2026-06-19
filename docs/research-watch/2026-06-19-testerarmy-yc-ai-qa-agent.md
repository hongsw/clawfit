# Research Watch: TesterArmy (YC P26) — AI Agents for Web/Mobile QA

- Repo/Link: https://tester.army
- Source: Hacker News (Launch HN: YC P26)

## Why this is worth watching
TesterArmy is a YC P26 company launching cloud-hosted AI agents that test web and mobile applications using plain-English test descriptions instead of Playwright/Cypress test code. It launches real browsers (Playwright primitives + AI visual understanding), handles OAuth/OTP flows, and produces bug reports with screenshots and recordings. This is the first *QA-specialized cloud agent service* in this scan taxonomy that operates at the workflow level rather than the infrastructure level.

## What stands out immediately
- **Natural-language test definition**: describe user journeys in English, agents execute them
- **AI visual understanding**: "sees pages like humans" — catches layout issues Playwright scripts miss
- **Handles auth complexity**: OAuth, OTP, multi-step auth flows without special code
- **CI/CD integration**: targets GitHub/Vercel deployment pipelines
- Customers include Novu, CodeCrafters, HireVoice, Copyfy — early traction signals
- YC P26 (current batch) — active investment signal

## Why clawfit should care
The current registry has two security-testing agent entries (Shannon, Strix) but no functional/UX QA agent service. TesterArmy represents a distinct sub-type: *cloud-hosted agent QA service* at L1, analogous to Twill.ai (fire-and-forget coding agent) but for testing rather than code generation. Architecturally relevant because it decouples test authoring (PM-accessible plain English) from test execution (agent + browser), eliminating the test maintenance burden that blocks QA agent adoption. Direct relevance to clawfit's `primary_task: qa` scoring dimension.

## Preliminary interpretation
Current best reading:
- **Level 1 — Specialized Base Agent (cloud-hosted QA sub-type)**
- L1 primary (autonomous agent loop: read test description → browser → validate → report)
- Similar to Twill.ai (cloud delegation model) but for QA rather than code generation
- Distinct from Strix (shift-left security testing) and Shannon (pentesting) — this is functional/UX regression testing

## Status
- First signal — hold (proprietary SaaS, no public repo, no star count; YC batch is the main signal)
- Promotion criterion: public API documentation OR confirmed paying team usage by a company outside YC network
- Registry candidate: `tasks: [qa]`, `roles: [developer, pm]`, `network: online`, `setup_complexity: low`, `pricing_tier: paid`
