# Research Watch: Maek — Local-First AI Memory Workspace

- Repo/Link: https://maek.cognica.io
- Source: GeekNews (Show GN)

## Why this is worth watching
Maek is a local-first AI memory workspace from the team behind BB25 Bayesian search infrastructure (Lucene lineage). It differs from existing memory layers by using Bayesian-ranked retrieval rather than pure vector similarity, which is a meaningful architectural choice for recall fidelity. Appeared on GeekNews front page as a community demo.

## What stands out immediately
- Local-first architecture: data stays on device, no cloud sync required
- BB25 Bayesian search (probabilistic ranking vs. cosine similarity)
- "AI memory workspace" framing suggests end-user memory management, not just API
- From a team with search infrastructure pedigree (Lucene search background)

## Why clawfit should care
Adds to the growing Level 4a (Memory Layer) signal cluster alongside GBrain, OpenMemory, cipher, and cognee. The Bayesian retrieval angle is architecturally distinct from graph-based (cognee) or vector-based (OpenMemory) approaches. For orgs with `data_sensitivity: confidential` and `network: offline` profiles, local-first memory layers are increasingly decision-relevant.

## Preliminary interpretation
Current best reading:
- **Level 4a — Memory Layer** (local-first, Bayesian retrieval, workspace UX)
- Adjacent to GBrain but with search-infrastructure credentials and workspace framing

## Status
- Early tracking — community demo stage, no public GitHub yet observed; watching for open-source release
