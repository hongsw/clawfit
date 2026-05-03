# Research Watch: Mendral — "The Agent Harness Belongs Outside the Sandbox"

- Repo: https://www.mendral.com/blog/agent-harness-belongs-outside-sandbox
- Also see: https://www.mendral.com/blog/agent-harness-inside-vs-outside-sandbox, https://www.mendral.com/blog/anatomy-of-a-production-ai-agent, https://blaxel.ai/blog/mendral-builds-the-first-24-7-ai-devops-engineer-using-blaxel
- Source: Hacker News, 118 pts, 2026-04-10; authors Andrea Luzzardi and Sam Alba (Docker co-founders, Dagger alumni)

## Why this is worth watching

The post is an architectural opinion from two engineers who built Docker and Dagger — their choices carry ecosystem weight that a generic startup post does not. The central claim — that the agent control loop must live outside the execution sandbox, with sandboxes treated as stateless, ephemeral cattle — formalizes a split that the broader ecosystem (Blaxel, E2B, Daytona, Freestyle) has been converging on independently. This is not a product announcement; it is a named, reasoned pattern with a reference implementation, published as a harness-design argument rather than a marketing piece.

## What stands out immediately

**Architectural stance**
- The loop-outside-sandbox split draws a hard boundary: LLM API keys, user tokens, and database credentials never enter the sandbox; only tool invocations cross the boundary via API call
- Sandboxes are explicitly framed as "cattle not pets" — interchangeable, suspendable, and replaceable without session loss
- This contrasts with the common pattern (Cline, many self-hosted setups) where the loop and tools share a container and a filesystem

**Durable execution via Inngest**
- Each agent turn is an Inngest step; steps are individually retriable if the server restarts mid-session
- Claimed benefit: rolling deploys and infrastructure failures do not corrupt in-flight agent sessions
- The choice of Inngest (rather than a custom queue) is load-bearing: it means the harness's durability properties are inherited from a separate, composable durable-execution layer rather than built from scratch (claim — the production failure characteristics of Inngest in this configuration are not independently validated here)

**Sandbox lifecycle via Blaxel**
- Sandbox suspends during idle periods (LLM waiting, CI pipeline wait) and resumes in ~25ms (vendor-claimed figure; Blaxel uses Firecracker-forked microVMs)
- Boot from cold: under 125ms (Blaxel claim)
- This lifecycle model is only possible because the loop is outside: if the loop were inside the container, suspending the sandbox would kill the loop

**Filesystem virtualization**
- Rather than adding discrete database-query tools, Mendral routes at the filesystem path level: `/workspace/*` → ephemeral sandbox storage; `/skills/*` and `/memory/*` → Postgres
- The model's `read`/`write`/`edit` API surface is unchanged from its training distribution — the routing is invisible to the agent
- The stated motivation is explicit: "more tools make agents worse" — so instead of adding a DB tool, they virtualize the path to avoid touching the tool count
- Acknowledged limitation: filesystem consistency model is currently last-writer-wins per key; bash command interception relies on "best-effort guards" rather than strict enforcement (author's own words)

**Multi-user as a database problem**
- Multiple concurrent users sharing skills and memories is handled at the Postgres layer, not by replicating the sandbox
- Updates are immediately visible across parallel sessions — no sandbox coordination needed
- This is a meaningful architectural consequence: horizontal scale becomes orthogonal to per-session compute

**Production operational claims (claims to inspect)**
- Closes 16,000+ CI investigations monthly
- Processes 1.18 billion log lines from a single customer
- 575K+ CI jobs weekly
- ClickHouse for log ingestion at 35:1 compression with millisecond query latency
- Multi-model tier allocation: Opus for root-cause analysis, Sonnet for evidence gathering, Haiku for constrained log parsing

## Why clawfit should care

clawfit's recommendation engine currently treats the harness as an undifferentiated "orchestration" concern. The Mendral pattern makes the harness topology a first-class variable with direct consequences for the other axes clawfit scores on:

- **Latency**: sandbox suspend/resume (25ms) vs. cold boot (125ms) is directly affected by whether the loop lives inside or outside; recommending an inside-loop harness for a use case that involves long LLM wait times incurs unnecessary compute cost
- **Statefulness**: the loop-outside design makes multi-session statefulness a database property, not a sandbox property — relevant to clawfit's `statefulness: session` vs `persistent` axis
- **Cost**: idle sandbox suspension only works with an external loop; harnesses that bundle loop and sandbox together pay for idle compute that an outside-loop architecture would not
- **Security posture**: credential isolation is not currently a clawfit scoring dimension; if an `isolation_model` axis is added (as flagged in the NVIDIA OpenShell note on 2026-04-28), the loop-outside pattern would be the high-isolation archetype

The Freestyle signal (tracked 2026-04-24) and OpenAI Agents SDK sandbox update (2026-04-16) both push in the same direction — the harness/sandbox split is not Mendral-specific, it is becoming the production-standard architecture for cloud-side agent execution. Mendral's post is the most explicit named articulation of the pattern to date.

## Preliminary interpretation

Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layers** (primary): the post is an L2 harness architecture opinion, with Inngest as the durable-execution substrate and Blaxel as the compute substrate
- **Level 7 — Infrastructure / hardware / edge** (secondary, Blaxel): the ephemeral microVM/sandbox lifecycle is an L7 execution substrate; Blaxel would be the L7 entry, not Mendral itself
- **Level 5 — Memory / MCP / context layer** (adjacent): the `/skills/*` and `/memory/*` → Postgres routing pattern is a context-persistence mechanism that sits at L5 in function, even though Mendral implements it at the filesystem layer rather than via MCP

No registry entry warranted today (Mendral is a product, not an agent/LLM/hardware schema entry). If an `isolation_model` scoring dimension is added to clawfit, this post becomes a primary reference for the `harness_external` archetype.

Map entry warranted: yes, as an L2 architecture reference (not a product listing). The loop-outside-sandbox pattern deserves a named entry in `docs/reference-levels.md` L2 section as a harness topology archetype alongside the existing Anthropic sprint-contracts and Hashline references — flagging here rather than editing the map.

## Status
- Tracking. L2 architecture reference only; no registry entry. Flag for `docs/reference-levels.md` L2 update if a second independent source (not Blaxel marketing) validates the Inngest step-checkpoint durability claim in production. Watch whether "harness-outside-sandbox" becomes named vocabulary in the ecosystem the way "sprint contract" did.
