---
id: S0007
study_id: S0007
title: "Identifying Adolescent Mental Health and Behavioral Risk Profiles: The Role of Childhood Adversities, Family Environment, and Peer Support"
year: 2026
database: "Scopus"
venue: "Brain and Behavior"
doi: "10.1002/brb3.71531"
url: "https://www.scopus.com/pages/publications/105041191505?origin=resultslist"
status: "[Excluido Fase 2 - Criterio EC2 (Desfecho foca perfis gerais de saude mental/EBP e nao recusa escolar/absenteismo; sem modelo preditivo de IA/ML, apenas LCA e regressao multinomial associativa)]"
qa_score: 9
population_scope: "Educação Básica (Adolescentes)"
intervention_scope: "Modelagem Analítico-Preditiva / Network Analysis"
outcome_scope: "Predição de Absenteísmo Crônico Escolar"
authors:
  - "Firoj Al-Mamun"
  - "Moneerah Mohammad ALmerab"
  - "Mohammed A. Mamun"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "SDQ (Strengths and Difficulties Questionnaire - Bengali)"
  - "ISI-2 (Insomnia Severity Index - 2 itens)"
  - "ACEs (Adverse Childhood Experiences)"
algorithms:
  - "Latent Class Analysis (LCA)"
  - "Regressao Logistica Multinomial"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/absenteismo_cronico
---
# S0007: Identifying Adolescent Mental Health and Behavioral Risk Profiles: The Role of Childhood Adversities, Family Environment, and Peer Support

