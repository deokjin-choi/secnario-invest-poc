# 논문 요약 (Paper Summary)

이 폴더의 PDF 논문·자료에 대한 간단한 요약입니다.

---

## 목차 (총 18개 파일)

1. [LLM + 전략·의사결정](#llm--전략의사결정)
2. [인지 편향·편향 완화](#인지-편향편향-완화)
3. [LLM 추론·전략 선택](#llm-추론전략-선택)
4. [의사결정·구조화된 설명](#의사결정구조화된-설명)
5. [맥락·프레임·번역](#맥락프레임번역)
6. [도메인별 활용](#도메인별-활용)
7. [벤치마크·오염](#벤치마크오염)

---

## LLM + 전략·의사결정

| 파일명 | 주요 내용 |
|--------|-----------|
| **Discovering Differences in Strategic Behavior.pdf** | 인간 vs LLM의 전략적 행동 차이. AlphaEvolve로 데이터에서 해석 가능한 모델 발견. 반복 가위바위보 등에서 LLM이 인간보다 더 깊은 전략을 보일 수 있음. |
| **Game Theory Meets Large Language Models.pdf** | 게임이론과 LLM 교차점: (1) 게임 기반 벤치마크, (2) 게임이론적 알고리즘/훈련, (3) 사회적 영향 모델링. |
| **Human-guided collective LLM intelligence for strategic planning.pdf** | CIAIC: 인간 가이드 + 집단 AI 컨설턴트 협업으로 전략 수립. 5단계(목표 정의→검색 기반 초안→멀티에이전트 보완→집단 수정→다시점 전략 보고서). PESTEL/SWOT 분석 실험. |
| **Strategic Demonstration Selection for Improved.pdf** | ICL 데모 선택이 fairness에 미치는 영향. 소수 그룹 샘플을 의도적으로 포함하면 fairness 향상. |

---

## 인지 편향·편향 완화

| 파일명 | 주요 내용 |
|--------|-----------|
| **Cognitive Bias in Decision-Making with LLMs.pdf** | BIAS BUSTER: LLM 인지 편향 탐지·평가·완화. 13,465개 프롬프트로 Anchoring, Status Quo, Framing 등 테스트. 자기 인식 기반 디바이어싱 제안. |
| **cheung-et-al-2025-large-language-models-show-amplified-cognitive-biases-in-moral-decision-making.pdf** | LLM의 도덕적 의사결정 편향. omission bias, "no" 응답 편향 등 인간 대비 더 강함. Fine-tuning이 원인일 가능성. |
| **kdd_paper_prompt_bias.pdf** | System prompt가 LLM 편향 유발 메커니즘. 50개 인구학 그룹, system vs user prompt 차이. AI 감사에 system prompt 분석 필요성. |

---

## LLM 추론·전략 선택

| 파일명 | 주요 내용 |
|--------|-----------|
| **Adaptive-solver framework for dynamic strategy selection in large language model reasoning.pdf** | 문제 난이도에 맞춰 추론 전략을 동적으로 선택. API 비용 85% 절감 또는 동일 비용에서 성능 향상. |
| **Route-to-Reason.pdf** | LM과 추론 전략을 동시에 라우팅. "과잉 추론" 방지, 토큰 사용 60% 이상 절감. |

---

## 의사결정·구조화된 설명

| 파일명 | 주요 내용 |
|--------|-----------|
| **An LLM for Decision-Making with Structured Explanations.pdf** | STRUX: 호·악 facts를 구조화된 테이블로 정리, 핵심 facts 판별·우선순위화. 이어닝스 콜 기반 투자 의사결정에 활용. |
| **LLMs on interactive feature collections with implicit dynamic decision strategy.pdf** | 20질문·의료·비즈니스 진단 등에서 질문 순서와 내용을 동적으로 조정. CoT·Plan-and-Solve 한계 분석. |
| **llm as virtual expert.pdf** | 태양광 발전소 입지 선정에서 LLM을 AHP 가상 전문가로 사용. 전문가와 높은 상관(约 r=0.838), 특정 기준에 대한 편향 존재. |

---

## 맥락·프레임·번역

| 파일명 | 주요 내용 |
|--------|-----------|
| **Do LLMs Encode Frame Semantics.pdf** | LLM이 FrameNet 기반 frame semantics를 내재적으로 학습했는지 검증. 프롬프팅·Fine-tuning으로 frame identification 수행. |
| **Exploring Context Strategies in LLMs for Discourse-Aware Machine Translation.pdf** | 맥락이 LLM 기계번역 품질에 미치는 영향. 이전 문장·모델 가설·참조 번역 조합이 담화 일관성(formality, 대명사 등) 향상에 기여. |

---

## 도메인별 활용

| 파일명 | 주요 내용 |
|--------|-----------|
| **Enhancing LLM Performance in Asset Selection.pdf** | 자산 선택에서 전통 정량 신호와 LLM 통합 시의 과제와 접근법. |
| **LLM-MANUF_An integrated framework of Fine-Tuning large language models for intelligent Decision-Making in manufacturing.pdf** | 제조 의사결정용 LLM Fine-tuning 통합 프레임워크. 여러 LLM의 예비안 생성→DWMOE 랭킹→최종 결합. |
| **Large Language Models for Manufacturing(백서느낌).pdf** | 제조 영역 전반의 LLM 활용 백서 (설계, 품질, 공급망, 로봇 제어, 교육, 메타버스 등). |
| **using llms for market research(하바드).pdf** | 시장 조사에 LLM 활용 (Harvard/Microsoft). LLM 응답 분포를 활용한 소비자 선호 추정 방법론. |

---

## 벤치마크·오염

| 파일명 | 주요 내용 |
|--------|-----------|
| **Rethinking Benchmark and Contamination for Language Models.pdf** | MMLU·HumanEval 등 벤치마크 오염 문제. n-gram 제거만으로는 부족, LLM 기반 디컨테이미네이션 및 신규 시험 필요성 제안. |

---

## 프로젝트 관련성

- **Brand Bias**: Cognitive Bias, kdd_paper_prompt_bias
- **Context Dependency**: Exploring Context Strategies, LLMs on interactive feature collections
- **전략적 의사결정**: Discovering Differences in Strategic Behavior, Game Theory, Human-guided collective intelligence
- **Framing**: Do LLMs Encode Frame Semantics, Cognitive Bias
