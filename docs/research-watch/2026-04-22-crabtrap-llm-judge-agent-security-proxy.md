# Research Watch: CrabTrap — LLM-as-a-Judge HTTP Proxy for Agent Security

- Repo/Link: https://brex.com/blog/crabtrap
- Source: Hacker News (55 pts, 2026-04-22)

## Why this is worth watching
CrabTrap is an LLM-as-a-judge HTTP proxy that sits between an AI agent and its downstream actions (API calls, tool use), evaluating each request before allowing it through. Brex (a fintech company with production AI workloads) open-sourced it to address the gap between building an agent and running it safely in production. This is a new infrastructure sub-category: **production-side agent output validation**, distinct from input-side guardrails (system prompts) and evaluation harnesses (offline benchmarks).

## What stands out immediately
- Intercepts agent HTTP calls in real time; LLM judge decides allow/deny/rewrite
- Fintech provenance: designed for environments where agent mistakes carry financial or compliance risk
- Addresses a gap not covered by existing Level 4c tools in this taxonomy (serena, rtk, chrome-devtools-mcp are all capability-adding, not safety-enforcing)
- Architecturally closer to a WAF for agents than a memory or skill layer

## Why clawfit should care
- Fills a missing sub-type at Level 4c: **agent output/action guardrails** (as distinct from input validation or audit logging)
- Directly relevant to `governance_need: hard` profiles — large-org exec/compliance scenarios where agents have write access to systems
- kontext-cli (2026-04-15) covers credential scoping; CrabTrap covers semantic validation. Together they sketch a governance infrastructure layer below harnesses
- If this pattern matures, clawfit may need a `safety_infrastructure` feature flag alongside `governance` and `team-sharing`

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infrastructure** (safety-enforcement sub-type)

## Status
- Early signal; blog post only, no standalone GitHub repo confirmed yet
- Revisit when repo is public and star count is available
- Monitor: does this generalize beyond HTTP/REST to shell-tool interception?
