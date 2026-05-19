# Elsevier LLM-Decision 연구 노트

- 원본: `references/elsvier_llm_decision.bib`
- 총 논문 수: **100**
- 분류 원칙: 논문을 "LLM이 전략적 의사결정 프로세스의 어느 지점을 혁신하는가" 기준으로 **중복 없이 1개 그룹**에 배치함.
- 정렬 원칙: **그룹 크기 내림차순**.

## 그룹별 개수


| 그룹명                     | 논문 수 | 전략적 의사결정 관점의 의미                                         |
| ----------------------- | ---- | ------------------------------------------------------- |
| 운영 전략 실행의 자동화와 실시간 재계획  | 21   | 복잡한 물리적 환경에서 LLM/에이전트가 계획·스케줄링·배치·제어 결정을 실시간으로 바꾸는 연구   |
| 임상·바이오 의사결정의 구조화와 고도화   | 16   | 의료 판단을 더 일관되고 설명가능하며 단계적으로 만드는 연구                       |
| 신뢰 가능한 고위험 의사결정과 리스크 통제 | 16   | 할루시네이션·안전성·검증·이상탐지·플랫폼 위험을 통제해 의사결정 실패를 줄이는 연구          |
| 지식 접지형 의사결정 인프라 구축      | 14   | KG/RAG/온톨로지/정책 문서/SQL 인터페이스를 통해 의사결정에 필요한 근거 체계를 만드는 연구 |
| 시장·사회·금융 전략 인텔리전스       | 12   | 시장 신호, 금융 판단, 여론 변화, 전략적 인사이트 추출을 LLM으로 고도화하는 연구        |
| 의사결정 절차 자체의 설계와 평가      | 11   | 계획, 추론, 벤치마킹, 평가, 불확실성 반영 등 "결정하는 방식" 자체를 개선하는 연구       |
| 인간·전문가·조직과의 협업 설계       | 10   | 전문가·사용자·조직과 LLM의 역할 분담, 합의, 설명, 시민 참여를 설계하는 연구          |


---

## 운영 전략 실행의 자동화와 실시간 재계획

### MASC: Large language model-based multi-agent scheduling chain for flexible job shop scheduling problem

- **연구의 본질적 가치:** 제조 스케줄링을 단순 최적화가 아니라 현장 교란에 반응하는 대화형 의사결정 체인으로 바꾸며, LLM이 "재계획 능력"을 운영 경쟁력으로 전환할 수 있음을 보여준다.

### LLM-MANUF: An integrated framework of Fine-Tuning large language models for intelligent Decision-Making in manufacturing

- **연구의 본질적 가치:** 여러 후보 결정을 병렬 생성하고 다시 랭킹·융합하는 구조를 통해, 제조 의사결정에서 중요한 것은 "단일 정답 생성"보다 "후보안 경쟁과 통합"임을 보여준다.

### Intelligent port logistics: A spatiotemporal knowledge graph and AI-agent framework for berth allocation

- **연구의 본질적 가치:** 항만 배정 문제를 시공간 상호작용을 읽는 지식·에이전트 문제로 재구성함으로써, LLM이 자원 배분 전략의 병목을 줄이는 운영 두뇌로 작동할 수 있음을 제시한다.

### A multi-agent LLM framework for severity classification of complaint events: Probabilistic reasoning with scene uncertainty

- **연구의 본질적 가치:** 자동차 불만 데이터를 단순 분류가 아니라 불확실성 하의 위험판단 문제로 다루며, 규제·품질·소비자 보호 의사결정을 조기화하는 틀을 만든다.

### Large language model-empowered dynamic scheduling for intelligent hybrid flow shop using multi-agent deep reinforcement learning

- **연구의 본질적 가치:** LLM을 RL 위에 얹는 것이 아니라 상태 이해와 행동 선택을 의미적으로 보강하는 방식으로 결합해, 공장 운영 전략의 적응성을 높인다.

### Robust mobile robot path planning via LLM-based dynamic waypoint generation

- **연구의 본질적 가치:** LLM을 자연어 해석기에 머물게 하지 않고 경로 중간의 의사결정 지점을 생성하는 상위 계획자로 사용해, 로봇의 현장 대응력을 끌어올린다.

