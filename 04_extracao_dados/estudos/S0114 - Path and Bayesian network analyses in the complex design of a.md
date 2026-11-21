---
id: S0114
study_id: S0114
title: "Path and Bayesian network analyses in the complex design of a well-being survey via New Zealand’s Integrated Data Infrastructure"
year: 2026
database: "Scopus"
venue: "Frontiers in Psychiatry"
doi: "10.3389/fpsyt.2026.1826907"
url: "https://www.scopus.com/pages/publications/105048523094?origin=resultslist"
status: "[Excluido Fase 2 - Criterio EC2 (Desfecho fora de escopo: modela bem-estar mental WHO-5 e saude percebida via quantile regression/path/Bayesian Networks; absenteismo e apenas preditor nao significativo p=0.931)]"
qa_score: 9
population_scope: "Educacao Basica (Adolescentes 15+ anos)"
intervention_scope: "Triangulacao Analitica: Quantile Mixed Regression, Path Analysis e Bayesian Networks (HC, TABU, MMHC, RSMAX2) com Pesos Replicados"
outcome_scope: "Bem-Estar Mental (WHO-5), Sentido de Vida e Saude Geral Percebida (Fora de Escopo de Predicao de Recusa/Absenteismo)"
authors:
  - "Irene Suilan Zeng"
  - "Junxiang Hao"
  - "Mandie Foster"
  - "Kelly Marie Jones"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "WHO-5"
  - "General Social Survey (GSS 2018)"
algorithms:
  - "Bayesian Networks (Hill-Climbing, TABU, MMHC, RSMAX2)"
  - "Quantile Mixed-Effects Regression (lqmm)"
  - "Path Analysis (PROC CALIS)"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/absenteismo_cronico
---
# S0114: Path and Bayesian network analyses in the complex design of a well-being survey via New Zealand’s Integrated Data Infrastructure

