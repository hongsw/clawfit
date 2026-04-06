---
# Research Watch: oh-my-pi + Hashline — "The Harness Problem" analysis

- Repo: <https://github.com/can1357/oh-my-pi>
- Article: <https://blog.can.ac/2026/02/12/the-harness-problem/>

## Why this is worth watching
The author of `oh-my-pi` published a blog post explicitly called "The Harness Problem" — the first serious technical analysis of why harnesses themselves are often the bottleneck in agent workflows, not the model. The **Hashline** approach is their solution: content-hash verification of file reads to prevent editor corruption during concurrent multi-agent use. This is a rare signal: a technically rigorous critique of harness design that proposes a concrete protocol-level fix.

## What stands out immediately
- **Core thesis:** "The harness itself is often the bottleneck, not the model" — a precise diagnosis of where agent workflows break
- **Hashline:** each file read is verified by content hash; if the file has changed since the hash was issued, the agent re-reads before editing — prevents stale-read corruption
- **Problem being solved:** concurrent multi-agent editing of the same file causes silent corruption, especially in long-running sessions
- **`oh-my-pi`** is a fork of Mario Zechner's Pi coding agent implementing this approach
- Article predates most harness-design discussions but frames the problem more precisely than most

## Why clawfit should care
"The Harness Problem" framing is conceptually important for clawfit's ecosystem map — it names a failure mode that affects Level 2 tools directly. clawfit's scoring model currently has no axis for **harness reliability** (as distinct from latency or cost). The Hashline pattern represents an emerging class of harness-correctness tooling that may become a selection criterion.

Cross-reference with Anthropic's sprint-contract pattern (also tracked): both are responses to the same underlying problem of long-running agent workflows losing coherence.

## Preliminary interpretation
- Primary: **Level 2 — Meta wrappers / harnesses / orchestration layers**
- Technical contribution: Hashline as a protocol primitive for concurrent multi-agent file safety

## Status
- Medium priority for registry; high priority as a conceptual reference.
- "Harness reliability" is a candidate new scoring axis — flag for scoring-analyst.
