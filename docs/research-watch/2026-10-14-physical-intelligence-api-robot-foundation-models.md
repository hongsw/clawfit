# Research Watch: Physical Intelligence API Beta — Robot Foundation Models

- Repo/Link: https://www.pi.website/blog/api-beta
- Source: Hacker News

## Why this is worth watching
Physical Intelligence (π) opened an API beta giving developers access to frontier robot foundation models — the first time a general-purpose robot model is available as a hosted inference endpoint. This represents a new hardware+agent category that sits outside clawfit's current cloud/local/edge taxonomy: embodied agents running on physical hardware.

## What stands out immediately
- REST API for robot control models (trained across diverse robot morphologies)
- Models generalize across robot types, not robot-specific fine-tunes
- Beta access implies production readiness is near
- Puts robot AI on the same API-access curve as LLMs

## Why clawfit should care
clawfit's hardware registry covers cloud, laptop, edge, and mobile but not physical/robotic execution. If Physical Intelligence's API matures, "robot" becomes a valid hardware target for multi-agent systems. The org_fit taxonomy should account for orgs in manufacturing, logistics, or research that operate physical agents alongside software ones.

## Preliminary interpretation
Current best reading:
- **Level 1 — Hardware / Execution Environment**: physical robotic hardware as a new execution substrate for agent workloads.

## Status
- Tracking; flag for hardware registry expansion in a future release
