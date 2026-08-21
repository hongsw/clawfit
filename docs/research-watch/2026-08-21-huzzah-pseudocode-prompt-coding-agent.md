# Research Watch: Huzzah — Pseudocode-as-Prompt Coding Agent Editor

- Repo/Link: https://danielvaughn.dev/posts/huzzah/
- Source: Hacker News (rank 9, Show HN: "novel approach to coding with AI")

## Why this is worth watching
Huzzah proposes a structural shift in how developers issue instructions to AI coding agents: instead of chat-based imperative prompts, developers write persistent declarative pseudocode files that are diff-compared on each change so only the delta becomes the AI's prompt. This is a methodologically distinct alternative to the dominant streaming-chat interface used by Claude Code, Aider, Cursor, and Cline.

## What stands out immediately
- Prompts are **pseudocode** (not natural language), **declarative**, and **persistent** on disk
- Diff-capture: only changed pseudocode becomes the prompt context — reduces token waste from repeated instructions
- Produces a durable record of developer intent separate from the generated code
- Experimental personal project; no public repository link in the blog post
- No stars/public repo yet — blog post with working prototype demonstrated

## Why clawfit should care
The interaction paradigm affects L2 (harness/agent methodology) and L6 (human interface layer). If pseudocode-as-prompt gains adoption, clawfit's `primary_task` and `primary_role` scoring dimensions would need to distinguish between imperative-chat and declarative-file interaction modes. The diff-based context pattern is also a potential signal for how future coding agents reduce token cost — relevant to clawfit's `monthly_budget` scoring since efficient context use changes the cost calculus for medium-budget profiles.

## Preliminary interpretation
Current best reading:
- **Level 2 — Agent Methodology / Harness Layer** (primary: novel prompt-interaction pattern wrapping an AI coding backend; secondary: L6 human interface — the editor UI surface is where the pseudocode files live)

## Status
- Tracking: first signal for "persistent declarative pseudocode as prompt" interaction pattern
- Two-signal rule: not yet met
- No registry entry: experimental prototype, no public repository, no schema mapping
- Watch: if a public repo emerges or the approach is adopted by an existing L2 tool (Aider, Continue, etc.)
