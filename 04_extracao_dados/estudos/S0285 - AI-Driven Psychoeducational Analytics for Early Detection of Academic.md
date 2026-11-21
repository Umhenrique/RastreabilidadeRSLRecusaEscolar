---
id: S0285
study_id: S0285
title: "AI-Driven Psychoeducational Analytics for Early Detection of Academic Risk in Colombian Schools"
year: 2026
database: "IEEE Xplore"
venue: "2026 IEEE Engineering Education World Conference (EDUNINE)"
doi: "10.1109/EDUNINE62390.2026.11547119"
url: ""
status: "[Excluido Fase 2 - Criterio EC2 (Artigo metodologico/descritivo sem resultados empiricos e focado em risco academico, sem desfecho de recusa escolar ou absenteismo)]"
qa_score: 4
population_scope: "Ensino Básico (Escolas Públicas)"
intervention_scope: "Instrumentos Psicométricos Validados + IA (Regressão/Clustering)"
outcome_scope: "Predição Precoce de Risco Escolar e Saúde Mental"
authors:
  - "Ruth Y. Zuleta Torres"
  - "Dixon Salcedo Morillo"
  - "Raúl Ramírez Velarde"
  - "Pedro López Pérez"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/ieee_xplore
---
# S0285: AI-Driven Psychoeducational Analytics for Early Detection of Academic Risk in Colombian Schools

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0285`
> - **Autores:** Ruth Y. Zuleta Torres, Dixon Salcedo Morillo, Raúl Ramírez Velarde, Pedro López Pérez
> - **Ano:** 2026
> - **Veículo (Venue):** *2026 IEEE Engineering Education World Conference (EDUNINE)*
> - **Base de Origem:** `IEEE Xplore` (Bases: `['IEEE Xplore']`)
> - **DOI:** [10.1109/EDUNINE62390.2026.11547119](https://doi.org/10.1109/EDUNINE62390.2026.11547119)
> - **URL:** Não informado
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC2 (Artigo metodologico/descritivo sem resultados empiricos e focado em risco academico, sem desfecho de recusa escolar ou absenteismo)]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> This article presents the development of an academic management model integrating artificial intelligence, aimed at the early prediction of school failure risk. The study employed scientifically validated psychometric instruments, from which multi-stage databases were constructed, incorporating variables related to reading comprehension, mental health, spelling, and mathematical performance. Regression and clustering algorithms were compared with traditional linear approaches, showing a substantial enhancement in predictive performance. The proposed model is designed to support institutional data-driven decision-making and to guide timely pedagogical interventions. The findings confirm the high potential of artificial intelligence as a tool to strengthen educational inclusion, optimize academic management processes, and improve school performance in public education contexts marked by socioeconomic vulnerability. These findings lay the groundwork for scalable, ethical AI systems supporting inclusive education.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Ensino Básico (Escolas Públicas)
- **Intervencao/Tecnologia (Intervention Scope):** Instrumentos Psicométricos Validados + IA (Regressão/Clustering)
- **Desfecho (Outcome Scope):** Predição Precoce de Risco Escolar e Saúde Mental
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve modelo de gestão acadêmica com Inteligência Artificial integrando instrumentos psicométricos cientificamente validados e variáveis de saúde mental (mental health) para detecção precoce de risco escolar em escolas públicas. Responde a RQ1, RQ2 e RQ3.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0285`
- **Titulo Completo:** AI-Driven Psychoeducational Analytics for Early Detection of Academic Risk in Colombian Schools
- **Autores:** Ruth Y. Zuleta Torres, Dixon Salcedo Morillo, Raúl Ramírez Velarde, Pedro López Pérez
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** 2026 IEEE Engineering Education World Conference (EDUNINE)
- **DOI:** [10.1109/EDUNINE62390.2026.11547119](https://doi.org/10.1109/EDUNINE62390.2026.11547119)
- **Base de Dados:** IEEE Xplore
- **Pais/Regiao de Realizacao do Estudo:** Colombia (Valledupar, regiao do Caribe colombiano)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Basico (escola publica em contexto de vulnerabilidade socioeconomica, estratos 1, 2 e 3)
- **Faixa Etaria / Amostra ($N$):** Amostras parciais longitudinais em tres momentos (2024 e 2025): N = 140, N = 151 e N = 190 estudantes de 8 a 12 anos (amostragem nao probabilistica por conveniencia)
- **Publico-alvo Avaliado:** Estudantes de escola publica avaliados para risco de fracasso academico (leitura e matematica), sem desfecho de recusa escolar ou absenteismo
- **Fonte dos Dados / Dataset:** Aplicacao digital em tablets Android (PsyToolkit) de testes cognitivos/emocionais + dados sociodemograficos do sistema SIMAT (44 variaveis quantitativas e 6 categoricas)

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** DASS-21 adaptado para criancas (8-12 anos, 21 itens, escala Likert 0-3, pontos de corte depressao > 5, ansiedade > 4, estresse > 5) + itens de sono, suporte social e bem-estar subjetivo; EDICOLE (compreensao leitora, 18 itens no texto 1); tarefa de velocidade leitora (140 palavras/WPM); BERDE (desempenho matematico/discalculia); Simon Task (controle inibitorio via PsyToolkit)
- **Natureza da Ferramenta:** Bateria psicoeducacional e psicometrica digitalizada
- **Forma de Aplicacao:** Aplicacao coletiva (EDICOLE, 30-40 min) e individual em tablets Android (Simon Task ~15 min e questionarios via PsyToolkit)
- **Finalidade:** Triagem de risco academico (fracasso escolar em leitura/matematica) e saude mental associada

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Arquitetura descritiva/metodologica hibrida (Reducao de dimensionalidade via PCA + Aprendizado Nao Supervisionado e Supervisionado em implementacao longitudinal)
- **Algoritmos Empregados:** PCA (retendo 85% da variancia), K-means clustering, Regressao Multipla; menciona exploracao futura/em andamento de Arvores de Decisao, Regressao Logistica, Redes Neurais, Boosting e Series Temporais (sem resultados estatisticos publicados neste artigo)
- **Tarefa do Modelo:** Perfilamento de estudantes e predicao de risco de fracasso academico (sem tarefa de predicao de recusa escolar ou absenteismo)
- **Estagio de Deteccao:** Protocolo em fase de implementacao longitudinal; artigo explicitamente declara nao apresentar resultados estatisticos (`Section II.C.3`)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Depressao, ansiedade e estresse (DASS-21 adaptado), sono, suporte social e bem-estar subjetivo; ansiedade matematica mencionada na descricao geral do BERDE (embora apenas 2 componentes numericos do BERDE tenham sido usados)
- **Variaveis Comportamentais / Historico:** Compreensao leitora (EDICOLE: conhecimento previo, memoria textual, inferencia, integracao, controle), velocidade de leitura (WPM), cognicao numerica (BERDE), controle inibitorio (Simon Task) e historico de repetencia (SIMAT)
- **Variaveis Familiares / Sociodemograficas:** Idade, genero, serie, estrato socioeconomico (1, 2 e 3 via SIMAT)
- **Variaveis Institucionais / Contextuais:** Instituicao publica oficial em Valledupar (Caribe colombiano)
- **Features Mais Relevantes Identificadas:** N/A (o artigo afirma apenas associacoes preliminares qualitativas entre depressao/ansiedade e desempenho em leitura, sem pesos, SHAP ou coeficientes publicados)

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** Adequacao amostral para PCA: KMO = 0,82 e teste de esfericidade de Bartlett (p < 0,001); nenhuma metrica empirica nova dos testes e reportada nos resultados
- **Metricas Computacionais (ML):** N/A — Nenhuma metrica de desempenho preditivo (Acuracia, F1, AUC, RMSE, R2) e reportada; a Secao II.C.3 declara expressamente que o escopo e metodologico e descritivo, *"without presenting statistical results, as the study remains in its longitudinal implementation phase"*
- **Estrategia de Validacao:** Prevê Multiple Imputation (MICE), controle de outliers por distancia de Mahalanobis, padronizacao z-score e fluxo em R/Python (`caret`, `scikit-learn`), mas sem resultados de validacao reportados
- **Desafios Metodologicos Relatados:** Tratamento de dados faltantes (imputacao multipla) e outliers multivariados em coleta longitudinal em andamento
- **Aspectos Eticos e Transparencia (XAI):** Menciona necessidade futura de mecanismos de monitoramento etico, transparencia e supervisao humana; divulga uso do ChatGPT 5.2 para traducao espanhol-ingles
- **Limitacoes Declaradas:** O artigo nao apresenta secao formal de limitacoes, apenas reconhece que o estudo esta em fase longitudinal sem resultados estatisticos concluidos
- **Direcoes Futuras:** Expandir dataset com participacao familiar, feedback docente e monitoramento longitudinal; implementar redes neurais, boosting e series temporais

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** Versao adaptada do DASS-21 para criancas de 8 a 12 anos (21 itens em escala Likert de 4 pontos, 0-3; tres subescalas de 7 itens: depressao > 5, ansiedade > 4 e estresse > 5) + itens adicionais sobre sono, suporte social e bem-estar subjetivo. Aplicado digitalmente via PsyToolkit em tablets Android em tres momentos longitudinais (2024-2025).
- **Inventario completo de variaveis e justificativa de escolha:** Total de 50 variaveis (44 quantitativas e 6 categoricas) provenientes de EDICOLE (compreensao leitora), tarefa de leitura (WPM), BERDE (representacao analogica e verbal-numerica), Simon Task (diferenca de tempo de reacao incongruente vs. congruente), DASS-21 + bem-estar/sono/suporte social e SIMAT (idade, genero, serie, historico de repetencia). Escolhidas pela validade psicometrica e adequacao etaria para modelar fracasso academico em contextos vulneraveis, sem incluir frequencia escolar/absenteismo.
- **Fundamentacao teorica do identificador:** Baseia-se no modelo cognitivo de compreensao leitora de EDICOLE, no modelo de codigo triplo de Dehaene para cognicao numerica (BERDE), no paradigma de conflito/controle inibitorio de Simon e no modelo tripartite de estados emocionais negativos (Lovibond & Lovibond) do DASS-21.
- **Restricoes de recursos e limitacoes:** Requer tablets Android, acesso a web/PsyToolkit, aplicadores treinados para testes individuais (~15 min por aluno no Simon Task) e coletivos (30-40 min), o que limita escala em escolas sem infraestrutura. Limitacao critica para esta RSL: foco em desempenho academico/leitura/matematica sem variavel de absenteismo/recusa escolar e ausencia total de resultados empiricos preditivos publicados.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo de descrever arquitetura psicoeducacional baseada em IA para deteccao precoce de risco academico. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 1 | Descreve instrumentos, amostras parciais (140, 151, 190) e pipeline tecnico, mas sem especificacao de hiperparametros, rotulo-alvo ou protocolo completo de treino/teste. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 0 | Nao apresenta resultados estatisticos nem metricas de desempenho dos modelos (apenas KMO = 0,82 e Bartlett p < 0,001). |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Inclui DASS-21 e bem-estar subjetivo, mas voltados a desempenho em leitura/matematica e sem analise de recusa escolar ou absenteismo. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 0 | Nao apresenta discussao critica sobre limitacoes amostrais (conveniencia), ausencia de resultados ou vieses algoritmicos. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **4 / 10** | Excluido na Fase 2 (`EC2`) por ausencia de desfecho de recusa/absenteismo escolar e ausencia de resultados empiricos de IA/ML. |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
