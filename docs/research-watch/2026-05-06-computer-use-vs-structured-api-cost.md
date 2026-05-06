# Research Watch: Computer Use Is 45x More Expensive Than Structured APIs (Reflex.dev Benchmark)

- Source: https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/
- HN thread: https://news.ycombinator.com/item?id=48024859 (412 points, 235 comments)
- Related signals: 2026-04-06 Claude Computer Use desktop control; 2026-04-06 understudy demo learning agent; 2026-04-06 Gemma Gem browser computer use

## Why this is worth watching

This is not a tool — it is a quantitative cost-axis signal that puts a concrete number on a tradeoff clawfit has so far treated only qualitatively. Reflex ran the same end-to-end task (find customer "Smith", locate their most recent pending order, accept all pending reviews, mark order delivered — touching three resources with filtering, pagination, and cross-entity lookup) through two architectures on top of the same Reflex application: a vision-driven browser-use agent and a structured API agent over auto-generated handlers. The token deltas are large enough that, if even directionally correct, they reorder the cost dimension of any clawfit recommendation that includes a computer-use-capable agent. 412 HN points and 235 comments make this the single highest-signal cost analysis in the computer-use space since Anthropic's Claude Computer Use launch was first tracked here on 2026-04-06.

## What stands out immediately

- **The 45x figure is derived from input-token totals, not headline cost.** Vision agent (Claude Sonnet + browser-use 0.12): 53 ± 13 steps, 550,976 ± 178,849 input tokens, 37,962 ± 10,850 output tokens, ~1003s wall clock. API agent (Claude Sonnet): 8 ± 0 calls, 12,151 ± 27 input tokens, 934 ± 41 output tokens, ~19.7s wall clock. The ratio 550,976 / 12,151 ≈ 45.3, which is where the title number comes from. (Validated fact, source-confirmed.)
- **The wall-clock gap (≈51x) is larger than the token gap.** 1003s vs 19.7s. For interactive or sub-minute tasks, the latency penalty of vision-driven control is more punishing than the token-cost penalty for many users. This is a separate axis from cost-per-call.
- **Quality also diverged in the benchmark, not just cost.** The vision agent reportedly found only one of four pending reviews because the remaining three were below the visible fold and the agent had no signal to scroll. This is a correctness finding, not just an efficiency finding — the cheaper structured path was also more complete. (Claim to inspect: the published numbers come from Reflex, who has a vested interest in the structured-API conclusion. Independent replication would strengthen the claim.)
- **The architectural argument is durable even if the multiplier shifts.** Reflex's framing: "an agent that must see in order to act will always pay for the seeing, regardless of how good the model gets." Vision tokens, screenshot rendering per step, and multi-roundtrip observation loops are intrinsic to the modality, not a current-generation inefficiency. Smaller/faster models will reduce the absolute cost but not the ratio.
- **Top HN counter-arguments narrow the claim's scope, they do not refute it.** (1) Hybrid DOM + vision is much cheaper than pure vision and was not benchmarked. (2) Computer use is the "last resort" for systems without APIs — the comparison is unfair where structured access doesn't exist. (3) Legacy / pre-OpenAPI surfaces have no alternative. (4) Wall-clock matters more than token cost for some workloads. None of these refute the ratio on the benchmarked task; they bound the conditions under which the ratio is decision-relevant.
- **Output-token ratio (~40x) tracks input-token ratio.** This is consistent with vision agents emitting per-step reasoning over many short steps versus API agents emitting one structured plan. It rules out a "vision only inflates input" interpretation.
- **Haiku data point reframes "cheap structured" as the relevant baseline, not just "structured."** API agent on Haiku finished in 7.7s with 9,478 input tokens — still 8 calls. The right comparison for cost-conscious recommendations is vision-agent-on-Sonnet vs. structured-agent-on-Haiku, where the ratio widens further.

## Why clawfit should care