### Large language model based system with causal inference and Chain-of-Thoughts reasoning for traffic scene risk assessment

- **연구의 본질적 가치:** 자율주행 위험평가를 "장면 이해"에서 끝내지 않고 인과 사슬을 따라 단계적으로 검토하게 만들어, 차량 의사결정의 안전 근거를 강화한다.

### A LLM-informed multi-agent AI system for drone-based visual inspection for infrastructure

- **연구의 본질적 가치:** 인프라 점검을 여러 기능적 하위 에이전트의 협업 문제로 재설계해, LLM이 공간 추론과 작업 분할을 통해 현장 운영의 자동화를 이끈다는 점을 보여준다.

### CCMA: A framework for cascading cooperative multi-agent in autonomous driving merging using Large Language Models

- **연구의 본질적 가치:** 자율주행 합류 상황에서 개별 차량 최적화가 아니라 다차원 협력 전략을 설계해, 인간다운 교통 의사결정을 시스템 수준에서 복원하려는 시도다.

### Integrating adaptive divide-and-conquer and large language model for scheduling large-scale tasks in electromagnetic satellite systems

- **연구의 본질적 가치:** 대규모 조합 최적화 문제에서 LLM을 해답 생성기가 아니라 탐색 품질을 높이는 보조 지능으로 배치해, 전략적 스케줄링의 수렴 속도와 품질을 동시에 높인다.

### An LLM-based knowledge and function-augmented approach for optimal design of remanufacturing process

- **연구의 본질적 가치:** 복수 목표를 가진 공정 설계를 지식 검색과 함수 계산의 결합 문제로 풀어, LLM이 설계자의 판단 부담을 줄이는 상위 의사결정 도구가 될 수 있음을 입증한다.

### Water Membrane-Based Desalination Modeling Using a Ninja Optimization–Enhanced Bidirectional Long Short-Term Memory with Conceptually LLM-Informed Data Preparation

- **연구의 본질적 가치:** LLM을 직접 예측기가 아니라 데이터 준비 의사결정의 개념 설계자 역할로 제한적으로 활용해, 전략적 파이프라인 설계에서 어디까지 LLM을 써야 하는지 경계를 보여준다.

### A Large language model-based multi-agent manufacturing system for intelligent shopfloors

- **연구의 본질적 가치:** 사전학습 없이도 현장 정보를 해석해 설비 선택 결정을 내리는 구조를 제안함으로써, 공장 운영 의사결정을 더 유연한 협상형 시스템으로 전환한다.

### BearGen: LLM-guided signal generation framework for bearing fault diagnosis

- **연구의 본질적 가치:** 희소하고 민감한 산업 신호 데이터를 생성 가능 자산으로 바꾸어, 실제 의사결정 시스템 구축을 가로막는 데이터 부족 문제를 우회한다.

### A decision-making framework by large language model for green tide salvage ship scheduling

- **연구의 본질적 가치:** 해양 재난 대응 스케줄링을 다중 에이전트 집단 의사결정으로 바꾸어, 환경 위기 대응 전략에서 LLM의 현장 적용 가능성을 보여준다.

### Knowledge-aware cell formation in matrix-structured manufacturing systems via large and small model synergistic methods

- **연구의 본질적 가치:** 생산 셀 구성 결정을 의미적 지식과 물리 제약의 동시 최적화 문제로 다뤄, 제조전략 설계에서 "구조화된 지식 + 최적화"의 결합 가치를 증명한다.

### Large language model-enhanced graph neural network for quantile prediction of railway track settlement near deep excavations

- **연구의 본질적 가치:** 텍스트 로그와 센서 데이터를 결합해 불확실성까지 예측함으로써, 토목 인프라 의사결정을 평균 예측이 아닌 위험구간 관리 중심으로 바꾸게 한다.

### LLM-Guided risk-sensitive reinforcement learning for smart factories in the scenario of human-robot symbiosis

- **연구의 본질적 가치:** 스마트팩토리에서 LLM을 위험 민감형 RL의 상위 지침 엔진으로 써서, 안전성과 생산성을 함께 추구하는 운영전략의 가능성을 제시한다.

### LLM-augmented hierarchical reinforcement learning for human-like decision-making of autonomous driving

