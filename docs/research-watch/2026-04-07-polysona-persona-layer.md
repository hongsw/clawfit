# Research Watch: Polysona

- Repo/Link: https://github.com/LilMGenius/polysona
- Source: hongsw GitHub stars

## 무엇인가

Polysona는 **10가지 심리학 프레임워크(MBTI, 에니어그램, 동양 명상 체계 등)를 활용해 사용자의 다중 페르소나를 추출하고, 이를 구조화된 마크다운 파일로 저장해 여러 AI 에이전트에 이식할 수 있게 하는 메타인지 기반 시스템**이다. 페르소나를 시스템 프롬프트에 직접 쓰는 대신 포팅 가능한 구조적 아티팩트(`persona.md`, `nuance.md`, `accounts.md`)로 분리하는 것이 핵심 설계 차별점.

## 주요 특징

- **5단계 에이전트 파이프라인**: Profiler(1회 심리 인터뷰) → Trendsetter(트렌드 수집) → Content-Writer(페르소나 + 트렌드 → 콘텐츠) → Virtual-Follower → Admin
- **다중 서브 페르소나**: executive, creator, gamer 등 역할별 페르소나 전환
- **에이전트 간 이식**: Claude Code, Codex, OpenCode에 동일 페르소나 파일 사용
- **로컬 대시보드**: localhost:3000 HTML UI
- 기술 스택: HTML(61.7%), TypeScript(36.2%), Bun, MCP

## clawfit 관점에서 의미

- `persona` 카테고리 미등록 → clawfit 분류 체계 갭
- org_fit 스코어링에 `personalization` 피처 플래그 없음 → 개인 페르소나 아티팩트가 확산될 경우 대응 필요
- L4a(지속적 메모리)와 L4b(스킬팩/페르소나 레이어)의 하이브리드 성격
- 스타 71개: 초기 신호, 개념적 독창성은 높음

## 분류

**Level 4b — 스킬팩 / 페르소나 레이어 (메타인지 기반, 에이전트 간 이식 가능)**

## 상태

- 추적 중: 초기 관찰. 낮은 신호. 스타 71개. Claude Code 커뮤니티 내 채택 및 페르소나 이식성이 표준 패턴이 되는지 모니터링.
