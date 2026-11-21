---
id: S0659
study_id: S0659
title: "School dropout prediction and feature importance exploration in Malawi using household panel data: machine learning approach"
year: 2022
database: "Springer Link"
venue: "Journal of Computational Social Science"
doi: "10.1007/s42001-022-00195-3"
url: "https://link.springer.com/article/10.1007/s42001-022-00195-3"
status: "[Excluido Fase 2 - Criterio EC2 (Evasao puramente socioeconomica/estrutural sem fatores socioemocionais ou recusa escolar)]"
qa_score: 7
population_scope: "Educação Básica (K-12)"
intervention_scope: "Modelos de Machine Learning / IA e Análise Preditiva"
outcome_scope: "Predição de Risco de Abandono Escolar no K-12"
authors:
  - "Hazal Colak OzÇiçek GüvenGonzalo Nápoles"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
  - "[[Random_Forest]]"
  - "LASSO"
  - "Ridge"
  - "Multilayer Neural Network (MNN)"
  - "[[Regressao_Logistica]]"
  - "[[Explicabilidade_XAI]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/springer_link
  - fenomeno/absenteismo_cronico
---
# S0659: School dropout prediction and feature importance exploration in Malawi using household panel data: machine learning approach

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0659`
> - **Autores:** Hazal Colak Oz, Cicek Guven, Gonzalo Napoles
> - **Ano:** 2022 (online dez/2022; volume 2023, vol. 6, pp. 245-287)
> - **Veículo (Venue):** *Journal of Computational Social Science*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1007/s42001-022-00195-3](https://doi.org/10.1007/s42001-022-00195-3)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1007/s42001-022-00195-3)
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC2 (Evasao puramente socioeconomica/estrutural sem fatores socioemocionais ou recusa escolar)]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Designing early warning systems through machine learning (ML) models to identify students at risk of dropout can improve targeting mechanisms and lead to efficient social policy interventions in education. This study suggests using already collected household panel data to predict the probability of school dropout and explore feature importance for primary school children in Malawi through ML models. A rich set of variables is obtained from household data and used to build Random Forest (RF), least absolute shrinkage and selection operator (LASSO), Ridge and multilayer neural network (MNN) models, embedding sample weights into the cost function. LASSO and MNN models trained with sample weights achieve recall rates of 80.6% and 78.8%, and KernelSHAP reveals socio-economic characteristics such as working in household farming and father's education level as the most important features.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Ensino Fundamental - series 1 a 8 no Malawi)
- **Intervencao/Tecnologia (Intervention Scope):** Machine Learning Supervisionado (RF, LASSO, Ridge, MNN, Regressao Logistica) + KernelSHAP
- **Desfecho (Outcome Scope):** Predicao de Evasao Escolar (*School Dropout* em t+3 anos)
- **Criterios de Inclusao:** `Nao atende IC1 atualizado / Enquadrado em EC2`
- **Motivo da Exclusao:**
  > Excluido na Fase 2 pelo Criterio EC2: Embora aplique modelos concretos de ML e XAI (SHAP) no ensino basico, o estudo foca exclusivamente na evasao escolar (*dropout*) explicada por determinantes estritamente socioeconomicos, agricolas, nutricionais, trabalho infantil e infraestrutura comunitaria no Malawi, sem incluir qualquer variavel socioemocional, psicologica ou ligada a recusa escolar.

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0659`
- **Titulo Completo:** School dropout prediction and feature importance exploration in Malawi using household panel data: machine learning approach
- **Autores:** Hazal Colak Oz, Cicek Guven, Gonzalo Napoles
- **Ano de Publicacao:** 2022 (publicado online em 13/12/2022; impresso em 2023)
- **Tipo de Publicacao:** Artigo de Periodico
- **Nome do Veiculo:** Journal of Computational Social Science (6:245-287)
- **DOI:** [10.1007/s42001-022-00195-3](https://doi.org/10.1007/s42001-022-00195-3)
- **Base de Dados:** Springer Link
- **Pais/Regiao de Realizacao do Estudo:** Malawi (Africa Subsaariana - abrangencia nacional)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica - Ensino Fundamental (*Primary school*, series 1 a 8)
- **Faixa Etaria / Amostra ($N$):** Estudantes que frequentavam o ensino primario no round de 2016 do IHPS e participaram do round de 2019 (IHPS 2016: 12.266 individuos em 3.481 domicilios; taxa de retencao individual de 85,7% entre 2016 e 2019; 16,3% dos estudantes primarios evadiram ate 2019; split 70% treino / 30% teste).
- **Publico-alvo Avaliado:** Criancas e jovens matriculados no ensino primario no Malawi com risco de evasao em 3 anos (t+3).
- **Fonte dos Dados / Dataset:** *Integrated Household Panel Survey* (IHPS, rounds 2016 e 2019) coletado pelo *Malawi National Statistics Office* em parceria com o Banco Mundial (LSMS-ISA).

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** N/A (nao utiliza escalas psicometricas; emprega apenas modulos socioeconomicos do IHPS e o indice composto *Food Consumption Score* - FCS do Programa Mundial de Alimentos).
- **Natureza da Ferramenta:** N/A (questionarios censitarios domiciliares e comunitarios).
- **Forma de Aplicacao:** Entrevistas domiciliares e comunitarias aplicadas por recenseadores oficiais (relato do estudante ou responsavel domiciliar).
- **Finalidade:** Mapeamento socioeconomico para predicao de evasao escolar por politicas publicas.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** [[Machine_Learning]] Supervisionado, Deep Learning tabular (MNN), [[Early_Warning_Systems]] baseados em pesquisas domiciliares e [[Explicabilidade_XAI]] via KernelSHAP.
- **Algoritmos Empregados:** [[Random_Forest]] (RF), Regressao Logistica com regularizacao L1 (LASSO) e L2 (Ridge), Rede Neural Multicamadas (MNN - 2 camadas ocultas de 384 e 128 neuronios com dropout 0,5 em Keras/TensorFlow) e [[Regressao_Logistica]] sem regularizacao (baseline). Incorporacao de pesos amostrais (*sample weights*) e pesos de classe inversamente proporcionais na funcao de custo (entropia cruzada binaria e ganho de informacao Gini).
- **Tarefa do Modelo:** Classificacao binaria de evasao em t+3 (`Y = 1` se nao frequentou o ano anterior e nao frequenta/planeja frequentar em 2019; `Y = 0` caso contrario) usando features de 2016.
- **Estagio de Deteccao:** Alerta precoce prospectivo (horizonte de 3 anos) baseado em fatores de status socioeconomico, sem depender de sistemas administrativos escolares.

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** N/A (nenhuma variavel de ansiedade, depressao, estresse, regulacao emocional ou recusa escolar foi modelada; o modulo T de bem-estar subjetivo do IHPS refere-se a pobreza/consumo material, nao a escalas psicometricas).
- **Variaveis Comportamentais / Historico:** Serie escolar cursada em 2016 (*latest education degree*), participacao em trabalho agricola domiciliar (*household farming*) e trabalho casual/precario (*ganyu*), uso de computador e alfabetizacao basica.
- **Variaveis Familiares / Sociodemograficas:** Escolaridade e ocupacao da mae e do pai (ou adulto mais velho/falecido), gasto domiciliar ajustado pela inflacao e escala de equivalencia da OCDE, *Food Consumption Score* (FCS), indice de bens duraveis derivado por PCA, seguranca alimentar, choques e estrategias de enfrentamento.
- **Variaveis Institucionais / Contextuais:** Distancia ao mercado mais proximo e a clinica de saude, disponibilidade de escola primaria eletrificada na localidade, tipo de estradas na comunidade, religiao e tipos de casamento predominantes na comunidade.
- **Features Mais Relevantes Identificadas:** Via KernelSHAP no LASSO com pesos amostrais: trabalho infantil na agricultura familiar (*household farming*), trabalho casual *ganyu*, menor escore de consumo alimentar (FCS), ausencia de certificado educacional dos pais (MSCE), ocupacao paterna (*ganyu* vs. negocio agricola) e serie escolar mais avancada em 2016. Na MNN destacaram-se tambem distancia a mercados/clinicas e eletrificacao da escola primaria.

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A.
- **Metricas Computacionais (ML):** Recall (metrica principal), Precisao, F1-Score e Area Under Precision-Recall Curve (AUPR). Com pesos amostrais no conjunto de teste: LASSO (Recall = 0,806; Prec = 0,317; F1 = 0,455; AUPR = 0,365; 37 features ativas), MNN (Recall = 0,788; Prec = 0,355; F1 = 0,489; AUPR = 0,439), Ridge (Recall = 0,772; Prec = 0,316; F1 = 0,448; AUPR = 0,401), RF (Recall = 0,734; Prec = 0,315; F1 = 0,441; AUPR = 0,376) vs. Baseline LR (Recall = 0,248; Prec = 0,441; F1 = 0,318; AUPR = 0,394).
- **Estrategia de Validacao:** Split estratificado 70/30 treino/teste; grid-search com validacao cruzada 5-fold no treino otimizando F1-Score; avaliacao final sobre amostras ponderadas no conjunto de teste.
- **Desafios Metodologicos Relatados:** Desbalanceamento de classes (16,3% evasao vs. 83,7% permanencia), alta multicolinearidade inicial (71 de 176 features removidas por VIF >= 10), baixa precisao relativa (~31,5%-35,5%, ~33%-35% de falsos positivos), custo computacional do KernelSHAP (executado em VM Azure) e estrutura hierarquica aninhada nao modelada por ML multinivel.
- **Aspectos Eticos e Transparencia (XAI):** Alerta etico explicito contra o uso de variaveis sensiveis como religiao e tipo de casamento para rotular ou discriminar grupos de criancas na pratica; transparencia via KernelSHAP e preferencia pela interpretabilidade e parcimonia do LASSO (37 variaveis).
- **Limitacoes Declaradas:** Achados sobre ganho de pesos amostrais restritos ao contexto do IHPS no Malawi; valores SHAP nao implicam causalidade; ausencia de modelagem multinivel para capturar efeitos de cluster domiciliar e comunitario; inexistencia de variaveis escolares administrativas (notas/faltas) ou psicologicas.
- **Direcoes Futuras:** Testar formalmente o impacto de pesos amostrais em diferentes paises/datasets e integrar modelagem multinivel com algoritmos de Machine Learning.

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** N/A (o estudo nao mede ansiedade, depressao ou sofrimento psiquico; utiliza apenas questionarios domiciliares e comunitarios do IHPS coletados em 2016 e 2019 com entrevistas presenciais sobre renda, consumo alimentar, trabalho, bens e infraestrutura).
- **Inventario completo de variaveis e justificativa de escolha:** 176 variaveis iniciais (reduzidas por VIF < 10 para 105 dummies / 79 variaveis principais) extraidas de 25 modulos domiciliares e 12 modulos comunitarios do IHPS: trabalho infantil agricola e *ganyu*, *Food Consumption Score* (FCS), gasto domiciliar equivalente (OCDE), indice PCA de bens duraveis, escolaridade/ocupacao parental, serie escolar em 2016, infraestrutura comunitaria (eletrificacao escolar, distancia a clinica/mercado, estradas), religiao e casamento comunitario. Justificativa: em paises de baixa renda com sistemas escolares precarizados em dados, pesquisas domiciliares nacionais fornecem preditores estruturais ja coletados sem depender de bases administrativas escolares.
- **Fundamentacao teorica do identificador:** Enquadramento economico-social de pobreza intergeracional, custo de oportunidade do trabalho infantil (Freeman & Simonsen, 2015: *status risk factors* vs. *alterable risk factors*; Khan et al., 2021) e teoria de aprendizagem ponderada por funcao de custo (Hashemi & Karimi, 2018) e valores de Shapley da teoria dos jogos (Lundberg & Lee, 2017).
- **Restricoes de recursos e limitacoes:** Desenvolvido especificamente para contextos de extrema escassez de dados e restricao orcamentaria (Malawi: 70,3% abaixo da linha da pobreza), propondo substituir infraestrutura escolar cara por questionario curto de 37 variaveis derivadas do LASSO; contudo, o treinamento e o calculo de KernelSHAP exigiram computacao em nuvem (Microsoft Azure Esv3), o modelo gera ~33%-35% de falsos positivos (precisao ~0,32-0,36) e nao capta fatores emocionais ou absenteismo previo.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente 3 objetivos: comparar 4 modelos de ML por recall, avaliar pesos amostrais na funcao de custo e explorar features via SHAP. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha pre-processamento (CPI, OCDE, FCS, PCA, VIF < 10), split 70/30, 5-fold CV, espaco de hiperparametros (Apendice C) e equacoes da funcao de custo ponderada. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Recall, Precisao, F1-Score, AUPR e matrizes de confusao no conjunto de teste para todos os modelos com e sem pesos amostrais. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 0 | Analisa exclusivamente determinantes socioeconomicos, agricolas e estruturais de evasao escolar; nao contempla fatores socioemocionais, psicologicos ou recusa escolar. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 1 | Discute cautela etica (religiao/casamento), nao causalidade do SHAP, restricao ao Malawi e necessidade de ML multinivel, mas sem secao formal de limitacoes de vies amostral/atrito. |
| **TOTAL** | **Pontuacao de Rigor** | **7 / 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- **[Excluido - Criterio EC2]:** Estudo metodologicamente solido em ML e XAI (LASSO, MNN, RF, KernelSHAP), mas completamente fora do escopo socioemocional/psicologico da RSL: trata exclusivamente de evasao escolar no Malawi por pobreza extrema, trabalho infantil rural (*ganyu*/agricultura), inseguranca alimentar e infraestrutura comunitaria.
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
