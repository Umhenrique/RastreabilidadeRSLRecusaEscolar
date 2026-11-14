---
id: S0325
study_id: S0325
title: "Re-envisioning a K-12 Early Warning System with School Climate Factors"
year: 2022
database: "ACM DL"
venue: "Proceedings of the Ninth ACM Conference on Learning @ Scale"
doi: "10.1145/3491140.3528670"
url: "https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3491140.3528670"
status: "[Excluido Fase 2 - Criterio EC2 (WIP sem ML implementado)]"
qa_score: 8
population_scope: "Ensino Básico (K-12)"
intervention_scope: "Machine Learning em Early Warning Systems"
outcome_scope: "Assiduidade Escolar + Aprendizagem Socioemocional"
authors:
  - "Mengchen Su"
  - "Lukas A. Olson"
  - "Daniel C. Jarratt"
  - "Sashank Varma"
  - "Joseph A. Konstan"
  - "Rebecca J. L. Keller"
  - "Bodong Chen"
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
---
# S0325: Re-envisioning a K-12 Early Warning System with School Climate Factors

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0325`
> - **Autores:** Mengchen Su, Lukas A. Olson, Daniel C. Jarratt, Sashank Varma, Joseph A. Konstan, Rebecca J. L. Keller, Bodong Chen
> - **Ano:** 2022
> - **Veículo (Venue):** *Proceedings of the Ninth ACM Conference on Learning @ Scale*
> - **Base de Origem:** `ACM DL` (Bases: `['ACM DL']`)
> - **DOI:** [10.1145/3491140.3528670](https://doi.org/10.1145/3491140.3528670)
> - **URL:** [Link da Publicação](https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3491140.3528670)
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC2 (WIP sem ML implementado)]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> The Every Student Succeeds Act (ESSA) prescribes holistic measures of schools for student success and well-being. However, many early warning systems rely exclusively on the "Attendance, Behavior, Course" (ABC) taxonomy, which misses potentially crucial determinants such as school climate and students' socioemotional learning. We report early findings from a larger project that aims to apply machine learning methods to improve an early warning system by incorporating factors related to school climate and socioemotional learning. These preliminary analyses suggest that a culturally inclusive, socially supportive, and emotionally and physically safe school climate is related to academic success and fewer engagement/behavior problems at the school level. They suggest the promise of integrating these features into early warning systems to help schools change their practices to better support student well-being.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Ensino Básico (K-12)
- **Intervencao/Tecnologia (Intervention Scope):** Machine Learning em Early Warning Systems
- **Desfecho (Outcome Scope):** Assiduidade Escolar + Aprendizagem Socioemocional
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Aplica Machine Learning em Early Warning Systems no Ensino Básico (K-12) integrando diretamente assiduidade escolar (Attendance) com fatores socioemocionais (Socioemotional Learning - SEL) e clima escolar para suporte ao bem-estar do aluno. Responde diretamente às RQ2 e RQ3.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0325`
- **Titulo Completo:** Re-envisioning a K-12 Early Warning System with School Climate Factors
- **Autores:** Mengchen Su, Lukas A. Olson, Daniel C. Jarratt, Sashank Varma, Joseph A. Konstan, Rebecca J. L. Keller, Bodong Chen
- **Ano de Publicacao:** 2022
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Proceedings of the Ninth ACM Conference on Learning @ Scale
- **DOI:** [10.1145/3491140.3528670](https://doi.org/10.1145/3491140.3528670)
- **Base de Dados:** ACM DL
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (Estado de Nevada)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Basico (K-12)
- **Faixa Etaria / Amostra ($N$):** Amostra combinada final: ~60.000 estudantes de 277 escolas (2019) e ~75.000 estudantes de 261 escolas (2021) em 17 distritos de Nevada (base SIS estadual ~500.000 alunos K-12; survey original: 62.000 alunos/738 escolas em 2019 e 48.900 alunos/754 escolas em 2021)
- **Publico-alvo Avaliado:** Estudantes K-12 de escolas publicas (integracao de clima escolar e aprendizagem socioemocional [SEL] em Early Warning System)
- **Fonte dos Dados / Dataset:** Nevada School Climate / Social Emotional Learning Survey (NV-SCSEL, AIR / Nevada Department of Education) integrado ao Student Information System (SIS) da Infinite Campus

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** Nevada School Climate / Social Emotional Learning Survey (NV-SCSEL), baseado no ED School Climate Survey (U.S. Department of Education)
- **Natureza da Ferramenta:** Questionario web validado de clima escolar e aprendizagem socioemocional (escores de 100 a 500 em 4 dominios: CLC, REL, EMO, PSAF)
- **Forma de Aplicacao:** Autorrelato dos estudantes via web, agregado em nivel escolar
- **Finalidade:** Mensuracao de percepcoes de clima escolar e SEL para melhoria institucional e integracao em EWS

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Analise Estatistica (Regressao Linear Multipla no nivel escolar para os resultados preliminares) como etapa inicial de projeto em andamento (*Work in Progress*) para integrar clima escolar/SEL ao [[Early_Warning_Systems]] da Infinite Campus com Machine Learning (Gradient-Boosted Decision Trees e SHAP)
- **Algoritmos Empregados:** Regressao Linear Multipla (executada); [[Early_Warning_Systems]], Gradient-Boosted Decision Trees e [[Explicabilidade_XAI]] (SHAP) previstos para a etapa individual
- **Tarefa do Modelo:** Regressao no nivel escolar para explicar frequencia, atrasos, comportamento e GPA; classificacao binaria prevista para desfechos negativos de matricula (evasao, expulsao, retencao)
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (expansao do modelo ABC tradicional com clima escolar e SEL)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Aprendizagem Socioemocional (SEL), Seguranca Emocional (`EMO`), Relacionamentos (`REL`), Competencia Cultural e Linguistica (`CLC`) e Seguranca Fisica (`PSAF`)
- **Variaveis Comportamentais / Historico:** % de estudantes com faltas injustificadas ou desconhecidas (`pct unexcusedunknown`), % com atrasos (`pct tardy`), % com resolucoes comportamentais (`pct behaviorRes`), GPA acumulado medio (`avg cumGPA`)
- **Variaveis Familiares / Sociodemograficas:** % de estudantes do sexo masculino, % elegivel para almoco gratuito ou reduzido (proxy socioeconomico), % com ingles como lingua primaria
- **Variaveis Institucionais / Contextuais:** Clima escolar multidimensional agregado por escola (CLC, REL, EMO, PSAF)
- **Features Mais Relevantes Identificadas:** Todos os 4 dominios de clima escolar foram preditores significativos de atrasos e resolucoes comportamentais em 2019 e 2021 ($R^2_{change}$ entre 5% e 15% para atrasos). `Physical Safety (PSAF)` foi o preditor mais consistente de faltas injustificadas e GPA nos dois anos; `Emotional Safety (EMO)` apresentou $\beta = -0,11^{***}$ ($R^2_{change} = 0,15^{***}$) para atrasos e $\beta = 0,13^{***}$ para GPA em 2021

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A (escala validada previamente pelo U.S. Dept. of Education/AIR, sem reporte de Alfa de Cronbach na amostra deste artigo)
- **Metricas Computacionais (ML):** Reporta coeficientes padronizados ($\beta$), $p$-valores e $R^2_{change}$ (0,02 a 0,15) das regressoes lineares escolares. Metricas de ML (Precision, Recall, AUC-ROC, SHAP) constam apenas no protocolo em andamento (Secao 2.3.2), ainda sem resultados publicados neste *Work in Progress*
- **Estrategia de Validacao:** Modelos transversais independentes para 2019 (N=277 escolas) e 2021 (N=261 escolas) apos *listwise deletion*; protocolo futuro preve holdout aleatorio de 20% para modelos de ML
- **Desafios Metodologicos Relatados:** Grande perda amostral por dados faltantes ao cruzar o survey NV-SCSEL com o SIS; possivel interferencia da pandemia de COVID-19 nos padroes de 2021; analise preliminar restrita ao nivel escolar agregado
- **Aspectos Eticos e Transparencia (XAI):** Enfase em equidade racial e atendimento integral ao estudante ("whole child"); preve aplicacao de valores SHAP ([[Explicabilidade_XAI]]) na etapa de ML
- **Limitacoes Declaradas:** Elevada proporcao de dados faltantes apos juncao das bases; apenas um ano pandemico disponivel (2021); risco de baixa validade externa/generalizacao estadual; achados atuais limitados ao nivel da escola e nao ao nivel individual
- **Direcoes Futuras:** Integrar os fatores de clima escolar e SEL no EWS individual em producao da Infinite Campus com Gradient-Boosted Decision Trees e SHAP

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente as duas questoes de pesquisa para integrar clima escolar e SEL alem da taxonomia ABC em um EWS K-12. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 1 | Descreve fontes, variaveis e equacao da regressao escolar (2019 e 2021), mas por ser *Work in Progress*, o pipeline de ML (GBDT/SHAP) ainda esta em execucao. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Apresenta $\beta$, $p$-valores e $R^2_{change}$ para os modelos lineares escolares, mas ainda nao reporta metricas de ML (AUC, Precision, Recall) no nivel individual. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Aborda diretamente aprendizagem socioemocional (SEL), seguranca emocional, seguranca fisica, relacionamentos e competencia cultural-linguistica associados a faltas e comportamento. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute explicitamente perda amostral por dados faltantes, impacto da pandemia de COVID-19, ameacas a validade externa e restricao ao nivel agregado escolar. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **8 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
