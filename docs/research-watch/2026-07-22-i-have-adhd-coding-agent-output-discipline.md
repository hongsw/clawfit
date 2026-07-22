# Research Watch: i-have-adhd — Coding Agent Output Discipline Skill

- Repo: https://github.com/ayghri/i-have-adhd (⭐6,811)
- Source: GitHub Trending, all languages, 2026-07-22
- Also see: `2026-04-14-karpathy-skills-claudemd-harness-guide.md`; `2026-07-11-mattpocock-skills-real-engineers-claude-skill-pack.md`

## Why this is worth watching

6,811 stars for a 10-rule text file is a direct measure of developer pain: agents burying actionable output in preamble is a friction point with no prior dedicated fix. Unlike the karpathy-skills CLAUDE.md (25k stars, behavioral guidance) or addyosmani/agent-skills (76k, content skills), i-have-adhd makes output discipline its singular concern and ships with a cross-agent plugin manifest — making it the first installable "output discipline" skill in the tracked ecosystem.

## What stands out immediately

- **10 rules, no code**: lead with action, number steps, end with concrete follow-up, limit lists to 5 items, no preamble, no recap, no pleasantries — pure behavioral constraint, zero functional capability added
- **Plugin manifest packaging**: `plugin.json`, `.claude-plugin/`, `.codex-plugin/`, and `skills/i-have-adhd/` directories — structured for marketplace installation, not manual CLAUDE.md paste
- **Cross-agent compatibility**: Claude Code and Codex tested; runtime-agnostic by design (no inference dependency)
- **281 forks / 34 commits**: fork ratio (~4% of stars) is unusually high for a text-only repo, suggesting active per-team adaptation of the ruleset rather than passive starring
- **"ADHD-friendly" label**: marketing framing that increases discoverability; actual rules are general output-discipline constraints applicable across developer contexts, not ADHD-specific accommodations

## Why clawfit should care

clawfit's scoring dimensions (latency, cost, LLM preference, baseline fit) do not capture output verbosity posture. The 6.8k star signal suggests developer persona — solo or fast-context workflows in particular — may benefit from an output-discipline axis at recommendation time. Because i-have-adhd uses installable plugin packaging, it can be surfaced as a skill-layer recommendation rather than embedded in agent or harness configuration.

This is the first isolated signal for "output discipline" as a dedicated skill. GSD (2026-04-14) and karpathy-skills (2026-04-14) touched output behavior incidentally; neither made it the primary product concern. The plugin-format distribution is what separates it structurally from those L3 behavioral specs.

## Preliminary interpretation

Current best reading:
- **Level 4b — Skill / capability extension layer** (primary: cross-agent plugin packaging and marketplace-oriented distribution distinguish it from a CLAUDE.md governance file)
- **Level 3 — Behavioral governance** (secondary: content is purely a behavioral specification with no functional capability addition)

Not L3 primary: the plugin manifest format and marketplace-install path — not a drop-in CLAUDE.md instruction block — are the tie-breaker. Not L1/L2: no inference or orchestration surface.

## Status

- First signal 2026-07-22; 6,811 stars, GitHub Trending; no registry entry (no runnable software, no cost/latency data)
- Pattern watch: first "agent output discipline" installable skill; a second independent signal would confirm a named L4b sub-type ("output-discipline skill pack")
- No reference-levels.md mutation: single signal; "when in doubt" rule applied
