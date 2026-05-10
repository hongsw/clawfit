# Research Watch: hunk — Review-First Terminal Diff Viewer for Agent-Authored Changesets

- Repo: https://github.com/modem-dev/hunk
- Also see: https://deepwiki.com/modem-dev/hunk (architecture deep-dive); https://deepwiki.com/modem-dev/hunk/3.2-agent-context-and-annotations (agent context system detail); https://altbox.dev/tool/hunk/ (tool index entry)

## Why this is worth watching

hunk occupies a structural gap that no current tracked tool fills: it is a dedicated human-review checkpoint layer designed specifically for agent-generated code changes. Where other L2 harnesses manage agent execution, hunk positions itself at the output boundary — the moment a human must inspect and accept what an agent has produced. The MCP live-comment mechanism lets agents annotate their own diff output in real time, creating a two-way channel between agent and reviewer that is architecturally distinct from both the agent runtime and the diff display tool. At 3.1k stars and v0.11.1 released May 10, 2026, it is below the informal registry threshold but accelerating in a direction no peer tool currently occupies.

## What stands out immediately

- **"Review-first" is an architectural stance, not a UX label.** hunk reframes the terminal diff workflow: rather than piping `git diff` output to a pager and reading it linearly, it opens a structured review UI as the primary interaction mode. This is a claim that interactive, annotated inspection should precede any human acceptance decision on agent output — a design thesis consistent with human-in-the-loop patterns appearing across the agent ecosystem in 2026.

- **Dual annotation delivery mechanisms.** Static annotations arrive via a sidecar JSON file (`--agent-context`) merged at load time; dynamic annotations arrive via MCP "live comments" constructed at runtime. Both are normalized into the same `AgentAnnotation` interface (`oldRange`/`newRange` line tuples, `summary`, optional `rationale`, `confidence` level). The unification of static + live annotation into a single model is architecturally clean — claim to inspect whether agent tools actually produce the sidecar format in practice vs. the MCP path being the only used channel.

- **Agent-aware file ordering.** The `orderDiffFiles` function resequences the review file list according to the agent's own declared order in the `AgentContext`, not alphabetical or git-natural order. This means an agent can surface the most structurally significant change first — a subtle but consequential design choice that privileges agent reasoning about what matters over default tooling conventions.

- **MCP daemon as loopback, not server.** The MCP integration is described as a "loopback" that allows an external agent process to remotely steer an active hunk session — add live comments, navigate to hunks. This inverts the typical MCP topology: rather than the agent using hunk as a tool, hunk exposes a surface for agents to push context into a human-facing session. This is an observability-push pattern, not a capability-pull pattern.

- **Hunk skill file for agent loading.** The `docs/agent-workflows.md` describes loading a "Hunk skill file" inside the agent so it can drive the review session. This SKILL.md / skill-file pattern mirrors the clawfit-vocabulary and the broader skill-layer conventions tracked at L4. Claim to inspect: whether the skill file is an MCP skill, a CLAUDE.md snippet, or a separate protocol.

- **jj (Jujutsu VCS) support added in v0.11.0.** Alongside Git, hunk added `vcs = "jj"` support for `hunk diff [revset]` and `hunk show [revset]` — tracking the emerging Jujutsu version control adoption curve among developers who use advanced VCS tooling. This signals modem-dev is building for early-adopter developer profiles, not mainstream Git-only workflows.

- **macOS and Linux only.** No Windows binary listed. Same platform constraint seen in Helmor (macOS-only at v0.20.1). Not a showstopper for the developer profile hunk targets, but a filter dimension to record.

- **Built on OpenTUI and Pierre.** TypeScript 99.5%, Node.js 18+ runtime, React-based app shell rendering to terminal. The Pierre diff engine handles syntax-highlighted rendering. This is a modern TypeScript-native terminal UI stack — reproducible and auditable, not a thin wrapper over an existing pager (less, delta, difftastic).

- **Star velocity and version cadence.** 3.1k stars, v0.11.1 on May 10 (yesterday), with v0.10.0 on April 26 — roughly a minor version per two weeks. Active, directed iteration rather than a single-release project.

## Why clawfit should care

**1. hunk is the first explicit "review checkpoint" tool in the tracked taxonomy.** Every other tool at L2 (harnesses: Ruflo, deepagents, Helmor) is concerned with _running_ agent workflows. hunk is concerned with _inspecting_ agent output before human acceptance. This is a new architectural role — call it a review gate or changeset inspector — that sits between agent execution and human approval. If clawfit ever adds a `human_review_required: true` filter axis for governance-sensitive profiles, hunk is the natural recommendation alongside whatever L2 harness is running the agent.

