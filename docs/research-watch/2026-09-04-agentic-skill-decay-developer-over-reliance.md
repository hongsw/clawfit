# Research Watch: Agentic Skill Decay — Developer Over-Reliance Signal

- Repo/Link: https://addyo.substack.com
- Source: GeekNews

## Why this is worth watching
Addy Osmani (author of addyosmani/agent-skills, 92k★) argues that AI coding agents bypass the deliberate iteration loops that build and reinforce developer competency — creating a skill decay pattern where heavy agent users become dependent on agent output quality rather than understanding code correctness independently. This is the individual-level complement to The Agentic Awakening (2026-09-02), which addressed org-level coordination gaps.

## What stands out immediately
- Source is the same author as addyosmani/agent-skills — the argument is internal to the agent ecosystem, not external criticism
- Core mechanism: bypassing micro-iteration (write → fail → debug → understand) reduces deliberate practice that builds deep knowledge
- The concern is not about agents replacing jobs but about agents removing the learning signal embedded in failure
- Paired on the same GeekNews page as "Protecting Engineers' Skills in AI Era" (IEEE, HN 22 pts)

## Why clawfit should care
Skill decay has an implicit impact on org_fit scoring: a team whose developers have degraded foundational skills may need tools with stronger guardrails (explain mode, step-by-step reasoning output) rather than tools optimized for speed. The `growth_horizon` dimension in org_fit currently distinguishes `deepen` vs `stable` vs `explore` — skill decay is an argument for surfacing "skill-preservation" recommendations as a distinct sub-type under `deepen`. No immediate schema change warranted, but informs a future `learning_objective` or `guardrail_level` dimension.

## Preliminary interpretation
Current best reading:
- **Ecosystem discourse signal** — not a tool, harness, or model
- Complements The Agentic Awakening (L3 team coordination gap) at the individual L1/L2 usage layer

## Status
- Single blog post, no GitHub repo
- Building a pattern with The Agentic Awakening (2026-09-02): two consecutive signals about negative second-order effects of agent adoption, from within the agent ecosystem itself
- Flags `learning_objective` as a candidate future dimension for org_fit scoring
