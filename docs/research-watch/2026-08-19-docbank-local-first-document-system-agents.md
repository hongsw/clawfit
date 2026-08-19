# Research Watch: Docbank — Local-First Document System for Humans and Agents

- Repo/Link: https://github.com/kenn-io/docbank
- Source: GeekNews

## Why this is worth watching
Docbank is described as a "self-sovereign document system enabling humans and agents to manage, search, and verify documents collaboratively." The explicit agent-native design — co-read/write by both humans and LLM agents — is a different angle from typical RAG pipelines or vector stores. The "verify" capability hints at document integrity/provenance features, relevant to governance-heavy orgs.

## What stands out immediately
- Local-first, self-sovereign: data stays on-prem, no cloud dependency
- Explicitly built for human+agent collaboration, not humans alone
- "Verify" suggests checksums or cryptographic provenance, not just search
- From GeekNews (Korean tech community), suggesting possible i18n / multilingual doc focus

## Why clawfit should care
Docbank fits between Level 3 (Memory/Context) and a potential knowledge-management layer. It could appeal to orgs with confidential data sensitivity (offline_mid_codegen profile) that need agents to interact with internal documents. If it has MCP server support it would be directly relevant as an MCP tool entry.

## Preliminary interpretation
Current best reading:
- **Level 3 — Memory / Context Systems** (document-oriented, local-first variant)

## Status
- Tracking: new entry, 2026-08-19. Needs repo star check and MCP/API interface confirmation before registry consideration.
