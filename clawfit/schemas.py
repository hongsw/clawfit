"""Data classes for registry entries and recommendations."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Agent:
    id: str
    name: str
    description: str
    tasks: List[str]                # supported task categories
    latency: str                    # "low", "medium", "high"
    statefulness: str               # "stateless", "session", "persistent"
    network: str                    # "online", "offline", "hybrid"
    preferred_llms: List[str] = field(default_factory=list)
    # User maturity targeting (1–11, from ai-maturity-diagnosis)
    maturity_min: int = 1           # minimum recommended user maturity stage
    maturity_max: int = 11          # maximum recommended user maturity stage
    maturity_optimal: int = 6       # ideal user maturity stage


@dataclass
class LLM:
    id: str
    name: str
    provider: str
    tasks: List[str]
    latency: str
    cost_per_1k_tokens: float
    context_window: int
    network: str                    # "online", "offline"


@dataclass
class Hardware:
    id: str
    name: str
    type: str                       # "cloud", "edge", "on-prem"
    gpu: bool
    ram_gb: int
    cost_per_hour: float
    latency: str


@dataclass
class Recommendation:
    agent: str
    llm: str
    hardware: str
    architecture: str
    fit_score: float
    why: List[str]
    risk: List[str]
    maturity_note: str = ""         # guidance based on user maturity stage
