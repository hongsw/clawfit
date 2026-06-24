# Research Watch: Agentic Testing — Where Agents Fit in the E2E Testing Stack (Slack Engineering)

- Repo/Link: https://slack.engineering/agentic-testing-where-agents-fit-in-the-e2e-testing-stack/
- Source: GeekNews

## Why this is worth watching
Slack Engineering published a data-backed evaluation of AI agents for E2E UI testing with 200+ automated runs across three execution models (Playwright MCP, Playwright CLI, AI-generated tests), making it one of the more rigorous practitioner studies on agent reliability in production workflows. The cost finding — $15–30 per agent run vs. pennies for deterministic scripts — is a concrete constraint that directly maps to clawfit's budget and latency dimensions. The conclusion that agents occupy a new "exploration layer" above the traditional testing pyramid is a structural claim worth tracking as the QA tooling cluster matures.

## What stands out immediately
- Three execution models compared: Playwright MCP (0–12% failure rate), Playwright CLI (12–20%), AI-generated Playwright tests (8% simple / 48% complex)
- Models tested: Claude Sonnet 4.5, Opus 4.6, Haiku 4.5 — multi-model comparison at the same task
- Only ~20% of agent runs followed identical action sequences despite reaching correct outcomes; agents adapt paths rather than enforce them
- 40–85 token turns per run; cost driver is browser snapshot retransmission across turns, not model inference alone
- Prompt caching and context compaction were identified as cost mitigations but not yet implemented — baseline costs are therefore a ceiling, not a floor
- Effective use cases: exploring complex UI behaviors, debugging flaky workflows, reproducing production bugs
- Ineffective use cases: high-frequency CI regression testing (cost-prohibitive), multi-window / multi-workspace flows

## Why clawfit should care
This is the third independent QA-agent signal in this cycle (after TesterArmy 2026-06-19 and alibaba/open-code-review 2026-06-22), each arriving from a different vantage — YC startup, OSS enterprise tool, and now a practitioner benchmark from a major product company. Together they confirm that `task: qa` is splitting into at least two sub-types: **regression/CI testing** (cost-sensitive, deterministic, Playwright-script model) and **exploratory/debugging testing** (cost-tolerant, adaptive, agent model). clawfit's current `latency` and `budget` filters treat these as the same task. The $15–30 per-run cost data gives a defensible threshold for when to surface agent-QA tools vs. script-based tools in recommendations.

## Preliminary interpretation
Current best reading:
- **Level 1 — Specialized Base Agent (browser-automation QA sub-type)** — agents operate an autonomous loop over UI state; Playwright MCP is the substrate, the agent is the primary actor
- **Level 4 secondary** — Playwright MCP is a capability/tool-use layer (L4) consumed by the agent; the blog post evaluates L1 behavior but the tooling stack is L4
- The "exploration layer above the testing pyramid" framing does not map cleanly to a new level — it is a task-scoping pattern within L1, not a structural new layer

## Status
- First signal — hold (engineering blog post, no open-source repo, no star count)
- Analytically strong: 200+ runs, multi-model, quantified failure rates and per-run cost — more rigorous than most practitioner writeups
- Reinforces the `task: qa` sub-type split; flag for schema analyst review before next registry cycle
- Promotion criterion: companion open-source tooling OR a second practitioner benchmark reproducing the cost/reliability findings
