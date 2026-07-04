# Research Watch: "Better Models: Worse Tools" — Forgiving Harness Overfitting

- Source: https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/
- Also see: https://news.ycombinator.com/item?id=44pts-jul5-2026 (HN front page, 44 pts, July 5 2026) · https://letsdatascience.com/news/newer-claude-models-show-tool-calling-regression-6f029d5f

## Why this is worth watching

Armin Ronacher (creator of Flask and Jinja — one of the most credible Python ecosystem voices) published empirical observations showing that Claude Opus 4.8 and Sonnet 5 produce malformed tool calls at roughly 20% failure rate against non-Claude-Code-shaped schemas, while Opus 4.5 and Codex models do not. The failure mode is specific and reproducible: newer models invent fields that don't exist in the declared schema, but produce byte-correct payload content inside the valid fields. The proposed explanation — that heavy post-training inside Claude Code's permissive harness has biased the model's schema sampling distribution — is a testable architectural claim with direct implications for any practitioner using alternative tool schemas. With 44 HN points in the first day, the practitioner community is taking it seriously, not treating it as an edge case.

## What stands out immediately

- **The regression is schema-shape specific, not capability regression**: models hallucinate extra fields (`requireUnique`, `oldText2`, `newText2`, `matchCase`, `in_file`, `forceMatchCount`) after closing multi-line strings in nested arrays — "the highest-entropy point of that task." The actual `oldText` and `newText` payloads inside the malformed calls are byte-correct. This is not a comprehension failure; it is a sampling failure at a structurally complex point.
- **Asymmetry across model versions (validated, not speculative)**: Opus 4.5 adapted well to Pi's non-standard nested schema; Opus 4.8 and Sonnet 5 regressed. Codex models showed no regression. The split aligns with the post-training intensity timeline: Opus 4.8+ coincides with heavier Claude Code RLHF cycles (claim — post-training schedule not publicly confirmed by Anthropic).
- **Claude Code's harness is demonstrably permissive**: it accepts parameter aliases, filters unknown keys, and performs Unicode repair. This is documented behavior in Claude Code, not reverse-engineered. A harness that silently tolerates schema drift removes the training signal that would otherwise penalize drift.
- **Named mechanism — "forgiving harness overfitting"**: the blog does not use this exact phrase, but the phenomenon is: a permissive harness in the training/RL loop reduces gradient signal for schema violations, allowing schema-adjacent sampling noise to accumulate across post-training iterations. The dominant harness's schema shapes become attractors in the model's output distribution.
- **Strict mode as mitigation**: grammar-constrained sampling (strict mode in the API) eliminated the regression in Ronacher's runs. This is a client-side workaround, not a model fix — it shifts the responsibility for schema enforcement from the model to the harness.
- **Generalizes beyond Pi**: any tool schema that differs structurally from Claude Code's built-in tool shapes (especially nested array schemas vs. flat key-value schemas) may be in the affected regime. The risk scales with model recency and post-training intensity.
- **Asymmetric impact by harness type**: strict harnesses (Pi, custom schema deployments) surface the failure immediately and loudly. Permissive harnesses (Claude Code itself, LiteLLM with key filtering) absorb the failure silently — meaning the practitioner community's aggregate failure signal is systematically underreported.

## Why clawfit should care

clawfit scores `(agent, llm, hardware)` triples and currently treats model–tool compatibility as a binary: a tool either supports a given LLM or it doesn't. This signal introduces a continuous, version-sensitive, schema-shape-dependent dimension that the current registry schema cannot represent.

Three concrete implications:

1. **Model version is not a monotonic quality axis for tool-use**: clawfit's LLM entries do not currently distinguish between capability regression and capability progression across model versions for tool-calling specifically. Opus 4.8 > Opus 4.5 on coding benchmarks but Opus 4.8 < Opus 4.5 on schema-strict tool-calling. A new `tool_schema_compliance` axis (values: `strict`, `permissive`, `unknown`) on LLM registry entries would capture whether a given model version has been observed to respect non-Claude-Code-shaped schemas under load.

