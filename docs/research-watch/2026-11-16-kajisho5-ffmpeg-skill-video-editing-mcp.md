# Research Watch: kajisho5/ffmpeg-skill — Local Video Editing Skill Pack for Coding Agents

- Repo: https://github.com/kajisho5/ffmpeg-skill (⭐6,445)
- Source: GitHub Trending (475 stars today)

## Why this is worth watching
ffmpeg-skill exposes 42 FFmpeg operations as a typed MCP server and a machine-readable contract — no cloud service, no API keys, stdlib-only Python, FFmpeg 6.1+ required. It is a narrow single-domain L4 skill pack targeting video editing workloads in coding agents (Claude Code, Cursor, Codex). At 6,445 stars with 475 gained today, it is significantly above the 100-star signal threshold and is trending. This is the fifth domain-specialist skill pack tracked in the scan corpus, adding video/media editing to PM, scientific, finance/quant, and security/red-team.

## What stands out immediately
- 42 tools organized into Analysis, Editing, Audio, Picture, Delivery, and Orchestration categories
- `contract --json` generates machine-readable tool schemas at startup from argparse, keeping advertised signatures in sync with actual scripts
- MCP server uses stdio JSON-RPC transport (`mcp/server.py`) — no network daemon required; works in any MCP-compatible coding agent
- By default only 12 core tools are listed; `FFMPEG_SKILL_MCP_FULL=1` exposes all 42 — controlled surface area reduces agent tool-list bloat
- Five workflow prompts (`reel`, `podcast`, `multicam`, `delivery_check`, `hdr`) provide intent-level orchestration on top of primitive tools
- Arguments are typed and explicit (argparse-generated schemas); no raw filter-graph injection — reduces prompt-injection risk in video processing
- `doctor` command checks which FFmpeg capabilities are present before operation
- Optional local speech transcription for caption/subtitle generation; not required for core operations
- CI tests FFmpeg 6.1 through 9.x — unusually broad version range for compatibility coverage

## Why clawfit should care
ffmpeg-skill is structurally equivalent to claude-trading-skills and K-Dense scientific-agent-skills at the domain-specialist skill pack layer: a pure L4b drop-in with no harness changes required. The video editing domain is new to the tracked corpus. The pattern — domain expert produces a skills layer for a specific vertical rather than building a whole harness — is becoming common enough that clawfit's registry may need a `skill_domain` field to distinguish domain packs from general-purpose skill collections. ffmpeg-skill also demonstrates a mature capability contract pattern (`contract --json`) that could serve as a reference for skill pack quality standards.

## Preliminary interpretation
Current best reading:
- **Level 4b — Domain Skills Layer** (video/media editing vertical)
- Secondary classification: L4c (MCP server delivery)

## Claims to verify
- Star count authentic (6,445 is high for a domain skill pack; verify not inflated by bots)
- Whether the 42-tool surface is genuinely stable or still rapidly changing (commit cadence check needed)
- `contract --json` output is actually machine-parsable by all three named agents (Claude Code, Cursor, Codex) — only Claude Code confirmed in README
- Local speech transcription dependency and whether it conflicts with common agent sandboxing configurations

## Status
- First scan: 2026-11-16
- Registry action: deferred — L4 skill packs do not have a cost/latency scoring dimension in the current registry schema; `skill_domain` field is not yet available
- 📡 Note: Fifth domain-specialist skill pack signal (PM Jun-10, scientific Aug-04, finance/quant Nov-15, security Nov-16, video/media today); the four-signal rule for `domain_skill_pack` as a confirmed sub-type was met Nov-16 (security domain); five signals now span five independent verticals — the pattern is wider than the specific domains; `skill_domain` field addition to registry schema is now five-signal justified
