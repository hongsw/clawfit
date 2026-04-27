# Research Watch: claw0 — "build an AI agent gateway from scratch" tutorial

- Repo: <https://github.com/shareAI-lab/claw0>
- Description: "0 - 1 learn OpenClaw: sections to build an claw-AI agent from scratch"
- Stars / Forks: 2,385★ / 280 forks (created 2026-02-24, last push 2026-03-18)
- Language: Python 3.11+, MIT license
- Trilingual docs: English / 中文 / 日本語
- Also see (prior education-signal docs):
  - `docs/research-watch/2026-03-28-agent-patterns-education-signal.md`
  - `docs/research-watch/2026-04-01-claude-architect-exam-education-signal.md`

## Why this is worth watching
claw0 is not a runtime, harness, or skill pack — it is a **structured "from scratch" curriculum** that walks readers through the construction of an OpenClaw-style agent gateway in 10 numbered sections (s01–s10). It reaches 2,385 stars within ~2 months of creation, which positions it alongside the prior education-signal docs as evidence that **agent-internals literacy is now a distinct learning track**, not just a side effect of using SDKs.

The signal here is similar to the earlier "I've taught AI Agents to 2,300+ engineers" post and the Claude Architect certification guide: the ecosystem is producing reproducible, sectioned, code-anchored teaching material — but claw0 is the first one we have logged that is **built around reading a specific production codebase (OpenClaw)** rather than around generic agent patterns or vendor certification.

## What stands out immediately
Observed directly from the repo README:

- **10-section progressive structure**, each section adds exactly one concept while keeping prior code intact:
  - s01 Agent Loop (`while` + `stop_reason`)
  - s02 Tool Use (dispatch table & schema)
  - s03 Sessions & Context (JSONL persistence)
  - s04 Channels (Telegram, Feishu pipelines)
  - s05 Gateway & Routing (5-tier binding)
  - s06 Intelligence (prompt assembly, memory)
  - s07 Heartbeat & Cron (proactive scheduling)
  - s08 Delivery (write-ahead queue)
  - s09 Resilience (3-layer retry, auth rotation)
  - s10 Concurrency (named lanes, serialization)
- Approximately **~7,000 lines of progressive Python** across 10 runnable files — claim to inspect, but the layout matches the section count.
- **Anchored to Anthropic's Claude API directly** (requires `ANTHROPIC_API_KEY` + `MODEL_ID`). Not framework-mediated (no LangChain / LangGraph / etc.).
- **Trilingual documentation** (en / zh / ja). Korean is notably absent.
- Dependency surface is small but production-shaped: `anthropic`, `python-dotenv`, `websockets`, `croniter`, `python-telegram-bot`, `httpx`. The presence of `croniter` (s07 heartbeat) and `python-telegram-bot` (s04 channels) signals the curriculum reaches beyond REPL-style toy agents into delivery/scheduling concerns.
- Explicitly positions itself as a **reading aid for OpenClaw's production codebase** — i.e. the educational artifact is downstream of, and pointing toward, a specific harness implementation.

## Why clawfit should care
Three reasons, in increasing order of strategic weight:

1. **Education-signal continuity.** Adds a third datapoint to the education track (alongside the Maryam Miradi pattern-teaching post and the Claude Architect certification guide). Three independent signals in ~30 days is enough to treat "structured agent education" as a recurring axis, not noise.
2. **Harness-internals literacy as a new sub-axis.** Unlike the previous two signals (which teach *patterns* and *certification knowledge*), claw0 teaches the **internal anatomy of a harness** — agent loop, tool dispatch, session JSONL, write-ahead queue, retry onion, named lanes. This maps cleanly onto Level 2 (meta wrapper / harness) concerns, but viewed through the lens of "what does someone need to learn to build/extend one." That is a new framing the reference map doesn't currently capture.
3. **OpenClaw as an implicit reference target.** claw0 is downstream of an unlogged upstream: "OpenClaw." If OpenClaw is a meaningful Level 2 harness in the Chinese-language ecosystem, clawfit's reference map likely has a blind spot. This signal is a pointer worth following — but OpenClaw itself should be researched separately before any registry/reference-map action.

## Preliminary interpretation
Current best reading:

- **Education / ecosystem signal** (parallel to `2026-03-28` and `2026-04-01` docs).
- **Adjacent layer interest:** Level 2 (meta wrapper / harness) — the curriculum content describes harness internals — but the artifact itself is a teaching project, not a harness.
- **Sub-type:** "harness-internals tutorial" — distinct from pattern-teaching (Miradi) and certification-prep (Architect exam). Worth tagging if a third instance of this sub-type appears.

Distinguishing claim vs. validated fact:
- **Validated:** 10 sections, trilingual, MIT, Python 3.11+, anchored to Claude API directly, dependency list above, 2,385★ / 280 forks at scan time.
- **Claim to inspect (not yet validated):** ~7,000 LOC total; "each section adds exactly one new idea while keeping all prior code intact" (incremental property); accuracy of the OpenClaw-mapping claim (depends on OpenClaw's actual implementation).

## Status
- Logged as a research-watch signal under the education / ecosystem-maturity track. No reference-levels.md change recommended on a single signal; revisit if (a) a fourth education-track signal appears, or (b) OpenClaw itself surfaces as a harness worth mapping at Level 2.
