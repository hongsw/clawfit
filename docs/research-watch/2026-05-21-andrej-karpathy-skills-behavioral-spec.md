# Research Watch: multica-ai/andrej-karpathy-skills

- Repo/Link: https://github.com/multica-ai/andrej-karpathy-skills
- Source: GitHub Trending (#4, 141,000★, all languages)

## Why this is worth watching

A single `CLAUDE.md` file packaged as an installable Claude Code plugin, encoding Andrej Karpathy's observed LLM coding pitfalls into four declarative principles: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. At 141k stars it is the second-largest L3 behavioral-spec signal in this taxonomy (behind obra/superpowers at 199k). The multica-ai org already ships a managed agents platform (`multica`, tracked in registry); this repo is a standalone behavioral spec from the same org.

## What stands out immediately

- Installable as a Claude Code plugin: `/plugin install andrej-karpathy-skills@karpathy-skills`
- Four principles directly address Karpathy's complaint: "models make wrong assumptions and run with them without checking"
- Transforms imperative instructions into declarative goals with verification loops
- Cursor integration guidelines also provided
- MIT license — no commercial restrictions
- Available in English and Chinese README

## Why clawfit should care

This repo is the highest-starred L3 behavioral-spec entry that targets assumption-prevention and simplicity enforcement rather than team coordination or spec lifecycle. It defines the emerging "anti-bloat SSOT" sub-type: a CLAUDE.md that primarily encodes what *not* to do (assumptions, premature abstraction, dead code) rather than what workflow *to* follow. The plugin packaging is a new mechanism — installable via marketplace command, not just file-copy — which is the first L3 entry using the Claude Code plugin marketplace as distribution.

Note: `2026-04-14-karpathy-skills-claudemd-harness-guide.md` tracked a prior Karpathy reference. This `multica-ai/andrej-karpathy-skills` repo is a distinct, packaged, plugin-distributed derivation that has become the dominant community implementation.

## Preliminary interpretation

Current best reading:
- **Level 3 — Behavioral Spec / SSOT layer**
- Sub-type: anti-bloat declarative CLAUDE.md (distinct from methodology guides like gsd/superpowers and from git-native definitions like gitagent)
- Secondary: installable plugin-marketplace distribution (new distribution channel for L3 specs)

## Status

- 141k★, MIT, multica-ai org — exceeds registry threshold by star count
- Deferred per single-signal rule for the "anti-bloat plugin-distributed CLAUDE.md" sub-type
- Promotion threshold: a second independent ≥10k★ CLAUDE.md packaged and distributed via plugin marketplace, OR confirmation that this sub-type is structurally distinct from existing L3 entries in the canonical section
- Watch: whether this displaces file-copy install as the dominant CLAUDE.md distribution mechanism across the ecosystem
