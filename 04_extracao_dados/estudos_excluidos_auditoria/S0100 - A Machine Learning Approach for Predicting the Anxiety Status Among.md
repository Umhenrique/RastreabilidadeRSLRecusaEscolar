---
id: S0100
study_id: S0100
title: "A Machine Learning Approach for Predicting the Anxiety Status Among O/L Students: A Case Study from Elpitiya Educational Zone"
year: 2026
database: "Scopus"
venue: "2026 6th International Conference on Advanced Research in Computing: Responsible AGI: Balancing Intelligence, Responsibility and Sustainability, ICARC 2026 - Conference Proceedings"
doi: "10.1109/ICARC68737.2026.11453550"
url: "https://www.scopus.com/pages/publications/105036817477?origin=resultslist"
status: "Pendente Leitura Completa"
qa_score: 0
population_scope: "Educação Básica (Crianças)"
intervention_scope: "Random Forest / Ensemble Learning"
outcome_scope: "Rastreio e Diagnóstico de Recusa Escolar / EBSA"
authors:
  - "I.G.G. Umayangana"
  - "R.A.B. Abeygunawardana"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "[[SCARED]]"
algorithms:
  - "[[Random_Forest]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/recusa_escolar
---
# S0100: A Machine Learning Approach for Predicting the Anxiety Status Among O/L Students: A Case Study from Elpitiya Educational Zone

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0100`
> - **Autores:** I.G.G. Umayangana, R.A.B. Abeygunawardana
> - **Ano:** 2026
> - **Veículo (Venue):** *2026 6th International Conference on Advanced Research in Computing: Responsible AGI: Balancing Intelligence, Responsibility and Sustainability, ICARC 2026 - Conference Proceedings*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'IEEE Xplore']`)
> - **DOI:** [10.1109/ICARC68737.2026.11453550](https://doi.org/10.1109/ICARC68737.2026.11453550)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105036817477?origin=resultslist)
> - **Status da Extração:** `Pendente Leitura Completa`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> In Sri Lanka, anxiety and depression are common among youth. This study examined anxiety among O/L students in the Elpitiya Educational Zone, aiming to identify influential factors and apply machine learning for early detection. After getting the IOBSL ethical clearance approval using the SCARED child questionnaire and a stratified cluster sampling method, data were collected from 417 students, representing a population of 7,060. The study constructed one main response variable (Anxiety), and five sub-anxiety categories are Panic Disorder, Generalized Anxiety, Social Anxiety, Separation Anxiety, and School Avoidance. Overall, 61.3% of respondents experienced some level of anxiety, 42.2% with possible anxiety, and 19.1% with specific anxiety. The Random Forest classifier yielded the best performance for predicting anxiety, with an accuracy of 63.33%, an F1-score of 0.6239, a recall of 0.6333, and a precision of 0.6710. For multi-label sub-anxiety classification, a Multioutput Classifier with Random Forest achieved an F1-score of 0.7186 and a Hamming loss of 0.3017. Significant factors influencing anxiety included gender, BMI, screen time, physical activity, sleep duration, parental employment, school type, and academic stress. Notably, female students, those under high academic pressure, and those from smaller schools are more prone to anxiety, while regular exercise and 5-7 hours of sleep help reduce it. The results support the importance of mental well-being through awareness and early intervention. © 2026 IEEE.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Crianças)
- **Intervencao/Tecnologia (Intervention Scope):** Random Forest / Ensemble Learning
- **Desfecho (Outcome Scope):** Rastreio e Diagnóstico de Recusa Escolar / EBSA
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de rastreio e diagnóstico de recusa escolar / ebsa na educação básica (crianças), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0100`
- **Titulo Completo:** A Machine Learning Approach for Predicting the Anxiety Status Among O/L Students: A Case Study from Elpitiya Educational Zone
- **Autores:** I.G.G. Umayangana, R.A.B. Abeygunawardana
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** 2026 6th International Conference on Advanced Research in Computing: Responsible AGI: Balancing Intelligence, Responsibility and Sustainability, ICARC 2026 - Conference Proceedings
- **DOI:** [10.1109/ICARC68737.2026.11453550](https://doi.org/10.1109/ICARC68737.2026.11453550)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** *(Preencher durante leitura completa)*

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (Crianças)
- **Faixa Etaria / Amostra ($N$):** *(Ex: N = 1.250 estudantes, 12-16 anos)*
- **Publico-alvo Avaliado:** Rastreio e Diagnóstico de Recusa Escolar / EBSA
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
- **Algoritmos Empregados:** [[Random_Forest]]
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
