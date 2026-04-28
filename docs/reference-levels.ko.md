# clawfit 참조 레벨 v0.3 (한국어)

> 영문 원본: [`reference-levels.md`](reference-levels.md)

이 문서는 clawfit이 비교하고, 학습하고, 참조해야 할 외부 도구와 프로젝트를 분류합니다.

## 이 문서의 역할

clawfit의 **정식 에코시스템 맵**입니다.

다음 질문에 답합니다:
- 이 레포/제품/프로젝트는 어떤 종류인가?
- 생태계의 어느 레이어에 속하는가?
- 어떤 인접 시스템과 비교해야 하는가?

채택/성숙도 사다리가 아니며, 원시 발견 로그도 아닙니다.

---

### 2026-04 신규 패턴 (v0.3)

- **기관 하네스 진입:** LangChain/LangGraph가 `deepagents`로 L2에 직접 진입 — 독점 코딩 어시스턴트의 오픈소스 대항마로 포지셔닝
- **메모리 레이어 제품화:** `claude-mem` (45k★)이 L4 메모리 도구가 메인스트림 플러그인으로 진입했음을 증명
- **스킬 레이어 성숙:** L4가 스킬 매니저(생명주기 도구), 도메인 스킬팩, 툴-사용 확장으로 분화. `Chops`, `skills-cleaner`, `Impeccable`, `K-Skill`, `Expect`가 동시 신호
- **Git-native 에이전트 표준:** `gitagent`가 Git을 에이전트 정의 배포/버전관리 레이어로 제안 — 플러그인 레지스트리와 구별되는 L3 SSOT 패턴
- **집단 메모리 패턴:** Mozilla AI의 `cq`가 멀티에이전트 공유 지식 커먼스를 도입 — L5에서 이전에 없던 서브타입
- **Anthropic 정식 하네스 패턴:** 장기 실행 앱 하네스 설계 아티클 (듀얼에이전트, 스프린트 계약, 컨텍스트 리셋) — L2 아키텍처 레퍼런스
- **Agentic AI Foundation 거버넌스 전환:** MCP가 Linux Foundation 컨소시엄에 기증 (Microsoft + Google + OpenAI + Anthropic). 월 9,700만 다운로드. AGENTS.md(OpenAI)가 CLAUDE.md와 함께하는 크로스 플랫폼 SSOT 스펙으로 등장
- **하네스 신뢰성이 새 평가 축:** `oh-my-pi` Hashline 접근법과 Anthropic 스프린트-계약 모두 동일한 문제(장기 세션에서 에이전트 워크플로 일관성)에 대한 응답
- **스킬 마켓플레이스 제도화:** claudemarketplaces.com (150개+ 평점 스킬) + 단일 Anthropic 스킬 277k 설치 — 스킬 배포가 앱스토어 규모에 도달
- **컴퓨터 사용이 L1/L7 경계를 무너뜨림:** Claude 컴퓨터 사용(퍼스트파티)과 understudy(시연 기반) 모두 데스크탑 전체를 조작 — L7 정의를 컴퓨터 사용 에이전트로 확장 필요

---

## Level 1 — 기본 런타임 / 주요 에이전트 서페이스

