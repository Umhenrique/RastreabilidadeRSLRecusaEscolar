---
id: S0315
study_id: S0315
title: "Difficult Lessons on Social Prediction from Wisconsin Public Schools"
year: 2025
database: "ACM DL"
venue: "Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency"
doi: "10.1145/3715275.3732175"
url: "https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3715275.3732175"
status: "[Incluido Fase 2 - Extracao Concluida]"
qa_score: 9
population_scope: "Ensino Básico (Escolas Públicas K-12)"
intervention_scope: "Early Warning Systems / Modelos Preditivos"
outcome_scope: "Predição de Evasão Escolar e Efeito de Intervenções"
authors:
  - "Juan Carlos Perdomo"
  - "Tolani Britton"
  - "Moritz Hardt"
  - "Rediet Abebe"
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
# S0315: Difficult Lessons on Social Prediction from Wisconsin Public Schools

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0315`
> - **Autores:** Juan Carlos Perdomo, Tolani Britton, Moritz Hardt, Rediet Abebe
> - **Ano:** 2025
> - **Veículo (Venue):** *Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency*
> - **Base de Origem:** `ACM DL` (Bases: `['ACM DL']`)
> - **DOI:** [10.1145/3715275.3732175](https://doi.org/10.1145/3715275.3732175)
> - **URL:** [Link da Publicação](https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3715275.3732175)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Early warning systems (EWS) are predictive tools at the center of recent efforts to improve graduation rates in public schools across the United States. These systems assist in targeting interventions to individual students by predicting which students are at risk of dropping out. Despite significant investments in their widespread adoption, there remain large gaps in our understanding of the efficacy of EWS, and the role of statistical risk scores in education.In this work, we draw on nearly a decade’s worth of data and models — predictions and outcomes for over 200k students from 2013 to 2021 — from a system used throughout the State of Wisconsin to provide the first large-scale evaluation of the long-term impact of EWS on graduation outcomes. We present empirical evidence that the prediction system accurately sorts Wisconsin’s students by their dropout risk. We also find that it may have caused a single-digit percentage increase in graduation rates, though our empirical analyses cannot reliably rule out that there has been no positive treatment effect.Going beyond a retrospective evaluation of DEWS, we draw attention to a central question at the heart of the use of early warning systems: Are individual risk scores necessary for effectively targeting interventions? We propose a simple mechanism that only uses information about students’ environments—such as their communities, schools, and districts—and argue that this mechanism can target interventions just as efficiently as the individual risk score-based mechanism. Our argument holds even if individual risk predictions are highly accurate and effective interventions exist. In addition to motivating this simple targeting mechanism, our work provides a novel empirical backbone for the robust qualitative understanding among education researchers that dropout is structurally determined. Combined, our insights call into question the marginal value of individual predictions in settings where outcomes are driven by high levels of inequality.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Ensino Básico (Escolas Públicas K-12)
- **Intervencao/Tecnologia (Intervention Scope):** Early Warning Systems / Modelos Preditivos
- **Desfecho (Outcome Scope):** Predição de Evasão Escolar e Efeito de Intervenções
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Avaliação empírica em larga escala de sistemas de alerta precoce (Early Warning Systems - EWS) com modelos preditivos de evasão em mais de 200 mil estudantes da rede pública de ensino básico (Wisconsin). Responde diretamente às RQ2 e RQ4.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0315`
- **Titulo Completo:** Difficult Lessons on Social Prediction from Wisconsin Public Schools
- **Autores:** Juan Carlos Perdomo, Tolani Britton, Moritz Hardt, Rediet Abebe
- **Ano de Publicacao:** 2025
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency
- **DOI:** [10.1145/3715275.3732175](https://doi.org/10.1145/3715275.3732175)
- **Base de Dados:** ACM DL
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (Estado de Wisconsin)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Basico (Escolas Publicas K-12; predicoes no 8o ano para conclusao do ensino medio em 4 anos)
- **Faixa Etaria / Amostra ($N$):** Mais de 200.000 estudantes (~215.000 alunos em 4 coortes do 8o ano, 2013-2021; experimentos com CatBoost em ~160.000 treino / ~40.000 teste)
- **Publico-alvo Avaliado:** Estudantes da rede publica estadual de Wisconsin (avaliacao do sistema DEWS e comparacao entre alocacao individual e ambiental)
- **Fonte dos Dados / Dataset:** Wisconsin Department of Public Instruction (DPI) - DEWS / WISEDash (2013-2021), US Census Bureau American Community Survey (ACS 5 anos) e National Center for Education Statistics (ELSI)

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** N/A (nao utiliza escalas psicometricas; baseia-se em dados administrativos estaduais, exames padronizados e indicadores censitarios)
- **Natureza da Ferramenta:** Sistema administrativo de alerta precoce (DEWS) alimentado por registros escolares e censitarios (>40 features)
- **Forma de Aplicacao:** Registros institucionais estaduais (sem aplicacao de questionarios psicometricos aos alunos)
- **Finalidade:** Triagem e classificacao de risco de nao-conclusao do ensino medio no prazo (low, moderate, high)

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** [[Early_Warning_Systems]] (DEWS), Machine Learning Supervisionado (Ensemble Learning) e Inferencia Causal (Regression Discontinuity Design - RDD, alem de teste "predicting from predictions")
- **Algoritmos Empregados:** [[Early_Warning_Systems]], [[Random_Forest]], Gradient-Boosted Decision Trees (CatBoost), Regressao Linear Local (RDD)
- **Tarefa do Modelo:** Estimativa de probabilidade continua de formatura no prazo e classificacao em 3 categorias de risco (`low`, `moderate`, `high` via limiar $t^*=0,785$)
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (predicoes geradas do 5o ao 8o ano, com foco no 8o ano antes da entrada no ensino medio)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Nao mensura construtos psicologicos diretamente; inclui indicador de status de deficiencia (que engloba classificacoes como *Emotional Behavioral Disability*)
- **Variaveis Comportamentais / Historico:** Taxa de frequencia escolar (`Student Attendance Rate`), dias matriculados, notas em exames padronizados de leitura e matematica, retencao previa, numero de incidentes disciplinares, dias removidos/suspensao, tipo de remocao/descritores disciplinares, mobilidade entre escolas/distritos
- **Variaveis Familiares / Sociodemograficas:** Genero, raca/etnia, elegibilidade para almoco gratuito ou reduzido (proxy de pobreza), status de aprendiz de ingles (EL); no nivel distrital (ACS): renda domiciliar mediana, taxa de pobreza, desemprego, escolaridade de adultos, estrutura familiar, acesso a computador/internet e cobertura de seguro saude
- **Variaveis Institucionais / Contextuais:** Tamanho da coorte, medias e desvios padrao de leitura, matematica e frequencia da coorte, % de suspensoes/deficiencia/baixa renda/nao-brancos na coorte, receitas e despesas por aluno (ELSI)
- **Features Mais Relevantes Identificadas:** Preditores ambientais/comunitarios concentram quase todo o poder preditivo devido a segregacao entre distritos; dentre as variaveis individuais adicionadas ao modelo ambiental, `Attendance Rate` foi a mais importante (reducao de 4% no squared loss), seguida por notas em exames padronizados

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A
- **Metricas Computacionais (ML):** DEWS (8o ano, 2018-2021): AUC = 0,80; taxa real de formatura por grupo: ~97% (baixo risco), 83% (medio), <70% (alto). CatBoost (Performative vs. Non-Performative): AUC = 0,863 vs. 0,862; Log Loss = 0,185; Squared Loss = 0,052; 0-1 Loss = 0,065 vs. 0,066; $r^2$ = 0,184 vs. 0,183. Ganho ao adicionar features individuais sobre ambientais: -9,6% no Squared Loss, -14,6% no Log Loss, -3,9% no 0-1 Loss, +10,2% relativo (+0,082) no AUC. RDD causal: $\tau_{mod \to high} = +4,8\%$ (IC 95%: -2,0% a 11,6%, p=0,17); $\tau_{low \to mod} = +2,2\%$ (IC 95%: -2,7% a 7,1%, p=0,38)
- **Estrategia de Validacao:** Janela deslizante de 5 coortes anuais no DEWS; split 80/20 (~160k treino / ~40k teste) no CatBoost; Regression Discontinuity Design (RDD) com testes de balanceamento, manipulacao e sensibilidade de bandwidth ($h=0,005, 0,01, 0,02$) e Bootstrap (10.000 reamostragens)
- **Desafios Metodologicos Relatados:** Miscalibracao das probabilidades absolutas do DEWS; disparidades de calibracao entre subgrupos demograficos que podem despriorizar alunos historicamente marginalizados em rankings relativos; baixa variancia intraescolar devido a forte segregacao socioeconomica entre distritos
- **Aspectos Eticos e Transparencia (XAI):** Discussao central sobre equidade algoritmica (fairness/multicalibration), risco de despriorizacao sistematica de estudantes nao-brancos, de baixa renda ou com deficiencia, e vantagem de transparencia/custo/privacidade de politicas baseadas em escolas frente a escores individuais opacos
- **Limitacoes Declaradas:** Incerteza estatistica nas estimativas causais do RDD (ICs de 95% incluem zero); resultados sobre equivalencia da predicao ambiental refletem a segregacao socioeconomica de Wisconsin e podem nao se aplicar a contextos distintos (ex.: Nova York); dados de acesso ao portal WISEDash indisponiveis antes de 2018
- **Direcoes Futuras:** Realizar estudos qualitativos in situ com educadores sobre o uso pratico de EWS e priorizar intervencoes estruturais voltadas a escolas e comunidades vulneraveis

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente dois objetivos: avaliar o impacto causal de longo prazo do DEWS na formatura e comparar a eficacia de alocacao via escores individuais vs. variaveis ambientais. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Descreve rigorosamente a base estadual (>200k alunos, 2013-2021), todas as features (Apendice B), modelos CatBoost (80/20) e desenho causal RDD com testes de robustez. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Apresenta AUC (0,80 no DEWS; 0,863 no CatBoost), curvas de calibracao, Squared Loss, Log Loss, 0-1 Loss, $r^2$, estimativas RDD, ICs de 95% (Bootstrap/CLT) e p-valores. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Analisa profundamente fatores contextuais, institucionais, socioeconomicos e comportamentais (frequencia, disciplina, segregacao), mas nao aborda fatores psicologicos/socioemocionais individuais. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute amplamente vieses de calibracao entre grupos demograficos, incerteza estatistica das estimativas causais, limites de generalizacao geografica e restricoes dos dados de uso. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
