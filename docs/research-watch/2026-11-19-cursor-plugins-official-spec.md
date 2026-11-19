# Research Watch: Cursor Plugins (Official Spec)

- Repo/Link: https://github.com/cursor/plugins
- Source: GitHub Trending

## Why this is worth watching
Cursor has shipped an official plugin specification with bundled first-party plugins in TypeScript. At 17,185 stars on the first day trending, this formalizes the Cursor extension ecosystem and sets a standard that competing IDE agents (Roo Code, Continue, Windsurf) will need to respond to.

## What stands out immediately
- Official spec from Cursor team, not a third-party wrapper
- TypeScript-first — aligns with the broader VS Code extension pattern
- Likely to attract an ecosystem of community plugins quickly
- Directly comparable to Claude Code's skills/hooks system

## Why clawfit should care
clawfit already tracks Cursor as a tool. This formalization elevates Cursor's ecosystem score — it now has a stable plugin API, which improves its "extensibility" and "governance" dimensions. The existing Cursor entry in tools_registry.json may warrant a features update to include "plugins".

## Preliminary interpretation
Current best reading:
- **Level 4 — Plugin/Skill Layer**: This is the Cursor-native plugin/skill system, analogous to Claude Code skills. It operates above the IDE agent harness and below application-specific integrations.

## Status
- Tracking: new, official release
