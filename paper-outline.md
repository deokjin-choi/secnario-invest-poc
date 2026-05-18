# When to Trust the Agent: Task Difficulty Profiling in LLM-Driven Technology Scenario Planning

> Draft outline — ESWA submission target
> Author: Deokjin Choi (et al.)
> Date: 2026-05

---

## Abstract (초안)

Technology scenario planning is a critical tool for R&D and innovation management, yet it remains largely expert-dependent, time-intensive, and difficult to systematize. This study proposes an LLM agent-based system that automates the full scenario planning pipeline—from STEEP trend analysis to investment-oriented scenario narratives—and introduces a behavioral load profiling framework to characterize where the agent reliably operates and where it struggles. Using proxy metrics derived from agent interaction traces (tool call frequency, revision count, output variability, re-query patterns), we profile task difficulty across seven pipeline stages applied to an AI industry foresight case. Results reveal a consistent difficulty gradient: structural inference tasks (e.g., cross-impact role classification, axis validation) impose significantly higher agent load than generative tasks (e.g., narrative construction). These findings provide technology managers with an empirically grounded guide for designing human-in-the-loop oversight in LLM-assisted foresight systems.

**Keywords**: LLM agent, technology foresight, scenario planning, behavioral profiling, human-AI collaboration, management of technology

---

## 1. Introduction

### 1.1 Problem
- 전통적 시나리오 플래닝: 전문가 워크숍 중심, 3~6개월 소요, 대기업·대형 컨설팅에만 접근 가능
- 분석과 의사결정의 단절: foresight 결과가 실행 계획으로 연결되지 못하는 구조적 문제
- AI 환경 가속화: 기술 환경 변화 속도 대비 foresight 사이클이 너무 느림

### 1.2 Opportunity
- LLM 에이전트: 구조화된 다단계 분석을 자율적으로 실행 가능
- 속도·접근성: 수 시간 내 완성, 소규모 조직도 활용 가능
- 그러나: 어느 단계를 에이전트에 맡겨도 되는지, 어디에 인간 개입이 필요한지 알 수 없음

### 1.3 Research Questions
- **RQ1**: LLM 에이전트를 사용해 전체 시나리오 플래닝 파이프라인을 자동화할 수 있는가?
- **RQ2**: 에이전트의 행동 패턴(부하 지표)은 단계별로 어떻게 다른가?
- **RQ3**: 그 차이는 무엇으로 설명되며, 인간 개입 설계에 어떤 함의를 주는가?

### 1.4 Contributions
1. LLM 에이전트 기반 기술예측 시나리오 플래닝 시스템 설계 및 구현
2. 에이전트 행동 부하 프로파일링 프레임워크 (proxy metrics 정의)
3. 단계별 태스크 난이도 맵 — 인간-AI 협업 설계를 위한 실증 가이드

---

## 2. Related Work

### 2.1 Technology Scenario Planning Methodology
- STEEP 프레임워크, Impact-Uncertainty 매트릭스
- Cross-impact analysis (Gordona et al.)
- 2×2 시나리오 백본 및 내러티브 구조
- 한계: 전문가 의존성, 재현 불가, 감사 불가

### 2.2 LLMs in Strategic Decision Support
- LLM as decision agent (논문2 연결)
- Structured prompting for analytical tasks (논문1 연결)
- 기존 foresight 자동화 연구의 한계 (단일 단계 자동화, 전체 파이프라인 부재)

### 2.3 Agent Behavioral Analysis
- Cognitive load in AI systems
- Task difficulty characterization in multi-step LLM tasks
- Human-in-the-loop 설계 원칙

---

## 3. System Design

### 3.1 Pipeline Architecture
7단계 파이프라인 — 각 단계는 독립적 에이전트 태스크로 구성

