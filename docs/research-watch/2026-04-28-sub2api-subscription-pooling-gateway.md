# Research Watch: Sub2API — Subscription-Pooling Gateway for Claude / OpenAI / Gemini

- Repo: https://github.com/Wei-Shaw/sub2api
- Also see: https://github.com/lieeew/sub2api (fork), https://github.com/DR-lin-eng/sub2api (perf-tuned fork), https://shyft.ai/skills/sub2api, https://aitoolly.com/ai-news/article/2026-03-02-sub2api-crs2-open-source-unified-proxy-service-for-claude-openai-gemini-and-antigravity-subscription
- Source: GitHub Trending Daily Go (2026-04-28), 16,100★ total, +454 today
- Language: Go 1.25 (Gin + Ent ORM), Vue 3 frontend

## Why this is worth watching
Sub2API operationalizes a pattern that the ecosystem has been gravitating toward but has rarely been packaged this cleanly: **pooling multiple paid AI subscriptions (Claude Code, OpenAI Codex, Gemini, Antigravity) behind a single API surface with carpool-style cost sharing**. It lands at the exact moment the two largest paid coding-agent vendors — Anthropic (Pro tier removed 2026-04-22) and GitHub Copilot (PRUs → token-metered AI Credits announced for 2026-06-01) — are shifting toward usage-based billing. Sub2API is the explicit user-side counter-move: instead of accepting per-token unit pricing, end users pool flat-rate subscriptions and divide effective cost across many consumers.

## What stands out immediately
- Multi-upstream support: Claude, OpenAI, Gemini, Antigravity (claim to inspect: whether all four work via OAuth session reuse vs. API-key-only paths)
- Token-level usage tracking and precise per-user billing — not just a dumb proxy
- Intelligent account selection with sticky-session routing (avoids cross-account context bleed)
- Built-in payment integration: EasyPay, Alipay, WeChat Pay, Stripe — implies real money is changing hands between pool operators and end users, not just personal-use pooling
- Admin dashboard and iframe-embeddable management UI — designed to be operated as a service, not just self-hosted for one team
- LGPL-3.0; Go + Vue stack; PostgreSQL 15 + Redis 7 backing store
- README carries an explicit warning: *"Using this project may violate Anthropic's Terms of Service... All risks arising from the use of this project are borne solely by the user"*

## Why clawfit should care

**Direct relevance — cost metric integrity:**
clawfit's scoring weights `cost_per_1k_tokens` at 25% via the LLM cost axis. That metric assumes the user is paying the published API rate. If subscription pooling becomes a stable consumption pattern, the *effective* cost-per-1k for a Claude/Codex/Gemini-class model can drop by an order of magnitude (a $200/mo subscription split 10–20 ways), but only for consumers willing to use a pooled gateway. This means:
- `cost_per_1k_tokens` may need an `effective_cost_mode: api_metered | subscription_pooled` qualifier, or
- A new `pricing_access_pattern` axis distinct from `pricing_tier`

**Vendor counter-pressure dynamic:**
Today's signal sits in opposition to the GitHub Copilot pricing transition flagged in this morning's scan. The underlying tension:
- *Vendor side* (Copilot, Anthropic): seat → usage-based billing, capturing heavy users' surplus
- *User side* (Sub2API and similar gateways): flat-rate subscription pooling, redistributing surplus across light users

How that equilibrium settles over the next 6–12 months is a load-bearing question for clawfit's recommendation logic. A plausible vendor response is **subscription terms hardening** (per-account device fingerprinting, rate limits, OAuth session pinning) — which would partially neutralize Sub2API's pattern but would also raise a `tos_compliance_risk` signal that pooled-cost recommendations should carry.

**Adjacency to existing taxonomy:**
- Closest neighbor: GoModel (Level 4c gateway, 2026-04-22) and CLIProxyAPI — but those are *single-user multi-provider* proxies. Sub2API is *multi-user single-or-pooled-subscription* fan-out — a meaningfully different topology.
- Cross-cuts Level 7: payment integration + admin UI + sticky-session routing makes this closer to a SaaS-like infrastructure layer than a pure tool-use proxy.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infrastructure** (sub-type: subscription-pooling gateway / multi-tenant API fan-out) — primary classification
- **Cross-cut to Level 7 — Infrastructure / hardware / edge layer** for the SaaS-operator dimension (payment rails, admin UI, multi-tenant billing)
- **Distinct from GoModel/LiteLLM/CLIProxyAPI**: those route one user across many providers; Sub2API routes many users across pooled subscriptions of the same provider

Notable subcategories worth tracking if more entries appear:
- `subscription_pooling_gateway` as a sub-type of L4c
- `tos_compliance_risk` as a candidate scoring qualifier (not a hard filter — a disclosure axis)

## Legal / ToS posture
The repo itself flags ToS violation risk. Specifically:
- Anthropic's Claude Pro/Max subscriber terms restrict account sharing and programmatic access outside permitted clients
- OpenAI's ChatGPT/Codex subscription terms similarly prohibit account sharing and reselling access
- Google Gemini and "Antigravity" likely carry comparable restrictions
- Payment-integrated reselling (Stripe/Alipay flows present in the codebase) materially raises legal exposure beyond personal-use pooling

This is **not** a reason to discount the signal — the velocity (16.1k★, +454/day, multiple active forks) shows demand exists regardless. But any registry-adjacent treatment of pooled-cost economics needs to surface this risk explicitly rather than treat pooled cost-per-token as equivalent to API-metered cost-per-token.

## Status
- **No registry entry** — gateways/proxies do not map onto the agent/llm/hardware schema, and the ToS posture would create a recommendation-liability surface clawfit should not own
- **No `reference-levels.md` mutation today** — single-signal for the "subscription-pooling gateway" sub-type; revisit if 2+ more independent entries appear (likely candidates: similar Chinese-ecosystem CRS forks; Western equivalents have not yet surfaced at scale)
- **Strong meta-signal** — directly informs the cost-axis discussion triggered by Copilot's PRU → token-credit transition and Anthropic's Pro tier removal. Worth a follow-up scoring memo on whether `cost_per_1k_tokens` needs an access-pattern qualifier
- **Watch items:**
  - Whether Anthropic/OpenAI add device fingerprinting or session-binding that breaks the pattern
  - Whether a non-Chinese-ecosystem equivalent emerges (would signal pattern globalization)
  - Whether clawfit users in `team_size: solo` + `budget: low` profiles begin asking about pooled-access economics directly
