# Research Watch: memvid — Single-File Memory Layer Inspired by Video Encoding

- Repo: https://github.com/memvid/memvid
- Also see: https://github.com/memvid/claude-brain (Claude Code plugin built on memvid, 477 stars), MV2_SPEC.md (in-repo format spec)
- Related signals: docs/research-watch/2026-04-28-engram-coding-agent-persistent-memory.md, docs/research-watch/2026-04-28-wuphf-llm-wiki-maintained-by-agents.md, docs/research-watch/2026-04-17-cognee-memory-engine.md, plus Beads and GBrain prior signals

## Why this is worth watching
memvid is a Rust-native, single-file memory format (`.mv2`) that markets itself as a "RAG pipeline replacement." Unlike the markdown+git wiki track (wuphf, GBrain) or the SQLite+MCP track (Engram, Beads), memvid takes a third route: a self-contained binary container with embedded WAL, vector index (HNSW), full-text index (Tantivy/BM25), and temporal index — all in one file you can `git commit` or `scp`. At 15.3K stars and a v2.0 Python→Rust rewrite shipping March 2026, it is materially larger than the other memory-track signals tracked this month and adds a fourth distinct sub-pattern to the L5 cluster.

## What stands out immediately
- "memvid" derives from **video encoding**, not video storage. README claim: memory is organized as "an append-only, ultra-efficient sequence of Smart Frames" inspired by keyframe compression. No actual video codec is used — the inspiration is structural (immutable frames, append-only log, codec-style compression upgrades over time).
- `.mv2` file layout (claim from README, format spec referenced): `Header (4KB) → Embedded WAL (1-64MB) → Data Segments → Lex Index → Vec Index → Time Index → TOC footer`. No sidecar `.wal`/`.lock`/`.shm` files — the WAL is in-file.
- Rust 98.5%, Apache-2.0, 15.3K stars, latest v2.0.139 (2026-03-13). Project description explicitly notes "complete rewrite from Python to Rust" claiming "10-100x performance improvements."
- Indexing stack: Tantivy for BM25 full-text, HNSW for vector ANN, optional ONNX/CLIP/Whisper embedders. `api_embed` feature flag toggles cloud embeddings (OpenAI) vs local (BGE/Nomic/GTE).
- Claimed retrieval latency: 0.025ms P50 / 0.075ms P99. Claimed benchmark wins: +35% on LoCoMo, +76% multi-hop, +56% temporal vs "industry average" — baselines unspecified, claims to inspect.
- Distribution surface: `memvid-cli` (npm), `@memvid/sdk` (Node), `memvid-sdk` (Python), `memvid-core` (Rust). MCP listed in repo navigation but details not surfaced in README excerpt — claim to inspect.
- Time-travel capability: append-only frames support rewinding to past memory states (claim) — distinguishes from mutable-overwrite stores.
- Downstream traction signal: `memvid/claude-brain` (Claude Code plugin built on memvid) sits at 477 stars — early but real ecosystem build-out.

## Why clawfit should care
This is now the **6th datapoint** in the L5 "alternative-to-vector-DB agent memory" cluster that clawfit has been tracking, and the first one that cleanly inhabits a third architectural sub-track:

1. **Beads** (22.2K, Go) — retention-as-issue-ledger
2. **Engram** (2.9K, Go) — SQLite + MCP-native structured memory
3. **wuphf** (657, Go+TS) — markdown + git, multi-agent shared wiki
4. **GBrain** (Garry Tan) — markdown + PGLite, single-user
5. **cognee** — vector + graph memory (Python, traditional DB-backed)
6. **memvid** (this signal, 15.3K, Rust) — single-file binary container with embedded indices

The architectural taxonomy is firming up around three sub-tracks:
- **5a graph/vector-DB memory** — cognee, mem0, Letta (Python, requires infra)
- **5b human-inspectable wiki memory** — wuphf, GBrain, claude-mem (markdown + git)
- **5c portable-binary memory** — memvid, Engram-with-SQLite (single file or single binary, no infra, no human-readable surface)

memvid is the cleanest exemplar of 5c so far — Engram has SQLite which is binary-portable but its memory is structured as MCP-served records, not a self-describing format. memvid's claim that "the file IS the database, indices, and WAL" is more aggressive.

For clawfit's recommendation engine: `network: offline` + `setup_complexity: low` + `statefulness: persistent` profiles now have a Rust binary option distinct from the Go cluster (Beads/Engram). When the L5 sub-typing eventually formalizes, memvid is a candidate exemplar for the "portable binary, no human-readable surface" branch.

## memvid vs Engram vs wuphf — sub-track differentiation
All three reject the vector-DB-as-service model. The differences:

- **Storage surface**: memvid → opaque binary (`.mv2`); Engram → SQLite file at `~/.engram/engram.db` (queryable); wuphf → plain markdown in git
- **Inspectability**: memvid lowest (binary, requires CLI/SDK); Engram middle (SQLite, queryable but schema-bound); wuphf highest (grep + read)
- **Performance ceiling**: memvid claims sub-ms vector search at scale (HNSW + Tantivy in-file); Engram bounded by SQLite FTS5; wuphf bounded by grep + LLM-synthesized briefs
- **Multimodal**: memvid supports CLIP (image) + Whisper (audio) via feature flags; Engram and wuphf are text-only by design
- **Conflict / curation**: Engram has `mem_judge` MCP tool; wuphf has `/lint` for contradictions/orphans; memvid leans on append-only + time-travel rather than active curation

The summary read: memvid optimizes for **performance and portability** at the cost of inspectability; wuphf optimizes for **inspectability and multi-agent collaboration** at the cost of retrieval latency; Engram sits between, optimizing for **MCP-native structured access**.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / MCP / context layer** (primary; the entire product is a persistent memory backend for agents)
- **Level 4 — Capability / plugin / tool-use layer** (secondary, weak; ships SDKs and CLI consumed by agents, MCP integration referenced but unverified)
- Sub-pattern signal: "portable-binary memory" — memvid is the strongest exemplar to date. With cognee (vector-DB), wuphf+GBrain (markdown+git), and now memvid (single-file binary), the L5 sub-types are visible enough to consider documenting in reference-levels.md if a single additional 5c-track entrant appears.

## Status
- Tracking: active signal. 15.3K stars + v2.0 Rust rewrite + downstream plugin (claude-brain) materially exceeds typical L5 signal velocity. Of the 6 memory-track signals tracked this month, memvid has the largest installed base.
- Registry action: none — memory backends do not fit the agent/llm/hardware schema.
- reference-levels.md action: **flag, do not modify**. The L5 three-sub-track taxonomy (5a graph/vector, 5b markdown+git, 5c portable-binary) is becoming defensible. Recommend revisiting reference-levels.md within 30 days if (a) one more 5c entrant appears, or (b) memvid crosses 20K stars or gains visible enterprise adoption.
- Items to validate on next pass: actual MCP tool surface (claimed in nav but unverified in README), benchmark baselines for the +35%/+76%/+56% claims (LoCoMo eval methodology), real-world `.mv2` file size at meaningful scale, and whether the single-file format introduces practical limits (max file size, concurrent writers, partial corruption recovery).
