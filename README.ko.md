# clawfit

> AI 에이전트 + LLM + 하드웨어 추천 엔진 — **162+ 도구**, **7레이어 생태계 맵**, **192개 리서치워치 문서**, **10차원 스코어링**

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](pyproject.toml)
[![Tests](https://img.shields.io/badge/tests-pytest-informational)](tests/)
[![Status](https://img.shields.io/badge/status-early%20public-green)](https://github.com/hongsw/clawfit)

**다른 언어로 읽기:** [English 🇺🇸](README.md)

---

## clawfit이 뭔가요?

`clawfit`은 하나의 실용적인 질문에 답합니다:

**주어진 태스크, 레이턴시 목표, 예산, 네트워크 환경, 팀 성숙도에서 어떤 에이전트 + 모델 + 하드웨어 조합이 가장 적합한가?**

세 가지를 하나로 통합합니다:

1. **추천 엔진** — (에이전트, LLM, 하드웨어) 조합을 6개 가중 차원으로 스코어링. 하드 필터가 불일치를 제거하고, 소프트 멀티플라이어가 세부 조정.

2. **에코시스템 맵** — 7레이어 분류체계, 162+ 도구를 별 개수와 함께 추적. GitHub Trending / GeekNews / HN을 매일 자동 스캔, 186개 리서치워치 문서.

3. **조직 적합도 진단** — 10문항 인터랙티브 설문으로 조직의 제약 벡터를 구축, 우선순위화된 멀티 레이어 도구 스택 반환.

---

## 🗺 에코시스템 맵 — 7레이어 + 기반 서브스트레이트

![에코시스템 맵](docs/assets/ecosystem-map.ko.svg)

> **맵 vs 레지스트리**: 맵은 162+ 도구를 인식 목적으로 추적. **추천 레지스트리** (20개: 4 에이전트 × 11 LLM × 5 하드웨어)는 `clawfit recommend`가 스코어링하는 검증된 엔트리.

---

## ⚙️ 추천 엔진 축 구조

```
                    ┌──────────────────────────────────────────────────┐
   태스크 ────────▶ │              하드 필터                            │ ◀── 네트워크 (온라인/오프라인)
   code-gen/qa/...  │  태스크 일치 · 레이턴시 · 예산 · 네트워크        │     하드웨어 (클라우드/엣지/로컬)
                    │  상태유지성 · 하드웨어 타입                       │
   레이턴시 ──────▶ │──────────────────────────────────────────────────│
   low/mid/high     │              스코어링                             │ ◀── 예산 ($/1k 토큰)
                    │  레이턴시 일치   ×0.50                            │
   성숙도 ────────▶ │  비용 일치       ×0.25  (성숙도 시 ÷×0.80)       │
   1~11단계         │  LLM 선호도      ×0.15                            │
                    │  성숙도 적합도   ×0.15  (기준값 대체)             │
                    └────────────────────┬─────────────────────────────┘
                                         │
                                  fit_score 0–1.0
                                  (에이전트, LLM, 하드웨어) 조합
```

---

## 📊 숫자로 보는 clawfit

| 지표 | 수치 |
|------|------|
| 에코시스템 맵 추적 도구 (7레이어) | **162+** |
| 리서치워치 신호 문서 | **186개** |
| 추천 레지스트리 LLM | **11개** |
| 추천 레지스트리 에이전트 패턴 | **4개** |
| 추천 레지스트리 하드웨어 프로필 | **5개** |
| 자동화 테스트 | **29개** |
| 분류 레이어 (L0–L7) | **8개** |
| 스코어링 차원 수 | **6개** (레이턴시×3 + 비용 + 선호도 + 성숙도) |
| 추적된 스캔 날짜 | **24일** (2026-03-31 → 오늘) |

---

### 누구를 위한 것인가?

| 당신이 ... | clawfit이 주는 것 |
|------------|-----------------|
| 에이전트 스택을 고르는 개발자 | 태스크 + 제약에 맞는 스코어링된 (에이전트, LLM, 하드웨어) 조합 |
| 로컬 vs 클라우드를 결정하는 DevOps | 네트워크 / 하드웨어 / 비용 하드 필터 — 추측 불필요 |
| AI 도구 전략을 평가하는 CTO | 162+ 도구 7레이어 생태계 맵, 매일 업데이트 |
| 에이전트 생태계를 매핑하는 연구자 | 186개 증거 문서 + 별 개수 포함 분류체계 |
| 현재 동향을 파악하려는 누구든 | 매일 스캔: GitHub Trending + GeekNews + HN, 자동 커밋 |

> [!IMPORTANT]
> **에코시스템 맵 — 여기서 시작하세요**
>
> `clawfit`이 실제로 무엇을 매핑·비교·추적하는지 이해하려면:
>
> ## **[에코시스템 맵 바로가기: `docs/reference-levels.md`](https://github.com/hongsw/clawfit/blob/main/docs/reference-levels.md)**
>
> 현재 AI 도구 생태계의 전체 구도를 가장 빠르게 파악할 수 있습니다:
> - 기본 에이전트 런타임 (Claude Code, OpenClaw, Goose, Aider, pi-mono, ATLAS...)
> - 하네스 / 래퍼 레이어 (oh-my-*, DureClaw, SuperClaude, Archon...)
> - 리서치 루프 시스템 (autoresearch, mdarena, cq...)
> - MCP / 메모리 / 툴 에코시스템 (claude-mem, korean-law-mcp, rtk...)
> - 스킬팩 & 페르소나 레이어 (career-ops, caveman, Polysona...)
> - 휴먼 인터페이스 / 생성형 UI (pi-generative-ui, Ghost Pepper...)

---

## 🔥 지금 가장 뜨거운 것들 (2026-07-07)

| 신호 | 왜 중요한가 | 레벨 |
|------|------------|------|
| **[ruvnet/RuView](https://github.com/ruvnet/RuView) ⭐78.3k** | WiFi 공간지능 플랫폼(ESP32 메시): 재실감지·생체신호·자세추정 — MCP 서버(`rvagent`)로 에이전트가 물리 환경 상태를 쿼리 가능. 최초의 "물리세계 MCP 능력" 신호. 7.8만 스타는 메이커 + 에이전트 생태계 교차점 반영. | L4c |
| **[HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) ⭐20.6k** | 에이전트 네이티브 거래 환경: AI 에이전트가 등록하여 서로의 전략을 카피 트레이딩하고 $10만 모의 자본으로 리더보드에서 경쟁. "인간을 위한 거래 실행"이 아닌 "에이전트 간 경쟁" 프레임. 두 번째 HKUDS 금융 도메인 신호(vibe-trading 2026-05 이후). | L1/L5 |
| **[langbot-app/LangBot](https://github.com/langbot-app/LangBot) ⭐16.7k** | 오픈소스 멀티플랫폼 메시징 에이전트 프레임워크 — 단일 런타임으로 11개 플랫폼(Discord·Slack·Telegram·WeChat·WeCom·QQ·Lark·LINE·DingTalk·KOOK·Matrix) 지원; 네이티브 MCP; 접근제어·속도제한·콘텐츠 필터 내장; v4.10.5, 199회 릴리즈. 최초의 메시징 네이티브 L1 프레임워크. | L1/L2 |
| **Anthropic 전역 작업공간 논문 (HN 242점)** | 16인 공동 논문이 Claude에서 전역작업공간이론(GWT) 5개 속성을 만족하는 "J-공간" 확인(야코비안 렌즈). J-공간 어블레이션 시 숨겨진 추론 노출 — 안전 응용 주장. J-렌즈가 API로 제공되면 L5 기본 요소가 될 수 있음. | L1 ref |
| **AMD Ryzen AI Halo ($3,999, 소매 판매 중)** | 최초의 구매 가능한 AMD AI 개발 키트: 128GB 통합 LPDDR5x-8000, XDNA 2 NPU(50 TOPS), 20B 모델에서 35W로 ~20 tok/s. `hardware.json`에 추가 — 최초의 AMD 로컬 워크스테이션 프로파일. ROCm 의존성이 주요 채택 리스크. | L7 |
| **[kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) ⭐6k** | Kyutai Labs(Moshi 팀)의 CPU 전용 TTS: ~200ms 첫 청크, M4에서 실시간 대비 6배 속도, GPU 불필요; 음성 복제, 6개 언어, pip 설치. 세 번째 음성/오디오 신호 — 음성 클러스터 모니터링 조건(3번째 신호 + Meetily 2만 돌파) 충족. | L4b |
| **[bradautomates/claude-video](https://github.com/bradautomates/claude-video) ⭐4.2k** | `/watch <url> <question>`으로 Claude Code에 3단계 비디오 파이프라인(yt-dlp + ffmpeg + Whisper/Groq) 추가. 4가지 디테일 모드; 토큰 인식 프레임 예산 관리. L4b 스킬 레이어에서 추적된 최초의 비디오 입력 모달리티. | L4b |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi) ⭐1.3k** | 폐쇄 루프 평가+시뮬레이션+가드레일+프롬프트 최적화 플랫폼 — 프로덕션 트레이스가 6개 알고리즘을 통해 자동으로 프롬프트를 재작성. 최초의 오픈소스 "시뮬레이션→최적화" L5 도구. Langfuse(수동)·Claw Patrol(적대적 입력)와 구별. | L5 |

전체 분석: [`docs/research-watch/`](docs/research-watch/) (411개 문서) · 전체 맵: [`docs/reference-levels.md`](docs/reference-levels.md)

---

## 🧑‍💼 한국 AI 전문가 팀 리뷰 (2026-05-05)

7레이어 + L6a/L6b 분리를 포함한 에코시스템 맵을 4인 한국 AI 전문가 페르소나가 독립 검토했습니다.

| 검토자 | 역할 | 핵심 평가 | 주요 제안 |
|--------|------|----------|----------|
| **강민준** | 대기업 CTO | "L6a/L6b 분리는 엔터프라이즈 구매 판단에 직결된다. RAG 인프라 vs 에이전틱 KB는 벤더 선택이 다르다." | `governance_need: strict` 컴플라이언스 승수 필터 추가 |
| **이지수** | KAIST AI 연구자 | "쓰기 주체 / 읽기 주체로 L4a·L6b를 구분하는 조작적 정의가 반드시 필요하다. 지금 분류는 직관적이지만 경계 사례를 처리 못 한다." | 조작적 정의 문서화 — **완료**: `docs/reference-levels.md`에 반영 |
| **박성현** | MLOps 엔지니어 | "하드웨어 프로필에 VRAM이 없으면 L0* 기반 오프라인 추천이 절반짜리다. fp16 TFLOPS도 모델 선택에 필수." | `hardware.json`에 `vram_gb`, `fp16_tflops`, `cost_per_million_tokens_est` 필드 추가 |
| **최수현** | AI 전문 VC | "스타 개수보다 일별 증가 속도가 시그널이다. ruflo +2,594★/일, TradingAgents +2,181★/일 — 이게 투자 판단 근거." | 뜨거운 것 테이블에 `+★/일` 속도 컬럼 추가 |

> 이지수 연구자의 조작적 정의는 이미 [`docs/reference-levels.md`](docs/reference-levels.md) L6b 섹션에 반영되었습니다. 나머지 제안(거버넌스 필터, 하드웨어 필드, 속도 컬럼)은 다음 마일스톤에서 처리 예정입니다.

---

## 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-07-07 | 데일리 스캔 (10개 문서, 2회 실행): run 1 — AMD Ryzen AI Halo(hardware.json +1, 최초 AMD 로컬워크스테이션 프로파일); Anthropic 전역작업공간 논문(HN 242점); claude-video ⭐4.2k L4b(비디오 입력 스킬, 최초 비디오 모달리티); OpenTag L6(CopilotKit Slack 구현체); ternlight L1/L7(브라우저 WASM 임베딩, 7MB). Run 2 — LangBot ⭐16.7k L1/L2(11플랫폼 메시징 에이전트, 네이티브 MCP, 199회 릴리즈); pocket-tts ⭐6k L4b/L6(Kyutai CPU TTS, ~200ms, 3번째 음성 신호 — 클러스터 조건 충족); RuView ⭐78.3k L4c(WiFi 공간AI + 물리세계 MCP 브릿지); AI-Trader ⭐20.6k L1/L5(에이전트 네이티브 거래 경쟁, 2번째 HKUDS 금융 신호); future-agi ⭐1.3k L5(폐쇄루프 시뮬+평가+가드레일+프롬프트최적화). reference-levels.md: 2026-07-07 발견 로그; 메시징 배포 2-신호 클러스터(OpenTag + LangBot). 50/50 테스트. |
| 2026-07-06 | 데일리 스캔 (8개 문서, 2회 실행): system_prompts_leaks ⭐51.2k L3(첫 크로스벤더 시스템 프롬프트 카탈로그, GitHub 트렌딩 1위), awesome-claude-code ⭐48.7k L4b(Claude Code 에코시스템 허브, 4.3k 포크), Fable5/Vending-Bench L5/meta(HN 123점 — "그럴듯한 부인가능성" 정렬 회귀 vs Opus 4.8, 안전 분류기 대응 확인), alibaba/zvec ⭐13.3k L5(첫 인프로세스 임베디드 벡터 DB), OfficeCLI ⭐8.4k L4c(에이전트 네이티브 Office 파일 자동화 v1.0.129), gastown ⭐16.6k L2(Go 멀티에이전트 워크스페이스 매니저), CodexBar ⭐16.7k L7(개발자 비용 모니터), 신문 편집 구조 L3/meta. reference-levels.md: 2026-07-06 발견 로그(8개 신호); 정규 섹션 변경 없음. 50/50 테스트. |
| 2026-07-05 | 데일리 스캔 run 4 (5개 문서): planning-with-files ⭐24.6k L5/L4b (크래시 방지 플래닝, 60개+ 에이전트), free-llm-api-resources ⭐25.4k L7 (추론 상품화 신호), nano-vllm ⭐14.4k L7 (최소 vLLM 재구현), OpenClaw-RL ⭐5.4k L1 (Princeton 비동기 RL 훈련), pxpipe ⭐~2.3k L7 (PNG 컨텍스트 프록시 59-70% 절감). reference-levels.md: run 4 로그 7항목 추가; 정규 섹션 변경 없음. 50/50 테스트 통과. |
| 2026-07-05 | 데일리 스캔 (5개 문서): agent-deck L2/L6(터미널 멀티에이전트 세션 매니저, Conductor 패턴, 스타 수 불일치 플래그); microsoft/intelligent-terminal L7/L1(ACP 3벤더 표준 확정 — Zed+JetBrains+Microsoft); terax-ai ⭐8k L1/L7(7MB 풋프린트 제약 터미널 워크스페이스, 오프라인 LLM); MCP stateless RC(세션 레이어 제거, 7월 28일 발효); "Better Models: Worse Tools" L2 메타(Armin Ronacher, HN 44점, 하네스 스키마 회귀). reference-levels.md: L4c MCP stateless RC 노트; L7 ACP 3벤더 어노테이션; 2026-07-05 발견 로그. 50/50 테스트. 레지스트리 추가 없음. |
| 2026-07-04 | 데일리 스캔 (7개 문서, 2회 실행): meetily ⭐14.9k L1/L6(완전 로컬 회의 에이전트, 첫 `meeting-notes` 태스크 버티컬, 로컬 음성/오디오 클러스터 형성); alirezarezvani/claude-skills ⭐20k L4b(337 스킬, 10+ 에이전트, 비엔지니어링 영역); unity-mcp ⭐11.5k L4c(Unity Editor 인프로세스 MCP); huggingface/speech-to-speech ⭐5.3k L4b 음성(완전 로컬 STT→LLM→TTS, Tier-1 출처); astryx L4b(Meta 에이전트 네이티브 디자인 시스템, MCP+CLI 내장); mcpsnoop L4c(127★, MCP 투명 프록시); jamesob/local-llm ref(666★, HN 388점). reference-levels.md: 2026-07-04 발견 로그 추가; 음성/오디오 2신호 모니터링 플래그. 50/50 테스트. 레지스트리 추가 없음 (스키마 공백: meeting-notes·voice-agent·game-dev·skill_pack). |
| 2026-07-02 | 데일리 스캔 (7개 문서, 2회 실행): codex-plugin-cc ⭐22.5k L4c(첫 크로스벤더 위임 브릿지); strands-agents/harness-sdk ⭐6.4k L2(Python+TS 이중 언어 프로덕션 하네스); Senior SWE-Bench L5(Princeton/UW-Madison, Opus 4.8 선두 24%); Manufact MCP Cloud L7 YC S25(첫 MCP 전용 호스팅 플랫폼); NVIDIA/skills ⭐2.2k L4b(OMS 서명 공식 하드웨어 벤더 스킬, 첫 출처 체인); ZCode L1/L7 중국 네이티브(첫 CJK 엔터프라이즈 에이전트 신호); video-use ⭐13.7k L4b(4번째 content-creation 신호). 50/50 테스트. 레지스트리 추가 없음. |
| 2026-07-01 | 데일리 스캔 (8개 문서, 3회 실행): CubeSandbox ⭐6.7k L7(Tencent KVM 마이크로VM 샌드박스, `execution_isolation` 스키마 공백); book-to-skill ⭐7.4k L4b(PDF→Claude Code 스킬, 지식-스킬 팩 서브타입 최초 신호); go-micro ⭐23k L2(첫 Go 하네스, MCP+A2A); OmniRoute ⭐9.4k L7(231+ 공급자 게이트웨이); Claude Code 스테가노그래피 마킹(메타 신호, `api_routing` 스키마 공백); awesome-harness-engineering ⭐2.1k(3번째 하네스-규율 신호); taOS ⭐515 L1/L7(2번째 스택-붕괴 신호, 베타); AutoHarness ⭐335 L2/L3(4번째 하네스-규율 신호, 첫 동작 구현체). 50/50 테스트. 레지스트리 추가 없음. |
| 2026-06-30 | 사용자 지목 (taxonomy 교차 참조): ECC ⭐223k L2 (크로스 하네스 코디네이터, 271 스킬 — 최대 미추적 신호; 서브타입 2신호 대기 + 스타 출처 검증 필요), meta-harness ⭐113 L3 (Codex 런타임 Team-Architecture Factory — 3번째 데이터포인트). 데일리 스캔 갭: 2026-05-24 → 2026-06-30 (5주). |
| 2026-05-12 | 사용자 지목: DSPy RLM (공식 DSPy 모듈, 커뮤니티 레포 ⭐87) L4c — REPL 루프 컨텍스트 탐색, "변수 공간 vs 토큰 공간" 분리로 컨텍스트 rot 해결. 새 L4c 서브클러스터 "REPL-as-context-explorer". 기본 신호는 공식 dspy.ai 문서. |
| 2026-05-11 | 데일리 스캔 (5개 문서): anthropics/skills ⭐132k L4b (L4b "1st-party skill pack" 서브타입 **공식 확정** — 2신호 충족), UI-TARS-desktop ⭐32k L1+L6 (ByteDance 멀티모달 에이전트 스택), react-doctor ⭐7.5k L4b (React 품질 스캐너), codeburn ⭐6k L5 (크로스벤더 비용 관측성 TUI), hunk ⭐3.1k L6 (에이전트 변경 집합 검토 게이트). reference-levels.md: L4b 1st-party 서브타입 확정. 메타데이터 수정 1건: mistral-medium-3-5 비용 $1.50/M → $0.40/M. 50/50 테스트 통과. |
| 2026-05-10 | 사용자 지목: Awesome-Agent-Harness ⭐187 L2 — 에이전트 하네스 6-component H=(E,T,C,S,L,V) 모델 학술 서베이 (논문 110+개, 시스템 20+개 비교 행렬). clawfit L2 분류어의 학술 정의 앵커. 1개 문서. |
| 2026-05-09 | 데일리 스캔 8개 문서: opencode ⭐157k L1(워치큐 최고 스타), pi/earendil-works ⭐46.5k L1(badlogic/pi-mono에서 조직 이전), ds4/antirez HN447pts L1-인프라(디스크 영속 KV캐시 Metal), codegraph ⭐1.1k L4c(MCP+CLAUDE.md 자동 주입), OpenSpec ⭐46.2k L3(6일 내 3번째 spec-first 신호). 사용자 stars 추가: OpenManus ⭐56.2k L1, Vibe-Trading ⭐6.2k L2+L4+MCP, helmor ⭐1k L2. reference-levels.md: opencode 스타 수 갱신. 50/50 테스트. 레지스트리 변경 없음. |
| 2026-05-06 | 데일리 스캔 5개 문서: PageIndex ⭐28.2k L6a 구조 서브타입 + L6c 후보(단일 신호 미승격), anthropics/financial-services ⭐8.5k 1st-party L4b 후보 서브타입, Cloudflare×Stripe 에이전트 프로비저닝+금융 자율성 L4c 서브트랙 후보, Reflex 45배/51배 Computer Use 비용 벤치마크(아키텍처 신호 — 4월 L1/L7 붕괴 패턴 보강), Understand-Anything ⭐12.7k L4b 플러그인. **금융 버티컬 클러스터 메타-패턴 공식화** (5개 신호 × 3+ 레이어 / 1주). 50/50 테스트. 레지스트리 변경 없음. |
| 2026-05-05 | 데일리 스캔 11개 문서: agency-agents ⭐92.4k L4b, Kimi K2.6 → llms.json, MemPalace ⭐51k L4a(벤치마크 논란), local-deep-research ⭐4.8k L5, cloudflare/vibesdk L2, flue L2 샌드박스, manifest L4c 라우팅. L6a/L6b 공식 분리(v0.4). 찰떡AI L6b 추가. 한국 전문가 리뷰 섹션 추가. 29/29 테스트. |
| 2026-05-04 | 데일리 스캔: ruflo ⭐38.8k L2, TradingAgents ⭐65k, ouroboros Agent OS, cocoindex L6, n8n-mcp L4c (1,650+ 노드). n8n-mcp + CocoIndex → reference-levels.md. 5개 research-watch. |
| 2026-05-03 | 데일리 스캔: DeepSeek V4-Pro (SWE-Bench 80.6, $0.44/M), xAI Grok 4.3 (83% 저렴), MS Agent Framework v1.0 (AutoGen+SK 통합), acai.sh ACID 스펙 주도 개발, TradingAgents 57.7k★. 스코어링 성숙도 가중치 버그 수정. 9개 docs. |
| 2026-04-30 | 데일리 스캔: Warp 오픈소스 +11,955★/일 기록, Zed 1.0 안정화, Mistral Medium 3.5 → llms.json, NVIDIA OpenShell L1, memvid L4a 이식형 바이너리, cc-connect L7 3번째 데이터포인트, hongsw/harness L2. research-watch 7개 추가. |
| 2026-04-28 | GitHub 스타 전체 최신화. 분류 목록·테이블 스타순 정렬. 04-21~04-28 데일리 스캔: cc-switch 52.8k★, cmux 15.6k★, GitNexus 31.5k★, dirac TB2 리더, Engram+wuphf L4a, DureClaw L3 SSOT 확인. research-watch 12개 추가. |
| 2026-04-20 | Thunderbolt Mozilla AI 클라이언트 L7, OpenMythos 루프 트랜스포머 신호, Qwen3.6-35B-A3B 오픈웨이트 에이전틱 코딩. |
| 2026-04-12 | DureClaw 하이라이트 추가. 신규 도구 8개 (50→58). 태스크 분류 확장: +orchestration, +education, +legal-research. exec 역할 스코어링 수정. |
| 2026-04-12 | 데일리 스캔: Strix 보안 에이전트, GBrain 개인 지식 베이스 |
| 2026-04-11 | 데일리 스캔: superpowers 145k★, Archon 하네스 빌더, rowboat 메모리 네이티브, Twill.ai 클라우드 위임 |
| 2026-04-08 | Claude Mythos Preview 모델, GLM-5.1 장기 태스크, NVIDIA PersonaPlex, Addy Osmani agent-skills |
| 2026-04-07 | hongsw stars 8개 리포 추가: career-ops, claude-peers-mcp, polysona, pi-generative-ui, dureclaw. 한국어 재작성. 전체 수치 검증. |
| 2026-04-06 | reference-levels.md v0.3: L4 → 4a/4b/4c 세분화. research-watch 19개. 하네스팀 (`.claude/agents/`). |
| 2026-03-31 | 에코시스템 맵 v0.2: 7레이어 분류체계, research-watch 스캔 시작 |

---

## 빠른 시작

### 설치

**방법 A — pipx (권장: 가상환경 없이 전역 설치)**

```bash
pipx install git+https://github.com/hongsw/clawfit
```

> pipx가 없으면: `brew install pipx` 또는 `pip install pipx`

**방법 B — 개발용 editable 설치**

```bash
git clone https://github.com/hongsw/clawfit.git
cd clawfit
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
```

---

### 조직 적합도 진단 — 우리 팀에 맞는 도구 스택 찾기

10개 질문에 답하면 팀에 최적화된 멀티 레이어 도구 조합을 추천합니다.

**TUI** (권장 — 화살표로 탐색, 오른쪽 패널에 결과 실시간 업데이트):

```bash
clawfit tui
```

```
 ████████████░░░░░░  5/10  [USECASE]
 ──────────────────────────┬──────────────────────────────
 AI로 주로 무엇을 하고     │ 4단계 — 도구 활용 에이전트
 싶으신가요?               │
                           │ [PRIMARY] L1 Base runtime
  ○ 코드 작성/리뷰         │    45% Claude Code
  ● 정보 조사 및 요약      │    39% Aider
  ○ 문서 Q&A               │    38% Goose
  ○ 데이터 분류            │
  ○ 데이터 분석            │ [PRIMARY] L4c Tool-use infra
  ○ 콘텐츠 요약            │    41% Serena
                           │    35% Context7
 ─ answered ─              │
  팀 규모: 소규모 팀       │ NEXT STEP
  역할: 개발자             │ meta-wrapper(L2) 도입을
                           │ 고려해보세요...
 ──────────────────────────┴──────────────────────────────
  ↑/↓ 이동   Space/Enter 선택+다음   ← 뒤로   → 앞으로   q 종료
```

| 키 | 동작 |
|----|------|
| `↑` / `↓` | 옵션 이동 |
| `Space` / `Enter` | 선택 + 다음 질문으로 자동 이동 |
| `←` / `h` | 이전 질문으로 |
| `→` / `l` | 다음 질문으로 (이미 답변한 경우) |
| `1` ~ `9` | 해당 번호 질문으로 바로 이동 |
| `q` / `ESC` | 종료 (터미널에 최종 결과 출력) |

**CLI (답변을 JSON으로 미리 입력):**

```bash
clawfit diagnose --answers '{
  "team_size": "small",
  "primary_role": "developer",
  "current_ai_usage": "coding_agent",
  "primary_task": "code-gen",
  "output_destination": "team",
  "frequency": "daily",
  "data_sensitivity": "internal",
  "monthly_budget": "medium",
  "governance_need": "soft",
  "growth_horizon": "deepen"
}'
```

답변 옵션값 참고:

| 질문 ID | 선택 가능한 값 |
|---------|--------------|
| `team_size` | `solo` / `small` / `mid` / `large` |
| `primary_role` | `developer` / `researcher` / `pm` / `exec` / `mixed` |
| `current_ai_usage` | `none` / `chat` / `coding_assistant` / `coding_agent` / `multi_agent` / `building` |
| `primary_task` | `code-gen` / `research` / `qa` / `classification` / `data-analysis` / `summarization` / `orchestration` / `education` / `legal-research` |
| `output_destination` | `personal` / `team` / `internal_product` / `external` |
| `frequency` | `occasional` / `daily` / `continuous` |
| `data_sensitivity` | `public` / `internal` / `confidential` / `regulated` |
| `monthly_budget` | `free` / `low` / `medium` / `high` |
| `governance_need` | `none` / `soft` / `hard` |
| `growth_horizon` | `stable` / `expand` / `deepen` |

**웹 UI** (브라우저에서 실시간 필터링):

```bash
clawfit serve          # http://localhost:7771 자동 오픈
clawfit serve --port 8080
```

---

### 제약 조건을 이미 알고 있다면 — 직접 추천

```bash
clawfit recommend --task qa --latency low --budget 0.01
```

```bash
clawfit recommend \
  --task code-gen \
  --latency medium \
  --budget 0.01 \
  --hardware cloud \
  --network online \
  --statefulness session \
  --maturity 5 \
  --top 5
```

> `--maturity 5` = 서브에이전트 운영 단계. 전체 11단계 정의는 [성숙도 × 레이어 맵](docs/pages/maturity-layer-map.md) 참고.

**실행 예시 출력:**

```
순위 1  fit_score: 0.900
  agent:    react-agent
  llm:      gpt-4o         (openai, $0.003/1k, latency: medium)
  hardware: cloud-serverless
  arch:     cloud-api
  why:
    - ReAct Agent는 medium 레이턴시로 'code-gen'을 지원
    - GPT-4o는 태스크 및 비용 프로파일에 적합
    - GPT-4o는 ReAct Agent의 선호 LLM

순위 2  fit_score: 0.900
  agent:    react-agent
  llm:      claude-sonnet  (anthropic, $0.003/1k, latency: medium)
  hardware: cloud-serverless
  arch:     cloud-api

순위 3  fit_score: 0.850
  agent:    react-agent
  llm:      kimi-k2-6      (moonshot, $0.00095/1k, latency: medium)
  hardware: aws-cpu-medium
  arch:     cloud-api
```

### 레지스트리 확인

```bash
clawfit list agents
clawfit list llms
clawfit list hardware
clawfit profile
```

---

## 스코어링 모델

10차원 가중 스코어링 + 하드 멀티플라이어:

| 차원 | 가중치 | 측정 대상 |
|------|--------|----------|
| task_fit | 0.22 | 도구의 태스크 목록이 사용자의 주요 태스크와 일치하는가? |
| maturity_fit | 0.18 | 사용자의 AI 성숙도 단계(1-11)에 적합한 도구인가? |
| role_fit | 0.15 | 사용자의 역할(개발자/경영진/연구자/DevOps)에 맞는 도구인가? |
| layer_relevance | 0.12 | 도구의 에코시스템 레이어(L1-L7)가 프로파일의 레이어 가중치와 일치하는가? |
| team_size_fit | 0.09 | 사용자의 팀 규모(solo/small/mid/large)에 설계된 도구인가? |
| network_fit | 0.08 | 필요한 네트워크 환경(online/offline/hybrid)에서 작동하는가? |
| latency_fit | 0.06 | 요구되는 레이턴시 티어를 충족하는가? |
| feature_fit | 0.05 | 필요한 기능(거버넌스, 팀 공유, 오프라인)을 지원하는가? |
| complexity_fit | 0.04 | 설치 복잡도가 팀 성숙도에 적합한가? |
| budget_fit | 0.01 | 가격 티어가 예산과 맞는가? |

**하드 멀티플라이어** (가중합 이후 적용):
- 오프라인 필요 + 온라인 전용 도구 → **x0.25**
- 역할 불일치 (역할 겹침 없음) → **x0.75**

---

## 지원 태스크 카테고리

| 태스크 | 설명 |
|--------|------|
| `code-gen` | 코드 생성, 리뷰, 리팩토링 |
| `research` | 정보 수집, 문헌 조사, 심층 분석 |
| `qa` | 질의응답, 문서 Q&A |
| `summarization` | 대규모 콘텐츠 요약 |
| `data-analysis` | 데이터 처리, 시각화, 통계 분석 |
| `orchestration` | 멀티 에이전트 조율, 크로스 머신 태스크 분배 |
| `education` | 개인화 학습, 튜터링, 퀴즈 생성 |
| `legal-research` | 법률 문서 검색, 판례 분석, 규정 준수 |

---

## 작동 방식

파이프라인은 의도적으로 단순하고 검사 가능합니다:

1. **레지스트리 로딩** — 20개 추천 엔트리 (4 에이전트 × 11 LLM × 5 하드웨어) + 162+ 생태계 맵 로드
2. **프로파일 구축** — 10개 설문 답변 → OrgProfile 변환
3. **스코어링** — 10차원 + 하드 멀티플라이어로 각 도구 평가
4. **레이어 그루핑** — 에코시스템 레이어(L1-L7)별 그룹화, 성숙도 단계별 우선순위
5. **추천 출력** — 근거가 포함된 우선순위화 멀티 레이어 스택 반환

---

## 리포지터리 구조

```text
clawfit/
├─ .claude/agents/          ← 하네스팀 서브에이전트 (5개)
├─ clawfit/
│  ├─ cli.py                ← argparse CLI (recommend, list, tui, serve, diagnose)
│  ├─ org_scorer.py         ← 10차원 스코어링 엔진
│  ├─ tui.py                ← curses TUI (분할 화면 실시간 프리뷰)
│  ├─ server.py             ← stdlib HTTP 서버 (localhost:7771)
│  ├─ diagnose.py           ← 인터랙티브 CLI 설문
│  ├─ filters.py            ← 하드 제약 필터링
│  ├─ scoring.py            ← 카테시안 프로덕트 스코어링 (에이전트 × LLM × 하드웨어)
│  ├─ recommend.py          ← 공개 API: recommend() → list[dict]
│  ├─ schemas.py            ← 데이터클래스: Agent, LLM, Hardware, Recommendation
│  ├─ loader.py             ← registry/*.json 로더
│  ├─ data/
│  │  ├─ tools_registry.json  ← 에코시스템 도구 (org_fit 10필드)
│  │  └─ org_questions.json   ← 10문항 설문, 3 페이즈
│  └─ registry/             ← agents.json, llms.json, hardware.json
├─ docs/
│  ├─ reference-levels.md   ← 에코시스템 맵 v0.3 (7레이어 분류체계)
│  ├─ research-watch/       ← 150개+ 신호 분석 문서 (데일리 자동 스캔)
│  └─ pages/                ← ecosystem-overview, ecosystem-axes, maturity-layer-map
├─ data/
│  └─ tools_registry.json   ← clawfit/data/ 미러
├─ tests/
│  ├─ test_filters.py
│  └─ test_recommend.py
└─ pyproject.toml
```

---

## 에코시스템 리서치 레이어

clawfit은 더 넓은 AI 도구 생태계를 추적합니다:
- [`docs/reference-levels.md`](docs/reference-levels.md) — 정식 7레이어 에코시스템 맵
- [`docs/pages/ecosystem-axes.md`](docs/pages/ecosystem-axes.md) — 분류 로직, 경계 규칙, 예제
- [`docs/research-watch/`](docs/research-watch/) — 186개 도구/트렌드 분석 (매일 자동 스캔)
- [`docs/pages/maturity-layer-map.md`](docs/pages/maturity-layer-map.md) — 성숙도 단계(1-11) × 도구 레이어(L1-L7) 매핑

### 7레이어 구조 (주요 항목 별 개수 기준 정렬)

| 레벨 | 이름 | 주요 도구 (★ = GitHub 별 개수) |
|------|------|-------------------------------|
| L0* | 추론 서브스트레이트 (동반 축) | Ollama · vLLM · llama.cpp · MLX · TensorRT-LLM · exo |
| L1 | 기본 런타임 | Claude Code · Aider · Goose · OpenHands · Cline · TradingAgents ★67k |
| L2 | 메타 래퍼 / 오케스트레이션 | ruflo ★40k · DureClaw · MS Agent Framework ★10k · Archon |
| L3 | 팀 하네스 / 실행 SSOT | CLAUDE.md · acai.sh · gitagent · gsd |
| L4a | 메모리 / 영구 컨텍스트 | GitNexus ★31k · cognee · claude-mem · memvid ★15k |
| L4b | 스킬팩 & 매니저 | superpowers ★145k · agency-agents ★92k · obsidian-skills |
| L4c | 도구 사용 / MCP | cc-switch ★52k · n8n-mcp ★19k · serena ★23k · GoModel |
| L5 | 리서치 / 평가 / 벤치마크 | autoresearch · SWE-bench · Engram · memvid |
| L6 | 데이터 / 지식 인프라 | CocoIndex ★7.9k · MinerU · LightRAG · PageIndex · airweave |
| L7 | 휴먼 인터페이스 | Voicebox · Ghost Pepper · Zed 1.0 · cc-connect |

---

## Python API

```python
from clawfit.recommend import recommend

results = recommend(
    task="research",
    latency="high",
    network="online",
    top_n=3,
)

print(results[0])
```

---

## 테스트 실행

```bash
python -m pytest tests/ -v
```

---

## 기여하기

특히 다음 영역의 기여를 환영합니다:
- 레지스트리 확장 (완전한 org_fit 메타데이터가 포함된 신규 도구)
- 스코어링 로직 개선
- 벤치마크 참조 및 증거
- research-watch 신호 분석

이슈 또는 PR을 열어주세요: 무엇을 추가하는지, 어떤 증거가 뒷받침하는지, 비교 모델에 어떻게 맞는지를 포함해주세요.

---

## 라이선스

MIT
