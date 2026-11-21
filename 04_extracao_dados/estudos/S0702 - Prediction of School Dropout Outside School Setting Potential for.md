---
id: S0702
study_id: S0702
title: "Prediction of School Dropout Outside School Setting: Potential for Early risk Stratification by Youth Health Care Services in the Netherlands. Results from a Retrospective Cohort Study"
year: 2023
database: "Springer Link"
venue: "Child & Youth Care Forum"
doi: "10.1007/s10566-023-09757-6"
url: "https://link.springer.com/article/10.1007/s10566-023-09757-6"
status: "[Excluido Fase 2 - Criterio EC2 (Foco exclusivo em dropout sem dados de absenteismo ou recusa escolar)]"
qa_score: 9
population_scope: "Educação Básica (Jovens/Youth)"
intervention_scope: "Modelos de Machine Learning / IA e Análise Preditiva"
outcome_scope: "Predição de Risco de Abandono Escolar no K-12"
authors:
  - "P PutrikIJ KantH HoofsR ReijsMJ Jansen"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "SDQ"
algorithms:
  - "[[Regressao_Logistica]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/springer_link
  - fenomeno/absenteismo_cronico
---
# S0702: Prediction of School Dropout Outside School Setting: Potential for Early risk Stratification by Youth Health Care Services in the Netherlands. Results from a Retrospective Cohort Study

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0702`
> - **Autores:** P. Putrik, I. J. Kant, H. Hoofs, R. Reijs, M. J. Jansen
> - **Ano:** 2023 (online mai/2023; fasciculo 2024, Child & Youth Care Forum 53:349-365)
> - **Veículo (Venue):** *Child & Youth Care Forum*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1007/s10566-023-09757-6](https://doi.org/10.1007/s10566-023-09757-6)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1007/s10566-023-09757-6)
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC2 (Foco exclusivo em dropout sem dados de absenteismo ou recusa escolar)]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Background: Early school dropout is an economic, social, and individual problem. In the Netherlands, the Youth Health Care (YHC) service may play a role in primary prevention of school dropout. Objective: We hypothesized that data collected by YHC on family background and Strength and Difficulties Questionnaire (SDQ) scores at ages 10 and 14 is predictive of school dropout. Methods: We analyzed Dutch YHC data from 24,988 children born in 1996-2001. Early school dropout was defined as having left school without diploma by the age of 17. Two multilevel logistic regression models were built with predictors measured at the ages of 10 and 14. Results: A child's SDQ was a strong predictor of early school dropout, in addition to gender and parents' socio-economic status at age 10 and age 14. Models showed moderate prediction performance (ROC value 0.70/0.69, respectively).

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educacao Basica (criancas e adolescentes aos 10 e 14 anos; desfecho aos 17 anos)
- **Intervencao/Tecnologia (Intervention Scope):** Modelagem preditiva supervisionada (Regressao Logistica Multinivel com validacao cruzada 10-fold) combinada ao questionario socioemocional SDQ
- **Desfecho (Outcome Scope):** Predicao de risco de evasao escolar precoce (*school dropout* antes dos 17 anos)
- **Criterios de Inclusao:** `IC1 (em duvida - desfecho e evasao e nao absenteismo), IC2, IC4`
- **Motivo da Inclusao:**
  > `[EM DUVIDA]` Desenvolve e valida um modelo preditivo supervisionado (regressao logistica multinivel com 10-fold CV e curvas ROC) utilizando escores socioemocionais do SDQ aos 10 e 14 anos para estratificacao precoce de risco fora do ambiente escolar (servico YHC). Contudo, o desfecho predito e estritamente a evasao escolar (*dropout* sem diploma aos 17 anos), sem dados de absenteismo ou recusa escolar.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0702`
