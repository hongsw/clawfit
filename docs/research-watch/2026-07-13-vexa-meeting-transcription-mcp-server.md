# Research Watch: Vexa — Self-Hosted Meeting Transcription API with MCP Server

- Repo: https://github.com/Vexa-ai/vexa (⭐2,500)
- Source: GitHub Trending Python (2026-07-13), v0.12.1
- Also see: `docs/research-watch/2026-07-04-meetily-privacy-first-local-meeting-agent.md` (local-first counterpart)

## Why this is worth watching

Vexa is the first tracked system that pairs a multi-platform meeting bot network with an explicit MCP server endpoint and an LLM-driven workspace compiler that outputs Markdown knowledge bases. That three-part combination — capture, MCP exposure, and LLM-maintained KB — is a named architectural pattern: a meeting context pipeline where the terminal artifact is agent-readable structured knowledge rather than a human-facing summary. The ephemeral container model (sub-second spawn, reaped on idle, continuity via session file) applied to both bot capture and agent workloads is architecturally closer to background-agents or Modal sandboxes than to conventional meeting-notes apps. At 2,500 stars and a v0.12.1 release dated July 12, the project has reached functional completeness in its capture domain while the agent/MCP layers remain early.

## What stands out immediately

- **Two-domain API behind a single gateway:** Meetings domain handles bot capture and transcript streaming (WebSocket/polling, speaker attribution); Agents domain handles workspace compilation and knowledge work. The gateway routes by domain, not by user session — this is a stateless routing model with domain-scoped state behind it.
- **Ephemeral container execution for both bots and agents:** Each bot or agent workload spawns an isolated container (Docker default, Kubernetes and process-based backends documented) that is reaped on idle. Continuity is carried by a session file in the workspace, not by the container lifetime. The repo claims sub-second starts and parallel thousands — both are claims to inspect.
- **MCP server asserted but underspecified:** The README header lists "MCP server for AI agents" as a key feature. No MCP compliance specification, tool manifest, or transport details appear in the extracted repo surface. Whether this is a stdio server, an HTTP/SSE server, or a stateless HTTP server per the 2026-07-28 RC protocol cannot be determined from public docs alone.
- **Workspace compilation to Markdown:** The Agents domain compiles meeting content (transcripts, attributed segments) into portable Markdown/OKF bundles. This is the Karpathy LLM Wiki pattern applied to meeting corpora — LLM as maintainer of a structured KB, not just consumer.
- **Calendar sync and scheduled auto-join:** Bots join meetings on calendar-driven schedules and support event-triggered dispatch. This is a production operational feature, not a demo capability — it assumes a persistent service rather than a one-shot CLI.
- **Four-platform bot coverage:** Google Meet, Microsoft Teams, Zoom, Jitsi. Compared with Meetily (macOS + Windows desktop app capturing local audio), Vexa's bots join remotely via platform APIs, requiring no local audio device on the user's machine. Deployment implication: Vexa can transcribe meetings the user is not physically attending.
- **No explicit local-inference guarantee:** Meetily specifies fully local inference (Parakeet + SortFormer + Ollama, no outbound API calls). Vexa makes no equivalent claim. The self-hosted deployment option provides some privacy boundary but does not preclude outbound LLM API calls in the Agents domain.
- **Python 49%, TypeScript 42.9%:** A language split suggesting the capture pipeline (Python) and the terminal UI / MCP server surface (TypeScript) are architecturally separated rather than collocated.

## Why clawfit should care

The taxonomy question the task description raises — whether MCP server or human-interface meeting capture is the right anchor — resolves as follows against the canonical reference-levels.md:

**The bot-capture layer is Level 7** (human interface / voice / input-output layer). Ghostmeet, Ghost Pepper, and the realtime voice agent frameworks (Pipecat, LiveKit) all sit in Level 7 precisely because audio/meeting input is their primary surface. Vexa's auto-join bots are the Level 7 component — they capture the meeting as a human-interface input event.

**The MCP server is the L4c anchor.** The MCP server, if compliant, transforms Vexa from a standalone transcription service into a tool-use capability layer that any MCP-compatible AI agent can consume. This is the same pattern as chrome-devtools-mcp or n8n-mcp: a pre-existing domain (browser, workflow automation, meeting transcription) exposed as a structured MCP capability surface. L4c (tool-use / action infrastructure) is the right primary classification — subject to verification of MCP compliance.

