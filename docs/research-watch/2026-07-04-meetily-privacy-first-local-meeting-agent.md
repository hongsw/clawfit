# Research Watch: Meetily — Privacy-First Local AI Meeting Assistant

- Repo: https://github.com/Zackriya-Solutions/meetily (⭐14,895)
- Source: GitHub Trending (all languages, +865 today, 2026-07-04)

## Why this is worth watching

Meetily claims to be the #1 self-hosted open-source AI meeting note-taker for macOS and Windows — 100% local processing, no cloud. The architectural claim is worth unpacking: transcription (Parakeet/Whisper), speaker diarization (SortFormer), and summarization (Ollama) are all running on-device. "4x faster" transcription refers to Parakeet versus Whisper on CPU; this is a quantified performance claim rather than a marketing slogan. At 14,895 stars and 1,640 forks, the repo has passed community adoption levels that suggest it solves a real deployment need. The "no cloud" constraint is not just a privacy posture — it is an architectural filter that puts Meetily in the same deployment profile as coding agents that operate air-gapped or in restricted enterprise environments.

## What stands out immediately

- **Fully local inference stack:** Parakeet (NVIDIA NeMo) or Whisper for transcription, SortFormer for speaker diarization, Ollama for LLM summarization — no API call leaves the machine
- **4x Parakeet speed claim:** Specific hardware benchmark (versus Whisper on CPU); testable, not vague
- **Rust backend:** Rust-native transcription pipeline is consistent with the low-latency, local-first positioning; not a Python wrapper around subprocess calls
- **Speaker diarization shipped in-box:** Distinguishes who said what — a meaningful capability gap in many self-hosted transcription tools, which typically offer only raw transcription
- **macOS + Windows coverage:** Both desktop platforms, no Linux native client; constrains deployment environments
- **No cloud dependency in normal operation:** Privacy boundary is architectural (no outbound API calls) rather than policy-based (terms of service promise)
- **14,895★, 1,640 forks:** Community adoption suggests real-world deployment, not only experimental usage
- **Created Dec 2024:** 18 months of development; last pushed June 2026; active maintenance but not rapid-release cadence

## Why clawfit should care

Meetily is the first high-star local AI meeting agent in this scan series. It does not fit any current clawfit task type (`qa`, `code-gen`, `research`, `vibe-coding`) — the implicit task is `meeting-assistance`, a completely different workflow category. The fully-local constraint means it maps naturally to `hardware: local`, `network: offline`, `statefulness: stateful` (each meeting session is stateful), and a cost profile of $0 per-session API cost. This is notable because:

1. clawfit's current scoring was designed for code-focused agents; Meetily is the strongest signal so far for a `task: meeting-notes` or `task: audio-transcription` axis.
2. The local inference stack (Whisper + Ollama) is shared infrastructure with several tracked L1 runtimes; Meetily demonstrates that local inference reaches task verticals beyond code generation.
3. 14,895★ is above the 5k registry threshold, but the current schema has no `task` field value that maps to this use case — registry addition requires a schema extension decision first.

## Preliminary interpretation

Current best reading:
- **Level 1 primary — Base agent runtime** (local inference loop: STT → LLM summarization → structured output; fully self-contained execution)
- **Level 6 secondary — Human interface layer** (meeting context as the human-facing interaction surface; audio and speaker diarization as modality inputs)
- Not L4: no skills, MCP tools, or plugin surface; the capability is built into the application, not exposed as a reusable layer

## Claims to verify

- "No cloud required" — confirm no telemetry, crash reporting, or phonehome in the Rust binary
- "4x faster" Parakeet claim — on what hardware? CPU only, or GPU-accelerated baseline?
- SortFormer accuracy at speaker overlap — claimed feature, no accuracy metric cited
- Whether the Ollama summarization step is configurable (model choice, prompt template)
- Actual memory footprint with all three components running simultaneously

## Status

- 14,895★ above registry threshold; task type not in current schema → registry hold pending `meeting-notes` or `audio` task type addition
- First signal for "local meeting AI agent" as a clawfit task vertical
- Promotion criterion: clawfit schema gains a `meeting-notes` or `audio-transcription` task type AND deterministic latency data is available on commodity hardware