```
Stage 1: STEEP Trend Scanning
    └─ 입력: 도메인 지정 / 출력: 계층화된 트렌드 목록 + 출처 태그

Stage 2: Impact-Uncertainty (I-U) Matrix
    └─ 입력: 트렌드 목록 / 출력: 페르소나별 I-U 점수 + 핵심 트렌드 선별

Stage 3: Core Trend Selection (~14개)
    └─ 입력: I-U 결과 / 출력: 분기 변수 확정 + 선택 근거

Stage 4: Cross-Impact Analysis + Backbone
    └─ 입력: 핵심 트렌드 / 출력: 14×14 매트릭스, 역할 분류, 2×2 축, DAG, CLD

Stage 5: Trend Projection
    └─ 입력: 역할 분류 + 축 / 출력: 시나리오별 트렌드 전개 카드

Stage 6: Scenario Narratives
    └─ 입력: 백본 + 전개 카드 / 출력: 4개 자기완결 시나리오 + 모니터링 트리거

Stage 7: Decision Mapping
    └─ 입력: 시나리오 / 출력: 페르소나별 포트폴리오 매핑 + 실행 가이드
```

### 3.2 Agentic Implementation
- 플랫폼: Cursor (Claude 기반)
- 각 단계: 목표 지정 → 에이전트 자율 실행 → 도구 사용 (파일 읽기/쓰기, 스크립트 실행)
- 단계 간 연결: 이전 단계 출력이 다음 단계의 컨텍스트로 자동 투입
- 기존 POC(this repo)와의 관계: 동일 케이스, 에이전트 모드로 재실행

### 3.3 Prompt Governance
- 프롬프트 버전 관리 (소스 코드와 동일하게 취급)
- 각 단계별 평가 기준(rubric) 내재화
- 논문1의 structured prompting 원칙 적용

---

## 4. Behavioral Load Profiling Framework

### 4.1 Agent "Load"의 정의
에이전트가 특정 단계 태스크를 완료하기까지 소비한 인지적 노력의 대리 지표.
수치 해석의 잔차(residual)와 달리, 자연어 추론 에이전트의 부하는 **행동 패턴**으로 간접 측정.

### 4.2 Proxy Metrics

| 지표 | 측정 방법 | 의미 |
|------|-----------|------|
| **Tool Call Frequency (TCF)** | 단계당 도구 호출 횟수 | 확인·검색 필요성 |
| **Revision Count (RC)** | 초기 출력 이후 수정 횟수 | 첫 출력 신뢰도 |
| **Output Length Variability (OLV)** | 다중 실행 간 출력 길이 분산 | 불확실성 수준 |
| **Re-query Rate (RQR)** | 인풋 재요청 또는 명확화 요청 비율 | 태스크 명세 불명확도 |

### 4.3 Load Profile 산출
- 3회 독립 실행 (동일 케이스, 동일 프롬프트)
- 단계별 4개 지표 → 복합 Load Score
- 시각화: 단계 × 부하 지표 히트맵

---

## 5. Case Application: AI Industry Technology Foresight (2025–2030)

### 5.1 Case Overview
- 도메인: 글로벌 AI 산업 (GenAI 포함)
- 시간 지평: 3~7년
- 페르소나: 개인 투자자 P1~P3, CVC P4
- 데이터: 공개 보고서 기반 (OECD, Stanford AI Index, Mirae 등)

### 5.2 System Execution
- 7단계 전체 에이전트 실행 기록
- 핵심 출력: 14개 핵심 트렌드, 4개 시나리오 (AI Democracy / AI Fortress / AI Fracture / AI Stagnation 유형)
- 모니터링 트리거 및 포트폴리오 매핑 포함

---

## 6. Results: Stage-Wise Load Profile

### 6.1 Load Profile 결과 (예상 패턴)

```
예상 난이도 분포
─────────────────────────────────────────────
High Load  │ Stage 4 (Cross-impact + Backbone)
           │ Stage 3 (Core trend selection)
           │
Mid Load   │ Stage 2 (I-U matrix)
           │ Stage 5 (Trend projection)
           │
Low Load   │ Stage 1 (STEEP scan)
           │ Stage 6 (Narrative construction)
           │ Stage 7 (Decision mapping)
─────────────────────────────────────────────
```

