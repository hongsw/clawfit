# Research Watch: hubble.md

- Repo/Link: https://github.com/bholmesdev/hubble.md
- Source: GeekNews front page (2026-08-16)
- Stars: ~1,300 (MIT, TypeScript/Electron)

## Why this is worth watching
hubble.md positions a markdown note-taking app as a shared workspace where human and AI agents co-edit the same files in real time. The note folder is a live mount point: agents write, the app reloads and renders — making markdown files the bidirectional coordination primitive between human and agent, not a static prompt template or a structured API.

## What stands out immediately
- **Live agent mount**: any folder can be "pointed at" a running agent; changes surface immediately in the editor UI
- **Electron desktop + CLI**: operates locally with no cloud dependency for core note/agent sync
- **HTML custom views**: frontmatter-backed notes can be visualized as tables, maps, or bookshelves via user-defined HTML templates — agent-generated structured data becomes a browsable human interface
- **Pnpm monorepo**: `apps/desktop` (Electron), `apps/web` (Astro), `apps/www` (React + Convex), editor core via Tiptap — well-structured stack for an early-stage project
- Uses Warp Factory agents for its own repo triage/implementation (dog-fooding)
- Star count: ~1,300 (below 5k registry threshold at scan time)

## Why clawfit should care
This is the first tracked entry where a *note-taking app* is the agent-human interface rather than a chat UI, terminal, or IDE. The mount-and-sync pattern (human and agent share a filesystem folder, UI reloads on agent writes) is a distinct L6 sub-type: "shared-filesystem human-agent interface" — different from control surfaces (t3code, paseo) and different from agent-populated dashboards (Refly). If this pattern spreads, a `human_interface_model` axis becomes relevant for filtering: `[chat | terminal | ide | shared-filesystem | overlay]`.

## Preliminary interpretation
Current best reading:
- **Level 6 — Human Interface / Control Surface** (primary): the Electron app is the surface through which a human observes and co-edits agent-produced content; agents operate on the underlying filesystem, the UI reflects their work in real time.
- **Level 4b secondary**: agent skill/command integration via `/` commands; note templates function as reusable agent task specs.

## Status
- First signal for "shared-filesystem human-agent note interface" pattern
- Below 5k threshold — no registry entry this run; watch for elevation
- No canonical section change: single-signal, two-signal rule requires a second independent shared-filesystem human-agent interface at ≥1k★
- Schema watch: `human_interface_model: [chat | terminal | ide | shared-filesystem | overlay]`
