# clawfit 참조 레벨 v0.4 (한국어)

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

### 2026-05 신규 패턴 (v0.4)

- **L6 분류 분리 — L6a / L6b 공식 확정:** L6가 두 개의 서브레이어로 분리됨. L6a = 검색-네이티브 (임베드 → 인덱스 → 검색 → 주입; LLM은 소비자). L6b = LLM-네이티브 KB (LLM이 지식 저장소를 직접 유지; 검색 파이프라인 없음). 카파시 LLM Wiki 기스트(2026-04-04) 기준. wuphf (L4a 기본, L6b 부차) 첫 확인 구현체.
- **조작적 정의 추가 (L4a vs L6b 경계):** 쓰기 주체로 구분 — LLM이 쓰면 L6b, 파이프라인/사람이 쓰면 L6a. 두 역할을 모두 지원하면 primary 역할로 분류하고 cross-reference 표기.

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

### 2026-05-03 신규 신호
- **Mendral — "하네스는 샌드박스 외부에" (HN 118pts):** Docker/Dagger 창업자 Andrea Luzzardi + Sam Alba. LLM 컨트롤 루프를 백엔드에서 실행하고 도구 실행 시만 샌드박스 API를 호출하는 아키텍처 패턴. 샌드박스는 임시(cattle), 자격증명은 샌드박스 진입 불가. Inngest(내구성 실행) + Blaxel(25ms 재개) 조합. L2 아키텍처 레퍼런스.
- **DeepSeek V4-Pro (HN 557pts):** 오픈웨이트 1.6T/49B 활성 MoE, 1M 컨텍스트, MIT 라이선스. 입력 $0.000435/1k — GPT-5.5·Claude Opus 4.7 대비 7배 저렴. 오픈소스 중 에이전틱 코딩 SWE-Bench SOTA. V4-Flash(13B 활성, $0.00014/1k)도 동시 출시. clawfit llms.json에 양쪽 추가됨.
- **microsoft/agent-framework 1.0 (~10k★):** Semantic Kernel(26k★) + AutoGen(50k★) 통합 프레임워크. .NET + Python 지원, 그래프 기반 멀티에이전트 오케스트레이션. 2026-04-03 v1.0 출시. L2 엔터프라이즈 하네스.
- **acai.sh / Specsmaxxing (HN 157pts):** YAML `feature.yaml` 스펙에 ACID(Acceptance Criteria ID)를 붙여 에이전트가 코드·테스트 전체에 자동 태깅. "스펙이 진실, 현재 동작은 임시" 철학. Apache 2.0 CLI. L3 요구사항-태깅 SSOT 서브타입 후보.
- **lukilabs/craft-agents-oss (GitHub Trending):** craft.do의 문서 중심 멀티에이전트 데스크탑 앱. 멀티세션 인박스, 스트리밍, 복수 LLM 연결. Claude Agent SDK + Pi SDK 동시 사용. TypeScript, Apache 2.0. L6 문서 중심 데스크탑 서브타입 후보.
- **xAI Grok 4.3 (2026-04-30 출시):** 2M 컨텍스트(서양 폐쇄형 최대), 네이티브 영상 입력, 슬라이드 생성, 40% 가격 인하. OpenClaw 업데이트에 채택. llms.json 보류 — 독립 벤치마크 확인 후 추가 예정.