2. **Harness permissiveness is an invisible modifier on model scoring**: clawfit does not model the harness layer that sits between the scored agent and the scored LLM. A permissive harness (Claude Code's built-in tool handling) inflates observed tool-call reliability by absorbing errors silently; a strict harness (Pi, custom schema) exposes the true error rate. The (agent, llm) pair's observed fit_score is harness-conditional in a way the current scoring model does not represent.

3. **The "forgiving harness" feedback loop is a structural risk for the registry's long-term validity**: if dominant harnesses (Claude Code with 50k+ star ecosystem) continue post-training on permissive schemas, each new model generation will be progressively harder to use in strict-schema contexts. clawfit's recommendation for `latency: low, statefulness: stateless` profiles that use tool-heavy agents with non-standard schemas may degrade in accuracy without any registry update, purely because model versions change.

## Preliminary interpretation

Current best reading:

- **Cross-layer meta-signal** — not a deployable tool; no registry entry warranted
- **Primary layer resonance: Level 2 — Harness / orchestration layer**: the mechanism is the co-evolutionary feedback loop between harness permissiveness and model post-training. The dominant L2 harness (Claude Code) is the environment shaping model behavior; alternative L2 harnesses inherit the resulting schema bias.
- **Secondary layer resonance: Level 4c — Tool-use / action infrastructure**: the observable failure surface is at the tool schema level; strict vs. permissive tool schema enforcement is an L4c design choice with L2-mediated model consequences.
- **No direct L1 implication**: the base runtime (Claude Code CLI binary) is not itself broken — its permissive harness is functioning as designed. The risk is in the feedback loop the permissive design creates across model generations.
- The phenomenon does not fit cleanly into any single layer because it is a **post-training feedback effect** that originates in L2 harness design choices and manifests as L4c tool schema compliance degradation. It is the first signal in this tracking cycle that names a cross-layer training-loop coupling mechanism rather than a product, framework, or architectural pattern.

## Claims to verify

- **Failure rate quantification**: the 20% figure is reported per Ronacher's user sessions, not a systematic benchmark. A controlled reproduction with published methodology does not yet exist; third-party replication is the critical next step.
- **Post-training schedule correlation**: the claim that Opus 4.8+ post-training is heavier on Claude Code RLHF cycles is inferred from the model version split, not confirmed by Anthropic. Anthropic has not publicly disclosed its RL training data sources or harness configurations.
- **Codex model exculpation**: Codex models showed no regression in Ronacher's tests. Whether this is because OpenAI's post-training uses stricter schema enforcement, uses different tool schema shapes, or is simply not comparable is unspecified.
- **Strict mode reliability**: grammar-constrained sampling eliminated the regression in Ronacher's runs, but at what cost to output quality or latency in complex multi-step tasks is not measured. The tradeoff between schema compliance and reasoning quality under strict mode is an open question.
- **Schema-distance threshold**: which structural schema differences trigger the regression (flat vs. nested, camelCase vs. snake_case, optional vs. required fields) is not characterized. Knowing the distance threshold would allow practitioners to design schemas that stay in-distribution without requiring strict mode.

## Status

- First signal — 2026-07-05; empirical blog post, no GitHub repo, no star count applicable
- No registry entry: this is a model-behavior observation, not a tool; the implication is a new `tool_schema_compliance` field on LLM registry entries and a harness-permissiveness note in agent entries
- Flag for `missing-recommendation-axes.md`: `llm.tool_schema_compliance` (strict / permissive / unknown) and `agent.harness_schema_strictness` as candidate new axes
- Monitor: third-party reproduction; Anthropic response or acknowledgment; whether strict mode adoption becomes a recommended default in community harness templates; whether this surfaces in L2 tools like claude-code-router or oh-my-claudecode as a known routing caveat
