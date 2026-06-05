# Research Watch: open-notebook (Open Source NotebookLM)

- Repo/Link: https://github.com/lfnovo/open-notebook
- Source: GitHub Trending

## Why this is worth watching
`open-notebook` is an open-source TypeScript implementation of Google's NotebookLM concept — a research workspace where agents digest documents, generate audio summaries, and synthesize knowledge from uploaded sources. At 24,993 stars, it's a high-signal alternative to proprietary NotebookLM for teams that need self-hosted or privacy-preserving research workflows.

## What stands out immediately
- Open-source (MIT) alternative to Google's NotebookLM — multi-LLM backend support
- "Enhanced flexibility and features" positioning vs. the locked-down Google product
- TypeScript-first; likely deploying as a web app with Docker
- Research-first use case: document ingestion, synthesis, audio generation
- At ~25k stars, indicates substantial demand for self-hosted knowledge workspace

## Why clawfit should care
This fills the `task: research` + `data_sensitivity: confidential` + `network: offline/hybrid` intersection that the registry currently has few strong entries for (AnythingLLM being the closest). It's structurally distinct from coding agents — no code-gen, no IDE integration — and targets researchers, executives, and PMs who need document-heavy knowledge synthesis without sending documents to Google cloud. Classified as **L6b primary** (LLM-native knowledge base; LLM synthesizes and writes the knowledge artifact from uploaded sources) with **L7 secondary** (web-app user interface).

## Preliminary interpretation
Current best reading:
- **Level 6b — LLM-native knowledge base (primary)**: Synthesizes and maintains knowledge artifacts from document sources via LLM
- **Level 7 — User interface (secondary)**: Web app interface for research workflows

## Status
- 24,993 stars exceeds threshold. Hold pending: (1) verification of self-hosting story (Docker Compose?) and true offline capability; (2) confirmation of multi-LLM backend support beyond OpenAI; (3) check whether `data_sensitivity: confidential` claim holds when fully self-hosted.
- Registry candidate for `task: research` + `role: researcher/exec` + `network: hybrid` profiles.
