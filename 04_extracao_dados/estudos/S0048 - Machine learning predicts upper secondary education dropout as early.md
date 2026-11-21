---
id: S0048
study_id: S0048
title: "Machine learning predicts upper secondary education dropout as early as the end of primary school"
year: 2024
database: "Scopus"
venue: "Scientific Reports"
doi: "10.1038/s41598-024-63629-0"
url: "https://www.scopus.com/pages/publications/85195344017?origin=resultslist"
status: "[Excluido Fase 2 - Criterio EC2 (Foco em dropout academico sem peso relevante de fatores socioemocionais)]"
qa_score: 9
population_scope: "Educação Básica (Ensino Fundamental Inicial)"
intervention_scope: "Modelos de Machine Learning / IA e Análise Preditiva"
outcome_scope: "Predição de Risco de Abandono Escolar no K-12"
authors:
  - "Maria Psyridou"
  - "Fabi Prezja"
  - "Minna Torppa"
  - "Marja-Kristiina Lerkkanen"
  - "Anna-Maija Poikkeus"
  - "Kati Vasalampi"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "Questionarios longitudinais First Steps / School Path (motivacao, burnout escolar, engajamento, bullying)"
  - "Testes padronizados cognitivos e academicos (RAN, Raven, leitura, aritmetica, PISA)"
algorithms:
  - "[[Random_Forest|Balanced Random Forest (B-RandomForest)]]"
  - "Easy Ensemble (AdaBoost Ensemble)"
  - "RSBoost (AdaBoost)"
  - "Bagging Decision Tree"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/absenteismo_cronico
---
# S0048: Machine learning predicts upper secondary education dropout as early as the end of primary school

