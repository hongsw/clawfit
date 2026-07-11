# Research Watch: Prismata — Cross-Site Prompt Injection Confinement for Web Agents

- Repo/Link: https://arxiv.org/abs/2607.08147
- Source: Hacker News (front page)

## Why this is worth watching
As web agents (browser-control, crawl-and-act) become mainstream, prompt injection from hostile web content is the primary attack surface. Prismata is a peer-reviewed defense mechanism specifically for this class of attack. It directly relates to how clawfit should score tools like `chrome-devtools-mcp`, `browser-harness`, and `crawl4ai` for `data_sensitivity: confidential` or `governance_need: hard` profiles.

## What stands out immediately
- Addresses cross-site prompt injection: attacker-controlled web content hijacking agent instructions
- "Confinement" approach: limits what injected instructions can cause agents to do
- Peer-reviewed (arXiv preprint); not a vendor blog post
- Directly applicable to any agent that browses or processes external web content
- Complements existing agent sandboxing approaches (scope-bounded execution, authorization-model)

## Why clawfit should care
The `governance_need: hard` dimension in clawfit's org_fit schema currently has no defense-layer tooling associated with it. Prismata defines what "hardened web agent" means at a mechanism level. Tools that implement confinement-style injection defenses should score higher for `governance_need: hard` + `data_sensitivity: confidential` profiles. This also reinforces the `task: security-testing` category for evaluating tools like Shannon and Strix against web-facing scenarios. Schema watch: `injection_defense: none | partial | confined`.

## Preliminary interpretation
Current best reading:
- **Level 3 — Behavioral governance / security constraint** (primary)
- **Level 5 — Evaluation methodology** (secondary, defines what to test for)

## Status
- First signal 2026-07-11 (arXiv preprint; no deployable artifact)
- No registry entry: pure research artifact, no implementation to recommend
- Monitor: reference implementations; adoption by browser-harness or crawl4ai maintainers
- Schema watch: `injection_defense: none | partial | confined`
