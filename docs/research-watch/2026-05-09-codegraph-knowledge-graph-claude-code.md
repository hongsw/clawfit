# Research Watch: codegraph — Pre-Indexed Code Knowledge Graph for Claude Code

- Repo: https://github.com/colbymchenry/codegraph
- Also see: https://medium.com/@me_82386/i-cut-my-claude-code-api-costs-by-40-with-one-tool-12cf4306a1ab (author Medium post); https://github.com/abhigyanpatwari/GitNexus (L4c primary, 31.5k★, 16 MCP tools, WASM/BM25+semantic hybrid — nearest neighbor); https://github.com/CodeGraphContext/CodeGraphContext (MCP server + CLI, deterministic symbol graph, separate project); https://github.com/tirth8205/code-review-graph (adjacent signal, 6.8x token reduction claim on reviews); https://github.com/Lum1104/Understand-Anything (L4b plugin, LLM multi-agent pipeline, no MCP — contrasting form factor)

## Why this is worth watching

codegraph is the first MCP-server code intelligence tool in this taxonomy to publish per-codebase benchmark tables (six real projects, named sizes, Claude Opus 4.6 with Claude Code v2.1.91 as the test harness) rather than aggregate marketing figures, which makes the 92% average tool-call reduction a more inspectable claim than the headline metrics typical of this space. It appeared on GitHub Trending TypeScript at rank 6 with +148 stars today (2026-05-09) after the author published a Medium post framing the value as cost reduction — a framing that resonates with the multi-vendor anti-lockin and cost-sensitivity patterns already prominent in this taxonomy. At 1.1k stars the tool is below the 5k registry threshold, but the architecture is well-defined and the competitive slot it occupies (deterministic parse-then-index MCP server, 100% local, 7 tools) is meaningfully distinct from both GitNexus and Understand-Anything.

## What stands out immediately

- **Benchmark structure is more transparent than peers but is still vendor-authored.** Six named codebases: VS Code (TypeScript, 4,002 files), Excalidraw (TypeScript), Claude Code (Python+Rust), Claude Code (Java), Alamofire (Swift), Swift Compiler (Swift/C++, 25,874 files, 272,898 graph nodes). Per-run numbers: tool calls without vs. with codegraph, wall-clock time without vs. with. The Swift Compiler indexing time (under 4 minutes for 272,898 nodes) is the largest codebase any L4c code-graph tool in this taxonomy has published a number against. All tests run by the project author using a single Explore agent with identical queries; no independent reproduction, no held-out codebase set. Claim to inspect — structure is sound, verification is needed.
- **7 MCP tools with clear semantic separation.** `codegraph_search` (symbol lookup), `codegraph_context` (task-relevant subgraph assembly), `codegraph_callers`/`codegraph_callees` (call tracing), `codegraph_impact` (change blast-radius), `codegraph_node` (single symbol with optional source), `codegraph_files` (indexed structure), `codegraph_status` (index health). The tool count is lower than GitNexus (16 tools) but the specialization into a callers/callees pair and a dedicated impact tool mirrors the same structural decomposition.
- **Extraction pipeline is Tree-sitter → SQLite + FTS5 (deterministic, not LLM-generated).** Language-specific queries extract function/class nodes and call/import/inheritance edges from ASTs; references are resolved post-extraction including framework-specific patterns (13 frameworks listed: Django, Flask, FastAPI, Express, Laravel, Rails, Spring, Gin, chi, gorilla/mux, Axum/actix/Rocket, ASP.NET, Vapor, React Router, SvelteKit). Storage is a local `.codegraph/codegraph.db` SQLite file — zero cloud dependency, zero API key. This is architecturally identical to GitNexus's deterministic parse path (Tree-sitter WASM + LadybugDB) but without the WASM browser mode or semantic/BM25 hybrid search.
- **File watcher uses native OS events (FSEvents/inotify/ReadDirectoryChangesW) with a 2-second debounce window.** Incremental sync on save; source files only. This is a stronger freshness story than a one-time indexing model but weaker than a transaction-log-based pipeline (CocoIndex class). Whether the 2-second debounce is acceptable in high-frequency edit sessions is not discussed.
- **Auto-configuration writes to `~/.claude.json` and `~/.claude/CLAUDE.md`.** The installer registers the MCP server in the Claude Code config and injects global instructions that guide agents to prefer `codegraph_explore` for discovery tasks while reserving lightweight tools for targeted work. This is more opinionated than most MCP servers, which leave prompt engineering to the user. The global CLAUDE.md injection is worth inspecting: it affects all Claude Code sessions on the machine, not just sessions in codegraph-indexed repos.
- **19+ languages, 13 framework-aware routing patterns.** Language list includes TypeScript, JavaScript, Python, Go, Rust, Java, C#, PHP, Ruby, C, C++, Swift, Kotlin, Dart, Svelte, Vue, Liquid, Pascal/Delphi. The breadth is a claim to inspect — framework-aware routing (e.g., Django URL dispatch, Express middleware chains) is substantially harder to get right than symbol extraction, and the README does not include precision/recall numbers on framework edge resolution.
- **MIT license, TypeScript 95.3% / JavaScript 4.7%, 255 commits, 12 open issues, 29 PRs.** Active but single-maintainer footprint. The PR queue (29 open) relative to commit count suggests external contributors are submitting but merge throughput is constrained. No release tags — all work is on `main`.
- **No explicit comparison to GitNexus, CodeGraphContext, or Understand-Anything in the README.** The author positions codegraph as a new category ("pre-indexed code knowledge graph for Claude Code") without acknowledging the existing cluster. This is a routine omission for solo tools but means the differentiation story requires external analysis rather than reading from the docs.

