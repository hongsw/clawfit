# Research Watch: asgeirtj/system_prompts_leaks — Multi-Model System Prompt Transparency Catalog

- Repo: https://github.com/asgeirtj/system_prompts_leaks (⭐51,200)
- Source: GitHub Trending (2026-07-06, top by daily stars)

## Why this is worth watching

A 51k-star repository compiling extracted system prompts from production AI products — Claude Fable 5, Opus 4.8, Claude Code, ChatGPT 5.5, Codex, Gemini 3.5, Grok, Cursor, Copilot, Perplexity — has landed as the fastest-rising repo on GitHub this week. The significance is not the leaks themselves (individual system prompts have circulated since 2023) but the aggregate: this is the first catalog that spans all major commercial AI products in one place, is actively maintained, and is growing faster than any individual agent framework tracked in this series. The repo functions as an involuntary audit of how leading AI products configure their L3 SSOT/governing-instructions layer in production, which has direct implications for how clawfit should model agent behavior profiles.

## What stands out immediately

- **Coverage breadth:** Claude Fable 5, Opus 4.8, Claude Code (distinct from the model), ChatGPT 5.5, Codex, Gemini 3.5, Grok, Cursor, Copilot, Perplexity — all major commercial coding and chat agents in one place; cross-vendor comparison is now trivially accessible
- **Repository structure is JavaScript/Python:** prompts are not raw text dumps; the repo appears to include tooling to process, format, and diff system prompts across versions — this is a structured transparency artifact, not just a paste bin
- **Star velocity indicates practitioner demand:** 51.2k total stars with high daily velocity (1,386 stars on a single trending day) implies a substantial share of the practitioner community is actively referencing this material — for prompt engineering, competitive analysis, or safety research
- **Claude Code system prompt is explicitly included:** The operating instructions governing Claude Code's behavior as an agent are part of this catalog — meaning the governing constraints the agent operates under are publicly extractable, not opaque
- **No official authorization documented:** Unlike Anthropic's published usage policies or model cards, these appear to be extracted rather than officially published — provenance and accuracy of each entry would require independent verification against the live product
- **Active maintenance pattern:** JavaScript (71.5%) + Python (28.5%) stack suggests automation is in use for keeping prompts current; this is not a one-time dump
- **Cross-model design comparison is now structurally possible:** Prior to this catalog, comparing how Claude's system prompt handles refusal patterns vs. Gemini's vs. GPT's required separate extraction efforts; this repo collapses that cost to near-zero

## Why clawfit should care

**System prompts are the L3 configuration layer made visible.** In the clawfit taxonomy, L3 is the "team workflow / executable SSOT layer" — the instructions that determine how an agent behaves relative to its task, how it refuses, how it handles ambiguity. System prompts are a product-specific implementation of this layer. Until now, the L3 configurations of commercial agents have been opaque in clawfit's registry: we score agents by their stated capabilities but cannot easily account for governing instruction differences. This catalog makes L3 configuration differences observable.

**Behavior profiling implications for recommendations:** An agent's effective task performance is not purely a function of its base LLM — it is a joint product of the LLM and its system prompt. Two products using the same underlying model (e.g., Claude Fable 5) may behave differently in task execution, refusal patterns, and autonomy scope because of differing system prompt configurations. This is not currently modeled in clawfit's scoring axes.

**Transparency signal about the Claude Code agent specifically:** The presence of the Claude Code system prompt in this catalog means the governing instructions for one of clawfit's reference-level agents (L1) are publicly inspectable. Whether this changes how teams provision, audit, or trust Claude Code in production is an open question, but the fact of public extractability is a new datum.

## Preliminary interpretation

Current best reading:
- **Level 3 primary reference — System prompt as SSOT artifact:** The catalog captures how commercial agents implement L3 governing instructions in production. This positions it primarily as an L3 reference artifact: it makes visible what has been the most opaque layer in the taxonomy.
- **Level 6 secondary weak — Human interface configuration:** System prompts define the persona, tone, and user-facing behavioral contract of a product — a genuine L6 dimension. However, the primary analytical value is in the governing instruction layer (L3), not the output surface.
- **Meta-signal about transparency norms:** The 51k star count itself is a signal: practitioners are treating system prompt inspection as normal infrastructure knowledge, the way API rate limits or model pricing were normalized over the prior two years. This is a shift in what the practitioner community considers public operational knowledge.

This is a reference artifact, not a deployable tool — same treatment as `cheahjs/free-llm-api-resources` (25.3k★, tracked 2026-07-05): no registry entry, no sub-type promotion, but noted as a practitioner-demand signal for a transparency pattern.

## Claims to verify

- **Accuracy and completeness of each prompt:** Extracted system prompts may be partial, version-lagged, or incomplete — particularly for products with dynamic system prompt assembly (tool definitions, context injection at inference time)
- **Automation tooling scope:** Whether the JavaScript/Python tooling automatically tracks prompt changes across model versions, or whether updates require manual extraction, is not confirmed from available sources
- **Official acknowledgment from any vendor:** Whether any of the vendors covered have acknowledged this repo — either confirming accuracy or issuing takedowns — would significantly affect how to interpret the data provenance

## Status

- First signal — 2026-07-06; 51,200 stars (well above threshold); highest-star L3-adjacent reference artifact in this scan series
- **No registry entry:** reference artifact, not a deployable tool; no agents.json / llms.json / hardware.json schema fields applicable
- **No taxonomy map mutation:** single signal; transparency artifact sub-type not previously named in taxonomy but does not require canonical section change at this stage
- Schema watch: `agent.system_prompt_visibility` (public / proprietary / partially-documented) as a potential registry field for commercial agents — this catalog makes the field populatable for the first time
- Promotion criterion: none needed for reference artifacts; monitor for vendor acknowledgments, prompt accuracy disputes, and whether a second comprehensive cross-vendor system prompt catalog appears independently