### 6.2 Stage 4의 높은 부하 이유 (구조 분석)
- Cross-impact: 14×14 = 196개 셀, 상호 의존적 판단
- Role classification: Active/Passive sum → Driving/Critical/Dependent/Inert 분류 — 논리적 일관성 필요
- Axis validation: 분류 결과가 기존 가설 축과 일치하는지 검증
- DAG + CLD: 두 표현 간 모순 없어야 함 → 에이전트가 반복 수정 집중

### 6.3 Stage 6의 낮은 부하 이유
- 백본과 전개 카드가 구조를 이미 제공 → 에이전트가 채워넣기만 함
- 내러티브는 정답 기준이 없어 에이전트가 수정 동기를 갖지 않음

### 6.4 함의: "Difficulty Gradient" 패턴
- **추론 집약 단계** (구조 도출, 분류, 검증) → 높은 부하
- **생성 집약 단계** (내러티브, 스캔) → 낮은 부하
- 이 패턴은 태스크 유형에 의해 설명됨 (Inference-heavy vs. Generation-heavy)

---

## 7. Discussion

### 7.1 Human-in-the-Loop 설계 가이드
부하 프로파일을 근거로, 기술 관리자가 어디에 인간 개입을 집중해야 하는지 제시.

```
High Load 단계 → 에이전트 출력 반드시 검토
  ├─ Stage 4: Cross-impact 매트릭스 수치 검증
  └─ Stage 3: 핵심 트렌드 선별 타당성 확인

Low Load 단계 → 에이전트에 위임 가능
  ├─ Stage 1: STEEP 스캔 (completeness 정도만 확인)
  └─ Stage 6: 내러티브 초안 (구조 적합성만 확인)
```

### 7.2 기존 방식 대비 효율성
- 전통 워크숍: 3~6개월, 다수 전문가 필요
- 이 시스템: 수 시간~수일, 1인 분석가 가능
- 단, 대체가 아닌 증강(augmentation): 에이전트 부하 높은 단계는 여전히 전문가 판단 필요

### 7.3 논문1·2와의 연결
- 논문1: structured prompting → 안정적 판단 (특허 비교 도메인)
- 논문2: 컨텍스트·프레이밍 → 전략 판단 민감도
- 이 논문: 다단계 에이전트 태스크에서 **어느 단계가 구조적으로 어려운가**
- 세 논문이 "LLM의 고위험 전문 판단" 연구 라인을 형성

### 7.4 한계
- 단일 케이스 (AI 산업): 다른 기술 도메인 일반화 필요
- Proxy metrics의 한계: 직접적 추론 비용 측정 불가
- 에이전트 플랫폼 종속성 (Cursor/Claude)

---

## 8. Conclusion

- LLM 에이전트가 전체 시나리오 플래닝 파이프라인을 실행 가능함을 실증
- 단계별 부하 프로파일이 일관된 난이도 패턴을 보임: 구조적 추론 > 생성 태스크
- 기술 관리자에게 실용적 함의: 에이전트 위임 가능 단계와 인간 개입 필수 단계의 구분
- 향후 연구: 다중 도메인 검증, 모델 간 비교, 정량적 부하 지표 정교화

---

## 논문 구성 요약

| 섹션 | 핵심 기여 | 분량 (목표) |
|------|-----------|-------------|
| Introduction | RQ 설정, 동기 | ~2p |
| Related Work | 포지셔닝 | ~3p |
| System Design | 아키텍처 기여 | ~4p |
| Load Framework | 메트릭 정의 기여 | ~2p |
| Case Application | 실증 케이스 | ~3p |
| Results | 핵심 발견 | ~4p |
| Discussion | MOT 함의 | ~3p |
| Conclusion | | ~1p |
| **Total** | | **~22p** |

---

## 메모: 다음 단계

- [ ] 실제 에이전트 실행 및 trace 기록 설계
- [ ] Proxy metrics 측정 방법 구체화 (로그 형식 정의)
- [ ] Related work 문헌 수집 (ESWA 게재 유사 논문 5~10편)
- [ ] 논문1 메트릭과의 연결 고리 명확화