### 2026-04-30 신규 신호
- **Warp 오픈소스 (⭐42,313, +11,955/일 신기록):** OpenAI를 창립 스폰서로 터미널/ADE 전환. clawfit 추적 역대 최고 속도. 벤더가 타사 에이전트 서페이스를 직접 후원하는 최초 사례. L6 primary + L2(Oz 클라우드 오케스트레이션) + L1(내장 코딩 에이전트) 멀티레이어 붕괴.
- **memvid (⭐15.3k, Apache-2.0):** 단일 `.mv2` 이식형 바이너리 메모리 컨테이너 (WAL + HNSW + BM25 + TOC). Rust v2.0, P50 검색 0.025ms. L4a 메모리 세 번째 서브트랙(이식형 바이너리) 확정. L4a에 추가됨.
- **NVIDIA OpenShell (⭐5.4k, alpha):** NVIDIA의 첫 L1 에이전트 런타임 진입. K3s-in-Docker, 핫 리로드 정책, 개인정보 라우팅. Claude Code·OpenCode·Codex·GitHub Copilot CLI·Ollama 호환. 단일 신호, 레지스트리 미등록.
- **Mistral "vibe remote agents" + Medium 3.5:** 주요 모델 랩 최초로 "vibe"를 공식 제품명 채택. Dense 128B, 256k ctx, SWE-Bench Verified 77.6%, modified MIT. clawfit llms.json에 추가됨. 4대 벤더(Anthropic/OpenAI/Google/Mistral) 관리형 비동기 에이전트 클러스터 완성.
- **hongsw/harness (⭐6, 디자인 오리진):** revfactory/harness에 한국어/음성 로케일 오버레이 3개 스킬 추가. locale/voice overlay가 L4b 세 번째 축 후보. DureClaw와 함께 hongsw 2레이어 디자인 오리진 레퍼런스로 L2에 추가.
- **cc-connect (⭐6.7k, Go):** 11개 채팅 플랫폼 + 10개 에이전트 단일 바이너리 브리지. CN 리전 커버리지 강점. L7 메시징 브리지 서브패턴 3번째 데이터포인트 — 패턴 확정.
- **Zed 1.0 안정화 + Zed for Business (HN 956pts):** 0.x → 1.0 출시, 중앙화 청구·RBAC·팀 관리. ACP 멀티플렉싱(Claude·Codex·OpenCode·Cursor). 엔터프라이즈 적합성 임계값 돌파.

### 2026-04-28 신규 신호 (요약)
- **cc-switch (⭐52.8k, +892/일):** Claude Code·Codex·Gemini·OpenCode·OpenClaw 통합 프로바이더 전환기. SSOT 원자쓰기·롤백. L3/L4 멀티벤더 anti-lockin 클러스터 최강 신호.
- **cmux (⭐15.6k, macOS):** OSC 알림·수직 탭 네이티브 터미널. `cmux claude-teams` 통합. L6 터미널 멀티플렉서.
- **GitNexus (⭐31.5k):** WASM/WebGPU 클라이언트 사이드 코드 그래프-RAG, MCP 16개 도구. L4a/L4c.
- **dirac:** Cline 포크, Terminal-Bench 2.0 1위(65.2%). MCP 비채택 명시. Gemini flash로 소형 모델 에이전트 생산성 입증.
- **Engram + wuphf:** L4a SQLite+MCP-native 메모리 클러스터. 인스펙터블 메모리 서브패턴 확정. L4a 추가됨.
- **claw0 (⭐2,385):** OpenClaw 구현 10섹션 커리큘럼, 3개국어. L3 에이전트 내부 구조 리터러시 서브패턴 3번째 데이터포인트.
- **GitHub Copilot PRU→AI Credits 전환 (2026-06-01):** Anthropic의 Claude Code Pro 폐지와 함께 6주 안에 최대 2개 벤더가 사용량 기반 요금으로 수렴. `pricing_tier: paid` 예측력 약화.

