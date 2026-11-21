---
id: S0532
study_id: S0532
title: "A Latent Class Analysis of Mental Health Symptoms in Primary School Children: Exploring Associations with School Attendance Problems"
year: 2023
database: "Springer Link"
venue: "School Mental Health"
doi: "10.1007/s12310-023-09610-0"
url: "https://link.springer.com/article/10.1007/s12310-023-09610-0"
status: "[Excluido Fase 2 - Criterio EC2 (LCA/BCH transversal sem split/CV de ML supervisionado - usar no referencial)]"
qa_score: 9
population_scope: "Educação Básica (Ensino Fundamental Inicial)"
intervention_scope: "Modelagem Analítico-Preditiva / Network Analysis"
outcome_scope: "Predição de Absenteísmo Crônico Escolar"
authors:
  - "Jane SharpeBrendan BuntingCaroline Heary"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "SDQ (20 itens)"
  - "CES-D (8 itens)"
algorithms:
  - "Latent Class Analysis (LCA)"
  - "Regressao Logistica Multinomial (BCH 3-Step)"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/springer_link
  - fenomeno/absenteismo_cronico
---
# S0532: A Latent Class Analysis of Mental Health Symptoms in Primary School Children: Exploring Associations with School Attendance Problems

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0532`
> - **Autores:** Jane Sharpe, Brendan Bunting, Caroline Heary
> - **Ano:** 2023
> - **Veículo (Venue):** *School Mental Health* (vol. 15, pp. 1128-1144)
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1007/s12310-023-09610-0](https://doi.org/10.1007/s12310-023-09610-0)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1007/s12310-023-09610-0)
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC2 (LCA/BCH transversal sem split/CV de ML supervisionado - usar no referencial)]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Although there is a wealth of research addressing the association between mental health and school absenteeism, there are calls for a better understanding of how mental health difficulties might predict SAPs. Using a sample of Irish 9-year-olds (N = 8570) from the Growing Up In Ireland Study (GUI'98), the research used latent class analysis (LCA) to identify combinations of mental health symptoms. Twenty items from the Strengths and Difficulty Questionnaire (SDQ) were used to measure a range of emotional and behavioural difficulties. The analysis yielded four mental health classes - High Risk of Emotional and Behavioural Difficulties (EBD), High Risk of Emotional Difficulties (ED), High Risk of Behavioural Difficulties (BD) and Low Risk of EBD. Children in the high-risk mental health symptomology groups had significantly higher odds of absenteeism compared to the low-risk class and significantly greater odds of experiencing multiple family, school and demographic risk factors.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Ensino Fundamental Inicial - 9 anos)
- **Intervencao/Tecnologia (Intervention Scope):** Modelagem por Analise de Classes Latentes (LCA) + Regressao Logistica Multinomial (abordagem manual BCH 3-step no Mplus)
- **Desfecho (Outcome Scope):** Predicao de Absenteismo Escolar Problematico Emergente (11-20 dias) e Cronico (>20 dias) / SAPs
- **Criterios de Inclusao:** `IC1 (em duvida - LCA estatistico sem ML supervisionado), IC2, IC4`
- **Motivo da Inclusao:**
  > `[EM DUVIDA]` Trata diretamente de [[Absenteismo_Cronico|absenteismo escolar]] e problemas de frequencia escolar (SAPs) na educacao basica (9 anos) associados a fatores socioemocionais e familiares (SDQ, depressao parental CES-D, bullying, relacao professor-aluno). Contudo, emprega Analise de Classes Latentes (LCA) e regressao logistica multinomial auxiliar (BCH) no Mplus 8.7 em dados transversais, sem algoritmos de Machine Learning preditivo ou validacao treino/teste.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0532`
