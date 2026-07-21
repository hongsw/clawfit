# Research Watch: Nativ — Apple Silicon Local LLM Runner

- Repo/Link: https://github.com/blaizzy/nativ / https://blaizzy.github.io/nativ/
- Source: Hacker News (154 points, front page 2026-07-21)

## Why this is worth watching
Nativ is a polished macOS-native (SwiftUI + embedded Python) app for running MLX models locally on Apple Silicon, exposing OpenAI- and Anthropic-compatible API endpoints at `localhost:8080`. Unlike Ollama (Linux-first, CLI-centric), Nativ is Mac-only and UI-first, targeting developers who want a GUI model manager that also acts as a local inference server for Claude Code or any OpenAI-compatible agent harness.

## What stands out immediately
- **OpenAI + Anthropic API endpoints** — drop-in local replacement for cloud API calls from agent harnesses
- **MLX-VLM backend** — multimodal (text, images, video, code, audio) via Apple Silicon Metal
- **Live performance telemetry** — tokens/second, memory usage, thermal state in a SwiftUI dashboard
- **Model library** — discovers HuggingFace-cached MLX models; curated selection including vision models
- **MIT license**, 167 GitHub stars at time of observation (very recently launched)
- macOS 26+ requirement (bleeding-edge OS)

## Why clawfit should care
Nativ fills a gap in the local hardware + runner matrix: Apple Silicon users who want a GUI-managed local inference server compatible with agentic harnesses (Claude Code, Cursor, etc.). Relevant to the `hardware: local-mac` × `network: offline` × `budget: low` recommendation path. Also signals the growing appetite for Anthropic-API-compatible local endpoints as a privacy-first alternative to cloud.

## Preliminary interpretation
Current best reading:
- **Level 1 — Local Inference Runtime** (primary: runs the model on-device via MLX)
- **Level 6 — User Interface / App Layer** (secondary: native Mac GUI for model management and chat)

Closest comparables: LM Studio (Electron, broader hardware support), Ollama (CLI-first, Linux-primary), ATLAS (tracked, offline coding agent). Nativ is the most polished Apple-native option seen so far.

## Status
- First signal. 154 HN points signals developer awareness. Stars low (167) but very fresh launch.
- Monitor for: star growth, model library expansion, official Claude Code MCP integration
- Registry candidate if a second independent signal confirms adoption
