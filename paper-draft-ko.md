# LLM 에이전트 기반 기술 시나리오 플래닝의 행동 부하 프로파일링: 인간-에이전트 협업 설계를 위한 진단 프레임워크

> 투고 대상 저널: Expert Systems with Applications (ESWA)
> 언어: 한국어 초안 (투고 시 영문 번역 예정)
> 상태: 초안 작성 중

---

## 목차

1. 서론
   - 1.1 연구 배경 및 동기
   - 1.2 연구 공백 및 연구 질문
   - 1.3 연구 기여

2. 선행연구
   - 2.1 기술 시나리오 플래닝의 방법론적 구조
   - 2.2 기업 예측(Corporate Foresight)과 조직 역량
   - 2.3 전략적 예측에서의 AI·LLM 활용
   - 2.4 LLM 에이전트 시스템의 인간 참여(Human-in-the-Loop) 설계

3. 행동 부하 프로파일링(BLP) 프레임워크
   - 3.1 에이전트 부하의 정의
   - 3.2 대리 지표 정의
   - 3.3 복합 부하 점수 산출
   - 3.4 프레임워크의 일반화 가능성

4. 케이스: 기술 예측 시나리오 플래닝 파이프라인
   - 4.1 7단계 파이프라인 설계
   - 4.2 에이전트 기반 구현
   - 4.3 케이스 범위 (AI 산업, 2025–2030)

5. 실험 결과: 단계별 BLP 프로파일
   - 5.1 측정 프로토콜
   - 5.2 단계별 부하 점수 결과
   - 5.3 고부하 단계의 구조적 원인 분석
   - 5.4 주요 발견: 난이도 기울기 패턴

6. 논의
   - 6.1 인간 참여 설계 가이드라인
   - 6.2 기존 전문가 중심 방식과의 비교
   - 6.3 다른 MOT 태스크로의 확장 가능성
   - 6.4 연구 한계

7. 결론

참고문헌

---

## 1. 서론

### 1.1 연구 배경 및 동기

기술 시나리오 플래닝은 핵심 동인 간 상호작용을 분석하고 대안적 미래를 구성함으로써 조직이 깊은 불확실성 속에서도 전략적 판단을 내릴 수 있도록 지원한다(Schoemaker, 1995). 체계적인 예측 역량을 보유한 기업은 경쟁사 대비 수익성에서 최대 33%, 성장률에서 최대 200% 높은 성과를 달성한다는 실증 결과는 그 전략적 가치를 뒷받침한다(Rohrbeck and Kum, 2018). 그러나 현존하는 23가지 시나리오 개발 기법 모두가 전문가 워크숍과 도메인 지식을 전제로 하며(Bishop et al., 2007), 방법론이 정교할수록 실행에 필요한 조직 역량도 커지는 구조적 병목이 존재한다(Rohrbeck, 2010).

LLM 기반 자율 에이전트는 이 병목을 완화할 가능성을 제시한다. 도구 사용과 자기 검토 능력을 갖춘 에이전트는 최소한의 인간 조율로 복잡한 분석 파이프라인을 실행할 수 있다. 그러나 다단계 워크플로우에서 어느 단계를 에이전트에 안전하게 위임하고 어느 단계에서 인간 감독이 필요한지는 아직 경험적으로 규명되지 않았다. 잘못된 단계를 위임하면 오류가 후속 단계로 연쇄되고, 모든 단계를 인간이 검토하면 자동화의 효율이 사라진다.

### 1.2 연구 공백 및 연구 질문

기존 연구는 LLM을 전략적 분석의 단일 단계 태스크—특허 평가(Choi and Park, 2026), 전략 내러티브 생성(Rohrbeck et al., forthcoming)—에 적용하는 데 집중해 왔다. 복잡한 MOT 태스크의 전체 파이프라인에 걸쳐 에이전트 행동을 분석하고, 단계별 태스크 난이도를 특성화하는 프레임워크를 제안한 연구는 아직 없다. 기업 예측 연구 역시 AI 통합의 필요성을 강조하면서도(Fergnani, 2022) 다단계 워크플로우 내 인간-에이전트 경계 설계에 대한 구체적 지침을 제공하지 못하고 있다.

