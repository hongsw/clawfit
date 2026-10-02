# Research Watch: LlamaIndex Extract v2.5 — Purpose-Built Document Extraction Agent Harness

- Repo/Link: https://www.llamaindex.ai/blog/introducing-extract-v2-5 (LlamaCloud product; parent framework: https://github.com/run-llama/llama_index)
- Source: LlamaIndex official blog (2026-10-01); via unite.ai coverage

## Why this is worth watching

LlamaIndex Extract v2.5 introduces a structural distinction that has been implicit in document AI systems but rarely stated directly: a general-purpose agent harness performs worse at document extraction than one purpose-built for that task. The v2.5 release explicitly ships "a new agent harness purpose-built for document extraction, taking inspiration from the latest coding agents and tuned around the models to handle failure modes across vision, reasoning, and verification." This is the same architectural argument that drove the coding agent specialization wave (general-purpose agents performed worse at code tasks than task-specialized harnesses like Aider, Claude Code, Goose) — now applied to document extraction. The accuracy improvement from 87.1 to 93.9 overall value F1 (Cost Effective tier, 6.8 point gain) and 46.8 to 80.6 citation accuracy (Agentic tier, 33.8 point gain) at no pricing increase confirms that harness specialization produces concrete capability gains, not just architectural claims.

## What stands out immediately

- **"Agent harness purpose-built for document extraction"**: LlamaIndex names this a harness, not a model or a prompt template; the architectural layer matters — this is an orchestration layer tuned to document-specific failure modes (vision interpretation, multi-page cross-reference, scanned form OCR) rather than a general instruction-following loop
- **Structural Reasoning**: adapts computational effort to document type, layout, and information density; complex documents receive more agent loop iterations, simpler ones process faster; this is task-adaptive orchestration at the document level
- **Citation accuracy jump**: 46.8 → 80.6 for Agentic tier, 46.4 → 82.2 for Agentic Plus — the 33-point gain in citation accuracy (grounding evidence to source location) is the most significant single metric improvement; citations were the weakest point of v2 and are now competitive
- **Spreadsheet mode**: native workbook cell extraction instead of flattened text representation; Excel/CSV structure is preserved in extraction, not re-parsed from a text dump — enables schema extraction directly from tabular financial or operational documents
- **Long lists and cross-page records**: specific task improvements — long lists 82.0 → 92.6 (Cost Effective), cross-page records 80.3 → 92.0 — confirm that the harness specifically addresses multi-element, multi-page document patterns that generalist agents fail on
- **Three-tier architecture maintained**: Cost Effective (now at previous Agentic accuracy), Agentic (now at previous Agentic Plus accuracy), Agentic Plus (new ceiling) — each generation has effectively moved up one tier in capability; pricing unchanged
- **Coding-agent-inspired design**: LlamaIndex explicitly cites coding agent methodology as the inspiration; this is a technology transfer signal — techniques developed for code (verify-then-commit loops, specialized tool selection, multi-step verification) are being adapted for documents

## Why clawfit should care

The harness specialization argument in Extract v2.5 is the same argument underlying clawfit's core taxonomy question: do specialized harnesses outperform general ones for specific tasks? The answer in document extraction is now empirically yes (6.8+ F1 points at constant cost). This reinforces the `task` filter axis in clawfit's recommendation engine — if a task is "document extraction" or "structured data extraction from PDFs," a specialized extraction harness will outperform a general coding agent configured with a PDF reader tool. The registry currently has no `task: document-extraction` category (tasks tracked: `code-gen`, `qa`, `research`, `planning`, `automation`). The growth of specialized extraction harnesses (LlamaIndex Extract, Reducto, Unstructured) suggests `document-extraction` or `structured-extraction` as a candidate task axis. The `statefulness` dimension is also relevant: Extract v2.5 handles multi-page documents with cross-page record linking — this is a form of session-level state that differs from stateless single-page extraction.

## Preliminary interpretation

Current best reading:
- **Level 2 — Agent Harness / SDK (document extraction specialization sub-type)**
- Secondary: Level 4 — the structured output schema, citation anchoring, and spreadsheet mode are capability features

This is an unusual L2 entry: most tracked L2 harnesses are code execution or general coding agents. Extract v2.5 is the first tracked harness signal that specializes at the document processing task, not the code generation or research task. The "new agent harness" language in the release makes the L2 classification more confident than previous LlamaIndex signals (which were typically L4 or data-layer).

## Claims to verify

- Whether the "new agent harness" is a separately installable open-source package vs. a cloud-only orchestration layer inside LlamaCloud (the blog post describes it as part of the cloud service; verify if it is open-sourced in llama_index)
- Whether the ExtractBench benchmark is public and reproducible or an internal LlamaIndex benchmark (a self-reported benchmark is a meaningful signal, but independently reproducible benchmarks are stronger)
- What models power each tier (Cost Effective, Agentic, Agentic Plus) — the blog post does not specify underlying LLMs; model choice affects latency and cost tradeoffs
- Whether Spreadsheet Mode works via the same JSON schema interface as document extraction or requires a separate API call pattern
- Whether LlamaIndex's parent framework star count (~40k for run-llama/llama_index at last check) has grown materially with Extract v2.5 launch

## Status

- NOT in clawfit registry (cloud SaaS product; no deterministic per-page pricing published in the blog post; latency per extraction not documented)
- First signal for "purpose-built document extraction agent harness" as a distinct L2 sub-type
- Related tracked signals: LlamaIndex was not previously tracked in this corpus directly; related context: Reducto (document extraction, if tracked), iFixAi (2026-10-01, agent output auditing L5), TileLang (2026-10-01, inference kernel L7)
- Monitoring — watch for open-source harness release and per-page pricing disclosure