**2. The MCP loopback pattern is architecturally distinct from all current L5 MCP entries.** Current L5 entries (codegraph, GitNexus, claude-peers) consume the MCP protocol to extend agent capability. hunk uses MCP as a push channel from agent into a human-facing UI. This is a new MCP usage pattern — not tool provision, not context retrieval, but real-time annotation injection into a review interface. It does not fit cleanly into the L4 (capability) or L5 (memory/context) definitions. It is closer to L2 observability infrastructure but with an L6 (human interface) delivery mechanism. The dual-layer characteristic is analytically interesting.

**3. The sidecar AgentContext schema is an emerging standard candidate.** The `AgentContext` JSON format (version, summary, files → path + summary + annotations → oldRange/newRange + summary + rationale + confidence) is a minimal but complete schema for structured agent change rationale. If this format were adopted by multiple agents as a standard output artifact (similar to how `CLAUDE.md` became a cross-tool governance convention), it would constitute an L3-adjacent specification. Single implementation today — not enough to flag as a standard, but worth watching for adoption by a second agent tool.

**4. No current clawfit scoring axis captures "agent output review tooling."** The recommendation pipeline filters on task, latency, budget, network, and statefulness. None of these surfaces a `review_tooling` or `changeset_inspection` dimension. For `task: code-gen` profiles with `governance_need: hard` or `data_sensitivity: confidential`, the absence of a review-gate recommendation is a gap. hunk names and fills that gap.

**5. The `confidence` field on annotations (`low`/`medium`/`high`) is a lightweight trust signal.** An agent that annotates its own changes with confidence levels is providing a self-assessment that a human reviewer can weight. This is a different signal from the pass/fail evaluation patterns tracked in the Awesome-Agent-Harness survey's V component — it is inline, per-hunk, and authored by the agent rather than derived from a post-hoc evaluation harness. Whether agents in practice populate this field meaningfully vs. always asserting `high` is a claim to inspect.

## Preliminary interpretation

Current best reading:

- **Level 6 — Human interface / multimodal layer (primary).** hunk's primary architectural function is surfacing agent-generated change context to a human reviewer. The terminal UI, annotation rendering, file navigation, and confidence display are all in service of a human making an informed accept/reject decision. This is an L6 concern — the human interface through which agent work becomes human-legible and human-approved. The "review-first" thesis is explicitly a human-attention design claim.

- **Level 2 — Meta wrappers / harnesses / orchestration layers (secondary, MCP loopback).** The MCP daemon that allows agents to remotely inject live comments into an active session is an orchestration-layer capability: it closes the loop between agent execution and agent visibility into the review state. The skill-file loading mechanism that lets an agent drive a hunk session also sits at L2 (harness-initiated control flow). This secondary classification reflects the agent-control surface, not the human-facing surface.

- **Not L4.** hunk does not provide capability tools for agents to invoke. The MCP surface is annotation injection, not tool provision.

- **Not L5.** No memory retrieval, context store, or persistent knowledge substrate. The sidecar JSON is a per-session artifact, not a long-lived context layer.

- **Sub-type candidate: terminal review gate / changeset inspector.** Distinguished from diff pagers (delta, difftastic, lumen) by agent-annotation rendering and MCP push channel; distinguished from L2 harnesses (Helmor, Ruflo) by operating on agent output rather than agent execution; distinguished from L4 MCP servers (codegraph, GitNexus) by pushing annotations toward humans rather than pulling context into agents. This sub-type has no existing name in the taxonomy and no second sample yet — record as candidate.

## Status

- 3.1k stars, MIT, TypeScript 99.5%, v0.11.1 (May 10, 2026). Below the 5k-star registry promotion threshold. Active cadence (minor version per two weeks). Not a registry entry candidate today. Watch at 5k stars or first confirmed adoption by a second agent tool consuming the `AgentContext` sidecar format as a standard output artifact. Primary classification: **L6** (terminal human interface for agent changeset review). Secondary: **L2** (MCP agent-loopback control channel). Sub-type "terminal review gate / changeset inspector" recorded as candidate — promotion threshold is a second independent tool occupying the same review-checkpoint role in the agent pipeline. The `AgentContext` JSON schema is an embryonic standard worth tracking separately from the tool itself.
