---
id: S0198
study_id: S0198
title: "A Machine Learning Approach to Classifying School Absenteeism Patterns in Youth with ADHD"
year: 2026
database: "Web of Science"
venue: "SCHOOL MENTAL HEALTH"
doi: "10.1007/s12310-026-09893-z"
url: ""
status: "[Incluido Fase 2 - Extracao Concluida]"
qa_score: 10
population_scope: "Educação Básica (Crianças)"
intervention_scope: "Random Forest / Ensemble Learning"
outcome_scope: "Predição de Absenteísmo Crônico Escolar"
authors:
  - "Patrick K. Goh"
  - "Maria A. Rogers"
  - "Ashlyn A. W. W. A. Wong"
  - "Grace S. Mellor"
  - "Jess Whitley"
  - "J. David Smith"
  - "Natasha McBrearty"
  - "Natasha Tatartcheff-Quesnel"
  - "George J. DuPaul"
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
  - base/web_of_science
  - fenomeno/absenteismo_cronico
---
# S0198: A Machine Learning Approach to Classifying School Absenteeism Patterns in Youth with ADHD

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0198`
> - **Autores:** Patrick K. Goh, Maria A. Rogers, Ashlyn A. W. W. A. Wong, Grace S. Mellor, Jess Whitley, J. David Smith, Natasha McBrearty, Natasha Tatartcheff-Quesnel, George J. DuPaul
> - **Ano:** 2026
> - **Veículo (Venue):** *SCHOOL MENTAL HEALTH*
> - **Base de Origem:** `Web of Science` (Bases: `['Web of Science', 'Springer Link']`)
> - **DOI:** [10.1007/s12310-026-09893-z](https://doi.org/10.1007/s12310-026-09893-z)
> - **URL:** Não informado
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Research suggests that youth with attention-deficit/hyperactivity disorder (ADHD) are at elevated risk for chronic absenteeism from school, with long term consequences including educational underachievement, increased mental illness, and economic difficulties later in life. However, limited research has examined whether theoretical models of absenteeism risk derived largely from non-ADHD populations generalize to youth with ADHD, and data-driven methods to identify those at greatest risk remain underdeveloped. Machine learning approaches may complement traditional theory-driven analyses by evaluating whether established risk factors replicate in this population while accounting for complex interactions among predictors. Using data from a clinical sample of youth with ADHD, the current study applied machine learning methods to develop an algorithm capable of classifying youth with patterns of school absenteeism and identifying the most influential problem areas for classification. Parents/caregivers of 194 clinically-referred youth with ADHD (Mage: 10.7 years; SDage = 2.98; 21.1\% girls, 77.3\% boys, 1.5\% transgender or other) reported on their child's history of school absenteeism and also completed 80 items assessing bio-psycho-social-educational problem areas. Random forest analyses yielded a model that classified youth with versus without a history of school absenteeism with acceptable discriminability (AUCs = .75-.79). The most influential problem areas included interfering behavior at school and home, depressed mood or thoughts, inconsistent parenting, attachment disorder, and vulnerability to at-risk behavior. Results provided support for the use of actuarial classification approaches as a complement to theory-driven methods for identifying absenteeism risk in youth with ADHD and may inform early identification and targeted prevention efforts.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Crianças)
- **Intervencao/Tecnologia (Intervention Scope):** Random Forest / Ensemble Learning
- **Desfecho (Outcome Scope):** Predição de Absenteísmo Crônico Escolar
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de predição de absenteísmo crônico escolar na educação básica (crianças), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0198`
- **Titulo Completo:** A Machine Learning Approach to Classifying School Absenteeism Patterns in Youth with ADHD
- **Autores:** Patrick K. Goh, Maria A. Rogers, Ashlyn A. W. W. A. Wong, Grace S. Mellor, Jess Whitley, J. David Smith, Natasha McBrearty, Natasha Tatartcheff-Quesnel, George J. DuPaul
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** SCHOOL MENTAL HEALTH
- **DOI:** [10.1007/s12310-026-09893-z](https://doi.org/10.1007/s12310-026-09893-z)
- **Base de Dados:** Web of Science
- **Pais/Regiao de Realizacao do Estudo:** Canada

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Criancas e Adolescentes, 4-17 anos)
- **Faixa Etaria / Amostra ($N$):** N = 194 jovens com diagnostico de TDAH encaminhados clinicamente (idade 4-17 anos; M = 10,7 anos, DP = 2,98; 77,3% meninos, 21,1% meninas, 1,5% transgenero ou outro; 56% / n = 108 com historico de absenteismo e n = 86 sem historico)
- **Publico-alvo Avaliado:** Jovens com TDAH em atendimento ambulatorial avaliados para classificacao de historico de [[Absenteismo_Cronico|absenteismo escolar]]
- **Fonte dos Dados / Dataset:** Questionario clinico de admissao preenchido por pais/cuidadores entre 2018 e 2020 em uma agencia comunitaria de saude mental infantil localizada em grande cidade canadense

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** Questionario institucional de admissao clinica composto por item binario de historico de absenteismo, checklist de 69 areas problematicas biopsicossocioeducacionais em 8 dominios (Kuder-Richardson 20 = 0,80) e 15 itens de historico diagnostico (totalizando 80 preditores analisados apos exclusao de itens sem variancia)
- **Natureza da Ferramenta:** Checklist clinico de triagem biopsicossocioeducacional (respostas binarias sim/nao)
- **Forma de Aplicacao:** Relato dos pais/cuidadores junto a assistente de caso clinico na admissao ambulatorial
- **Finalidade:** Triagem inicial e estratificacao atuarial do risco de absenteismo escolar em jovens com TDAH

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Machine Learning Supervisionado (Ensemble Learning) com ranqueamento de importancia de variaveis
- **Algoritmos Empregados:** [[Random_Forest]] (1.000 arvores, ajuste de `mtry` entre 2 e 80 via pacote `caret` no R 4.3.2; comparacao tentada com Regressao Logistica, que nao convergiu)
- **Tarefa do Modelo:** Classificacao binaria (com vs. sem historico de absenteismo escolar), avaliada com limiar padrao (0,50) e limiar ajustado para alta sensibilidade (0,42)
- **Estagio de Deteccao:** Triagem atuarial / alerta precoce prospectivo (embora modelado sobre historico retrospectivo de absenteismo)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Humor ou pensamentos depressivos, humor ansioso, transtornos comorbidos (ansiedade 43,3%, transtorno desafiador opositivo 34,0%, depressao 13,9%, TEA 13,9%, TOC 8,2%, transtorno de apego 5,2%, transtorno de conduta 4,1%) e isolamento social
- **Variaveis Comportamentais / Historico:** Comportamento disruptivo/interferente na escola e em casa, vulnerabilidade a comportamentos de risco, dificuldades de aprendizagem, vitimizacao/bullying e historico de absenteismo
- **Variaveis Familiares / Sociodemograficas:** Parentalidade inconsistente, incapacidade da familia de atender as necessidades do jovem, dinamicas familiares, idade, genero e identidade cultural
- **Variaveis Institucionais / Contextuais:** Dificuldades de acesso a servicos comunitarios e problemas escolares (nao incluiu variaveis sistemicas como clima escolar ou transporte)
- **Features Mais Relevantes Identificadas:** Top 6 preditores com escore de importancia > 50 (escala 0-100 por permutacao): (1) comportamento interferente na escola, (2) humor ou pensamentos depressivos, (3) comportamento interferente em casa, (4) parentalidade inconsistente, (5) transtorno de apego e (6) vulnerabilidade a comportamentos de risco; idade e genero nao aumentaram o desempenho (delta AUC = 0,002, p = 0,95)

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** Kuder-Richardson 20 (KR-20) = 0,80 para o checklist de 69 areas problematicas
- **Metricas Computacionais (ML):** Validacao cruzada no treino (n = 131): AUC = 0,75 (DP = 0,08), Acuracia = 0,69 (vs. No Information Rate 0,56, p < 0,001), Sensibilidade = 0,68, Especificidade = 0,70, Kappa = 0,38. Amostra de teste independente (n = 63): AUC = 0,79 (IC 95% [0,68, 0,90]); com threshold 0,50: Acuracia = 0,73 (p = 0,003), Sensibilidade = 0,76 (Tabela 3) / 0,74 (texto), Especificidade = 0,69 (Tabela 3) / 0,71 (texto), Kappa = 0,46; com threshold 0,42: Sensibilidade = 0,80, Especificidade = 0,57, Acuracia = 0,70
- **Estrategia de Validacao:** Split aleatorio estratificado 67% treino (n = 131) / 33% teste independente (n = 63) e validacao cruzada 5-fold repetida 5 vezes no treino
- **Desafios Metodologicos Relatados:** Tamanho amostral relativamente reduzido para ML (N = 194), nao convergencia da regressao logistica com elevado numero de preditores, ausencia de definicao operacional formal de absenteismo no item de entrada e respostas binarias que limitam granularidade
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao por IRB e consentimento informado; codigo em R disponivel no Open Science Framework (OSF); interpretabilidade via escores de importancia de variaveis por permutacao
- **Limitacoes Declaradas:** Amostra clinica pequena e predominantemente masculina (77,3% meninos), restringindo generalizacao para amostras comunitarias ou meninas; dados transversais e retrospectivos baseados apenas no relato dos pais/cuidadores sem confirmacao clinica independente dos diagnosticos; ausencia de fatores sistemicos (qualidade da escola, clima escolar, transporte)
- **Direcoes Futuras:** Validar prospectivamente em amostras maiores, mais diversas e comunitarias; incorporar dados multi-informantes e fatores sistemicos escolares; avaliar utilidade incremental e viabilidade em fluxos reais de clinicas e escolas

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo e quatro hipoteses explicitamente definidos para classificacao de absenteismo em jovens com TDAH via Random Forest. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Amostra (N = 194), instrumento (KR-20 = 0,80), split estratificado 67/33, 5x5-fold CV, 1.000 arvores e ajuste de `mtry` descritos de forma replicavel (codigo no OSF). |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta KR-20 = 0,80, AUC-ROC (0,75 CV / 0,79 teste), Acuracia, Sensibilidade, Especificidade, Kappa e VPP/VPN. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa 80 variaveis biopsicossocioeducacionais e diagnosticos comorbidos, identificando depressao, comportamento disruptivo, parentalidade inconsistente e apego. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute detalhadamente vies do relato parental unico, amostra clinica masculina, natureza transversal/retrospectiva e ausencia de fatores sistemicos. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **10 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