> [!INFO] Metadados Rapidos
> - **ID do Estudo:** `S0048`
> - **Autores:** Maria Psyridou, Fabi Prezja, Minna Torppa, Marja-Kristiina Lerkkanen, Anna-Maija Poikkeus, Kati Vasalampi
> - **Ano:** 2024
> - **Veiculo (Venue):** *Scientific Reports* (Nature Portfolio, Vol. 14, 12956)
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science', 'Springer Link']`)
> - **DOI:** [10.1038/s41598-024-63629-0](https://doi.org/10.1038/s41598-024-63629-0)
> - **URL:** [Link da Publicacao](https://www.scopus.com/pages/publications/85195344017?origin=resultslist)
> - **Status da Extracao:** `[Excluido Fase 2 - Criterio EC2 (Foco em dropout academico sem peso relevante de fatores socioemocionais)]`

> [!WARNING] [EM DUVIDA] Zona Cinzenta na Triagem Restritiva (IC1)
> Este estudo aplica **Machine Learning supervisionado rigoroso** (`Balanced Random Forest`, `EasyEnsemble`, `RSBoost`, `Bagging Decision Tree`, validacao cruzada estratificada 6-fold) em uma coorte longitudinal de 13 anos da educacao basica finlandesa. Contudo, apresenta **duas restricoes importantes** sob o criterio IC1 restritivo: (1) o desfecho predito e **evasao/nao conclusao no ensino medio (*upper secondary dropout* aos 18-19 anos)** e nao recusa escolar ou absenteismo cronico (embora *school absences* seja uma das 311 features de entrada); (2) embora inclua variaveis socioemocionais entre as 311 features (*school burn-out*, bullying, relacao professor-aluno, motivacao, comportamento prosocial), o ranking das 20 features mais relevantes e dominado quase exclusivamente por **habilidades cognitivas e desempenho academico** (fluencia/compreensao leitora, aritmetica, RAN), sem analise dedicada dos fatores socioemocionais. Submetido ao pesquisador para deliberacao entre inclusao ou exclusao por EC2.

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Education plays a pivotal role in alleviating poverty, driving economic growth, and empowering individuals, thereby significantly influencing societal and personal development. However, the persistent issue of school dropout poses a significant challenge, with its effects extending beyond the individual. While previous research has employed machine learning for dropout classification, these studies often suffer from a short-term focus, relying on data collected only a few years into the study period. This study expanded the modeling horizon by utilizing a 13-year longitudinal dataset, encompassing data from kindergarten to Grade 9. Our methodology incorporated a comprehensive range of parameters, including students' academic and cognitive skills, motivation, behavior, well-being, and officially recorded dropout data. The machine learning models developed in this study demonstrated notable classification ability, achieving a mean area under the curve (AUC) of 0.61 with data up to Grade 6 and an improved AUC of 0.65 with data up to Grade 9. Further data collection and independent correlational and causal analyses are crucial. In future iterations, such models may have the potential to proactively support educators' processes and existing protocols for identifying at-risk students, thereby potentially aiding in the reinvention of student retention and success strategies and ultimately contributing to improved educational outcomes.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Ensino Fundamental Inicial)
- **Intervencao/Tecnologia (Intervention Scope):** Modelos de Machine Learning / IA e Análise Preditiva
- **Desfecho (Outcome Scope):** Predição de Risco de Abandono Escolar no K-12
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao / Observacao Fase 2:**
  > Mantido provisoriamente como `[Incluido Fase 2 - Extracao Concluida]` com sinalizacao `[EM DUVIDA]`: aplica ML supervisionado longitudinal (K-Grade 9) com fatores socioemocionais parciais entre 311 features, porem prediz evasao no ensino medio (*dropout*) e nao recusa escolar/absenteismo, com predominio de features academicas e AUC modesto (0,61-0,65).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0048`
- **Titulo Completo:** Machine learning predicts upper secondary education dropout as early as the end of primary school
- **Autores:** Maria Psyridou, Fabi Prezja, Minna Torppa, Marja-Kristiina Lerkkanen, Anna-Maija Poikkeus, Kati Vasalampi
- **Ano de Publicacao:** 2024
- **Tipo de Publicacao:** Periodico cientifico revisado por pares
- **Nome do Veiculo:** Scientific Reports
- **DOI:** [10.1038/s41598-024-63629-0](https://doi.org/10.1038/s41598-024-63629-0)
- **Base de Dados:** Scopus (tambem indexado em Web of Science e Springer Link)
- **Pais/Regiao de Realizacao do Estudo:** Finlandia (quatro municipios: dois medios, um grande e um rural; projetos *First Steps* e *School Path*)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (pre-escola/Kindergarten ao 9o ano como entrada; Ensino Medio - *upper secondary*, track academico ou profissionalizante - como desfecho)
- **Faixa Etaria / Amostra ($N$):** Aproximadamente 2.000 criancas nascidas em 2000 acompanhadas em 10 ondas da pre-escola (6-7 anos) ao 9o ano (15-16 anos) no estudo *First Steps*, somadas a novos colegas de turma na transicao para o ensino medio (total $N = 4.160$ no *School Path*, acompanhados nos Grades 10 [16-17 anos] e 12 [18-19 anos]; participacao apenas de alunos presentes em ambos os estudos).
- **Publico-alvo Avaliado:** Estudantes em risco de nao concluir o ensino medio no prazo esperado de 3,5 anos (*dropout* registrado).
- **Fonte dos Dados / Dataset:** Dados longitudinais de pesquisa (tarefas academicas/cognitivas em grupo, questionarios de alunos em sala de aula e questionarios de pais) combinados com registros administrativos oficiais de conclusao do ensino medio (T3, final de 2019).

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** Nao utiliza escalas clinicas de recusa escolar ([[SRAS-R]], [[SCREEN]] ou [[SCARED]]). Utiliza questionarios autorrelatados e de pais dos estudos *First Steps*/*School Path* (incluindo *school burn-out*, motivacao, valor da tarefa, autoconceito, comportamento prosocial, hiperatividade, bullying, engajamento e relacao professor-aluno) e baterias cognitivo-academicas padronizadas (RAN, Raven, vocabulario, fluencia/compreensao leitora, aritmetica, multiplicacao, PISA).
- **Natureza da Ferramenta:** Questionarios longitudinais de pesquisa educacional e testes cognitivos/academicos aplicados em grupo.
- **Forma de Aplicacao:** Autorrelato dos alunos em sala de aula, questionarios aos pais e testes aplicados em grupo + registros oficiais escolares.
- **Finalidade:** Rastreio preditivo longitudinal precoce (Grade 6 e Grade 9) de risco de abandono escolar no ensino medio.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Machine Learning Supervisionado (Ensembles para dados desbalanceados via `imbalanced-learn` / `scikit-learn`).
- **Algoritmos Empregados:** [[Random_Forest|Balanced Random Forest]] (`B-RandomForest`, 100 estimadores com configuracao padrao), `Easy Ensemble` (`E-Ensemble` / AdaBoost Ensemble), `RSBoost` (`B-Boosting` / AdaBoost com subamostragem aleatoria) e `Bagging Decision Tree` (`B-Bagging`).
- **Tarefa do Modelo:** Classificacao binaria (`dropout` vs. `non-dropout` 3,5 anos apos iniciar o ensino medio), avaliada em dois horizontes: dados da pre-escola ate o Grade 9 (15-16 anos) e dados ate o Grade 6 (12-13 anos).
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva de longo prazo (ao final do ensino fundamental I [Grade 6] e fundamental II [Grade 9]).

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** *School burn-out*, hiperatividade, comportamento prosocial, bem-estar, autoconceito e valor da tarefa (*task value*), vitimizacao e perpetracao de bullying.
- **Variaveis Comportamentais / Historico:** Faltas escolares (*absences from school*), engajamento em sala, comportamentos de saude (tabagismo, alcool), uso de midia/telefone/internet, habilidades cognitivas (RAN, Raven, vocabulario) e desempenho academico (fluencia leitora, compreensao leitora, PISA, aritmetica, multiplicacao).
- **Variaveis Familiares / Sociodemograficas:** Genero, escolaridade parental (`voedo`) e nivel socioeconomico (NSE).
- **Variaveis Institucionais / Contextuais:** Relacao professor-aluno (*teacher-student relationships*) e trilha escolar no ensino medio (academica vs. profissionalizante).
- **Features Mais Relevantes Identificadas:** No `B-RandomForest` ate o Grade 9 (Top 20, Fig. 6), **todas** as 20 features mais importantes foram de desempenho academico (fluencia leitora Grades 1-4, 7, 9; compreensao leitora Grades 1-4; PISA Grade 9; aritmetica Grades 1-4; multiplicacao Grades 4, 7) e habilidades cognitivas na pre-escola (RAN e vocabulario). Ate o Grade 6 (Top 20, Fig. 7), entraram tambem escolaridade parental (`voedo`) e valor da tarefa em matematica no Grade 6 (`tavma_g6`), ainda sob dominio absoluto de variaveis academicas/cognitivas. Faltas escolares e variaveis socioemocionais nao apareceram entre as 20 principais.

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A (nao reporta coeficientes psicometricos das escalas no artigo).
- **Metricas Computacionais (ML):** Melhor modelo = `B-RandomForest`. Com dados ate o Grade 9: AUC = $0,65$, Balanced Accuracy = $0,607$, Accuracy = $0,611$, Recall = $0,599$ ($0,60$), Specificity = $0,62$, Precision = $0,582$, F1-score = $0,573$ (comparado a `E-Ensemble` BalAcc $0,596$, `B-Boosting` $0,571$, `B-Bagging` $0,550$). Com dados ate o Grade 6: AUC = $0,61$, Balanced Accuracy = $0,588$, Accuracy = $0,589$, Recall = $0,587$, Specificity = $0,59$, Precision = $0,569$, F1-score = $0,554$.
- **Estrategia de Validacao:** Validacao cruzada estratificada $K$-fold ($K = 6$), matrizes de confusao normalizadas medias e curvas ROC/AUC agregadas nos 6 folds. Imputacao por moda (categoricas) e mediana (numericas) derivada em amostra temporaria subamostrada para balanceamento.
- **Desafios Metodologicos Relatados:** Forte desbalanceamento da classe positiva (*dropout* reduzido), alta dimensionalidade (311 features; maldicao da dimensionalidade) e grande proporcao de dados faltantes devido a entrada de novos colegas em etapas posteriores (exclusao de features com >30% de *missingness*, reduzindo de 586 para 311 features).
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao etica da University of Jyväskylä (2006 e 2018) e consentimento dos responsaveis (T1/T2) e dos proprios jovens (T3). Extrai ranking medio de importancia de features do Random Forest, ressaltando explicitamente que tais importancias nao implicam causalidade ou correlacao direta.
- **Limitacoes Declaradas:** Poder preditivo moderado (AUC 0,61-0,65); exclusao de 275 features com >30% de dados faltantes; ausencia de ajuste de hiperparametros (uso de *defaults*); amostra cultural e etnicamente homogenea da Finlandia (generalizacao incerta); ausencia de conjunto de teste externo independente e ausencia de analise causal.
- **Direcoes Futuras:** Coleta de dados mais abrangentes em outros contextos educacionais/demograficos, validacao em conjuntos de teste independentes, investigacao de melhores estrategias de imputacao/selecao de features e analises correlacionais/causais independentes.

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** Dados longitudinais de pesquisa aplicados em sala de aula (Grades K a 9, em 10 ondas de 2006 a 2016) cobrindo questionarios autorrelatados (motivacao, *school burn-out*, bullying, comportamento, relacao professor-aluno), questionarios de pais e testes cognitivo-academicos presenciais, cruzados com registro administrativo oficial de conclusao escolar aos 18-19 anos (T3, final de 2019). Nao utiliza escalas clinicas especificas de ansiedade ou recusa escolar.
- **Inventario completo de variaveis e justificativa de escolha:** 311 features finais (com *one-hot encoding*, selecionadas dentre 586 originais com <30% de dados faltantes) distribuidas em 10 dominios: contexto familiar, fatores individuais (genero, faltas, *burnout* escolar), comportamento (prosocial, hiperatividade), motivacao (autoconceito, valor da tarefa), engajamento (relacao professor-aluno, engajamento em aula), bullying (vitima e autor), comportamentos de saude (tabagismo, alcool), uso de midias/internet, habilidades cognitivas (RAN, Raven, vocabulario) e desempenho academico (leitura, aritmetica, multiplicacao, PISA). A escolha ampla visa capturar precocemente o processo gradual de desengajamento escolar ao longo de 13 anos.
- **Fundamentacao teorica do identificador:** Baseia-se na teoria do abandono escolar como processo cumulativo e de longo prazo iniciado nos primeiros anos da escolarizacao (Balfanz et al., 2007; Schoeneberger, 2012; Rumberger, 2012; De Witte et al., 2013; Esch et al., 2014) e no paradigma de *Early Warning Systems* (Knowles, 2015), empregando ensembles balanceados baseados em arvores (Breiman, 2001; Liu et al., 2008) para lidar com alta dimensionalidade e desbalanceamento severo.
- **Restricoes de recursos e limitacoes:** Exige infraestrutura longitudinal massiva (13 anos de coletas multi-ondas com testes cognitivos e academicos padronizados aplicados em grupo e integracao com registros nacionais de graduacao), sendo inviavel como solucao pronta de baixo custo em escolas sem coleta longitudinal sistematica. Limitacoes incluem AUC modesto (0,61-0,65), descarte de variaveis com >30% de *missingness*, uso de hiperparametros padrao, homogeneidade da amostra finlandesa e ausencia de validacao externa.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Formula duas questoes de pesquisa explicitas sobre predicao de evasao no ensino medio com dados ate Grade 9 e comparacao com Grade 6. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Coorte longitudinal de 13 anos, tratamento de dados faltantes (>30%), imputacao balanceada, 4 algoritmos do `imbalanced-learn` e CV 6-fold bem especificados. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Accuracy, Balanced Accuracy, Recall, Precision, F1-score, Specificity, matrizes de confusao normalizadas e curvas ROC/AUC nos dois horizontes. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Incorpora *school burn-out*, bullying, bem-estar, motivacao e relacao professor-aluno entre as 311 features, mas nao analisa especificamente recusa escolar e os resultados principais sao puramente academico-cognitivos. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute desbalanceamento de classe, maldicao da dimensionalidade, dados faltantes (>30%), impossibilidade de inferencia causal e limitacao de generalizacao fora da Finlandia. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | Estudo de ML tecnicamente robusto, porem em zona cinzenta (`[EM DUVIDA]`) por focar *dropout* e ter fatores socioemocionais apenas secundarios/parciais. |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- **`[EM DUVIDA]` para deliberacao de Matheus:** Embora seja o estudo mais rigoroso do Lote A em termos de pipeline de Machine Learning supervisionado, ele prediz **evasao/nao conclusao no ensino medio (*upper secondary dropout*)**, nao recusa escolar ou absenteismo cronico. Faltas escolares e *school burn-out* entram apenas como features dentro de um conjunto de 311 variaveis dominado por testes cognitivos e de leitura/matematica (AUC = 0,61-0,65).

---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
