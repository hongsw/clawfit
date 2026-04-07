# Research Watch: AnythingLLM — 프라이버시 우선 올인원 AI 생산성 플랫폼

- Repo/Link: https://github.com/Mintplex-Labs/anything-llm
- Source: hongsw GitHub stars

## 무엇인가

Mintplex Labs가 만든 **자체 호스팅 AI 생산성 가속기**다. 문서(PDF, TXT, DOCX 등)와의 채팅, 노코드 AI 에이전트 빌더, MCP 완전 호환, 40개 이상의 LLM 프로바이더 지원을 단일 Docker 컨테이너로 제공한다. 최신 버전 1.11.2 기준 스타 57,800개, 포크 6,200개, 커밋 1,896개.

## 주요 특징

- **40+ LLM 프로바이더**: OpenAI, Anthropic, AWS Bedrock, Google Gemini, Ollama, HuggingFace, Groq 등
- **다중 벡터 DB**: LanceDB(기본), PGVector, Pinecone, Chroma, Weaviate, Qdrant, Milvus, Zilliz, Astra DB
- **노코드 에이전트 빌더**: 지능형 도구 선택 포함
- **MCP 완전 호환**
- **멀티유저 + 권한 관리**
- **임베드 가능 채팅 위젯**: 웹사이트 삽입 가능
- **오디오/TTS**: OpenAI Whisper, PiperTTS, ElevenLabs 지원
- 배포: Docker + bare-metal, macOS/Windows/Linux 데스크톱 앱

## clawfit 관점에서 의미

- L1(기본 런타임)과 L2(메타 래퍼) 경계에 위치 — 문서 처리 + 에이전트 오케스트레이션이 하나로 통합
- `network=offline` 또는 혼합 프로파일 모두 지원 (LLM 프로바이더 선택에 따라)
- 스타 57,800개: 비개발자 대상 AI 플랫폼으로 가장 높은 채택률 중 하나
- clawfit 레지스트리의 `role=exec` + `statefulness=session` 프로파일에 강력한 후보

## 분류

**Level 1/2 — 기본 런타임 + 문서 RAG 오케스트레이션 (자체 호스팅)**

## 상태

- 추적 중: 신규 등록. 스타 57,800개 (포크 6,200, 커밋 1,896, v1.11.2). 지속적 업데이트 중. MCP 통합 깊이와 에이전트 빌더 성숙도 모니터링.