- **Titulo Completo:** A Latent Class Analysis of Mental Health Symptoms in Primary School Children: Exploring Associations with School Attendance Problems
- **Autores:** Jane Sharpe, Brendan Bunting, Caroline Heary
- **Ano de Publicacao:** 2023
- **Tipo de Publicacao:** Artigo de Periodico
- **Nome do Veiculo:** School Mental Health (15:1128-1144)
- **DOI:** [10.1007/s12310-023-09610-0](https://doi.org/10.1007/s12310-023-09610-0)
- **Base de Dados:** Springer Link
- **Pais/Regiao de Realizacao do Estudo:** Irlanda (amostra nacional representativa)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica - Ensino Fundamental Inicial (*Primary School*, criancas de 9 anos)
- **Faixa Etaria / Amostra ($N$):** N = 8.570 criancas irlandesas de 9 anos no resumo (N = 8.568 descritos na secao Participants, sendo 49,8% feminino e 50,2% masculino, selecionadas em 910 escolas nacionais; 13 casos com valores ausentes na LCA; n = 8.553 classificados nas 4 classes latentes; desfecho de dias ausentes disponivel para n = 8.547: <=10 dias n = 7.570, 11-20 dias n = 801, >20 dias n = 176; na secao Limitations citam N = 189 para >20 dias).
- **Publico-alvo Avaliado:** Populacao escolar geral de 9 anos no Ensino Fundamental irlandes, avaliada quanto ao risco de problemas de frequencia escolar (SAPs).
- **Fonte dos Dados / Dataset:** Microdados da Onda 1 (coleta entre agosto de 2007 e maio de 2008) do estudo longitudinal nacional *Growing Up In Ireland* (GUI Cohort '98, Research Microdata File - CSO), com dados reponderados (*reweighted*) para representatividade nacional.

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** *Strengths and Difficulties Questionnaire* (SDQ - 20 itens das 4 subescalas de dificuldades de ajustamento, relato dos pais; subescala prossocial excluida) e *Centre for Epidemiological Studies Depression Scale* (CES-D versao de 8 itens para depressao parental).
- **Natureza da Ferramenta:** Questionarios padronizados de triagem psicossocial e psicopatologica aplicados em inquerito populacional.
- **Forma de Aplicacao:** Multi-informante: relato dos pais (SDQ, CES-D, conflito parental, NSE e dias ausentes da crianca), autorrelato da crianca (bullying, atitude frente a escola e ao professor) e relato do professor (problemas domesticos afetando a participacao escolar).
- **Finalidade:** Triagem inicial de perfis de sintomas emocionais e comportamentais e associacao com niveis de absenteismo escolar.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Analise Estatistica Avancada / Modelagem de Misturas Latentes (*Latent Class Analysis* - LCA) combinada a Regressao Logistica Multinomial (metodo manual BCH de 3 passos para desfechos e covariaveis auxiliares) no software Mplus 8.7. Sem algoritmos de Machine Learning supervisionado.
- **Algoritmos Empregados:** LCA com indicadores binarios, estimacao por Maxima Verossimilhanca (ML / MLR) sob pressuposto MAR, estimador sanduiche para erros padrao corrigidos por cluster escolar (`school ID`) e metodo manual BCH (*Bolck-Croon-Hagenaars*) de 3 etapas.
- **Tarefa do Modelo:** Agrupamento probabilistico latente de perfis de saude mental (4 classes: High Risk EBD [15,3%], High Risk ED [20,9%], High Risk BD [31,1%], Low Risk EBD [32,7%]) e predicao da razao de chances (OR) de absenteismo (>10 dias vs. <=10 dias).
- **Estagio de Deteccao:** Rastreio precoce de vulnerabilidade aos 9 anos de idade (enquadrado no modelo RtI de 3 camadas: satisfatorio <=10 dias, problematico emergente 11-20 dias, cronico >20 dias).

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** 20 itens do SDQ cobrindo Problemas Emocionais (queixas somaticas, preocupacao excessiva, medo, nervosismo, infelicidade), Problemas de Conduta (birras, desobediencia, mentira), Hiperatividade-Desatencao (hiperatividade, desatencao, impulsividade) e Problemas com Pares (brincar sozinho, sofrer bullying, preferir adultos a pares).
- **Variaveis Comportamentais / Historico:** Dias ausentes no ultimo ano letivo relatados pelos pais (<=10 dias, 11-20 dias, >20 dias), vitimizacao por bullying no ultimo ano (Sim/Nao), atitude da crianca frente a escola (*like school*) e relacao com o professor (*like teacher*).
- **Variaveis Familiares / Sociodemograficas:** Sexo da crianca, baixo nivel socioeconomico (dificuldade financeira de "making ends meet"), conflito entre os pais (relato do cuidador principal), depressao parental (CES-D 8 itens, corte >= 7) e problemas em casa afetando a participacao escolar (relato do professor).
- **Variaveis Institucionais / Contextuais:** Efeito de cluster por escola (`school ID`, 910 escolas primarias) e percepcao do ambiente escolar/docente pela crianca.
- **Features Mais Relevantes Identificadas:** Antes da inclusao de covariaveis, pertencer a classe *High Risk of EBD* (OR = 2,433; p < 0,001) e *High Risk of ED* (OR = 2,208; p < 0,001) mais que dobrou a chance de absenteismo >10 dias em comparacao com *Low Risk of EBD*; *High Risk of BD* apresentou OR = 1,597 (p < 0,001). Apos ajuste pelas covariaveis, os efeitos mantiveram-se significativos (EBD OR = 1,916; ED OR = 1,842; BD OR = 1,386). O efeito de bullying, depressao parental (OR = 4,881 para EBD; 2,488 para ED), aversao escolar/docente e problemas em casa relatados pelo professor (OR = 4,949 para EBD) foi mediado pelas classes de saude mental, enquanto baixo NSE teve efeito direto em EBD (OR = 2,748) e BD (OR = 2,107) e conflito parental teve efeito direto em ED (OR = 2,101) e Low Risk (OR = 2,234).

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** Propriedades previas do SDQ citadas para o GUI Wave 1 (CFA: chi2 = 4403,47, df = 179, CFI = 0,853, TLI = 0,916, RMSEA = 0,053; cargas medias de 0,59 a 0,71; alfa medio historico = 0,73) e CES-D 8 itens (alfa de Cronbach = 0,87).
- **Metricas Computacionais (ML):** N/A para ML supervisionado. Metricas do modelo LCA de 4 classes: Log-Likelihood = -87.566,067; AIC = 175.298,633; BIC = 175.883,628; SSABIC = 175.619,869; LMR-LRT significativo (p < 0,0000; 5a classe nao significativa p = 0,0827); Entropia = 0,717; probabilidades diagonais > 0,80 (Classes 1, 3 e 4) e 0,771 (Classe 2); Odds Ratios e IC 95% nas regressoes BCH.
- **Estrategia de Validacao:** Comparacao estatistica de modelos LCA de 2 a 5 classes (BIC, AIC, LMR-LRT, entropia, probabilidades diagonais e interpretabilidade teorica); ponderacao amostral complexa e correcao de erros padrao por cluster escolar. Sem split treino/teste ou validacao cruzada.
- **Desafios Metodologicos Relatados:** 17% dos casos (n = 1.452) com dados ausentes em alguma covariavel (tratados por maxima verossimilhanca sob MAR); excesso de dados ausentes nos registros dos professores sobre faltas (obrigando uso do relato parental); baixa contagem na categoria >20 dias (n = 176 na secao Method / N = 189 citada em Limitations, exigindo agrupar 11-20 e >20 dias para >10 dias nos testes de OR); perda de granularidade ao dicotomizar o SDQ.
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao pelo *Health Research Board's Research Ethics Committee* na Irlanda; uso de microdados anonimizados (RMF/CSO); discussao sobre como sintomas emocionais puros frequentemente passam despercebidos pelos professores.
- **Limitacoes Declaradas:** Delineamento transversal (impede inferencia causal ou longitudinal); dados antigos (coleta 2007/2008); subnotificacao provavel de faltas pelo relato parental (~2% de >20 dias vs. 10,9%-12% nos dados escolares nacionais da epoca); subjetividade do relato docente sobre problemas domesticos; dicotomizacao dos itens do SDQ inflando classes de alto risco; ausencia de analise de fatores protetores nas criancas de alto risco que faltam <=10 dias.
- **Direcoes Futuras:** Analisar a onda seguinte do GUI (aos 13 anos) para testar validade preditiva longitudinal das classes e trajetorias dos 9 aos 13 anos; investigar fatores protetores escolares e familiares no modelo RtI.

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** 20 itens das 4 subescalas de dificuldades do SDQ (*Emotional Problems*, *Conduct Problems*, *Hyperactivity-Inattention*, *Peer Problems*), preenchidos pelos pais sobre criancas de 9 anos em escala original de 3 pontos (*not true*, *somewhat true*, *certainly true*) e dicotomizados em 0 (*not true*) vs. 1 (*somewhat/certainly true*, com 5 itens invertidos); somados a CES-D de 8 itens para depressao parental (corte >= 7), itens binarios de autorrelato infantil (bullying no ultimo ano, gostar da escola, gostar do professor), relato parental de conflito e dificuldade financeira, e relato docente de problemas domesticos; coleta unica na Onda 1 do GUI '98 (2007-2008).
- **Inventario completo de variaveis e justificativa de escolha:** (1) 20 itens do SDQ (escolhidos para capturar sintomas emocionais e comportamentais especificos sem recorrer a escores somados arbitrarios; subescala prossocial excluida por falta de associacao previa com SAPs); (2) Dias ausentes no ultimo ano letivo categorizados em <=10, 11-20 e >20 dias (alinhado ao modelo RtI de 3 camadas e ao marco irlandes TUSLA); (3) Sexo e baixo NSE (*making ends meet*); (4) Fatores escolares: bullying, relacao com professor e atitude diante da escola (escolhidos por representarem microssistemas escolares ligados a evitacao e *truancy*); (5) Fatores familiares: conflito parental, depressao parental (CES-D) e problemas domesticos reportados pelo professor (selecionados por influencia proximal no desenvolvimento infantil).
- **Fundamentacao teorica do identificador:** Baseia-se no modelo bioecologico de Bronfenbrenner e Morris (2006) aplicado aos problemas de frequencia escolar (Kearney, 2021; Melvin et al., 2019), na diferenciacao tipologica entre evitacao escolar (*school avoidance*, ligada a sintomas emocionais) e *truancy* (ligada a dificuldades comportamentais) segundo Heyne et al. (2019), no modelo funcional comorbido de Kearney e Silverman (1993) e na estrutura multitarefa *Response to Intervention* (RtI, Kearney & Graczyk, 2014, 2020).
- **Restricoes de recursos e limitacoes:** Embora o SDQ e itens curtos de triagem sejam instrumentos de baixo custo aplicaveis na rede publica, o estudo aponta limitacoes criticas para uso pratico: (a) dependencia de software estatistico especializado (Mplus) e ponderacao complexa; (b) criancas com sintomas puramente emocionais (*High Risk of ED*) nao foram significativamente identificadas pelos professores como tendo problemas domesticos afetando a escola, revelando cegueira de triagem exclusivamente docente; (c) ausencia de dados administrativos digitais de frequencia completos nas escolas (excesso de missing docente) e subestimacao por relato parental; (d) desenho transversal sem validacao preditiva longitudinal ou fora da amostra.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente 3 questoes de pesquisa sobre classes latentes de saude mental aos 9 anos, variacao no absenteismo e fatores de risco sistemicos. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha amostra GUI '98 (N = 8.568 / 910 escolas), dicotomizacao do SDQ, abordagem BCH manual em 3 passos no Mplus 8.7, ponderacao e tratamento de missing (MAR). |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Reporta indices completos da LCA (LL, AIC, BIC, SSABIC, LMR-LRT, Entropia = 0,717), ORs e ICs 95%, mas nao possui validacao preditiva fora da amostra (CV ou split treino/teste). |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Explora perfis emocionais, comportamentais e comorbidos do SDQ, depressao parental (CES-D), conflito familiar, bullying e vinculo escolar/docente. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Dedica secao especifica a transversalidade, subnotificacao parental, antiguidade dos dados (2007/2008), dicotomizacao do SDQ e baixa contagem em >20 faltas. |
| **TOTAL** | **Pontuacao de Rigor** | **9 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- **[EM DUVIDA]:** O artigo investiga diretamente o [[Absenteismo_Cronico|absenteismo escolar]] na educacao basica (9 anos) em funcao de sintomas de saude mental (SDQ) e fatores socioemocionais/familiares (CES-D, bullying, clima escolar). Porem, a tecnica analitica e estatistica baseada em Analise de Classes Latentes (LCA) + regressao logistica multinomial (BCH 3-step) em Mplus sobre dados transversais, sem algoritmos de Machine Learning supervisionado nem validacao preditiva fora da amostra. Submetido a decisao do pesquisador sobre permanencia como estudo primario ou transferencia para o referencial teorico.
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