clawfit's current `cost_match` filter operates on `cost_per_1k_tokens` from `llms.json`. That field captures **price per token** but not **token volume per task**. The Reflex data shows that the choice of *interaction modality* (vision-driven computer use vs. structured tool calls) can move token volume by 45x for the same task — a multiplier larger than the cost-per-token spread between the cheapest and most expensive models in the current registry. In other words: an agent's modality dominates an LLM's per-token price as a cost predictor for any task that admits both paths.

This exposes three concrete gaps:

1. **Cost dimension is incomplete.** The current scoring path treats `cost_per_1k_tokens × budget` as the cost reasoning. For computer-use-capable agents, the effective per-task cost is `cost_per_1k_tokens × E[tokens_per_task | modality]`, and the modality term is the larger swing. A user passing `--budget 0.01` to a Claude Computer Use recommendation today receives the same accept/reject treatment as a structured-tool agent at the same model price, despite a ~45x expected-token-volume gap.

2. **Latency dimension is incomplete.** The 17-minute wall-clock for the vision path violates `--latency low` and likely violates `--latency medium` for most reasonable interpretations. The current `latency` field on agents is a static label; for computer-use-capable agents it is task-dependent. A vision-driven invocation of an agent that also supports structured tools should not inherit the structured-tool latency band.

3. **Risk surface for L1/L7 boundary tools.** This is the cost-quantified follow-up to the 2026-04 pattern note that Claude Computer Use and `understudy` collapse the L1↔L7 boundary. The boundary is real, but it carries a cost penalty that should be flagged whenever clawfit recommends one of these tools. Recommendations involving Computer Use, understudy, Gemma Gem browser control, or similar L1/L7-collapsing tools should ship with an explicit "structured-first if possible" caveat in the rationale field — at minimum until clawfit can express the modality dimension in scoring.

This signal also resolves a competitive question: vision-based agents (Computer Use class) vs. structured-tool agents (MCP / function-calling class) are not in the same cost regime, and the data point sides with structured. clawfit's L4c entries that lean on MCP and structured tool calling (Manifest, the broader MCP cluster, code-mode patterns) gain weight as the cost-efficient default; L1/L7-collapse tools are repositioned as last-resort candidates for surfaces without APIs, not first-class peers.

## Preliminary interpretation

Current best reading:
- **Architectural / cost-axis signal — not a tool.** Do not register. Do not score. Do not promote.
- Affects scoring of existing entries that touch the L1/L7 collapse zone (computer-use-capable agents) and reinforces existing L4c entries (MCP-based structured tool routing).
- Closest existing analytical neighbor in `docs/research-watch/`: the 2026-04-12 Berkeley benchmark-vulnerability post — both are methodology/cost signals that recalibrate how registry entries should be weighted, not new entries themselves.
- Modality cost is a **new dimension**, not a refinement of an existing one. Candidate name: `interaction_modality` ∈ {`structured_api`, `vision_computer_use`, `hybrid_dom_vision`, `terminal_text`}, with an associated expected-tokens-per-task multiplier.

## Status

- Architectural signal logged. No registry change. No reference-levels.md change (flagged for ecosystem-mapper to consider whether the L1/L7 collapse note in v0.4 should cite this cost ratio).
- Flag for scoring-analyst: open question whether `cost_per_1k_tokens` should be paired with a per-modality `expected_tokens_per_task_multiplier` field on agents, or whether modality should become a top-level filter axis. The 45x magnitude argues for top-level — modality dominates model price.
- Flag for hot-table updater: include as today's lead architectural signal in README "🔥 What's hot right now".
- Independent replication of the 45x figure is the main outstanding validation. Reflex authored both the benchmark and the structured-API product being implicitly recommended; the directional finding is plausible from first principles (vision tokens, screenshot rendering, multi-step observation), but the precise multiplier should be treated as "claim to inspect" until reproduced by a neutral third party.