사용자가 기본 환경으로 가장 직접적으로 선택하는 도구들.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [OpenClaw](https://github.com/openclaw/openclaw) | ⭐ 365,342 | 대규모 오픈소스 에이전트 런타임 |
| [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | ⭐ 30,697 | |
| [Claude Code](https://github.com/anthropics/claude-code) | ⭐ 118,485 | Anthropic 공식 CLI |
| [OpenCode](https://github.com/anomalyco/opencode) | ⭐ 150,654 | |
| [Goose](https://github.com/block/goose) | ⭐ 43,404 | Block의 오픈소스 에이전트 |
| [Crush](https://github.com/charmbracelet/crush) | ⭐ 23,571 | |
| [Aider](https://github.com/paul-gauthier/aider) | ⭐ 44,022 | Git-aware 코딩 에이전트 |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | ⭐ 72,201 | |
| [Cline](https://github.com/cline/cline) | ⭐ 61,063 | VS Code 에이전트 |
| [Continue](https://github.com/continuedev/continue) | ⭐ 32,841 | |
| Cursor | — | https://cursor.com/ |
| Kiro CLI | — | https://kiro.dev/ |
| [deepagents](https://github.com/langchain-ai/deepagents) | ⭐ 21,878 | LangGraph 기반 하네스 *(L2 중복)* |
| [understudy](https://github.com/understudy-ai/understudy) | ⭐ 422 | 시연으로 배우는 로컬 데스크탑 에이전트 |
| Claude Computer Use | — | 퍼스트파티 데스크탑 제어 *(L7 중복)* |

---

## Level 2 — 메타 래퍼 / 하네스 / 오케스트레이션 레이어

기존 기본 에이전트 위에 올라가 작동 방식을 변환하는 프로젝트들.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | ⭐ 54,537 | 에이전트 하네스 / 메타 래퍼 |
| [oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) | ⭐ 31,602 | Claude Code 멀티에이전트 오케스트레이션 |
| [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | ⭐ 26,371 | Codex 확장 / 훅 / HUD / 에이전트 팀 |
| [oh-my-gemini-cli](https://github.com/Joonghyun-Lee-Frieren/oh-my-gemini-cli) | ⭐ 155 | Gemini CLI 워크플로우 팩 |
| [oh-my-agent](https://github.com/first-fluke/oh-my-agent) | ⭐ 856 | 다중 런타임 에이전트 하네스 |
| [Aperant](https://github.com/AndyMik90/Aperant) | ⭐ 14,093 | |
| [ralph-claude-code](https://github.com/frankbria/ralph-claude-code) | ⭐ 8,878 | |
| [open-ralph-wiggum](https://github.com/Th0rgal/open-ralph-wiggum) | ⭐ 1,584 | |
| [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) | ⭐ 22,511 | Claude 워크플로우 프레임워크 |
| [claudecodeui](https://github.com/siteboon/claudecodeui) | ⭐ 10,291 | |
| [agentapi](https://github.com/coder/agentapi) | ⭐ 1,372 | |
| [claude-code-router](https://github.com/musistudio/claude-code-router) | ⭐ 33,100 | Claude Code 라우팅 래퍼 |
| [deepagents](https://github.com/langchain-ai/deepagents) | ⭐ 21,878 | LangGraph SDK *(L1 중복)* |
| [oh-my-pi](https://github.com/can1357/oh-my-pi) | ⭐ 3,541 | Hashline: 동시 멀티에이전트 파일 안전성 해시 검증 |
| [Anthropic 하네스 설계](https://www.anthropic.com/engineering/harness-design-long-running-apps) | — | 정식 듀얼에이전트 + 스프린트-계약 아키텍처 |
| [ouroboros](https://github.com/Q00/ouroboros) | ⭐ 2,761 | "Agent OS: stop prompting, start specifying" — Claude Code/Codex/OpenCode/Hermes 위에 올라가는 spec-driven 하네스; Double-Diamond 워크플로우 + 9개 전문 에이전트 + Ralph evolutionary loop + PAL cost-tier router + EventStore; ralph-family 동족 |

---

## Level 3 — 팀 하네스 / 실행 가능 SSOT / 거버넌스 레이어

LLM 사용이 개인 습관에서 팀 운영 시스템으로 전환되는 레벨.

핵심 개념 — **실행 가능 SSOT(단일 진실 공급원)**:
- 사람은 워크플로우 또는 운영 가이드로 읽고,
- 에이전트는 실행 가능한 지시로 읽는다.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [Toss 하네스 아티클](https://toss.tech/article/harness-for-team-productivity) | — | 팀 생산성 바닥을 높이는 하네스 |
| [oh-my-agent](https://github.com/first-fluke/oh-my-agent) | ⭐ 856 | |
| [everything-claude-code](https://github.com/affaan-m/everything-claude-code) | ⭐ 168,366 | 스킬/규칙/에이전트 하네스 최적화 시스템 |
| [cc-sdd](https://github.com/gotalab/cc-sdd) | ⭐ 3,217 | 스펙 기반 개발 워크플로우 |
| [gitagent](https://github.com/open-gitagent/gitagent) | ⭐ 2,545 | Git-native 에이전트 정의 오픈 표준 |
| **AGENTS.md** | — | OpenAI의 크로스 플랫폼 에이전트 스펙. Agentic AI Foundation 소속. CLAUDE.md와 경쟁/보완 관계 |
| [DureClaw](https://github.com/DureClaw/dureclaw) | ⭐ 2 | *(주 분류 Level 2)* — 크로스 머신 multi-agent team coordinator; Phoenix WebSocket 메시지 버스 + oah-agent 워커가 Mac/Linux/Windows/Raspberry Pi에 걸친 multi-machine SSOT 패턴 구현 |

---

## Level 4 — 기능 확장 레이어 (MCP / 메모리 / 플러그인 / 도구)

기본 런타임을 대체하지 않고 기능을 추가하는 시스템들.

Level 4는 세 가지 서브타입으로 분화 중:

### 4a. 메모리 / 영구 컨텍스트

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [claude-mem](https://github.com/thedotmack/claude-mem) | ⭐ 68,547 🔥 | 훅 기반 영구 메모리 (SQLite + Chroma). `npx claude-mem install` |
| [OpenMemory](https://github.com/CaviraOSS/OpenMemory) | ⭐ 4,029 | |
| [cipher](https://github.com/campfirein/cipher) | ⭐ 4,657 | |
| [claude-context](https://github.com/zilliztech/claude-context) | ⭐ 9,859 | |
| [Engram](https://github.com/Gentleman-Programming/engram) | ⭐ 2,912 | Go 바이너리 영구 메모리; 17개 MCP 툴 + What/Why/Where/Learned 스키마 + session lifecycle 훅; SQLite+FTS5; Beads(런타임-레이어)와 인터페이스 축에서 분기되는 protocol-endpoint 설계 *(L5 inspectable agent memory 서브패턴 동시)* |
| [wuphf](https://github.com/nex-crm/wuphf) | — | Karpathy 스타일 LLM wiki를 에이전트가 Markdown+Git으로 유지; multi-agent 공유 workspace에 notebook→wiki promotion + lint 게이트; human-inspectable agent-maintained memory; vector-DB 비의존 트랙 (Beads/Engram/GBrain 동족) *(L5 inspectable agent memory 서브패턴 동시)* |

### 4b. 스킬 팩 & 스킬 매니저

**스킬 매니저 (생명주기/디스커버리):**

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [Chops](https://github.com/Shpigford/chops) | ⭐ 1,167 | macOS 스킬 매니저. Claude Code, Cursor, Codex, Windsurf, Amp 동시 지원 |
| [skills-cleaner](https://github.com/amebahead/skills-cleaner) | ⭐ 13 | `.claude/plugin/` 스킬 목록 조회/중복 제거 |
| [claudemarketplaces.com](https://claudemarketplaces.com/) | — | 150개+ 평점 스킬 마켓플레이스 (2026-03) |
| [claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) | ⭐ 1,851 | 340 플러그인 + 1,367 에이전트 스킬 카탈로그 |

**플랫폼 네이티브 플러그인 시스템:**

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| OpenAI Codex 플러그인 | — | Skills + Apps + MCP 번들. GitHub, Linear, Vercel, Slack, Figma, Notion, Gmail 공식 플러그인 |
| [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | ⭐ 18,040 | Anthropic 공식 플러그인 |

**도메인 스킬 팩:**

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [Impeccable](https://github.com/pbakaus/impeccable) | ⭐ 16,060 | 7개 도메인 20개 디자인 명령어 (레이아웃, 간격, 색상, 타이포그래피…) |
| [K-Skill](https://github.com/NomaDamas/k-skill) | ⭐ 1,514 | 한국어 서비스 스킬팩 (SRT, 서울 지하철, KBO, 로또) |
| [plugins-for-claude-natives](https://github.com/team-attention/plugins-for-claude-natives) | ⭐ 748 | |

### 4c. 툴-사용 / 액션 인프라

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [Expect](https://github.com/millionco/expect) | ⭐ 3,062 | 코드 변경으로부터 브라우저 기반 테스트 플랜 자동 생성 실행 |
| [serena](https://github.com/oraios/serena) | ⭐ 23,498 | 코딩 에이전트용 시맨틱 검색/편집 툴킷 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | ⭐ 84,644 | MCP 서버 에코시스템. 2025-12 Agentic AI Foundation에 기증 |
| [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | ⭐ 15,963 | Microsoft MCP 교육 커리큘럼 |
| [mcp-context-forge](https://github.com/IBM/mcp-context-forge) | ⭐ 3,620 | IBM AI 게이트웨이 + MCP 프록시 |
| [Composio](https://github.com/ComposioHQ/composio) | ⭐ 27,933 | 에이전트용 대형 툴-액세스 플랫폼 |
| [Pica](https://github.com/withoneai/pica) | ⭐ 1,476 | 에이전트 도구 플랫폼 (Rust) |

---

## Level 5 — 리서치 / 평가 / 벤치마크 / 자율연구 패턴

평가 하네스, 벤치마크 참조, 자율 리서치 루프, **집단 에이전트 지식 시스템**.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [cq](https://blog.mozilla.ai/cq-stack-overflow-for-agents/) | — | Mozilla AI 에이전트 공유 지식 커먼스. "에이전트를 위한 Stack Overflow" |
| [autoresearch](https://github.com/karpathy/autoresearch) | ⭐ 77,236 | |
| [any-agent](https://github.com/mozilla-ai/any-agent) | ⭐ 1,156 | 멀티에이전트 프레임워크 인터페이스 |
| [any-llm](https://github.com/mozilla-ai/any-llm) | ⭐ 1,926 | 통합 LLM 제공자 인터페이스 |
| [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | ⭐ 12,342 | 언어 모델 평가 프레임워크 |
| [agent-lightning](https://github.com/microsoft/agent-lightning) | ⭐ 17,042 | Microsoft AI 에이전트 훈련 프레임워크 |
| [Ko-AgentBench](https://github.com/Hugging-Face-KREW/Ko-AgentBench) | ⭐ 64 | 한국어 에이전트 벤치마크 |

---

## Level 6 — 데이터 / 증거 / 지식 인프라

에이전트가 외부 지식에 어떻게 접근하고 구조화하는지.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [LightRAG](https://github.com/HKUDS/LightRAG) | ⭐ 34,415 | |
| [RAG-Anything](https://github.com/HKUDS/RAG-Anything) | ⭐ 19,033 | |
| [airweave](https://github.com/airweave-ai/airweave) | ⭐ 6,266 | |
| [PageIndex](https://github.com/VectifyAI/PageIndex) | ⭐ 25,871 | |
| [MinerU](https://github.com/opendatalab/MinerU) | ⭐ 61,356 | |

---

## Level 7 — 휴먼 인터페이스 / 음성 / 컴퓨터 사용 레이어

음성 입력, 토크 모드, 원격 릴레이, 데스크탑 제어 등 인간이 에이전트를 실제로 조작하는 방식.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [deep-agents-ui](https://github.com/langchain-ai/deep-agents-ui) | ⭐ 1,577 | deepagents용 Next.js 웹 UI (채팅 + 파일 모니터 + 단계별 디버그) |
| Claude 컴퓨터 사용 | — | Anthropic 퍼스트파티 데스크탑 제어 (마우스+키보드+화면) *(L1 중복)* |
| [Ghostmeet](https://github.com/Higangssh/ghostmeet) | ⭐ 37 | 셀프호스팅 AI 미팅 비서 (Whisper 실시간 전사 + Claude 요약) |
| Superwhisper | — | https://superwhisper.com/ |

---

## 관련 문서

- 영문 에코시스템 맵: [`reference-levels.md`](reference-levels.md)
- research-watch 문서들: [`research-watch/`](research-watch/)
- 에코시스템 개요: [`pages/ecosystem-overview.md`](pages/ecosystem-overview.md)
- 한국어 README: [`../README.ko.md`](../README.ko.md)
