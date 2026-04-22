# Research Watch: Claude Code Removed from Pro Tier — Pricing Escalation Signal

- Repo/Link: https://bsky.app/profile/anthropic.bsky.social (announcement)
- Source: Hacker News (185 pts, 2026-04-22)

## Why this is worth watching
Anthropic has removed Claude Code from the $20/month Pro tier. Claude Code now requires Max ($100+/month), Team, or Enterprise plans. This is the first major pricing-layer change for Claude Code since its launch. For clawfit, the `budget_fit` dimension scores Claude Code as `pricing_tier: paid` — which previously aligned with Pro-tier budgets (~$20/month). That alignment no longer holds: `monthly_budget: medium` org profiles will now see Claude Code as potentially out of budget, pushing users toward free alternatives (OpenCode, Aider, Goose, Cline, Crush).

## What stands out immediately
- 185 HN points signals significant community reaction — notably higher than typical pricing announcements
- Free-tier-compatible alternatives (OpenCode, Aider, Continue, Goose, Cline) are all in the registry and will now rank higher for `budget_tier: low` or `budget_tier: medium` solo/small profiles
- Anthropic appears to be segmenting Claude Code into professional/enterprise positioning — consistent with the addition of Routines, Team, and Enterprise governance features
- Opens market space for open-source alternative runtimes that were previously second-choice due to Claude Code's accessible pricing

## Why clawfit should care
- The `pricing_tier: paid` for `claude_code` no longer accurately captures the cost reality for medium-budget solo developers
- Consider adding a `pricing_tier: premium` tier to the scoring schema to distinguish $20/month SaaS tools from $100+/month tools
- The change may accelerate adoption of OpenCode, Aider, and Cline for budget-constrained profiles — these tools' registry weights should not be adjusted (they're already scored correctly) but `claude_code` may need a pricing tier correction
- Claude Code Routines (already `pricing_tier: paid`, Pro/Max/Team/Enterprise) is unaffected — it was never at a $20 price point

## Preliminary interpretation
Actionable impact on registry:
- Short term: no code change needed; `paid` tier still applies
- Medium term: if clawfit adds `premium` pricing tier, `claude_code` would be a candidate, while Superwhisper and Cursor (also `paid`) would need audit
- Watch: does competitor pricing follow (Cursor, Continue, Cline)?

## Status
- Confirmed pricing change as of 2026-04-22
- No registry edit made today; flagged for schema discussion
