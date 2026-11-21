---
id: S0249
study_id: S0249
title: "Using data-driven analytics and ecological systems theory to identify risk and protective factors for school absenteeism among secondary students"
year: 2023
database: "ScienceDirect"
venue: "Journal of School Psychology"
doi: "https://doi.org/10.1016/j.jsp.2023.03.002"
url: "https://www.sciencedirect.com/science/article/pii/S0022440523000298"
status: "[Incluido Fase 2 - Extracao Concluida]"
qa_score: 10
population_scope: "Educação Básica (K-12)"
intervention_scope: "Modelos de Machine Learning / IA e Análise Preditiva"
outcome_scope: "Predição de Absenteísmo Crônico Escolar"
authors:
  - "Knoo Lee"
  - "Barbara J. McMorris"
  - "Chih-Lin Chi"
  - "Wendy S. Looman"
  - "Matthew K. Burns"
  - "Connie W. Delaney"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "Minnesota Student Survey (MSS 2016)"
  - "PHQ-2"
  - "Social Competency Scale (SCS)"
  - "School Engagement Scale (SE)"
  - "Teacher-Student Relationship (TSR)"
  - "Adverse Childhood Experiences (ACEs)"
algorithms:
  - "J48 Decision Tree (C4.5)"
  - "Regressao Logistica"
  - "CART (MICE Imputation)"
  - "SMOTE"
  - "Correlation & Information Gain Filter Selection"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/sciencedirect
  - fenomeno/absenteismo_cronico
