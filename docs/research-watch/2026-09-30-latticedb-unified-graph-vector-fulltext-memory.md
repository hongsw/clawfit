# Research Watch: LatticeDB — Embedded Property-Graph Database with Native Vector and Full-Text Indexing

- Repo: https://github.com/jeffhajewski/latticedb (⭐711)
- Source: GeekNews front page (11 points, 2026-09-30)

## Why this is worth watching

Agent memory is currently served by a fragmented stack: separate tools for graph relationships (Neo4j, Kuzu), vector similarity (Qdrant, Chroma, FAISS), and full-text search (Elasticsearch, SQLite FTS). Each system has different query semantics, connection management, and consistency guarantees. LatticeDB combines all three into a single embedded, configuration-free, single-file database with a unified query layer. For agent runtimes that need relationship traversal, semantic retrieval, and lexical search within one reasoning step, this eliminates the multi-system coordination overhead that currently defines the L5 stack. The benchmark claims (0.13 μs node lookup, 0.83 ms 10-NN at 1M vectors with 100% recall) are aggressive enough to warrant independent verification, but the architecture is sound.

## What stands out immediately

- **Single-file embedded storage**: zero configuration, portable, no server process — deployable inside an agent container or on-device
- **Unified HNSW + BM25 + graph traversal**: queries can combine all three modalities in one call — for example, find semantically similar document chunks AND traverse to their source documents AND match on a keyword, without switching engines
- **Sub-microsecond node lookups (0.13 μs)**: competitive with in-memory hash maps; relevant for high-frequency agent memory reads
- **Event streams and graph changefeeds**: agents can subscribe to changes in the graph, enabling reactive memory patterns (e.g., "notify when a related node is updated")
- **Language bindings**: Python, TypeScript, Go, Java — covers the major agent runtime languages
- **MIT license**: permissive, suitable for embedding in commercial agent products
- **711 stars with GeekNews feature today**: early but gaining attention; project appears newly public

## Why clawfit should care

The L5 (memory/observability) taxonomy currently separates persistent memory tools (mem0, LangMem, Graphiti) from retrieval systems (Chroma, Qdrant). LatticeDB doesn't fit either slot cleanly — it's a substrate that enables both, in one process, without a server. If it holds up under benchmarking, this could represent a new sub-type: "unified embedded agent memory store" that eliminates the need for a separate vector DB + graph DB combination. The single-file characteristic is also directly relevant to clawfit's `offline` hardware filter: an agent deployed on a local/edge node could carry its full memory substrate as a single file with no external dependencies.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory / Storage** (primary): unified local agent memory store combining graph relationships, vector embeddings, and full-text indexes
- No secondary level; LatticeDB is pure storage infrastructure, not a harness or capability layer

## Claims to verify

- "100% recall" on 10-NN vector search at 1M vectors: needs independent benchmarking; HNSW recall at that scale depends heavily on M/ef_construction parameters that may be tuned for the benchmark
- 0.13 μs node lookup: plausible for embedded graph traversal with a good implementation, but this is a best-case figure; access patterns for agent workloads (random access, varied graph depth) may differ
- Durable event streams: the README mentions changefeeds but the durability model (WAL, replication, crash recovery) is not detailed
- Python binding maturity: star count and GeekNews timing suggest this is a recent public release; binding stability and Python GIL behavior under concurrent agent writes are unverified

## Status

- 📡 Tracking: first signal for **unified embedded graph+vector+full-text agent memory store** sub-type
- No prior clawfit research-watch doc; independent from existing L5 entries (mem0, LangMem, Graphiti, Chroma)
- Below single-signal promotion threshold for canonical L5 sub-type; watching for second unified-memory-store signal
- Registry eligibility: not applicable (infrastructure layer, not an agent/LLM/hardware entry for the current registry schema)
