# Research Watch: Swiftlet — MoE Weight-Streaming Inference on iOS and Mac

- Repo: https://github.com/leonickson1/Swiftlet (⭐317)
- Source: Hacker News Show HN (285 points, 2026-08-04)

## Why this is worth watching

Swiftlet runs 80B-parameter Qwen models in 4.3 GB of RAM on a Mac, and 35B models on an iPhone 17. The mechanism is MoE expert weight streaming from SSD — only the dense "resident" weights (attention, routers, shared experts, embeddings) stay in RAM; activated expert weights are read on-demand via `pread` calls from fixed-stride storage containers.

This is the third independent implementation of the same architectural pattern in the corpus within 7 days: turbo-fieldfare (2026-07-29, Gemma 4 26B on Apple Silicon SSD, HN 326 pts), WASTE (2026-08-01, Kimi K3 2.78T on NVMe, HN 305 pts), and now Swiftlet (Qwen 80B on Apple SSD/NVMe + Qwen 35B on iPhone). Three independent implementations, three different codebases, across two architectures (Apple Silicon + x86) and now two device classes (laptop + phone). The pattern is no longer experimental.

The iOS dimension is distinct from prior signals: turbo-fieldfare and WASTE target macOS/x86 desktops. Swiftlet extends SSD-streamed MoE inference to iOS 17+ — the first runtime in the corpus that makes 35B-class model execution viable on a phone without cloud API calls.

## What stands out immediately

- **80B Qwen in 4.3 GB RAM on Mac:** keeps only dense weights resident; activated MoE experts loaded on-demand from SSD — steady-state memory is proportional to dense core, not full parameter count
- **35B Qwen on iPhone 17 at ~1 tok/s:** production iOS deployment via the bundled "Priv AI" app on the App Store; not a proof-of-concept — the inference path is shipping to users
- **Benchmarks from the repo:** 4.5–5 tok/s for 80B on Mac; 7–11 tok/s for 35B on Mac; ~1 tok/s on iPhone 17 — numbers specific enough to cross-check against hardware specs
- **Swift + Metal implementation:** Apple-native; `pread` for storage access bypasses OS page cache eviction issues that plague general-purpose streaming approaches
- **OpenAI-compatible API server:** 80B Qwen exposed as a local endpoint — drop-in replacement for cloud API in offline agent configurations
- **Apache 2.0 license:** commercially deployable
- **285 HN points on Show HN:** strong community signal well above noise floor for a 317-star repo — suggests practitioner interest disproportionate to current star count

## Why clawfit should care

The `network: offline + hardware: local` filter currently resolves to Apple Silicon entries in hardware.json. Swiftlet changes the scope of what "local" means for those filter combinations:

1. **Laptop-class inference floor drops to 80B parameters:** prior to this pattern (turbo-fieldfare, WASTE, Swiftlet), recommending 80B+ models on local hardware required high-VRAM desktop setups. SSD-streaming changes the RAM requirement from "≥80 GB" to "≥4.3 GB + sufficient SSD" — most modern laptops qualify
2. **iOS as an agent hardware tier:** clawfit's hardware registry covers desktop (Apple Silicon, RTX Spark, DGX Spark) and cloud. Swiftlet's iPhone 17 deployment introduces mobile-Apple-Silicon as a new tier, distinct from mobile-GPU-Android (Nightcrawler, 2026-08-03)
3. **Three-signal confirmation:** SSD-streamed MoE inference is now the most-confirmed new hardware pattern in the corpus (turbo-fieldfare July 29 + WASTE August 1 + Swiftlet August 4). Three cross-day signals from independent implementations confirm the pattern is real and reproducible

Schema gap: `inference_strategy: ssd-streamed` (first flagged 2026-07-29, now confirmed by third independent implementation); `hardware: mobile-apple-silicon` (distinct from `hardware: mobile-gpu` flagged for Android 2026-08-03); `ios_compatible: bool`.

## Preliminary interpretation

- **Level 7 — Infrastructure / hardware** (primary: extends viable local inference hardware to Apple Silicon + iOS tiers)
- Secondary: **Level 1 — Base runtime** (OpenAI-compatible API server makes it a deployable offline agent backend)
- Cross-watch: turbo-fieldfare (2026-07-29) — same SSD-streaming pattern, Gemma 4 on Mac; WASTE (2026-08-01) — same pattern, Kimi K3 on x86/NVMe; Nightcrawler (2026-08-03) — on-device mobile inference on Android (different pattern: full model in phone GPU rather than SSD-streamed)

## Claims to verify

- **4.3 GB RAM for 80B:** verify via repo benchmarks and independent testing; the number is specific and reproducible but depends on quantization level (4-bit reported) and model variant
- **iPhone 17 at ~1 tok/s:** Priv AI app exists on App Store; verify model is running fully on-device vs. offloading parts to server
- **Qwen3-Next-80B-A3B model:** verify this model exists under this exact name on Hugging Face; "Next" naming suggests a variant not yet in the main Qwen3 release
- **pread vs. mmap:** the repo uses `pread` for explicit streaming — verify this is genuinely faster than mmap-based approaches for MoE expert loading patterns on Apple storage

## Status

- Third signal for SSD-streamed MoE inference pattern (cross-day: turbo-fieldfare July 29 + WASTE August 1 + Swiftlet August 4)
- First signal for iOS 17+ agent inference runtime
- 317 stars above threshold; HN 285 pts is the stronger signal
- No registry entry: hardware tier (mobile-apple-silicon) not modeled; throughput too hardware-generation-specific for deterministic `hardware.json` value
- Schema watch: `inference_strategy: ssd-streamed` (now third-confirmed); `hardware: mobile-apple-silicon`; `ios_compatible: bool`
- Three-signal note: `inference_strategy: ssd-streamed` has now accumulated three independent cross-day confirmations — strongest candidate for schema formalization in the next review cycle
