---
id: S0058
study_id: S0058
title: "Anxiety as a risk factor for school absenteeism: What differentiates anxious school attenders from non-attenders?"
year: 2013
database: "Scopus"
venue: "Annals of General Psychiatry"
doi: "10.1186/1744-859x-12-25"
url: "https://www.scopus.com/pages/publications/85040697712?origin=resultslist"
status: "[Excluido Fase 2 - Criterio EC2 (MDA classica in-sample sem validacao cruzada/ML - usar no referencial)]"
qa_score: 9
population_scope: "Educacao Basica (Ensino Medio)"
intervention_scope: "Instrumentos Diagnosticos e Escalas Psicometricas + Analise Discriminante Multigrupo (MDA)"
outcome_scope: "Diagnostico e Diferenciacao de Absenteismo Escolar Ansioso / Recusa Escolar"
authors:
  - "Jo Magne Ingul"
  - "Hans M. Nordahl"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "[[SCARED]]"
  - "SMFQ"
  - "IPDS"
  - "SDQ"
  - "READ"
  - "SLE"
algorithms:
  - "Multigroup Discriminant Analysis (MDA)"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/recusa_escolar
---
# S0058: Anxiety as a risk factor for school absenteeism: What differentiates anxious school attenders from non-attenders?

> [!INFO] Metadados Rapidos
> - **ID do Estudo:** `S0058`
> - **Autores:** Jo Magne Ingul, Hans M. Nordahl
> - **Ano:** 2013
> - **Veiculo (Venue):** *Annals of General Psychiatry* (Vol. 12, Art. 25)
> - **Base de Origem:** `Scopus` (Bases: `['Scopus']`)
> - **DOI:** [10.1186/1744-859x-12-25](https://doi.org/10.1186/1744-859x-12-25)
> - **URL:** [Link da Publicacao](https://www.scopus.com/pages/publications/85040697712?origin=resultslist)
> - **Status da Extracao:** `[Excluido Fase 2 - Criterio EC2 (MDA classica in-sample sem validacao cruzada/ML - usar no referencial)]`
> - **Observacao de Triagem:** **[EM DUVIDA]** — Estudo empirico altamente aderente ao fenomeno (absenteismo escolar ansioso/recusa escolar com fatores socioemocionais profundos), porem emprega Analise Discriminante Multigrupo (MDA) classica no SPSS 18 para classificacao em 4 grupos (73% de acuracia in-sample, sem validacao cruzada/split treino-teste), configurando zona cinzenta entre estatistica multivariada classica e Machine Learning preditivo. Aguarda deliberacao do pesquisador.

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Background: Anxiety is a major risk factor for problematic school absenteeism. However, most anxious students attend school. What differentiates anxious attenders from non-attenders? Method: High school students (N = 865) were assigned to groups based on anxiety and absenteeism scores. These groups were then tested for differences in risk factor profiles using discriminant analysis. Results: Anxious school attenders were less affected by negative personality traits, total number of risk factors, social anxiety, panic, and behavioural and family problems. They also displayed greater resilience. Conclusions: This study indicates that the risk for problematic school absenteeism increases as the number of risk factors aggregate and that treatment for anxious school refusal should be based on a profile of the individual's risk factors. (c) 2013 Ingul and Nordahl.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educacao Basica (Ensino Medio)
- **Intervencao/Tecnologia (Intervention Scope):** Instrumentos Psicometricos + Analise Discriminante Multigrupo (MDA)
- **Desfecho (Outcome Scope):** Diferenciacao e Classificacao de Absenteismo Escolar Problematico com Ansiedade
- **Criterios de Inclusao:** `IC1 [EM DUVIDA - MDA classica sem split/CV], IC2, IC3, IC4`
- **Motivo da Avaliacao (Fase 2):**
  > **[EM DUVIDA]**: Atende plenamente ao escopo clinico-educacional ([[Recusa_Escolar]] / [[Absenteismo_Cronico]] associado a ansiedade, depressao, personalidade, resiliencia e ambiente escolar/familiar em adolescentes), mas a modelagem preditiva utiliza Analise Discriminante Multigrupo (MDA) via SPSS 18 sem validacao cruzada ou algoritmos modernos de ML.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0058`
- **Titulo Completo:** Anxiety as a risk factor for school absenteeism: What differentiates anxious school attenders from non-attenders?
- **Autores:** Jo Magne Ingul, Hans M. Nordahl
- **Ano de Publicacao:** 2013
- **Tipo de Publicacao:** Periodico (Artigo Original, Open Access)
- **Nome do Veiculo:** Annals of General Psychiatry
- **DOI:** [10.1186/1744-859x-12-25](https://doi.org/10.1186/1744-859x-12-25)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Noruega (Nord-Trondelag, duas escolas de ensino medio)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Ensino Medio / High School noruegues)
- **Faixa Etaria / Amostra ($N$):** $N = 865$ estudantes participantes (de 1.025 elegiveis; taxa de resposta de 84,4%), sendo 452 mulheres (52,3%) e 413 homens (47,7%), idade entre 16 e 21 anos ($M = 17,21$; $DP = 1,28$). Divididos em 4 grupos: alta ansiedade + alta ausencia ($n = 21$), alta ansiedade + baixa ausencia ($n = 73$), ansiedade normal + alta ausencia ($n = 80$) e ansiedade normal + baixa ausencia ($n = 636$). *(Nota: a soma dos 4 subgrupos na Tabela 1 totaliza 810 devido a dados faltantes em alguns participantes na classificacao por grupo).*
- **Publico-alvo Avaliado:** Estudantes adolescentes com diferentes niveis de ansiedade e absenteismo problematico (corte $\ge 13,5$ dias de falta no primeiro semestre letivo).
- **Fonte dos Dados / Dataset:** Questionario de autorrelato aplicado em sala de aula durante horario escolar + registros oficiais de faltas (em dias e horas) informados pelos professores no primeiro semestre.

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** [[SCARED]] (Screen for Child Anxiety-Related Emotional Disorders, 41 itens, corte $\ge 26$), SMFQ (Short Mood and Feeling Questionnaire, 13 itens), IPDS (Iowa Personality Disorders Screen, 11 itens, corte $\ge 2$ no subconjunto 1, 3-8), SDQ (Strengths and Difficulties Questionnaire, 25 itens), READ (Resilience Scale for Adolescents, 28 itens), SLE (12 eventos estressantes baseados em Holmes & Rahe e Life Events Checklist). *(Nota: a nota da Fase 1 listava SCREEN e SRAS-R por inferencia automatica, porem o artigo real utiliza SCARED, SMFQ, IPDS, SDQ, READ e SLE, e nao SCREEN ou SRAS-R).*
- **Natureza da Ferramenta:** Bateria de instrumentos psicometricos tradicionais (escalas clinicas de rastreio e avaliacao comportamental/resiliencia).
- **Forma de Aplicacao:** Autorrelato do aluno em papel/questionario durante horario escolar (alunos ausentes no dia responderam em ate 2 semanas apos retorno), combinado com registro administrativo docente de faltas.
- **Finalidade:** Triagem, estratificacao em grupos de risco (ansiedade x absenteismo) e identificacao de perfis de fatores de risco para orientar tratamento individualizado.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Analise Estatistica Multivariada / Classificacao Linear Discriminante (Multigroup Discriminant Analysis - MDA, com ANOVA univariada e testes post-hoc Fisher LSD, alem de testes t e qui-quadrado em SPSS v18). Nao emprega algoritmos modernos de Machine Learning supervisionado ou Deep Learning.
- **Algoritmos Empregados:** Multigroup Discriminant Analysis (MDA / Analise Discriminante Linear Multigrupo).
- **Tarefa do Modelo:** Classificacao multiclasse (4 grupos combinando ansiedade alta/normal e ausencia alta/normal) e reducao dimensional em funcoes discriminantes canonicas.
- **Estagio de Deteccao:** Analise transversal / diagnostico de perfil diferencial a posteriori (identificar fatores que distinguem estudantes ansiosos que frequentam vs. os que faltam).

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Ansiedade total e subtipos pela [[SCARED]] (ansiedade social, sindrome do panico/somatica, ansiedade generalizada, ansiedade de separacao, evitacao escolar), sintomas depressivos (SMFQ), tracos/problemas de personalidade (IPDS), problemas emocionais e de conduta/hiperatividade (SDQ), resiliencia (READ), severidade psiquiatrica acumulada (contagem de escalas acima do ponto de corte) e eventos de vida estressantes (SLE).
- **Variaveis Comportamentais / Historico:** Dias/horas de faltas escolares registradas pelos professores no primeiro termo (corte de absenteismo problematico $\ge 13,5$ dias), uso de alcool semanal, experimentacao de cannabis e outros narcoticos, participacao em atividades de lazer e exercicio fisico, ressentimento em ir a escola.
- **Variaveis Familiares / Sociodemograficas:** Sexo, idade, escolaridade e ocupacao do pai e da mae, morar com os pais, economia familiar percebida, numero de amigos proximos, saude fisica percebida e doenca cronica.
- **Variaveis Institucionais / Contextuais:** Programa educacional, tamanho da escola, contato com professor regente, percepcao de ser tratado com respeito na escola, sentimento de seguranca na escola, dificuldades de aprendizagem e vitimizacao por bullying.
- **Features Mais Relevantes Identificadas:** Na Funcao Discriminante 1 (85,4% da variancia entre grupos; $R = 0,868$): severidade psiquiatrica acumulada ($0,872$), tracos de personalidade negativos ($0,318$), depressao SMFQ ($0,308$), problemas relacionais SDQ ($0,239$), seguranca escolar ($-0,236$). Na Funcao 2 (10,1%; $R = 0,516$): uso de narcoticos ($0,546$), cannabis ($0,301$), mae trabalhando ($-0,279$), problemas comportamentais SDQ ($0,256$). Na Funcao 3 (4,5%; $R = 0,371$): atividades de lazer ($0,370$), idade ($-0,319$), hiperatividade SDQ ($-0,305$), respeito na escola ($0,303$), resiliencia ($0,207$). Na comparacao direta entre ansiosos com alta vs. baixa ausencia: ansiedade social ($p = 0,034$), panico/somatico ($p = 0,041$), severidade psiquiatrica ($p = 0,013$), problemas comportamentais SDQ ($p = 0,019$), uso de narcoticos ($p = 0,048$), menos amigos proximos ($p < 0,001$) e pior percepcao da propria saude ($p = 0,038$).

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** Consistencia interna na amostra (Alfa de Cronbach): SCARED total $\alpha = 0,94$ (panico/somatico $0,87$, ansiedade generalizada $0,88$, fobia social $0,85$, separacao $0,74$, evitacao escolar $0,62$); SMFQ $\alpha = 0,88$; SDQ total $\alpha = 0,72$ (problemas de conduta $0,58$, hiperatividade $0,68$); READ $\alpha = 0,94$.
- **Metricas Computacionais (ML):** Acuracia global de classificacao da MDA na amostra total ($N = 865$) = **73%** (com 28,2% de erro concentrado entre os dois grupos de ansiedade normal: baixa vs. alta ausencia). Lambdas de Wilks significativos para as 3 funcoes ($\Lambda_1 = 0,156$, $p < 0,001$; $\Lambda_2 = 0,633$, $p < 0,001$; $\Lambda_3 = 0,862$, $p < 0,01$); correlacoes canonicas $R = 0,87$, $0,52$ e $0,37$. Poder estatistico reportado: 81,4%.
- **Estrategia de Validacao:** Avaliacao puramente in-sample (sem divisao treino/teste, sem validacao cruzada k-fold e sem validacao temporal em segundo momento).
- **Desafios Metodologicos Relatados:** Tamanho reduzido do subgrupo critico de alta ansiedade + alta ausencia ($n = 21$), desbalanceamento acentuado entre os 4 grupos ($21, 73, 80, 636$), uso de pontos de corte para dicotomizar variaveis continuas (ansiedade e faltas) e impossibilidade de validar as funcoes discriminantes em amostra independente.
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao pelo comite de etica regional (REK Midt-Norge n. 008-04) e termos de consentimento via escola; interpretabilidade direta via cargas estruturais das funcoes discriminantes canonicas.
- **Limitacoes Declaradas:** (1) Delineamento transversal impede inferencia causal ou temporal entre fatores de risco e frequencia escolar; (2) Dicotomizacao por pontos de corte pode gerar sensibilidade a pequenas variacoes nos limiares; (3) Ausencia de medida de funcionamento cognitivo dos alunos; (4) Ausencia de validacao cruzada (split-sample ou teste-reteste longitudinal) para generalizacao dos coeficientes discriminantes.
- **Direcoes Futuras:** Realizar validacao cruzada das funcoes discriminantes em novas amostras ou delineamentos longitudinais; ampliar manuais de intervencao para recusa escolar ansiosa incluindo manejo de isolamento social, problemas comportamentais, dinamicas familiares e fortalecimento de resiliencia (alem do tratamento isolado da ansiedade).

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** Questionario estruturado de autorrelato aplicado presencialmente em sala de aula durante o horario letivo (com recaptura em ate 2 semanas para ausentes no dia da coleta), composto por: [[SCARED]] (41 itens em escala de 3 pontos, corte $\ge 26$ para alta ansiedade, cobrindo panico/somatico, ansiedade generalizada, separacao, fobia social e evitacao escolar), SMFQ (13 itens em escala de 3 pontos para depressao), IPDS (11 itens binarios/criterios DSM-IV para transtornos de personalidade, corte $\ge 2$), SDQ (25 itens em 5 subescalas), READ (28 itens Likert de 5 pontos para resiliencia), SLE (12 itens sim/nao de eventos estressantes), alem de itens categoricos de contexto escolar, familiar e registro oficial docente das faltas em dias e horas ao longo do primeiro semestre (corte $\ge 13,5$ dias para alta ausencia).
- **Inventario completo de variaveis e justificativa de escolha:** Todas as variaveis (exceto os escores da propria SCARED, usados para definir os grupos-alvo) foram inseridas na MDA: severidade psiquiatrica acumulada (contagem de escalas clinicas acima do corte), tracos de personalidade (IPDS), depressao (SMFQ), problemas comportamentais, de relacionamento com pares e hiperatividade (SDQ), uso de alcool semanal, cannabis e outros narcoticos, eventos negativos de vida (SLE), resiliencia (READ), numero de amigos proximos, atividades de lazer, exercicio fisico, percepcao de seguranca na escola, ser tratado com respeito na escola, ressentimento em ir a escola, bullying sofrido, contato com professor, dificuldades de aprendizagem, tamanho da escola, doenca cronica, percepcao da propria saude, morar com os pais, economia familiar, trabalho e escolaridade do pai e da mae, sexo e idade. A escolha justifica-se pela hipotese de agregacao cumulativa de risco (comorbidades externalizantes, tracos de personalidade, fatores psicossociais e subtipos de ansiedade, especialmente fobia social) baseada em Egger et al. (2003), Lounsbury et al. (2004) e Kearney (2008), visando superar a visao de que a ansiedade isolada explica o absenteismo.
- **Fundamentacao teorica do identificador:** Modelo conceitual de absenteismo escolar problematico de Kearney (2008) para definicao do limiar de ausencia ($\ge 13,5$ dias), modelo de acumulacao/agregacao de fatores de risco psiquiatricos e psicossociais ao longo do tempo (Egger et al., 2003; Ingul et al., 2012), e construto disposicional de "absence proneness" associado a tracos de personalidade (Lounsbury et al., 2004) e cognicoes negativas/ataques de panico nao clinicos na adolescencia (Maric et al., 2012; Mattis & Ollendick, 2002).
- **Restricoes de recursos e limitacoes:** A coleta depende da aplicacao presencial de uma bateria extensa (>130 itens combinando SCARED, SMFQ, IPDS, SDQ, READ, SLE e dados demograficos/escolares) em horario de aula, exigindo logistica de recaptura por ate 2 semanas para alunos ausentes — justamente o publico-alvo mais critico. Em escolas com restricao de recursos, o tempo de aplicacao, a pontuacao multi-escala e a falta de integracao automatizada com sistemas de frequencia impoem barreira operacional, agravada pelo fato de o modelo MDA nao ter sido validado fora da amostra original e depender de dados que os proprios faltosos podem nao responder se estiverem ausentes de forma prolongada.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define explicitamente a questao de diferenciar estudantes ansiosos assiduos dos nao assiduos e testar combinacoes de risco via MDA. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Descreve amostra ($N=865$), comparacao entre participantes e nao participantes, instrumentos com cortes definidos e MDA no SPSS 18. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Reporta Cronbach, Wilks' lambda, correlacoes canonicas e 73% de acuracia in-sample, mas sem split treino/teste ou validacao cruzada. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analise abrangente de subtipos de ansiedade, depressao, personalidade, resiliencia, comorbidades externalizantes, pares e clima escolar. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute transversalidade, arbitrariedade de pontos de corte, ausencia de medida cognitiva e falta de validacao cruzada da MDA. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | Estudo clinico-epidemiologico robusto, porem em zona cinzenta metodologica por usar MDA classica sem validacao externa/CV. |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- **[EM DUVIDA para decisao do pesquisador]:** O artigo aborda exatamente a diferenciacao entre alunos ansiosos que frequentam vs. os que faltam a escola (nucleo teorico da RSL), mas usa Analise Discriminante Multigrupo (MDA) classica no SPSS sem split de validacao. Avaliar se permanece no corpus principal (IC1 ampliado para modelos estatisticos discriminantes) ou se migra para o referencial teorico/clinico (por nao ser ML preditivo validado out-of-sample).
- Achado importante para a RSL: ansiedade isolada nao basta para explicar absenteismo; a **agregacao de fatores de risco** (severidade psiquiatrica, tracos de personalidade, fobia social, panico, problemas comportamentais, baixa rede de amigos e uso de substancias) e o principal diferenciador.

---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
