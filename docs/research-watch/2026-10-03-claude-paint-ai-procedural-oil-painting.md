# Research Watch: claude-paint / stillwet.art — AI Procedural Oil Painting via Code Execution

- Repo: https://github.com/aliceisjustplaying/claude-paint (⭐76 — HN signal primary)
- Source: Hacker News front page (352 pts, Show HN, October 3, 2026)

## Why this is worth watching

stillwet.art is a running experiment that asks language models to paint physical-simulation oil paintings by writing code — specifically Rust programs targeting a physics-accurate paint engine (Kubelka–Munk pigment optics, bristle simulation, drying physics). No image generation model is used; every brushstroke is a code instruction that executes in a deterministic paint physics simulator. The project has run 21+ rounds of Claude Opus 5.5 painting sessions alongside GPT-6, Gemini, and DeepSeek variants. The 352 HN points signal is significant not because the star count is high (76 is below threshold) but because it surfaced substantive technical discussion about what it demonstrates: that language models trained on text descriptions of paintings independently converge on similar compositional structures when given a generative code medium — a finding about language model implicit visual knowledge that is distinct from diffusion model image generation. The GitHub star count is cited for completeness; the primary signal here is the HN coverage.

## What stands out immediately

- **Code-as-painting-medium**: agents do not call an image generation API — they write programs that control simulated brush physics; the rendering is deterministic, not sampled; this distinguishes the output from DALL-E/Midjourney/FLUX artifacts
- **Kubelka–Munk pigment optics**: physically-based paint mixing model that determines how colors interact on a simulated canvas; this is real optical physics, not a stylistic approximation; it means agents must reason about paint behavior rather than just specifying colors
- **Iterative easel loop**: some sessions show agents "stepping back" between painting passes to evaluate composition before continuing — a form of visual self-evaluation loop without pixel inspection (the agent evaluates its own code output, not an image rendering)
- **Cross-model convergence**: multiple different model families independently generate similar compositional motifs when given identical Friedrich-corpus prompts — the recurrence is too consistent to be coincidence; suggests shared implicit visual knowledge embedded in LLM training data
- **Replayable session logs**: every painting session is logged as a replayable code trace; the project has a research artifact quality that studio demos typically lack
- **Physics-accurate Rust engine in a separate crate**: the paint engine is a standalone Rust library (`crates/paint`) with published API; the "easel" is the agent interface; separation of concerns makes the engine independently reusable for other agent painting experiments
- **MIT license**: no restrictions on reuse or extension

## Why clawfit should care

clawfit's L6 (human interface) taxonomy currently covers text-to-UI systems, coding agents, and TUI/CLI interfaces. stillwet.art represents a distinct L6 sub-type: **generative creative output through procedural code execution** — where the agent's output is not text, UI, or working code but sensory artifacts (paintings) produced by deterministic simulation. This is distinct from image generation models (diffusion sampling) and from code generation tools (functional correctness is not the goal). The practical ecosystem implication is narrow but real: creative workflow agents that produce visual outputs through code simulation rather than generation models bypass image generation costs and diffusion artifacts while gaining full reproducibility. The cross-model convergence finding also has a research implication for clawfit's evaluation framework: LLM implicit knowledge about visual structure may be testable through code output rather than through direct visual generation.

## Preliminary interpretation

Current best reading:
- **Level 6 — Human Interface / Generative Creative Output** (primary)
- Secondary: L4 (the paint engine as an MCP-connectable simulation substrate, once formalized)

The project is currently closer to a research demonstration than a production ecosystem tool. However, the technical depth (Rust engine, replayable logs, multi-model comparison) distinguishes it from prior art in "AI draws pictures" demos.

## Claims to verify

- Whether the cross-model compositional convergence has been analyzed rigorously (sample size, control for prompt-driven guidance vs. emergent structure)
- Whether the Rust paint engine has an MCP server or HTTP API that would make it callable from agent harnesses
- Whether the iterative self-evaluation loop is harness-enforced or model-initiated (the distinction matters for whether this is an agent loop skill or a prompting artifact)
- GPU/hardware requirements for running the paint engine at real-time or near-real-time speeds for interactive agent sessions

## Status

- NOT in clawfit registry: creative simulation tool; no inference cost profile applicable to the paint engine
- GitHub: 76 stars (below 100-star threshold; signal is HN-sourced at 352 points)
- First tracked signal for "AI procedural visual art generation through physical paint simulation code"
- Monitoring for paint engine MCP integration and multi-model convergence research writeups
