---
id: S0133
study_id: S0133
title: "A PSO weighted ensemble framework with SMOTE balancing for student dropout prediction in smart education systems"
year: 2025
database: "Scopus"
venue: "Scientific Reports"
doi: "10.1038/s41598-025-97506-1"
url: "https://www.scopus.com/pages/publications/105005547670?origin=resultslist"
status: "[Excluido Fase 2 - Criterio EC2]"
qa_score: 7
population_scope: "Educação Básica (K-12)"
intervention_scope: "Random Forest / Ensemble Learning"
outcome_scope: "Predição de Risco de Abandono Escolar no K-12"
authors:
  - "Achin Jain"
  - "Arun Kumar Dubey"
  - "Shakir Khan"
  - "Arvind Panwar"
  - "Mohammad Alkhatib"
  - "Abdulaziz M Alshahrani"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
  - "[[Random_Forest]]"
  - "[[XGBoost]]"
  - "[[Explicabilidade_XAI]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/absenteismo_cronico
---
# S0133: A PSO weighted ensemble framework with SMOTE balancing for student dropout prediction in smart education systems

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0133`
> - **Autores:** Achin Jain, Arun Kumar Dubey, Shakir Khan, Arvind Panwar, Mohammad Alkhatib, Abdulaziz M Alshahrani
> - **Ano:** 2025
> - **Veículo (Venue):** *Scientific Reports*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Springer Link']`)
> - **DOI:** [10.1038/s41598-025-97506-1](https://doi.org/10.1038/s41598-025-97506-1)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105005547670?origin=resultslist)
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC2]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Student dropout is a critical issue that affects not only educational institutions but also students’ mental well-being, career prospects, and long-term quality of life. The ability to predict dropout rates accurately enables timely interventions that can support students’ academic success and psychological resilience. However, the imbalanced nature of student dropout datasets often results in biased and less effective predictive models. To address this, we propose a Particle Swarm Optimization (PSO)-Weighted Ensemble Framework integrated with the Synthetic Minority Oversampling Technique (SMOTE). This methodology balances the dataset using SMOTE, optimizes model hyperparameters, and fine-tunes ensemble weights through PSO to improve predictive performance. The framework achieves 86% accuracy, an AUC score of 0.9593, and enhanced dropout class metrics, including an F1-Score of 0.8633, precision of 0.8633, and recall of 0.86. Compared to Ant Colony Optimization (ACO) and Firefly algorithms, which achieve accuracies of 83% and 85% respectively, our approach demonstrates up to a 3% improvement in key performance metrics. Additionally, in comparison to individual baseline models used in ensemble model Random Forest (RF) with SMOTE (83.5% accuracy, 0.95 AUC) and XGBoost (XGB) with SMOTE (82.7% accuracy, 0.95 AUC), the proposed framework significantly enhances predictive reliability. Furthermore, PSO offers computational efficiency advantages over Firefly and Ant Colony Optimization, reducing hyperparameter tuning time while improving ensemble performance. The proposed framework is scalable and adaptable for real-world applications, particularly in educational institutions, where it can aid in early intervention strategies to mitigate dropout rates. © The Author(s) 2025.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (K-12)
- **Intervencao/Tecnologia (Intervention Scope):** Random Forest / Ensemble Learning
- **Desfecho (Outcome Scope):** Predição de Risco de Abandono Escolar no K-12
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de predição de risco de abandono escolar no k-12 na educação básica (k-12), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0133`
- **Titulo Completo:** A PSO weighted ensemble framework with SMOTE balancing for student dropout prediction in smart education systems
- **Autores:** Achin Jain, Arun Kumar Dubey, Shakir Khan, Arvind Panwar, Mohammad Alkhatib, Abdulaziz M Alshahrani
- **Ano de Publicacao:** 2025
- **Tipo de Publicacao:** Periodico (Artigo Original)
- **Nome do Veiculo:** Scientific Reports (15:17463)
- **DOI:** [10.1038/s41598-025-97506-1](https://doi.org/10.1038/s41598-025-97506-1)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Autores da India e Arabia Saudita; dataset publico UCI originario do Ensino Superior em Portugal (Martins et al., 2021).

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Superior (Higher Education) — **Motivo de exclusao na Fase 2 (EC2):** embora triado inicialmente como K-12 na Fase 1, a leitura integral comprova que o dataset utilizado refere-se a estudantes universitarios e nao contempla fatores socioemocionais ou recusa escolar.
- **Faixa Etaria / Amostra ($N$):** N = 4.424 registros de estudantes (2.209 Graduate, 1.421 Dropout, 794 Enrolled), com 36 features.
- **Publico-alvo Avaliado:** Estudantes de Ensino Superior classificados em tres classes (Dropout, Enrolled, Graduate).
- **Fonte dos Dados / Dataset:** Dataset publico UCI Machine Learning Repository (*Predict Student Dropout and Academic Success*).

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** N/A (nao utiliza instrumentos psicometricos).
- **Natureza da Ferramenta:** N/A.
- **Forma de Aplicacao:** N/A.
- **Finalidade:** N/A.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Machine Learning Supervisionado (Ensemble Ponderado com Otimizacao Meta-heuristica), Tecnicas de Balanceamento de Dados e [[Explicabilidade_XAI|XAI (SHAP)]].
- **Algoritmos Empregados:** [[Random_Forest]] (RF) e [[XGBoost]] (XGB) em ensemble ponderado otimizado por Particle Swarm Optimization (PSO), comparados a Ant Colony Optimization (ACO), Firefly Algorithm (FA), Logistic Regression (LR), Decision Tree (DT), KNN, CNN, LSTM, CNN+LSTM, CatBoost+Optuna e LightGBM+Optuna. Balanceamento: SMOTE, ADASYN e Random Under-sampling (RU).
- **Tarefa do Modelo:** Classificacao multiclasse (Dropout, Enrolled, Graduate).
- **Estagio de Deteccao:** Predicao precoce de evasao academica em plataformas de ensino superior/smart education.

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Nenhuma (o estudo apenas menciona bem-estar mental e estresse de forma generica na introducao e conclusao, sem incluir variaveis psicologicas no modelo).
- **Variaveis Comportamentais / Historico:** Desempenho academico semestral (unidades curriculares aprovadas no 1o e 2o semestres, notas de admissao) e situacao de pagamento de mensalidades (tuition fees up to date).
- **Variaveis Familiares / Sociodemograficas:** Genero, nacionalidade, estado civil, ocupacao parental e bolsa de estudos (scholarship).
- **Variaveis Institucionais / Contextuais:** Indicadores macroeconomicos e institucionais (PIB/GDP, taxa de inflacao).
- **Features Mais Relevantes Identificadas:** Via [[Explicabilidade_XAI|SHAP]]: (1) Curricular units 2nd sem (approved) (~0,8), (2) Curricular units 1st sem (approved) (~0,5), (3) Tuition fees up to date (~0,5); importancia intermediaria para bolsa de estudos, nota de admissao, PIB e taxa de inflacao; menor importancia (< 0,1) para nacionalidade, estado civil e ocupacao parental.

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A.
- **Metricas Computacionais (ML):** Modelo proposto (PSO-Weighted Ensemble RF+XGB com SMOTE): Acuracia = 86%, AUC-ROC = 0,9593, Macro F1-Score = 0,8633 (Precisao = 0,8633, Recall = 0,86). Por classe: Dropout (F1 = 0,88, Precisao = 0,93, Recall = 0,83, Acuracia = 0,86), Enrolled (F1 = 0,84, Precisao = 0,82, Recall = 0,86), Graduate (F1 = 0,87, Precisao = 0,84, Recall = 0,89). Comparado a ACO (83%, AUC 0,9490) e Firefly (85%, AUC 0,9575). Analise multicriterio TOPSIS (C* = 1,0000 para PSO) e paired t-test (p <= 0,01 contra todos os comparadores).
- **Estrategia de Validacao:** Split treino/teste (80% treino, 20% teste), 10 execucoes para comparacao de estabilidade dos otimizadores, teste t pareado e TOPSIS.
- **Desafios Metodologicos Relatados:** Forte desbalanceamento de classes no dataset original (especialmente classe Enrolled com baixo F1 = 0,305-0,471 sem balanceamento) e custo computacional de ajuste de hiperparametros.
- **Aspectos Eticos e Transparencia (XAI):** Aplica SHAP (TreeSHAP) para interpretabilidade global e local das predicoes; menciona conformidade com leis de privacidade de dados estudantis como requisito para implantacao real.
- **Limitacoes Declaradas:** Generalizacao limitada entre diferentes instituicoes educacionais e escalabilidade para grandes conjuntos de dados.
- **Direcoes Futuras:** Integracao em sistemas de gestao academica com retreinamento periodico anual, exploracao de arquiteturas de Deep Learning e ampliacao de tecnicas de XAI.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo claramente definido: propor um framework ensemble ponderado por PSO com SMOTE para predicao de evasao estudantil em dados desbalanceados. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Pipeline detalhado (SMOTE/ADASYN/RU, espaco de busca de hiperparametros, pesos PSO, split 80/20, TOPSIS e paired t-test). |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Acuracia, Precisao, Recall, F1-Score por classe, Macro F1, AUC-ROC, matrizes de confusao, curvas ROC/PR e testes estatisticos. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 0 | Nao contempla variaveis socioemocionais, psicologicas ou de recusa escolar (dataset exclusivamente academico, administrativo e macroeconomico do Ensino Superior; excluido por EC2). |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 1 | Menciona brevemente limitacoes de generalizacao institucional, escalabilidade e privacidade, sem aprofundar vieses de geracao sintetica (SMOTE) ou do dataset UCI. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **7 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