- **연구의 본질적 가치:** LLM을 인간 운전자 같은 상위 목표 생성자에 두어, 자율주행 의사결정을 더 설명가능하고 인간 가치 정렬적인 형태로 발전시킨다.

### Decision support for in-operation monitoring of the WEST tokamak first wall using multimodal large language model (LLM) on infrared imaging

- **연구의 본질적 가치:** 고위험 실험시설의 운영 모니터링에서 LLM을 현장 전문가 보조자로 배치해, 빠른 해석과 사후 판단의 품질을 높이는 방향을 제시한다.

### R2D-EQ: a two-stage workflow for risk reasoning and decision-making in earthquake emergency scenarios

- **연구의 본질적 가치:** 재난 의사결정을 "위험 인식"과 "행동 생성"의 두 단계로 분리해, 실제 대응 시스템에서 LLM이 어떤 식으로 구조화되어야 하는지 보여준다.

---

## 임상·바이오 의사결정의 구조화와 고도화

### Explainable medical visual question answering via chain of evidence

- **연구의 본질적 가치:** 의료 VQA를 정답 생성 문제가 아니라 근거 생성 문제로 바꿔, 임상 의사결정에서 설명가능성이 성능만큼 중요하다는 점을 제도화한다.

### CDAFlow: Enhancing LLM clinical decision-making through agentic workflow

- **연구의 본질적 가치:** 임상 판단을 상태전이, 지식 필터링, 메모리 관리로 분해해, LLM을 의료현장의 실제 워크플로에 맞는 의사결정 엔진으로 재설계한다.

### LLMs For drug-Drug interaction prediction using textual drug descriptors

- **연구의 본질적 가치:** 구조화 화학 정보 없이도 자유 텍스트 기반으로 약물 상호작용을 예측해, 의사결정 지원의 진입 장벽을 낮추는 실용적 경로를 제시한다.

### HELIOT: LLM-Based CDSS for adverse drug reaction management

- **연구의 본질적 가치:** 임상 노트 같은 비정형 정보를 활용해 경고 피로를 줄이는 방향으로 CDSS를 재설계해, "더 많이 경고"가 아니라 "더 잘 경고"가 핵심임을 보여준다.

### Large language model vs. traditional machine learning: Evaluating predictive models for early detection of tumor relapse

- **연구의 본질적 가치:** LLM이 기존 ML을 완전히 대체하기보다, 암 재발 예측에서 보완적 예측 자산이 될 수 있음을 보여주며 실제 임상 도입의 현실적 전략을 제시한다.

### ETS-MLLM: A large time series-language model for electrocardiogram question answering

- **연구의 본질적 가치:** 시계열 생체신호를 언어모델의 해석 가능 공간으로 끌어와, 진단 분류를 넘어서 질문응답형 임상 의사결정을 가능하게 한다.

### CausalMedLM: Causal inference-augmented LLMs for high-accuracy disease prediction

- **연구의 본질적 가치:** 상관 기반 진단을 넘어 인과 지식을 직접 주입함으로써, 희귀질환과 불균형 데이터 상황에서도 더 설득력 있는 진단판단을 가능하게 한다.

### Decoding the mind: A RAG-LLM on ICD-11 for decision support in psychology

- **연구의 본질적 가치:** 정신건강 진단을 표준 분류체계에 근거한 검색-생성 문제로 바꿔, 임상적 일관성과 해석 가능성을 동시에 높인다.

### MSDiagnosis: A benchmark and framework for evaluating large language models in multi-step clinical diagnosis

- **연구의 본질적 가치:** 진단을 단발성 정답 문제가 아니라 초진-감별-최종 진단의 연속적 과정으로 모델링해, 실제 의료 의사결정과 더 가까운 평가 기준을 세운다.

### Leveraging a large language model (LLM) to predict hospital admissions of emergency department patients

- **연구의 본질적 가치:** 환자 여정을 스토리 형태로 서술해 조기 입원 결정을 가능하게 함으로써, 병원 운영과 임상 판단을 동시에 개선하는 예측 모형을 제안한다.

### A framework for evaluation and requirement extraction for fine-tuning of Large Language Models in multimodal medical diagnosis

