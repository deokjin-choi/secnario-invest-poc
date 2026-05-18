# When to Trust the Agent: Behavioral Load Profiling of LLM Agents in Complex MOT Tasks

> Draft outline — Expert Systems with Applications (ESWA) submission target
> Author: Deokjin Choi (et al.)
> Date: 2026-05

---

## Abstract (초안)

Large language models (LLMs) are increasingly deployed as autonomous agents in multi-step analytical tasks, yet practitioners lack principled guidance on which stages of a complex workflow can be safely delegated to an agent and which require human oversight. This study proposes a **Behavioral Load Profiling (BLP) framework** that characterizes LLM agent task difficulty across pipeline stages using observable proxy metrics: tool call frequency, revision count, output length variability, and re-query rate. To stress-test the framework, we apply it to technology scenario planning—one of the most expert-intensive, structurally complex tasks in management of technology—implemented as a seven-stage agentic pipeline on an AI industry foresight case. Results reveal a consistent difficulty gradient: structural inference stages (cross-impact role classification, axis validation) impose substantially higher agent load than generative stages (narrative construction, trend scanning). These findings provide a reusable instrument for diagnosing automation readiness in complex MOT tasks and offer technology managers empirically grounded guidance for human-in-the-loop design.

**Keywords**: LLM agent, behavioral load profiling, management of technology, technology foresight, human-AI collaboration, scenario planning automation

---

## 1. Introduction

### 1.1 The Delegation Problem
- LLM 에이전트가 복잡한 분석 태스크를 자율 실행할 수 있게 됐지만, 실무자는 "어디까지 믿어도 되는가"를 판단하는 원칙이 없음
- 에이전트에 전부 맡기면 구조적 오류가 누적되고, 전부 인간이 검토하면 자동화 이득이 사라짐
- **핵심 질문**: 다단계 복잡 태스크에서 LLM 에이전트의 단계별 난이도를 어떻게 측정하고, 이를 인간 개입 설계에 어떻게 활용할 수 있는가?

### 1.2 왜 MOT 태스크인가
- MOT(Management of Technology) 태스크는 에이전트 능력의 한계를 시험하기에 이상적
  - 구조적 추론과 도메인 지식이 동시에 필요
  - 단계 간 내부 정합성이 요구됨
  - 전문가 의존도가 높아 자동화 이득이 큼
- 본 연구의 저자 라인: LLM × 특허 평가(논문1) → LLM × 전략 판단(논문2) → LLM 에이전트 × 다단계 MOT 파이프라인(본 논문)

### 1.3 왜 시나리오 플래닝인가 (케이스 선택 근거)
- MOT 태스크 중 복잡도가 가장 높은 축에 속하는 대표적 사례
  - 다단계(7단계), 단계 간 결과가 서로 의존
  - 구조적 추론(Cross-impact) + 생성(내러티브)이 동시에 요구
  - 전통적으로 전문가 워크숍 3~6개월 소요 → 자동화 이득 극대
- **Stress test 논리**: 이 태스크에서 BLP 프레임워크가 유효하다면, 더 단순한 MOT 태스크(특허 분류, 기술 로드맵 등)에는 당연히 적용 가능

### 1.4 Research Questions
- **RQ1**: LLM 에이전트의 단계별 태스크 난이도를 측정하는 프레임워크를 어떻게 설계할 수 있는가?
- **RQ2**: 기술예측 시나리오 플래닝 파이프라인에서 BLP 프레임워크는 어떤 난이도 패턴을 보이는가?
- **RQ3**: 그 패턴은 무엇으로 설명되며, 기술 관리자의 human-in-the-loop 설계에 어떤 함의를 주는가?

### 1.5 Contributions
1. **Behavioral Load Profiling (BLP) 프레임워크**: LLM 에이전트 단계별 난이도를 측정하는 일반화 가능한 도구
2. **MOT 스트레스 테스트**: 시나리오 플래닝을 대상으로 한 프레임워크 실증 — 가장 어려운 케이스에서의 유효성 확인
3. **실용적 가이드**: 어느 단계를 에이전트에 위임하고 어디에 인간이 개입해야 하는지에 대한 경험적 근거

---

## 2. Related Work

### 2.1 LLM Agents in Complex Analytical Tasks
- 단일 프롬프트 vs. 다단계 에이전트 파이프라인의 차이
- Tool-using agents, ReAct, chain-of-thought 등 에이전트 아키텍처
- 기존 연구의 한계: 태스크 난이도를 단계 수준에서 측정한 연구 부재

### 2.2 Human-in-the-Loop 설계
- HITL 원칙: 언제, 어디에 인간을 개입시킬 것인가
- 기존 접근: 오류율 기반, 신뢰도 점수 기반
- 본 연구의 차별점: **에이전트 행동 자체**에서 개입 필요 지점을 도출

