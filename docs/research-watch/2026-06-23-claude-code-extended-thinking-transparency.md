# Research Watch: Claude Code Extended Thinking — Audit Trail Transparency Gap

- Repo/Link: https://patrickmccanna.net (article: "The text in Claude Code's 'Extended Thinking' output is not authentic")
- Source: Hacker News (265 pts, 185 comments)

## Why this is worth watching
Discovery that Claude Code's extended thinking blocks (Ctrl+O) contain only a ~600-character encrypted signature — the actual reasoning is not exposed to users, Anthropic holds the decryption key, and the visible thinking is a summary rather than authentic step-by-step reasoning. 265 HN points signals significant developer concern.

## What stands out immediately
- `thinking` blocks returned by the Claude API contain only an opaque signature; no readable reasoning text in local session logs
- The API returns a **summary** of reasoning, not the reasoning itself — full thinking requires an enterprise agreement with Anthropic
- Users cannot build genuine audit trails of agent decision-making from local files alone
- Directly affects promises of "explainability" or "auditability" made to stakeholders when deploying Claude Code in enterprise contexts
- This is Fable/Opus extended thinking behavior; standard (non-thinking) mode is unaffected

## Why clawfit should care
clawfit's `governance_need: hard` scoring dimension recommends tools based in part on their auditability. Claude Code currently scores well for large enterprise profiles partly because of its structured session logging. This finding narrows that advantage: **session logs do not constitute a full reasoning audit trail** unless the team has an enterprise agreement with Anthropic. Two impacts: (1) `data_sensitivity: confidential` + `governance_need: hard` profiles should be warned that extended thinking transparency is enterprise-gated; (2) tools like `re_gent` (L5 prompt-attribution VCS, 2026-06-16) gain relative standing for teams needing genuine action-level provenance.

## Preliminary interpretation
Current best reading:
- **Level 1 ecosystem transparency signal** — affects metadata confidence for Claude Code's audit characteristics
- **Level 5 secondary** — relevant to the evaluation/provenance layer (what counts as an audit trail)

## Status
- Single author report; Hacker News validated at 265 pts and 185 comments — signal strength is high
- No registry change required; Claude Code metadata does not currently claim full reasoning transparency
- Watch: whether Anthropic clarifies the enterprise boundary for extended thinking access or makes reasoning output available to all tiers
