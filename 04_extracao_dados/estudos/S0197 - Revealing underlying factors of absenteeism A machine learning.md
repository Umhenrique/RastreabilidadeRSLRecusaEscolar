---
id: S0197
study_id: S0197
title: "Revealing underlying factors of absenteeism: A machine learning approach"
year: 2022
database: "Web of Science"
venue: "Frontiers in Psychology"
doi: "10.3389/fpsyg.2022.958748"
url: ""
status: "[Incluido Fase 2 - Extracao Concluida]"
qa_score: 8
population_scope: "Educacao Basica (Ensino Fundamental - K-6)"
intervention_scope: "Modelos de Machine Learning Hibrido (K-Means + Gaussian Naive Bayes + KNN)"
outcome_scope: "Classificacao de Risco Socioemocional e Analise de Fatores Subjacentes do Absenteismo Escolar"
authors:
  - "Francis Bowen"
  - "Carolyn Gentle-Genitty"
  - "Janaina Siegler"
  - "Marlin Jackson"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "Building Dreams (BD) Platform - 10 SEL Core Values"
algorithms:
  - "K-Means Clustering"
  - "Gaussian Naive Bayes"
  - "K-Nearest Neighbors (KNN)"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/web_of_science
  - fenomeno/absenteismo_cronico
---
# S0197: Revealing underlying factors of absenteeism: A machine learning approach

