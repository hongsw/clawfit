# Research Watch: Apple Foundation Models Framework

- Repo/Link: https://developer.apple.com/foundation-models-framework/
- Source: GeekNews

## Why this is worth watching
Apple's Foundation Models Framework is a Swift API that unifies Apple's on-device Private Cloud Compute models with external providers (Claude, Gemini) under a single interface. For the first time, iOS/macOS developers can write one AI call and let the framework decide whether to run locally, in Apple's private cloud, or via a third-party model — with a declared privacy posture for each path. This is the highest-authority "local vs. cloud" unification signal to date for the Apple developer ecosystem.

## What stands out immediately
- Single Swift API spans on-device, Private Cloud Compute, and Claude/Gemini
- Privacy posture declared per call — framework routes accordingly
- No separate SDK installation; ships with Xcode and system frameworks
- Directly addresses the local vs. cloud execution dimension clawfit tracks

## Why clawfit should care
The on-device/cloud execution dimension in clawfit's `network` field (online/offline/hybrid) is now a first-class API concern for Apple platform developers. Tools built on this framework should be classified as `network: "hybrid"` with `offline` capability when running on Apple silicon. The framework also materializes the "edge execution" tier that clawfit's L1-L7 taxonomy sketches but rarely sees as a production API.

## Preliminary interpretation
Current best reading:
- **Level 4c — Context/Capability Infrastructure** (execution routing layer under agent frameworks)

## Status
- Tracking — Shipped with Xcode; watch for third-party adoption and Claude/Gemini on-device quota details