> [!INFO] Metadados Rapidos
> - **ID do Estudo:** `S0114`
> - **Autores:** Irene Suilan Zeng, Junxiang Hao, Mandie Foster, Kelly Marie Jones
> - **Ano:** 2026
> - **Veiculo (Venue):** *Frontiers in Psychiatry* (Vol. 17, Art. 1826907)
> - **Base de Origem:** `Scopus` (Bases: `['Scopus']`)
> - **DOI:** [10.3389/fpsyt.2026.1826907](https://doi.org/10.3389/fpsyt.2026.1826907)
> - **URL:** [Link da Publicacao](https://www.scopus.com/pages/publications/105048523094?origin=resultslist)
> - **Status da Extracao:** `[Excluido Fase 2 - Criterio EC2 (Desfecho fora de escopo: modela bem-estar mental WHO-5 e saude percebida via quantile regression/path/Bayesian Networks; absenteismo e apenas preditor nao significativo p=0.931)]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Introduction - In mental health research involved with sensitive features and privacy issues, using integrated data offers an efficient alternative to traditional approaches such as interviews or in-person data collection. These conventional methods frequently face logistical barriers, including low response rates among study populations. Using integrated data from multiple existing administrative and survey sources provides protection for participants and economic savings for researchers, despite being constrained by the limitations of the original data sources. Our research questions were: 1) Can we conduct path and network analyses of school absenteeism, psychosocial factors, and mental health outcomes using the integrated survey data from New Zealand's Integrated Data Infrastructure (IDI)? and 2) How can we account for the complex design of the General Social Survey (GSS) to ensure representative inference? Materials and methods - The study population was New Zealand youth enrolled in school, aged 15 years and older in 2018, who participated in the 2018 GSS. The study analyzed the Ministry of Education data integrated with the 2018 GSS survey data from New Zealand's IDI. To explore the relationship between outcomes of including the WHO-5, "perceived life worthwhileness", "perceived general health", and predictors including school absenteeism, psychosocial factors, and family factors, quantile mixed-effects regression, path analysis, and Bayesian network (BN) analysis were used. The complex survey design was calibrated using replicated weights from the GSS, a design-based method for complex sampling, in path and regression analyses, and bootstrap resampling, in BN analysis. Results - In descending order from the weighted path model, overall life satisfaction (standardized path coefficient: 0.36), perceived health condition (0.34), ease in accepting cultural identity (0.12), and trust in the education system (0.07) were all significantly (positively) related to students' mental health well-being (WHO-5). Perceived life worthwhileness correlated with the WHO-5 but was only connected to overall life satisfaction. Similar factors were identified for perceived health, with additional attributing factors, such as fear of crime in the area and the family's overall well-being. Conclusion - The integration of Bayesian networks and path analysis offers rigorous methods for detecting complex interrelationships among integrated mental health outcomes from population data and variables from a complex survey design. Copyright (c) 2026 Zeng, Hao, Foster and Jones.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educacao Basica (Estudantes 15+ anos, Year levels 6-13)
- **Intervencao/Tecnologia (Intervention Scope):** Triangulacao com Regressao Quantilica Mista, Path Analysis e Aprendizado de Estrutura de Redes Bayesianas (BN)
- **Desfecho (Outcome Scope):** Bem-estar mental (WHO-5), sentido de vida (*life worthwhileness*) e saude geral percebida
- **Criterios de Inclusao / Exclusao na Fase 2:** `EXCLUIDO por EC2 / nao atende IC1 restritivo`
- **Motivo da Exclusao:**
  > Excluido na leitura integral (criterio restritivo IC1 / EC2): Os desfechos modelados sao bem-estar mental (WHO-5), sentido de vida e saude geral percebida — e NAO recusa escolar ou absenteismo escolar. O absenteismo escolar (dados do Term 2 de 2015-2018) entra exclusivamente como covariavel/exposicao na regressao quantilica para WHO-5 (onde nao foi significativo: $p = 0,931$ ponderado; $p = 0,80$ nao ponderado) e sequer integra os modelos de Path Analysis e Redes Bayesianas (HC, TABU, MMHC). Trata-se de estudo metodologico sobre calibracao de pesos amostrais complexos (replicated weights) na triangulacao de modelos graficos e regressao.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0114`
- **Titulo Completo:** Path and Bayesian network analyses in the complex design of a well-being survey via New Zealand’s Integrated Data Infrastructure
- **Autores:** Irene Suilan Zeng, Junxiang Hao, Mandie Foster, Kelly Marie Jones
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico (Original Research, Open Access)
- **Nome do Veiculo:** Frontiers in Psychiatry
- **DOI:** [10.3389/fpsyt.2026.1826907](https://doi.org/10.3389/fpsyt.2026.1826907)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Nova Zelandia (base populacional nacional via Integrated Data Infrastructure - IDI)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (estudantes matriculados nos anos escolares 6 a 13 em 2018, com idade $\ge 15$ anos)
- **Faixa Etaria / Amostra ($N$):** $N = 330$ jovens com 15 anos ou mais participantes da 2018 General Social Survey (GSS) vinculados aos registros escolares na IDI (165 meninos, 165 meninas; 84 classificados com absenteismo pela definicao da NZ [presenca $< 80\%$] e 240 com presenca normal; 192 europeus, 66 Maori, 24 povos do Pacifico e 48 asiaticos/outros suprimidos segundo regras de confidencialidade).
- **Publico-alvo Avaliado:** Subamostra escolar saudavel da pesquisa nacional domiciliar GSS 2018 (nenhum caso com internacao hospitalar por suicidalidade entre 2019-2021).
- **Fonte dos Dados / Dataset:** Integrated Data Infrastructure (IDI) da Stats NZ integrando: (1) dados de frequencia escolar do Ministerio da Educacao (2015-2018, Term 2); (2) registros de matricula sociodemograficos (2018); e (3) 2018 General Social Survey (GSS, entrevista presencial assistida por computador com 100 pesos bootstrap replicados).

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** WHO-5 Well-Being Index (indice de bem-estar mental, escore 0-100, corte $< 50$ para baixo bem-estar), itens da General Social Survey (GSS 2018: satisfacao geral com a vida 0-10, sentido de vida / *life worthwhileness*, saude geral percebida de Excelente a Ruim, confianca institucional 0-10, medo de crime 0-10, bem-estar familiar 0-10). Nao utiliza escalas de recusa escolar.
- **Natureza da Ferramenta:** Questionario populacional domiciliar (CAPI) integrado a microdados administrativos nacionais.
- **Forma de Aplicacao:** Entrevista pessoal assistida por computador (GSS, um respondente de 15+ anos por domicilio) vinculada probabilisticamente a registros administrativos escolares.
- **Finalidade:** Avaliacao populacional de bem-estar subjetivo e calibracao metodologica de amostragem complexa em analise de redes.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Aprendizado Hibrido/Complementar (Triangulacao Metodologica): Aprendizado Supervisionado (Regressao Quantilica Mista Linear `lqmm` na mediana P50 com distribuicao de Laplace Assimétrica + Path Analysis via `PROC CALIS`) e Aprendizado Nao Supervisionado (Aprendizado de Estrutura de Redes Bayesianas via `bnlearn` em R com 100 reamostragens bootstrap ponderadas pelos pesos replicados da GSS + experimentos de simulacao Monte Carlo).
- **Algoritmos Empregados:** Hill-Climbing (HC, score-based), TABU search (score-based), Max-Min Hill-Climbing (MMHC, constraint/hybrid) e Restricted Maximization (RSMAX2, hybrid); `lqmm` (Quantile Mixed-Effects Regression); `PROC CALIS` (Path Analysis).
- **Tarefa do Modelo:** Descoberta de estrutura causal/dependencia probabilistica (DAGs) e modelagem explicativa ponderada para bem-estar mental (WHO-5) e saude percebida — nao executa classificacao preditiva de absenteismo ou recusa escolar.
- **Estagio de Deteccao:** Exploratorio / inferencial transversal-retrospectivo sobre determinantes de bem-estar.

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Indice WHO-5 de bem-estar mental (media 65, mediana 68), satisfacao geral com a vida (0-10), percepcao de que a vida vale a pena (*life worthwhileness*), saude geral percebida, facilidade em aceitar a propria identidade cultural, experiencia de discriminacao nos ultimos 12 meses. (Nao mensura ansiedade clinica, depressao clinica ou sintomas de recusa escolar).
- **Variaveis Comportamentais / Historico:** Frequencia escolar no Term 2 (2015-2018), classificada segundo o Ministerio da Educacao da Nova Zelandia em: presenca normal ($>80\%$), ausencia moderada (20%-30% de faltas) e ausencia cronica ($>30\%$ de faltas em meios-dias). Usada apenas na regressao quantilica mista como exposicao repetida.
- **Variaveis Familiares / Sociodemograficas:** Genero, cidadania neozelandesa, etnia (Europeu, Maori, Pacifico, Asiatico/outros), bem-estar geral da familia (0-10), numero de criancas dependentes no domicilio (0, 1, 2, 3+), adequacao do contato com a familia e contato com amigos.
- **Variaveis Institucionais / Contextuais:** Confianca no sistema educacional (0-10), construto latente de confianca institucional (saude, parlamento, policia), medo de crime na vizinhanca (0-10).
- **Features Mais Relevantes Identificadas:** Para WHO-5 no modelo Path ponderado: satisfacao com a vida (coef. padronizado $0,342$ na Tab. 3 / $0,36$ no resumo), saude geral percebida ($0,356$), aceitacao da identidade cultural ($0,158$) e confianca no sistema educacional ($0,109$). Nas BNs (100 bootstraps): aceitacao da identidade cultural (26-36/100 vezes) e confianca no sistema educacional (22-29/100 vezes). **Absenteismo escolar nao teve associacao significativa com WHO-5** (estimativa ponderada $= 0,03$, EP $= 0,40$, $p = 0,931$).

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A (nao avalia confiabilidade psicometrica de escalas na amostra).
- **Metricas Computacionais (ML):** Ajuste do modelo Path ponderado: CFI = $0,98$, AGFI = $0,95$, RMSEA = $0,05$, SRMR = $0,06$; modelos replicados (100 runs): mediana GFI = $0,979$, RMSEA = $0,05$. Regressao quantilica: AIC (4.150.976 ponderado, df = 27; 7.244 nao ponderado com covariaveis vs. 8.303 nulo). BNs: frequencia de aparecimento de arestas em 100 bootstraps (>33% evidencia moderada) e simulacoes ($p = 50, 100, 200$; $n = 300, 500, 1000$) com taxas de Verdadeiro Positivo (TP), Falso Positivo (FP) e Precisao ($P = TP/(TP+FP)$ de 53,2% a 100%).
- **Estrategia de Validacao:** 100 reamostragens bootstrap calibradas por pesos replicados (metodo Rao-Wu e STATA) + triangulacao entre tres familias de modelos + simulacao sintetica de redes esparsas.
- **Desafios Metodologicos Relatados:** Amostra pequena apos vinculacao ($N=330$) frente a alta dimensionalidade; assimetria a esquerda no WHO-5; violacao de independencia pelo desenho amostral complexo da GSS; supressao de celulas pequenas por regras de privacidade da IDI (*Five Safes*); divergencia entre algoritmos de BN (TABU vs MMHC).
- **Aspectos Eticos e Transparencia (XAI):** Governanca *Five Safes* da IDI com dados desidentificados, supressao de contagens pequenas (arredondamento base 3), aprovacao pelo comite de etica da AUT (AUTEC, projeto MAA-2022-23) e alta interpretabilidade grafica via DAGs e diagramas de caminhos.
- **Limitacoes Declaradas:** (1) Vies de respondente saudavel: nenhum caso de hospitalizacao por suicidalidade esteve presente na subamostra da GSS (pois jovens mais graves tendem a nao responder pesquisas); (2) Calibracao por pesos replicados nao corrige totalmente vieses de nao resposta; (3) Programas atuais de BN ponderada nao fornecem distribuicao empirica de AIC e BIC; (4) Restricao etaria da GSS a estudantes $\ge 15$ anos.
- **Direcoes Futuras:** Desenvolver funcoes para agregacao de coeficientes em BNs ponderadas com criterios AIC/BIC e criterios de ajuste no `lqmm` com pesos replicados, alem de testar pipelines hibridos sequenciais entre regressao linear e BNs.

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** Dados integrados da Pesquisa Social Geral (GSS 2018, entrevista CAPI unica) usando o indice WHO-5 (5 itens de bem-estar mental nos ultimos dias, convertido para 0-100) e escalas unicas ordinais/continuas (0-10) de satisfacao com a vida, sentido de vida e saude geral percebida, cruzados com registros administrativos anuais de frequencia do Term 2 (2015-2018) na IDI. Nao ha coleta de ansiedade, depressao clinica ou recusa escolar.
- **Inventario completo de variaveis e justificativa de escolha:** Frequencia escolar (normal $>80\%$, moderada 20-30% faltas, cronica $>30\%$ faltas), genero, cidadania, etnia, bem-estar familiar, numero de criancas dependentes, confianca na educacao/saude/parlamento/policia, saude geral percebida, satisfacao com a vida, sentido de vida, aceitacao da identidade cultural, adequacao do contato com familia e amigos, medo de crime no bairro e discriminacao nos ultimos 12 meses. Escolhidas por estarem disponiveis de forma padronizada e segura na integracao GSS + Ministerio da Educacao dentro da IDI para testar triangulacao estatistico-computacional em desenhos complexos.
- **Fundamentacao teorica do identificador:** Framework de Triangulacao Metodologica (Denzin, 1978; Munafo & Davey Smith, 2018) combinado com Aprendizado Hibrido Complementar (supervisionado + nao supervisionado) e as duas culturas de modelagem de Breiman (2003), sob governanca *Five Safes*.
- **Restricoes de recursos e limitacoes:** Depende de uma infraestrutura nacional de integracao de microdados governamentais de alta complexidade (IDI / Stats NZ), rigorosos protocolos de seguranca (*Five Safes*), pesos bootstrap pre-computados por agencias estatisticas e pacotes avancados em SAS/R — completamente inviavel para implementacao autonoma em escolas comuns com restricao de recursos. Alem disso, sofre de severo vies de selecao (excluiu exatamente os casos clinicos graves e estudantes $< 15$ anos).

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente duas questoes metodologicas sobre viabilidade de path/BN na IDI e calibracao por pesos replicados. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Especifica integracao na IDI, pacotes `lqmm`, `PROC CALIS`, `bnlearn`, 100 pesos replicados (Rao-Wu) e simulacoes. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Apresenta CFI/AGFI/RMSEA/SRMR, AIC, ICs de bootstrap replicado, estabilidade de arestas e TP/FP/Precisao em simulacoes. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Investiga bem-estar WHO-5, identidade cultural e confianca institucional, mas sem foco em recusa escolar e com absenteismo nao significativo. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute explicitamente vies de respondente saudavel, nao resposta residual, ausencia de AIC/BIC em BN ponderada e limite etario. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | Artigo metodologico rigoroso em bioestatistica/redes bayesianas, porem excluido na Fase 2 por desfecho fora de escopo (EC2). |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- **Decisao de Triagem Fase 2:** Excluido pelo criterio **EC2 / IC1 restritivo**. Apesar do titulo mencionar *Bayesian network analyses* e *school absenteeism*, o estudo **nao prediz absenteismo nem recusa escolar** — seu desfecho principal e o bem-estar mental (WHO-5) e saude percebida; o absenteismo entra apenas como preditor na regressao quantilica (onde foi nao significativo, $p = 0,931$) e nao participa dos modelos de Path Analysis ou Redes Bayesianas.

---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