### 2.3 MOT에서의 LLM 활용
- 특허 평가(논문1), 전략 판단(논문2)의 선행 성과
- 기술예측·시나리오 플래닝의 LLM 활용 기존 연구 — 단일 단계 자동화에 집중, 전체 파이프라인 부재
- STEEP, Cross-impact, 2×2 시나리오 방법론 개요

### 2.4 Task Complexity in AI Systems
- Cognitive load theory의 AI 적용
- Task decomposition과 difficulty characterization 관련 연구
- 본 프레임워크의 이론적 토대

---

## 3. Behavioral Load Profiling (BLP) Framework

> **이 섹션이 논문의 핵심 기여**

### 3.1 "에이전트 부하"의 정의
수치 해석의 잔차(residual)와 달리, 자연어 추론 에이전트의 난이도는 **행동 패턴**으로 간접 측정.

에이전트 부하(Agent Load) = 특정 단계 태스크 완료까지 소비한 인지적 노력의 대리 지표

### 3.2 Proxy Metrics (4개)

| 지표 | 약어 | 측정 방법 | 의미 |
|------|------|-----------|------|
| Tool Call Frequency | TCF | 단계당 도구 호출 횟수 | 외부 확인·검색 필요성 |
| Revision Count | RC | 초기 출력 이후 자기수정 횟수 | 첫 출력 신뢰도 |
| Output Length Variability | OLV | 다중 실행 간 출력 길이 분산 | 불확실성 수준 |
| Re-query Rate | RQR | 인풋 명확화 요청 비율 | 태스크 명세 불명확도 |

### 3.3 복합 Load Score 산출
- 4개 지표 → 단계별 Load Score (정규화 후 합산 또는 주성분)
- 3회 독립 실행 → 평균 및 분산

### 3.4 프레임워크의 일반성
- 이 메트릭은 도구 실행 로그에서 추출 가능 → 시나리오 플래닝 외 다른 다단계 태스크에 그대로 적용 가능
- 특정 도메인 지식 불필요

---

## 4. 케이스: 시나리오 플래닝 파이프라인 구현

### 4.1 파이프라인 아키텍처 (7단계)

```
Stage 1  STEEP Trend Scanning
         입력: 도메인 지정 / 출력: 계층화된 트렌드 목록 + 출처 태그
         태스크 유형: 생성(Generation-heavy)

Stage 2  Impact-Uncertainty (I-U) Matrix
         입력: 트렌드 목록 / 출력: 페르소나별 I-U 점수 + 핵심 트렌드 선별
         태스크 유형: 판단(Judgment-heavy)

Stage 3  Core Trend Selection (~14개)
         입력: I-U 결과 / 출력: 분기 변수 확정 + 선택 근거
         태스크 유형: 추론(Inference-heavy)

Stage 4  Cross-Impact Analysis + Backbone
         입력: 핵심 트렌드 / 출력: 14×14 매트릭스, 역할 분류, 2×2 축, DAG, CLD
         태스크 유형: 구조적 추론(Structural Inference — 최고 복잡도)

Stage 5  Trend Projection
         입력: 역할 분류 + 축 / 출력: 시나리오별 트렌드 전개 카드
         태스크 유형: 추론 + 생성 혼합

Stage 6  Scenario Narratives
         입력: 백본 + 전개 카드 / 출력: 4개 자기완결 시나리오 + 모니터링 트리거
         태스크 유형: 생성(Generation-heavy)

Stage 7  Decision Mapping
         입력: 시나리오 / 출력: 페르소나별 포트폴리오 매핑 + 실행 가이드
         태스크 유형: 생성 + 구조화
```

### 4.2 Agentic Implementation
- 플랫폼: Cursor (Claude 기반 에이전트)
- 각 단계: 목표 지정 → 에이전트 자율 실행 → 도구 사용(파일 읽기/쓰기, 스크립트 실행)
- Human 역할: 목표 설정 + 단계 간 gate 승인 (orchestration 아님)

### 4.3 케이스 적용 범위
- 도메인: 글로벌 AI 산업 (GenAI 포함), 2025–2030
- 페르소나: 개인 투자자 P1~P3, CVC P4
- 데이터 기반: 공개 보고서 (OECD, Stanford AI Index, Mirae 등)

---

## 5. Results: BLP Framework 적용 결과

### 5.1 단계별 Load Score

```
예상 난이도 분포
──────────────────────────────────────────────
High    │ ██████████ Stage 4 (Cross-impact + Backbone)
        │ ███████    Stage 3 (Core trend selection)
        │
Mid     │ █████      Stage 2 (I-U matrix)
        │ █████      Stage 5 (Trend projection)
        │
Low     │ ███        Stage 7 (Decision mapping)
        │ ██         Stage 1 (STEEP scan)
        │ ██         Stage 6 (Narrative construction)
──────────────────────────────────────────────
```

