# Research Watch: RuView — WiFi Spatial Intelligence Platform with Agent MCP Bridge

- Repo: https://github.com/ruvnet/RuView (⭐78,336)
- Source: GitHub Trending (2026-07-07)

## Why this is worth watching

RuView converts WiFi radio signals from ESP32 microcontrollers into structured spatial intelligence — presence detection, vital sign monitoring (breathing 6–30 BPM, heart rate 40–120 BPM), pose estimation, and occupancy counting — without cameras. At 78,336★ it is one of the highest-starred repositories in the current scan series. The reason it enters clawfit's scope is not the WiFi sensing itself but the explicit agent integration layer: an MCP server (`rvagent`) that bridges the sensing stack to Claude, Cursor, and swarm agents, and a 9-skill Claude Code plugin with 7 `/ruview-*` slash commands. This is the first tracked example of a physical-world sensing system that ships agent integration as a first-class artifact rather than a community afterthought.

## What stands out immediately

- MCP server (`rvagent`) with 6 tools for presence, vitals, and BFLD (body fluid / location / density) queries: agents can read physical environment state the same way they read files or call APIs
- 9-skill Claude Code plugin + 7 `/ruview-*` slash commands — the agent integration is maintained alongside the sensing stack, not a separate community project
- MetaHarness-based portable operator (`npx @ruvnet/ruview`) enabling deployment across multiple agent platforms
- "MEASURED-vs-CLAIMED honesty guardrail enforced in code" — explicit distinction between sensor readings and inferred values surfaced to the agent
- Contrastive CSI embeddings (128-dimensional) self-adapt to new environments in ~30 seconds, reducing setup friction for new deployments
- Quantized models fit in 8 KB; runs on $9 ESP32 boards — hardware cost is near-zero for the sensing layer
- 105-module catalog covering health, security, building, retail, and industrial verticals
- Models available on Hugging Face; institutional framing (RuVector + Cognitum Seed platform branding) suggests an org rather than a solo developer
- 82.69% accuracy on MM-Fi pose estimation dataset claimed — not independently verified in available sources

## Why clawfit should care

RuView sits at the edge of clawfit's defined scope ("AI coding agents, LLM agent runtimes, harnesses, workflows, capabilities, interfaces"). The WiFi sensing layer itself is outside scope. But the MCP server presents a genuine L4c entry point: any tracked agent with MCP support can now query physical environment state (is someone in the room? what's their breathing rate? how many people in the space?) via the same protocol used to access browser automation, code intelligence, or document retrieval. This creates a new capability category: **physical-world sensing as an MCP tool**. No prior L4c entry in clawfit's registry addresses physical environment observability; all current L4c tools operate on digital artifacts (code, documents, web pages, APIs). The "MEASURED-vs-CLAIMED honesty guardrail" is an interesting pattern worth monitoring — it suggests the author is aware that sensor uncertainty is a different class of uncertainty than LLM hallucination, and has made it a first-class design constraint in the agent integration layer.

The 78k★ count is an outlier for an IoT project. This level of community interest in a WiFi sensing tool that explicitly ships agent integration suggests that the physical-world ↔ agent boundary is a more active area than clawfit's current taxonomy reflects. This is primarily a scope-extension signal, not a recommendation candidate.

## Preliminary interpretation

Current best reading:
- **Level 4c primary — MCP/tool capability**: the `rvagent` MCP server is the mechanism through which existing tracked agents (Claude Code, Cursor, others) interact with physical sensing data; this is structurally parallel to Chrome DevTools MCP (browser environment) and Safari MCP (rendering environment)
- **Level 7 secondary — Infrastructure**: the ESP32 mesh sensing network is physical sensing infrastructure, analogous to edge compute for AI inference workloads

First signal for "physical-world MCP capability" as a named L4c sub-type — distinct from all current L4c entries (browser, game engine, document, code intelligence) by virtue of operating on physical sensor data rather than digital artifacts. The "environment class" taxonomy (browser-vendor MCP at L4c) would extend to `environment: physical` if a second independently maintained physical-world MCP sensor bridge appears.

## Status

- 78,336★, v0.8.3-esp32 (latest), Rust primary (55.1%), Python (15.1%), JavaScript (14.1%)
- Registry ineligible: no matching schema fields; `task` mapping unclear (presence detection, health monitoring, and building intelligence are not current clawfit task types); hardware dependency (ESP32) not expressible in current `hardware.json`
- Star count does NOT compensate for schema gap or scope-boundary status; 78k★ reflects IoT + maker community interest, not AI coding agent ecosystem adoption
- Schema watch: `environment: [browser, physical, game-engine, document]` for L4c MCP servers; `task: environment-sensing` candidate
- Scope note: recommend flagging in `docs/reference-notes/missing-recommendation-axes.md` under "physical sensing integration" — if a second physical-world MCP sensor bridge appears, this becomes a named L4c sub-type
- Claims to verify: 82.69% MM-Fi accuracy; no-latency-penalty claim for concurrent sensing + inference; "30-second adaptation" to new environments
- Promotion criterion: second independently maintained physical-world MCP sensor bridge → named `environment: physical` L4c sub-type; or `task: environment-sensing` added to schema