> [!INFO] Metadados Rapidos
> - **ID do Estudo:** `S0197`
> - **Autores:** Francis Bowen, Carolyn Gentle-Genitty, Janaina Siegler, Marlin Jackson
> - **Ano:** 2022
> - **Veiculo (Venue):** *Frontiers in Psychology* (Vol. 13, Art. 958748)
> - **Base de Origem:** `Web of Science` (Bases: `['Web of Science']`)
> - **DOI:** [10.3389/fpsyg.2022.958748](https://doi.org/10.3389/fpsyg.2022.958748)
> - **URL:** Nao informado
> - **Status da Extracao:** `[Incluido Fase 2 - Extracao Concluida]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Introduction: The basis of support is understanding. In machine learning, understanding happens through assimilated knowledge and is centered on six pillars: big data, data volume, value, variety, velocity, and veracity. This study analyzes school attendance problems (SAP), which encompasses its legal statutes, school codes, students' attendance behaviors, and interventions in a school environment. The support pillars include attention to the physical classroom, school climate, and personal underlying factors impeding engagement, from which socio-emotional factors are often the primary drivers. Methods: This study asked the following research question: What can we learn about specific underlying factors of absenteeism using machine learning approaches? Data were retrieved from one school system available through the proprietary Building Dreams (BD) platform, owned by the Fight for Life Foundation (FFLF), whose mission is to support youth in underserved communities. The BD platform, licensed to K-12 schools, collects student-level data reported by educators on core values associated with in-class participation (a reported-negative or positive-behavior relative to the core values) based on Social-Emotional Learning (SEL) principles. We used a multi-phased approach leveraging several machine learning techniques (clustering, qualitative analysis, classification, and refinement of supervised and unsupervised learning). Unsupervised technique was employed to explore strong boundaries separating students using unlabeled data. Results: From over 20,000 recorded behaviors, we were able to train a classifier with 90.2% accuracy and uncovered a major underlying factor directly affecting absenteeism: the importance of peer relationships. This is an important finding and provides data-driven support for the fundamental idea that peer relationships are a critical factor affecting absenteeism. Discussion: The reported results provide a clear evidence that implementing socio-emotional learning components within a curriculum can improve absenteeism by targeting a root cause. Such knowledge can drive impactful policy and programming changes necessary for supporting the youth in communities overwhelmed with adversities.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educacao Basica (Ensino Fundamental, K-6)
- **Intervencao/Tecnologia (Intervention Scope):** Pipeline Multifase de Machine Learning (K-Means + Naive Bayes Gaussiano + KNN) sobre dados de Aprendizagem Socioemocional (SEL)
- **Desfecho (Outcome Scope):** Estratificacao de risco (baixo, medio, alto) e identificacao de fatores socioemocionais subjacentes ao absenteismo escolar
- **Criterios de Inclusao:** `IC1, IC2, IC3, IC4`
- **Motivo da Inclusao:**
  > **INCLUIDO**: Estudo empirico revisado por pares que aplica concretamente tecnicas de Machine Learning nao supervisionado (K-Means) e supervisionado (Gaussian Naive Bayes e KNN, atingindo 90,2% de acuracia) sobre registros comportamentais socioemocionais (SEL) de estudantes K-6 para estratificar perfis de risco e revelar fatores subjacentes ao absenteismo escolar (destacando relacionamento com pares e etica de trabalho/engajamento).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0197`
- **Titulo Completo:** Revealing underlying factors of absenteeism: A machine learning approach
- **Autores:** Francis Bowen, Carolyn Gentle-Genitty, Janaina Siegler, Marlin Jackson
- **Ano de Publicacao:** 2022
- **Tipo de Publicacao:** Periodico (Original Research, Open Access)
- **Nome do Veiculo:** Frontiers in Psychology
- **DOI:** [10.3389/fpsyg.2022.958748](https://doi.org/10.3389/fpsyg.2022.958748)
- **Base de Dados:** Web of Science
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (Indiana Central — uma escola K-6 em comunidade vulneravel)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Kindergarten ate 6o ano / K-6, Ensino Fundamental)
- **Faixa Etaria / Amostra ($N$):** $N = 332$ estudantes distribuidos em 15 turmas (K-6), gerando $26.741$ registros comportamentais ao longo do semestre de outono (Fall 2021), com media de $4,2$ registros por aluno por dia. Apos classificacao final: baixo risco $C_{LR}$ ($n = 210$), medio risco $C_{MR}$ ($n = 68$) e alto risco $C_{HR}$ ($n = 54$).
- **Publico-alvo Avaliado:** Estudantes de escola publica K-6 em comunidade socialmente vulneravel/subatendida usando a plataforma Building Dreams.
- **Fonte dos Dados / Dataset:** Dados observacionais longitudinais (semestre de outono 2021) registrados por educadores e administradores na plataforma proprietaria *Building Dreams* (BD) da *Fight for Life Foundation* (FFLF).

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** Matriz comportamental de 10 Valores Centrais (*Core Values*, CV1 a CV10) da plataforma gamificada *Building Dreams* (FFLF), fundamentada em principios de Aprendizagem Socioemocional (SEL). Nao utiliza escalas psicometricas clinicas tradicionais (como [[SRAS-R]] ou [[SCARED]]).
- **Natureza da Ferramenta:** Plataforma digital gamificada com metafora de futebol americano (*first downs*, *sacks*, *extra points*, *flags* e *red zones*) integrada ao curriculo escolar e a sistemas MTSS/RTI.
- **Forma de Aplicacao:** Relato continuo diario por educadores e administradores previamente treinados (registro de comportamentos positivos e negativos em sala de aula).
- **Finalidade:** Monitoramento comportamental continuo, estratificacao de risco em 3 niveis (verde/baixo, amarelo/medio, vermelho/alto) e direcionamento de intervencoes SEL.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Pipeline Hibrido Multifase combinando Machine Learning Nao Supervisionado (K-Means por turma), Analise Qualitativa de Rotulacao, Machine Learning Supervisionado (Gaussian Naive Bayes e K-Nearest Neighbors) e Refinamento Iterativo para classificacao final.
- **Algoritmos Empregados:** `K-Means Clustering` (distancia euclidiana, $K = 3$ por turma), `Gaussian Naive Bayes` (classificador probabilistico final), `K-Nearest Neighbors` (KNN, distancia euclidiana, $K = 5$).
- **Tarefa do Modelo:** Classificacao multiclasse em 3 niveis de risco ($C_{LR}$ baixo risco, $C_{MR}$ medio risco, $C_{HR}$ alto risco) a partir de vetores de proporcao de 5 tipos de registros gamificados, seguida de analise descritiva comparativa dos fatores de absenteismo entre $C_{LR}$ e $C_{HR}$.
- **Estagio de Deteccao:** Alerta precoce / estratificacao preventiva continua baseada em registros diarios de sala de aula.

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** 10 Valores Centrais SEL (CV1 a CV10): entusiasmo em aula (CV1), foco em aula (CV2), cumprimento de tarefas (CV3), iniciativa (CV4), seguir instrucoes (CV5), respeito ao espaco alheio (CV6), respeito ao ambiente fisico (CV7), responsabilidade/*accountability* (CV8), comunicacao respeitosa (CV9) e relacionamentos positivos (CV10).
- **Variaveis Comportamentais / Historico:** Vetor de 5 features normalizadas por aluno $s_i$: proporcao de *first downs* ($x_{fd}$, comportamento positivo), *sacks* ($x_s$, comportamento negativo), *extra points* ($x_{ep}$, traco positivo de carater), *flags* ($x_f$, comportamento preocupante) e *red zones* ($x_{rz}$, remocao grave de sala). Razoes especificas ligadas a assiduidade ("chegar a aula no horario" e "chegar preparado para aprender"), conduta (brigas, desrespeito a regras, insultos, ameacas) e desempenho academico.
- **Variaveis Familiares / Sociodemograficas:** Contexto comunitario de vulnerabilidade socioeconomica da escola (nao incluidas como features individuais no vetor do modelo).
- **Variaveis Institucionais / Contextuais:** Estrutura de turma (15 turmas K-6 agrupadas independentemente para controlar vieses de registro docente) e clima de sala de aula.
- **Features Mais Relevantes Identificadas:** *First downs*, *sacks* e *red zones* foram os maiores diferenciadores entre $C_{LR}$ (96% first downs, 1% sacks, 0% red zones) e $C_{HR}$ (63% first downs, 21% sacks, 6% red zones). Na analise dos motivos subjacentes: **relacionamento com pares** (4 das 6 principais razoes diferenciadoras em $C_{HR}$, como discutir, brigar, insultar/ameacar colegas), **assiduidade/pontualidade** (99,6% dos registros positivos de chegar no horario pertenceram ao grupo $C_{LR}$; $91,4\%$ de estar preparado para aprender) e **etica de trabalho/desempenho academico**.

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A (nao reporta Alfa de Cronbach ou validade fatorial dos 10 Core Values).
- **Metricas Computacionais (ML):** Na fase intermediaria (27 centros de cluster de 9 turmas avaliando as 6 turmas restantes): Gaussian Naive Bayes = **77,8% de acuracia** (matriz de confusao 3x3: CLR 8/9, CMR 5/9, CHR 8/9) e KNN ($K=5$) = **63,0% de acuracia** (CLR 7/9, CMR 6/9, CHR 6/9). Apos refinamento qualitativo e remocao de 4 outliers (41 centros de cluster finais): modelo final **Gaussian Naive Bayes atingiu 90,2% de acuracia**. Nao reporta F1-score, AUC-ROC, precisao ou recall especificos por classe no artigo, nem metricas diretas contra registros oficiais de dias de falta.
- **Estrategia de Validacao:** Separacao entre 9 turmas com clusters claros (27 centroides) para treino e 6 turmas restantes (18 centroides) para avaliacao e consenso entre Bayes e KNN + refinamento qualitativo para modelo final sobre 41 centroides (sem k-fold cross-validation explicito na acuracia final de 90,2%).
- **Desafios Metodologicos Relatados:** Dados originalmente nao rotulados (exigindo clusterizacao K-Means previa e interpretacao humana); inconsistencia de registro entre professores (ex.: uma turma nao registrou nenhum *first down*); nem todas as turmas apresentam naturalmente 3 niveis de risco; sensibilidade da clusterizacao a metrica de distancia (euclidiana).
- **Aspectos Eticos e Transparencia (XAI):** Pipeline transparente por regras de proporcao de 5 indicadores comportamentais e inspecao direta dos motivos textuais/valores centrais associados a cada grupo (XAI descritiva pos-hoc), embora use plataforma proprietaria e nao detalhe comite de etica no texto.
- **Limitacoes Declaradas:** (1) Coleta restrita a um unico semestre (Outono 2021) em uma unica escola; (2) Ausencia de fatores externos/familiares/socioeconomicos no modelo; (3) Subjetividade e dependencia da consistencia de registro dos educadores; (4) Nao comparacao com outros algoritmos (SVM, Random Forest, Redes Neurais); (5) Observacao metodologica adicional: o rotulo supervisionado nao e o absenteismo oficial medido em dias de falta, mas sim clusters comportamentais SEL nos quais a pontualidade/presenca e analisada pos-hoc.
- **Direcoes Futuras:** Expandir a coleta para multiplos semestres e outras escolas; incorporar fatores externos (familiares/socioeconomicos) e desfechos de desempenho academico e evasao (*dropout*); comparar SVM, Random Forest e Redes Neurais com a abordagem proposta.

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** Registros comportamentais diarios lancados por professores e administradores na plataforma gamificada *Building Dreams* (26.741 registros em 332 alunos, media de 4,2 registros/dia/aluno), codificados em 10 valores centrais SEL (CV1-CV10) e agregados em 5 proporcoes por aluno: *first downs*, *sacks*, *extra points*, *flags* e *red zones*. Nao coleta autorrelato psicometrico de ansiedade ou depressao internalizante diretamente do aluno, capturando sofrimento/desajuste via manifestacoes observadas em sala (isolamento/conflitos com pares, desregulacao, falta de engajamento e atrasos/ausencias).
- **Inventario completo de variaveis e justificativa de escolha:** Vetor numerico de 5 dimensoes por aluno ($x_{fd}, x_s, x_{ep}, x_f, x_{rz}$ representando proporcoes dos 5 tipos de registros sobre o total de registros do aluno), associado aos 10 Core Values (CV1-CV10) e suas razoes subjacentes (incluindo "chegar a aula no horario" e "chegar preparado para aprender"). Escolhidas por representarem dados ecologicos diarios de sala de aula ja coletados continuamente pela escola sob o arcabouco SEL e MTSS, evitando sobrecarga de questionarios externos.
- **Fundamentacao teorica do identificador:** Aprendizagem Socioemocional (SEL; Durlak et al., 2011; Hoffman, 2009), Sistema de Suporte em Multiplas Camadas (MTSS / RTI; Kearney & Graczyk, 2014, 2020), modelo dimensional-categorial de problemas de frequencia escolar (Skedgell & Kearney, 2016; Heyne et al., 2019), Cognitivismo, Teoria Social Cognitiva (Bandura) e Behaviorismo (Skinner).
- **Restricoes de recursos e limitacoes:** Requer licenciamento da plataforma proprietaria *Building Dreams* (FFLF), infraestrutura digital continua em sala de aula e programa rigoroso de treinamento previo de todos os professores para garantir consistencia na observacao e registro diario (4,2 registros/aluno/dia). Em escolas com restricao de recursos ou alta rotatividade docente, a sobrecarga de registro continuo e o vies de reporte entre turmas (como observado na turma que nao registrou *first downs*) representam gargalos significativos.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Formula claramente a pergunta de pesquisa sobre o que se pode aprender sobre fatores subjacentes ao absenteismo usando ML. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 1 | Descreve equacoes de K-Means, Bayes e KNN ($K=5$) e dataset ($N=332$; 26.741 registros), mas depende de filtragem qualitativa manual de 6 turmas e 4 outliers e nao detalha particionamento da avaliacao final. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Apresenta matrizes de confusao (77,8% Bayes, 63,0% KNN) e acuracia final (90,2%), mas sem F1, AUC-ROC, validacao cruzada k-fold ou metrica direta contra faltas oficiais. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Foco central nos 10 valores SEL, relacionamentos com pares, engajamento e comportamento em sala de aula no contexto MTSS. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute vies de registro docente, limitacoes de K-Means/distancia euclidiana, escola/semestre unico e ausencia de variaveis externas. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **8 / 10** | Estudo primario incluido na RSL (IC1 atendido), contribuindo com pipeline hibrido de ML sobre dados SEL diarios. |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- **Estudo INCLUIDO (IC1):** Aplicacao concreta de ML nao supervisionado (K-Means) + supervisionado (Gaussian Naive Bayes e KNN) sobre dados socioemocionais (SEL) escolares para identificar perfis de risco ligados ao absenteismo no ensino fundamental (K-6).
- **Ponto de atencao para a sintese (RQ2/RQ4):** Os rotulos de risco (`CLR/CMR/CHR`) sao construidos por clusterizacao sobre ocorrencias SEL (nao diretamente por um limiar de dias de falta do diario de classe), e a ligacao com absenteismo e demonstrada pela forte concentracao de registros de assiduidade/pontualidade no grupo `CLR` (99,6%) e de conflitos com pares no grupo `CHR`.

---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
