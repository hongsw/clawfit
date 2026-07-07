# Research Watch: claude-video — Video Analysis Slash Command for Claude

- Repo/Link: https://github.com/bradautomates/claude-video
- Source: GitHub Trending (2026-07-07)

## Why this is worth watching
claude-video ships a `/watch` command that gives Claude Code a three-stage video analysis pipeline — acquisition via `yt-dlp`, frame extraction via `ffmpeg`, and transcription via Whisper/Groq — without requiring any changes to Claude itself. At ~4,205 stars it sits just below the standard 5k registry threshold, but the slash-command form factor is a direct match for the L4b installable-skill pattern already well-represented in the ecosystem. Video is the only major input modality not yet covered by a tracked L4b capability in this scan series.

## What stands out immediately
- `/watch <url> <question>` is the entire user-facing surface — thin interface over a non-trivial pipeline
- Four detail modes (`transcript`, `efficient`, `balanced`, `token-burner`) let callers trade latency for fidelity; `efficient` completes in ~0.5s
- Intelligent frame budgeting caps token use by video duration (30s ≈ 30 frames; 10min+ capped at 100 by default)
- Frame deduplication via 16×16 grayscale MAD comparison drops near-identical frames before they reach Claude — token-aware by design
- Prefers native captions (free, instant) over Whisper transcription; Groq is the preferred fallback, OpenAI is secondary
- Zero-config install: missing `ffmpeg`/`yt-dlp` dependencies auto-install on first run
- No persistent memory or agentic loop — purely a preprocessing shim; Claude does all reasoning

## Why clawfit should care
clawfit currently has no L4b entry covering video as an input modality. The `/watch` command pattern is directly analogous to `graphify` (code → knowledge graph skill) and `book-to-skill` (PDF → skill), both tracked L4b. If video analysis becomes a recurring task profile — bug reproduction clips, tutorial walkthroughs, product demo reviews — this is the natural recommendation for orgs already running Claude Code. The detail modes map cleanly to existing latency filter values (`transcript` ≈ low latency, `balanced` ≈ medium). Token-budgeting design is a positive signal for `budget`-constrained profiles.

## Preliminary interpretation
Current best reading:
- **Level 4b — Capability / skill layer** (multimodal video input sub-type; slash-command installable)
- Level 6 secondary weak (multimodal input modality expansion)

## Status
- First signal at ~4,205★ — below 5k registry threshold; monitor for threshold crossing; no schema gap blocking eventual registry entry
