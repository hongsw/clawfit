# Research Watch: Project N.O.M.A.D. (Node for Offline Media, Archives, and Data)

- Repo/Link: https://github.com/Crosstalk-Solutions/project-nomad
- Source: GitHub Trending Daily (All Languages) #12, 318 stars today, 27,000 total stars

## Why this is worth watching
At 27k total stars, Project N.O.M.A.D. is the highest-starred offline-first AI knowledge stack tracked in this taxonomy — significantly above AnythingLLM (the nearest comparable at the privacy-first platform layer). Its bundling of local AI inference, offline reference content (Wikipedia, Khan Academy, maps), and semantic document search into a single Docker-orchestrated deployment provides a complete offline stack rather than a single tool, which is structurally distinct from any prior entry in this taxonomy.

## What stands out immediately
- Docker Compose orchestration of multiple independent services (Ollama/LM Studio/llama.cpp for inference, Qdrant for vector search, Kiwix for offline Wikipedia/medical references, Kolibri for Khan Academy courses, ProtoMaps for offline maps, CyberChef for data utilities, FlatNotes for local markdown notes) under a unified "Command Center" management UI and API
- Inference backend is pluggable: Ollama, LM Studio, llama.cpp, or any OpenAI-compatible API — no lock-in to a single local runtime
- Semantic document search via Qdrant is built in, not bolted on — uploads feed directly into the same local vector store used by the chat interface
- Data encryption is listed as a feature (via CyberChef integration); this is the first entry in this taxonomy that explicitly names encryption tooling as a co-packaged component
- Hardware benchmarking with a community leaderboard is bundled — signals awareness that offline AI viability is hardware-dependent and that the project intends to surface that data
- Minimum viable hardware is 4GB RAM / dual-core; recommended AI workload config specifies RTX 3060+ and 32GB RAM — practical for edge or fieldwork deployment, not just home lab
- Install target is Debian/Ubuntu via shell script; no cloud account, API key, or ongoing internet required post-setup
- No public GitHub stars breakdown by day confirms this is sustained community interest, not a one-day trending spike (27k total, 318 on the capture day)

## Why clawfit should care
N.O.M.A.D. directly activates clawfit's `network: offline` filter and is relevant to any profile scoring `data_sensitivity: confidential`. Currently clawfit's offline-capable hardware and agent entries (Goose/offline, Aider, local Ollama configs) treat inference isolation and data isolation as separate concerns. N.O.M.A.D. bundles both — plus offline knowledge bases and encrypted storage utilities — into one deployable unit, which is a structurally different recommendation surface than standalone offline agents. If a `task: research` or `task: summarization` profile with `network: offline` is queried, N.O.M.A.D. is the only entry that provides the knowledge corpus alongside the inference stack. No current registry entry covers this combination. The hardware benchmarking leaderboard is also a signal: it implies that hardware recommendation quality is a community concern, which aligns with clawfit's hardware-axis scoring.

## Preliminary interpretation
Current best reading:
- **Level 7 — Infrastructure / hardware / edge layer** (offline-first AI execution stack, Docker-orchestrated, edge/fieldwork deployment target)
- Secondary: **Level 5 — Memory / MCP / context layer** (embedded semantic document search via Qdrant constitutes a local retrieval context layer)
- Closest prior entry: AnythingLLM (privacy-first AI platform, L7 primary). N.O.M.A.D. is broader in knowledge-corpus scope (offline Wikipedia, Khan Academy, maps) but narrower in agent programmability — it is a knowledge hub, not an agent harness.

## Status
- Medium-high signal — 27k stars is a strong floor; not a registry candidate yet (no `task: offline-research` type in current schema; no `deployment_mode: bundled-stack` field exists)
- Flag for schema-analyst: `network: offline` + `data_sensitivity: confidential` + `task: research` combination has no adequate current registry match; N.O.M.A.D. exposes a gap
- Revisit at 35k stars or if a second offline-first bundled AI knowledge stack emerges at comparable scale
