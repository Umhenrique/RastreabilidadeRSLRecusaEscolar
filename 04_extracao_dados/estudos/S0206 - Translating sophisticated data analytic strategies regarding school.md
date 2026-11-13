---
id: S0206
study_id: S0206
title: "Translating sophisticated data analytic strategies regarding school attendance and absenteeism into targeted educational policy"
year: 2023
database: "Web of Science"
venue: "IMPROVING SCHOOLS"
doi: "10.1177/13654802231174986"
url: ""
status: "[Pendente Leitura Completa]"
qa_score: 0
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
> - **Status da Extração:** `[Pendente Leitura Completa]`

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
- **Pais/Regiao de Realizacao do Estudo:** *(Preencher durante leitura completa)*

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (K-12)
- **Faixa Etaria / Amostra ($N$):** *(Ex: N = 1.250 estudantes, 12-16 anos)*
- **Publico-alvo Avaliado:** Predição de Absenteísmo Crônico Escolar
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
- **Algoritmos Empregados:** SVM, [[Early_Warning_Systems]], [[Random_Forest]]
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
