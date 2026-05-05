# Research Watch: MemPalace — "Best-Benchmarked" Open-Source AI Memory System

- Repo: https://github.com/MemPalace/mempalace
- Also see: https://github.com/thedotmack/claude-mem (68.5k★, hooks-based SQLite+Chroma memory, L4a); https://github.com/topoteretes/cognee (16.9k★, graph-native memory, L4a); https://github.com/memvid/memvid (15.3k★, portable-binary memory, L4a); https://github.com/garrytan/gbrain (markdown+PGLite compounding KB, L4a/L6b); https://github.com/milla-jovovich/mempalace (mirror of the viral origin repo); https://github.com/MemPalace/mempalace/issues/875 (active benchmark dispute issue)

## Why this is worth watching

MemPalace reached 51k+ stars after going viral in early April 2026 — reportedly gaining 7k stars in 48 hours and 23k within a week, making it one of the fastest-growing AI memory repos in this taxonomy. Star velocity at that scale is a curator signal independent of technical merit: it tells us something about latent demand for a "best-benchmarked" memory system narrative. The tool also introduces a 29-tool MCP server with a spatial metaphor architecture (wings / rooms / drawers) that is structurally distinct from all existing L4a entries. Whether the benchmark claims hold is a separate question from whether the adoption signal is real.

## What stands out immediately

