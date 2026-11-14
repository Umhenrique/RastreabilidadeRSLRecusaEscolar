---
id: S0500
study_id: S0500
title: "How is loneliness orientation implicated in the relationship between sleep problems, loneliness intensity, and school refusal in adolescents?"
year: 2025
database: "Springer Link"
venue: "Sleep and Biological Rhythms"
doi: "10.1007/s41105-025-00586-9"
url: "https://link.springer.com/article/10.1007/s41105-025-00586-9"
status: "[Excluido Fase 2 - Criterio EC2 (Psicometrico/estatistico sem IA/ML preditivo - usar no referencial)]"
qa_score: 10
population_scope: "Educação Básica (Adolescentes)"
intervention_scope: "Instrumentos Diagnósticos e Escalas Psicométricas"
outcome_scope: "Diagnóstico e Rastreio de Recusa Escolar (SRAS/SCREEN/EBSA)"
authors:
  - "Isa OkajimaSetoka Hiruma"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "FSAS"
  - "LOT"
  - "TILS"
  - "AIS"
  - "SDI"
  - "CIRENS"
algorithms:
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/springer_link
  - fenomeno/recusa_escolar
---
# S0500: How is loneliness orientation implicated in the relationship between sleep problems, loneliness intensity, and school refusal in adolescents?

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0500`
> - **Autores:** Isa OkajimaSetoka Hiruma
> - **Ano:** 2025
> - **Veículo (Venue):** *Sleep and Biological Rhythms*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1007/s41105-025-00586-9](https://doi.org/10.1007/s41105-025-00586-9)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1007/s41105-025-00586-9)
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC2 (Psicometrico/estatistico sem IA/ML preditivo - usar no referencial)]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Resumo não disponível na base de origem.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Adolescentes)
- **Intervencao/Tecnologia (Intervention Scope):** Instrumentos Diagnósticos e Escalas Psicométricas
- **Desfecho (Outcome Scope):** Diagnóstico e Rastreio de Recusa Escolar (SRAS/SCREEN/EBSA)
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Avalia, valida ou investiga instrumentos diagnósticos, escalas psicométricas ou ferramentas de triagem clínica/educacional focadas especificamente em recusa escolar e problemas de assiduidade em crianças/adolescentes (Responde à RQ1 e RQ3).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0500`
- **Titulo Completo:** How is loneliness orientation implicated in the relationship between sleep problems, loneliness intensity, and school refusal in adolescents?
- **Autores:** Isa OkajimaSetoka Hiruma
- **Ano de Publicacao:** 2025
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Sleep and Biological Rhythms
- **DOI:** [10.1007/s41105-025-00586-9](https://doi.org/10.1007/s41105-025-00586-9)
- **Base de Dados:** Springer Link
- **Pais/Regiao de Realizacao do Estudo:** Japao (Toquio)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Medio (Senior High School - escolas publicas e privadas)
- **Faixa Etaria / Amostra ($N$):** Recrutados N = 168 estudantes; amostra final analisada N = 128 estudantes (52 meninos, 70 meninas [6 sem genero reportado na descr.]; idade media = 16,55 +- 0,64 anos; coleta entre nov-dez de 2023)
- **Publico-alvo Avaliado:** Adolescentes do ensino medio (relacao entre problemas de sono, intensidade/orientacao da solidao, sentimentos de recusa escolar e faltas)
- **Fonte dos Dados / Dataset:** Questionario presencial aplicado a estudantes de escolas publicas e privadas de Toquio (dados abertos disponiveis no Zenodo)

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** `Feeling of School-Avoidance Scale (FSAS)` (6 itens sobre aversao/evitacao escolar), `Loneliness Orientation Test (LOT)` (7 pares semanticos de -3 a +3, desenvolvido no estudo), `Three-Item Loneliness Scale (TILS)`, `Athens Insomnia Scale (AIS)` (8 itens, corte >=6), `Sleep Debt Index (SDI)` e `Circadian Energy Scale (CIRENS)` (2 itens)
- **Natureza da Ferramenta:** Bateria de escalas psicometricas tradicionais de autorrelato + registro de numero de dias ausentes desde abril de 2023
- **Forma de Aplicacao:** Autorrelato do aluno (levantamento presencial)
- **Finalidade:** Triagem e avaliacao psicometrica de sentimentos de recusa escolar, solidao (intensidade e orientacao) e disturbios do sono

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Analise Estatistica Avancada e Psicometria (Analise Fatorial Exploratoria [EFA], Analise Fatorial Confirmatoria [CFA], Modelos Lineares Generalizados [GLM Gamma e Poisson] e Clustering Hierarquico nao supervisionado pelo metodo de Ward). Nao emprega Machine Learning supervisionado preditivo
- **Algoritmos Empregados:** EFA, CFA, Modelos Lineares Generalizados (GLM Gamma com log-link e Poisson com log-link), Clustering Hierarquico (Ward)
- **Tarefa do Modelo:** Validacao fatorial (EFA/CFA), regressao explicativa (GLM para TILS, FSAS e numero de faltas) e agrupamento (clustering de perfis de solidao: LN, nLP, LP)
- **Estagio de Deteccao:** Triagem preventiva e analise de mecanismos etiologicos (sentimentos de evitacao escolar `FSAS` como antecedente do absenteismo e [[Recusa_Escolar]])

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Intensidade da solidao (`TILS`), orientacao a solidao (`LOT` - positiva vs. negativa), sentimentos de recusa/evitacao escolar (`FSAS`), sintomas de insonia (`AIS`), divida de sono (`SDI`), cronotipo (`CIRENS`)
- **Variaveis Comportamentais / Historico:** Numero de dias de ausencia escolar entre abril de 2023 e a data da pesquisa (media = 3,26 +- 0,48 dias)
- **Variaveis Familiares / Sociodemograficas:** Idade (16,55 +- 0,64 anos), sexo, rede escolar (publica e privada em Toquio)
- **Variaveis Institucionais / Contextuais:** Criterio institucional japones de recusa escolar (>=30 dias de ausencia anual nao causados por doenca ou dificuldade financeira)
- **Features Mais Relevantes Identificadas:** No GLM: intensidade da solidao (`TILS`, $\beta=0,13, p<0,001$) foi o principal preditor de sentimentos de recusa escolar (`FSAS`, $R^2=0,29$), junto a tendencia de insonia (`AIS`, $\beta=0,05, p=0,07$). Para o numero de faltas ($R^2=0,38$), os preditores significativos foram `FSAS` ($\beta=0,32, p<0,001$) e cronotipo vespertino (`CIRENS`, $\beta=0,13, p<0,05$). Nos clusters, o grupo com solidao e orientacao negativa (`LN`, 28%) apresentou maior divida de sono e vespertinidade que o grupo com orientacao positiva (`LP`, 22%)

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** `LOT`: Alfa de Cronbach = 0,94; Omega de McDonald = 0,94; CFA com bom ajuste ($\chi^2_{14}=16,58, p=0,28$, CFI = 0,99, RMSEA = 0,05); cargas fatoriais de 0,76 a 0,85 (64% de variancia explicada)
- **Metricas Computacionais (ML):** N/A (estudo estatistico/psicometrico; reporta Nagelkerke's $R^2$ = 0,12 [TILS], 0,29 [FSAS] e 0,38 [faltas], alem de Hedges' $g$ entre clusters)
- **Estrategia de Validacao:** Calculo previo de poder amostral ($1-\beta=0,80$, n minimo = 110); analise paralela + EFA/CFA para o LOT; validacao do numero de clusters via *silhouette*, *gap statistic* e `NbClust`
- **Desafios Metodologicos Relatados:** Delineamento transversal (sem inferencia causal), vies de selecao por incluir apenas alunos frequentes, baixa variancia explicada (~10%) para intensidade da solidao
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao do Comite de Etica da Tokyo Kasei University (Ita-E2023-16), consentimento informado (Declaracao de Helsinque) e disponibilizacao aberta dos dados no Zenodo
- **Limitacoes Declaradas:** Amostra relativamente pequena (N=128 analisados); amostra limitada ao ensino medio; inclusao apenas de estudantes que conseguiam comparecer a escola (excluindo casos ja afastados); impossibilidade de estabelecer causalidade; ausencia de validacao concorrente do LOT com construtos como resiliencia
- **Direcoes Futuras:** Estudar amostras do ensino fundamental II a universidade, incluir estudantes atualmente afastados da escola, e investigar a relacao da orientacao a solidao com resiliencia, autocrescimento e bem-estar

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente os tres objetivos: desenvolver o LOT, analisar o impacto diferencial de problemas de sono na solidao/recusa escolar/faltas e comparar perfis combinados via clusters. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha calculo amostral, criterios de inclusao (SDI >= 0), 6 instrumentos, pacotes R utilizados, EFA/CFA, GLMs (Gamma/Poisson) e clustering de Ward. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta $\alpha=0,94$, $\omega=0,94$, indices de ajuste da CFA (CFI=0,99, RMSEA=0,05), $R^2$ de Nagelkerke, ICs de 95% e tamanhos de efeito (Hedges' $g$). |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Investiga aprofundadamente solidao (intensidade e orientacao cognitiva), insonia, divida de sono, cronotipo e sentimentos de evitacao escolar (FSAS). |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute explicitamente tamanho amostral, restricao ao ensino medio, vies de amostragem (apenas alunos frequentes), ausencia de causalidade e falta de validade concorrente do LOT. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **10 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