- **연구의 본질적 가치:** 의료 LLM을 전면 재학습하기보다 취약 영역을 찾아 정밀 보정하는 방식으로, 제한 자원 하에서 진단 시스템을 개선하는 전략을 제시한다.

### Developing a decision support system using different classification algorithms for polyclinic selection

- **연구의 본질적 가치:** 실제로는 LLM보다 전통 모델이 더 나을 수 있음을 보여주며, 전략적 의사결정 연구에서 "무조건 LLM"이 아니라 "문제 적합성"이 중요함을 일깨운다.

### IntelliCare: Improving healthcare analysis with patient-level knowledge from large language models

- **연구의 본질적 가치:** 환자 수준 외부지식을 정제해 기존 EHR 모델을 보강함으로써, LLM을 독립 진단자가 아니라 예측모델의 지식 증폭기로 활용한다.

### Knowledge-embedded large language models for emergency triage

- **연구의 본질적 가치:** 응급 분류를 도메인 적응된 LLM으로 표준화해, 숙련도 차이로 생기는 판단 변동성을 줄이는 방향을 보여준다.

### Reviewing clinical knowledge in medical large language models: Training and beyond

- **연구의 본질적 가치:** 의료 LLM의 핵심 경쟁력이 단순 모델 크기가 아니라 신뢰 가능한 임상지식의 접합 방식에 있음을 정리해, 후속 연구의 설계 원칙을 제공한다.

### Brain compensation mechanisms of large language models in clinical decision-making in acupuncture: A fusion study using fNIRS and eye-tracking

- **연구의 본질적 가치:** LLM 보조가 실제 인간 의사결정의 인지 부담을 어떻게 바꾸는지 실험적으로 보여주며, AI 보조의 효용을 성능이 아니라 인간 인지 변화로도 평가하게 만든다.

---

## 신뢰 가능한 고위험 의사결정과 리스크 통제

### SORA-ATMAS: Adaptive trust management and multi-LLM aligned governance for future smart cities

- **연구의 본질적 가치:** 여러 LLM이 낸 결정을 정책과 규범에 맞게 통제하는 거버넌스 층을 도입해, 자율 시스템의 책임성과 규제 적합성을 핵심 문제로 전환한다.

### HaluGNN: Hallucination detection in large language models using graph neural network

- **연구의 본질적 가치:** 할루시네이션을 토큰 간 관계가 무너진 구조적 문제로 보고 탐지함으로써, 고위험 의사결정에서 오류를 더 정교하게 걸러낼 수 있게 한다.

### HaluCheck: Explainable and verifiable automation for detecting hallucinations in LLM responses

- **연구의 본질적 가치:** 사실성 평가를 사용자 인터페이스와 결합해, 신뢰성 검증을 연구실 실험이 아니라 실무 의사결정 도구로 바꾸는 데 의미가 있다.

### Stylometry recognizes human and LLM-generated texts in short samples

- **연구의 본질적 가치:** 생성 텍스트의 흔적을 분별할 수 있다는 점을 보여주며, 전략 문서·보고서·증거 텍스트의 진위 관리라는 새로운 리스크 통제 문제를 제기한다.

### Query-efficient and dataset-independent red teaming for LLMs content safety evaluation

- **연구의 본질적 가치:** 안전성 검증을 데이터셋 의존적 시험이 아니라 적응형 탐색 문제로 바꿔, 더 저비용으로 시스템 취약점을 찾는 전략을 제안한다.

### A framework for hallucination mitigation in domain-specialized large language models with application to aviation maintenance decision support

- **연구의 본질적 가치:** 안전중요 도메인에서는 "더 똑똑한 답"보다 "근거가 추적되는 답"이 중요하다는 점을 명확히 보여준다.

### ATLASky-AI: An autonomous framework for physics-based trustworthy verification of LLM-generated spatiotemporal knowledge

- **연구의 본질적 가치:** 라벨 없는 운영 환경에서도 물리 법칙과 제약으로 검증하는 방식을 도입해, LLM 검증을 사후평가가 아니라 상시 운영 통제로 확장한다.

### Advancing text adversarial example generation using large language models

- **연구의 본질적 가치:** 모델 취약점을 더 정교하게 드러내는 공격 예제를 만들어, LLM 기반 의사결정 시스템의 방어 설계 필요성을 선명하게 보여준다.

