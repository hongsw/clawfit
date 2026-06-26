# Research Watch: opendatalab/MinerU — Document Intelligence Pipeline for Agentic Workflows

- Repo/Link: https://github.com/opendatalab/MinerU
- Source: GitHub Trending — 69,545★

## Why this is worth watching
MinerU converts complex documents (PDFs, Office files, web pages) into LLM-ready markdown or structured JSON, explicitly positioning itself as a preprocessing layer for agentic workflows. At 69.5k★ it is the highest-starred document intelligence tool in any recorded scan — larger than any agent runtime tracked in this taxonomy. It signals that the document-ingestion layer is becoming a first-class infrastructure concern for production agent deployments.

## What stands out immediately
- 69,545★ — among the top-5 highest-starred items ever observed in this scan program
- Explicit "for your Agentic workflows" positioning in the repo description
- Handles layout analysis, formula recognition, table structure extraction — not simple text extraction
- Output formats: LLM-ready Markdown and structured JSON, both optimized for agent consumption
- Python; AGPL-3.0; from Shanghai AI Lab / OpenDataLab (research institution)

## Why clawfit should care
Current registry has no document intelligence / data ingestion layer entries. MinerU occupies a layer between raw data and the agent's context window — a preprocessing substrate that increases the quality of what agents receive. This is distinct from memory systems (which store agent-produced artifacts) and RAG pipelines (which retrieve stored chunks). The star count alone demands tracking. Potential clawfit axes: `input_format: [pdf, office, web, raw-text]` and `agentic_output: [markdown, json, chunks]` as data-layer fields.

## Preliminary interpretation
Current best reading:
- **Level 6a — Data ingestion and preparation** (document-to-LLM-ready preprocessing sub-type)
- No existing L6 sub-type covers this architectural role; represents a new named cell.

## Status
- 69,545★ — far exceeds all registry thresholds. Held as first signal for this L6a sub-type.
- Registry candidate pending `data-analysis` or `preprocessing` task type addition to schema.
- Promotion criterion: second independent document intelligence pipeline with explicit agentic workflow targeting, OR a clawfit maintainer creates a `data-ingestion` task type.