> [!INFO] Metadados Rapidos
> - **ID do Estudo:** `S0007`
> - **Autores:** Firoj Al-Mamun, Moneerah Mohammad ALmerab, Mohammed A. Mamun
> - **Ano:** 2026
> - **Veiculo (Venue):** *Brain and Behavior* (Vol. 16, e71531)
> - **Base de Origem:** `Scopus` (Bases: `['Scopus']`)
> - **DOI:** [10.1002/brb3.71531](https://doi.org/10.1002/brb3.71531)
> - **URL:** [Link da Publicacao](https://www.scopus.com/pages/publications/105041191505?origin=resultslist)
> - **Status da Extracao:** `[Excluido Fase 2 - Criterio EC2 (Desfecho foca perfis gerais de saude mental/EBP e nao recusa escolar/absenteismo; sem modelo preditivo de IA/ML, apenas LCA e regressao multinomial associativa)]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Background: Adolescents in low- and middle-income countries (LMICs) experience a disproportionately high burden of emotional and behavioral problems (EBPs), shaped by early adversities, limited psychosocial support, and structural disadvantages. In Bangladesh, mental health concerns among adolescents remain under-recognized, with limited data on how mental health symptoms cluster and which subgroups are at elevated risk. Identifying distinct risk profiles is essential for informing targeted interventions. Methods: Using data from a cross-sectional school-based survey (N = 1040), we applied latent class analysis (LCA) to identify mental health risk profiles based on emotional symptoms, conduct problems, insomnia, suicidal behavior, truancy, physical fights, bullying, and peer/social isolation. Multinomial logistic regression models were used to examine associations between latent class membership and adverse childhood experiences (ACEs), family/peer relational factors, and sociodemographic characteristics. Results: Three distinct mental health and behavioral risk classes were identified: low risk (36.3%), moderate risk (36.1%), and high risk (27.6%). The high-risk class showed elevated internalizing symptoms, externalizing behaviors, and psychosocial adversities, including conduct problems, loneliness, truancy, bullying, and physical fighting. In the fully adjusted model, sexual abuse (aOR = 2.64) and witnessing violence against the mother (aOR = 3.56) were the strongest predictors of high-risk membership. Lack of peer support was significantly associated with both moderate-risk (aOR = 2.13) and high-risk (aOR = 2.25) membership, whereas poor parental understanding increased the odds of moderate-risk classification (aOR = 1.70). In the interaction model, females exposed to household mental illness had disproportionately higher odds of belonging to the high-risk class. Conclusion: Adolescent mental health in Bangladesh is shaped by a complex interplay of trauma, family functioning, and gender. Trauma-informed, gender-sensitive interventions are urgently needed to address these disparities.

---

## Escopos e Elegibilidade na Triagem (Fase 1 e Revisao Fase 2)
- **Populacao (Population Scope):** Educação Básica (Adolescentes)
- **Intervencao/Tecnologia (Intervention Scope):** Modelagem Analítico-Preditiva / Network Analysis
- **Desfecho (Outcome Scope):** Predição de Absenteísmo Crônico Escolar
- **Criterios de Inclusao (Fase 1):** `IC1, IC2, IC4`
- **Decisao na Leitura Completa (Fase 2 - Criterio IC1 Restritivo):**
  > **[EXCLUIDO - EC2]** Na leitura integral verificou-se dupla desconformidade com o criterio IC1 restritivo: (1) o desfecho modelado nao e recusa escolar nem absenteismo escolar, mas sim perfis latentes gerais de risco em saude mental e problemas emocionais/comportamentais (EBPs), nos quais *truancy* (falta escolar sem permissao) entra apenas como 1 de 11 indicadores binarios da LCA e sequer diferencia a classe de baixo risco (probabilidade condicional 0,485) da classe de alto risco (0,485); (2) nao emprega algoritmos de Inteligencia Artificial ou Machine Learning preditivo (apenas Analise de Classes Latentes via `poLCA` e regressao logistica multinomial associativa/explicativa em R, sem particionamento treino/teste ou metricas preditivas).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0007`
- **Titulo Completo:** Identifying Adolescent Mental Health and Behavioral Risk Profiles: The Role of Childhood Adversities, Family Environment, and Peer Support
- **Autores:** Firoj Al-Mamun, Moneerah Mohammad ALmerab, Mohammed A. Mamun
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico cientifico revisado por pares
- **Nome do Veiculo:** Brain and Behavior (Wiley Periodicals LLC)
- **DOI:** [10.1002/brb3.71531](https://doi.org/10.1002/brb3.71531)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Phulbari, subdistrito de Kurigram, Bangladesh (coleta entre setembro e outubro de 2024)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Ensino Secundario, Grades 7 a 10)
- **Faixa Etaria / Amostra ($N$):** $N = 1.040$ casos completos apos delecao *listwise* (faixas etarias: 12-14 anos = 58,65% [$n=610$] e 15-17 anos = 41,35% [$n=430$]; 52,79% sexo masculino [$n=549$], 47,21% sexo feminino [$n=491$]; 51,92% area urbana e 48,08% rural), oriundos de 8 escolas (3 urbanas e 5 rurais) por amostragem estratificada por conglomerados em dois estagios.
- **Publico-alvo Avaliado:** Adolescentes escolares matriculados e presentes no dia da coleta (perfis gerais de risco psicossocial e saude mental; nao focado especificamente em recusa escolar).
- **Fonte dos Dados / Dataset:** Inquerito escolar transversal por questionario autorrelatado aplicado presencialmente em sala de aula (estudo piloto previo com 30 alunos excluido da amostra final).

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** *Strengths and Difficulties Questionnaire* (SDQ - versao em bengali, 4 subescalas clinicas), *Insomnia Severity Index* breve de 2 itens (ISI-2), itens estruturados de *Adverse Childhood Experiences* (ACEs) e itens do GSHS/Khan et al. (2020) para contexto familiar, pares e comportamentos de risco. Nao utiliza [[SRAS-R]] ou [[SCREEN]].
- **Natureza da Ferramenta:** Questionarios psicometricos e epidemiologicos tradicionais em papel (autorrelato).
- **Forma de Aplicacao:** Autorrelato do aluno presencialmente em sala de aula com apoio de pesquisadores e professores para esclarecimentos.
- **Finalidade:** Rastreio epidemiologico transversal de problemas emocionais e comportamentais (EBPs) e exposicao a adversidades.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Modelagem Estatistica Latente e Associativa (Analise de Classes Latentes - LCA nao supervisionada probabilistica + Regressao Logistica Multinomial hierarquica). Nao implementa algoritmos de IA/ML preditivo nem [[Explicabilidade_XAI]].
- **Algoritmos Empregados:** Latent Class Analysis (LCA, pacote `poLCA` no R v4.3.1, estimacao por maxima verossimilhanca com 5.000 iteracoes e 50 inicios aleatorios; 2 a 5 classes testadas) e 6 modelos hierarquicos de Regressao Logistica Multinomial (pacote `nnet`).
- **Tarefa do Modelo:** Agrupamento latente (3 perfis de risco em saude mental: Baixo risco [36,27%, $n=382$], Risco moderado [36,10%, $n=381$] e Alto risco [27,63%, $n=277$]) seguido de regressao associativa para estimar razoes de chances ajustadas ($aOR$) de pertencimento as classes.
- **Estagio de Deteccao:** Analise epidemiologica transversal associativa (nao configura sistema de alerta precoce ou modelo preditivo longitudinal).

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Sintomas emocionais (SDQ $\ge 7$), problemas com pares (SDQ $\ge 6$), hiperatividade/desatencao (SDQ $\ge 7$), sintomas de insonia (ISI-2 $\ge 6$), tentativa de suicidio ao longo da vida (1 item binario) e solidao nos ultimos 12 meses (1 item binario).
- **Variaveis Comportamentais / Historico:** Problemas de conduta (SDQ $\ge 5$), falta escolar sem permissao / *truancy* no ultimo mes (1 item binario), envolvimento em briga fisica no ultimo ano (1 item binario), vitimizacao por bullying no ultimo mes (1 item binario) e ausencia de amigos proximos (1 item binario).
- **Variaveis Familiares / Sociodemograficas:** Genero, faixa etaria, serie escolar (Grades 7-10), tipo de familia (nuclear 70,67% vs. conjunta 29,33%), localizacao (urbana vs. rural), verificacao de tarefas pelos pais, ma compreensao com os pais (72,88%), falta de apoio de pares (37,31%) e 6 dominios de ACEs (abuso psicologico [19,13%], fisico [7,79%], sexual [5,48%], doenca mental domiciliar [18,08%], violencia contra a mae [7,12%] e familiar preso [8,37%]).
- **Variaveis Institucionais / Contextuais:** Localizacao geografica da escola (urbana vs. rural) e clima relacional entre pares na escola (bullying e apoio de pares).
- **Features Mais Relevantes Identificadas:** No modelo ajustado sem interacoes (Modelo 3, Tabela 7), os principais fatores associados a classe de alto risco (vs. baixo risco) foram violencia contra a mae ($aOR = 3,56$; IC 95% [1,51; 8,38]; $p = 0,004$), abuso sexual ($aOR = 2,64$; IC 95% [1,16; 6,02]; $p = 0,021$) e falta de apoio de pares ($aOR = 2,25$; IC 95% [1,59; 3,19]; $p < 0,001$). Para risco moderado: falta de apoio de pares ($aOR = 2,13$; $p < 0,001$) e ma compreensao com os pais ($aOR = 1,70$; $p = 0,003$). No Modelo 6, destacou-se a interacao genero feminino $\times$ doenca mental no domicilio ($aOR = 2,43$; $p = 0,042$). A variavel *truancy* apresentou probabilidade condicional identica nas classes de baixo risco (0,485) e alto risco (0,485), sendo menor apenas no risco moderado (0,090).

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** Nao reporta alfa de Cronbach ou omega na amostra atual; adota pontos de corte clinicos validados na literatura para o SDQ (Goodman et al., 1998) e ISI-2 (sensibilidade = 84%, especificidade = 76%; Kraepelien et al., 2021).
- **Metricas Computacionais (ML):** Nao aplica metricas de classificacao preditiva (Acuracia, F1, AUC-ROC). Reporta indices de ajuste da LCA para 3 classes: Log-verossimilhanca = $-4.896,024$, AIC = $9.862,047$, BIC = $10.035,190$, aBIC = $9.924,027$, $G^2 = 745,198$, Entropia = $0,761$, estabilidade em 50/50 inicios aleatorios e probabilidades posteriores medias entre $0,750$ e $0,804$. Na regressao multinomial: McFadden $R^2$ de $0,033$ (Modelo 1) a $0,072$ (Modelo 6), Cox & Snell $R^2$ de $0,078$ a $0,163$, McKelvey & Zavoina $R^2$ de $0,069$ a $0,144$.
- **Estrategia de Validacao:** Nenhuma validacao preditiva (sem split treino/teste, sem validacao cruzada e sem coorte externa); avaliacao apenas de estabilidade de convergencia da LCA (50 inicios aleatorios) e comparacao hierarquica de modelos de regressao.
- **Desafios Metodologicos Relatados:** Dados faltantes entre 0% e 5,35% (consistentes com MCAR, $p = 0,658$, tratados por delecao *listwise*), ausencia do teste Lo-Mendell-Rubin e de diagnostico formal de independencia local no pacote `poLCA`, e entropia apenas moderada ($0,761$).
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao etica pelo comite CHINTA Research Bangladesh (`chinta/2024/08(1)`), consentimento livre e esclarecido escrito dos pais/responsaveis e alunos, e declaracao de uso de IA generativa (ChatGPT/OpenAI) apenas para revisao linguistica do manuscrito. Sem tecnicas de XAI.
- **Limitacoes Declaradas:** Desenho transversal impede inferencia causal; uso de autorrelato sujeito a vies de memoria e desejabilidade social (especialmente em abuso infantil); inclusao apenas de adolescentes presentes na escola (excluindo jovens fora da escola ou ausentes no dia); amostra restrita a um unico subdistrito de Bangladesh; perda de eficiencia estatistica por delecao *listwise*; limitacoes tecnicas do `poLCA`; e precisao de classificacao apenas moderada (entropia = 0,761).
- **Direcoes Futuras:** Estudos longitudinais para mapear trajetorias causais, incorporacao de biomarcadores ou entrevistas clinicas diagnosticas (ex.: cortisol), expansao amostral para jovens fora da escola e avaliacao de intervencoes escolares e familiares sensiveis a trauma e genero.

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** Coleta transversal unica (setembro-outubro de 2024) por questionario estruturado de autorrelato em sala de aula (com estudo piloto previo em 30 estudantes). Inclui 20 itens da versao bengali do SDQ (4 subescalas de 5 itens em escala 0-2 dicotomizadas por cortes clinicos: emocional $\ge 7$, conduta $\ge 5$, hiperatividade $\ge 7$, pares $\ge 6$), 2 itens do ISI (Likert 0-4, corte $\ge 6$), 6 dominios binarios de ACEs, 3 itens binarios de relacionamento familiar/pares (ultimo mes) e 6 itens individuais binarios de estressores/comportamentos (suicidio na vida, solidao no ano, *truancy* no mes, briga no ano, bullying no mes e ausencia de amigos proximos).
- **Inventario completo de variaveis e justificativa de escolha:** (a) 11 indicadores binarios na LCA (sintomas emocionais, conduta, hiperatividade, problemas com pares, insonia, tentativa de suicidio, solidao, *truancy*, briga fisica, bullying, sem amigos proximos) escolhidos pela relevancia empirica na coocorrencia de problemas internalizantes, externalizantes e estressores sociais na adolescencia; (b) 6 variaveis de ACEs (abuso psicologico, fisico, sexual; doenca mental familiar; violencia materna; encarceramento familiar) e 3 variaveis proximais (monitoramento de licao de casa, compreensao parental, apoio de pares) para explicar vulnerabilidades de trauma e suporte; (c) 5 covariaveis sociodemograficas (genero, idade, serie, tipo familiar, area urbana/rural) e termos de interacao genero $\times$ ACE para captar disparidades contextuais.
- **Fundamentacao teorica do identificador:** Fundamenta-se na perspectiva da Psicopatologia do Desenvolvimento (Cicchetti & Rogosch, 2002; Cicchetti & Toth, 2008), argumentando que traumas precoces comprometem sistemas de regulacao emocional e controle comportamental; na Teoria dos Sistemas Ecologicos de Bronfenbrenner (1979), integrando vulnerabilidades individuais aos microssistemas familiar e de pares; e na Hipotese de Seguranca Emocional (Davies & Cummings, 1994) para explicar o impacto da violencia domestica.
- **Restricoes de recursos e limitacoes:** Embora utilize instrumentos gratuitos de autorrelato (SDQ-Bengali e itens curtos do GSHS/ISI-2) adequados a paises de baixa/media renda (LMICs), a aplicacao presencial exige equipe treinada, autorizacao institucional e triagem de consentimento, alem de falhar em capturar estudantes cronicamente ausentes ou evadidos (excluidos pela ausencia no dia da coleta). Limita-se ainda pelo desenho transversal, autorrelato em temas estigmatizados (abuso sexual/violencia domestica), amostra local nao generalizavel, delecao *listwise*, ausencia de teste de Lo-Mendell-Rubin e entropia moderada (0,761).

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo explicito de identificar perfis latentes de saude mental/comportamento e testar associacoes com ACEs, familia, pares e genero. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Amostragem estratificada em 2 estagios ($N=1.040$), criterios de elegibilidade, pontos de corte das escalas e pacotes R (`poLCA`, `nnet`, `MissMech`) detalhados. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Apresenta AIC, BIC, aBIC, entropia ($0,761$) e pseudo-$R^2$ da regressao, mas nao realiza validacao preditiva nem calcula alfa de Cronbach na amostra. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa em profundidade sintomas internalizantes/externalizantes, ACEs, compreensao parental, apoio de pares e moderacao por genero (embora o foco nao seja recusa escolar). |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Secao especifica discute corte transversal, vies de autorrelato, exclusao de alunos ausentes/fora da escola, entropia moderada e limitacoes do `poLCA`. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | Estudo metodologicamente rigoroso em saude mental, porem excluido na Fase 2 por EC2 (desfecho fora do escopo e ausencia de ML preditivo). |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- Estudo excluido sob criterio restritivo IC1/EC2: apesar de mencionar `truancy` no resumo e utilizar LCA + regressao multinomial, a falta escolar e apenas um entre onze indicadores de perfil geral de risco psicopatologico (com igual prevalencia condicional de 0,485 nos perfis de baixo e alto risco) e nao ha modelagem preditiva de IA/ML para recusa escolar ou absenteismo.

---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
