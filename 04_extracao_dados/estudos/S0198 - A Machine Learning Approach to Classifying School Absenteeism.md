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

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
1. **Dados de entrada para identificar ansiedade/sofrimento:** O estudo nao emprega escalas psicometricas continuas ou Likert para ansiedade/sofrimento. Os dados provem de um questionario clinico de admissao (*intake questionnaire*) desenvolvido previamente pela propria agencia de saude mental, com respostas estritamente binarias ("yes"/"no") e sem definicoes operacionais padronizadas ou exemplos comportamentais fornecidos aos respondentes. O conjunto inclui: (a) 1 item binario de desfecho (*"Has your youth displayed a history of absenteeism since enrollment in school?"*); (b) um checklist de 69 areas problematicas biopsicossocioeducacionais em 8 dominios (KR-20 = 0,80; reduzido a 68 apos exclusao de 1 item sem variancia), no qual o dominio *Mood, Perception, Thought Disturbances* contempla itens como *"Is the Youth Experiencing an Anxious Mood/Thoughts?"* e *"Youth experiences depressed mood or thoughts"*; e (c) 15 itens binarios de historico diagnostico previo (reduzidos a 12 apos exclusao de ADD, ADHD e Bipolar Disorder), incluindo *Anxiety Disorder*, *Depression*, *Obsessive Compulsive Disorder*, *Post-Traumatic Stress Disorder*, *Attachment Disorder* e *Adjustment Disorder*. A fonte e exclusivamente o relato de pais ou cuidadores junto a um assistente de caso clinico (*clinical case worker*) na visita de admissao, sem autorrelato do estudante, sem relato de professores e sem confirmacao clinica independente dos diagnosticos. A periodicidade e pontual/transversal unica (coleta na admissao entre 2018 e 2020), de carater retrospectivo.
2. **Inventario completo de variaveis e justificativa de escolha:** As variaveis utilizadas dividem-se em: (a) **Desfecho:** historico de absenteismo escolar desde a matricula (binario sim/nao; 56% sim); (b) **68 itens do checklist de areas problematicas** (de 69 originais; lista integral disponivel apenas no Material Suplementar online, nao listada completamente no PDF) distribuidos em 8 dominios: *Disruptive Behavior* (ex.: comportamento interferente em casa e na escola, vulnerabilidade a comportamentos de risco), *School and Learning* (ex.: dificuldades de aprendizagem na escola), *Physical and Sensory* (ex.: deficiencia fisica, enurese; item *"Medically Fragile"* removido por variancia zero), *Mood, Perception, Thought Disturbances* (ex.: humor/pensamentos ansiosos, humor/pensamentos depressivos), *Victimization* (ex.: bullying/ameacas), *Intellectual, Adaptive, or Functional* (ex.: deficits de funcionamento intelectual, comportamento sexual inadequado mencionado na discussao), *Social Withdrawal* (ex.: isolamento social) e *Family Issues, Concerns, or Dynamics* (ex.: incapacidade da familia de atender as necessidades do jovem, parentalidade inconsistente); (c) **12 itens de diagnostico comorbido** (de 15 originais): *Attachment Disorder* (5,2%), *Adjustment Disorder* (1,0%), *Communication Disorder* (2,6%), *Depression Disorder* (13,9%), *Anxiety Disorder* (43,3%), *Obsessive Compulsive Disorder* (8,2%), *Tourette Syndrome* (1,0%), *Conduct Disorder* (4,1%), *Oppositional Defiant Disorder* (34,0%), *Autism Spectrum Disorder* (13,9%), *Post-Traumatic Stress Disorder* (0,5%) e *Other Diagnosis* (27,8%); (d) **Variaveis demograficas testadas em modelo comparativo:** idade (4–17 anos) e genero (menina, menino, transgenero ou outro). A identidade cultural consta apenas para caracterizacao descritiva da amostra (Tabela 1). **Justificativa de escolha:** os autores justificam a selecao pelo uso pragmatico de dados ja coletados na triagem rotineira da clinica (onde restricoes de tempo inviabilizam escalas longas; Goldman et al., 2025), pela aderencia aos 7 temas meta-analiticos de risco de absenteismo de Gubbels et al. (2019) e revisoes de Kearney & Childs (2023) e Niemi et al. (2022), pela alta taxa de comorbidades no TDAH e pela evidencia de heterogeneidade do TDAH e do absenteismo segundo idade e genero.
3. **Fundamentacao teorica do identificador:** O modelo articula o referencial multifatorial da etiologia do absenteismo escolar (os 7 temas meta-analiticos de Gubbels et al., 2019; revisoes de Kearney, 2008 e Kearney & Childs, 2023) com a psicopatologia do desenvolvimento aplicada ao TDAH (comorbidades internalizantes/externalizantes, desregulacao emocional e prejuizos academicos). No plano clinico-psicometrico, apoia-se na superioridade da predicao atuarial sobre o julgamento clinico intuitivo (Sawyer, 1966), na validade do relato parental em triagens breves ambulatoriais (Goldman et al., 2025; Cree et al., 2023; Wrobel & Lachar, 1998) e na evidencia empirica de que absenteismo previo prediz absenteismo futuro (Ansari & Gottfried, 2021; Simon et al., 2020). Computacionalmente, fundamenta-se em *Random Forest* (Breiman, 2001) e importancia por permutacao (Ishwaran, 2007) como abordagem orientada a dados complementar a modelos teoricos de regressao para capturar interacoes nao lineares de alta ordem em amostras pequenas.
4. **Restricoes de recursos e limitacoes do trabalho:** **Dependencias e aplicabilidade:** a coleta ocorreu em uma agencia comunitaria ambulatorial de saude mental infantil (Canada) e depende de entrevista/preenchimento presencial de admissao com apoio de um assistente de caso clinico (*clinical case worker*), nao dependendo de tablets escolares, sensores ou sistemas governamentais de educacao. O pipeline computacional utiliza software gratuito (R 4.3.2 / `caret`, codigo aberto no OSF). Os autores argumentam que, diferentemente de abordagens custosas ou demoradas (ex.: biomarcadores pupilometricos; Das & Khanna, 2021), o uso de itens curtos e indicadores rotineiros de avaliacoes de TDAH facilita integracao em fluxos clinicos e escolares (*multi-tiered systems of support*) sem sobrecarga significativa; contudo, sua viabilidade, aceitabilidade e valor incremental em escolas reais ainda nao foram avaliados empiricamente. **Limitacoes declaradas pelos autores:** (i) ausencia de fatores sistemicos/estruturais (qualidade da escola, clima de sala de aula, transporte); (ii) amostra relativamente pequena para ML ($N = 194$) e majoritariamente masculina (77,3% meninos), impedindo modelos estratificados por idade ou genero; (iii) uso de itens unicos dicotomicos (sim/nao) sem definicao operacional formal de absenteismo ou comportamentos, restringindo granularidade; (iv) delineamento transversal e retrospectivo (prediz historico passado, nao absenteismo futuro prospectivo); (v) informante unico (pais/cuidadores) sem confirmacao diagnostica independente nem dados multi-informantes; e (vi) amostra clinica encaminhada por dificuldades comportamentais/academicas, limitando a generalizacao para amostras comunitarias ou jovens com TDAH menos grave ou sem comorbidades.

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
