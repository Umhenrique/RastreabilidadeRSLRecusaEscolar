---
id: S0179
study_id: S0179
title: "Predicting mental health trajectories after potentially traumatic events: a machine learning approach"
year: 2026
database: "Scopus"
venue: "European Child and Adolescent Psychiatry"
doi: "10.1007/s00787-026-03022-6"
url: "https://www.scopus.com/pages/publications/105034756985?origin=resultslist"
status: "Pendente Leitura Completa"
qa_score: 0
population_scope: "Educação Básica (Adolescentes)"
intervention_scope: "Random Forest / Ensemble Learning"
outcome_scope: "Predição de Risco de Abandono Escolar no K-12"
authors:
  - "Dunja Tutus"
  - "Tanmay Nayyar"
  - "Jörg M. Fegert"
  - "Ann-Christin Haag"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
  - "Regressão Logística"
  - "[[Explicabilidade_XAI]]"
  - "[[Random_Forest]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/absenteismo_cronico
---
# S0179: Predicting mental health trajectories after potentially traumatic events: a machine learning approach

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0179`
> - **Autores:** Dunja Tutus, Tanmay Nayyar, Jörg M. Fegert, Ann-Christin Haag
> - **Ano:** 2026
> - **Veículo (Venue):** *European Child and Adolescent Psychiatry*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Springer Link']`)
> - **DOI:** [10.1007/s00787-026-03022-6](https://doi.org/10.1007/s00787-026-03022-6)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105034756985?origin=resultslist)
> - **Status da Extração:** `Pendente Leitura Completa`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> This study aimed to investigate the trajectories of internalizing and externalizing problems following childhood potentially traumatic events (PTEs) and analyse a comprehensive set of baseline variables (PTEs, individual, environmental) to elucidate their predictive role as contributors to different mental health trajectories. The sample consisted of 4,141 participants (M = 9.48, SD = 0.51 years at baseline; 48.7% girls; 72.1% White) from the Adolescent Brain Cognitive Development study who had experienced at least one PTE. Participants’ mental health problems were assessed using the Brief Problem Monitor self-report form. Latent Growth Mixture Modelling was used to identify trajectories of youth´s internalizing and externalizing problems across the six assessments. Machine learning was utilized to investigate 37 predictors of different trajectories. Three distinct trajectories were identified for both internalizing and externalizing problems: “Resilient”, “Mild” and “Moderate chronic”. Predictors of the “Moderate chronic” versus “Resilient” trajectories were identified using machine learning. The three most important predictors of the internalizing problems trajectory were: behavioural inhibition, caregiver internalizing problems, and female gender, whereas predictors of the externalizing problems trajectory were family conflicts, screentime, and a low level of prosocial behaviour. The findings can help characterize individual variation in mental health trajectories following childhood PTEs and provide potential targets for intervention to foster mental health. © The Author(s) 2026.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Adolescentes)
- **Intervencao/Tecnologia (Intervention Scope):** Random Forest / Ensemble Learning
- **Desfecho (Outcome Scope):** Predição de Risco de Abandono Escolar no K-12
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de predição de risco de abandono escolar no k-12 na educação básica (adolescentes), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0179`
- **Titulo Completo:** Predicting mental health trajectories after potentially traumatic events: a machine learning approach
- **Autores:** Dunja Tutus, Tanmay Nayyar, Jörg M. Fegert, Ann-Christin Haag
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** European Child and Adolescent Psychiatry
- **DOI:** [10.1007/s00787-026-03022-6](https://doi.org/10.1007/s00787-026-03022-6)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** *(Preencher durante leitura completa)*

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (Adolescentes)
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
- **Algoritmos Empregados:** Regressão Logística, [[Explicabilidade_XAI]], [[Random_Forest]]
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
