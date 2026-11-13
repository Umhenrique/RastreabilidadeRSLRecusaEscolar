---
id: S0118
study_id: S0118
title: "Predicting Adverse Childhood Experiences from Family Environment Factors: A Machine Learning Approach"
year: 2025
database: "Scopus"
venue: "Behavioral Sciences"
doi: "10.3390/bs15091216"
url: "https://www.scopus.com/pages/publications/105017425850?origin=resultslist"
status: "Pendente Leitura Completa"
qa_score: 0
population_scope: "Educação Básica (Adolescentes)"
intervention_scope: "Random Forest / Ensemble Learning"
outcome_scope: "Predição de Absenteísmo Crônico Escolar"
authors:
  - "Nii Adjetey Tawiah"
  - "Emmanuel A. Appiah"
  - "Felisha White"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
  - "[[Random_Forest]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/absenteismo_cronico
---
# S0118: Predicting Adverse Childhood Experiences from Family Environment Factors: A Machine Learning Approach

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0118`
> - **Autores:** Nii Adjetey Tawiah, Emmanuel A. Appiah, Felisha White
> - **Ano:** 2025
> - **Veículo (Venue):** *Behavioral Sciences*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.3390/bs15091216](https://doi.org/10.3390/bs15091216)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105017425850?origin=resultslist)
> - **Status da Extração:** `Pendente Leitura Completa`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Adverse childhood experiences (ACEs) are associated with profound long-term health and developmental consequences. However, current identification strategies are largely reactive, often missing opportunities for early intervention. Therefore, the potential of machine learning to proactively identify children at risk of ACE exposure needs to be explored. Using nationally representative data from 63,239 children in the 2018–2020 National Survey of Children’s Health (NSCH) after listwise deletion, we trained and validated multiple machine learning models to predict ACE exposure categorized as none, one, or two or more ACEs. Model performance was assessed using accuracy, precision, recall, F1 scores, and area under the curve (AUC) metrics with 5-fold cross-validation. The Random Forest model achieved the highest predictive accuracy (82%) and demonstrated strong performance across ACE categories. Key predictive features included child sex (female), food insufficiency, school absenteeism, quality of parent–child communication, and experiences of bullying. The model yielded high performance in identifying children with no ACEs (F1 = 0.89) and moderate performance for those with multiple ACEs (F1 = 0.64). However, performance for the single ACE category was notably lower (F1 = 0.55), indicating challenges in predicting this intermediate group. These findings suggest that family environment factors can be leveraged to predict ACE exposure with clinically meaningful accuracy, offering a foundation for proactive screening protocols. However, implementation must carefully address systematic selection bias, clinical utility limitations, and ethical considerations regarding predictive modeling of vulnerable children. © 2025 by the authors.

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
- **ID do Estudo:** `S0118`
- **Titulo Completo:** Predicting Adverse Childhood Experiences from Family Environment Factors: A Machine Learning Approach
- **Autores:** Nii Adjetey Tawiah, Emmanuel A. Appiah, Felisha White
- **Ano de Publicacao:** 2025
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Behavioral Sciences
- **DOI:** [10.3390/bs15091216](https://doi.org/10.3390/bs15091216)
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
- **Nome do Instrumento/Escala:** *(Identificar na leitura ou N/A)*
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
