---
id: S0133
study_id: S0133
title: "A PSO weighted ensemble framework with SMOTE balancing for student dropout prediction in smart education systems"
year: 2025
database: "Scopus"
venue: "Scientific Reports"
doi: "10.1038/s41598-025-97506-1"
url: "https://www.scopus.com/pages/publications/105005547670?origin=resultslist"
status: "[Pendente Leitura Completa]"
qa_score: 0
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
> - **Status da Extração:** `[Pendente Leitura Completa]`

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
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Scientific Reports
- **DOI:** [10.1038/s41598-025-97506-1](https://doi.org/10.1038/s41598-025-97506-1)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** *(Preencher durante leitura completa)*

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (K-12)
- **Faixa Etaria / Amostra ($N$):** *(Ex: N = 1.250 estudantes, 12-16 anos)*
- **Publico-alvo Avaliado:** Predição de Risco de Abandono Escolar no K-12
- **Fonte dos Dados / Dataset:** *(Ex: Sistema de Gestao Escolar, registros clinicos, questionarios)*

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** *(Identificar na leitura ou N/A)*
- **Natureza da Ferramenta:** (Instrumento psicometrico tradicional / Escala clinica / Ferramenta digitalizada / Questionario de triagem)
- **Forma de Aplicacao:** (Autorrelato do aluno / Relato dos pais / Relato dos professores / Entrevista clinica)
- **Finalidade:** (Diagnostico diferencial / Triagem inicial / Avaliacao de evolucao)

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** (Machine Learning Supervisionado / Nao Supervisionado / Deep Learning / Early Warning System - EWS / Analise Estatistica Avancada / XAI)
- **Algoritmos Empregados:** [[Random_Forest]], [[XGBoost]]
- **Tarefa do Modelo:** (Classificacao binaria [risco sim/nao] / Regressao [probabilidade de infrequencia] / Clustering [perfis de comportamento])
- **Estagio de Deteccao:** (Alerta precoce / deteccao preventiva vs. diagnostico a posteriori)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** (Ansiedade de separacao, ansiedade social, depressao, estresse, regulacao emocional, somatizacao)
- **Variaveis Comportamentais / Historico:** (Padrao de faltas/atrasos, historico de notas, engajamento escolar, conflitos, bullying)
- **Variaveis Familiares / Sociodemograficas:** (Estrutura familiar, dinamica parental, renda, historico medico)
- **Variaveis Institucionais / Contextuais:** (Clima escolar, relacao professor-aluno, localizacao da escola)
- **Features Mais Relevantes Identificadas:** (Feature importance / SHAP / coeficientes principais)

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** (Alfa de Cronbach, Omega de McDonald, Validade convergente/discriminante)
- **Metricas Computacionais (ML):** (Acuracia, Sensibilidade/Recall, Precisao, F1-Score, AUC-ROC, MCC)
- **Estrategia de Validacao:** (K-Fold Cross-validation, split temporal treino/teste, validacao externa)
- **Desafios Metodologicos Relatados:** (Desbalanceamento de classes, dados faltantes/ruidosos, tamanho restrito da amostra)
- **Aspectos Eticos e Transparencia (XAI):** (Privacidade dos dados dos alunos, interpretabilidade do modelo, mitigacao de vies)
- **Limitacoes Declaradas:** 
- **Direcoes Futuras:** 

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 0 | |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 0 | |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 0 | |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 0 | |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 0 | |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **/ 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
