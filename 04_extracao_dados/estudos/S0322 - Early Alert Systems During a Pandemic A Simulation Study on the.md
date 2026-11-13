---
id: S0322
study_id: S0322
title: "Early Alert Systems During a Pandemic: A Simulation Study on the Impact of Concept Drift"
year: 2021
database: "ACM DL"
venue: "LAK21: 11th International Learning Analytics and Knowledge Conference"
doi: "10.1145/3448139.3448190"
url: "https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3448139.3448190"
status: "[Pendente Leitura Completa]"
qa_score: 0
population_scope: "Ensino Médio (High School / Ensino Básico)"
intervention_scope: "Machine Learning em Early Warning Systems"
outcome_scope: "Predição de Abandono Escolar frente a Desvios de Dados"
authors:
  - "Yang Xu"
  - "Kevin Wilson"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
  - "[[Early_Warning_Systems]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/acm_dl
  - fenomeno/absenteismo_cronico
---
# S0322: Early Alert Systems During a Pandemic: A Simulation Study on the Impact of Concept Drift

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0322`
> - **Autores:** Yang Xu, Kevin Wilson
> - **Ano:** 2021
> - **Veículo (Venue):** *LAK21: 11th International Learning Analytics and Knowledge Conference*
> - **Base de Origem:** `ACM DL` (Bases: `['ACM DL']`)
> - **DOI:** [10.1145/3448139.3448190](https://doi.org/10.1145/3448139.3448190)
> - **URL:** [Link da Publicação](https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3448139.3448190)
> - **Status da Extração:** `[Pendente Leitura Completa]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Predictions from early alert systems are increasingly being used by institutions to assist decision-making and support at-risk individuals. Concept drifts caused by the 2020 SARS-CoV-2 pandemic are threatening the performance and usefulness of the machine learning models that power these systems. In this paper, we present an analytical framework that uses imputation-based simulations to perform preliminary evaluation on the extent to which data quality and availability issues impact the performance of machine learning models. Guided by this framework, we studied how these issues would impact the performance of the high school dropout prediction model implemented in the Early Warning System (EWS). Results show that despite the disruptions, this model can still be reasonably useful in assisting decision-making. We discuss the implications of these findings in more general educational contexts and recommend steps in countering the challenges of using predictions from imperfect machine learning models in early alert systems and, more broadly, learning analytic research that uses longitudinal data.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Ensino Médio (High School / Ensino Básico)
- **Intervencao/Tecnologia (Intervention Scope):** Machine Learning em Early Warning Systems
- **Desfecho (Outcome Scope):** Predição de Abandono Escolar frente a Desvios de Dados
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Investiga a robustez e desempenho de modelos de Machine Learning implementados em sistemas de alerta precoce (EWS) para predição de abandono no Ensino Médio (High School Dropout). Responde diretamente às RQ2 e RQ4.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0322`
- **Titulo Completo:** Early Alert Systems During a Pandemic: A Simulation Study on the Impact of Concept Drift
- **Autores:** Yang Xu, Kevin Wilson
- **Ano de Publicacao:** 2021
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** LAK21: 11th International Learning Analytics and Knowledge Conference
- **DOI:** [10.1145/3448139.3448190](https://doi.org/10.1145/3448139.3448190)
- **Base de Dados:** ACM DL
- **Pais/Regiao de Realizacao do Estudo:** *(Preencher durante leitura completa)*

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Médio (High School / Ensino Básico)
- **Faixa Etaria / Amostra ($N$):** *(Ex: N = 1.250 estudantes, 12-16 anos)*
- **Publico-alvo Avaliado:** Predição de Abandono Escolar frente a Desvios de Dados
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
- **Algoritmos Empregados:** [[Early_Warning_Systems]]
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