- **Spatial metaphor architecture (claim to inspect).** The wings/rooms/drawers hierarchy is a named organizational model for conversation history, not just a search index. Wings scope by entity (person, project), rooms by topic, drawers by original verbatim content. This is architecturally distinct from flat vector stores (claude-mem), graph schemas (cognee), and portable binaries (memvid). Whether the hierarchy actually improves retrieval in practice — rather than serving as UX framing over ChromaDB — is not proven by the current benchmarks.
- **96.6% LongMemEval R@5 headline score is ChromaDB, not MemPalace.** The benchmark dispute issue (#875, unresolved as of 2026-05-05) documents a significant methodological problem: the 96.6% result uses ChromaDB's default all-MiniLM-L6-v2 embeddings in "raw mode" with no palace architecture involved. No wings, rooms, or drawers appear in the benchmark file. The score measures ChromaDB default retrieval performance, not the MemPalace system it is attributed to.
- **100% LongMemEval claim involved teaching to the test.** The project's own BENCHMARKS.md acknowledges that the team identified the three specific failing questions, applied targeted fixes for those exact cases, then retested on the same set. The held-out validation (450 unseen questions, Hybrid v4) yields 98.4% — a more defensible but still strong result.
- **Metric category mixing against competitors.** The comparison table conflates retrieval-recall (R@5, MemPalace's metric) with end-to-end QA accuracy (Mastra 94.87%, Mem0 ~85%). These are not the same metric on the same scale. The "more than 2× Mem0" claim on ConvoMem is a comparison of retrieval recall (92.9%) against QA accuracy — a meaningless apples-to-oranges figure. Mem0's updated token-efficient algorithm raised their LongMemEval score from ~49% to 93.4%, narrowing the gap substantially.
- **LoCoMo 100% R@10 uses top-k=50 retrieval.** Per-conversation session counts in LoCoMo range from 19–32 sessions. Retrieving top-50 candidates from a pool of ~20 conversations is functionally "return everything" — it does not demonstrate retrieval discrimination.
- **BEAM benchmark shows 49% raw accuracy (absent from public claims).** End-to-end QA benchmarking in BEAM showed 49% raw accuracy and 26–43% on MemPalace-specific modes. These numbers are not present on the README, official website, or comparison tables as of 2026-05-05.
- **MCP surface is the most credible integration claim.** The 29-tool MCP server covers palace operations (write/read/search), knowledge-graph queries (SQLite-backed temporal entity-relationship DB), cross-wing navigation, and agent diary tools. Claude Code auto-save hooks and a `wake-up` context-loading command are documented. This integration surface is concrete and independently verifiable — it does not depend on the disputed benchmark claims.
- **MIT license, Python 91.8%, ChromaDB-pluggable backend.** The retrieval backend is interface-abstracted; ChromaDB is the default but substitutable. Python 3.9+ requirement, ~300 MB disk. No cloud dependency for core operation.
- **Active scam-warning in the README.** The project explicitly flags unofficial mirrors and PyPI imposters, which is consistent with the viral growth pattern generating impersonation attempts within days.
- **Maintainer partial acknowledgment, unresolved.** Issue #875 documents that maintainers acknowledged problems in April 2026 but made only partial README corrections. The headline banner, About text, and official website comparison tables still contain the disputed framing as of this writing.

## Why clawfit should care

MemPalace maps to L4a (agent memory / persistent context), where the existing cluster — claude-mem, cognee, memvid, Engram, GBrain, wuphf — already covers the major architectural sub-types. MemPalace would occupy a "verbatim-store + spatial-metaphor + MCP-native" sub-type not yet named in L4a, and its 51k★ star count would place it third in the L4a table behind claude-mem (68.5k★). That alone is meaningful for discovery purposes.

However, the benchmark dispute is a registry-entry blocker under clawfit's evidence standards. The primary marketing claim — "best-benchmarked" — is built on a score that measures ChromaDB's default embeddings, not MemPalace's architecture. Registering an agent memory tool whose headline metric is demonstrably attributed to its underlying library (not its own logic) would erode confidence in the registry's evidence quality. The unresolved issue #875, the missing BEAM results, and the metric-mixing in competitor comparisons each independently support holding.

The star count itself is a signal worth noting: 51k stars in under a month means a large developer cohort is actively evaluating or installing this tool regardless of benchmark validity. If the spatial-metaphor UX proves useful in practice and the benchmark framing is corrected, this tool has the adoption base to become a significant L4a entry.

For the L4a vs. L6b operational definition established 2026-05-05: MemPalace is read-write by both the LLM (via MCP tools) and the user, with no clear write-authority boundary. The `mempalace mine` ingest command is human-initiated pipeline; MCP write tools are LLM-initiated. This dual-write model means it does not cleanly fit either the L4a (pipeline writes, LLM reads) or L6b (LLM writes, human reads) definition. Primary classification remains L4a (agent memory plugin) with no L6b secondary warranted.

## Preliminary interpretation

Current best reading:
- **Level 4a — Memory / persistent context** (candidate; registry entry blocked pending benchmark claim resolution)
  - Sub-type: verbatim-store + spatial-metaphor organization (wings/rooms/drawers); structurally distinct from existing L4a entries
  - MCP surface: 29 tools covering read/write/search/knowledge-graph; directly comparable to Engram's 17 MCP tools
  - Storage: ChromaDB (default) + SQLite temporal entity graph; ~300 MB footprint; local-only operation
  - Does not qualify for L6b secondary classification: dual human/LLM write-authority model does not satisfy the "LLM is primary maintainer" criterion

**Flags for ecosystem-mapper review:**
- The spatial metaphor (palace, wings, rooms, drawers) may become a named architectural sub-type at L4a if independently validated in end-to-end benchmarks rather than retrieval-recall-only tests.
- The benchmark dispute pattern (engineering metrics to headline numbers, competitor metric mixing) is structurally similar to the "openclaw energy" critique raised in the HN thread. If MemPalace revises its benchmark framing to reflect actual architectural performance rather than ChromaDB baseline performance, the signal quality improves significantly.

## Status

- Watching; not a registry candidate today. Two conditions for re-evaluation: (1) issue #875 resolves with corrected benchmark framing on README and official website, and (2) at least one independent end-to-end QA benchmark (not retrieval-recall only) confirms MemPalace's spatial-metaphor architecture adds measurable value over a flat ChromaDB store. Star count (51k★) is strong enough to fast-track evaluation if those conditions are met. If a second spatial-metaphor memory tool with ≥5k stars appears, a named L4a sub-type for "hierarchical-scope verbatim stores" should be considered.