## Why clawfit should care

The L4c code-intelligence sub-cluster now has three distinct entries with different architectural bets: GitNexus (BM25 + semantic hybrid, WASM client-side mode, PolyForm Noncommercial, 16 tools), CodeGraphContext (CLI + MCP, earlier entry, lower star count), and now codegraph (deterministic Tree-sitter + FTS5, MIT, 7 tools, native file watcher, global CLAUDE.md injection). The differentiation matrix for a `task: code-gen` profile with `statefulness: session` and `setup_complexity: low` preferences is no longer single-entry: codegraph's MIT license and simpler tool count may make it lower friction than GitNexus for individual developers, while GitNexus's PolyForm Noncommercial license and enterprise-framing suit team contexts.

For clawfit's scoring model, the implicit assumption that "any MCP code-graph tool is equivalent" breaks down at three axes: (1) **search quality** — FTS5 full-text vs. BM25+semantic hybrid has measurable recall differences on symbol-rename and cross-language import queries; (2) **freshness model** — debounced file watch vs. full re-index on demand vs. incremental CocoIndex-class pipelines; (3) **governance** — MIT vs. PolyForm Noncommercial affects `governance_need: hard` enterprise profiles. The current L4c table does not yet capture these sub-axes.

The global `~/.claude/CLAUDE.md` injection behavior also introduces a new pattern not previously observed in L4c entries: the tool modifies the agent's default behavior machine-wide, not just within a project scope. This is structurally closer to an L3 SSOT mutation than a L4c capability extension, and it sets an architectural precedent that other MCP servers could follow. If this pattern spreads, the boundary between L3 (agent governance/SSOT) and L4c (MCP capability) will need to be re-examined.

## Comparison to GitNexus (closest neighbor)

| Axis | codegraph | GitNexus |
|------|-----------|----------|
| Stars (2026-05-09) | 1.1k | ~31.5k |
| License | MIT | PolyForm Noncommercial |
| MCP tools | 7 | 16 |
| Graph construction | Deterministic Tree-sitter → SQLite/FTS5 | Deterministic Tree-sitter WASM + LadybugDB |
| Search | FTS5 full-text | BM25 + semantic hybrid |
| Browser client-side mode | None | Yes (zero-install WASM) |
| Freshness | Native OS file watcher (2s debounce) | Re-index on demand |
| CLAUDE.md injection | Yes (global, auto) | Not documented |
| Benchmarks published | Yes, 6 codebases, vendor-authored | No public per-codebase benchmark table |
| Languages | 19+ with 13 framework routes | 7 languages documented |
| clawfit level | L4c (MCP code intelligence) | L4c (MCP code intelligence) |

The tools occupy the same L4c cell. codegraph's differentiators at this stage are MIT licensing, published benchmark tables (even if vendor-authored), and a native file-watcher freshness model. GitNexus's differentiators are the BM25+semantic hybrid search, the browser/zero-install mode, and the far larger community (31.5k★ vs. 1.1k★). For a `governance_need: standard` individual developer profile, codegraph is a credible lower-friction alternative; for team and enterprise profiles, GitNexus's search quality and community size dominate.

## Preliminary interpretation

Current best reading:

- **Level 4c — Tool-use / action infrastructure (MCP code intelligence server):** Deterministic Tree-sitter parse → SQLite/FTS5 graph → 7 MCP tools exposing symbol search, call graph traversal, and impact analysis to any MCP-compatible agent. This is the same L4c sub-type as GitNexus (code knowledge graph MCP server), with a narrower tool set and a single-maintainer footprint.
- **Weak L3 secondary (CLAUDE.md injection pattern only):** The auto-injection of global agent instructions via `~/.claude/CLAUDE.md` is a L3-adjacent behavior — it modifies the agent's default reasoning behavior machine-wide. This is the only current L3 characteristic; it does not warrant a primary L3 classification, but it is architecturally notable and worth flagging for taxonomy reviewers.
- **Not L4a:** codegraph does not maintain a session-scoped memory artifact or a persistent knowledge base written by the LLM. The SQLite graph is a static derived index, not a living knowledge store.
- **Not L4b:** The distribution form factor is an MCP server, not a host-embedded plugin. The agent calls codegraph tools on demand; it does not run inside the agent's plugin runtime.
- **Not L5/L6:** No ingestion pipeline, no retrieval loop, no vector index. The graph is precomputed by deterministic AST parsing, not by embedding or LLM-generated enrichment.

## Status

- On-watch; below the 5k-star registry threshold (1.1k as of 2026-05-09). MIT license and transparent benchmark structure are positive signs for eventual registry promotion, but single-maintainer development pace and the absence of independent benchmark reproduction are material concerns. The global CLAUDE.md injection pattern is an architectural anomaly worth tracking regardless of star count — if other MCP servers adopt it, it has taxonomy implications for the L3/L4c boundary. Revisit at 5k stars or when a second independent replication of the 92% tool-call-reduction claim is published. No `docs/reference-levels.md` mutation today; the existing L4c cluster accommodates this sub-type (code knowledge graph MCP server) without taxonomy change.
