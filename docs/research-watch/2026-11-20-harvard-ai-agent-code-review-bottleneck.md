# Research Watch: Harvard Study — AI Coding Agents Shift Bottleneck to Code Review

- Repo/Link: https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/
- Source: GeekNews front page

## Why this is worth watching
A Harvard study of 655 companies found that after adopting AI coding agents, code output volume increased but the bottleneck moved from writing to code review and deployment. This is the first large-scale empirical study confirming an org-level workflow effect of agent adoption: agents do not remove the bottleneck, they move it downstream.

## What stands out immediately
- 655-company dataset — large enough to generalize across org sizes and industries
- Agents increased raw code output significantly
- Bottleneck shifted to code review and deployment pipeline
- Implies that orgs need to invest in review tooling (plannotator, Reticle, OpenQodex) alongside agents
- Directly challenges the "just add an agent and ship faster" narrative

## Why clawfit should care
This finding has direct implications for clawfit's org-fit scoring. `org.growth_horizon: scale` profiles that add coding agents need concurrent investment in L5 (evaluation) and L2 (review-integrated harnesses). The `governance_need: hard` scoring should weight review-supporting features more heavily. Tools like plannotator, Reticle, and OpenQodex that sit at the review layer become higher-priority recommendations. First empirical signal for "agent adoption without review infrastructure creates downstream bottleneck."

## Preliminary interpretation
Current best reading:
- **Level 3 / Level 5 signal** — governance gap (L3) and evaluation layer (L5) become critical when agents scale output; not a tool entry

## Status
- First scan 2026-11-20 (GeekNews)
- Not a tool — governance/research signal only
- 📡 Watch: second independent study or vendor survey confirming the same downstream bottleneck pattern would justify adjusting `growth_horizon: scale` scoring to require a review-layer tool recommendation alongside any coding agent
