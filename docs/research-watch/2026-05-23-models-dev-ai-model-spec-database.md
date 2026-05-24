# Research Watch: models.dev — AI Model Spec Database

- Repo: https://github.com/anomalyco/models.dev
- Also see: https://models.dev · https://models.dev/api.json · https://github.com/anomalyco/opencode (primary consumer)

## Why this is worth watching

At 4,000+ stars and 986 forks, models.dev has accumulated substantial community adoption for a data-only project — star velocity of this magnitude for a TOML/JSON registry signals that the gap it fills (a single, machine-readable, MIT-licensed source of truth for model pricing, capabilities, and context windows) is genuinely felt. Its origin is the anomalyco org, which also ships opencode (L1, 157k stars, canonical entry in this taxonomy), giving models.dev a direct first-class consumer with demonstrated production reach. The JSON API surface (`models.dev/api.json`) means downstream tools can consume it without vendoring the TOML source, widening integration potential beyond the opencode ecosystem.

## What stands out immediately

- Data format: provider-scoped TOML files; SVG logos co-located — structured for both machine consumption and human authorship
- Coverage: pricing (input/output token costs per model), capabilities (tool calling, reasoning, structured output, JSON mode), context windows, output token limits, modalities, knowledge cutoff dates, API endpoints — these are exactly the fields clawfit's `llms.json` tracks manually
- JSON API: `models.dev/api.json` is a static, publicly accessible snapshot — no auth, no rate limits, CDN-served; usable as a live upstream for any recommendation engine
- TypeScript frontend (89% of codebase) renders the web UI; the data layer is TOML-only and language-agnostic
- Community-contributed: MIT license, open PRs for new providers — not a single-vendor-controlled source; continuity risk is lower than a proprietary API but higher than a foundation-backed spec
- Integrates with AI SDK (Vercel) and opencode as named consumers — not a standalone product, positioned as infrastructure

## Why clawfit should care

clawfit maintains `clawfit/registry/llms.json` by hand: 7 entries with fields for `max_context`, `cost_per_1k_tokens`, `latency_class`, and `preferred_tasks`. models.dev tracks 100s of models with the superset of those fields plus capability flags (`tool_calling`, `reasoning`, `structured_output`) that clawfit does not yet expose. Two direct implications:

1. **Registry sync candidate:** models.dev/api.json could serve as an upstream source-of-truth to validate and extend `llms.json` without manual curation. The TOML structure maps cleanly to clawfit's existing schema — capability flags in models.dev would directly inform the `preferred_tasks` and future `capabilities` fields flagged in `docs/reference-notes/missing-recommendation-axes.md`.
2. **Capability-aware scoring gap:** clawfit's `scoring.py` does not currently distinguish between models that support tool calling vs. those that do not. models.dev exposes this at the field level; if clawfit adds a `capabilities` filter, models.dev is the natural upstream.

The MIT license removes any adoption friction. The main risk is data freshness: as a community-maintained static file, models.dev may lag behind provider pricing changes by days to weeks — a known limitation for cost-sensitive recommendation profiles.

## Preliminary interpretation

Current best reading:
- **Level 7 — Infrastructure / hardware / edge layer** (primary): models.dev is infrastructure for the AI tooling stack — a shared, community-maintained data substrate that other tools build on, analogous to a package registry or CDN for model metadata. It does not run agents, wrap LLMs, or provide interfaces; it is pure reference data consumed by L1–L4 tools
- The suggested "Level 6 — Infrastructure / Model Registry" label in the incoming signal is a reasonable first read but misapplies the layer numbering; Level 6 in this taxonomy is the human interface / voice / multimodal layer. The correct mapping is Level 7 (infrastructure), with a note that models.dev is a *data* infrastructure primitive rather than hardware or edge compute

## Status

- Not a registry candidate by type — models.dev is not an agent, harness, or hardware option; it is a reference data source. Actionable as an upstream for `llms.json` maintenance and as a capability-flag reference for the scoring model. No map mutation warranted. Flag for the scoring-analyst: evaluate models.dev/api.json as a sync source at the next `llms.json` calibration cycle.