본 연구는 이 공백을 메우기 위해 다음 세 가지 연구 질문을 설정한다.

- **RQ1**: LLM 에이전트 기반 분석 파이프라인에서 단계별 태스크 난이도를 관찰 가능한 행동 대리 지표로 어떻게 특성화할 수 있는가?
- **RQ2**: 기술 시나리오 플래닝 파이프라인에 이 프레임워크를 적용했을 때 어떤 난이도 기울기(difficulty gradient)가 나타나는가?
- **RQ3**: 관찰된 난이도 패턴의 구조적 원인은 무엇이며, 인간 참여 거버넌스 설계에 어떤 함의를 주는가?

### 1.3 연구 기여

1. **행동 부하 프로파일링(BLP) 프레임워크**: 에이전트 상호작용 흔적에서 도출 가능한 네 가지 대리 지표를 활용한 단계별 태스크 난이도 진단 도구.
2. **극한 사례 실증**: MOT 태스크 중 구조적 복잡도가 높은 기술 시나리오 플래닝을 의도적 검증 사례로 삼아 프레임워크의 유효성 확인.
3. **거버넌스 가이드**: 에이전트 위임 가능 단계와 인간 판단 집중 단계를 경험적으로 구분하고, 다른 MOT 워크플로우로의 일반화 지침 제시.

---

## 2. 선행연구

### 2.1 기술 시나리오 플래닝의 방법론적 구조

Schoemaker(1995)의 10단계 프레임워크—범위 정의, 트렌드 식별, 핵심 불확실성 파악, 시나리오 구성, 의사결정 시나리오 발전—는 이 분야의 표준적 구조적 프로세스로 자리잡고 있다. 이와 병행하여 Godet(1986)의 MICMAC 방법론은 변수를 능동·수동 영향 점수로 분류해 Driving, Critical, Dependent, Inert 네 역할군을 도출하고, 이를 2×2 시나리오 백본의 축 선택에 활용한다. 정량적 기반이 재현 가능성을 높이는 반면, 14개 변수 분석 기준 196쌍의 평가가 필요해 전문가 의존도는 여전히 높다.

Bradfield et al.(2005)은 세 학파—직관적 논리, 프랑스 *prospective*, 확률론적 접근—의 발전 과정을 종합하며, 공통된 평가 기준이 없는 "방법론적 혼란"을 지적한다. 이는 각 방법론이 고도의 전문 인력을 요구한다는 점에서 비롯된 필연적 결과이기도 하다.

### 2.2 기업 예측(Corporate Foresight)과 조직 역량

Rohrbeck(2010)의 성숙도 모델은 조직이 불연속적 변화에 대응하는 미래 지향성을 다섯 가지 차원으로 측정한다. 예측 역량의 성과 효과는 실증적으로 확인된다: 예측 역량이 높은 기업은 동종 업계 대비 수익성 33%·성장률 200% 우위를 달성하는 반면, 역량이 부족한 기업은 37~108%의 성과 할인을 경험한다(Rohrbeck and Kum, 2018).

Fergnani(2022)는 이를 동적 역량 프레임워크 안에서 재정의하며, 예측 수행 능력 자체가 기업 수준의 경쟁 우위 원천임을 주장한다. Gavetti and Menon(2016)은 전략적 예측을 에이전시의 관점에서 이론화하며, 규율 있는 예측이 제한된 조건 내에서 재현 가능함을 보인다. 이들의 에이전시 개념은 LLM 에이전트를 예측 행위자로 위치시키는 이론적 토대가 된다.

### 2.3 전략적 예측에서의 AI·LLM 활용

Rohrbeck et al.(forthcoming)은 Siemens 사례를 통해 AI-인간 협업 모델이 예측 프로세스 소요 시간 20%, 자원 활용 25%, 전문가 투입 시간 50%를 절감하면서 분석 품질을 30% 향상시켰음을 보고한다. 이 연구의 핵심 교훈은 성공적 AI 통합이 기존 워크플로우에 AI를 삽입하는 것이 아니라 프로세스 자체를 재설계하는 데 달려 있다는 것이다.

