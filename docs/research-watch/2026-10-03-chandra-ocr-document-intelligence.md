# Research Watch: Chandra 2 — OCR Model for Complex Layout-Preserving Document Conversion

- Repo: https://github.com/datalab-to/chandra (⭐12,397)
- Source: GitHub Trending Python (2026-10-03)

## Why this is worth watching

Chandra 2 (released March 2026) is a vision-language model for document-to-text conversion that targets the specific subset of OCR problems where layout matters: multi-column tables, nested forms, handwritten fields, mixed-language documents, and mathematical expressions. Unlike general-purpose VLMs that handle documents as one of many tasks, Chandra is built and benchmarked specifically on document structure. The project originated from datalab.to (a document intelligence company) and converts documents to HTML, Markdown, or JSON with explicit layout annotation rather than raw text extraction. The Apache 2.0 code license (model weights under Modified OpenRAIL-M) and active CLI and Python API distribution suggest it is targeting developer-side document pipelines, not consumer OCR.

## What stands out immediately

- **Layout-preserving output formats**: HTML, Markdown, and JSON output modes — preserving table structure, form field relationships, and heading hierarchy rather than flattening to plain text; this is the key functional claim that distinguishes it from pdf-to-text extraction tools
- **90+ language support with multilingual emphasis**: not just Unicode character detection — claimed performance on cross-script document forms and international regulatory documents
- **Handwriting recognition included**: most OCR models treat handwriting as a separate specialty; Chandra includes it in the same inference pass as typed text and form fields
- **Dual inference modes**: local HuggingFace (full weights on-device) and remote vLLM server (streaming, higher throughput) — same API surface both ways; useful for clawfit's `hardware: local` vs `hardware: cloud` axis
- **Image extraction with captions**: embedded images in documents are extracted with their captions as structured output, not dropped; important for technical documents with diagrams
- **Chandra 2 improvements over Chandra 1**: math, tables, layout, and multilingual OCR specifically called out — not a minor incremental update
- **CLI and Python API alongside Streamlit UI**: not a demo-first tool; designed for pipeline integration
- **12.4k stars, active GitHub Trending presence**: genuine developer adoption, not just academic citation

## Why clawfit should care

clawfit's L4 capability layer currently tracks web extraction (Scrapling), browser automation (Browserbase Skills), and domain-specific data tools (TradingView MCP, AWS Agent Toolkit). Document intelligence — converting PDFs, scanned forms, and mixed-format business documents into structured agent-readable format — is a distinct sub-type that is conspicuously absent from the tracked capability corpus. Chandra 2 is the clearest standalone signal for this sub-type: purpose-built, open-weight, layout-aware, and developer-ready via CLI and Python API. The `task: qa` and `task: code-gen` profiles in clawfit don't currently surface document parsing as a capability requirement, but many real-world QA pipelines start with PDF or scanned document inputs. The vLLM server mode also makes it compatible with the inference-runtime-substrate layer already tracked, giving it a clear integration path in clawfit's reference stack.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capabilities / Document Intelligence Sub-type** (primary)
- Secondary: L1 (the model itself runs as a small VLM; the capability claim is L4 but the substrate is L1)

The Modified OpenRAIL-M license on model weights warrants attention: it restricts certain use cases (details require reviewing the specific OpenRAIL-M variant). For enterprise deployment advice, this is materially different from Apache 2.0 on both code and weights.

## Claims to verify

- Whether layout preservation holds on complex nested tables (the "handles complex tables" claim needs benchmark comparison vs. Marker, DocETL, or LlamaIndex Extract)
- Modified OpenRAIL-M restrictions: what specifically is prohibited vs. permitted for commercial enterprise use
- GPU memory requirements for local inference (the model card for Chandra 2 should list this explicitly)
- Whether the vLLM server mode requires a separate Chandra-specific server or works with a standard vLLM deployment
- Quality degradation on handwriting vs. typed text in mixed-form documents (not benchmarked separately in available documentation)

## Status

- NOT in clawfit registry: no per-call inference cost profile; model weights under Modified OpenRAIL-M (not fully permissive)
- First tracked signal for "layout-preserving OCR model as standalone L4 document intelligence capability"
- 12,397 GitHub stars; Trending Python October 3, 2026
- Related tracked signals: LlamaIndex Extract v2.5 (2026-10-02, document extraction agent harness L2); Scrapling (2026-10-02, web extraction L4)
- Monitoring for benchmark comparisons vs. LlamaIndex Extract and commercial document APIs
