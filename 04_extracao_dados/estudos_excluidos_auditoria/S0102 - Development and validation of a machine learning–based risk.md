---
id: S0102
study_id: S0102
title: "Development and validation of a machine learning–based risk prediction model for non-suicidal self-injury in adolescents"
year: 2026
database: "Scopus"
venue: "Frontiers in Psychiatry"
doi: "10.3389/fpsyt.2026.1837161"
url: "https://www.scopus.com/pages/publications/105041030226?origin=resultslist"
status: "Pendente Leitura Completa"
qa_score: 0
population_scope: "Educação Básica (Adolescentes)"
intervention_scope: "Random Forest / Ensemble Learning"
outcome_scope: "Predição de Absenteísmo Crônico Escolar"
authors:
  - "Yujun Zhao"
  - "Qian Wang"
  - "Wei Liu"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "[[SCARED]]"
algorithms:
  - "Regressão Logística"
  - "SVM"
  - "[[Explicabilidade_XAI]]"
  - "[[Random_Forest]]"
  - "[[XGBoost]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/absenteismo_cronico
---
# S0102: Development and validation of a machine learning–based risk prediction model for non-suicidal self-injury in adolescents

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0102`
> - **Autores:** Yujun Zhao, Qian Wang, Wei Liu
> - **Ano:** 2026
> - **Veículo (Venue):** *Frontiers in Psychiatry*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus']`)
> - **DOI:** [10.3389/fpsyt.2026.1837161](https://doi.org/10.3389/fpsyt.2026.1837161)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105041030226?origin=resultslist)
> - **Status da Extração:** `Pendente Leitura Completa`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Background – Non-suicidal self-injury (NSSI) among adolescents has long been an important social issue. This study aims to construct a predictive model for NSSI based on machine learning models. Methods – A retrospective cohort study design was adopted, including 588 adolescent patients who received psychological and psychiatric assessments. The occurrence of NSSI behavior was used as the outcome variable. Candidate predictors including demographic characteristics, psychological and emotional status, behavioral characteristics, and peer support were collected. The dataset was randomly divided into a training set and a test set at a ratio of 7:3. By comparing the performance of four machine learning models—multiple logistic regression (MLR), random forest (RF), support vector machine (SVM), and eXtreme Gradient Boosting (XGBoost)—at different time points (T1, T2, T3) using area under the curve (AUC), accuracy, precision, recall, and F1 score, the optimal model was selected. The Shapley additive explanations (SHAP) method was further used to conduct interpretability analysis for the optimal model. Results – The incidence rates of NSSI at T1, T2, and T3 were approximately 24%, 23%, and 22%, respectively. The SVM model demonstrated superior discrimination ability and stability in predicting the risk of NSSI among adolescents, with AUC values all greater than 0.75 and recall and F1 scores both higher than 0.7. SHAP analyses at all three time points consistently showed that suicide-related ideation and behaviors, school bullying, and depressive status had high contributions to the prediction of NSSI risk. Conclusion – The support vector machine model performed best in predicting NSSI among adolescents. Suicide-related behaviors are important predictors of NSSI. The findings of this study help improve the early identification of adolescents at high risk of NSSI and provide evidence for developing targeted prevention and intervention strategies. Copyright © 2026 Zhao, Wang and Liu.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Adolescentes)
- **Intervencao/Tecnologia (Intervention Scope):** Random Forest / Ensemble Learning
- **Desfecho (Outcome Scope):** Predição de Absenteísmo Crônico Escolar
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de predição de absenteísmo crônico escolar na educação básica (adolescentes), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0102`
- **Titulo Completo:** Development and validation of a machine learning–based risk prediction model for non-suicidal self-injury in adolescents
- **Autores:** Yujun Zhao, Qian Wang, Wei Liu
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Frontiers in Psychiatry
- **DOI:** [10.3389/fpsyt.2026.1837161](https://doi.org/10.3389/fpsyt.2026.1837161)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** *(Preencher durante leitura completa)*

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (Adolescentes)
- **Faixa Etaria / Amostra ($N$):** *(Ex: N = 1.250 estudantes, 12-16 anos)*
- **Publico-alvo Avaliado:** Predição de Absenteísmo Crônico Escolar
- **Fonte dos Dados / Dataset:** *(Ex: Sistema de Gestao Escolar, registros clinicos, questionarios)*

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** [[SCARED]]
- **Natureza da Ferramenta:** (Instrumento psicometrico tradicional / Escala clinica / Ferramenta digitalizada / Questionario de triagem)
- **Forma de Aplicacao:** (Autorrelato do aluno / Relato dos pais / Relato dos professores / Entrevista clinica)
- **Finalidade:** (Diagnostico diferencial / Triagem inicial / Avaliacao de evolucao)

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** (Machine Learning Supervisionado / Nao Supervisionado / Deep Learning / Early Warning System - EWS / Analise Estatistica Avancada / XAI)
- **Algoritmos Empregados:** Regressão Logística, SVM, [[Explicabilidade_XAI]], [[Random_Forest]], [[XGBoost]]
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