### 2026-04-08 ~ 2026-04-27 신규 신호 (요약)
- **Claude Mythos Preview:** 새 Anthropic 모델 티어. 장기 태스크·보안 도메인 특화. Glasswing AI 거버넌스 프레임워크.
- **Harness Engineering 패러다임 명명:** "프롬프트 엔지니어링 → 컨텍스트 엔지니어링 → 하네스 엔지니어링(2025–2026)" 4년 회고록 GeekNews 1위. L2–L3 강조 검증.
- **obra/superpowers (⭐145k+):** 하네스/SSOT 중 최대 스타 리포. Shell 기반 에이전틱 스킬 + 방법론. L3/L4b.
- **Archon (⭐15k):** 하네스 빌더(하네스를 생성하는 메타 도구). 결정론적·반복 가능 프레임 L2 새 서브타입.
- **Twill.ai / rowboat / multica:** 비동기 클라우드 에이전트 위임, 메모리-퍼스트 AI 동료, 팀 중심 멀티에이전트 관리. L1–L2 전반.
- **Shannon (⭐36k):** AI 자율 침투 테스터. 단일 비-코딩 도메인(보안) 특화 L1 에이전트. `security-testing` 태스크 라벨 신설 검토.
- **Thunderbolt (Mozilla, ⭐2.2k):** 프라이버시 퍼스트 크로스플랫폼 AI 클라이언트. `data_sensitivity: confidential` + `governance_need: hard` 프로파일용. L7.
- **Qwen3.6-35B-A3B:** 오픈웨이트 에이전틱 코딩 MoE. 오프라인 저예산 프로파일 유력 후보. SWE-bench 확인 후 등록 검토.
- **Freestyle:** sub-700ms 부팅 클라우드 Linux VM, 라이브 포크·pause/resume. L2 실행 기판 제품 카테고리화 신호.

---

## Level 1 — 기본 런타임 / 주요 에이전트 서페이스

