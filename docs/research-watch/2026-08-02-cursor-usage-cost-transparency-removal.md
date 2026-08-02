# Research Watch: Cursor Removed Cost Information from Usage Page

- Repo/Link: https://forum.cursor.com/t/usage-page-to-token-amount-what/167153
- Source: Hacker News (2026-08-02, 293 pts, 127 comments)

## Why this is worth watching
Cursor silently removed per-token cost breakdowns and token counts from its usage dashboard and CSV export. At 293 HN points and 127 comments, this is the highest-engagement developer grievance signal of the day. It directly surfaces the tension between commercial AI tool opacity and the developer expectation of cost observability — a dimension that clawfit's `monthly_budget` filter relies on but cannot fully model for proprietary tools.

## What stands out immediately
- Cursor removed the ability to see which models consumed which tokens and at what cost
- The CSV export no longer contains token amount columns developers relied on for billing reconciliation
- Community reaction split: some attribute it to a pricing model shift (moving to unlimited flat tiers), others to deliberate opacity
- This follows the Tokenless signal (2026-07-30) which also highlighted model-switching cost opacity
- Proprietary AI tools (Cursor, GitHub Copilot) have weaker cost transparency guarantees than open or API-direct tools

## Why clawfit should care
clawfit recommends tools partly on `monthly_budget` fit. For proprietary IDE agents like Cursor, the actual per-task cost is now unverifiable — which makes the `budget: low` filter less reliable when recommending commercial closed tools. This strengthens the case for adding a `cost_transparency: [metered | opaque | flat-tier]` schema field. Transparent cost metering is a genuine org-fit dimension for teams with finance approval workflows. First signal for "proprietary agent cost opacity" as a recommendation quality risk.

## Preliminary interpretation
Current best reading:
- **Cross-cutting governance signal** — not a tool but a behavioral signal about proprietary tooling opacity affecting `budget` filter reliability
- Affects L1 closed-source agents (Cursor, GitHub Copilot) most directly

## Status
- First signal; monitoring for similar events from other commercial AI coding agents
- Schema gap candidate: `cost_transparency: [metered | opaque | flat-tier | open-source]`
