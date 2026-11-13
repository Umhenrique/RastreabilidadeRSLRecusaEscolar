---
id: S0290
study_id: S0290
title: "Explainable Ensemble Learning for Student Dropout Prediction in Conflict-Affected Educational Systems"
year: 2026
database: "IEEE Xplore"
venue: "2026 IEEE 5th International Maghreb Meeting of the Conference on Sciences and Techniques of Automatic Control and Computer Engineering (MI-STA)"
doi: "10.1109/MI-STA68962.2026.11511168"
url: ""
status: "[Pendente Leitura Completa]"
qa_score: 0
population_scope: "Ensino Secundário / Médio"
intervention_scope: "Ensemble Learning (XGBoost/RF) + XAI (LIME)"
outcome_scope: "Risco de Evasão Escolar + Fatores de Estresse e Ansiedade"
authors:
  - "Amna Abas"
  - "Mansour Essgaer"
  - "Llahm Ben Dalla"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
  - "[[Explicabilidade_XAI]]"
  - "[[Random_Forest]]"
  - "[[XGBoost]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/ieee_xplore
  - fenomeno/absenteismo_cronico
---
# S0290: Explainable Ensemble Learning for Student Dropout Prediction in Conflict-Affected Educational Systems

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0290`
> - **Autores:** Amna Abas, Mansour Essgaer, Llahm Ben Dalla
> - **Ano:** 2026
> - **Veículo (Venue):** *2026 IEEE 5th International Maghreb Meeting of the Conference on Sciences and Techniques of Automatic Control and Computer Engineering (MI-STA)*
> - **Base de Origem:** `IEEE Xplore` (Bases: `['IEEE Xplore']`)
> - **DOI:** [10.1109/MI-STA68962.2026.11511168](https://doi.org/10.1109/MI-STA68962.2026.11511168)
> - **URL:** Não informado
> - **Status da Extração:** `[Pendente Leitura Completa]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> This study investigates higher-education nonenrollment among secondary school graduates in Libya’s Fezzan region, formulated as a binary classification task distinguishing Continued Enrollment from Dropout Risk. A synthetic target variable was created using a rule-based scoring mechanism integrating risk and protective indicators. Advanced feature engineering produced composite indices—Parental Engagement, Student Commitment, Resource Availability, and Stress-Anxiety—while class imbalance was handled using SMOTE. Several feature-selection methods were evaluated, with LASSO proving most effective. Two ensemble models, Random Forest (RF) and XGBoost (XGB), were compared. Results show that XGBoost outperformed RF, achieving a higher F1-score and better capturing nonlinear relationships, while RF provided stable but lower performance. LIME-based interpretability indicated that high anxiety and reliance on academic support increased dropout risk, whereas strong resources and student commitment supported continuation. These findings highlight the importance of parental engagement, mental-health support, and socio-economic assistance to improve higher-education retention.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Ensino Secundário / Médio
- **Intervencao/Tecnologia (Intervention Scope):** Ensemble Learning (XGBoost/RF) + XAI (LIME)
- **Desfecho (Outcome Scope):** Risco de Evasão Escolar + Fatores de Estresse e Ansiedade
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Utiliza modelos de ensemble (XGBoost e Random Forest) integrados à interpretabilidade por IA Explicável (XAI via LIME) para predizer risco de abandono no ensino secundário, analisando variáveis compostas de estresse-ansiedade (Stress-Anxiety) e apoio parental. Responde a RQ2, RQ3 e RQ4.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0290`
- **Titulo Completo:** Explainable Ensemble Learning for Student Dropout Prediction in Conflict-Affected Educational Systems
- **Autores:** Amna Abas, Mansour Essgaer, Llahm Ben Dalla
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** 2026 IEEE 5th International Maghreb Meeting of the Conference on Sciences and Techniques of Automatic Control and Computer Engineering (MI-STA)
- **DOI:** [10.1109/MI-STA68962.2026.11511168](https://doi.org/10.1109/MI-STA68962.2026.11511168)
- **Base de Dados:** IEEE Xplore
- **Pais/Regiao de Realizacao do Estudo:** *(Preencher durante leitura completa)*

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Secundário / Médio
- **Faixa Etaria / Amostra ($N$):** *(Ex: N = 1.250 estudantes, 12-16 anos)*
- **Publico-alvo Avaliado:** Risco de Evasão Escolar + Fatores de Estresse e Ansiedade
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
- **Algoritmos Empregados:** [[Explicabilidade_XAI]], [[Random_Forest]], [[XGBoost]]
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
