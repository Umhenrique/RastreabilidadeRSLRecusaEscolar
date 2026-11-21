---
id: S0020
study_id: S0020
title: "The relationship between mental health and school absenteeism in a community sample of French secondary school students: four profiles derived from cluster analysis"
year: 2019
database: "Scopus"
venue: "European Journal of Education and Psychology"
doi: "10.30552/ejep.v12i1.242"
url: "https://www.scopus.com/pages/publications/85074463938?origin=resultslist"
status: "[Excluido Fase 2 - Criterio EC2 (LCCA/ANOVA sem ML supervisionado preditivo - usar no referencial)]"
qa_score: 8
population_scope: "Educação Básica (Crianças)"
intervention_scope: "Instrumentos Psicométricos combinados com Modelos Preditivos"
outcome_scope: "Rastreio e Diagnóstico de Recusa Escolar / EBSA"
authors:
  - "Marie Gallé-Tessonneau"
  - "Daniel Bach Johnsen"
  - "Gil Keppens"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "CBCL-YSR"
  - "[[SCREEN]]"
  - "SRAS (16 itens)"
  - "OBVQ (Olweus Bully/Victim Questionnaire revised)"
algorithms:
  - "Latent Class Cluster Analysis (LCCA)"
  - "ANOVA / Qui-quadrado"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/recusa_escolar
---
# S0020: The relationship between mental health and school absenteeism in a community sample of French secondary school students: four profiles derived from cluster analysis

