# Daily Scan — Sources & Keywords

이 문서는 `daily-ecosystem-scan` 스킬이 매일 스캔하는 **소스 목록**과 **주제 키워드**를 정의한다. 변경 시 git에 함께 커밋.

---

## Tier 1 — 매일 반드시 확인 (필수)

| # | 소스 | URL | 가져올 것 | 컷오프 |
|---|------|-----|----------|--------|
| 1 | GitHub Trending — Daily | https://github.com/trending?since=daily | 상위 25개 (모든 언어) | stars/day ≥ 50 |
| 2 | GitHub Trending — Python | https://github.com/trending/python?since=daily | 상위 15개 | AI/agent 관련 |
| 3 | GitHub Trending — TypeScript | https://github.com/trending/typescript?since=daily | 상위 15개 | AI/agent 관련 |
| 4 | GeekNews 메인 | https://news.hada.io | 상위 30개 | AI/도구/에이전트 키워드 매치 |
| 5 | Hacker News 프론트 | https://news.ycombinator.com | 상위 30개 | AI 관련 + ≥ 50 pts |
| 6 | hongsw 최근 stars | https://github.com/hongsw?tab=stars | 최근 1일 신규 star | 전체 (사용자 큐레이션 신호) |

## Tier 2 — 가능하면 확인 (보너스)

| # | 소스 | 빈도 | 비고 |
|---|------|------|------|
| 7 | Anthropic 블로그/changelog | https://www.anthropic.com/news | 매일 | Claude Code, MCP, skills 관련 |
| 8 | OpenAI 릴리스 | https://openai.com/blog | 매일 | 모델/agentic 발표 |
| 9 | Hugging Face Daily Papers | https://huggingface.co/papers | 매일 | agent/memory/voice/multimodal |
| 10 | Show HN | https://news.ycombinator.com/show | 매일 | AI 도구 런치 |
| 11 | Product Hunt — AI | https://www.producthunt.com/topics/artificial-intelligence | 매일 | top of day |

## Tier 3 — 주간 (월요일에만)

| # | 소스 | URL |
|---|------|-----|
| 12 | GitHub Trending — Weekly | https://github.com/trending?since=weekly |
| 13 | TLDR AI 뉴스레터 | https://tldr.tech/ai |
| 14 | Latent Space 팟캐스트/뉴스레터 | https://www.latent.space |

---

## 주제 키워드 (clawfit 7-layer 매핑)

각 후보를 빠르게 분류하기 위한 키워드. 하나라도 매치되면 추적 후보.

### Level 1 — Base runtimes
`coding agent`, `agent CLI`, `claude code alternative`, `cursor alternative`, `aider`, `cline`, `goose`, `roo code`, `vscode agent`, `terminal agent`, `IDE agent`

### Level 2 — Meta wrappers / harnesses
`harness`, `wrapper`, `oh-my-`, `agent orchestrator`, `multi-agent`, `agent framework`, `claude code plugin`, `agent loop`, `super agent`

### Level 3 — Team / SSOT
`team agent`, `company orchestration`, `agent governance`, `workflow SSOT`, `ralph`, `paperclip`, `enterprise agent platform`

### Level 4 — Capability / skill / plugin
`MCP server`, `MCP plugin`, `skill pack`, `claude skill`, `agent skill`, `tool use`, `function calling`, `awesome skills`, `skill manager`, `skill directory`

### Level 5 — Memory / context
`agent memory`, `context window`, `sparse attention`, `RAG agent`, `vector memory`, `working memory`, `episodic memory`, `context engine`, `cognee`, `mem0`

### Level 6 — Human interface / multimodal
`voice agent`, `realtime voice`, `vibe coding`, `multimodal agent`, `screen agent`, `computer use`, `CUA`, `browser agent`, `desktop agent`

### Level 7 — Infrastructure / hardware
`edge LLM`, `on-device`, `inference engine`, `agent hardware`, `agent GPU`, `TPU agent`, `serverless agent`, `local-first agent`

### Cross-cutting (반드시 챙길 메타 신호)
- 평가/벤치마크: `SWE-bench`, `agent eval`, `LLM judge`, `red team`
- 보안/거버넌스: `agent security`, `prompt injection defense`, `agent sandbox`
- 가격/접근성: `claude pricing`, `free agent`, `open source claude`
- 한국어 신호: GeekNews에서 `에이전트`, `AI 코딩`, `MCP`, `스킬`, `하네스`

---

## 제외 필터 (스킵)

다음에 해당하면 추적하지 않는다:
- 단순 awesome-list 갱신 (단, 새 카테고리가 추가됐으면 예외)
- 모델 가중치만 공개된 케이스 (응용/agentic 측면이 없으면)
- 일반적인 ML 라이브러리 (clawfit의 7-layer와 무관)
- 100 stars 미만의 신규 repo (학술 저자 또는 신뢰 가능 출처가 아닌 한)
- 이미 `docs/research-watch/`에 등록된 도구 (repo URL grep으로 중복 체크)

---

## 운영 규칙

- 이 파일은 **분기 1회 검토** — 신호 패턴이 바뀌면 소스/키워드 갱신
- 새 소스 추가 시: 30일 시범 운영 후 신호 산출량 평가
- Tier 1 소스가 다운/막힐 경우 즉시 보고하고 임시 대안 모색
- 키워드는 `clawfit/docs/reference-levels.md`의 7-layer 정의와 일치 유지
