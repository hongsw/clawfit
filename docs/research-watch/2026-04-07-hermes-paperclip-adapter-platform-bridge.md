# Research Watch: hermes-paperclip-adapter — Hermes↔Paperclip 플랫폼 브릿지

- Repo/Link: https://github.com/NousResearch/hermes-paperclip-adapter
- Source: hongsw GitHub stars

## 무엇인가

NousResearch가 만든 **Hermes Agent를 Paperclip 플랫폼의 관리형 직원으로 작동시키는 어댑터**다. Hermes의 학습 루프와 Paperclip의 팀 오케스트레이션 인프라를 연결하는 브릿지 역할을 한다. 기본 모델은 `anthropic/claude-sonnet-4`, TypeScript/JavaScript/Python 혼합, 스타 636개, 포크 92개, 커밋 14개.

## 주요 특징

- **8개 추론 프로바이더**: Anthropic, OpenRouter, OpenAI 지원
- **30+ 네이티브 도구**, 80+ 로드 가능 스킬
- **MCP 통합** 내장
- **세션 지속성** (Hermes의 크로스 세션 메모리 활용)
- **마크다운 후처리** 자동화
- **9개 도구셋**: terminal, file, web, browser, code_execution, vision, mcp, creative, productivity
- 기본 타임아웃: 300초, 그레이스 기간: 10초 (SIGKILL 전)

## clawfit 관점에서 의미

- L1(Hermes 런타임) + L2(Paperclip 오케스트레이션)의 하이브리드 어댑터 — 플랫폼 간 에이전트 이식성 패턴
- hermes-agent(L1)와 별도 추적 필요: 동일 Nous Research이지만 역할이 다름
- 스타 636개 (포크 92, 커밋 14): 초기 단계이나 Nous Research 공식 리포
- `team_size=large` + `statefulness=persistent` 프로파일에서 Paperclip 도입 시 핵심 어댑터

## 분류

**Level 1/2 — 에이전트 런타임 어댑터 (Hermes→Paperclip 플랫폼 브릿지)**

## 상태

- 추적 중: 신규 등록. 스타 636개 (포크 92, 커밋 14). Nous Research 공식 프로젝트. Paperclip 플랫폼 채택 확산 여부 모니터링.