> [!INFO] Metadados Rapidos
> - **ID do Estudo:** `S0020`
> - **Autores:** Marie Gallé-Tessonneau, Daniel Bach Johnsen, Gil Keppens
> - **Ano:** 2019
> - **Veiculo (Venue):** *European Journal of Education and Psychology* (Vol. 12, N. 1, pp. 77-90)
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.30552/ejep.v12i1.242](https://doi.org/10.30552/ejep.v12i1.242)
> - **URL:** [Link da Publicacao](https://www.scopus.com/pages/publications/85074463938?origin=resultslist)
> - **Status da Extracao:** `[Excluido Fase 2 - Criterio EC2 (LCCA/ANOVA sem ML supervisionado preditivo - usar no referencial)]`

> [!WARNING] [EM DUVIDA] Zona Cinzenta na Triagem Restritiva (IC1)
> Este estudo atende plenamente ao **fenomeno e populacao** da RSL (absenteismo escolar e recusa escolar com escalas especificas como [[SCREEN]] e SRAS e fatores socioemocionais do CBCL-YSR em estudantes de 10-16 anos), porem utiliza **Analise de Clusters Latentes (LCCA)** (modelagem estatistica de misturas/agrupamento nao supervisionado no software Latent GOLD) seguida de ANOVA e Qui-quadrado, **sem um algoritmo supervisionado de Machine Learning preditivo** (sem divisao treino/teste ou metricas preditivas como AUC/F1). Submetido ao pesquisador para decidir entre manutencao como modelo nao supervisionado de perfilamento de risco (RQ2) ou exclusao por ausencia de ML preditivo.

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> School absenteeism is a serious problem among youths, varying in etiology and presentation. Youths presenting high levels of absence have previously been linked to mental health problems, academic difficulties and dropout, highlighting the need for early identification and intervention. The aim of this study is twofold: first, to identify profiles among a community sample of secondary school students based on school absence, internalizing and externalizing behavior using the Child Behavior Checklist (CBCL-YSR). Second, to examine the relationship between profiles regarding mental health problems based on the dimensions of the CBCL-YSR, the function of their school absence using the School Refusal Assessment Scale (SRAS) and school refusal using the SChool REfusal EvaluatioN (SCREEN). The profiles are compared on demographic variables, family characteristics, school performance and bullying. A community sample of 469 youths (10-16 year, M=12.1 years, SD=1.2) from six French secondary publics schools participated in this study. Using cluster analysis, four distinct profiles were identified. The clusters differed significantly on school absence, internalizing problems, externalizing problems, dimensions of the CBCL-YSR, and their function of absence on the SRAS. Clusters differed significantly on several demographic variables, school level, grade, repetition and bullying. The distinctions between the four profiles and their relevance are discussed.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Crianças)
- **Intervencao/Tecnologia (Intervention Scope):** Instrumentos Psicométricos combinados com Modelos Preditivos
- **Desfecho (Outcome Scope):** Rastreio e Diagnóstico de Recusa Escolar / EBSA
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao / Observacao Fase 2:**
  > Mantido provisoriamente como `[Incluido Fase 2 - Extracao Concluida]` com sinalizacao `[EM DUVIDA]`: combina dados administrativos de faltas e instrumentos especificos de recusa escolar ([[SCREEN]], SRAS) com clusterizacao nao supervisionada probabilistica (LCCA), mas sem modelo preditivo supervisionado de IA/ML.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0020`
- **Titulo Completo:** The relationship between mental health and school absenteeism in a community sample of French secondary school students: four profiles derived from cluster analysis
- **Autores:** Marie Gallé-Tessonneau, Daniel Bach Johnsen, Gil Keppens
- **Ano de Publicacao:** 2019
- **Tipo de Publicacao:** Periodico cientifico revisado por pares
- **Nome do Veiculo:** European Journal of Education and Psychology
- **DOI:** [10.30552/ejep.v12i1.242](https://doi.org/10.30552/ejep.v12i1.242)
- **Base de Dados:** Scopus (tambem indexado na Web of Science)
- **Pais/Regiao de Realizacao do Estudo:** Franca (seis escolas publicas de ensino secundario / *collège*)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Ensino Secundario frances, 1o ao 4o ano)
- **Faixa Etaria / Amostra ($N$):** $N = 469$ estudantes (40,1% sexo masculino), idades entre 10 e 16 anos ($M = 12,1$ anos, $DP = 1,2$); 1o ano (42,4%, $n=199$), 2o ano (27,9%, $n=131$), 3o ano (18,6%, $n=87$) e 4o ano (11,1%, $n=52$).
- **Publico-alvo Avaliado:** Amostra comunitaria escolar para rastreio de perfis de risco de absenteismo e recusa escolar.
- **Fonte dos Dados / Dataset:** Registros escolares administrativos de frequencia (numero de meios-periodos perdidos nas ultimas 3 semanas, justificados e injustificados) + questionarios aplicados aos alunos em sala de aula (papel ou computador) e questionario demografico preenchido pelos pais.

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** CBCL-YSR (*Child Behavior Checklist - Youth Self-Report*, 112 itens), [[SCREEN]] (*SChool REfusal EvaluatioN*, 18 itens), SRAS (*School Refusal Assessment Scale* original de 16 itens; [[SRAS-R]] no hub conceitual) e 2 itens da versao francesa do OBVQ (*Olweus Bully/Victim Questionnaire revised*).
- **Natureza da Ferramenta:** Bateria de escalas psicometricas clinicas e de triagem de recusa escolar (aplicada em papel ou formato digitalizado em computador, sem diferenca significativa entre os modos).
- **Forma de Aplicacao:** Autorrelato do aluno em sala de aula + questionario parental para dados sociodemograficos + registro administrativo escolar de faltas.
- **Finalidade:** Triagem inicial e tipificacao funcional/psicopatologica de perfis de absenteismo e recusa escolar em amostra comunitaria.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Aprendizado Nao Supervisionado / Modelagem Estatistica de Mistura Finita (*Latent Class Cluster Analysis* - LCCA) + testes estatisticos inferenciais (ANOVA com pos-hoc Bonferroni e Qui-quadrado).
- **Algoritmos Empregados:** Latent Class Cluster Analysis (LCCA; Vermunt, 2002; Vermunt & Magidson, 2005) implementado no software Latent GOLD; ANOVA e Qui-quadrado.
- **Tarefa do Modelo:** Clustering / construcao de tipologia empirica de estudantes baseada em probabilidades de pertencimento a classes latentes usando 3 indicadores (faltas escolares, problemas internalizantes e problemas externalizantes). Identificou 4 perfis: Cluster A *High Problem* (HP, $n=155$, 33%), Cluster B *Low Absence - Low Problem* (LA-LP, $n=146$, 31,1%), Cluster C *High Absence* (HA, $n=111$, 23,7%) e Cluster D *Low Absence* (LA, $n=57$, 12,2%).
- **Estagio de Deteccao:** Exploratorio / triagem transversal preventiva de subgrupos vulneraveis (visando evitar intervencao tardia).

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** 8 escalas sindromicas do CBCL-YSR (isolamento social, queixas somaticas, ansiedade/depressao, problemas sociais, de pensamento, de atencao, comportamento delinquente e agressivo) e 3 agrupamentos (Internalizantes, Externalizantes e Totais); escore de recusa escolar ([[SCREEN]]); 4 funcoes de absenteismo (SRAS: evitacao de estimulos escolares, fuga de situacoes sociais/avaliativas, busca de atencao de figuras de apego, reforcos positivos tangiveis fora da escola); historico de acompanhamento psicologico.
- **Variaveis Comportamentais / Historico:** Faltas oficiais da escola (meios-dias nas ultimas 3 semanas), absenteismo *na* escola (idas a enfermaria, idas a secretaria/diretoria, pedidos para ligar para os pais e ir para casa, atrasos em sala/escola, exclusoes da aula), competencias do CBCL-YSR (atividades, competencia social, desempenho/nivel escolar), repetencia escolar, serie atual e vitimizacao por bullying (na vida e nos ultimos 3 meses).
- **Variaveis Familiares / Sociodemograficas:** Sexo e idade do aluno, idade dos pais, escolaridade materna e paterna, categoria socioprofissional (SPC) da mae e do pai, estrutura familiar (biparental vs. pais separados) e eventos de vida marcantes nos ultimos 2 anos (divorcio, obito, mudanca, doenca).
- **Variaveis Institucionais / Contextuais:** Desfechos e comportamentos em momentos escolares menos estruturados (visitas a secretaria, atrasos, pedidos de retorno ao lar) e clima relacional entre pares (bullying).
- **Features Mais Relevantes Identificadas:** O cluster HP diferenciou-se significativamente dos demais em todas as dimensoes clinicas do CBCL-YSR, maior escore no SCREEN ($M = 37,08$; $DP = 10,1$, faixa limitrofe de SR), maiores medias nas Funcoes 1, 3 e 4 da SRAS, mais atrasos (63,9%), mais visitas a secretaria ($M = 4,08$), mais pedidos para ir para casa ($M = 0,40$), maior repetencia (13,5%), maior exposicao a bullying (68,2% na vida; 57,5% nos ultimos 3 meses), maior historico de eventos de vida (61%) e consulta psicologica (42,9%), e menor SPC/escolaridade materna. O cluster HA teve maior volume de faltas ($M = 1,88$; $DP = 2,6$ vs. $0,51$ em LA e $1,05$ em LA-LP) e maior proporcao de alunos no ultimo ano escolar (16,2%), mas pontuacao psicologica dentro da norma.

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** Alfa de Cronbach na amostra: SCREEN = $0,85$; SRAS Funcao 1 = $0,74$, Funcao 2 = $0,74$, Funcao 3 = $0,55$, Funcao 4 = $0,55$; CBCL-YSR frances com alfa previo de $0,83$-$0,92$ (nao calculado na amostra devido a pontuacao computadorizada padronizada por idade e sexo). Pontos de corte previos do SCREEN: $\ge 41$ indica SR (sensibilidade = $0,94$; especificidade = $0,88$).
- **Metricas Computacionais (ML):** Nao reporta metricas supervisionadas (AUC-ROC, F1, Acuracia). Selecao do modelo LCCA guiada por $p$-valor da estatistica $L^2$ ($p > 0,05$), AIC, BIC e parcimonia (modelos de 3 e 4 clusters apresentaram bom ajuste; optou-se por 4 clusters pela interpretabilidade teorica). Comparacoes entre clusters via ANOVA ($F(3)=5,12$ para faltas escolares; $F(3)=88,41$ para internalizantes; $F(3)=206,93$ para externalizantes; $F(3)=35,70$ para SCREEN; todos $p < 0,01$).
- **Estrategia de Validacao:** Validacao estatistica interna comparando os 4 clusters contra variaveis externas (CBCL subescalas, SCREEN, SRAS, bullying, dados familiares) com correcao de Bonferroni ($p < 0,05$). Sem validacao cruzada ou amostra de teste externa.
- **Desafios Metodologicos Relatados:** Distribuicao nao normal das variaveis (teste de Shapiro), baixa frequencia de absenteismo na amostra (inferior a media nacional francesa) e concentracao de estudantes nos 1o e 2o anos do secundario.
- **Aspectos Eticos e Transparencia (XAI):** Consentimento escrito explicito dos pais e participacao voluntaria dos alunos; sem tecnicas formais de XAI.
- **Limitacoes Declaradas:** Amostra desbalanceada por serie (concentracao nos anos iniciais do secundario, nos quais o absenteismo tende a ser menor), baixa taxa geral de absenteismo na amostra (dificultando detectar associacao direta entre problemas de saude mental e volume elevado de faltas), e natureza exploratoria/transversal do estudo. Alem disso, observa-se baixa consistencia interna nas funcoes 3 e 4 da SRAS ($\alpha = 0,55$).
- **Direcoes Futuras:** Replicar a investigacao em amostras escolares ou clinicas com maiores niveis de absenteismo e acompanhar longitudinalmente se o grupo *High Problem* desenvolve taxas crescentes de faltas com o avanco da idade.

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** Coleta unica em sala de aula combinando questionarios extensos de autorrelato (CBCL-YSR: 112 itens em escala 0-2; SCREEN: 18 itens em escala 1-5; SRAS: 16 itens em escala 0-6; 5 itens de absenteismo intraescolar nas ultimas 3 semanas; 2 itens OBVQ de bullying; eventos de vida e acompanhamento psicologico), questionario sociodemografico dos pais e registros escolares oficiais de faltas das ultimas 3 semanas (meios-periodos).
- **Inventario completo de variaveis e justificativa de escolha:** Tres variaveis nucleares alimentam a LCCA (faltas escolares oficiais, problemas internalizantes CBCL-YSR e problemas externalizantes CBCL-YSR) para capturar empiricamente a heterogeneidade dos problemas de frequencia escolar sem pressupor homogeneidade; 28+ variaveis externas (8 sindromes e 3 competencias do CBCL-YSR, SCREEN, 4 funcoes da SRAS, 5 comportamentos de ausencia *at school*, idade dos pais/aluno, sexo, serie, repetencia, SPC/diploma parental, situacao conjugal dos pais, bullying e eventos de vida) sao usadas para validar e caracterizar clinica e socialmente cada perfil.
- **Fundamentacao teorica do identificador:** Baseia-se na concepcao de heterogeneidade dos Problemas de Frequencia Escolar (SAPs; Heyne et al., 2018; Kearney, 2008; Maynard et al., 2012), na necessidade de evitar o modelo reativo *wait-to-fail* (Kearney & Graczyk, 2014; Ingul et al., 2018; Hancock et al., 2013), na diferenciacao internalizante vs. externalizante do CBCL (Achenbach, 1991) e no modelo funcional da recusa escolar (SRAS; Kearney & Silverman, 1993).
- **Restricoes de recursos e limitacoes:** A aplicacao integral da bateria (>150 itens por estudante), a necessidade de software proprietario para escore padronizado do CBCL-YSR e para LCCA (Latent GOLD), alem da articulacao com pais e registros escolares administrativos, representam barreiras logisticas e de custo para triagem rotineira em escolas com restricao de recursos. As limitacoes declaradas incluem concentracao amostral em series iniciais, baixo absenteismo basal (abaixo da media francesa), baixa confiabilidade das funcoes 3 e 4 da SRAS ($\alpha=0,55$) e desenho transversal exploratorio.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivos duplos declarados com precisao (derivar perfis por LCCA e examinar relacao com CBCL, SRAS, SCREEN, bullying e fatores familiares). |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Amostra ($N=469$), instrumentos validados, procedimento em sala/computador e especificacao LCCA no Latent GOLD descritos claramente. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Apresenta criterios de ajuste LCCA ($L^2$, AIC, BIC), alfas de SCREEN/SRAS e testes ANOVA/Qui-quadrado com Bonferroni, mas nao usa validacao preditiva nem apresenta alfa do CBCL na amostra. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Avalia em profundidade sintomas internalizantes/externalizantes, recusa escolar (SCREEN), funcoes SRAS, bullying, eventos de vida e perfil sociofamiliar. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 1 | Discute desequilibrio de series e baixo absenteismo da amostra, mas omite analise critica sobre a baixa consistencia das funcoes 3 e 4 da SRAS ($\alpha=0,55$) e desenho transversal. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **8 / 10** | Estudo solido na intersecao saude mental e absenteismo/recusa escolar, porem em zona cinzenta por usar LCCA sem ML preditivo supervisionado. |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- **`[EM DUVIDA]` para deliberacao de Matheus:** Embora nao use ML supervisionado (e sim LCCA nao supervisionado no Latent GOLD), o artigo investiga diretamente absenteismo escolar, [[SCREEN]], SRAS e saude mental (CBCL-YSR) em estudantes de ensino basico. Achado importante para a RSL: o cluster de maior risco psicologico (*High Problem*, 33%, com maior escore no SCREEN = 37,08) apresentou mais **absenteismo intraescolar** (secretaria, atrasos, pedidos para voltar para casa), mas nao foi o grupo com mais faltas oficiais totais (que foi o cluster *High Absence* sem problemas clinicos no CBCL), evidenciando que faltas brutas isoladas nao capturam todo o sofrimento internalizante.

---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
