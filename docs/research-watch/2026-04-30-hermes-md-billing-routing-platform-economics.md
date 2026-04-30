# Research Watch: HERMES.md Claude Code Billing Routing

- Repo: https://github.com/anthropics/claude-code/issues/53171
- Also see: https://github.com/anthropics/claude-code/issues/53262

## Why this is worth watching
Anthropic introduced a server-side content classifier on 2026-04-04 that routes Claude Code sessions to pay-as-you-go "extra usage" billing when the classifier detects harness-usage patterns — including the presence of the string "HERMES.md" in git commit history. The mechanism is silent, server-side, and pattern-based, not consent-based: users are reclassified without notification at the point of tool invocation. With 960 HN points and public commentary from Theo (t3.gg) and ThePrimeagen, this is among the highest-visibility platform-trust incidents in the Claude Code lifecycle to date.

## What stands out immediately
- The billing reclassification was introduced 2026-04-04, the same date Anthropic began blocking Pro/Max subscribers from routing flat-rate plan usage through third-party harnesses such as Hermes Agent
- The classifier operates on content patterns — the string "HERMES.md" appearing in git commit history is documented as sufficient to trigger reclassification, with no harness actively running required
- An affected user lost $200+ while 86% of their prepaid plan capacity remained unused; Anthropic declined to issue a refund (reported in issue #53171)
- The classifier is server-side: the Claude Code client does not expose any flag, log entry, or UI indicator that reclassification has occurred
- The scope of pattern matching beyond "HERMES.md" is not publicly documented — whether filenames like AGENTS.md, CLAUDE.md, or other harness-adjacent strings trigger similar routing is unconfirmed (claim to inspect, not validated)
- Issue #53262 appears to document a second affected user, suggesting this is not a single edge case
- Viral reach includes Theo (t3.gg) and ThePrimeagen, both with large developer audiences — reputational surface is disproportionate relative to the number of confirmed cases

## Why clawfit should care
clawfit's `monthly_budget` and `governance_need` profile axes both assume that billing tier is a stable, user-controlled property. This incident introduces a new failure mode: **billing-routing risk** — the cost of operating on a given platform can change silently based on artifacts present in the project's git history, independent of user intent or current tool usage.

Concrete implications:
1. The `budget_fit` scoring dimension currently treats `pricing_tier: paid` as a static property of an agent entry. A classifier-driven billing tier is not static — it is a function of the project's history. This is a new risk axis that `budget_fit` does not model.
2. Any clawfit user profile that has previously used a harness (Hermes, and possibly others) and has that harness's configuration file in commit history is a candidate for silent reclassification, even after switching to direct Claude Code usage.
3. The `governance_need: hard` dimension — currently used to filter for auditability and data-handling guarantees — should arguably also flag this category of billing-transparency risk. Governance is not only about data; it extends to cost predictability under the same platform contract.
4. The 2026-04-22 signal (Claude Code removed from Pro tier) and this signal are architecturally related: both are Anthropic platform-economics interventions at the Level 3 governance layer. Together they represent a pattern — not isolated incidents.

## Preliminary interpretation
Current best reading:
- **Level 3 — Team harness / executable SSOT / governance layer**: The classifier enforces a billing boundary between first-party and third-party harness usage. This is a governance-layer mechanism: it controls which execution path is permitted under a given commercial contract, and it does so by inspecting project artifacts (commit history) rather than runtime state.
- Secondary relevance: **Level 2 — Meta wrappers / harnesses**: Any harness that causes a configuration file to appear in git history (Hermes Agent, and potentially others) now carries downstream billing risk for users who later migrate away from that harness.
- This is not a tool signal — no registry entry is warranted. It is a platform-economics enforcement signal that changes the risk profile of Level 2 and Level 3 entries in general.

Notable distinction from prior signals: the 2026-04-06 Agentic AI Foundation signal documented governance moving toward multi-stakeholder openness (MCP donated to Linux Foundation). This signal documents the inverse — unilateral, opaque governance enforcement by a single platform vendor. Both are Level 3 governance signals; they point in opposite directions.

## Status
- Two confirmed GitHub issues (2026-04-30); refund denied in at least one case. Community reaction is high-signal (960 HN points).
- No registry edit warranted. The `pricing_tier` schema field and `governance_need` filter axis should be reviewed for a `billing_routing_risk` boolean or equivalent — flag for schema discussion alongside the `pricing_tier: premium` discussion from 2026-04-22.
- Monitor: whether Anthropic documents the full classifier pattern list, and whether any harness other than Hermes Agent is confirmed to trigger reclassification.
- Note for reference-levels.md Level 3: platform-enforced billing routing via content classification is a new governance sub-pattern distinct from harness licensing or access control — worth capturing if a second incident confirms the pattern is durable.
