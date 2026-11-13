---
id: S0156
study_id: S0156
title: "Predicting louisiana public high school dropout through imbalanced learning techniques"
year: 2019
database: "Scopus"
venue: "Proceedings - 18th IEEE International Conference on Machine Learning and Applications, ICMLA 2019"
doi: "10.1109/ICMLA.2019.00085"
url: "https://www.scopus.com/pages/publications/85080965065?origin=resultslist"
status: "[Pendente Leitura Completa]"
qa_score: 0
population_scope: "Educação Básica (Ensino Médio)"
intervention_scope: "Modelos de Machine Learning / IA e Análise Preditiva"
outcome_scope: "Predição de Risco de Abandono Escolar no K-12"
authors:
  - "Marmar Orooji"
  - "Jianhua Chen"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
  - "Redes Neurais / Deep Learning"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/absenteismo_cronico
---
# S0156: Predicting louisiana public high school dropout through imbalanced learning techniques

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0156`
> - **Autores:** Marmar Orooji, Jianhua Chen
> - **Ano:** 2019
> - **Veículo (Venue):** *Proceedings - 18th IEEE International Conference on Machine Learning and Applications, ICMLA 2019*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'IEEE Xplore']`)
> - **DOI:** [10.1109/ICMLA.2019.00085](https://doi.org/10.1109/ICMLA.2019.00085)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/85080965065?origin=resultslist)
> - **Status da Extração:** `[Pendente Leitura Completa]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> This study is motivated by the magnitude of the problem of Louisiana high school dropout and its negative impacts on individual and public well-being. Our goal is to predict students who are at risk of high school dropout, by examining Louisiana administrative dataset. Due to the imbalanced nature of the dataset, imbalanced learning techniques including resampling, case weighting, and cost-sensitive learning have been applied to enhance the prediction performance on the rare class. Performance metrics used in this study are F-measure, recall and precision of the rare class. We compare the performance of several machine learning algorithms such as neural networks, decision trees and bagging trees in combination with the imbalanced learning approaches using an administrative dataset of size of 366k+ from Louisiana Department of Education. Experiments show that application of imbalanced learning methods produces good results on recall but decreases precision, whereas base classifiers without regard of imbalanced data handling gives better precision but poor recall. Overall application of imbalanced learning techniques is beneficial, yet more studies are desired to improve precision. © 2019 IEEE.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Ensino Médio)
- **Intervencao/Tecnologia (Intervention Scope):** Modelos de Machine Learning / IA e Análise Preditiva
- **Desfecho (Outcome Scope):** Predição de Risco de Abandono Escolar no K-12
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de predição de risco de abandono escolar no k-12 na educação básica (ensino médio), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0156`
- **Titulo Completo:** Predicting louisiana public high school dropout through imbalanced learning techniques
- **Autores:** Marmar Orooji, Jianhua Chen
- **Ano de Publicacao:** 2019
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Proceedings - 18th IEEE International Conference on Machine Learning and Applications, ICMLA 2019
- **DOI:** [10.1109/ICMLA.2019.00085](https://doi.org/10.1109/ICMLA.2019.00085)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** *(Preencher durante leitura completa)*

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (Ensino Médio)
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
- **Algoritmos Empregados:** Redes Neurais / Deep Learning
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