사용자가 기본 환경으로 가장 직접적으로 선택하는 도구들.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [OpenClaw](https://github.com/openclaw/openclaw) | ⭐ 365,342 | 대규모 오픈소스 에이전트 런타임 |
| [OpenCode](https://github.com/anomalyco/opencode) | ⭐ 150,654 | |
| [Claude Code](https://github.com/anthropics/claude-code) | ⭐ 118,485 | Anthropic 공식 CLI |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | ⭐ 72,201 | |
| [Cline](https://github.com/cline/cline) | ⭐ 61,063 | VS Code 에이전트 |
| [Aider](https://github.com/paul-gauthier/aider) | ⭐ 44,022 | Git-aware 코딩 에이전트 |
| [Goose](https://github.com/block/goose) | ⭐ 43,404 | Block의 오픈소스 에이전트 |
| [Continue](https://github.com/continuedev/continue) | ⭐ 32,841 | |
| [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | ⭐ 30,697 | |
| [Crush](https://github.com/charmbracelet/crush) | ⭐ 23,571 | |
| [deepagents](https://github.com/langchain-ai/deepagents) | ⭐ 21,878 | LangGraph 기반 하네스 *(L2 중복)* |
| [understudy](https://github.com/understudy-ai/understudy) | ⭐ 422 | 시연으로 배우는 로컬 데스크탑 에이전트 |
| Cursor | — | https://cursor.com/ |
| Kiro CLI | — | https://kiro.dev/ |
| Claude Computer Use | — | 퍼스트파티 데스크탑 제어 *(L7 중복)* |

---

## Level 2 — 메타 래퍼 / 하네스 / 오케스트레이션 레이어

기존 기본 에이전트 위에 올라가 작동 방식을 변환하는 프로젝트들.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | ⭐ 54,537 | 에이전트 하네스 / 메타 래퍼 |
| [claude-code-router](https://github.com/musistudio/claude-code-router) | ⭐ 33,100 | Claude Code 라우팅 래퍼 |
| [oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) | ⭐ 31,602 | Claude Code 멀티에이전트 오케스트레이션 |
| [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | ⭐ 26,371 | Codex 확장 / 훅 / HUD / 에이전트 팀 |
| [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) | ⭐ 22,511 | Claude 워크플로우 프레임워크 |
| [deepagents](https://github.com/langchain-ai/deepagents) | ⭐ 21,878 | LangGraph SDK *(L1 중복)* |
| [Aperant](https://github.com/AndyMik90/Aperant) | ⭐ 14,093 | |
| [claudecodeui](https://github.com/siteboon/claudecodeui) | ⭐ 10,291 | |
| [ralph-claude-code](https://github.com/frankbria/ralph-claude-code) | ⭐ 8,878 | |
| [oh-my-pi](https://github.com/can1357/oh-my-pi) | ⭐ 3,541 | Hashline: 동시 멀티에이전트 파일 안전성 해시 검증 |
| [ouroboros](https://github.com/Q00/ouroboros) | ⭐ 2,761 | "Agent OS: stop prompting, start specifying" — Claude Code/Codex/OpenCode/Hermes 위에 올라가는 spec-driven 하네스; Double-Diamond 워크플로우 + 9개 전문 에이전트 + Ralph evolutionary loop + PAL cost-tier router + EventStore; ralph-family 동족 |
| [open-ralph-wiggum](https://github.com/Th0rgal/open-ralph-wiggum) | ⭐ 1,584 | |
| [agentapi](https://github.com/coder/agentapi) | ⭐ 1,372 | |
| [oh-my-agent](https://github.com/first-fluke/oh-my-agent) | ⭐ 856 | 다중 런타임 에이전트 하네스 |
| [oh-my-gemini-cli](https://github.com/Joonghyun-Lee-Frieren/oh-my-gemini-cli) | ⭐ 155 | Gemini CLI 워크플로우 팩 |
| [Anthropic 하네스 설계](https://www.anthropic.com/engineering/harness-design-long-running-apps) | — | 정식 듀얼에이전트 + 스프린트-계약 아키텍처 |

---

## Level 3 — 팀 하네스 / 실행 가능 SSOT / 거버넌스 레이어

LLM 사용이 개인 습관에서 팀 운영 시스템으로 전환되는 레벨.

핵심 개념 — **실행 가능 SSOT(단일 진실 공급원)**:
- 사람은 워크플로우 또는 운영 가이드로 읽고,
- 에이전트는 실행 가능한 지시로 읽는다.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [everything-claude-code](https://github.com/affaan-m/everything-claude-code) | ⭐ 168,366 | 스킬/규칙/에이전트 하네스 최적화 시스템 |
| [cc-sdd](https://github.com/gotalab/cc-sdd) | ⭐ 3,217 | 스펙 기반 개발 워크플로우 |
| [gitagent](https://github.com/open-gitagent/gitagent) | ⭐ 2,545 | Git-native 에이전트 정의 오픈 표준 |
| [oh-my-agent](https://github.com/first-fluke/oh-my-agent) | ⭐ 856 | |
| [DureClaw](https://github.com/DureClaw/dureclaw) | ⭐ 2 | *(주 분류 Level 2)* — 크로스 머신 multi-agent team coordinator; Phoenix WebSocket 메시지 버스 + oah-agent 워커가 Mac/Linux/Windows/Raspberry Pi에 걸친 multi-machine SSOT 패턴 구현 |
| [Toss 하네스 아티클](https://toss.tech/article/harness-for-team-productivity) | — | 팀 생산성 바닥을 높이는 하네스 |
| **AGENTS.md** | — | OpenAI의 크로스 플랫폼 에이전트 스펙. Agentic AI Foundation 소속. CLAUDE.md와 경쟁/보완 관계 |

---

## Level 4 — 기능 확장 레이어 (MCP / 메모리 / 플러그인 / 도구)

기본 런타임을 대체하지 않고 기능을 추가하는 시스템들.

Level 4는 세 가지 서브타입으로 분화 중:

### 4a. 메모리 / 영구 컨텍스트

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [claude-mem](https://github.com/thedotmack/claude-mem) | ⭐ 68,547 🔥 | 훅 기반 영구 메모리 (SQLite + Chroma). `npx claude-mem install` |
| [claude-context](https://github.com/zilliztech/claude-context) | ⭐ 9,859 | |
| [cipher](https://github.com/campfirein/cipher) | ⭐ 4,657 | |
| [OpenMemory](https://github.com/CaviraOSS/OpenMemory) | ⭐ 4,029 | |
| [Engram](https://github.com/Gentleman-Programming/engram) | ⭐ 2,912 | Go 바이너리 영구 메모리; 17개 MCP 툴 + What/Why/Where/Learned 스키마 + session lifecycle 훅; SQLite+FTS5; Beads(런타임-레이어)와 인터페이스 축에서 분기되는 protocol-endpoint 설계 *(L5 inspectable agent memory 서브패턴 동시)* |
| [wuphf](https://github.com/nex-crm/wuphf) | — | Karpathy 스타일 LLM wiki를 에이전트가 Markdown+Git으로 유지; multi-agent 공유 workspace에 notebook→wiki promotion + lint 게이트; human-inspectable agent-maintained memory; vector-DB 비의존 트랙 (Beads/Engram/GBrain 동족) *(L5 inspectable agent memory 서브패턴 동시)* |

### 4b. 스킬 팩 & 스킬 매니저

**스킬 매니저 (생명주기/디스커버리):**

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) | ⭐ 1,851 | 340 플러그인 + 1,367 에이전트 스킬 카탈로그 |
| [Chops](https://github.com/Shpigford/chops) | ⭐ 1,167 | macOS 스킬 매니저. Claude Code, Cursor, Codex, Windsurf, Amp 동시 지원 |
| [skills-cleaner](https://github.com/amebahead/skills-cleaner) | ⭐ 13 | `.claude/plugin/` 스킬 목록 조회/중복 제거 |
| [claudemarketplaces.com](https://claudemarketplaces.com/) | — | 150개+ 평점 스킬 마켓플레이스 (2026-03) |

**플랫폼 네이티브 플러그인 시스템:**

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | ⭐ 18,040 | Anthropic 공식 플러그인 |
| OpenAI Codex 플러그인 | — | Skills + Apps + MCP 번들. GitHub, Linear, Vercel, Slack, Figma, Notion, Gmail 공식 플러그인 |

**도메인 스킬 팩:**

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [Impeccable](https://github.com/pbakaus/impeccable) | ⭐ 16,060 | 7개 도메인 20개 디자인 명령어 (레이아웃, 간격, 색상, 타이포그래피…) |
| [K-Skill](https://github.com/NomaDamas/k-skill) | ⭐ 1,514 | 한국어 서비스 스킬팩 (SRT, 서울 지하철, KBO, 로또) |
| [plugins-for-claude-natives](https://github.com/team-attention/plugins-for-claude-natives) | ⭐ 748 | |

### 4c. 툴-사용 / 액션 인프라

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | ⭐ 84,644 | MCP 서버 에코시스템. 2025-12 Agentic AI Foundation에 기증 |
| [Composio](https://github.com/ComposioHQ/composio) | ⭐ 27,933 | 에이전트용 대형 툴-액세스 플랫폼 |
| [serena](https://github.com/oraios/serena) | ⭐ 23,498 | 코딩 에이전트용 시맨틱 검색/편집 툴킷 |
| [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | ⭐ 15,963 | Microsoft MCP 교육 커리큘럼 |
| [mcp-context-forge](https://github.com/IBM/mcp-context-forge) | ⭐ 3,620 | IBM AI 게이트웨이 + MCP 프록시 |
| [Expect](https://github.com/millionco/expect) | ⭐ 3,062 | 코드 변경으로부터 브라우저 기반 테스트 플랜 자동 생성 실행 |
| [Pica](https://github.com/withoneai/pica) | ⭐ 1,476 | 에이전트 도구 플랫폼 (Rust) |

---

## Level 5 — 리서치 / 평가 / 벤치마크 / 자율연구 패턴

평가 하네스, 벤치마크 참조, 자율 리서치 루프, **집단 에이전트 지식 시스템**.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [autoresearch](https://github.com/karpathy/autoresearch) | ⭐ 77,236 | |
| [agent-lightning](https://github.com/microsoft/agent-lightning) | ⭐ 17,042 | Microsoft AI 에이전트 훈련 프레임워크 |
| [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | ⭐ 12,342 | 언어 모델 평가 프레임워크 |
| [any-llm](https://github.com/mozilla-ai/any-llm) | ⭐ 1,926 | 통합 LLM 제공자 인터페이스 |
| [any-agent](https://github.com/mozilla-ai/any-agent) | ⭐ 1,156 | 멀티에이전트 프레임워크 인터페이스 |
| [Ko-AgentBench](https://github.com/Hugging-Face-KREW/Ko-AgentBench) | ⭐ 64 | 한국어 에이전트 벤치마크 |
| [cq](https://blog.mozilla.ai/cq-stack-overflow-for-agents/) | — | Mozilla AI 에이전트 공유 지식 커먼스. "에이전트를 위한 Stack Overflow" |

---

## Level 6 — 데이터 / 증거 / 지식 인프라

에이전트가 외부 지식에 어떻게 접근하고 구조화하는지.

두 가지 구조적 서브타입으로 분리됨 (2026-05-05 공식화):

### L6a — 검색-네이티브 지식 인프라

전처리 → 임베드 → 인덱스 → 검색 → 주입. **LLM은 소비자**이고, 파이프라인/사람이 저장소를 유지.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [MinerU](https://github.com/opendatalab/MinerU) | ⭐ 61,356 | 고품질 PDF/문서 파이프라인 |
| [LightRAG](https://github.com/HKUDS/LightRAG) | ⭐ 34,415 | 그래프+벡터 듀얼 레벨 검색 |
| [PageIndex](https://github.com/VectifyAI/PageIndex) | ⭐ 25,871 | LLM-쿼리 가능 문서 인덱스 |
| [RAG-Anything](https://github.com/HKUDS/RAG-Anything) | ⭐ 19,033 | 멀티모달 RAG |
| [CocoIndex](https://github.com/cocoindex-io/cocoindex) | ⭐ 7,900 | 증분 데이터 파이프라인 엔진, Rust 코어 |
| [airweave](https://github.com/airweave-ai/airweave) | ⭐ 6,266 | LLM 접근 가능 저장소로 읽기 전용 동기화 |

### L6b — LLM-네이티브 지식 베이스

**LLM이 지식 저장소를 직접 생성·유지**. 검색 파이프라인 없음; LLM(또는 사람)이 쿼리. [카파시 LLM Wiki 패턴](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (2026-04-04).

**조작적 정의:** 쓰기 주체가 LLM → L6b. 쓰기 주체가 파이프라인/사람 → L6a.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [wuphf](https://github.com/nex-crm/wuphf) | — | 에이전트가 유지하는 Markdown+Git 위키. L4a 기본, L6b 부차 *(첫 확인 구현체)* |
| GBrain | — | 개인 LLM-네이티브 지식 베이스. L4a 기본, L6b 부차 |
| [찰떡AI](https://chaltteok-app.baryon.ai/) | 클베 | Baryon Labs (서울). 中企 견적·법무 문서 AI 어시스턴트. 이전 견적·메모 → **LLM이 노드/엣지 지식맵 직접 유지** → 다음 문서 자동 적용. 로컬 전용(클라우드 없음). MCP 모듈 [`chaltteok-app-mcp`](https://github.com/baryonlabs/chaltteok-app-mcp) (Rust, MIT) 오픈소스. 카파시 패턴 국내 첫 구현체. L1 부차(도메인 특화 에이전트 런타임). |

---

## Level 7 — 휴먼 인터페이스 / 음성 / 컴퓨터 사용 레이어

음성 입력, 토크 모드, 원격 릴레이, 데스크탑 제어 등 인간이 에이전트를 실제로 조작하는 방식.

| 프로젝트 | 스타 | 설명 |
|---------|------|------|
| [deep-agents-ui](https://github.com/langchain-ai/deep-agents-ui) | ⭐ 1,577 | deepagents용 Next.js 웹 UI (채팅 + 파일 모니터 + 단계별 디버그) |
| [Ghostmeet](https://github.com/Higangssh/ghostmeet) | ⭐ 37 | 셀프호스팅 AI 미팅 비서 (Whisper 실시간 전사 + Claude 요약) |
| Claude 컴퓨터 사용 | — | Anthropic 퍼스트파티 데스크탑 제어 (마우스+키보드+화면) *(L1 중복)* |
| Superwhisper | — | https://superwhisper.com/ |

---

## 관련 문서

- 영문 에코시스템 맵: [`reference-levels.md`](reference-levels.md)
- research-watch 문서들: [`research-watch/`](research-watch/)
- 에코시스템 개요: [`pages/ecosystem-overview.md`](pages/ecosystem-overview.md)
- 한국어 README: [`../README.ko.md`](../README.ko.md)
