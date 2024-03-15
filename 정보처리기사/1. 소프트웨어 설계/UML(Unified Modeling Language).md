## UML(Unified Modeling Language)

개발자와 고객 또는 개발자 상호간의 의사소통이 원활하게 이루어지도록 표준화한 대표적인 객체지향 모델링 언어  
UML 구성요소 : 사물(Things), 관계(Relationship), 다이어그램(Diagram)

### 사물(Things)

| 사물                             | 설명                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------ |
| 구조 사물<br>(Structural Things) | - 시스템의 개념적, 물리적 요소를 표현<br>- 클래스, 유스케이스(Use Case), 컴포넌트, 노드 등 |
| 행동 사물<br>(Behavior)          | - 시간과 공간에 따른 요소들의 행위를 표현<br>- 상호작용, 상태 머신 등                      |
| 그룹 사물<br>(Grouping Things)   | - 요소들을 그룹으로 묶어서 표현<br>- 패키지                                                |
| 주해 사물<br>(Annotation Things) | - 부가적인 설명이나 제약조건 등을 표현<br>- 노트                                           |

### 관계(Relationship)

사물과 사물 사이의 연관성

- 연관 관계(Association)
- 집합 관계(Aggregation)
- 포함 관계(Composition)
- 일반화 관계(Generalization)
- 의존 관계(Dependency)
- 실체화 관계(Realizaiton)

### 다이어그램(Diagram)

여러 관점에서 시스템을 가시화한 뷰(View)를 제공함으로써 의사소통에 도움  
정적 모델링 - 구조적 다이어그램  
동적 모델링 - 행위 다이어그램

> 구조적 다이어그램: Class, Object, Component, 배치(Deployment), 복합체 구조(Composite Structure), Package

> 행위 다이어그램: 유스케이스(Use Case), 순차(Sequence), Communication, State, Activity, Interaction Overview, Timing