- **Titulo Completo:** Prediction of School Dropout Outside School Setting: Potential for Early risk Stratification by Youth Health Care Services in the Netherlands. Results from a Retrospective Cohort Study
- **Autores:** P. Putrik, I. J. Kant, H. Hoofs, R. Reijs, M. J. Jansen
- **Ano de Publicacao:** 2023 (publicado online em 25/05/2023; fasciculo 2024)
- **Tipo de Publicacao:** Artigo de Periodico
- **Nome do Veiculo:** Child & Youth Care Forum (53:349-365)
- **DOI:** [10.1007/s10566-023-09757-6](https://doi.org/10.1007/s10566-023-09757-6)
- **Base de Dados:** Springer Link
- **Pais/Regiao de Realizacao do Estudo:** Paises Baixos (provincia de South Limburg)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica - Transicao Ensino Fundamental (*primary*, 10 anos) e Ensino Medio (*secondary*, 14 anos: *Bridge class*, VMBO, HAVO, VWO; exclui educacao especial para deficiencias fisicas/intelectuais graves).
- **Faixa Etaria / Amostra ($N$):** Coorte retrospectiva de 24.988 criancas nascidas entre 1996 e 2001 em South Limburg; subamostra medida aos 10 anos: n = 11.589 (51,2% meninos; 508 [4,4%] evadiram ate 17 anos); subamostra medida aos 14 anos: n = 18.955 (51,0% meninos; 680 [3,6%] evadiram ate 17 anos; estratificada em Bridge n=924, VMBO n=7.720, HAVO n=4.681, VWO n=5.696).
- **Publico-alvo Avaliado:** Populacao geral de criancas e adolescentes acompanhados pelo servico publico municipal *Youth Health Care* (YHC).
- **Fonte dos Dados / Dataset:** Dossies digitais do YHC de South Limburg vinculados (via *Statistics Netherlands*) aos registros nacionais de populacao e ao registro nacional de educacao (DUO).

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** *Strengths and Difficulties Questionnaire* (SDQ - 25 itens em escala Likert de 3 pontos: *Not true*, *Somewhat true*, *Certainly true*; 5 subescalas de 0-10 e escore total de dificuldades 0-40 excluindo prossocial).
- **Natureza da Ferramenta:** Instrumento de triagem psicossocial e socioemocional integrado ao prontuario digital rotineiro do servico de saude infantojuvenil (YHC).
- **Forma de Aplicacao:** Relato dos pais aos 10 anos de idade; autorrelato do proprio adolescente aos 14 anos de idade.
- **Finalidade:** Triagem inicial de dificuldades emocionais, comportamentais, hiperatividade e problemas com pares para estratificacao precoce de risco de evasao escolar.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** [[Machine_Learning]] Supervisionado / Modelagem Preditiva Estatistica (Modelo Linear Misto Generalizado com ligacao logit - Regressao Logistica Multinivel com interceptos aleatorios por escola; Stata 16).
- **Algoritmos Empregados:** [[Regressao_Logistica]] multinivel com selecao *backward* de variaveis (p < 0,10) e validacao cruzada k-fold (k = 10, modulo `CVAUROC`).
- **Tarefa do Modelo:** Classificacao binaria (`enrolled or graduated` vs. `dropped out` pelo menos uma vez sem diploma aos 17 anos), estratificada por nivel de ensino secundario no modelo dos 14 anos devido a interacao significativa SDQ x nivel escolar (p < 0,01).
- **Estagio de Deteccao:** Alerta precoce preventivo fora da escola (aos 10 e aos 14 anos, anos antes do desfecho aos 17 anos).

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Escore total do SDQ (0-40, incluindo problemas emocionais, problemas de conduta, hiperatividade e problemas com pares) e pontos de corte normativos (*normal*, *borderline*, *high*); subescalas individuais testadas separadamente apresentaram desempenho inferior ao escore total.
- **Variaveis Comportamentais / Historico:** Nivel secundario cursado aos 14 anos (*Bridge*, VMBO vocacional, HAVO profissional, VWO cientifico - proxy indireto do desempenho primario/CITO). Ausencia declarada de dados de notas escolares e historico de absenteismo no YHC.
- **Variaveis Familiares / Sociodemograficas:** Sexo da crianca, historico de imigracao (holandes, imigrante de 1a/2a geracao - nao significativo apos ajuste), nivel educacional mais alto dos pais (baixo, medio, alto, desconhecido), recebimento de subsidio estatal de desemprego/bem-estar por pelo menos um dos pais, e pais nao registrados no mesmo endereco (proxy de familia monoparental).
- **Variaveis Institucionais / Contextuais:** Efeito aleatorio da escola (ICC = 7%) e trilha educacional secundaria (VMBO/HAVO/VWO).
- **Features Mais Relevantes Identificadas:** Aos 10 anos: escore total SDQ (OR = 1,07 por ponto [IC 95%: 1,05; 1,09]), baixa escolaridade parental vs. alta (OR = 2,37 [1,72; 3,28]), pais separados/enderecos distintos (OR = 1,59 [1,25; 2,01]), subsidio estatal (OR = 1,57 [1,16; 2,13]) e sexo masculino (OR = 1,37 [1,11; 1,69]). Aos 14 anos no nivel vocacional (VMBO): SDQ total (OR = 1,04 [1,03; 1,06]), baixa escolaridade parental (OR = 2,00), subsidio estatal (OR = 1,62), sexo masculino (OR = 1,61) e pais separados (OR = 1,37). Probabilidades marginais de evasao para aluno desfavorecido variaram de 6% a 16% (aos 10 anos) e de 10% a 16% no VMBO (aos 14 anos) conforme decil do SDQ.

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** Validade previa do SDQ na populacao holandesa citada; nao reporta alfa de Cronbach na coorte atual.
- **Metricas Computacionais (ML):** AUC-ROC aos 10 anos = 0,697 (vs. 0,66 sem SDQ; Hosmer-Lemeshow p = 0,03); AUC-ROC aos 14 anos no VMBO = 0,69 (vs. 0,66 sem SDQ; Hosmer-Lemeshow p = 0,65); AUC < 0,60 nos niveis Bridge, HAVO e VWO (0,54 a 0,57). Valores preditivos positivos (PPV) entre 0,01 e 0,44 (10 anos) e 0,02 a 0,35 (14 anos) para pontos de corte 0,07 e 0,20.
- **Estrategia de Validacao:** Validacao cruzada aleatoria 10-fold (`CVAUROC`), graficos de calibracao, teste de Hosmer-Lemeshow e analises de sensibilidade por quintis/decis e idade exata da aplicacao.
- **Desafios Metodologicos Relatados:** Taxa elevada de falsos positivos (inadequado para intervencoes caras/intensivas sem triagem adicional); NPV nao superior a probabilidade a priori (nao permite descartar risco); 20,7%-22,1% de missing em escolaridade parental; cobertura incompleta do questionario YHC (63% aos 10 anos; 58% e 26% aos 14 anos) com maior taxa de evasao entre nao respondentes (6,6% vs. 4,2% aos 10 anos; 5,7% vs. 3,8% aos 14 anos); transicao de software do prontuario em 2014-2015.
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao etica (METC azM/UM 2020-1573), ligacao pseudoanonimizada por terceiro confiavel (*Statistics Netherlands*), uso de modelo logistico interpretavel e alerta contra risco de estigmatizacao pelo escore SDQ.
- **Limitacoes Declaradas:** Definicao precoce de evasao aos 17 anos (abaixo da idade formal europeia de 18-22 anos); vies de nao resposta dos jovens de maior risco; mudanca de informante (pais aos 10 anos vs. autorrelato aos 14 anos); ausencia de variaveis de desempenho escolar, absenteismo previo, diagnosticos clinicos formais e politicas de apoio de cada escola.
- **Direcoes Futuras:** Integrar dados de notas escolares, absenteismo e saude mental diagnosticada as consultas do YHC para alunos classificados como "em risco"; avaliar barreiras e facilitadores com escolas, familias e profissionais YHC antes da implantacao clinica.

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** 25 itens do SDQ em escala Likert de 3 pontos (5 subescalas: problemas emocionais, problemas comportamentais, hiperatividade, problemas com pares e comportamento prossocial), gerando escore total de dificuldades (0-40). Coletados rotineiramente em duas idades-chave no dossie digital municipal do YHC: relato dos pais aos 10 anos (cobertura ~63%) e autorrelato do adolescente aos 14 anos (cobertura ~58% e 26%).
- **Inventario completo de variaveis e justificativa de escolha:** (1) Escore total e subescalas do SDQ (escolhidos por serem o padrao de triagem socioemocional ja disponivel no YHC); (2) Sexo e origem migratoria (registro municipal); (3) Escolaridade maxima parental, recebimento de subsidio estatal de desemprego/assistencia e residencia conjunta dos pais como proxy de monoparentalidade (determinantes socioeconomicos familiares obtidos de registros nacionais); (4) Nivel escolar secundario aos 14 anos - Bridge, VMBO, HAVO, VWO (escolhido como proxy do desempenho academico previo e estratificador de risco). Justificativa central: usar exclusivamente variaveis ja coletadas rotineiramente fora da escola para permitir estratificacao precoce pelo sistema de saude juvenil.
- **Fundamentacao teorica do identificador:** Fundamenta-se na visao da evasao como processo cumulativo de desengajamento (Bowers et al., 2012; Hauser & Koenig, 2011), na perspectiva de saude publica (Freudenberg & Ruglis, 2007) e na Teoria Social Cognitiva de Bandura (1989), segundo a qual atributos pessoais (saude mental medida pelo SDQ), comportamento e fatores contextuais/familiares interagem continuamente na formacao das trajetorias escolares.
- **Restricoes de recursos e limitacoes:** Vantagem operacional relevante por utilizar dados ja coletados em consultas rotineiras de saude publica com apenas 6-7 preditores simples (baixo custo computacional e sem nova coleta escolar). Contudo, apresenta limitacoes severas de aplicabilidade: desempenho moderado/baixo (AUC ~0,70 aos 10 anos e no VMBO; <0,60 nos demais niveis aos 14 anos), alta taxa de falsos positivos (PPV <= 0,44), dependencia de integracao de registros nacionais e prontuarios eletronicos (vulneravel a trocas de software como em 2014-2015) e nao inclusao de faltas ou notas escolares.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Hipoteses e objetivo claramente definidos para avaliar o poder preditivo de SDQ e contexto familiar no YHC aos 10 e 14 anos para evasao aos 17. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Coorte retrospectiva massiva (N = 24.988), ligacao pseudoanonimizada, definicao exata das variaveis, regressao multinivel e analises de sensibilidade descritas em detalhe. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta AUC-ROC com 10-fold CV, Hosmer-Lemeshow, curvas de calibracao, sensibilidade/especificidade, PPV/NPV e probabilidades marginais. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Incorpora o SDQ (problemas emocionais, comportamentais e com pares) e contexto socioeconomico familiar, mas foca em evasao escolar sem analisar absenteismo ou recusa escolar. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute exaustivamente vies de nao resposta, definicao de evasao aos 17 anos, mudanca de informante (10 vs. 14 anos), falsos positivos e risco de estigmatizacao. |
| **TOTAL** | **Pontuacao de Rigor** | **9 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- **[EM DUVIDA]:** O estudo utiliza modelagem preditiva supervisionada com validacao cruzada 10-fold (`CVAUROC`) e inclui um instrumento socioemocional validado (SDQ) na educacao basica (idades 10 e 14). Porem, o desfecho predito e exclusivamente a evasao escolar (*dropout* sem diploma aos 17 anos) e nao o absenteismo cronico ou a recusa escolar (os proprios autores declaram nao dispor de registros de faltas). Submetido a aprovacao do pesquisador quanto a inclusao na sintese ou exclusao por EC2.
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