**The workspace compiler is the L6b secondary.** The Agents domain producing Markdown/OKF bundles from meeting content is the LLM-native knowledge base pattern (L6b): the LLM maintains the structured artifact, the meeting transcript is the source corpus, and the output is a human-inspectable and agent-queryable Markdown KB. This aligns with wuphf and GBrain's L6b classification in the reference map.

Note: the meetily research watch doc (2026-07-04) classifies Meetily as "Level 6 secondary — Human interface layer." In reference-levels.md canonical numbering, human interface is Level 7, not Level 6. The meetily doc appears to use an older or informal level numbering. This document follows the canonical reference-levels.md numbering: capture = Level 7, MCP = L4c, KB compiler = L6b.

clawfit's current task types (`qa`, `code-gen`, `research`, `vibe-coding`) do not map to meeting transcription or meeting-knowledge compilation. The same schema gap that blocks meetily applies here. However, Vexa's MCP server, if verified, has a cleaner registry path: it could qualify as an L4c MCP capability provider paired with an existing task type if a `meeting-transcription` or `knowledge-capture` task type is added, or if an `mcp_capability_type: meeting` field is introduced in the registry schema.

## Preliminary interpretation

Current best reading:

- **L4c primary — MCP capability provider / tool-use infrastructure** (the MCP server, if specification-compliant, exposes meeting transcription data as a structured agent capability layer; first signal for a "meeting-transcription MCP server" sub-type in L4c, distinct from browser-vendor MCP and workflow-platform MCP sub-types already named)
- **L6b secondary — LLM-native knowledge base** (workspace compiler produces Markdown KB bundles from meeting content; LLM maintains the structured artifact, not just queries it; aligns with wuphf / GBrain L6b pattern applied to a new source corpus type: meeting transcripts)
- **Level 7 tertiary (capture mechanism only)** — auto-join bots as the audio/meeting input capture layer; this is the means by which content enters the pipeline, not the architectural novelty that determines the primary classification

This is structurally different from Meetily (L1 primary runtime + Level 7 secondary capture) and from Ghostmeet (Level 7 only, no MCP or KB compilation layer). Vexa's primary value for AI agents is downstream of capture, in the MCP/KB layers.

## Claims to verify

- **MCP server specification compliance:** The README asserts an MCP server exists. Transport model (stdio / HTTP+SSE / stateless HTTP per 2026-07-28 RC), tool count, tool manifest, and whether `MCP-Protocol-Version` headers are present are not visible from repo surface. A stateful session-bearing MCP server would require migration if the 2026-07-28 RC is adopted.
- **Sub-second ephemeral container starts and parallel thousands:** Specific quantitative claims without a cited benchmark environment. Docker cold-start behavior varies significantly by image size and host; the claim is plausible for pre-warmed images but not verified.
- **Calendar sync scope and permissions:** Calendar integration implies OAuth or service account access to user calendar data. The privacy boundary of this access (what is read, what leaves the self-hosted instance) is not visible from the repo surface.
- **LLM backend for workspace compilation:** The Agents domain description says agents "compile meeting content into Markdown knowledge bases." Which LLM, at what cost, with what prompt template, and with what privacy characteristics (local model vs. outbound API call) is not specified.
- **Four-platform bot stability:** Joining Teams, Zoom, Meet, and Jitsi via bots depends on undocumented or semi-stable platform APIs; reliability per platform is not reported.

## Status

- 2,500★ — below the 5k registry threshold; registry entry deferred
- No schema match: no `task` value in current clawfit schema covers meeting transcription or meeting-knowledge compilation
- MCP server classification held pending specification verification; single-signal rule applies to "meeting-transcription MCP server" as an L4c sub-type
- Contrast signal against Meetily: Vexa is the API-first, multi-platform, MCP-exposing counterpart to Meetily's local-desktop-only positioning; they do not overlap architecturally and neither displaces the other
- Promotion path: 5k★ AND verified MCP compliance AND `task: meeting-transcription` or `mcp_capability_type: meeting` schema addition