---
# S0249: Using data-driven analytics and ecological systems theory to identify risk and protective factors for school absenteeism among secondary students

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0249`
> - **Autores:** Knoo Lee, Barbara J. McMorris, Chih-Lin Chi, Wendy S. Looman, Matthew K. Burns, Connie W. Delaney
> - **Ano:** 2023
> - **Veículo (Venue):** *Journal of School Psychology*
> - **Base de Origem:** `ScienceDirect` (Bases: `['ScienceDirect']`)
> - **DOI:** [https://doi.org/10.1016/j.jsp.2023.03.002](https://doi.org/https://doi.org/10.1016/j.jsp.2023.03.002)
> - **URL:** [Link da Publicação](https://www.sciencedirect.com/science/article/pii/S0022440523000298)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Chronic absenteeism is an administrative term defining extreme failure for students to be present at school, which can have devastating long-term impacts on students. Although numerous prior studies have investigated associated variables and interventions, there are few studies that utilize both theory-driven and data-informed approaches to investigate absenteeism. The current study applied data-driven machine learning techniques, grounded in “The Kids and Teens at School” (KiTeS) theoretical framework, to student-level data (N = 121,005) to identify risk and protective variables that are highly associated with school absences. A total of 18 risk and protective variables were identified; all 18 variables were characteristics of the microsystem or mesosystem, emphasizing school absences' proximity to variables within inner ecological systems rather than the exosystem or macrosystem. Implications for future studies and health infrastructure are discussed.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (K-12)
- **Intervencao/Tecnologia (Intervention Scope):** Modelos de Machine Learning / IA e Análise Preditiva
- **Desfecho (Outcome Scope):** Predição de Absenteísmo Crônico Escolar
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de predição de absenteísmo crônico escolar na educação básica (k-12), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0249`
- **Titulo Completo:** Using data-driven analytics and ecological systems theory to identify risk and protective factors for school absenteeism among secondary students
- **Autores:** Knoo Lee, Barbara J. McMorris, Chih-Lin Chi, Wendy S. Looman, Matthew K. Burns, Connie W. Delaney
- **Ano de Publicacao:** 2023
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Journal of School Psychology
- **DOI:** [https://doi.org/10.1016/j.jsp.2023.03.002](https://doi.org/https://doi.org/10.1016/j.jsp.2023.03.002)
- **Base de Dados:** ScienceDirect
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (Estado de Minnesota)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica — Ensino Secundario (8a, 9a e 11a series; K-12)
- **Faixa Etaria / Amostra ($N$):** N = 121.005 estudantes (filtrados de 126.868 participantes originais apos exclusao de dados ausentes em raca/etnia [3,6%], sexo biologico [0,2%] e faltas [0,7%]): 42.791 da 8a serie (35,4%), 43.246 da 9a serie (35,7%) e 34.968 da 11a serie (28,9%); 50,4% masculino (60.931) e 49,6% feminino (60.074); 76% brancos, 9% multiplas racas, 7% negros, 7% hispanicos/latinos, 6% asiaticos, 2% indigenas americanos/nativos do Alasca, 1% nativos havaianos/ilhas do Pacifico; 27% elegiveis para almoco gratuito/reduzido. Desfecho binario: 7.630 (6%) com alta frequencia de faltas nao justificadas vs. 113.375 (94%) com nenhuma ou poucas faltas
- **Publico-alvo Avaliado:** Estudantes secundarios de escolas publicas, *charter*, tribais, privadas, centros alternativos e unidades juvenis avaliados para predicao de [[Absenteismo_Cronico|absenteismo escolar]] nao justificado
- **Fonte dos Dados / Dataset:** *2016 Minnesota Student Survey* (MSS) — levantamento estadual trienal de vigilancia epidemiologica e escolar conduzido pelo Departamento de Educacao de Minnesota (dados desidentificados)

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** *2016 Minnesota Student Survey* (MSS) organizado sob o arcabouco bioecologico *Kids and Teens at School* (KiTeS), incorporando escalas e subescalas padronizadas: *Patient Health Questionnaire-2* (PHQ-2), *Social Competency Scale* (SCS, 8 itens), *Positive Identity Scale* (6 itens), *Empowerment* (3 itens), *School Engagement Scale* (SE, 6 itens adaptados do *Student Engagement Instrument*), *Teacher-Student Relationship* (TSR, 5 itens), *Adverse Childhood Experiences* (ACEs, 7 itens), *Global Appraisal of Individual Needs* (GAIN, 5 itens), *Hostile School Climate* (5 itens por pares / 5 por respondente), *Perception of Family Caring* (2 itens) e *Positive Youth Development Scale* (7 itens)
- **Natureza da Ferramenta:** Questionario epidemiologico multidimensional de autorrelato contendo escalas psicometricas, comportamentais e contextuais
- **Forma de Aplicacao:** Autorrelato anonimo/desidentificado dos estudantes em ambito estadual
- **Finalidade:** Rastreamento populacional e identificacao orientada por teoria + dados (*Theory-Driven Data-Informed Analysis* - TDDIA) de fatores de risco e protecao associados a faltas escolares nao justificadas

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Machine Learning Supervisionado com selecao de atributos hibrida (metodos *Filter* + *Wrapper*), imputacao baseada em arvores (CART/MICE) e balanceamento sintetico de classes (SMOTE), integrado a teoria ecologica (TDDIA / KiTeS)
- **Algoritmos Empregados:** Imputacao CART (MICE, 5 iteracoes); selecao de features via *Correlation Attribute Evaluation*, *Information Gain Attribute Evaluation* e *Wrapper* com Arvore de Decisao **J48 (C4.5)** (`best-first forward`, 10-fold CV); modelagem preditiva comparativa com **J48 Decision Tree** (limiar de poda = 0,25, min 2 instancias por folha) e **[[Regressao_Logistica|Regressao Logistica]]** (R 3.5.0 e Weka), com e sem **SMOTE** (proporcao original 15:1 ajustada para 1,7:1)
- **Tarefa do Modelo:** Classificacao binaria de risco de absenteismo nao justificado nos ultimos 30 dias (`0` = nenhuma ou 1-2 vezes vs. `1` = >=3 vezes de dia inteiro ou parcial sem justificativa)
- **Estagio de Deteccao:** Rastreio/alerta precoce baseado em faltas nos ultimos 30 dias como antecedente/proxy de absenteismo cronico anual (>=15 dias/ano)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Sintomas depressivos (PHQ-2), historico de saude mental de longo prazo (>=6 meses), historico de tratamento em saude mental, ideacao suicida, tentativa de suicidio, autolesao nao suicida, *Social Competency Scale* (SCS: regulacao emocional, resolucao de conflitos, empatia, amizades), *Positive Identity Scale*, *Empowerment* e percepcao de cuidado por pares/familia/adultos
- **Variaveis Comportamentais / Historico:** Faltas por doenca, visitas a enfermaria escolar, encaminhamentos disciplinares, suspensoes intraescolares (ISS) e extraescolares (OSS), *School Engagement Scale* (SE), uso de substancias (tabaco, alcool, *binge drinking*, maconha, drogas ilicitas e prescritas sem receita), GAIN, violencia por parceiro intimo (IPV), perpetracao de violencia, fuga de casa (*runaway*), jogo patologico, sono e atividade fisica
- **Variaveis Familiares / Sociodemograficas:** Serie escolar, sexo biologico, raca/etnia, educacao especial/IEP, estrutura familiar (dois pais biologicos/adotivos), relacionamento com mae e pai, seguranca no lar, pais encarcerados, experiencias adversas na infancia (ACEs), aprovacao parental do uso de substancias, almoco gratuito/reduzido e inseguranca alimentar/habitacional (*homelessness*)
- **Variaveis Institucionais / Contextuais:** Relacionamento professor-aluno (TSR), clima escolar hostil, bullying/assedio por pares (raca, religiao, genero, LGB, deficiencia, peso, aparencia, bullying online), seguranca na escola, no trajeto e no bairro, atividades extracurriculares/apos a escola e regiao (Twin Cities Metro vs. Greater Minnesota)
- **Features Mais Relevantes Identificadas:** O Subconjunto E (18 de 113 variaveis = Top 10% dos filtros + recorrentes no J48) obteve o melhor equilibrio parcimonia-desempenho, sendo **100% composto por fatores proximais do microssistema (10) e mesossistema (8)**: *Social Competency Scale* (SCS — rank #1 no Information Gain), *School Engagement* (SE — rank #3 no IG), *Teacher-Student Relationship* (TSR), *Adverse Childhood Experiences* (ACEs), aprovacao de substancias pelos amigos, suspensoes intra e extraescolares, encaminhamento disciplinar, uso de tabaco/maconha/alcool/outras substancias, ficar em casa por doenca, check-up medico preventivo e pertencimento a grupos indigenas americanos ou nativos havaianos/ilhas do Pacifico

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** Alfa de Cronbach reportado no Apendice para todas as escalas multi-itens: Positive Identity (0,84), Social Competency Scale (0,84), Empowerment (0,81), PHQ-2 (0,71), School Engagement (0,68), Teacher-Student Relationship (0,85), Hostile School Climate por pares (0,76) e pelo respondente (0,74), Perception of Family Caring (0,79), Positive Youth Development (0,85), Parents'/Friends' approval of substance use (0,92 / 0,93), GAIN (0,50)
- **Metricas Computacionais (ML):** Subconjunto E (18 variaveis, melhor conjunto):
  - Dados originais (15:1): Regressao Logistica (Acuracia = 93,84%, F-score ponderado = 0,919 [0,92], AUC = 0,839 [0,84]); J48 Decision Tree (Acuracia = 93,61%, F-score = 0,917 [0,92], AUC = 0,687 [0,69]).
  - Dados balanceados com SMOTE (1,7:1): Regressao Logistica (Acuracia = 76,21%, F-score = 0,760 [0,76], AUC = 0,848 [0,85]); **J48 Decision Tree (Acuracia = 92,80%, F-score = 0,928 [0,93], AUC = 0,957 [0,96])** — superando F (37 vars: Acc = 92,60%, AUC = 0,941) e G (64 vars: Acc = 92,86%, AUC = 0,94/0,865 no texto vs. Tabela 7).
- **Estrategia de Validacao:** Validacao cruzada 10-fold (*10-fold cross-validation*) na selecao de atributos (Correlation, Information Gain e J48 wrapper) e na comparacao dos modelos preditivos (com e sem SMOTE)
- **Desafios Metodologicos Relatados:** Forte desbalanceamento de classes (15:1; 94% baixa ausencia vs. 6% alta ausencia), tratado comparando dados originais e SMOTE; custo computacional da imputacao CART/MICE em matriz de 121.005 x 103 variaveis (5 iteracoes em CPU i7-10700 + RTX 3070 + 32 GB RAM); 6 variaveis com >10% de missings mantidas apenas para implicacoes; perda de acuracia na Regressao Logistica apos SMOTE (de 93,84% para 76,21%)
- **Aspectos Eticos e Transparencia (XAI):** Dados estaduais desidentificados; uso de modelos intrinsecamente interpretaveis (Arvore de Decisao J48 e Regressao Logistica) e hierarquizacao teorica explicita (KiTeS), evitando interpretacao meramente exploratoria ("efeito poste de luz" / *streetlight effect*)
- **Limitacoes Declaradas:** Desfecho dicotomico autorrelatado referente apenas aos ultimos 30 dias (sem registros administrativos escolares nem medicao do ano letivo completo); amostra restrita ao estado de Minnesota; predominio de variaveis no micro (44) e mesossistema (35) no MSS em comparacao ao exo (18) e macrosistema (6); exclusao da variavel de identidade de genero (disponivel apenas para 9a e 11a series em 2016) para maximizar tamanho amostral; classificacao ecologica das variaveis por consenso sem indice de concordancia inter-avaliadores
- **Direcoes Futuras:** Integrar dados de autorrelato a registros administrativos nacionais (ex.: *Civil Rights Data Collection*) e variaveis comunitarias objetivas (coesao social, exposicoes territoriais); conduzir analises de descoberta causal (*causal discovery*) sobre suspensoes e absenteismo; validar externamente em outros estados e com informantes escolares/familiares

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** Autorrelato anonimo de estudantes no levantamento estadual *2016 Minnesota Student Survey* (aplicado a cada 3 anos nas escolas de Minnesota). Inclui rastreamento breve de depressao via PHQ-2 (2 itens Likert 1-4 sobre as ultimas 2 semanas, dicotomizado; alpha = 0,71), itens binarios de historico/tratamento em saude mental, ideacao/tentativa de suicidio, autolesao nao suicida e escalas socioemocionais continuas (SCS 8 itens, Positive Identity 6 itens, Empowerment 3 itens, SE 6 itens, TSR 5 itens, clima hostil/bullying nos ultimos 30 dias).
- **Inventario completo de variaveis e justificativa de escolha:** Inicialmente 103/113 variaveis selecionadas do MSS 2016 por consenso da equipe segundo os quatro sistemas ecologicos do modelo KiTeS (44 no microssistema, 35 no mesossistema, 18 no exossistema e 6 no macrosistema; sem cronossistema por ser corte transversal), reduzidas empiricamente via filtros + wrapper J48 para o Subconjunto E (18 preditores principais, 10 do microssistema e 8 do mesossistema). A escolha combinou fundamento teorico (evitar vies de disponibilidade de dados) e validacao empirica em Weka.
- **Fundamentacao teorica do identificador:** Integracao da Teoria dos Sistemas Bioecologicos de Bronfenbrenner (1977; Bronfenbrenner & Morris, 2007) por meio do arcabouco *Kids and Teens at School* (KiTeS; Melvin et al., 2019), operacionalizada via protocolo *Theory-Driven Data-Informed Analysis* (TDDIA; Haardorfer, 2019).
- **Restricoes de recursos e limitacoes:** Apesar de o modelo final enxuto usar apenas 18 variaveis de questionario autorrelatado (viavel para triagem escolar sem prontuarios clinicos complexos), o pre-processamento em escala populacional (N = 121.005 x 103 variaveis com imputacao CART/MICE e SMOTE) exigiu hardware dedicado (32 GB RAM, GPU RTX 3070) e levantamentos estaduais trienais que nao capturam trajetoria diaria nem substituem registros oficiais de frequencia.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo e a questao norteadora de integrar teoria bioecologica (KiTeS) e ML para identificar fatores de risco e protecao para faltas escolares. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha amostra (N = 121.005), exclusoes, todas as 103+ variaveis no Apendice (Tabelas A.1-A.4), imputacao CART, SMOTE, 3 seletores, 10-fold CV e hiperparametros do J48. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Alfa de Cronbach das escalas e Acuracia, F-score ponderado e AUC-ROC para todos os subconjuntos (A-G) com J48 e Regressao Logistica (original e SMOTE). |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Avalia PHQ-2, saude mental, competencia social (SCS), engajamento escolar (SE), relacao professor-aluno (TSR), ACEs, bullying e suporte familiar sob o modelo KiTeS. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute desfecho dicotomico de 30 dias autorrelatado, restricao geografica a Minnesota, desbalanceamento de variaveis entre sistemas do KiTeS, exclusao de identidade de genero e falta de IRR. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **10 / 10** | Estudo primario empirico robusto de ML aplicado a absenteismo escolar com forte ancoragem teorica e socioemocional. |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