### CM-MRAG: A multimodal retrieval-augmented framework for content moderation

- **연구의 본질적 가치:** 변화하는 규정을 반복 재학습 없이 반영하게 만들어, 콘텐츠 안전 의사결정을 더 유연하고 확장 가능하게 만든다.

### A smaller model can be better: Domain adaptation for LLM-generated text detection via soft prompt-tuning

- **연구의 본질적 가치:** 더 큰 모델보다 더 적합한 모델이 낫다는 점을 보여주며, 신뢰성 문제에서는 규모 경쟁보다 도메인 적응 전략이 핵심임을 시사한다.

### LLM-LADE: Large language model-based log anomaly detection with explanation

- **연구의 본질적 가치:** 시스템 이상탐지를 단순 경보에서 원인 설명 가능한 판단으로 바꾸어, 운영 의사결정의 후속 조치 품질을 높인다.

### Is It genuine or fake? Analyzing e-commerce reviews using large language models

- **연구의 본질적 가치:** 온라인 리뷰 신뢰성을 자동 판별해 소비자와 플랫폼의 전략 판단 기반을 더 건강하게 만든다.

### A comprehensive review of LLM-based content moderation: advancements, challenges, and future directions

- **연구의 본질적 가치:** 플랫폼 거버넌스에서 정확도만이 아니라 절차적 정당성, 다언어 공정성, 설명 가능성이 핵심 기준이 되어야 함을 정리한다.

### DelphiAgent: A trustworthy multi-agent verification framework for automated fact verification

- **연구의 본질적 가치:** 사실검증을 단일 모델 응답에서 다중 에이전트 합의 과정으로 전환해, 신뢰 가능한 판단 절차 자체를 설계한다.

### RaSA-BoDX: A meta-cognitive reasoning framework for cyberbullying language detection and mitigation using multi-agent systems

- **연구의 본질적 가치:** 탐지와 대응을 함께 설계하면서, 온라인 위해행동 관리에서 LLM이 단순 필터가 아니라 맥락을 보존한 완화 시스템이 될 수 있음을 보여준다.

### Do not wait: Preemptive rumor detection with cooperative LLMs and accessible social context

- **연구의 본질적 가치:** 공개 이후 대응이 아니라 공개 이전 억제를 목표로 해, 정보 리스크 관리에서 선제적 판단 체계의 가능성을 제시한다.

---

## 지식 접지형 의사결정 인프라 구축

### Optimizing text-to-SQL conversion techniques through the integration of intelligent agents and large language models

- **연구의 본질적 가치:** 비전문가가 데이터를 직접 질의하게 만들어, 조직 의사결정의 병목이던 "데이터 접근권" 문제를 줄인다.

### Assessing Open LLMs’ Ability to Identify Biomedical Taxonomic Relationships: A SNOMED CT-Based Experimental Evaluation

- **연구의 본질적 가치:** LLM이 도메인 지식 구조를 어디까지 이해하는지 검증함으로써, 향후 지식기반 의사결정 시스템에 LLM을 넣을 때 필요한 신뢰 경계를 드러낸다.

### DR-RAG: Domain-Rule-based Retrieval-Augmented Generation for aviation digital model design

- **연구의 본질적 가치:** 규칙·지식그래프·디지털트윈을 한 흐름으로 엮어, 복잡한 공학 설계를 근거 기반 의사결정으로 전환한다.

### A knowledge graph-enhanced large language model for question answering of hydraulic structure safety management

- **연구의 본질적 가치:** 안전관리 매뉴얼 의존을 줄이고 질의응답형 의사결정 지원으로 옮겨, 위기 상황에서 더 빠르고 과학적인 판단을 가능하게 한다.

### Advancing quality control in off-site construction with large language models enhanced by hybrid retrieval-augmented generation

- **연구의 본질적 가치:** 품질관리 의사결정에서 흩어진 지식을 통합 회수하는 능력이 핵심이라는 점을 보여주며, medium-sized 모델도 적절한 검색 구조가 있으면 충분하다는 메시지를 준다.

### Knowledge assimilation: Implementing knowledge-guided agricultural large language model

