---
id: S0206
study_id: S0206
title: "Translating sophisticated data analytic strategies regarding school attendance and absenteeism into targeted educational policy"
year: 2023
database: "Web of Science"
venue: "IMPROVING SCHOOLS"
doi: "10.1177/13654802231174986"
url: ""
status: "[Excluido Fase 2 - Criterio EC1 (Sintese de politicas - usar no referencial teorico)]"
qa_score: 8
population_scope: "Educação Básica (K-12)"
intervention_scope: "Random Forest / Ensemble Learning"
outcome_scope: "Predição de Absenteísmo Crônico Escolar"
authors:
  - "Christopher A. Kearney"
  - "Joshua Childs"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
  - "SVM"
  - "[[Early_Warning_Systems]]"
  - "[[Random_Forest]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/web_of_science
  - fenomeno/absenteismo_cronico
---
# S0206: Translating sophisticated data analytic strategies regarding school attendance and absenteeism into targeted educational policy

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0206`
> - **Autores:** Christopher A. Kearney, Joshua Childs
> - **Ano:** 2023
> - **Veículo (Venue):** *IMPROVING SCHOOLS*
> - **Base de Origem:** `Web of Science` (Bases: `['Web of Science']`)
> - **DOI:** [10.1177/13654802231174986](https://doi.org/10.1177/13654802231174986)
> - **URL:** Não informado
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC1 (Sintese de politicas - usar no referencial teorico)]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> School attendance and absenteeism are critical targets of educational policies and practices that often depend heavily on aggregated attendance/absenteeism data. School attendance/absenteeism data in aggregated form, in addition to having suspect quality and utility, minimizes individual student variation, distorts detailed and multilevel modeling, and obscures underlying causes and disparities of absenteeism. Recent advances in data analytics/mining and modeling may assist researchers and other stakeholders by evaluating large-scale data sets in more targeted ways to identify key root causes and patterns of school absenteeism in a particular community, school, or group of students. This would allow for more accurate educational policies tailored to unique local conditions and student/family circumstances. This article provides a summary of recent algorithm- and model-based efforts in this regard. Algorithm-based efforts include classification and regression tree analysis, ensemble analysis, support vector machines, receiver operating characteristic analysis, and random forests. Model-based efforts include multilevel modeling, structural equation modeling, latent class analysis, and meta-analytic modeling. We then illustrate how these efforts can enhance a full and nuanced understanding of the root, interconnected causes of absenteeism, improve early warning systems, and assist multi-tiered systems of support interventions for absenteeism.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (K-12)
- **Intervencao/Tecnologia (Intervention Scope):** Random Forest / Ensemble Learning
- **Desfecho (Outcome Scope):** Predição de Absenteísmo Crônico Escolar
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de predição de absenteísmo crônico escolar na educação básica (k-12), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0206`
- **Titulo Completo:** Translating sophisticated data analytic strategies regarding school attendance and absenteeism into targeted educational policy
- **Autores:** Christopher A. Kearney, Joshua Childs
- **Ano de Publicacao:** 2023
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** IMPROVING SCHOOLS
- **DOI:** [10.1177/13654802231174986](https://doi.org/10.1177/13654802231174986)
- **Base de Dados:** Web of Science
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (University of Nevada, Las Vegas; University of Texas at Austin)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (K-12)
- **Faixa Etaria / Amostra ($N$):** N/A - Artigo de revisao/sintese metodologica e de politicas educacionais abrangendo estudantes K-12 em grandes bases analisadas nos estudos revisados
- **Publico-alvo Avaliado:** Estudantes K-12 em risco de [[Absenteismo_Cronico|absenteismo cronico]] e evasao escolar, com enfase em subgrupos vulneraveis e politicas educacionais locais
- **Fonte dos Dados / Dataset:** Sintese de estudos baseados em grandes conjuntos de dados educacionais distritais, estaduais e nacionais (EUA, Suecia, Coreia do Sul, Australia, entre outros)

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** N/A (Foca em dados administrativos desagregados, pesquisas de clima escolar e indicadores socioemocionais, nao em um instrumento psicometrico especifico)
- **Natureza da Ferramenta:** Sistemas de dados analiticos educacionais e levantamentos contextuais locais
- **Forma de Aplicacao:** Registros escolares longitudinais, entrevistas qualitativas com equipe escolar e questionarios de clima/fatores de risco
- **Finalidade:** Analise de causa raiz (Root Cause Analysis), aprimoramento de EWS e direcionamento de politicas locais e MTSS

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Machine Learning Supervisionado, Ensemble Learning, [[Early_Warning_Systems|Early Warning System - EWS]] e Modelagem Estatistica Avancada
- **Algoritmos Empregados:** Abordagens baseadas em algoritmos: CART, Ensemble Analysis (CHAID), SVM, Boosting, LASSO, ROC Analysis, [[Random_Forest]]; abordagens baseadas em modelos: Multilevel Modeling, SEM, Latent Class Analysis (LCA) e Meta-analytic Modeling; aplicados a [[Early_Warning_Systems]]
- **Tarefa do Modelo:** Classificacao de risco de absenteismo cronico e evasao, segmentacao de perfis/subgrupos e identificacao de causas raiz locais
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (EWS desagregado e adaptado a condicoes locais, integrado a Tiers 1, 2 e 3 de MTSS)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Sintomas internalizantes, problemas de saude mental, disturbio emocional grave, comportamento externalizante e aprendizagem socioemocional (SEL)
- **Variaveis Comportamentais / Historico:** Faltas nao autorizadas, atrasos, saidas antecipadas, GPA, historico de suspensoes/expulsoes, reprovacao, participacao extracurricular e engajamento escolar
- **Variaveis Familiares / Sociodemograficas:** Pobreza/baixa renda, inseguranca habitacional e alimentar, violencia na vizinhanca, escolaridade parental, familia monoparental, raca/etnia, status de migrante e elegibilidade a IEP/educacao especial
- **Variaveis Institucionais / Contextuais:** Clima escolar, seguranca na escola, rotatividade docente, transporte escolar, politicas punitivas de tolerancia zero e mobilidade/mudancas de escola
- **Features Mais Relevantes Identificadas:** Variam conforme localidade e severidade: GPA baixo, suspensoes, idade avancada para a serie, mudanca de escola, inseguranca habitacional/alimentar, clima escolar negativo, sintomas internalizantes/externalizantes e participacao extracurricular

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** Tamanhos de efeito em modelagem meta-analitica e indices de ajuste em SEM (citados dos estudos sintetizados)
- **Metricas Computacionais (ML):** Menciona uso de curvas ROC/AUC e desempenho diferencial (ex.: Random Forest prevendo melhor nao-evasao do que evasao), sem tabela comparativa de metricas numericas proprias
- **Estrategia de Validacao:** Revisao narrativa/sintese de estudos empiricos baseados em algoritmos e modelos aplicados a politicas educacionais
- **Desafios Metodologicos Relatados:** Distorcao por uso de dados agregados (perda de variacao individual e mascaramento de disparidades), baixa qualidade e manipulacao de registros de faltas, arbitrariedade do limiar de 10% e instabilidade de indicadores entre subgrupos e series
- **Aspectos Eticos e Transparencia (XAI):** Enfase em interseccionalidade, reducao de politicas punitivas desproporcionais contra grupos minoritarios, uso de dados desagregados para equidade e traducao transparente para formuladores de politicas
- **Limitacoes Declaradas:** Dificuldade de implementacao de estrategias analiticas sofisticadas em escolas com restricoes orcamentarias; transformacoes recentes (ensino hibrido/virtual pos-pandemia, crises climaticas) que exigem novas definicoes e metricas de frequencia
- **Direcoes Futuras:** Integrar sistemas interagencias em tempo real com dashboards acessiveis, combinar dados quantitativos e qualitativos, calibrar limiares empiricos locais para MTSS e investigar impactos do ensino virtual/hibrido

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo claro de sintetizar estrategias analiticas baseadas em algoritmos e modelos para traduzir em politicas educacionais, EWS e MTSS. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 1 | Organizacao clara entre metodos algoritmo-baseados e modelo-baseados, porem revisao narrativa sem protocolo sistematico de busca/selecao. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Cita aplicacoes de ROC/AUC e modelos sintetizados, sem apresentar benchmark quantitativo comparativo proprio. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa amplamente fatores socioemocionais, clima escolar, pobreza, saude mental e mecanismos contextuais do absenteismo. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute criticamente limitacoes de dados agregados, manipulacao de registros, vieses em politicas punitivas e desafios pos-pandemia. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **8 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
