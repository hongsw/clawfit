# Research Watch: experientiallabs/experiential — Adaptive Model Gateway with Production-Traffic Router Optimization

- Repo: https://github.com/experientiallabs/experiential (⭐1.8k, +568 today)
- Platform: https://platform.experientiallabs.ai
- Source: GitHub Trending all languages (2026-09-06, +568 stars today — 31% single-day growth)

## Why this is worth watching

`experiential` is a model gateway that serves OpenAI-compatible endpoints across closed, open-source, local, and custom models — but with two features that distinguish it from the gateway/router tools already tracked in this log (freellmapi, CLIProxyAPI). First, it enforces per-user and per-agent spending controls, treating AI budget as a managed resource with explicit permission structures. Second, it uses production traffic to build custom optimized routers: rather than using a fixed routing policy, it observes real call patterns (quality/cost/latency tradeoffs) from your actual workload and fits routers that improve over time. The +568 stars gained today on a 1.8k-total repo represents 31% single-day growth — exceptional velocity for a gateway tool that is not freshly announced.

## What stands out immediately

- **Per-user and per-agent spending controls**: budget enforcement is native, not bolted on — agents get spending limits that fail closed rather than fail open; this is the first gateway in this log to treat agent-spending as a first-class access control problem
- **Three-tier model access**: hosted models (via API keys the gateway holds), bring-your-own-key models (user provides keys, gateway routes), and local models (Ollama, llamafile) — all behind a single OpenAI-compatible endpoint
- **Production-traffic router optimization**: the gateway collects real call data and trains custom router models that pick the best backend for each request based on quality, cost, and speed — moving from static routing to adaptive routing as traffic accumulates
- **Apache-2.0 license, 587 commits**: active development; not a weekend prototype; PostHog telemetry (disabled by default), trace optimization pipeline
- **Claude Code, Cursor, Codex native support**: documented integration paths for all three major coding agent harnesses
- **Self-hosted at localhost**: primary use case is developer teams and individuals managing model access across team members and CI/CD agents — not a cloud-first product

## Why clawfit should care

1. **`per_agent_spending_control` gap in registry schema**: clawfit scores cost as a hard budget filter — a request below the per-token budget passes, above it is excluded. `experiential` shows that production teams don't want a filter — they want a spending controller that enforces limits at runtime, not at recommendation time. A future `cost_governance: [filter | controller | unlimited]` dimension would let clawfit surface gateway tools for teams with mixed-maturity agents where some agents need spending guardrails.

2. **Adaptive routing as a distinct L2 sub-type**: freellmapi (2026-08-28) aggregates free tiers via static routing; CLIProxyAPI (2026-09-04) pools subscriptions behind static adapters; Spotify Portal (2026-09-05) implements task-type routing via hooks+scripts. `experiential` adds a fourth routing mechanism — traffic-adaptive routing that improves with use. This is a meaningfully different architecture from all three prior signals: the router is a learned model, not a hardcoded policy.

3. **`pricing_access_pattern` gap reinforced again**: the three gateway tools (freellmapi, CLIProxyAPI, experiential) break clawfit's per-token cost model in three distinct ways: zero-cost aggregation, subscription pooling, and now traffic-learned routing. The `pricing_access_pattern: [api_metered | subscription_pooled | unified_proxy | adaptive_routed]` schema gap is now four signals deep.

4. **Registry candidate — blocked on deterministic cost data**: the gateway itself has no inference cost (it's a routing layer); cost depends on which backend is selected per-request, which is intentionally non-deterministic (the whole point is adaptive selection). Not eligible for registry under current schema.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness / Wrapper Layer (primary)**: experiential sits between agent clients and model backends, routing requests, enforcing budgets, and optimizing over time — this is harness behavior, not base runtime behavior
- **Level 5 — Memory / Observability / Evaluation (secondary)**: the production-traffic router optimization is a learning/evaluation mechanism; call traces feed a model that improves routing policy — this has structural similarity to evaluation-guided systems at L5

## Claims to verify

- Whether the "production-traffic router optimization" is a trained ML model (gradient-based routing policy) or a simpler heuristic based on historical latency/cost averages — the claim is significant and the implementation details matter
- Whether the per-agent spending controls are enforced via API key quotas (simple) or via agent identity tracking (more sophisticated); the distinction affects whether it can enforce limits on anonymous agent calls
- Whether the local model backend (Ollama, llamafile) integration is production-grade or early-stage; local backend quality is a key differentiator from cloud-only gateways
- Whether the platform.experientiallabs.ai hosted version shares router training data across users or trains per-account routers

## Status

- 1.8k stars total, +568 today (31% single-day growth); above research-watch threshold (100★); well below registry threshold (5k★)
- Not eligible for current registry: gateway tool, no schema slot; no deterministic per-token pricing (routing is adaptive)
- Fourth signal for the `pricing_access_pattern` gateway sub-type at L2 (freellmapi 2026-08-28, CLIProxyAPI 2026-09-04, Spotify Portal 2026-09-05, experiential 2026-09-06); adaptive-routing is the first signal for the learned-policy variant within this sub-type
- Watch: star trajectory over next 7 days (if it holds above +200/day, approaching 5k threshold within a month); whether the traffic-adaptive router methodology is described in a technical blog or paper; whether `per-agent spending controls` appear in competing gateway tools