- **연구의 본질적 가치:** 농업처럼 데이터가 부족한 영역에서도 지식 동화 전략을 쓰면 LLM을 다중 의사결정 지원 도구로 만들 수 있음을 보여준다.

### Domain-specific SQL generation with LLMs: A hybrid framework combining knowledge graphs and retrieval-augmentation

- **연구의 본질적 가치:** 복잡한 관계형 데이터베이스에 대한 자연어 접근을 가능하게 해, 인프라 관리 의사결정의 속도와 설명가능성을 함께 높인다.

### GraphRAG-ASCOC: A lightweight framework for adaptive synonym-aware clustering and ontology completion

- **연구의 본질적 가치:** 표준 문서를 실행 가능한 온톨로지로 바꿔주어, 전문가 시스템과 의사결정 엔진의 지식 기반을 더 저렴하고 정교하게 구축하게 한다.

### Large language model for interpreting research policy using adaptive two-stage retrieval augmented fine-tuning method

- **연구의 본질적 가치:** 정책 해석을 근거 인용 가능한 형태로 바꿔, 연구비·기관 전략 판단의 투명성을 실무 수준에서 끌어올린다.

### A graph-guided LLM prompting for supply-demand reasoning in substation flood prevention

- **연구의 본질적 가치:** 기후 리스크 대응에서 도메인 그래프와 사례 기반 추론을 결합해, 공급 수요 판단을 더 맥락적이고 안정적으로 만든다.

### Ontology-based prompting with large language models for inferring construction activities from construction images

- **연구의 본질적 가치:** 시각 정보를 온톨로지 개념으로 번역해 LLM이 해석하게 함으로써, 시공 현장 의사결정의 맥락 이해력을 크게 높인다.

### Meet2Mitigate: An LLM-powered framework for real-time issue identification and mitigation from construction meeting discourse

- **연구의 본질적 가치:** 회의록을 단순 요약이 아니라 "문제-근거-대응안" 체계로 재조합해, 프로젝트 관리 의사결정을 실시간화한다.

### Knowledge graph enhanced large language model framework for causal chain reasoning in industrial fault diagnosis

- **연구의 본질적 가치:** 고장 진단을 단일 원인 추정이 아니라 증상-원인-해결책 사슬 추론으로 재구성해, 산업 현장의 판단 품질과 설명력을 높인다.

### Power ops agent: A knowledge and data dual-driven multi-agent framework for substation operation and maintenance

- **연구의 본질적 가치:** 지식 추론과 데이터 분석을 분리된 하위 에이전트로 설계함으로써, 전력 설비 운영 의사결정의 정확성과 신뢰성을 동시에 확보한다.

---

## 시장·사회·금융 전략 인텔리전스

### FinBloom: Knowledge-Grounding Large Language Model with Real-Time Financial Data

- **연구의 본질적 가치:** 금융 의사결정에서 핵심은 언어모델 자체보다 실시간 정보 접속성이라는 점을 보여주며, 정적인 모델을 동적 에이전트로 바꾼다.

### Explainable prediction of knowledge recombination: A synergized method with heterogeneous hypergraph learning and large language models

- **연구의 본질적 가치:** 미래 지식 결합 가능성을 읽어내는 능력을 통해, 연구기획과 기술전략 수립에서 "다음 혁신 조합"을 탐색하게 한다.

### Complex forecasting and investment strategy optimization via chain-of-thought of large language models

- **연구의 본질적 가치:** CoT가 단순 설명을 넘어서 실제 투자수익과 연결될 수 있음을 보이며, 재무 의사결정에 언어적 추론을 실전 도구로 끌어들인다.

### Automating customer feedback analysis in E-commerce: A multi-Model approach

- **연구의 본질적 가치:** 고객 피드백을 세밀한 행동 인사이트로 전환해, 기업이 경험 개선과 상품 전략을 더 빠르게 조정하도록 만든다.

### Unlocking knowledge-sharing live streaming e-commerce: An LLM-empowered analytics framework for book sales prediction

- **연구의 본질적 가치:** 라이브커머스 담론의 의미 구조를 판매 성과와 연결해, 플랫폼과 판매자의 전략적 메시지 설계에 직접적인 통찰을 준다.

