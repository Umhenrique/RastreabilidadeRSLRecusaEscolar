---
id: S0290
study_id: S0290
title: "Explainable Ensemble Learning for Student Dropout Prediction in Conflict-Affected Educational Systems"
year: 2026
database: "IEEE Xplore"
venue: "2026 IEEE 5th International Maghreb Meeting of the Conference on Sciences and Techniques of Automatic Control and Computer Engineering (MI-STA)"
doi: "10.1109/MI-STA68962.2026.11511168"
url: ""
status: "[Incluido Fase 2 - Extracao Concluida]"
qa_score: 9
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
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

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
- **Pais/Regiao de Realizacao do Estudo:** Libia (Sabha, regiao de Fezzan)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Secundario / Medio (transicao para o ensino superior)
- **Faixa Etaria / Amostra ($N$):** N = 1.158 estudantes do ensino medio (de populacao de 2.635 examinandos em 5 escolas, 2023; faixas de 17-18 e 19-22 anos; 1.129 registros rotulados na distribuicao final: 84,0% [949] continuam vs. 16,0% [180] risco de evasao)
- **Publico-alvo Avaliado:** Estudantes concluintes do ensino secundario em contexto afetado por conflito armado (risco de evasao / nao-matricula no ensino superior)
- **Fonte dos Dados / Dataset:** Questionario estruturado de 34 itens aplicado em 5 escolas de Sabha, Libia (2023), adaptado de estudos previos para o contexto sociocultural local

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** Questionario estruturado de 34 itens (adaptado) + 4 indices compostos engenheirados (PES, SCI, RAS, SAI); sem escala clinica padronizada (ex.: SRAS-R/SCARED)
- **Natureza da Ferramenta:** Questionario de triagem multidimensional (6 categorias de atributos) e indicadores compostos
- **Forma de Aplicacao:** Autorrelato do aluno
- **Finalidade:** Triagem inicial e perfilamento exploratorio de risco de evasao / nao-transicao

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Machine Learning Supervisionado (Ensemble Learning: Bagging e Boosting) com IA Explicavel ([[Explicabilidade_XAI]] via LIME), selecao de features (LASSO, RFE, Mutual Information, Chi-Squared) e balanceamento SMOTE ([[Early_Warning_Systems]])
- **Algoritmos Empregados:** [[XGBoost]], [[Random_Forest]], LASSO, [[Explicabilidade_XAI]] (LIME)
- **Tarefa do Modelo:** Classificacao binaria (`Continued Enrollment` vs. `Dropped Out`) sobre variavel-alvo sintetica construida por heuristicas baseadas em regras
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (perfilamento exploratorio de risco na transicao ensino medio-superior)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Stress and Anxiety Index (SAI: frequencia de ansiedade, disciplinas dificeis, estresse autoavaliado), ansiedade nos estudos, motivacao para aprender, aspiracao ao ensino superior, bem-estar fisico/saude
- **Variaveis Comportamentais / Historico:** Faltas (1-7, 8-20, >20 dias), horas de estudo (<2, 2-5, >5h), historico de reprovacoes, Student Commitment Index (SCI), socializacao com amigos, engajamento em ensino a distancia
- **Variaveis Familiares / Sociodemograficas:** Parental Engagement Score (PES), escolaridade e ocupacao materna/paterna, estado civil dos pais, coesao familiar, suporte financeiro, tamanho da familia, genero, idade, area residencial
- **Variaveis Institucionais / Contextuais:** Tipo de escola (publica/privada/homeschool), tempo de deslocamento, eficacia docente, acesso a internet, posse de dispositivo eletronico (RAS), aulas particulares, contexto de conflito armado
- **Features Mais Relevantes Identificadas:** Consenso entre >=3 seletores: PES, SCI, SAI, desejo de cursar ensino superior, motivacao para aprender, engajamento em ensino a distancia, eficacia dos professores, socializacao com amigos e bem-estar fisico. No LIME: deslocamento >=30 min, posse de dispositivo, ansiedade nos estudos, eficacia docente e tutoria privada

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A (nao reporta Alfa de Cronbach ou validade fatorial do questionario)
- **Metricas Computacionais (ML):** XGBoost: Acuracia = 0,941, Precisao = 0,941, Recall = 0,941, F1-Score = 0,941, LogLoss = 0,161, CV Accuracy = 0,940, CV F1 = 0,939. Random Forest: Acuracia = 0,939, Precisao = 0,939, Recall = 0,939, F1-Score = 0,939, LogLoss = 0,161, CV Accuracy = 0,935, CV F1 = 0,934
- **Estrategia de Validacao:** Split estratificado 70% treino / 30% teste + GridSearchCV com 10-fold cross-validation
- **Desafios Metodologicos Relatados:** Ausencia de rotulos reais (ground truth) exigindo alvo sintetico por regras; desbalanceamento de classes (84% vs. 16%) mitigado com SMOTE; risco de overfitting tratado com regularizacao e profundidade limitada (XGBoost `max_depth=3`)
- **Aspectos Eticos e Transparencia (XAI):** Uso de LIME ([[Explicabilidade_XAI]]) para explicabilidade local por estudante, mitigando o problema de caixa-preta e apoiando intervencoes direcionadas
- **Limitacoes Declaradas:** Dependencia de variavel-alvo sintetica baseada em heuristicas; as metricas refletem o aprendizado do proxy baseado em regras, e nao uma previsao definitiva das taxas reais de evasao
- **Direcoes Futuras:** Validacao com dados longitudinais reais de evasao e implementacao de politicas de apoio psicossocial, engajamento parental e suporte socioeconomico

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo de estabelecer framework explicavel de ML para perfilamento exploratorio de risco de evasao / nao-transicao em Sabha, Libia. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha amostra (N=1.158), questionario (34 itens), formulas dos 4 indices compostos, alvo sintetico, SMOTE, selecao LASSO, split 70/30, 10-fold GridSearchCV, hiperparametros e LIME. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Acuracia, Precisao, Recall, F1-Score, LogLoss, CV Accuracy e CV F1 para XGBoost e Random Forest, alem de comparacao entre 4 tecnicas de selecao de features. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa estresse e ansiedade (SAI), motivacao, aspiracoes, coesao familiar, engajamento parental (PES), socializacao e o impacto do conflito armado. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 1 | Reconhece explicitamente a limitacao da variavel-alvo sintetica (proxy heuristico sem ground truth real), mas nao discute o potencial vazamento entre features e regras do alvo ou vieses de autorrelato. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
