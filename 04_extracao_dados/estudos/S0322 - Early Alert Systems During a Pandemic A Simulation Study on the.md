---
id: S0322
study_id: S0322
title: "Early Alert Systems During a Pandemic: A Simulation Study on the Impact of Concept Drift"
year: 2021
database: "ACM DL"
venue: "LAK21: 11th International Learning Analytics and Knowledge Conference"
doi: "10.1145/3448139.3448190"
url: "https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3448139.3448190"
status: "[Incluido Fase 2 - Extracao Concluida]"
qa_score: 8
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
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

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
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (Estado de Rhode Island)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Medio (High School, 9o ao 12o ano; treino com dados de 9o a 11o ano)
- **Faixa Etaria / Amostra ($N$):** Todos os estudantes das escolas publicas de ensino medio de Rhode Island (coortes de treino SY 2007-2015; conjunto de teste SY 2016 com N = 2.731 casos positivos de evasao escolar)
- **Publico-alvo Avaliado:** Estudantes do ensino medio da rede publica estadual (avaliacao de robustez de EWS frente a *concept drift* pandemico)
- **Fonte dos Dados / Dataset:** Sistema de Informacoes Estudantis do Rhode Island Department of Education (RIDE), em parceria com The Policy Lab (Brown University) e DataSpark

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** N/A (nao utiliza instrumentos psicometricos; utiliza registros administrativos e desempenho academico)
- **Natureza da Ferramenta:** Painel de EWS (`teacher information portal`) com 6 indicadores atualizados mensalmente (frequencia, retencao, suspensoes, proficiencia em matematica e ELA, e indicador de risco)
- **Forma de Aplicacao:** Registros institucionais estaduais
- **Finalidade:** Triagem inicial e alerta precoce de risco de evasao (codificado em vermelho [top 3%], amarelo [2% seguintes] e verde)

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** [[Early_Warning_Systems]] (EWS), Machine Learning Supervisionado ([[Random_Forest]] via `FastForest` / `nimbusml`) e simulacao baseada em imputacao para analise de *concept drift* (3 cenarios)
- **Algoritmos Empregados:** [[Early_Warning_Systems]], [[Random_Forest]] (`FastForest`)
- **Tarefa do Modelo:** Classificacao binaria (evasao escolar ate o 12o ano) e ranqueamento por escore de risco (`high`: top 3%, `moderate`: 2% seguintes)
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (gerado no inicio de cada ano letivo utilizando historico dos 2 anos anteriores)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** N/A (nao inclui variaveis psicologicas ou socioemocionais diretas)
- **Variaveis Comportamentais / Historico:** Taxa de frequencia escolar (`attendance percentages`), retencao de serie, numero de infracoes (`grievances`), dias de suspensao interna e externa, notas em testes estaduais padronizados (Math, ELA), SAT e PSAT
- **Variaveis Familiares / Sociodemograficas:** Genero, idade, raca, etnia, nivel socioeconomico e status de educacao especial
- **Variaveis Institucionais / Contextuais:** Mudanca na politica estadual de suspensoes (SY 2012), exclusao de unidade de detencao juvenil por perfil atipico, disrupcao pandemica (ensino remoto e cancelamento de testes em SY 2019-20)
- **Features Mais Relevantes Identificadas:** Taxa de frequencia escolar (`attendance rates`) apontada como mais importante que infracoes e suspensoes; o uso de dados dos 2 anos anteriores conferiu maior robustez a falhas pontuais de coleta

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A
- **Metricas Computacionais (ML):** Modelo Original (teste 2016): Overall Accuracy = 0,9130, NPV = 0,9502, Precision = 0,4812, Recall = 0,5057, F1-Score = 0,4931, AUC = 0,8902, Accuracy @ Top 3% = 0,6452, Accuracy @ Top 5% = 0,5622, Accuracy @ Top 100 = 0,83. Nos 3 cenarios de simulacao (Set to Zero, Mean, Median, Nearest Neighbor, Worst): AUC variou de 0,8683 a 0,8910 e Accuracy @ Top 3% de 0,6002 a 0,6524; sob imputacao "Worst" no Cenario 3, Recall subiu para 0,5965 com queda de Precision para 0,4135
- **Estrategia de Validacao:** Split temporal (treino SY 2007-2015; teste SY 2016) e simulacao de *concept drift* com 5 estrategias de imputacao em 3 cenarios
- **Desafios Metodologicos Relatados:** *Concept drift* por interrupcao pandemica (ausencia de notas padronizadas, alteracao no significado de frequencia e infracoes no ensino remoto); desbalanceamento de classes (tratado com over- e under-sampling); ausencia de rotulos reais pos-pandemia ($y_{t+1}$)
- **Aspectos Eticos e Transparencia (XAI):** Discussao sobre implicacoes sociopoliticas de predicoes imperfeitas, risco de estigma do rotulo "at-risk", necessidade de decisoes de baixo risco ("lower the stakes"), transparencia clara das limitacoes e auditoria de equidade entre subgrupos
- **Limitacoes Declaradas:** A simulacao modela apenas mudanca na distribuicao das features $P(X_{t+1}) \neq P(X_t)$ e assume fortemente que a relacao $P(Y|X)$ permaneceu inalterada durante a pandemia; resultados ligados a estrutura especifica dos dados de Rhode Island
- **Direcoes Futuras:** Quantificar incerteza sob mudanca em $P(Y|X)$, investigar praticas de modelagem que aumentem a robustez de EWS e validar desempenho por subgrupos com dados pos-pandemia

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo de propor um framework de simulacao por imputacao para avaliar o impacto de *concept drift* pandemico no EWS de evasao de Rhode Island. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha o modelo (`FastForest`/Random Forest), features, split temporal (2007-2015 vs. 2016), reamostragem, 3 cenarios e 5 estrategias de imputacao. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Accuracy, NPV, Precision, Recall, F1, AUC e metricas operacionais (Accuracy @ Top 3%, Top 5% e Top 100) para o baseline e todos os cenarios. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 0 | Nao contempla fatores psicologicos, socioemocionais ou de clima escolar; utiliza apenas registros administrativos (frequencia, disciplina, notas) e demograficos. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute explicitamente a premissa sobre invariancia de $P(Y|X)$, dependencia de contexto, risco de estigma, equidade entre subgrupos e implicacoes sociopoliticas. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **8 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