### 5.2 Stage 4 높은 부하의 구조적 원인
- 196개(14×14) 셀, 모두 상호의존적 판단
- Role classification: Active/Passive 합산 → Driving/Critical/Dependent/Inert — 일관성 필수
- Axis validation: 분류 결과 ↔ 가설 축 일치 검증
- DAG ↔ CLD: 두 표현 간 모순 없어야 함
- **결과**: RC·TCF 지표 모두 최고치 → 에이전트가 반복 수정 집중

### 5.3 Stage 6 낮은 부하의 구조적 원인
- 백본·전개 카드가 구조를 이미 제공 → 채워넣기 태스크
- 내러티브는 정답 기준 없음 → 에이전트가 수정 동기를 갖지 않음
- **결과**: RC·OLV 최저치

### 5.4 핵심 발견: Difficulty Gradient
- **Structural Inference 단계** (Cross-impact, Core trend selection) → 높은 부하
- **Generation 단계** (Narrative, STEEP scan) → 낮은 부하
- 이 패턴은 태스크 유형(Inference vs. Generation)으로 설명 가능
- 도메인 지식이 아닌 **태스크 구조**가 부하를 결정함 → 프레임워크 일반화 가능성 지지

---

## 6. Discussion

### 6.1 Human-in-the-Loop 설계 가이드
BLP 결과를 근거로 한 실용 가이드:

```
High Load 단계 → 인간 개입 필수
  ├─ Stage 4: Cross-impact 수치 검증, 역할 분류 타당성 확인
  └─ Stage 3: 핵심 트렌드 선별 — 도메인 지식으로 보완

Low Load 단계 → 에이전트 위임 가능
  ├─ Stage 1: 완성도 체크 수준으로 충분
  └─ Stage 6: 구조 적합성만 확인
```

### 6.2 기존 방식 대비 전략적 가치
- 속도: 3~6개월 → 수 시간~수일 (접근성 민주화)
- 에이전트 위임 가능 단계: 반복 작업 자동화
- 인간 집중 단계: 전문가 에너지를 구조적 추론에 집중 배치
- 결과: 에이전트 + 인간의 **보완적 분업** 설계 가능

### 6.3 BLP 프레임워크의 다른 MOT 태스크로의 확장 가능성
- 특허 포트폴리오 분석
- 기술 로드맵 수립
- R&D 투자 우선순위 결정
- 각 태스크를 단계 분해 → BLP 적용 → 인간 개입 지점 도출

### 6.4 저자 연구 라인과의 위치
- 논문1: structured prompting → LLM 판단 안정성 (단일 단계, 특허)
- 논문2: 컨텍스트·프레이밍 → 전략 판단 민감도 (단일 단계, 전략)
- 본 논문: 에이전트 행동 프로파일링 → 다단계 태스크 위임 설계 (파이프라인, MOT)
- 세 논문 → **LLM의 고위험 전문 판단 연구 라인**: 단일 단계에서 다단계 자율 파이프라인으로 진화

### 6.5 한계
- 단일 케이스(AI 산업): 다른 기술 도메인 일반화 필요
- Proxy metrics의 간접성: 직접적 추론 비용 측정 불가
- 플랫폼 종속성: Cursor/Claude 기반 — 다른 에이전트 플랫폼 비교 필요

---

## 7. Conclusion

- BLP 프레임워크: LLM 에이전트 단계별 난이도를 측정하는 일반화 가능한 도구 제안
- 시나리오 플래닝 케이스: 가장 복잡한 MOT 태스크에서 프레임워크의 유효성 확인
- 핵심 발견: 태스크 구조(Inference vs. Generation)가 에이전트 부하를 결정 — 도메인 지식 독립적
- 실용 기여: 기술 관리자가 에이전트를 어디에 믿고 어디에 개입할지를 경험적으로 판단할 수 있는 근거 제공
- 향후 연구: 다중 도메인 검증, 모델 간 비교(Claude vs. GPT-4 등), 정량적 부하 지표 정교화

---

## 논문 구성 요약

| 섹션 | 주인공 | 분량 (목표) |
|------|--------|-------------|
| Introduction | 위임 문제 + MOT 선택 근거 | ~2p |
| Related Work | 포지셔닝 | ~3p |
| **BLP Framework** | **핵심 기여 — 프레임워크** | **~3p** |
| Case: Pipeline Design | 스트레스 테스트 설계 | ~3p |
| Results | BLP 적용 결과 + 패턴 | ~4p |
| Discussion | MOT 함의 + 확장 가능성 | ~3p |
| Conclusion | | ~1p |
| **Total** | | **~19p** |

---

## 메모: 다음 단계

- [ ] 실제 에이전트 실행 및 trace 기록 설계 (BLP 지표 로그 형식 정의)
- [ ] 3회 독립 실행 프로토콜 수립
- [ ] Related work 문헌 수집 (ESWA 게재 유사 논문 5~10편)
- [ ] 논문1의 진단 메트릭과 BLP 프레임워크 연결 고리 명확화
- [ ] Stage 4 구조적 원인 분석 심화 (Cross-impact complexity 이론화)