### Enhancing large language models for bitcoin time series forecasting

- **연구의 본질적 가치:** 복잡하고 비정상적인 금융 시계열에서도 LLM이 도메인적 가공과 추가 정보 결합을 통해 더 나은 예측 자산이 될 수 있음을 보여준다.

### LLM-infused bi-level semantic enhancement for corporate credit risk prediction

- **연구의 본질적 가치:** 숫자 데이터에 의미 층을 입혀 기업 신용위험 판단을 정교화함으로써, 재무 의사결정의 맥락 민감성을 높인다.

### Embedding-Based decision support framework for large-scale content analysis

- **연구의 본질적 가치:** 대규모 비정형 문서를 전략 인텔리전스로 바꾸는 체계를 제공해, 규제·시장·CSR 분석 같은 상위 의사결정을 가속한다.

### Do not wait: Preemptive rumor detection with cooperative LLMs and accessible social context

- **연구의 본질적 가치:** 정보 확산 전 단계에서 조기 경보를 가능하게 해, 사회적 리스크와 평판 관리의 선제적 전략을 가능하게 한다.

### Explainable zero-shot trading using multi-agent LLM architecture: A backtested approach for Bitcoin price

- **연구의 본질적 가치:** 서로 다른 금융 신호를 전문 에이전트별로 해석하게 해, 투자 판단을 더 모듈화되고 설명가능한 전략 체계로 바꾼다.

### RoleSimLLM: Towards large-scale and comprehensive social propagation simulation via role-based LLM-driven agents

- **연구의 본질적 가치:** 사회 확산을 역할 기반 행위자 시뮬레이션으로 모델링해, 정책·마케팅·여론 전략 수립에 필요한 거시적 실험장을 제공한다.

### LLM-powered explanations: Unraveling recommendations through subgraph reasoning

- **연구의 본질적 가치:** 추천 결과의 이유를 구조적으로 드러내어, 추천시스템을 단순 예측기가 아니라 협상 가능한 전략 인터페이스로 전환한다.

---

## 의사결정 절차 자체의 설계와 평가

### CART: A traceable zero-shot planning framework for large language models with adaptive replanning

- **연구의 본질적 가치:** 계획 실패 이후 어떻게 다시 계획할지를 체계화해, LLM 의사결정을 일회성 답변이 아닌 연속적 계획 프로세스로 만든다.

### User-defined trade-offs in LLM benchmarking: balancing accuracy, scale, and sustainability

- **연구의 본질적 가치:** 모델 선택을 단일 점수 경쟁에서 다기준 선호 반영 문제로 바꿔, 실제 조직의 전략적 선택 상황에 맞는 평가 체계를 제시한다.

### Semantic knowledge abstraction: Consistent reasoning in large language models for natural language inference

- **연구의 본질적 가치:** 추론 성능 향상의 핵심이 더 많은 정보가 아니라 더 높은 수준의 추상화일 수 있음을 보여주며, 의사결정 품질 개선의 다른 방향을 제시한다.

### Enhancing belief consistency of large language model agents in decision-making process based on attribution theory

- **연구의 본질적 가치:** 선택 이전에 신념 귀인을 수행하게 함으로써, LLM 에이전트가 상황에 흔들리지 않고 더 일관된 의사결정을 하도록 만든다.

### A survey of slow thinking-based reasoning LLMs using reinforcement learning and test-time scaling law

- **연구의 본질적 가치:** 전략적 의사결정의 핵심이 빠른 응답이 아니라 계산 자원을 적절히 배분하는 느린 사고 설계에 있음을 정리한다.

### Multimodal hierarchical classification using cascade-of-thought

- **연구의 본질적 가치:** 복잡한 분류를 여러 단계 판단으로 나눔으로써, 비정형 고차원 문제도 의사결정 파이프라인 형태로 풀 수 있음을 보여준다.

### D2A2: Enhancing LLM knowledge distillation efficiency and performance with difficulty-aware and adaptive distillation framework

- **연구의 본질적 가치:** 어떤 샘플에 더 집중해 학습할지 결정하는 메타 의사결정을 도입해, 효율적인 LLM 운영 전략의 기초를 제공한다.

### MeetMulti-X: A benchmark analysis of scaling and prompting large language models on automatic minuting