LLM의 구조화된 판단 태스크 적용 측면에서, Choi and Park(2026)은 구조화된 프롬프팅 프레임워크가 특허 평가에서 LLM 판단의 일관성과 해석 가능성을 향상시킴을 보인다. 이는 LLM이 단순한 텍스트 생성을 넘어 구조화된 전문가 판단의 대리자로 기능할 수 있음을 시사한다. 단, LLM의 출력이 태스크 구조와 도메인에 따라 달라진다는 점에서, 각 단계의 구조적 요구가 크게 다른 시나리오 플래닝 워크플로우에서 에이전트 행동 역시 단계 간 차이를 보일 것으로 예상된다.

### 2.4 LLM 에이전트 시스템의 인간 참여(Human-in-the-Loop) 설계

다단계 투명 워크플로우 연구(arXiv:2501.10909)는 AI 추론이 오류에 취약한 환경에서 구조화된 인간 체크포인트가 단일 단계 협업보다 우수하며, 전체적인 검토보다 고위험 단계를 겨냥한 세분화된 감독이 더 효과적임을 보인다. 계층적 위임 프레임워크(arXiv:2506.11887) 또한 태스크 복잡도에 따라 적응적으로 위임 범위를 조정할 것을 제안한다.

이 연구들의 공통된 원칙은 인간-AI 분담이 워크플로우 전체가 아닌 단계 수준에서 설계되어야 한다는 것이다. 본 연구는 이 원칙을 계승하되, 개입이 필요한 단계를 식별하는 수단으로 정답 기준 측정 대신 에이전트의 관찰 가능한 행동 대리 지표를 활용한다. 이 접근법은 표준 참조 출력이 없는 개방형 분석 도메인—시나리오 플래닝이 대표적 사례—에 특히 적합하다.

---

## 참고문헌

Bradfield, R., Wright, G., Burt, G., Cairns, G. and Van der Heijden, K. (2005). The origins and evolution of scenario techniques in long range business planning. *Futures*, 37(8), pp.795–812. https://doi.org/10.1016/j.futures.2005.01.003

Bishop, P., Hines, A. and Collins, T. (2007). The current state of scenario development: an overview of techniques. *Foresight*, 9(1), pp.5–25. https://doi.org/10.1108/14636680710727516

Choi, D. and Park, B. (2026). Structured LLM-based patent comparison across three evaluation dimensions. *World Patent Information*, 102430. https://doi.org/10.1016/j.wpi.2026.102430

Fergnani, A. (2022). Corporate foresight: A new frontier for strategy and management. *Academy of Management Perspectives*, 36(2), pp.820–844. https://doi.org/10.5465/amp.2018.0178

Gavetti, G. and Menon, A. (2016). Evolution cum agency: Toward a model of strategic foresight. *Strategy Science*, 1(3), pp.207–233. https://doi.org/10.1287/stsc.2016.0018

Godet, M. (1986). Introduction to *la prospective*: Seven key ideas and one scenario method. *Futures*, 18(2), pp.134–157. https://doi.org/10.1016/0016-3287(86)90094-7

Rohrbeck, R. (2010). Towards a maturity model for organizational future orientation. *Academy of Management Proceedings*, 2010(1), pp.1–6. https://doi.org/10.5465/AMBPP.2010.54493637

Rohrbeck, R. and Kum, M.E. (2018). Corporate foresight and its impact on firm performance: A longitudinal analysis. *Technological Forecasting and Social Change*, 129, pp.105–116. https://doi.org/10.1016/j.techfore.2017.12.013

Rohrbeck, R., Szuppa, S. and Schmidt, J. (forthcoming). Artificial intelligence in strategic foresight: The case of Siemens Professional Education. [⚠ SSRN 5636869 — 저자 직접 접근 확인 필요]

Schoemaker, P.J.H. (1995). Scenario planning: A tool for strategic thinking. *Sloan Management Review*, 36(2), pp.25–40. https://sloanreview.mit.edu/article/scenario-planning-a-tool-for-strategic-thinking/

---

> **[⚠] 확인 필요 항목**
> - **Rohrbeck et al. (forthcoming)**: https://ssrn.com/abstract=5636869 에서 직접 확인 필요
> - **2.4절 arXiv 논문 2편**: ESWA 투고 시 저널 게재 여부 확인 후 인용 권장
