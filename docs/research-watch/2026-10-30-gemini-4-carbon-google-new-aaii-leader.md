# Research Watch: Gemini 4 Carbon — Google's New AAII v5 Leader

- Repo/Link: https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
- Source: GeekNews front page (2026-10-30); limited rollout to selected users as of today

## Why this is worth watching

Gemini 4 Carbon is Google's latest frontier model, scoring 59 on the Artificial Analysis Intelligence Index v5 — 9 points above Gemini 4 Argon and the new overall leader. It is not yet publicly available, rolling out to selected users at the same pricing as Argon ($4/$20 per million tokens with a 50% launch discount). The architecture, parameter count, and training approach are not disclosed in the Artificial Analysis write-up.

The headline benchmark position matters less than two specific trade-offs that affect clawfit recommendation profiles: (1) Carbon leads the Intelligence Index while running roughly even in cost per task ($7.76 vs. $7.68 for Argon), and (2) Carbon's hallucination rate on AA-Omniscience v1.1 is 11%, more than twice Argon's 4%. A model that scores higher overall but hallucinates more frequently is a direct counter-example to the common assumption that better benchmarks imply better reliability.

## What stands out immediately

- **AAII v5 score: 59**, up from Argon's 50; leads HLE-Diamond, Terminal-Bench-Science, AA-Omniscience, and AutomationBench-AA — four of nine Index evaluations
- **Hallucination rate: 11%** on AA-Omniscience v1.1, versus Argon's 4%; accuracy on the same benchmark rose from 48% to 58% — Carbon knows more facts but states invented ones more freely
- **Coding Agent Index: #2** (59 points) behind Claude Code + Opus 5.5 (max); ranks second on Terminal-Bench 4.0 (64%) and FrontierCode v1.1 (51%) — not a coding-agent leader despite topping the general index
- **Context window: 1M tokens** (same as Argon); multimodal input (text, image, video, speech); text output only
- **Pricing: $4/$20** per million tokens standard, 50% launch discount with no confirmed end date; cached input at $0.20/M (95% discount); cost per Index task $7.76 (23% less than Claude Opus 5.5 (max) at $10.04)
- **AA-Briefcase leadership: no** — Carbon scores 1609 Elo here, behind Grok 4.7, Muse Wonder, and Kimi K3.1 Pro; Argon scored 1483; a gain but not the lead
- **Availability: limited rollout**, not yet publicly available via API; no confirmed GA date

## Why clawfit should care

Gemini 4 Argon was tracked 2026-10-14. Carbon requires a separate entry because the capability profile is materially different, not just incrementally better.

The key clawfit implication is the **hallucination rate regression**: Carbon is a worse choice for `task: qa` and `task: research` profiles where factual reliability is critical, even though it tops the general intelligence index. The scoring.py LLM preference weights would need to distinguish between general capability (Intelligence Index) and reliability (hallucination rate) — these diverge with Carbon in a way they did not with Argon.

Current scoring does not model hallucination rate as a distinct dimension. If Carbon becomes generally available, a `hallucination_risk` annotation on registry LLM entries would be needed to prevent clawfit from recommending it for reliability-sensitive tasks on the basis of its leading benchmark score alone.

Coding agent second-place position (behind Claude Code + Opus 5.5 max) is relevant: at $4/$20 with 50% discount, Carbon may be the most cost-effective frontier LLM available for coding tasks where top performance is needed but Opus 5.5 pricing is prohibitive.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base LLM** (primary): frontier model update, clawfit `llms.json` candidate once publicly available
- Registry action: **deferred** — not yet publicly available via API; no confirmed pricing post-discount; hallucination regression needs annotation before inclusion

## Claims to verify

- Whether the 11% hallucination rate on AA-Omniscience v1.1 is reproducible outside the Artificial Analysis controlled test and whether it holds on other evaluation sets
- Whether the 50% launch discount has a fixed end date (current state: "no confirmed end date")
- Whether the limited rollout converts to public API availability and on what timeline
- Whether the AAII v5 #1 position holds after other frontier labs respond with updates (Kimi K3.1 Pro open weights drop November 4, 2026 per prior tracking)
- Whether Carbon's 1M context window has any degraded performance at the long end compared to Argon

## Status

- Tracking: new model release signal, GeekNews front page / Artificial Analysis, 2026-10-30
- Registry eligibility: deferred — limited rollout only, no public API, hallucination regression requires annotation design before inclusion
- Related: Gemini 4 Argon (2026-10-14), Kimi K3.1 Pro (2026-10-24, open weights pending Nov 4 2026)