- **연구의 본질적 가치:** 회의 요약에서 "더 큰 모델"이 항상 답이 아니라는 점을 실증하며, 운영 환경에 맞는 모델-프롬프트 설계 전략을 구체화한다.

### Heuristically motivating large language models for task planning

- **연구의 본질적 가치:** LLM을 주계획자가 아니라 휴리스틱 계획의 보강자에 두어, 계획 시스템에서 LLM의 가장 생산적인 역할을 재정의한다.

### An uncertainty-aware framework integrating large language model and fuzzy inference system for commonsense reasoning

- **연구의 본질적 가치:** 모든 판단을 이분법으로 강제하지 않고 애매함을 계산 가능한 형태로 남겨, 더 신중한 의사결정 구조를 만든다.

### UniDE: A multi-level and low-resource framework for automatic dialogue evaluation via LLM-based data augmentation and multitask learning

- **연구의 본질적 가치:** 대화 품질 평가를 자원 집약적 초거대 모델 의존에서 벗어나게 해, 작고 실용적인 평가 시스템 설계의 가능성을 보여준다.

---

## 인간·전문가·조직과의 협업 설계

### Provoking critical thinking: Using counter-arguments in online discussion summarisation

- **연구의 본질적 가치:** LLM이 사용자를 설득하는 기계가 아니라 더 나은 숙고를 유도하는 반론 제시자로 설계될 수 있음을 보여준다.

### Large language models as virtual experts? Evaluating AHP-based criteria weighting performance for solar power plant site selection

- **연구의 본질적 가치:** LLM을 전문가 대체가 아니라 전문가 합의에 가까워질 수 있는 가상 조언자로 검증해, 고위험 의사결정에서의 적절한 역할 범위를 제시한다.

### Expert-guided forecasting of epidemic ARI incidence based on physics-informed neural networks and large language models

- **연구의 본질적 가치:** 비정형 전문가 의견을 수리모형 수정으로 연결해, 사람의 직관과 AI 예측을 결합하는 새로운 협업 구조를 보여준다.

### Toward human-centric coal mine auxiliary operations in Industry 5.0: An XR-based approach for human-robot hybrid decision-making

- **연구의 본질적 가치:** 완전 자동화가 아닌 인간-로봇 공동판단을 목표로 해, 전략적 의사결정에서 LLM의 역할을 "대체"보다 "증강"으로 재정립한다.

### Building Society 5.0: a foundation for decision-making based on open models and digital twins

- **연구의 본질적 가치:** 시민이 모델의 가정과 검증 과정을 이해하고 참여해야 한다는 관점을 통해, 전략적 의사결정의 민주성과 책임성을 강조한다.

### A group experts–LLMs collaborative decision making method to improve reliability in FMEA risk evaluation

- **연구의 본질적 가치:** 전문가와 LLM의 이질적 판단을 합의 메커니즘으로 통합해, 위험평가를 더 견고한 집단 의사결정으로 만든다.

### A2C: A modular multi-stage collaborative decision framework for human–AI teams

- **연구의 본질적 가치:** 자동화, 보조, 공동 탐색의 모드를 전환하게 하여, 인간-AI 협업의 핵심이 단순 defer가 아니라 상황별 협업 모드 선택임을 보여준다.

### Court to conversation: Tactical badminton analysis via computer vision and RAG-enhanced LLMs

- **연구의 본질적 가치:** 코치의 암묵지를 질의 가능한 전술 인텔리전스로 바꾸어, 현장 전문가의 분석 역량을 확장하는 협업형 도구를 제시한다.

### Uncertainty reports as explainable AI: A cognitive-adaptive framework for human-AI decision systems in context tasks

- **연구의 본질적 가치:** 설명의 핵심을 "이유"가 아니라 "불확실성 전달 방식"으로 옮겨, 인간이 AI 판단을 어떻게 받아들이는지까지 설계 대상으로 포함한다.

### Bias explained: Generation of high-quality natural language explanations for classification decisions

- **연구의 본질적 가치:** 분류 결과 설명을 사용자 이해 중심으로 재설계해, 인간이 결정을 납득하고 활용할 수 있는 XAI의 실용적 기준을 제시한다.

