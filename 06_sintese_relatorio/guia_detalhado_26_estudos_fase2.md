# Guia Detalhado de Estudo — 26 PDFs Analisados (Fase 2)

**Pesquisador:** Matheus Henrique Assuncao de Medeiros (PGCC UERN / UFERSA)  
**Conteudo:** Extracao integral de cada artigo (Identificacao, PICOC, RQ1-RQ4, Metricas, Limitacoes e Avaliacao QA1-QA5).

---

# Parte I — Eixo Computacional: IA, Machine Learning, EWS e XAI (12 estudos)

## S0501: Interpretable machine learning for predicting school absenteeism at-scale in Brazil: evidence from 22,000 schools

> - **ID do Estudo:** `S0501`
> - **Autores:** Abílio Nogueira Barros, Felipe Vieira Roque, Tiago Paulino, Augusto Schmidt, Flavia Galvani, Rafael Oliveira, Leonardo Brandão Marques, Diego Dermeval, Anita Gea Martinez Stefani, Marisa de Santana da Costa, Emanuel Marques Queiroga, Elthon Oliveira, Cristian Cechinel, Thales Vieira
> - **Ano:** 2026
> - **Veículo (Venue):** *Scientific Reports*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1038/s41598-026-48729-3](https://doi.org/10.1038/s41598-026-48729-3)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1038/s41598-026-48729-3)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0501`
- **Titulo Completo:** Interpretable machine learning for predicting school absenteeism at-scale in Brazil: evidence from 22,000 schools
- **Autores:** Abílio Nogueira Barros, Felipe Vieira Roque, Tiago Paulino, Augusto Schmidt, Flavia Galvani, Rafael Oliveira, Leonardo Brandão Marques, Diego Dermeval, Anita Gea Martinez Stefani, Marisa de Santana da Costa, Emanuel Marques Queiroga, Elthon Oliveira, Cristian Cechinel, Thales Vieira
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Artigo de Periódico
- **Nome do Veiculo:** Scientific Reports
- **DOI:** [10.1038/s41598-026-48729-3](https://doi.org/10.1038/s41598-026-48729-3)
- **Base de Dados:** Springer Link
- **Pais/Regiao de Realizacao do Estudo:** Brasil (abrangência nacional)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Médio (Educação Básica / K-12)
- **Faixa Etaria / Amostra ($N$):** N = 22.476 escolas brasileiras de Ensino Médio (filtradas de 29.993 escolas no Censo Escolar 2024 após integração com SGP), estratificadas em 6 níveis do Indicador de Complexidade de Gestão da Escola (ICG 1 a 6). Análise em nível institucional (escolar), sem dados individuais de alunos.
- **Publico-alvo Avaliado:** Escolas públicas/participantes de Ensino Médio no Brasil classificadas quanto ao risco sistêmico de absenteísmo escolar elevado.
- **Fonte dos Dados / Dataset:** Consolidação de três fontes oficiais brasileiras (INEP/MEC, ano-base 2024): (1) Sistema Gestão Presente (SGP, registros de frequência de estudantes do Ensino Médio); (2) Censo Escolar da Educação Básica 2024; (3) Indicador de Complexidade de Gestão da Escola (ICG 2024).

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** N/A (não utiliza escalas psicométricas; emprega as faixas de absenteísmo de Kearney [Low >=96%, Moderate 91-95%, Significant 81-90%, High 71-80%, Severe <=70%] apenas como critério de rotulagem da variável-alvo a partir de registros administrativos de frequência).
- **Natureza da Ferramenta:** N/A (baseada exclusivamente em registros administrativos educacionais e censo escolar).
- **Forma de Aplicacao:** N/A (coleta administrativa automatizada via SGP e Censo Escolar/INEP).
- **Finalidade:** Classificação institucional de risco de absenteísmo escolar elevado para apoio a políticas públicas.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Machine_Learning Supervisionado, Early_Warning_Systems em nível institucional, Explicabilidade_XAI (SHAP e análise de sensibilidade contrafactual "what-if").
- **Algoritmos Empregados:** Random_Forest (modelo principal selecionado pelo equilíbrio entre desempenho, interpretabilidade e equivalência estatística via teste de DeLong), CatBoost, XGBoost, LightGBM e Regressao_Logistica (baseline linear). Seleção de atributos via Informação Mútua + Mean Decrease in Impurity (MDI) do Random Forest (cutoff = 0.01, ~35 features por ICG); balanceamento via SMOTE.
- **Tarefa do Modelo:** Classificação binária em nível escolar (por faixa de ICG): Classe 1 (baixo risco: >50% dos alunos com frequência Low/Moderate) vs. Classe 0 (alto risco: >50% dos alunos com frequência Significant/High/Severe).
- **Estagio de Deteccao:** Alerta precoce institucional e diagnóstico exploratório de fatores estruturais/organizacionais associados ao absenteísmo.

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** N/A (o estudo opera exclusivamente no nível agregado da escola e declara explicitamente a ausência de variáveis socioemocionais ou psicológicas individuais).
- **Variaveis Comportamentais / Historico:** Taxa agregada de frequência escolar no Ensino Médio (SGP 2024) usada para compor a variável-alvo binária por escola.
- **Variaveis Familiares / Sociodemograficas:** N/A no nível individual; contexto regional capturado indiretamente por localização urbano/rural (`tp_location`) e composição de modalidades (regular, técnico, EJA).
- **Variaveis Institucionais / Contextuais:** ~350 atributos iniciais do Censo Escolar (294 após filtragem de correlação >0.85 e baixa informação mútua), agrupados em: (a) infraestrutura (`qt_classroom_used`, `qt_classroom_aircon`, `qt_pc_student`, `qt_projector`, `qt_tv`, `in_distance_learning`, `in_sewage_public`, `in_sewage_septic`, `in_material_none`); (b) recursos humanos (`qt_teacher_hs`, `qt_pedagogical_staff`, `qt_general_staff`, `qt_librarian_staff`, `qt_food_staff`, `qt_admin_staff`); (c) organização/governança (`in_regular`, `in_parent_teacher_association`, `qt_enroll_hs`, `qt_enroll_tech_hs`, `qt_class_hs`, `tp_location`) e estratificação pelo ICG (níveis 1 a 6).
- **Features Mais Relevantes Identificadas:** Via MDI e SHAP, `qt_pc_student`, `qt_pedagogical_staff`, `qt_teacher_hs` e `qt_class_hs` figuraram em 5 dos 6 modelos. `in_regular` destacou-se no ICG 1; `qt_classroom_aircon` nos ICGs 2, 3, 4 e 6 (Flip Rate >4% no ICG 3); `qt_pedagogical_staff` e `in_distance_learning` nos ICGs 5 e 6. Nas simulações contrafactuais (+1 DP), a taxa de reversão (Flip Rate 0->1) foi de 49,38% no ICG 1, 16,29% no ICG 2, 18,84% no ICG 3, 8,55% no ICG 4, 2,60% no ICG 5 e 0,57% no ICG 6.

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** N/A.
- **Metricas Computacionais (ML):** Acurácia, Precisão, Recall, F1-Score e teste de DeLong para AUC-ROC (sem diferença estatística entre RF e CatBoost). Desempenho do Random Forest no conjunto de teste: ICG 1 (Acc=0,85; Prec=0,76; Rec=0,89; F1=0,81), ICG 2 (Acc=0,75; Prec=0,76; Rec=0,82; F1=0,79), ICG 3 (Acc=0,67; Prec=0,68; Rec=0,81; F1=0,74), ICG 4 (Acc=0,74; Prec=0,69; Rec=0,64; F1=0,67), ICG 5 (Acc=0,78; Prec=0,80; Rec=0,72; F1=0,75), ICG 6 (Acc=0,84; Prec=0,86; Rec=0,43; F1=0,58). CatBoost obteve leve vantagem em ICG 3 (Acc=0,71; F1=0,77) e ICG 4 (Acc=0,75; F1=0,68).
- **Estrategia de Validacao:** Split estratificado 75/25 treino/teste com validação cruzada estratificada 5-fold (`StratifiedKFold`, k=5) e grid-search no conjunto de treino; comparação estatística de AUC-ROC via teste de DeLong.
- **Desafios Metodologicos Relatados:** Desbalanceamento de classes entre ICGs (54,70% classe 0 vs. 45,30% classe 1 no total, chegando a 75% classe 0 no ICG 6), mitigado com SMOTE; alta dispersão/desigualdade estrutural nas variáveis escolares; baixo recall no ICG 6 (0,43 no RF); risco de interpretar variáveis proxy (como ar-condicionado) como alavancas causais diretas.
- **Aspectos Eticos e Transparencia (XAI):** Conformidade com a LGPD (dados do SGP restritos por conterem informações sensíveis ligadas a programa de transferência de renda); uso de SHAP e simulações contrafactuais para transparência; alerta explícito contra interpretações causais/prescritivas diretas.
- **Limitacoes Declaradas:** Granularidade agregada em nível escolar (não individual por estudante), omitindo fatores pessoais, familiares e socioemocionais; natureza observacional/associativa (não causal); dependência da qualidade dos registros administrativos; presença de variáveis proxy socioeconômicas.
- **Direcoes Futuras:** Estender a modelagem para o nível individual do aluno integrando Censo Escolar, histórico individual de frequência, dados sociodemográficos e indicadores de vizinhança; avaliar LIME e Anchors; incorporar técnicas de fairness-aware ML.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo e duas RQs formais sobre ML interpretável e análise contrafactual para predizer risco de absenteísmo escolar por nível de complexidade (ICG). |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha consolidação de 3 bases oficiais (N = 22.476 escolas), filtragem de 350 para 294 variáveis, seleção por RF MDI, SMOTE, split 75/25, 5-fold CV e 5 algoritmos comparados. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Acurácia, Precisão, Recall e F1-Score por modelo e por ICG na Tabela 5, além de teste de DeLong para AUC-ROC e taxas de reversão (Flip Rate) nas simulações. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Analisa extensivamente fatores contextuais, institucionais, infraestrutura e recursos humanos por ICG, mas não inclui variáveis psicológicas ou socioemocionais individuais. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute explicitamente a limitação da agregação escolar, ausência de dados socioemocionais individuais, natureza não causal, variáveis proxy e necessidade de fairness. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | Estudo robusto em escala nacional com XAI (SHAP + contrafactuais), limitado apenas pela ausência de dados individuais/socioemocionais. |

---

---

## S0290: Explainable Ensemble Learning for Student Dropout Prediction in Conflict-Affected Educational Systems

> - **ID do Estudo:** `S0290`
> - **Autores:** Amna Abas, Mansour Essgaer, Llahm Ben Dalla
> - **Ano:** 2026
> - **Veículo (Venue):** *2026 IEEE 5th International Maghreb Meeting of the Conference on Sciences and Techniques of Automatic Control and Computer Engineering (MI-STA)*
> - **Base de Origem:** `IEEE Xplore` (Bases: `['IEEE Xplore']`)
> - **DOI:** [10.1109/MI-STA68962.2026.11511168](https://doi.org/10.1109/MI-STA68962.2026.11511168)
> - **URL:** Não informado
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0290`
- **Titulo Completo:** Explainable Ensemble Learning for Student Dropout Prediction in Conflict-Affected Educational Systems
- **Autores:** Amna Abas, Mansour Essgaer, Llahm Ben Dalla
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** 2026 IEEE 5th International Maghreb Meeting of the Conference on Sciences and Techniques of Automatic Control and Computer Engineering (MI-STA)
- **DOI:** [10.1109/MI-STA68962.2026.11511168](https://doi.org/10.1109/MI-STA68962.2026.11511168)
- **Base de Dados:** IEEE Xplore
- **Pais/Regiao de Realizacao do Estudo:** Libia (Sabha, regiao de Fezzan)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Secundario / Medio (transicao para o ensino superior)
- **Faixa Etaria / Amostra ($N$):** N = 1.158 estudantes do ensino medio (de populacao de 2.635 examinandos em 5 escolas, 2023; faixas de 17-18 e 19-22 anos; 1.129 registros rotulados na distribuicao final: 84,0% [949] continuam vs. 16,0% [180] risco de evasao)
- **Publico-alvo Avaliado:** Estudantes concluintes do ensino secundario em contexto afetado por conflito armado (risco de evasao / nao-matricula no ensino superior)
- **Fonte dos Dados / Dataset:** Questionario estruturado de 34 itens aplicado em 5 escolas de Sabha, Libia (2023), adaptado de estudos previos para o contexto sociocultural local

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** Questionario estruturado de 34 itens (adaptado) + 4 indices compostos engenheirados (PES, SCI, RAS, SAI); sem escala clinica padronizada (ex.: SRAS-R/SCARED)
- **Natureza da Ferramenta:** Questionario de triagem multidimensional (6 categorias de atributos) e indicadores compostos
- **Forma de Aplicacao:** Autorrelato do aluno
- **Finalidade:** Triagem inicial e perfilamento exploratorio de risco de evasao / nao-transicao

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Machine Learning Supervisionado (Ensemble Learning: Bagging e Boosting) com IA Explicavel (Explicabilidade_XAI via LIME), selecao de features (LASSO, RFE, Mutual Information, Chi-Squared) e balanceamento SMOTE (Early_Warning_Systems)
- **Algoritmos Empregados:** XGBoost, Random_Forest, LASSO, Explicabilidade_XAI (LIME)
- **Tarefa do Modelo:** Classificacao binaria (`Continued Enrollment` vs. `Dropped Out`) sobre variavel-alvo sintetica construida por heuristicas baseadas em regras
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (perfilamento exploratorio de risco na transicao ensino medio-superior)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Stress and Anxiety Index (SAI: frequencia de ansiedade, disciplinas dificeis, estresse autoavaliado), ansiedade nos estudos, motivacao para aprender, aspiracao ao ensino superior, bem-estar fisico/saude
- **Variaveis Comportamentais / Historico:** Faltas (1-7, 8-20, >20 dias), horas de estudo (<2, 2-5, >5h), historico de reprovacoes, Student Commitment Index (SCI), socializacao com amigos, engajamento em ensino a distancia
- **Variaveis Familiares / Sociodemograficas:** Parental Engagement Score (PES), escolaridade e ocupacao materna/paterna, estado civil dos pais, coesao familiar, suporte financeiro, tamanho da familia, genero, idade, area residencial
- **Variaveis Institucionais / Contextuais:** Tipo de escola (publica/privada/homeschool), tempo de deslocamento, eficacia docente, acesso a internet, posse de dispositivo eletronico (RAS), aulas particulares, contexto de conflito armado
- **Features Mais Relevantes Identificadas:** Consenso entre >=3 seletores: PES, SCI, SAI, desejo de cursar ensino superior, motivacao para aprender, engajamento em ensino a distancia, eficacia dos professores, socializacao com amigos e bem-estar fisico. No LIME: deslocamento >=30 min, posse de dispositivo, ansiedade nos estudos, eficacia docente e tutoria privada

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** N/A (nao reporta Alfa de Cronbach ou validade fatorial do questionario)
- **Metricas Computacionais (ML):** XGBoost: Acuracia = 0,941, Precisao = 0,941, Recall = 0,941, F1-Score = 0,941, LogLoss = 0,161, CV Accuracy = 0,940, CV F1 = 0,939. Random Forest: Acuracia = 0,939, Precisao = 0,939, Recall = 0,939, F1-Score = 0,939, LogLoss = 0,161, CV Accuracy = 0,935, CV F1 = 0,934
- **Estrategia de Validacao:** Split estratificado 70% treino / 30% teste + GridSearchCV com 10-fold cross-validation
- **Desafios Metodologicos Relatados:** Ausencia de rotulos reais (ground truth) exigindo alvo sintetico por regras; desbalanceamento de classes (84% vs. 16%) mitigado com SMOTE; risco de overfitting tratado com regularizacao e profundidade limitada (XGBoost `max_depth=3`)
- **Aspectos Eticos e Transparencia (XAI):** Uso de LIME (Explicabilidade_XAI) para explicabilidade local por estudante, mitigando o problema de caixa-preta e apoiando intervencoes direcionadas
- **Limitacoes Declaradas:** Dependencia de variavel-alvo sintetica baseada em heuristicas; as metricas refletem o aprendizado do proxy baseado em regras, e nao uma previsao definitiva das taxas reais de evasao
- **Direcoes Futuras:** Validacao com dados longitudinais reais de evasao e implementacao de politicas de apoio psicossocial, engajamento parental e suporte socioeconomico

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo de estabelecer framework explicavel de ML para perfilamento exploratorio de risco de evasao / nao-transicao em Sabha, Libia. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha amostra (N=1.158), questionario (34 itens), formulas dos 4 indices compostos, alvo sintetico, SMOTE, selecao LASSO, split 70/30, 10-fold GridSearchCV, hiperparametros e LIME. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Acuracia, Precisao, Recall, F1-Score, LogLoss, CV Accuracy e CV F1 para XGBoost e Random Forest, alem de comparacao entre 4 tecnicas de selecao de features. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa estresse e ansiedade (SAI), motivacao, aspiracoes, coesao familiar, engajamento parental (PES), socializacao e o impacto do conflito armado. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 1 | Reconhece explicitamente a limitacao da variavel-alvo sintetica (proxy heuristico sem ground truth real), mas nao discute o potencial vazamento entre features e regras do alvo ou vieses de autorrelato. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | |

---

---

## S0315: Difficult Lessons on Social Prediction from Wisconsin Public Schools

> - **ID do Estudo:** `S0315`
> - **Autores:** Juan Carlos Perdomo, Tolani Britton, Moritz Hardt, Rediet Abebe
> - **Ano:** 2025
> - **Veículo (Venue):** *Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency*
> - **Base de Origem:** `ACM DL` (Bases: `['ACM DL']`)
> - **DOI:** [10.1145/3715275.3732175](https://doi.org/10.1145/3715275.3732175)
> - **URL:** [Link da Publicação](https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3715275.3732175)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0315`
- **Titulo Completo:** Difficult Lessons on Social Prediction from Wisconsin Public Schools
- **Autores:** Juan Carlos Perdomo, Tolani Britton, Moritz Hardt, Rediet Abebe
- **Ano de Publicacao:** 2025
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency
- **DOI:** [10.1145/3715275.3732175](https://doi.org/10.1145/3715275.3732175)
- **Base de Dados:** ACM DL
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (Estado de Wisconsin)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Basico (Escolas Publicas K-12; predicoes no 8o ano para conclusao do ensino medio em 4 anos)
- **Faixa Etaria / Amostra ($N$):** Mais de 200.000 estudantes (~215.000 alunos em 4 coortes do 8o ano, 2013-2021; experimentos com CatBoost em ~160.000 treino / ~40.000 teste)
- **Publico-alvo Avaliado:** Estudantes da rede publica estadual de Wisconsin (avaliacao do sistema DEWS e comparacao entre alocacao individual e ambiental)
- **Fonte dos Dados / Dataset:** Wisconsin Department of Public Instruction (DPI) - DEWS / WISEDash (2013-2021), US Census Bureau American Community Survey (ACS 5 anos) e National Center for Education Statistics (ELSI)

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** N/A (nao utiliza escalas psicometricas; baseia-se em dados administrativos estaduais, exames padronizados e indicadores censitarios)
- **Natureza da Ferramenta:** Sistema administrativo de alerta precoce (DEWS) alimentado por registros escolares e censitarios (>40 features)
- **Forma de Aplicacao:** Registros institucionais estaduais (sem aplicacao de questionarios psicometricos aos alunos)
- **Finalidade:** Triagem e classificacao de risco de nao-conclusao do ensino medio no prazo (low, moderate, high)

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Early_Warning_Systems (DEWS), Machine Learning Supervisionado (Ensemble Learning) e Inferencia Causal (Regression Discontinuity Design - RDD, alem de teste "predicting from predictions")
- **Algoritmos Empregados:** Early_Warning_Systems, Random_Forest, Gradient-Boosted Decision Trees (CatBoost), Regressao Linear Local (RDD)
- **Tarefa do Modelo:** Estimativa de probabilidade continua de formatura no prazo e classificacao em 3 categorias de risco (`low`, `moderate`, `high` via limiar $t^*=0,785$)
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (predicoes geradas do 5o ao 8o ano, com foco no 8o ano antes da entrada no ensino medio)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Nao mensura construtos psicologicos diretamente; inclui indicador de status de deficiencia (que engloba classificacoes como *Emotional Behavioral Disability*)
- **Variaveis Comportamentais / Historico:** Taxa de frequencia escolar (`Student Attendance Rate`), dias matriculados, notas em exames padronizados de leitura e matematica, retencao previa, numero de incidentes disciplinares, dias removidos/suspensao, tipo de remocao/descritores disciplinares, mobilidade entre escolas/distritos
- **Variaveis Familiares / Sociodemograficas:** Genero, raca/etnia, elegibilidade para almoco gratuito ou reduzido (proxy de pobreza), status de aprendiz de ingles (EL); no nivel distrital (ACS): renda domiciliar mediana, taxa de pobreza, desemprego, escolaridade de adultos, estrutura familiar, acesso a computador/internet e cobertura de seguro saude
- **Variaveis Institucionais / Contextuais:** Tamanho da coorte, medias e desvios padrao de leitura, matematica e frequencia da coorte, % de suspensoes/deficiencia/baixa renda/nao-brancos na coorte, receitas e despesas por aluno (ELSI)
- **Features Mais Relevantes Identificadas:** Preditores ambientais/comunitarios concentram quase todo o poder preditivo devido a segregacao entre distritos; dentre as variaveis individuais adicionadas ao modelo ambiental, `Attendance Rate` foi a mais importante (reducao de 4% no squared loss), seguida por notas em exames padronizados

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** N/A
- **Metricas Computacionais (ML):** DEWS (8o ano, 2018-2021): AUC = 0,80; taxa real de formatura por grupo: ~97% (baixo risco), 83% (medio), <70% (alto). CatBoost (Performative vs. Non-Performative): AUC = 0,863 vs. 0,862; Log Loss = 0,185; Squared Loss = 0,052; 0-1 Loss = 0,065 vs. 0,066; $r^2$ = 0,184 vs. 0,183. Ganho ao adicionar features individuais sobre ambientais: -9,6% no Squared Loss, -14,6% no Log Loss, -3,9% no 0-1 Loss, +10,2% relativo (+0,082) no AUC. RDD causal: $\tau_{mod \to high} = +4,8\%$ (IC 95%: -2,0% a 11,6%, p=0,17); $\tau_{low \to mod} = +2,2\%$ (IC 95%: -2,7% a 7,1%, p=0,38)
- **Estrategia de Validacao:** Janela deslizante de 5 coortes anuais no DEWS; split 80/20 (~160k treino / ~40k teste) no CatBoost; Regression Discontinuity Design (RDD) com testes de balanceamento, manipulacao e sensibilidade de bandwidth ($h=0,005, 0,01, 0,02$) e Bootstrap (10.000 reamostragens)
- **Desafios Metodologicos Relatados:** Miscalibracao das probabilidades absolutas do DEWS; disparidades de calibracao entre subgrupos demograficos que podem despriorizar alunos historicamente marginalizados em rankings relativos; baixa variancia intraescolar devido a forte segregacao socioeconomica entre distritos
- **Aspectos Eticos e Transparencia (XAI):** Discussao central sobre equidade algoritmica (fairness/multicalibration), risco de despriorizacao sistematica de estudantes nao-brancos, de baixa renda ou com deficiencia, e vantagem de transparencia/custo/privacidade de politicas baseadas em escolas frente a escores individuais opacos
- **Limitacoes Declaradas:** Incerteza estatistica nas estimativas causais do RDD (ICs de 95% incluem zero); resultados sobre equivalencia da predicao ambiental refletem a segregacao socioeconomica de Wisconsin e podem nao se aplicar a contextos distintos (ex.: Nova York); dados de acesso ao portal WISEDash indisponiveis antes de 2018
- **Direcoes Futuras:** Realizar estudos qualitativos in situ com educadores sobre o uso pratico de EWS e priorizar intervencoes estruturais voltadas a escolas e comunidades vulneraveis

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente dois objetivos: avaliar o impacto causal de longo prazo do DEWS na formatura e comparar a eficacia de alocacao via escores individuais vs. variaveis ambientais. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Descreve rigorosamente a base estadual (>200k alunos, 2013-2021), todas as features (Apendice B), modelos CatBoost (80/20) e desenho causal RDD com testes de robustez. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Apresenta AUC (0,80 no DEWS; 0,863 no CatBoost), curvas de calibracao, Squared Loss, Log Loss, 0-1 Loss, $r^2$, estimativas RDD, ICs de 95% (Bootstrap/CLT) e p-valores. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Analisa profundamente fatores contextuais, institucionais, socioeconomicos e comportamentais (frequencia, disciplina, segregacao), mas nao aborda fatores psicologicos/socioemocionais individuais. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute amplamente vieses de calibracao entre grupos demograficos, incerteza estatistica das estimativas causais, limites de generalizacao geografica e restricoes dos dados de uso. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | |

---

---

## S0322: Early Alert Systems During a Pandemic: A Simulation Study on the Impact of Concept Drift

> - **ID do Estudo:** `S0322`
> - **Autores:** Yang Xu, Kevin Wilson
> - **Ano:** 2021
> - **Veículo (Venue):** *LAK21: 11th International Learning Analytics and Knowledge Conference*
> - **Base de Origem:** `ACM DL` (Bases: `['ACM DL']`)
> - **DOI:** [10.1145/3448139.3448190](https://doi.org/10.1145/3448139.3448190)
> - **URL:** [Link da Publicação](https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3448139.3448190)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0322`
- **Titulo Completo:** Early Alert Systems During a Pandemic: A Simulation Study on the Impact of Concept Drift
- **Autores:** Yang Xu, Kevin Wilson
- **Ano de Publicacao:** 2021
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** LAK21: 11th International Learning Analytics and Knowledge Conference
- **DOI:** [10.1145/3448139.3448190](https://doi.org/10.1145/3448139.3448190)
- **Base de Dados:** ACM DL
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (Estado de Rhode Island)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Medio (High School, 9o ao 12o ano; treino com dados de 9o a 11o ano)
- **Faixa Etaria / Amostra ($N$):** Todos os estudantes das escolas publicas de ensino medio de Rhode Island (coortes de treino SY 2007-2015; conjunto de teste SY 2016 com N = 2.731 casos positivos de evasao escolar)
- **Publico-alvo Avaliado:** Estudantes do ensino medio da rede publica estadual (avaliacao de robustez de EWS frente a *concept drift* pandemico)
- **Fonte dos Dados / Dataset:** Sistema de Informacoes Estudantis do Rhode Island Department of Education (RIDE), em parceria com The Policy Lab (Brown University) e DataSpark

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** N/A (nao utiliza instrumentos psicometricos; utiliza registros administrativos e desempenho academico)
- **Natureza da Ferramenta:** Painel de EWS (`teacher information portal`) com 6 indicadores atualizados mensalmente (frequencia, retencao, suspensoes, proficiencia em matematica e ELA, e indicador de risco)
- **Forma de Aplicacao:** Registros institucionais estaduais
- **Finalidade:** Triagem inicial e alerta precoce de risco de evasao (codificado em vermelho [top 3%], amarelo [2% seguintes] e verde)

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Early_Warning_Systems (EWS), Machine Learning Supervisionado (Random_Forest via `FastForest` / `nimbusml`) e simulacao baseada em imputacao para analise de *concept drift* (3 cenarios)
- **Algoritmos Empregados:** Early_Warning_Systems, Random_Forest (`FastForest`)
- **Tarefa do Modelo:** Classificacao binaria (evasao escolar ate o 12o ano) e ranqueamento por escore de risco (`high`: top 3%, `moderate`: 2% seguintes)
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (gerado no inicio de cada ano letivo utilizando historico dos 2 anos anteriores)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** N/A (nao inclui variaveis psicologicas ou socioemocionais diretas)
- **Variaveis Comportamentais / Historico:** Taxa de frequencia escolar (`attendance percentages`), retencao de serie, numero de infracoes (`grievances`), dias de suspensao interna e externa, notas em testes estaduais padronizados (Math, ELA), SAT e PSAT
- **Variaveis Familiares / Sociodemograficas:** Genero, idade, raca, etnia, nivel socioeconomico e status de educacao especial
- **Variaveis Institucionais / Contextuais:** Mudanca na politica estadual de suspensoes (SY 2012), exclusao de unidade de detencao juvenil por perfil atipico, disrupcao pandemica (ensino remoto e cancelamento de testes em SY 2019-20)
- **Features Mais Relevantes Identificadas:** Taxa de frequencia escolar (`attendance rates`) apontada como mais importante que infracoes e suspensoes; o uso de dados dos 2 anos anteriores conferiu maior robustez a falhas pontuais de coleta

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** N/A
- **Metricas Computacionais (ML):** Modelo Original (teste 2016): Overall Accuracy = 0,9130, NPV = 0,9502, Precision = 0,4812, Recall = 0,5057, F1-Score = 0,4931, AUC = 0,8902, Accuracy @ Top 3% = 0,6452, Accuracy @ Top 5% = 0,5622, Accuracy @ Top 100 = 0,83. Nos 3 cenarios de simulacao (Set to Zero, Mean, Median, Nearest Neighbor, Worst): AUC variou de 0,8683 a 0,8910 e Accuracy @ Top 3% de 0,6002 a 0,6524; sob imputacao "Worst" no Cenario 3, Recall subiu para 0,5965 com queda de Precision para 0,4135
- **Estrategia de Validacao:** Split temporal (treino SY 2007-2015; teste SY 2016) e simulacao de *concept drift* com 5 estrategias de imputacao em 3 cenarios
- **Desafios Metodologicos Relatados:** *Concept drift* por interrupcao pandemica (ausencia de notas padronizadas, alteracao no significado de frequencia e infracoes no ensino remoto); desbalanceamento de classes (tratado com over- e under-sampling); ausencia de rotulos reais pos-pandemia ($y_{t+1}$)
- **Aspectos Eticos e Transparencia (XAI):** Discussao sobre implicacoes sociopoliticas de predicoes imperfeitas, risco de estigma do rotulo "at-risk", necessidade de decisoes de baixo risco ("lower the stakes"), transparencia clara das limitacoes e auditoria de equidade entre subgrupos
- **Limitacoes Declaradas:** A simulacao modela apenas mudanca na distribuicao das features $P(X_{t+1}) \neq P(X_t)$ e assume fortemente que a relacao $P(Y|X)$ permaneceu inalterada durante a pandemia; resultados ligados a estrutura especifica dos dados de Rhode Island
- **Direcoes Futuras:** Quantificar incerteza sob mudanca em $P(Y|X)$, investigar praticas de modelagem que aumentem a robustez de EWS e validar desempenho por subgrupos com dados pos-pandemia

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo de propor um framework de simulacao por imputacao para avaliar o impacto de *concept drift* pandemico no EWS de evasao de Rhode Island. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha o modelo (`FastForest`/Random Forest), features, split temporal (2007-2015 vs. 2016), reamostragem, 3 cenarios e 5 estrategias de imputacao. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Accuracy, NPV, Precision, Recall, F1, AUC e metricas operacionais (Accuracy @ Top 3%, Top 5% e Top 100) para o baseline e todos os cenarios. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 0 | Nao contempla fatores psicologicos, socioemocionais ou de clima escolar; utiliza apenas registros administrativos (frequencia, disciplina, notas) e demograficos. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute explicitamente a premissa sobre invariancia de $P(Y|X)$, dependencia de contexto, risco de estigma, equidade entre subgrupos e implicacoes sociopoliticas. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **8 / 10** | |

---

---

## S0325: Re-envisioning a K-12 Early Warning System with School Climate Factors

> - **ID do Estudo:** `S0325`
> - **Autores:** Mengchen Su, Lukas A. Olson, Daniel C. Jarratt, Sashank Varma, Joseph A. Konstan, Rebecca J. L. Keller, Bodong Chen
> - **Ano:** 2022
> - **Veículo (Venue):** *Proceedings of the Ninth ACM Conference on Learning @ Scale*
> - **Base de Origem:** `ACM DL` (Bases: `['ACM DL']`)
> - **DOI:** [10.1145/3491140.3528670](https://doi.org/10.1145/3491140.3528670)
> - **URL:** [Link da Publicação](https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3491140.3528670)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
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

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Basico (K-12)
- **Faixa Etaria / Amostra ($N$):** Amostra combinada final: ~60.000 estudantes de 277 escolas (2019) e ~75.000 estudantes de 261 escolas (2021) em 17 distritos de Nevada (base SIS estadual ~500.000 alunos K-12; survey original: 62.000 alunos/738 escolas em 2019 e 48.900 alunos/754 escolas em 2021)
- **Publico-alvo Avaliado:** Estudantes K-12 de escolas publicas (integracao de clima escolar e aprendizagem socioemocional [SEL] em Early Warning System)
- **Fonte dos Dados / Dataset:** Nevada School Climate / Social Emotional Learning Survey (NV-SCSEL, AIR / Nevada Department of Education) integrado ao Student Information System (SIS) da Infinite Campus

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** Nevada School Climate / Social Emotional Learning Survey (NV-SCSEL), baseado no ED School Climate Survey (U.S. Department of Education)
- **Natureza da Ferramenta:** Questionario web validado de clima escolar e aprendizagem socioemocional (escores de 100 a 500 em 4 dominios: CLC, REL, EMO, PSAF)
- **Forma de Aplicacao:** Autorrelato dos estudantes via web, agregado em nivel escolar
- **Finalidade:** Mensuracao de percepcoes de clima escolar e SEL para melhoria institucional e integracao em EWS

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Analise Estatistica (Regressao Linear Multipla no nivel escolar para os resultados preliminares) como etapa inicial de projeto em andamento (*Work in Progress*) para integrar clima escolar/SEL ao Early_Warning_Systems da Infinite Campus com Machine Learning (Gradient-Boosted Decision Trees e SHAP)
- **Algoritmos Empregados:** Regressao Linear Multipla (executada); Early_Warning_Systems, Gradient-Boosted Decision Trees e Explicabilidade_XAI (SHAP) previstos para a etapa individual
- **Tarefa do Modelo:** Regressao no nivel escolar para explicar frequencia, atrasos, comportamento e GPA; classificacao binaria prevista para desfechos negativos de matricula (evasao, expulsao, retencao)
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (expansao do modelo ABC tradicional com clima escolar e SEL)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Aprendizagem Socioemocional (SEL), Seguranca Emocional (`EMO`), Relacionamentos (`REL`), Competencia Cultural e Linguistica (`CLC`) e Seguranca Fisica (`PSAF`)
- **Variaveis Comportamentais / Historico:** % de estudantes com faltas injustificadas ou desconhecidas (`pct unexcusedunknown`), % com atrasos (`pct tardy`), % com resolucoes comportamentais (`pct behaviorRes`), GPA acumulado medio (`avg cumGPA`)
- **Variaveis Familiares / Sociodemograficas:** % de estudantes do sexo masculino, % elegivel para almoco gratuito ou reduzido (proxy socioeconomico), % com ingles como lingua primaria
- **Variaveis Institucionais / Contextuais:** Clima escolar multidimensional agregado por escola (CLC, REL, EMO, PSAF)
- **Features Mais Relevantes Identificadas:** Todos os 4 dominios de clima escolar foram preditores significativos de atrasos e resolucoes comportamentais em 2019 e 2021 ($R^2_{change}$ entre 5% e 15% para atrasos). `Physical Safety (PSAF)` foi o preditor mais consistente de faltas injustificadas e GPA nos dois anos; `Emotional Safety (EMO)` apresentou $\beta = -0,11^{***}$ ($R^2_{change} = 0,15^{***}$) para atrasos e $\beta = 0,13^{***}$ para GPA em 2021

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** N/A (escala validada previamente pelo U.S. Dept. of Education/AIR, sem reporte de Alfa de Cronbach na amostra deste artigo)
- **Metricas Computacionais (ML):** Reporta coeficientes padronizados ($\beta$), $p$-valores e $R^2_{change}$ (0,02 a 0,15) das regressoes lineares escolares. Metricas de ML (Precision, Recall, AUC-ROC, SHAP) constam apenas no protocolo em andamento (Secao 2.3.2), ainda sem resultados publicados neste *Work in Progress*
- **Estrategia de Validacao:** Modelos transversais independentes para 2019 (N=277 escolas) e 2021 (N=261 escolas) apos *listwise deletion*; protocolo futuro preve holdout aleatorio de 20% para modelos de ML
- **Desafios Metodologicos Relatados:** Grande perda amostral por dados faltantes ao cruzar o survey NV-SCSEL com o SIS; possivel interferencia da pandemia de COVID-19 nos padroes de 2021; analise preliminar restrita ao nivel escolar agregado
- **Aspectos Eticos e Transparencia (XAI):** Enfase em equidade racial e atendimento integral ao estudante ("whole child"); preve aplicacao de valores SHAP (Explicabilidade_XAI) na etapa de ML
- **Limitacoes Declaradas:** Elevada proporcao de dados faltantes apos juncao das bases; apenas um ano pandemico disponivel (2021); risco de baixa validade externa/generalizacao estadual; achados atuais limitados ao nivel da escola e nao ao nivel individual
- **Direcoes Futuras:** Integrar os fatores de clima escolar e SEL no EWS individual em producao da Infinite Campus com Gradient-Boosted Decision Trees e SHAP

---

### 4. Avaliacao de Qualidade Metodologica (QA)
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

---

## S0198: A Machine Learning Approach to Classifying School Absenteeism Patterns in Youth with ADHD

> - **ID do Estudo:** `S0198`
> - **Autores:** Patrick K. Goh, Maria A. Rogers, Ashlyn A. W. W. A. Wong, Grace S. Mellor, Jess Whitley, J. David Smith, Natasha McBrearty, Natasha Tatartcheff-Quesnel, George J. DuPaul
> - **Ano:** 2026
> - **Veículo (Venue):** *SCHOOL MENTAL HEALTH*
> - **Base de Origem:** `Web of Science` (Bases: `['Web of Science', 'Springer Link']`)
> - **DOI:** [10.1007/s12310-026-09893-z](https://doi.org/10.1007/s12310-026-09893-z)
> - **URL:** Não informado
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0198`
- **Titulo Completo:** A Machine Learning Approach to Classifying School Absenteeism Patterns in Youth with ADHD
- **Autores:** Patrick K. Goh, Maria A. Rogers, Ashlyn A. W. W. A. Wong, Grace S. Mellor, Jess Whitley, J. David Smith, Natasha McBrearty, Natasha Tatartcheff-Quesnel, George J. DuPaul
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** SCHOOL MENTAL HEALTH
- **DOI:** [10.1007/s12310-026-09893-z](https://doi.org/10.1007/s12310-026-09893-z)
- **Base de Dados:** Web of Science
- **Pais/Regiao de Realizacao do Estudo:** Canada

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Criancas e Adolescentes, 4-17 anos)
- **Faixa Etaria / Amostra ($N$):** N = 194 jovens com diagnostico de TDAH encaminhados clinicamente (idade 4-17 anos; M = 10,7 anos, DP = 2,98; 77,3% meninos, 21,1% meninas, 1,5% transgenero ou outro; 56% / n = 108 com historico de absenteismo e n = 86 sem historico)
- **Publico-alvo Avaliado:** Jovens com TDAH em atendimento ambulatorial avaliados para classificacao de historico de absenteismo escolar
- **Fonte dos Dados / Dataset:** Questionario clinico de admissao preenchido por pais/cuidadores entre 2018 e 2020 em uma agencia comunitaria de saude mental infantil localizada em grande cidade canadense

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** Questionario institucional de admissao clinica composto por item binario de historico de absenteismo, checklist de 69 areas problematicas biopsicossocioeducacionais em 8 dominios (Kuder-Richardson 20 = 0,80) e 15 itens de historico diagnostico (totalizando 80 preditores analisados apos exclusao de itens sem variancia)
- **Natureza da Ferramenta:** Checklist clinico de triagem biopsicossocioeducacional (respostas binarias sim/nao)
- **Forma de Aplicacao:** Relato dos pais/cuidadores junto a assistente de caso clinico na admissao ambulatorial
- **Finalidade:** Triagem inicial e estratificacao atuarial do risco de absenteismo escolar em jovens com TDAH

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Machine Learning Supervisionado (Ensemble Learning) com ranqueamento de importancia de variaveis
- **Algoritmos Empregados:** Random_Forest (1.000 arvores, ajuste de `mtry` entre 2 e 80 via pacote `caret` no R 4.3.2; comparacao tentada com Regressao Logistica, que nao convergiu)
- **Tarefa do Modelo:** Classificacao binaria (com vs. sem historico de absenteismo escolar), avaliada com limiar padrao (0,50) e limiar ajustado para alta sensibilidade (0,42)
- **Estagio de Deteccao:** Triagem atuarial / alerta precoce prospectivo (embora modelado sobre historico retrospectivo de absenteismo)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Humor ou pensamentos depressivos, humor ansioso, transtornos comorbidos (ansiedade 43,3%, transtorno desafiador opositivo 34,0%, depressao 13,9%, TEA 13,9%, TOC 8,2%, transtorno de apego 5,2%, transtorno de conduta 4,1%) e isolamento social
- **Variaveis Comportamentais / Historico:** Comportamento disruptivo/interferente na escola e em casa, vulnerabilidade a comportamentos de risco, dificuldades de aprendizagem, vitimizacao/bullying e historico de absenteismo
- **Variaveis Familiares / Sociodemograficas:** Parentalidade inconsistente, incapacidade da familia de atender as necessidades do jovem, dinamicas familiares, idade, genero e identidade cultural
- **Variaveis Institucionais / Contextuais:** Dificuldades de acesso a servicos comunitarios e problemas escolares (nao incluiu variaveis sistemicas como clima escolar ou transporte)
- **Features Mais Relevantes Identificadas:** Top 6 preditores com escore de importancia > 50 (escala 0-100 por permutacao): (1) comportamento interferente na escola, (2) humor ou pensamentos depressivos, (3) comportamento interferente em casa, (4) parentalidade inconsistente, (5) transtorno de apego e (6) vulnerabilidade a comportamentos de risco; idade e genero nao aumentaram o desempenho (delta AUC = 0,002, p = 0,95)

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Kuder-Richardson 20 (KR-20) = 0,80 para o checklist de 69 areas problematicas
- **Metricas Computacionais (ML):** Validacao cruzada no treino (n = 131): AUC = 0,75 (DP = 0,08), Acuracia = 0,69 (vs. No Information Rate 0,56, p < 0,001), Sensibilidade = 0,68, Especificidade = 0,70, Kappa = 0,38. Amostra de teste independente (n = 63): AUC = 0,79 (IC 95% [0,68, 0,90]); com threshold 0,50: Acuracia = 0,73 (p = 0,003), Sensibilidade = 0,76 (Tabela 3) / 0,74 (texto), Especificidade = 0,69 (Tabela 3) / 0,71 (texto), Kappa = 0,46; com threshold 0,42: Sensibilidade = 0,80, Especificidade = 0,57, Acuracia = 0,70
- **Estrategia de Validacao:** Split aleatorio estratificado 67% treino (n = 131) / 33% teste independente (n = 63) e validacao cruzada 5-fold repetida 5 vezes no treino
- **Desafios Metodologicos Relatados:** Tamanho amostral relativamente reduzido para ML (N = 194), nao convergencia da regressao logistica com elevado numero de preditores, ausencia de definicao operacional formal de absenteismo no item de entrada e respostas binarias que limitam granularidade
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao por IRB e consentimento informado; codigo em R disponivel no Open Science Framework (OSF); interpretabilidade via escores de importancia de variaveis por permutacao
- **Limitacoes Declaradas:** Amostra clinica pequena e predominantemente masculina (77,3% meninos), restringindo generalizacao para amostras comunitarias ou meninas; dados transversais e retrospectivos baseados apenas no relato dos pais/cuidadores sem confirmacao clinica independente dos diagnosticos; ausencia de fatores sistemicos (qualidade da escola, clima escolar, transporte)
- **Direcoes Futuras:** Validar prospectivamente em amostras maiores, mais diversas e comunitarias; incorporar dados multi-informantes e fatores sistemicos escolares; avaliar utilidade incremental e viabilidade em fluxos reais de clinicas e escolas

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo e quatro hipoteses explicitamente definidos para classificacao de absenteismo em jovens com TDAH via Random Forest. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Amostra (N = 194), instrumento (KR-20 = 0,80), split estratificado 67/33, 5x5-fold CV, 1.000 arvores e ajuste de `mtry` descritos de forma replicavel (codigo no OSF). |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta KR-20 = 0,80, AUC-ROC (0,75 CV / 0,79 teste), Acuracia, Sensibilidade, Especificidade, Kappa e VPP/VPN. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa 80 variaveis biopsicossocioeducacionais e diagnosticos comorbidos, identificando depressao, comportamento disruptivo, parentalidade inconsistente e apego. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute detalhadamente vies do relato parental unico, amostra clinica masculina, natureza transversal/retrospectiva e ausencia de fatores sistemicos. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **10 / 10** | |

---

---

## S0191: Medical expert system as a chatbot for screening of anxiety disorders in children and adolescents

> - **ID do Estudo:** `S0191`
> - **Autores:** Venkateshwar Rao Madasu, Mohammadreza Hajiarbabi
> - **Ano:** 2026
> - **Veículo (Venue):** *Journal of Medical Artificial Intelligence*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.21037/jmai-24-366](https://doi.org/10.21037/jmai-24-366)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105030280295?origin=resultslist)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0191`
- **Titulo Completo:** Medical expert system as a chatbot for screening of anxiety disorders in children and adolescents
- **Autores:** Venkateshwar Rao Madasu, Mohammadreza Hajiarbabi
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Journal of Medical Artificial Intelligence
- **DOI:** [10.21037/jmai-24-366](https://doi.org/10.21037/jmai-24-366)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (Purdue University Fort Wayne, IN)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Criancas e Adolescentes, 6-18 anos)
- **Faixa Etaria / Amostra ($N$):** N = 100 participantes no estudo experimental (70 pais de criancas/adolescentes de 6-18 anos, idade media 41,5 anos, DP = 7,2, 65% mulheres; 30 profissionais de saude - pediatras, conselheiros escolares e psicologos infantis, idade media 38,1 anos, DP = 5,8, 70% mulheres)
- **Publico-alvo Avaliado:** Rastreio e identificacao preliminar de transtornos de ansiedade e evitacao escolar em criancas e adolescentes (6-18 anos)
- **Fonte dos Dados / Dataset:** Dados experimentais anonimizados coletados via interface web do chatbot administrando o questionario SCARED (41 itens) e pesquisa pos-interacao de aceitacao/usabilidade

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** SCARED (Screen for Child Anxiety Related Disorders - 41 itens, versao autorrelato e relato dos pais)
- **Natureza da Ferramenta:** Ferramenta digitalizada / Questionario de triagem psicometrica integrado a chatbot especialista
- **Forma de Aplicacao:** Autorrelato do aluno ou relato dos pais via interface conversacional web 24/7
- **Finalidade:** Triagem inicial / identificacao preliminar de sintomas em 5 categorias de ansiedade, incluindo evitacao escolar significativa (School Avoidance)

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Sistema Especialista Baseado em Regras (Medical Expert System) / Chatbot Conversacional
- **Algoritmos Empregados:** Motor de inferencia por encadeamento para frente (Forward Chaining), modelagem de conhecimento via BPMN (Business Process Model and Notation) convertida em AIML (Artificial Intelligence Markup Language) por modelo de estados finitos
- **Tarefa do Modelo:** Classificacao multiclasse baseada em regras e limiares clinicos (somatorio de respostas 0/1/2 do SCARED para Panico >=7, Ansiedade Generalizada >=9, Separacao >=5, Fobia Social >=8 e Evitacao Escolar >=3)
- **Estagio de Deteccao:** Alerta precoce / triagem preventiva preliminar 24/7 para encaminhamento a avaliacao clinica especializada

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Sintomas de transtorno de panico/somaticos (13 itens), ansiedade generalizada (9 itens), ansiedade de separacao (8 itens), fobia social (7 itens) e evitacao escolar significativa (4 itens)
- **Variaveis Comportamentais / Historico:** Respostas somaticas e evitativas associadas a escola (ex.: dores de cabeca na escola, medo de dormir fora de casa, evitacao de pessoas desconhecidas)
- **Variaveis Familiares / Sociodemograficas:** Perspectiva parental (versao para pais do SCARED), idade/genero dos avaliadores e experiencia previa com interfaces digitais
- **Variaveis Institucionais / Contextuais:** Contexto de paises de baixa e media renda (LMICs) e ambientes com escassez de profissionais especializados em saude mental infantil
- **Features Mais Relevantes Identificadas:** Subescala de Evitacao Escolar do SCARED (itens 2, 11, 17 e 36 com limiar de corte >= 3) e demais 4 subescalas de ansiedade

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Concordancia com os criterios padronizados de pontuacao do SCARED (92% para ansiedade generalizada e 89% para transtorno de panico; categorizacao correta nas 5 dimensoes incluindo evitacao escolar)
- **Metricas Computacionais (ML):** Taxa de concordancia com pontuacao esperada do SCARED (89% a 92% reportados) e avaliacao de aceitacao/usabilidade (85% consideraram intuitivo e facil de usar; 90% satisfeitos com o processo e feedback)
- **Estrategia de Validacao:** Estudo experimental com N = 100 participantes (70 pais e 30 profissionais de saude) recrutados em centro comunitario e convites online, comparando saidas do chatbot aos criterios do SCARED
- **Desafios Metodologicos Relatados:** Manutencao de contexto em conversas multi-turno, gerenciamento de dialogo para entradas ambiguas, representacao de conhecimento sem dependencia de engenheiros de IA e adaptabilidade linguistica/cultural
- **Aspectos Eticos e Transparencia (XAI):** Alta transparencia por raciocinio explicito baseado em regras (BPMN-AIML); discussao aprofundada sobre privacidade (GDPR/HIPAA), consentimento parental para menores, risco de sobrediagnostico, medicalizacao de comportamento normal e sobrecarga do sistema de saude
- **Limitacoes Declaradas:** Identificacao apenas preliminar (nao substitui diagnostico clinico); dependencia da precisao do relato do usuario; necessidade de adaptacao linguistica e cultural; dados empiricos limitados (amostra de 100 participantes)
- **Direcoes Futuras:** Integrar algoritmos de ML e NLP/NLU para compreensao de linguagem natural, decisoes sensiveis ao contexto clinico, integracao com IoT/wearables e aprendizado continuo da base de conhecimento

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo claro de desenvolver e avaliar um chatbot especialista BPMN-AIML baseado no SCARED para triagem de ansiedade e evitacao escolar. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Arquitetura BPMN-AIML, 41 regras do SCARED, limiares de corte e desenho experimental (N = 100, criterios de inclusao/exclusao) descritos de forma replicavel. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Apresenta concordancia (92% ansiedade generalizada, 89% panico) e usabilidade (85%/90%), mas nao reporta validacao clinica contra diagnostico padrao-ouro nem metricas individuais para evitacao escolar. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Incorpora diretamente a dimensao de evitacao escolar significativa e 4 transtornos de ansiedade do SCARED, alem de fatores de acesso e estigma. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Apresentam secao dedicada a limitacoes e consideracoes eticas (vies de autorrelato, sobrediagnostico, adaptacao cultural, amostra limitada). |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | |

---

---

## S0283: Predicting School Dropout and Simulating Educational Scenarios in Colombia Using Machine Learning

> - **ID do Estudo:** `S0283`
> - **Autores:** Mairely Narvaez Fernandez, Fernando Rafael Morales Nuñez, Ruthber Rodrȷguez Serrezuela, Daniel Felipe Bermeo Cuenca
> - **Ano:** 2025
> - **Veículo (Venue):** *2025 IEEE VIII Congreso Internacional en Inteligencia Ambiental, Ingenieria de Software y Salud Electronica y Movil (AmITIC)*
> - **Base de Origem:** `IEEE Xplore` (Bases: `['IEEE Xplore']`)
> - **DOI:** [10.1109/AmITIC68284.2025.11214605](https://doi.org/10.1109/AmITIC68284.2025.11214605)
> - **URL:** Não informado
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0283`
- **Titulo Completo:** Predicting School Dropout and Simulating Educational Scenarios in Colombia Using Machine Learning
- **Autores:** Mairely Narvaez Fernandez, Fernando Rafael Morales Nuñez, Ruthber Rodrȷguez Serrezuela, Daniel Felipe Bermeo Cuenca
- **Ano de Publicacao:** 2025
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** 2025 IEEE VIII Congreso Internacional en Inteligencia Ambiental, Ingenieria de Software y Salud Electronica y Movil (AmITIC)
- **DOI:** [10.1109/AmITIC68284.2025.11214605](https://doi.org/10.1109/AmITIC68284.2025.11214605)
- **Base de Dados:** IEEE Xplore
- **Pais/Regiao de Realizacao do Estudo:** Colombia (regiao rural do sul da Colombia / Huila)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica / Ensino Secundario (Colombia)
- **Faixa Etaria / Amostra ($N$):** N = 2.000 estudantes do ensino secundario (analise de fatores preditivos); validacao de campo piloto com N = 120 usuarios finais (gestores escolares, professores e assessores de politicas publicas)
- **Publico-alvo Avaliado:** Estudantes do ensino secundario em contextos socioeconomicos vulneraveis (predicao de risco de evasao escolar e simulacao de cenarios de intervencao)
- **Fonte dos Dados / Dataset:** Repositorios nacionais oficiais (Ministerio da Educacao da Colombia e Departamento Nacional de Estatistica) e instituicoes educacionais locais (nota: o texto menciona "hypothetical dataset" na Secao III-A para os 2.000 estudantes)

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** N/A (nao utiliza instrumento psicometrico padronizado)
- **Natureza da Ferramenta:** Registros administrativos/academicos e indicadores autorrelatados de saude mental (sem especificacao de escala clinica validada)
- **Forma de Aplicacao:** Registros institucionais e autorrelato dos alunos (para ansiedade e depressao)
- **Finalidade:** Triagem inicial de risco de evasao integrada a sistema de apoio a decisao

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Machine Learning Supervisionado + Simulacao de Cenarios baseada em Dinamica de Sistemas (System Dynamics), integrados na plataforma `EduAnalytics Huila` (Early_Warning_Systems)
- **Algoritmos Empregados:** Artificial Neural Networks (ANN), Support Vector Machines (SVM), Decision Trees (DT)
- **Tarefa do Modelo:** Classificacao binaria (risco de evasao escolar) combinada com simulacao dinamica do impacto de politicas educacionais
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (Early_Warning_Systems) e simulacao ex-ante de intervencoes

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Ansiedade ou depressao autorrelatadas (presentes em 42% dos casos de evasao, p < 0,01), perda de confianca e desmotivacao academica
- **Variaveis Comportamentais / Historico:** Baixo desempenho academico em matematica e leitura (72% dos evadidos, p < 0,001), Absenteismo_Cronico (>20% do ano letivo; 65% dos evadidos, p < 0,001), repetencia escolar
- **Variaveis Familiares / Sociodemograficas:** Baixo nivel socioeconomico / renda familiar / instabilidade habitacional (58% dos evadidos, p < 0,01), pais sem ensino medio completo (49% dos evadidos, p < 0,05)
- **Variaveis Institucionais / Contextuais:** Infraestrutura escolar, razao professor-aluno, acesso a subsidios educacionais, programas de apoio em saude mental e aconselhamento
- **Features Mais Relevantes Identificadas:** Baixo desempenho em matematica e leitura (72%), Absenteismo_Cronico >20% (65%), baixo nivel socioeconomico (58%), baixa escolaridade dos pais (49%) e ansiedade/depressao autorrelatada (42%)

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** N/A (nao aplicavel; sem validacao psicometrica de escalas)
- **Metricas Computacionais (ML):** ANN: Acuracia = 85,4%, F1-Score = 0,84, ROC-AUC = 0,88; SVM: Acuracia = 81,2%; Decision Trees: Acuracia = 77,3%. Validacao de campo (N=120): 91% facilidade de uso (p < 0,001), 88% melhoria na identificacao precoce (p < 0,001), 84% eficacia para intervencoes direcionadas (p < 0,01), 79% viabilidade em baixo recurso (p < 0,01), 87% valor para politicas publicas (p < 0,001)
- **Estrategia de Validacao:** Validacao cruzada estratificada (stratified cross-validation) e validacao piloto em campo via entrevistas e estudos de caso (N = 120)
- **Desafios Metodologicos Relatados:** Natureza multifatorial e nao linear da evasao, limitacoes de infraestrutura em escolas de baixos recursos, interpretabilidade para usuarios nao tecnicos
- **Aspectos Eticos e Transparencia (XAI):** Anonimizacao dos dados; interface visual exploratoria (mapas de calor de correlacao e histogramas) voltada a gestores sem formacao tecnica, embora nao empregue metodos formais de XAI (ex.: SHAP/LIME)
- **Limitacoes Declaradas:** Os autores nao apresentam secao dedicada a limitacoes; mencionam apenas menor profundidade analitica das Arvores de Decisao frente as ANNs e referem "hypothetical dataset" na Secao III-A sem detalhar hiperparametros ou divisao exata treino/teste
- **Direcoes Futuras:** Ampliar a adocao da plataforma para planejamento de politicas publicas e reformas educacionais abrangentes orientadas a equidade

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo de projetar e validar o sistema `EduAnalytics Huila` para predicao precoce de evasao escolar e simulacao de cenarios politicos na Colombia. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 1 | Descreve fontes, algoritmos (DT, SVM, ANN), validacao cruzada estratificada e amostras (N=2.000; N=120), mas omite hiperparametros/arquitetura da ANN, numero de folds e apresenta ambiguidade ao citar "hypothetical dataset" na Secao III-A. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta metricas claras de desempenho para os tres modelos (ANN: Acuracia 85,4%, F1 0,84, ROC-AUC 0,88; SVM: 81,2%; DT: 77,3%), alem de p-valores dos fatores e validacao de campo. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Analisa ansiedade/depressao autorrelatadas (42% dos evadidos, p < 0,01), motivacao, absenteismo cronico e fatores socioeconomicos/familiares, mas sem escalas psicometricas validadas. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 0 | Nao ha secao ou discussao explicita sobre limitacoes metodologicas, vieses dos dados, restricoes da amostra ou riscos de overfitting. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **6 / 10** | |

---

---

## S0104: Early detection of students’ mental health issues from a traditional daily health observation scheme in Japanese schools and its digitalization

> - **ID do Estudo:** `S0104`
> - **Autores:** Tomoko Nishimura, Manabu Wakuta, Yuko Osuka, Nobuaki Tsukui, Ikue Hirata, Michio Takahashi, Masaki Adachi, Taiichi Katayama, Kyoko Aizaki, Motofumi Sumiya, Sayaka Kawakami, Toshiki Iwabuchi, Atsushi Senju
> - **Ano:** 2024
> - **Veículo (Venue):** *Frontiers in Public Health*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.3389/fpubh.2024.1430011](https://doi.org/10.3389/fpubh.2024.1430011)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/85204796852?origin=resultslist)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0104`
- **Titulo Completo:** Early detection of students’ mental health issues from a traditional daily health observation scheme in Japanese schools and its digitalization
- **Autores:** Tomoko Nishimura, Manabu Wakuta, Yuko Osuka, Nobuaki Tsukui, Ikue Hirata, Michio Takahashi, Masaki Adachi, Taiichi Katayama, Kyoko Aizaki, Motofumi Sumiya, Sayaka Kawakami, Toshiki Iwabuchi, Atsushi Senju
- **Ano de Publicacao:** 2024
- **Tipo de Publicacao:** Periodico (Original Research)
- **Nome do Veiculo:** Frontiers in Public Health
- **DOI:** [10.3389/fpubh.2024.1430011](https://doi.org/10.3389/fpubh.2024.1430011)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Japao (cidade de porte medio no oeste do Japao; 5 escolas publicas)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Fundamental I, II e Junior High (1o ao 9o ano japones: 3 escolas primarias e 2 escolas secundarias)
- **Faixa Etaria / Amostra ($N$):** $N = 2.433$ alunos iniciais; $N = 2.143$ analisados apos exclusao de baixa taxa de resposta (1.241 do fundamental e 902 do junior high; 49,4% sexo feminino)
- **Publico-alvo Avaliado:** Estudantes da educacao basica publica monitorados ao longo de 76 dias letivos (setembro a dezembro de 2022) para predicao de sintomas depressivos/ansiosos e absenteismo escolar (*Futoukou*)
- **Fonte dos Dados / Dataset:** Aplicativo digital de observacao diaria de saude (*daily health observation*) via tablets do programa GIGA School, registros diarios de presenca pelos professores e questionarios psicometricos (PHQ-4 e JaSC)

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** *Daily Health Observation* digitalizado (8 itens fisicos/ritmo de vida + item emocional baseado em *Zones of Regulation*), *Patient Health Questionnaire-4* (PHQ-4: 2 itens PHQ-9 + 2 itens GAD-7) e *Japan School Climate Scale* (JaSC, 32 itens)
- **Natureza da Ferramenta:** Ferramenta digitalizada de triagem diaria longitudinal combinada com escalas psicometricas padronizadas
- **Forma de Aplicacao:** Autorrelato diario do aluno em tablet escolar e registro diario de faltas pelo professor regente
- **Finalidade:** Triagem inicial continua, deteccao precoce de sofrimento mental e monitoramento de risco de absenteismo/recusa escolar (*Futoukou*)

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Analise Estatistica Avancada Longitudinal, Modelagem de Trajetorias Baseada em Grupos (*Group-Based Trajectory Modeling* - GBTM com modelo *zero-inflated Poisson*) e Deteccao de Anomalias via *Rolling Z-Score* (janela movel de 7 dias) + Regressao Binomial Negativa Multinivel
- **Algoritmos Empregados:** Group-Based Trajectory Modeling (Stata `traj`, ZIP), Rolling Z-Score (limiar $z > +1$ para respostas incomuns), Regressao Binomial Negativa Multinivel
- **Tarefa do Modelo:** Clustering longitudinal de trajetoria (5 perfis de risco) + deteccao de anomalias diarias + predicao prospectiva de sintomas (PHQ-4) e dias de falta
- **Estagio de Deteccao:** Alerta precoce / monitoramento preventivo diario em ambiente escolar

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Sintomas somaticos (dor de estomago, dor de cabeca, nausea), fadiga, estados emocionais das 4 zonas (*Zones of Regulation*: feliz/calmo, cansado/ansioso/triste, irritado/tenso, frustrado/raiva/panico), sintomas depressivos e ansiosos (PHQ-4)
- **Variaveis Comportamentais / Historico:** Ritmo de vida/sono (dormir tarde, dificuldade de acordar, pular cafe da manha), numero total de dias de falta no periodo de 4 meses
- **Variaveis Familiares / Sociodemograficas:** Serie escolar (*grade*), genero e idioma principal falado (japones vs. nao-japones)
- **Variaveis Institucionais / Contextuais:** Clima escolar percebido em nivel individual e media da turma (seguranca, aprendizagem e relacoes interpessoais via JaSC)
- **Features Mais Relevantes Identificadas:** Pertencimento ao Grupo 5 de trajetoria cronica (5,4% dos alunos, 3-4 queixas diarias crescentes), media do escore diario de saude e contagem de respostas anomalas (*rolling z-score* $> +1$)

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Alfa de Cronbach = 0,71 para a estrutura unifatorial de 8 itens do *daily health issue*; analise fatorial exploratoria e confirmatoria (PHQ-4 tratado como 1 fator)
- **Metricas Computacionais (ML):** BIC = -95.746,63, SA-BIC = -95.713,37, Entropia = 0,900 (solucao otima de 5 grupos); *Incident Rate Ratio* (IRR): Grupo 5 apresentou IRR = 5,17 (IC 95%: 3,82-6,99) para depressao/ansiedade e IRR = 2,14 (IC 95%: 1,19-3,85) para dias de falta em relacao ao Grupo 1; Clima escolar (IRR = 0,58 para sintomas)
- **Estrategia de Validacao:** Ajuste longitudinal por BIC/SA-BIC, probabilidade posterior > 0,7, entropia e regressao multinivel ajustada por aluno e sala de aula (sem split treino/teste de ML classico)
- **Desafios Metodologicos Relatados:** Exclusao de 290 alunos (11,9%) com baixa taxa de resposta (<50% dos dias); maioria dos alunos com zero faltas (distribuicao altamente inflacionada de zeros)
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao em comite de etica, consentimento parental opt-out; os autores destacam que o *rolling z-score* e um algoritmo simples e transparente que permite aos professores explicar facilmente por que um alerta foi gerado, evitando dependencia cega de algoritmos
- **Limitacoes Declaradas:** Nao registrou os motivos especificos das faltas (doenca fisica vs. recusa escolar); amostra restrita a uma cidade japonesa; nao analisou separadamente fundamental vs. junior high nos modelos principais
- **Direcoes Futuras:** Integrar explicabilidade para professores, expandir validacao por faixa etaria/regiao e usar dados diarios para fortalecer alfabetizacao em saude mental dos estudantes

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo explicito de avaliar o valor preditivo da observacao diaria digitalizada para detectar depressao, ansiedade e absenteismo escolar. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Descreve amostra ($N=2.433$ / $2.143$), 76 dias letivos, itens, formulas (GBTM ZIP, *rolling z-score*) e covariaveis multinivel em Stata 17.0. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Alfa de Cronbach (0,71), BIC/SA-BIC, Entropia (0,900) e IRRs com IC 95% e p-valores. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Integra sintomas somaticos, emocoes (*Zones of Regulation*), sono, clima escolar (JaSC), PHQ-4 e dias de ausencia escolar. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 1 | Discute perda amostral (11,9%), ausencia do motivo das faltas e diferencas entre niveis escolares, embora sem validacao externa em outras regioes. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | Estudo empirico robusto e diretamente aplicavel a sistemas escolares de triagem diaria digital. |

---

---

## S0012: Artificial intelligence as decision support for adolescent depression and anxiety: a mini review of clinical utility, safety, and implementation

> - **ID do Estudo:** `S0012`
> - **Autores:** Xinyue Zhou, Lei Geng
> - **Ano:** 2026
> - **Veículo (Venue):** *Frontiers in Psychiatry*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.3389/fpsyt.2026.1910713](https://doi.org/10.3389/fpsyt.2026.1910713)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105048745161?origin=resultslist)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0012`
- **Titulo Completo:** Artificial intelligence as decision support for adolescent depression and anxiety: a mini review of clinical utility, safety, and implementation
- **Autores:** Xinyue Zhou, Lei Geng
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico (Mini Review)
- **Nome do Veiculo:** Frontiers in Psychiatry
- **DOI:** [10.3389/fpsyt.2026.1910713](https://doi.org/10.3389/fpsyt.2026.1910713)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Dinamarca e China (autores da Copenhagen Business School e Wuhan Mental Health Center; revisao narrativa internacional)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica / Adolescencia (faixa de risco ate 18 anos; destaque para pico de DALYs entre 15-19 anos)
- **Faixa Etaria / Amostra ($N$):** N/A (Mini Review narrativa sobre adolescentes com depressao e ansiedade; discute coortes como ABCD Study e amostras escolares/clinicas)
- **Publico-alvo Avaliado:** Adolescentes em risco ou em acompanhamento para depressao, ansiedade e problemas internalizantes (incluindo manifestacoes indiretas como recusa escolar / *school refusal*)
- **Fonte dos Dados / Dataset:** Revisao narrativa de literatura clinica, prontuarios eletronicos (EHR), fenotipagem digital (smartphones/wearables), coortes longitudinais (ex.: ABCD Study) e interfaces conversacionais (LLMs)

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** Menciona PHQ-9, GAD-7 e cuidado baseado em medicoes (*Measurement-Based Care* - MBC) com escalas padronizadas repetidas; nao aplica escala especifica de recusa escolar (como SRAS-R)
- **Natureza da Ferramenta:** Escalas clinicas padronizadas e questionarios digitais integrados a monitoramento continuo
- **Forma de Aplicacao:** Autorrelato do adolescente, relato dos pais e avaliacao clinica estruturada
- **Finalidade:** Triagem, monitoramento entre consultas, avaliacao de gravidade (PHQ-9/GAD-7) e suporte a decisao clinica

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Analise conceitual e revisao de modelos de Machine Learning preditivo prospectivo, Deep Learning multitarefa (NLP), Fenotipagem Digital (*digital phenotyping*) e Grandes Modelos de Linguagem (LLMs / agentes conversacionais)
- **Algoritmos Empregados:** N/A (estudo de revisao; discute modelos de predicao longitudinal, deep learning textual para PHQ-9/GAD-7, sensores moveis e chatbots baseados em LLMs)
- **Tarefa do Modelo:** Suporte a decisao clinica (*decision-first*): predicao prospectiva de risco/inicio, triagem, deteccao precoce de nao-resposta ao tratamento e escalonamento de seguranca
- **Estagio de Deteccao:** Alerta precoce / identificacao prospectiva e monitoramento continuo entre consultas (rejeita diagnostico autonomo)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Afeto negativo, sensibilidade a ameaca, desregulacao emocional, sintomas somaticos, disturbios do sono, irritabilidade, ideacao suicida/autolesao
- **Variaveis Comportamentais / Historico:** Recusa escolar (*school refusal*), queda de frequencia e rendimento academico, isolamento social, uso de chatbots de IA, padroes de atividade/sono via smartphone
- **Variaveis Familiares / Sociodemograficas:** Conflito familiar, acesso a cuidados de saude, idioma minoritario, alfabetizacao digital, posse de dispositivos e nivel socioeconomico
- **Variaveis Institucionais / Contextuais:** Contexto escolar, fluxos de encaminhamento escolar, capacidade de atendimento dos servicos clinicos e barreiras culturais
- **Features Mais Relevantes Identificadas:** Piora do sono, nao-frequencia escolar (*school non-attendance*), historico previo de ansiedade, estresse familiar e escalada recente de sintomas

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** N/A (nao reporta experimentos proprios; discute precisao de medicao e concordancia entre relato de pais e adolescentes)
- **Metricas Computacionais (ML):** Discute insuficiencia de AUC isolada; enfatiza calibracao (curva/inclinacao de calibracao), beneficio liquido (*net benefit* / *decision-curve analysis*) e taxas de falsos positivos/negativos em eventos de baixa prevalencia
- **Estrategia de Validacao:** Recomenda validacao externa prospectiva, avaliacao por subgrupos, comparadores realistas e diretrizes TRIPOD+AI, PROBAST+AI, CONSORT-AI, DECIDE-AI e CHART
- **Desafios Metodologicos Relatados:** Desenhos retrospectivos, amostras selecionadas, *outcome leakage* (modelos que preveem documentacao/encaminhamento em vez de adoecimento), baixa prevalencia base, falta de calibracao e fadiga de alertas
- **Aspectos Eticos e Transparencia (XAI):** Privacidade e consentimento/assentimento em adolescentes, risco de vigilancia intrusiva por sensores passivos, vies racial/socioeconomico de acesso, interpretabilidade acionavel para clinicos e proibicao de diagnostico/crise autonomos por LLMs
- **Limitacoes Declaradas:** Revisao narrativa (nao sistematica), focada em utilidade clinica, limites de seguranca e implementacao, sem sintese quantitativa exaustiva de algoritmos
- **Direcoes Futuras:** Desenvolver IA orientada a decisoes concretas (*decision-first*), testar prospectivamente em fluxos reais de cuidado, priorizar transportabilidade cultural e comprovar melhoria de desfechos clinicos

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o foco em utilidade clinica, seguranca e implementacao de IA como suporte a decisao em depressao e ansiedade na adolescencia. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 1 | Trata-se de uma Mini Review narrativa ("Literature was selected narratively"), sem protocolo sistematico replicavel ou experimento proprio. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 0 | Nao apresenta experimentos ou metricas empiricas proprias de validacao (apenas framework conceitual na Tabela 1). |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Cita recusa escolar e queda de frequencia como sinais precoces/features relevantes, mas o foco central e depressao e ansiedade clinicas. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Analise extensa e rigorosa sobre *outcome leakage*, calibracao, vies de acesso, privacidade em adolescentes, riscos de LLMs e transportabilidade. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **6 / 10** | Artigo conceitual/revisao forte para fundamentar XAI, etica e arquitetura *decision-first* na RSL. |

---

---

## S0204: Integrating Systemic and Analytic Approaches to School Attendance Problems: Synergistic Frameworks for Research and Policy Directions

> - **ID do Estudo:** `S0204`
> - **Autores:** Christopher A. Kearney
> - **Ano:** 2021
> - **Veículo (Venue):** *CHILD & YOUTH CARE FORUM*
> - **Base de Origem:** `Web of Science` (Bases: `['Web of Science', 'Springer Link']`)
> - **DOI:** [10.1007/s10566-020-09591-0](https://doi.org/10.1007/s10566-020-09591-0)
> - **URL:** Não informado
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0204`
- **Titulo Completo:** Integrating Systemic and Analytic Approaches to School Attendance Problems: Synergistic Frameworks for Research and Policy Directions
- **Autores:** Christopher A. Kearney
- **Ano de Publicacao:** 2021
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** CHILD & YOUTH CARE FORUM
- **DOI:** [10.1007/s10566-020-09591-0](https://doi.org/10.1007/s10566-020-09591-0)
- **Base de Dados:** Web of Science
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (University of Nevada, Las Vegas)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Pre-escola, Ensino Fundamental e Ensino Medio / K-12)
- **Faixa Etaria / Amostra ($N$):** N/A - Revisao integrativa teorica e metodologica abrangendo estudantes K-12 em multiplos estudos empiricos sintetizados
- **Publico-alvo Avaliado:** Criancas e adolescentes com problemas de frequencia escolar (absenteismo cronico, recusa escolar, truancy, retirada parental e exclusao escolar)
- **Fonte dos Dados / Dataset:** Literatura cientifica multidisciplinar de abordagens sistemicas e analiticas sobre frequencia e problemas de frequencia escolar

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** Sintetiza medidas especificas de avaliacao analitica por tipo, funcao e perfil sintomatico (ex.: avaliacao funcional, entrevistas estruturadas, checklists, observacoes diarias e triagens breves de ansiedade/depressao como RCADS-25)
- **Natureza da Ferramenta:** Framework heuristico integrando avaliacao sistemica (registros escolares, notas, clima) e avaliacao psicometrica/clinica de banda estreita
- **Forma de Aplicacao:** Multi-informante (autorrelato, pais, professores, registros administrativos e sistemas online de deteccao precoce)
- **Finalidade:** Integrar avaliacao somativa (politicas e programas) com avaliacao formativa/diagnostica (triagem individual e intervencao em MTSS)

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Early Warning System - EWS / Data Mining / Machine Learning Supervisionado e Nao Supervisionado integrados a cascatas desenvolvimentais e MTSS
- **Algoritmos Empregados:** Early_Warning_Systems, arvores de classificacao e regressao (CART), metodos Ensemble (CHAID), Random_Forest, Support Vector Machines (SVM), Boosting, LASSO, analise ROC, Latent Class Analysis (LCA) e Growth Mixture Modeling (revisados da literatura)
- **Tarefa do Modelo:** Classificacao de risco (absenteismo cronico e evasao), deteccao de sinais precoces de alerta e agrupamento de perfis/trajetorias (LCA)
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (EWS com dados multidimensionais em tempo real, dashboards e sinais individuais antes da cronificacao)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Ansiedade (separacao, social, teste/desempenho), depressao, afetividade negativa, queixas somaticas, baixa autoeficacia academica, isolamento social e funcoes de reforco da recusa escolar
- **Variaveis Comportamentais / Historico:** Padrao de faltas, atrasos, saidas antecipadas, comportamento disruptivo matinal, notas/reprovacoes, suspensoes, engajamento escolar e participacao extracurricular
- **Variaveis Familiares / Sociodemograficas:** Pobreza, inseguranca habitacional/alimentar, mobilidade residencial, conflito familiar, estilos parentais, escolaridade parental, transporte e raca/etnia
- **Variaveis Institucionais / Contextuais:** Clima escolar, seguranca, relacao professor-aluno, politicas disciplinares punitivas, racismo estrutural e niveis ecologicos de Bronfenbrenner (micro, meso, exo e macrossistema)
- **Features Mais Relevantes Identificadas:** Destaca modelo "ABC" (Attendance, Behavior, Course grades) enriquecido por variaveis domiciliares, clima escolar, seguranca, coesao familiar e sintomas internalizantes identificados em estudos de ML/EWS

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Validade de construto e discriminante (critica a baixa validade de subtipos tradicionais de faltas justificadas/injustificadas e do corte binario de 10%)
- **Metricas Computacionais (ML):** Discute sensibilidade, especificidade e analise ROC/AUC como essenciais para evitar classificacoes erroneas em EWS
- **Estrategia de Validacao:** Revisao integrativa teorico-conceitual em 5 dominios (construtos, fatores influenciadores, trajetorias, mensuracao e intercessao)
- **Desafios Metodologicos Relatados:** Inconsistencia de definicoes e limiares entre jurisdicoes, manipulacao/gaming de dados de frequencia, sobrecarga de conselheiros escolares, instabilidade de indicadores entre subgrupos e desconexao entre EWS e intervencoes
- **Aspectos Eticos e Transparencia (XAI):** Defende uso nao punitivo de dados, protecao de privacidade no compartilhamento interagencias, equidade para estudantes marginalizados e desagregacao de dados
- **Limitacoes Declaradas:** Propoe heuristicas integrativas sem validacao empirica direta no estudo; aponta ausencia de dados qualitativos nos sistemas atuais e barreiras estruturais de implementacao nas escolas
- **Direcoes Futuras:** Desenvolver sistemas integrados interagencias em tempo real com dashboards, incorporar triagens psicometricas breves de ansiedade/depressao sem onerar escolas e vincular predicoes diretamente a intervencoes em MTSS

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo claro de propor heuristicas integrativas entre abordagens sistemicas e analiticas em 5 dominios centrais. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 1 | Revisao integrativa extensa e bem organizada nos 5 dominios, mas sem protocolo sistematico de busca ou criterios de selecao descritos. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Discute sensibilidade, especificidade e ROC/AUC conceitualmente a partir da literatura, sem apresentar metricas empiricas proprias. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analise aprofundada de fatores emocionais (ansiedade, depressao, funcoes da recusa escolar), familiares e ecologicos. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute criticamente limitacoes de EWS tradicionais, vieses de limiares binarios, manipulacao de dados e barreiras de implementacao. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **8 / 10** | |

---

---

## S0206: Translating sophisticated data analytic strategies regarding school attendance and absenteeism into targeted educational policy

> - **ID do Estudo:** `S0206`
> - **Autores:** Christopher A. Kearney, Joshua Childs
> - **Ano:** 2023
> - **Veículo (Venue):** *IMPROVING SCHOOLS*
> - **Base de Origem:** `Web of Science` (Bases: `['Web of Science']`)
> - **DOI:** [10.1177/13654802231174986](https://doi.org/10.1177/13654802231174986)
> - **URL:** Não informado
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0206`
- **Titulo Completo:** Translating sophisticated data analytic strategies regarding school attendance and absenteeism into targeted educational policy
- **Autores:** Christopher A. Kearney, Joshua Childs
- **Ano de Publicacao:** 2023
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** IMPROVING SCHOOLS
- **DOI:** [10.1177/13654802231174986](https://doi.org/10.1177/13654802231174986)
- **Base de Dados:** Web of Science
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (University of Nevada, Las Vegas; University of Texas at Austin)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (K-12)
- **Faixa Etaria / Amostra ($N$):** N/A - Artigo de revisao/sintese metodologica e de politicas educacionais abrangendo estudantes K-12 em grandes bases analisadas nos estudos revisados
- **Publico-alvo Avaliado:** Estudantes K-12 em risco de absenteismo cronico e evasao escolar, com enfase em subgrupos vulneraveis e politicas educacionais locais
- **Fonte dos Dados / Dataset:** Sintese de estudos baseados em grandes conjuntos de dados educacionais distritais, estaduais e nacionais (EUA, Suecia, Coreia do Sul, Australia, entre outros)

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** N/A (Foca em dados administrativos desagregados, pesquisas de clima escolar e indicadores socioemocionais, nao em um instrumento psicometrico especifico)
- **Natureza da Ferramenta:** Sistemas de dados analiticos educacionais e levantamentos contextuais locais
- **Forma de Aplicacao:** Registros escolares longitudinais, entrevistas qualitativas com equipe escolar e questionarios de clima/fatores de risco
- **Finalidade:** Analise de causa raiz (Root Cause Analysis), aprimoramento de EWS e direcionamento de politicas locais e MTSS

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Machine Learning Supervisionado, Ensemble Learning, Early Warning System - EWS e Modelagem Estatistica Avancada
- **Algoritmos Empregados:** Abordagens baseadas em algoritmos: CART, Ensemble Analysis (CHAID), SVM, Boosting, LASSO, ROC Analysis, Random_Forest; abordagens baseadas em modelos: Multilevel Modeling, SEM, Latent Class Analysis (LCA) e Meta-analytic Modeling; aplicados a Early_Warning_Systems
- **Tarefa do Modelo:** Classificacao de risco de absenteismo cronico e evasao, segmentacao de perfis/subgrupos e identificacao de causas raiz locais
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (EWS desagregado e adaptado a condicoes locais, integrado a Tiers 1, 2 e 3 de MTSS)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Sintomas internalizantes, problemas de saude mental, disturbio emocional grave, comportamento externalizante e aprendizagem socioemocional (SEL)
- **Variaveis Comportamentais / Historico:** Faltas nao autorizadas, atrasos, saidas antecipadas, GPA, historico de suspensoes/expulsoes, reprovacao, participacao extracurricular e engajamento escolar
- **Variaveis Familiares / Sociodemograficas:** Pobreza/baixa renda, inseguranca habitacional e alimentar, violencia na vizinhanca, escolaridade parental, familia monoparental, raca/etnia, status de migrante e elegibilidade a IEP/educacao especial
- **Variaveis Institucionais / Contextuais:** Clima escolar, seguranca na escola, rotatividade docente, transporte escolar, politicas punitivas de tolerancia zero e mobilidade/mudancas de escola
- **Features Mais Relevantes Identificadas:** Variam conforme localidade e severidade: GPA baixo, suspensoes, idade avancada para a serie, mudanca de escola, inseguranca habitacional/alimentar, clima escolar negativo, sintomas internalizantes/externalizantes e participacao extracurricular

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Tamanhos de efeito em modelagem meta-analitica e indices de ajuste em SEM (citados dos estudos sintetizados)
- **Metricas Computacionais (ML):** Menciona uso de curvas ROC/AUC e desempenho diferencial (ex.: Random Forest prevendo melhor nao-evasao do que evasao), sem tabela comparativa de metricas numericas proprias
- **Estrategia de Validacao:** Revisao narrativa/sintese de estudos empiricos baseados em algoritmos e modelos aplicados a politicas educacionais
- **Desafios Metodologicos Relatados:** Distorcao por uso de dados agregados (perda de variacao individual e mascaramento de disparidades), baixa qualidade e manipulacao de registros de faltas, arbitrariedade do limiar de 10% e instabilidade de indicadores entre subgrupos e series
- **Aspectos Eticos e Transparencia (XAI):** Enfase em interseccionalidade, reducao de politicas punitivas desproporcionais contra grupos minoritarios, uso de dados desagregados para equidade e traducao transparente para formuladores de politicas
- **Limitacoes Declaradas:** Dificuldade de implementacao de estrategias analiticas sofisticadas em escolas com restricoes orcamentarias; transformacoes recentes (ensino hibrido/virtual pos-pandemia, crises climaticas) que exigem novas definicoes e metricas de frequencia
- **Direcoes Futuras:** Integrar sistemas interagencias em tempo real com dashboards acessiveis, combinar dados quantitativos e qualitativos, calibrar limiares empiricos locais para MTSS e investigar impactos do ensino virtual/hibrido

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo claro de sintetizar estrategias analiticas baseadas em algoritmos e modelos para traduzir em politicas educacionais, EWS e MTSS. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 1 | Organizacao clara entre metodos algoritmo-baseados e modelo-baseados, porem revisao narrativa sem protocolo sistematico de busca/selecao. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Cita aplicacoes de ROC/AUC e modelos sintetizados, sem apresentar benchmark quantitativo comparativo proprio. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa amplamente fatores socioemocionais, clima escolar, pobreza, saude mental e mecanismos contextuais do absenteismo. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute criticamente limitacoes de dados agregados, manipulacao de registros, vieses em politicas punitivas e desafios pos-pandemia. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **8 / 10** | |

---

---


---

# Parte II — Eixo Psicometrico, Redes e Fatores Socioemocionais (12 estudos)

## S0735: Validation of the School Refusal Assessment Scale-Revised (SRAS-R) in the General Adolescent Population in China

> - **ID do Estudo:** `S0735`
> - **Autores:** Yanqiu Yu, Juliet Honglei Chen, Joseph T. F. Lau, Anise M. S. Wu, Mengni Du, Yu Chen, Bingru Chen, Mingxuan Du, Guohua Zhang, Debora Baofeng Wang, Dajin Du
> - **Ano:** 2024
> - **Veículo (Venue):** *School Mental Health*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1007/s12310-024-09647-9](https://doi.org/10.1007/s12310-024-09647-9)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1007/s12310-024-09647-9)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0735`
- **Titulo Completo:** Validation of the School Refusal Assessment Scale-Revised (SRAS-R) in the General Adolescent Population in China
- **Autores:** Yanqiu Yu, Juliet Honglei Chen, Joseph T. F. Lau, Anise M. S. Wu, Mengni Du, Yu Chen, Bingru Chen, Mingxuan Du, Guohua Zhang, Debora Baofeng Wang, Dajin Du
- **Ano de Publicacao:** 2024
- **Tipo de Publicacao:** Artigo de Periódico
- **Nome do Veiculo:** School Mental Health
- **DOI:** [10.1007/s12310-024-09647-9](https://doi.org/10.1007/s12310-024-09647-9)
- **Base de Dados:** Springer Link
- **Pais/Regiao de Realizacao do Estudo:** China (cidade de Taizhou, Província de Zhejiang)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (Ensino Fundamental II, Ensino Médio regular e Ensino Médio vocacional; 12 a 19 anos)
- **Faixa Etaria / Amostra ($N$):** N = 1.108 estudantes selecionados aleatoriamente (14,7%) de 7.556 questionários elegíveis (de 8.285 coletados em 9 escolas secundárias); M_idade = 15,1 +- 1,5 anos (12-19 anos); 56,5% masculino, 42,4% feminino (1,1% faltante); 53,1% junior middle school, 27,9% senior middle school, 19,0% vocational high school. Split aleatório em EFA (n = 536) e CFA (n = 572).
- **Publico-alvo Avaliado:** Adolescentes da população escolar geral na China.
- **Fonte dos Dados / Dataset:** Inquérito transversal anônimo realizado entre fevereiro e março de 2022 em 9 escolas secundárias selecionadas por conveniência (5 junior middle, 3 senior middle e 1 vocational school).

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** SRAS-R (School Refusal Assessment Scale-Revised; versão chinesa validada com 21 itens e 5 fatores, além da versão abreviada de 4 fatores SRAS-R-A para amostras não clínicas), PHQ-9 (sintomas depressivos) e item único de preferência por não ir à escola.
- **Natureza da Ferramenta:** Escala psicométrica funcional tradicional adaptada culturalmente para o chinês.
- **Forma de Aplicacao:** Autorrelato do aluno (escala Likert de 7 pontos: 1 = nunca a 7 = sempre), aplicado sem a presença de professores.
- **Finalidade:** Avaliação das funções e condições motivacionais do comportamento de recusa escolar (SRB) em população adolescente geral.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Análise Estatística Avançada / Psicometria (CFA com estimador MLR em Mplus 7.0; split-half com EFA Principal Axis Factoring + Direct Oblimin e CFA; MGCFA para invariância de medida). Sem Machine Learning.
- **Algoritmos Empregados:** N/A (EFA, CFA com MLR e MGCFA).
- **Tarefa do Modelo:** Validação fatorial, invariância de medida (configural, métrica e escalar) por sexo e tipo de escola, análise de efeitos piso/teto e validade concorrente.
- **Estagio de Deteccao:** Triagem e avaliação preventiva em população escolar geral.

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** 5 fatores da SRAS-R chinesa: F1 Evitar emoções negativas na escola (5 itens), F2 Busca de reforço fora da escola (4 itens), F3 Absenteísmo frequente para reduzir problemas psicossociais (4 itens), F4 Condições que aumentariam motivação para ir à escola (3 itens), F5 Preferência por ficar com a família (5 itens); sintomas depressivos (PHQ-9, alfa = 0,88).
- **Variaveis Comportamentais / Historico:** Preferência por não ir à escola (escala 1-5) e frequência de absenteísmo autorrelatada no Fator 3.
- **Variaveis Familiares / Sociodemograficas:** Idade, sexo, residência permanente (83,2%) e família monoparental (9,9%).
- **Variaveis Institucionais / Contextuais:** Tipo de escola (junior middle, senior middle, vocational high school) e contexto cultural confucionista (elevada pressão acadêmica no senior middle school para exame de admissão universitário).
- **Features Mais Relevantes Identificadas:** O modelo original de 4 fatores (24 itens) não se ajustou (CFI = 0,71; TLI = 0,67; RMSEA = 0,08; SRMR = 0,11). A remoção dos itens 16, 19 e 22 (<0,40) gerou modelo de 5 fatores (21 itens, 68,8% da variância), confirmado na CFA (chi2/df = 2,39; CFI = 0,92; TLI = 0,90; RMSEA = 0,05; SRMR = 0,07) e invariante por sexo e tipo de escola (Delta CFI <= 0,01). Todos os 5 fatores correlacionaram-se com depressão (r = 0,27 a 0,63; p < 0,001, destaque para F1 r = 0,63) e 4 fatores com preferência por não ir à escola (r = 0,14 a 0,27; p < 0,001). Alunos do senior middle school apresentaram escores significativamente maiores nos 5 fatores (p < 0,001).

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Alfas de Cronbach: F1 = 0,85, F2 = 0,82, F3 = 0,79, F4 = 0,82, F5 = 0,83; PHQ-9 = 0,88. Efeito piso elevado apenas no Fator 3 (79,6% no escore mínimo, esperado em amostra não clínica); sem efeito teto (0,1% a 6,2%). Ajuste CFA 5 fatores: CFI = 0,92, TLI = 0,90, RMSEA = 0,05, SRMR = 0,07; versão abreviada de 4 fatores (SRAS-R-A): CFI = 0,93, TLI = 0,91, RMSEA = 0,06, SRMR = 0,07.
- **Metricas Computacionais (ML):** N/A.
- **Estrategia de Validacao:** Validação cruzada split-half (EFA n = 536 / CFA n = 572) e MGCFA para invariância por sexo e tipo de escola.
- **Desafios Metodologicos Relatados:** Inadequação da estrutura original de 4 fatores na população geral chinesa; efeito piso acentuado no Fator 3 (79,6%) em amostra comunitária; exclusão de 3 itens (16, 19 e 22) por baixa carga fatorial.
- **Aspectos Eticos e Transparencia (XAI):** Aprovação do Comitê de Ética Médica do Affiliated Wenzhou Kangning Hospital (KNLL-20211011002), aplicação anônima sem professores na sala e consentimento parental via opt-out.
- **Limitacoes Declaradas:** Viés de desejabilidade social em autorrelato; amostragem por conveniência em uma única cidade chinesa; ausência de confiabilidade teste-reteste, validade convergente/divergente ampla e medida objetiva de absenteísmo real.
- **Direcoes Futuras:** Validar a versão chinesa em amostras clínicas e em outras regiões/países; avaliar confiabilidade teste-reteste e relação com absenteísmo efetivo e problemas internalizantes/externalizantes.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo de validar a SRAS-R na população adolescente geral chinesa, incluindo invariância e validade concorrente. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Descreve triagem de qualidade de 8.285 para 7.556 e amostra aleatória de 1.108 alunos, painel de tradução, split-half EFA/CFA e MGCFA. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta CFI, TLI, RMSEA, SRMR, alfas de Cronbach, efeitos piso/teto, invariância e correlações de validade concorrente. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa funções motivacionais de SRB, associação com depressão (PHQ-9), diferenças por sexo e estresse escolar por tipo de escola. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute desejabilidade social, amostragem por conveniência, falta de teste-reteste e ausência de medida objetiva de faltas escolares. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **10 / 10** | Validação psicométrica abrangente e replicável da SRAS-R chinesa, com forte suporte estatístico e discussão crítica de limitações. |

---

---

## S0561: School refusal evaluation scale: factorial invariance and latent means differences across gender and age in Spanish adolescents

> - **ID do Estudo:** `S0561`
> - **Autores:** María Pérez-Marco, Andrea Fuster, Aitana Fernández-Sogorb, Carolina Gonzálvez
> - **Ano:** 2026
> - **Veículo (Venue):** *Current Psychology*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1007/s12144-025-08993-4](https://doi.org/10.1007/s12144-025-08993-4)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1007/s12144-025-08993-4)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0561`
- **Titulo Completo:** School refusal evaluation scale: factorial invariance and latent means differences across gender and age in Spanish adolescents
- **Autores:** María Pérez-Marco, Andrea Fuster, Aitana Fernández-Sogorb, Carolina Gonzálvez
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Artigo de Periódico
- **Nome do Veiculo:** Current Psychology
- **DOI:** [10.1007/s12144-025-08993-4](https://doi.org/10.1007/s12144-025-08993-4)
- **Base de Dados:** Springer Link
- **Pais/Regiao de Realizacao do Estudo:** Espanha (Província de Alicante)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (Ensino Secundário, adolescentes de 13 a 16 anos)
- **Faixa Etaria / Amostra ($N$):** N = 681 estudantes (50,2% meninos), idade entre 13 e 16 anos (M = 14,14; DP = 1,31), selecionados por amostragem aleatória por conglomerados em 4 escolas secundárias (6 casos atípicos excluídos por distância de Mahalanobis nas análises multivariadas).
- **Publico-alvo Avaliado:** Adolescentes espanhóis da população escolar geral (amostra comunitária).
- **Fonte dos Dados / Dataset:** Questionário digital aplicado via Google Forms presencialmente durante o horário escolar em escolas urbanas (58,30%), suburbanas (26,63%) e rurais (15,07%).

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** SCREEN (School Refusal Evaluation Scale; versão espanhola refinada de 12 itens e 4 fatores, derivada dos 18 itens originais de Gallé-Tessonneau & Gana, 2019). A escala SRAS-R é apenas discutida teoricamente como contraste conceitual.
- **Natureza da Ferramenta:** Escala psicométrica tradicional digitalizada (Google Forms), fundamentada em teorias do apego, regulação emocional e processamento de informação social.
- **Forma de Aplicacao:** Autorrelato do aluno (escala Likert de 5 pontos).
- **Finalidade:** Triagem inicial e avaliação multidimensional de manifestações emocionais, relacionais e de evitação da recusa escolar.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Análise Estatística Avançada / Psicometria (EFA com eixos principais e rotação Varimax em 25% da amostra; CFA com Máxima Verossimilhança e bootstrap de 5.000 reamostragens; Análise Fatorial Confirmatória Multigrupo - MGCFA no SPSS 26.0 e AMOS). Sem Machine Learning.
- **Algoritmos Empregados:** N/A (EFA, CFA com bootstrap e MGCFA).
- **Tarefa do Modelo:** Validação fatorial (comparação de 4 modelos concorrentes), invariância de medida (configural, métrica, escalar e estrita) e comparação de médias latentes por gênero e idade.
- **Estagio de Deteccao:** Triagem preventiva em população escolar comunitária.

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** 4 dimensões da SCREEN espanhola (3 itens por fator): FI Antecipação ansiosa (emoções negativas antes de ir à escola), FII Transição difícil casa-escola (separação da família/zona de segurança), FIII Desconforto interpessoal nas relações escolares (relações com pares e autopercepção) e FIV Evitação escolar (absenteísmo e queixas somáticas).
- **Variaveis Comportamentais / Historico:** Comportamentos de evitação escolar e absenteísmo capturados pelo Fator IV.
- **Variaveis Familiares / Sociodemograficas:** Gênero, idade (13, 14, 15 e 16 anos), nacionalidade (80,61% espanhóis) e escolaridade paterna.
- **Variaveis Institucionais / Contextuais:** Localização da escola (urbana, suburbana, rural) e transição escolar para o ensino secundário.
- **Features Mais Relevantes Identificadas:** FII Transição difícil foi o fator mais prevalente (M = 6,07; DP = 3,53), seguido por FIII Desconforto interpessoal (M = 4,46; DP = 3,05). Na comparação de médias latentes, meninas pontuaram significativamente mais alto que meninos em FIII Desconforto interpessoal (z = 6,09; F = 18,20, p < 0,001; d = 0,47). Não houve diferenças significativas por idade.

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Modelo M3 (4 fatores correlacionados, 12 itens) com ajuste excelente: chi2/df = 2,83, RMSEA = 0,052 (IC 90%: 0,042-0,062), CFI = 0,949, TLI = 0,930, SRMR = 0,043. Consistência interna: FI (alfa = 0,74; ômega = 0,74), FII (alfa = 0,73; ômega = 0,74), FIII (alfa = 0,71; ômega = 0,73), FIV (alfa = 0,73; ômega = 0,73). Correlações entre fatores e escore total significativas (r = 0,64 a 0,77). Invariância configural, métrica e escalar confirmadas por gênero e idade (Delta CFI <= 0,01; Delta RMSEA <= 0,015); invariância estrita parcial.
- **Metricas Computacionais (ML):** N/A.
- **Estrategia de Validacao:** EFA em 25% aleatórios da amostra, CFA na amostra total com 5.000 reamostragens bootstrap e MGCFA por gênero e 4 faixas etárias.
- **Desafios Metodologicos Relatados:** Eliminação de 6 itens da versão original (2, 4, 9, 11, 14 e 15) por cargas cruzadas ou baixa correlação item-total (<0,30) associadas a redação negativa ou sobreposição conceitual; ausência de normalidade multivariada tratada com bootstrap.
- **Aspectos Eticos e Transparencia (XAI):** Aprovação ética universitária, conformidade com a Declaração de Helsinki, consentimento escrito dos pais e participação voluntária e anônima.
- **Limitacoes Declaradas:** Viés inerente ao autorrelato; generalização limitada por ser amostra comunitária regional (sem amostra clínica com problemas formais de frequência); ausência de estudo piloto ou entrevistas cognitivas prévias devido a restrições administrativas escolares.
- **Direcoes Futuras:** Replicar o estudo em amostras clínicas ou com problemas de assiduidade reconhecidos; conduzir estudo piloto e entrevistas cognitivas; desenvolver instrumentos com abordagem ecológica abrangendo escola, família e pares.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo geral, 4 objetivos secundários e 5 hipóteses formais para validação da SCREEN na Espanha. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Emprega amostragem aleatória por conglomerados (N = 681), tradução pelas diretrizes ITC (2017), EFA, CFA com bootstrap e MGCFA detalhada. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta CFI, TLI, RMSEA, SRMR, AIC, BIC, alfa de Cronbach, ômega de McDonald e índices completos de invariância fatorial. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa dimensões emocionais, transição/apego, desconforto interpessoal e diferenças de gênero com interpretação sociocultural. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute viés de autorrelato, uso de amostra comunitária sem grupo clínico e ausência de estudo piloto/entrevistas cognitivas. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **10 / 10** | Validação psicométrica de alta qualidade metodológica, com excelente ajuste fatorial e comprovação de invariância por gênero e idade. |

---

---

## S0567: Assessing School Refusal: Arabic Adaptation and Psychometric Properties of the School Refusal Evaluation (SCREEN) from Adolescents in Algeria

> - **ID do Estudo:** `S0567`
> - **Autores:** Nedjem Eddine Boudouda, Malika Elafri, Amira Hamel, Fadila Nabti, Kamel Gana
> - **Ano:** 2024
> - **Veículo (Venue):** *School Mental Health*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1007/s12310-024-09636-y](https://doi.org/10.1007/s12310-024-09636-y)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1007/s12310-024-09636-y)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0567`
- **Titulo Completo:** Assessing School Refusal: Arabic Adaptation and Psychometric Properties of the School Refusal Evaluation (SCREEN) from Adolescents in Algeria
- **Autores:** Nedjem Eddine Boudouda, Malika Elafri, Amira Hamel, Fadila Nabti, Kamel Gana
- **Ano de Publicacao:** 2024
- **Tipo de Publicacao:** Artigo de Periódico
- **Nome do Veiculo:** School Mental Health
- **DOI:** [10.1007/s12310-024-09636-y](https://doi.org/10.1007/s12310-024-09636-y)
- **Base de Dados:** Springer Link
- **Pais/Regiao de Realizacao do Estudo:** Argélia (escolas de ensino médio em cidades de porte médio)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (Ensino Fundamental II / Middle School, 12 a 16 anos)
- **Faixa Etaria / Amostra ($N$):** Duas amostras comunitárias independentes: Estudo 1 (N = 658 adolescentes, 350 meninas e 308 meninos; M = 13,83, DP = 1,2 anos) e Estudo 2 (N = 485 adolescentes, 248 meninas e 237 meninos; M = 14,4, DP = 0,89 anos), dividido aleatoriamente em EFA (n = 243) e CFA de validação cruzada (n = 242). Pré-teste com grupo focal de 34 adolescentes (12-16 anos).
- **Publico-alvo Avaliado:** Adolescentes argelinos da população escolar geral (12-16 anos).
- **Fonte dos Dados / Dataset:** Questionários em papel e digitais (Google Form) aplicados em escolas de ensino médio na Argélia (Estudo 2 em cinco escolas de duas cidades).

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** SCREEN (School Refusal Evaluation Scale, adaptação árabe de 18 itens com estrutura final de 3 fatores), SCARED (41 itens) e GAD-7 (7 itens) para validade convergente.
- **Natureza da Ferramenta:** Escala psicométrica tradicional adaptada transculturalmente (diretrizes ITC 2017) e aplicada em papel e formato digital.
- **Forma de Aplicacao:** Autorrelato do aluno (escala Likert de 5 pontos).
- **Finalidade:** Triagem inicial e avaliação clínica/pesquisa da recusa escolar ansiosa em adolescentes árabes.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Análise Estatística Avançada / Psicometria (CFA com estimador MLR no Estudo 1; EFA com critérios VSS/MAP/BIC + CFA de validação cruzada com MLR no Estudo 2, utilizando pacotes `lavaan` e `psych` em R). Sem Machine Learning.
- **Algoritmos Empregados:** N/A (Análise Fatorial Exploratória e Confirmatória).
- **Tarefa do Modelo:** Adaptação transcultural, validação da estrutura fatorial (comparação entre modelo de 4 fatores, 2a ordem, bifatorial e 3 fatores), confiabilidade e validade convergente.
- **Estagio de Deteccao:** Triagem preventiva em população escolar comunitária.

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Dimensões da SCREEN árabe (3 fatores): F1 Antecipação ansiosa (7 itens), F2 Transição difícil (5 itens), F3 Desconforto interpessoal (6 itens); sintomas de ansiedade infantil via SCARED (pânico/somático, ansiedade generalizada, ansiedade de separação, fobia social, fobia escolar) e ansiedade generalizada (GAD-7).
- **Variaveis Comportamentais / Historico:** Evitação escolar (subescala da SCARED e itens da SCREEN).
- **Variaveis Familiares / Sociodemograficas:** Idade (12-16 anos) e sexo.
- **Variaveis Institucionais / Contextuais:** Contexto escolar e cultural argelino (adaptação linguística para o mundo árabe).
- **Features Mais Relevantes Identificadas:** O modelo original de 4 fatores não apresentou ajuste aceitável no Estudo 1 (CFI = 0,855; TLI = 0,828; RMSEA = 0,075; SRMR = 0,061) devido a cargas negativas nos itens reversos 14 e 15. Após reformulação positiva desses itens no Estudo 2, emergiu solução de 3 fatores (44% da variância explicada na EFA), confirmada na CFA após correlação de erros entre itens 1-5 e 12-16 (CFI = 0,909; TLI = 0,891; RMSEA = 0,063; SRMR = 0,068). Correlações positivas e significativas do escore total da SCREEN com fobia escolar da SCARED (r = 0,54; p < 0,001) e ansiedade generalizada (r = 0,56; p < 0,001).

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Estudo 1: alfa total = 0,89 (fatores: 0,81; 0,81; 0,62; 0,72). Estudo 2: alfa total = 0,85 e ômega de Raykov = 0,86; F1 Antecipação ansiosa (alfa = 0,831; ômega = 0,844), F2 Transição difícil (alfa = 0,792; ômega = 0,797), F3 Desconforto interpessoal (alfa = 0,667; ômega = 0,672). Validade convergente com SCARED (r = 0,54 e r = 0,56, p < 0,001).
- **Metricas Computacionais (ML):** N/A.
- **Estrategia de Validacao:** Validação em duas etapas com amostras independentes (Estudo 1: N = 658; Estudo 2: N = 485 com split aleatório em EFA n = 243 e CFA n = 242).
- **Desafios Metodologicos Relatados:** Violação da normalidade multivariada (Mardia = 110,18), requerendo estimador MLR; problemas de compreensão com itens reversos (14 e 15); cargas fatoriais baixas nos itens 1 (0,348) e 5 (0,374) e confiabilidade limítrofe em F3 Desconforto interpessoal (alfa = 0,667); TLI abaixo de 0,90 (0,891) mesmo após correlação de erros.
- **Aspectos Eticos e Transparencia (XAI):** Aprovação ética institucional, conformidade com a Declaração de Helsinki (1964), consentimento informado das famílias e escolas e assentimento dos estudantes.
- **Limitacoes Declaradas:** Ausência de amostra clínica (apenas amostra comunitária); necessidade de validação cruzada em outros países árabes; não avaliação de confiabilidade teste-reteste, validade concorrente clínica, ponto de corte diagnóstico e sensibilidade a intervenções.
- **Direcoes Futuras:** Replicar em amostras clínicas e em outros países árabes; estabelecer pontos de corte clínicos; avaliar teste-reteste, validade concorrente e sensibilidade a intervenções terapêuticas.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo de adaptar e validar a SCREEN para o árabe em dois estudos complementares. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Descreve tradução pelas diretrizes ITC com grupo focal/entrevista cognitiva, duas amostras independentes (N=658 e N=485), split EFA/CFA e estimador MLR. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta alfa de Cronbach, ômega de Raykov, CFI, TLI, RMSEA, SRMR e correlações convergentes com SCARED. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Analisa antecipação ansiosa, transição, desconforto interpessoal e associação com ansiedade (SCARED), mas não aprofunda outros fatores contextuais/familiares ou depressão. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute ausência de amostra clínica, falta de ponto de corte diagnóstico, ausência de teste-reteste e limitações de generalização regional. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | Adaptação transcultural rigorosa em duas etapas, com validade estrutural trifatorial e convergente bem documentadas. |

---

---

## S0555: Network analysis of school refusal behavior and internalizing and externalizing problems among Chinese adolescents

> - **ID do Estudo:** `S0555`
> - **Autores:** Chaoqun Dong, Xinnan Mao, Haiyan Hu, Jiankang He, Gaoyang Liu, Wendan Chen, Chengjia Zhao, Liping Yang, Jingjing Zhang, Guohua Zhang
> - **Ano:** 2026
> - **Veículo (Venue):** *BMC Psychology*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1186/s40359-026-04494-6](https://doi.org/10.1186/s40359-026-04494-6)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1186/s40359-026-04494-6)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0555`
- **Titulo Completo:** Network analysis of school refusal behavior and internalizing and externalizing problems among Chinese adolescents
- **Autores:** Chaoqun Dong, Xinnan Mao, Haiyan Hu, Jiankang He, Gaoyang Liu, Wendan Chen, Chengjia Zhao, Liping Yang, Jingjing Zhang, Guohua Zhang
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Artigo de Periódico
- **Nome do Veiculo:** BMC Psychology
- **DOI:** [10.1186/s40359-026-04494-6](https://doi.org/10.1186/s40359-026-04494-6)
- **Base de Dados:** Springer Link
- **Pais/Regiao de Realizacao do Estudo:** China (Wenzhou e Lishui, Província de Zhejiang)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (Adolescentes de 12 a 18 anos)
- **Faixa Etaria / Amostra ($N$):** N = 303 adolescentes com comportamento de recusa escolar (SRB), de 324 recrutados inicialmente (21 excluídos por respostas incompletas; taxa de resposta de 93,5%); M_idade = 14,80 anos (DP = 1,71); 73,9% feminino (n = 224) e 26,1% masculino (n = 79).
- **Publico-alvo Avaliado:** Adolescentes em atendimento psiquiátrico que atendem aos critérios clínicos de Berg (1997) para Comportamento de Recusa Escolar (SRB).
- **Fonte dos Dados / Dataset:** Questionários impressos anônimos aplicados por amostragem de conveniência em dois hospitais psiquiátricos de Zhejiang, China.

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** SRAS-R (versão chinesa de 21 itens e 5 dimensões validada por Yu et al., 2024), GAD-7 (ansiedade), PHQ-9 (sintomas depressivos), ANSSIAQ (autolesão não suicida - NSSI), AIS (Athens Insomnia Scale - insônia) e YDQ (Young Diagnostic Questionnaire - adição à internet).
- **Natureza da Ferramenta:** Escala psicométrica tradicional de recusa escolar (SRAS-R) combinada a escalas clínicas validadas para problemas internalizantes e externalizantes.
- **Forma de Aplicacao:** Autorrelato do aluno (questionário em papel aplicado sob condições padronizadas, sem interferência dos pais).
- **Finalidade:** Avaliação clínica multidimensional das funções do SRB e mapeamento da comorbidade com sintomas internalizantes e externalizantes.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Analise_de_Redes Psicológicas / Análise Estatística Avançada (Gaussian Graphical Model - GGM regularizado por `EBICglasso` com gamma = 0,5, em R 4.4.2 pacotes `qgraph` e `bootnet`).
- **Algoritmos Empregados:** `EBICglasso` (LASSO gráfico com critério de informação bayesiano estendido), cálculo de Expected Influence (EI), Strength e Bridge Expected Influence (BEI), com validação via bootstrap não paramétrico e case-dropping (1.000 reamostragens).
- **Tarefa do Modelo:** Modelagem da estrutura de rede (11 nós, 55 arestas potenciais) para identificar sintomas centrais e sintomas-ponte entre as 5 dimensões da SRAS-R, problemas internalizantes e externalizantes.
- **Estagio de Deteccao:** Diagnóstico clínico / caracterização psicopatológica a posteriori (amostra clínica já apresentando SRB: 38,9% <=1 mês, 22,8% 1-6 meses, 18,2% 6-12 meses, 20,1% >=1 ano).

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** 5 dimensões da SRAS-R chinesa (SRB1: evitar emoções negativas na escola; SRB2: busca de reforço fora da escola; SRB3: absenteísmo frequente para reduzir problemas psicossociais; SRB4: condições que aumentariam motivação escolar; SRB5: preferência por ficar com a família), ansiedade (GAD-7), sintomas depressivos (PHQ-9) e insônia (AIS).
- **Variaveis Comportamentais / Historico:** Autolesão não suicida - comportamento e função (ANSSIAQ: NSSI1 e NSSI2), adição à internet (YDQ: IA), duração do SRB e situação de aprendizagem.
- **Variaveis Familiares / Sociodemograficas:** Idade, gênero, residência (68,6% urbana, 31,4% rural), estrutura familiar, presença de irmãos, escolaridade dos pais.
- **Variaveis Institucionais / Contextuais:** Não modeladas diretamente na rede (apenas residência urbano/rural no questionário demográfico).
- **Features Mais Relevantes Identificadas:** Das 55 arestas possíveis, 33 (60,0%) foram não nulas (peso médio = 0,07). Arestas inter-comunidade mais fortes: DE-NSSI1 (0,21), AN-SRB1 (0,17) e DE-SRB1 (0,14). Nós mais centrais: Sintomas depressivos (DE: EI = 1,30; Strength = 1,49) e Evitar emoções negativas na escola (SRB1: EI = 1,19; Strength = 1,08). Principais nós-ponte (BEI): DE (1,16), Ansiedade - AN (1,02), Insônia - IN (0,57) e SRB1 (0,42).

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Alfas de Cronbach na amostra: SRAS-R (0,86; 0,81; 0,85; 0,76; 0,86 nas 5 subescalas), GAD-7 (0,93), PHQ-9 (0,90), ANSSIAQ (0,89 comportamento; 0,76 função), AIS (0,84) e YDQ (0,73).
- **Metricas Computacionais (ML):** Coeficiente de estabilidade de correlação (CS-coefficient > 0,50 para índices de centralidade) e intervalos de confiança de 95% via bootstrap (1.000 reamostragens) para pesos das arestas e testes de diferença de EI.
- **Estrategia de Validacao:** Bootstrap não paramétrico e case-dropping bootstrap com 1.000 reamostragens (`bootnet`).
- **Desafios Metodologicos Relatados:** Tamanho amostral moderado (N = 303 para 66 parâmetros da rede), forte predominância feminina (73,9% vs. 26,1% masculino) e viés de memória retrospectivo.
- **Aspectos Eticos e Transparencia (XAI):** Aprovação pelo Comitê de Ética do Kangning Hospital Affiliated to Wenzhou Medical University (KNLL-20211011002), aderência à Declaração de Helsinki, consentimento escrito dos adolescentes e responsáveis legais e coleta anônima.
- **Limitacoes Declaradas:** Delineamento transversal (impede inferência causal); viés retrospectivo; amostra restrita a dois hospitais na China (generalização limitada); amostra moderada com desbalanceamento de gênero que limitou análises comparativas por sexo.
- **Direcoes Futuras:** Análises de rede longitudinais incorporando a duração do SRB para elucidar dinâmicas temporais e causais; amostras maiores e equilibradas por gênero; intervenções focadas em nós centrais e de ponte (depressão, ansiedade, insônia, evitação emocional na escola) e triagem de NSSI.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo de mapear a estrutura de rede entre SRB, problemas internalizantes e externalizantes e identificar nós centrais e de ponte. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha critérios de Berg, cálculo amostral para redes (66 parâmetros), escalas validadas, pacotes R e parametrização do `EBICglasso` (gamma = 0,5). |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta alfas de Cronbach de todos os instrumentos na amostra, matriz de pesos das arestas, EI, Strength, BEI e CS-coefficient > 0,50 com 1.000 bootstraps. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa detalhadamente a interconexão entre dimensões da SRAS-R, depressão, ansiedade, insônia, NSSI e adição à internet. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute transversalidade, viés retrospectivo, generalização regional/clínica e desbalanceamento de gênero na amostra. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **10 / 10** | Estudo metodologicamente rigoroso e transparente, com análise de rede estável e replicável em amostra clínica de adolescentes com SRB. |

---

---

## S0505: Developmental Differences in the Emotional and Behavioural Profiles of Emotionally Based School Avoidance (EBSA) in Children and Adolescents

> - **ID do Estudo:** `S0505`
> - **Autores:** Meliha Feyza Gök, Berrin Bilgiç, Celal Yeşilkaya, Serkan Turan, Caroline Bond
> - **Ano:** 2026
> - **Veículo (Venue):** *Psychiatric Quarterly*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1007/s11126-026-10299-y](https://doi.org/10.1007/s11126-026-10299-y)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1007/s11126-026-10299-y)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0505`
- **Titulo Completo:** Developmental Differences in the Emotional and Behavioural Profiles of Emotionally Based School Avoidance (EBSA) in Children and Adolescents
- **Autores:** Meliha Feyza Gök, Berrin Bilgiç, Celal Yeşilkaya, Serkan Turan, Caroline Bond
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Artigo de Periódico
- **Nome do Veiculo:** Psychiatric Quarterly
- **DOI:** [10.1007/s11126-026-10299-y](https://doi.org/10.1007/s11126-026-10299-y)
- **Base de Dados:** Springer Link
- **Pais/Regiao de Realizacao do Estudo:** Turquia (clínica ambulatorial urbana de psiquiatria infantil e adolescente)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educação Básica (Ensino Fundamental e Médio, 6 a 18 anos)
- **Faixa Etaria / Amostra ($N$):** N = 102 jovens com EBSA (de 124 triados; 22 excluídos por deficiência intelectual ou recusa), divididos em crianças (<12 anos: n = 40, M = 8,0 +- 1,8 anos, 50,0% feminino) e adolescentes (>=12 anos: n = 62, M = 15,3 +- 1,4 anos, 53,2% feminino). Nas regressões múltiplas (listwise deletion): n = 35 crianças e n = 49 adolescentes.
- **Publico-alvo Avaliado:** Crianças e adolescentes encaminhados clinicamente com EBSA (>=20 dias letivos acumulados de ausência, ~10% de absenteísmo crônico).
- **Fonte dos Dados / Dataset:** Amostra clínica ambulatorial consecutiva (2020-2024), entrevistas diagnósticas semiestruturadas (K-SADS-PL-DSM-5), formulários sociodemográficos e escalas psicométricas padronizadas.

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** SRAS-R (School Refusal Assessment Scale-Revised, escore total usado como índice contínuo de gravidade da EBSA), K-SADS-PL-DSM-5 (entrevista diagnóstica), RCADS (ansiedade e depressão), SNAP-IV (TDAH e sintomas opositivos), DERS (dificuldades de regulação emocional), SDQ (problemas emocionais e comportamentais) e CGI-S (gravidade clínica global).
- **Natureza da Ferramenta:** Escala psicométrica tradicional (SRAS-R) combinada a entrevista clínica semiestruturada e escalas clínicas validadas em turco.
- **Forma de Aplicacao:** Multi-informante: autorrelato do aluno, relato dos pais (RCADS pais, informações acadêmicas/sociodemográficas) e avaliação clínica por dois psiquiatras infantis e adolescentes.
- **Finalidade:** Avaliação clínica da carga sintomática/gravidade da EBSA e identificação de perfis emocionais e comportamentais por estágio desenvolvimental.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Análise Estatística Avancada (Regressão Linear Múltipla separada por grupo etário, testes t independentes e qui-quadrado no IBM SPSS 26.0; sem uso de Machine Learning).
- **Algoritmos Empregados:** N/A (Regressão Linear Múltipla com preditores especificados a priori).
- **Tarefa do Modelo:** Regressão (predição da gravidade da EBSA medida pelo escore total da SRAS-R em crianças e adolescentes).
- **Estagio de Deteccao:** Diagnóstico clínico / avaliação a posteriori (amostra clínica já apresentando >=20 dias acumulados de falta escolar).

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Ansiedade de separação (RCADS), ansiedade social, sintomas depressivos, dificuldades de regulação emocional (DERS, destaque para subescala Impulsividade), sintomas emocionais/comportamentais (SDQ), gravidade clínica global (CGI-S), comorbidades psiquiátricas (TDAH, Transtorno Desafiador Opositivo - ODD).
- **Variaveis Comportamentais / Historico:** Faltas escolares acumuladas (>=20 dias), duração da EBSA, desempenho acadêmico prévio, hiperatividade/desatenção (SDQ e SNAP-IV), comportamento opositor.
- **Variaveis Familiares / Sociodemograficas:** Idade, sexo, escolaridade materna e paterna (proxy socioeconômico), doença física crônica, uso de medicação psicotrópica.
- **Variaveis Institucionais / Contextuais:** Não coletadas (ausência de variáveis de clima escolar, relação professor-aluno e exposição a bullying declarada como limitação).
- **Features Mais Relevantes Identificadas:** Ansiedade de separação (RCADS-Child) foi significativamente maior em crianças (p = 0,004). No modelo infantil (R^2 = 0,47; p = 0,001): menor idade (beta = -0,34; p = 0,032) e menor CGI-S (beta = -0,41; p = 0,005) associaram-se a maior escore SRAS-R (efeito de mascaramento por psicopatologia global grave). No modelo adolescente (R^2 = 0,18; p = 0,029): menor hiperatividade/desatenção no SDQ (beta = -0,31; p = 0,036) associou-se a maior SRAS-R; DERS-Impulsividade (beta = 0,28; p = 0,057) e idade (beta = 0,26; p = 0,065) mostraram tendência positiva não significativa.

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Escore total da SRAS-R comparável entre grupos (94,3 +- 4,9 em crianças vs. 93,4 +- 5,0 em adolescentes, p = 0,429); instrumentos com confiabilidade e validade previamente estabelecidas em turco (sem reportar alfas na amostra atual).
- **Metricas Computacionais (ML):** N/A. Regressão linear: R^2 = 0,47, F(4, 30) = 6,74, p = 0,001 (crianças); R^2 = 0,18, F(3, 45) = 3,28, p = 0,029 (adolescentes), com coeficientes beta e IC 95%.
- **Estrategia de Validacao:** Verificação de pressupostos de linearidade, normalidade, homocedasticidade e multicolinearidade; sem validação cruzada ou grupo controle saudável.
- **Desafios Metodologicos Relatados:** Redução amostral por deleção listwise (n = 35 e n = 49); uso do escore total da SRAS-R (originalmente funcional) como índice de gravidade; menor sensibilidade da SRAS-R para recusa ligada à desregulação atencional/comportamental; impossibilidade de controlar estatisticamente o uso de psicotrópicos.
- **Aspectos Eticos e Transparencia (XAI):** Aprovação ética institucional (n. 2025/10-10) em conformidade com a Declaração de Helsinki e consentimento informado por escrito dos participantes e responsáveis.
- **Limitacoes Declaradas:** Delineamento transversal (impede inferência causal); ausência de grupo controle saudável; modelos separados por idade sem teste formal de interação; poder estatístico limitado nos subgrupos; viés de autorrelato/relato parental; ausência de variáveis do ambiente escolar; amostra restrita a faltas persistentes (>=20 dias) em centro clínico único.
- **Direcoes Futuras:** Estudos longitudinais multi-informantes para investigar trajetórias desenvolvimentais da EBSA e sua interação com família e escola; intervenções multicomponentes adaptadas à idade (apego/ansiedade de separação na infância; regulação emocional e atencional na adolescência).

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Define claramente o objetivo e hipóteses desenvolvimentais sobre perfis emocionais e comportamentais da EBSA em crianças vs. adolescentes. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Descreve fluxo completo de triagem (124 -> 102), critérios diagnósticos (K-SADS-PL-DSM-5), instrumentos validados e especificação a priori das regressões. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Reporta R^2, F, p e IC 95% das regressões, mas não apresenta consistência interna (alfa/ômega) na amostra atual nem validação cruzada/grupo controle. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa em profundidade ansiedade de separação, regulação emocional, impulsividade, TDAH, ODD e gravidade clínica na EBSA por faixa etária. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute amplamente delineamento transversal, ausência de controle, baixo poder nos subgrupos, psicotrópicos, centro único e ausência de variáveis escolares. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | Estudo clínico sólido sobre diferenças desenvolvimentais na EBSA, com limitações transversais e amostrais bem documentadas. |

---

---

## S0500: How is loneliness orientation implicated in the relationship between sleep problems, loneliness intensity, and school refusal in adolescents?

> - **ID do Estudo:** `S0500`
> - **Autores:** Isa OkajimaSetoka Hiruma
> - **Ano:** 2025
> - **Veículo (Venue):** *Sleep and Biological Rhythms*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1007/s41105-025-00586-9](https://doi.org/10.1007/s41105-025-00586-9)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1007/s41105-025-00586-9)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
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

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Medio (Senior High School - escolas publicas e privadas)
- **Faixa Etaria / Amostra ($N$):** Recrutados N = 168 estudantes; amostra final analisada N = 128 estudantes (52 meninos, 70 meninas [6 sem genero reportado na descr.]; idade media = 16,55 +- 0,64 anos; coleta entre nov-dez de 2023)
- **Publico-alvo Avaliado:** Adolescentes do ensino medio (relacao entre problemas de sono, intensidade/orientacao da solidao, sentimentos de recusa escolar e faltas)
- **Fonte dos Dados / Dataset:** Questionario presencial aplicado a estudantes de escolas publicas e privadas de Toquio (dados abertos disponiveis no Zenodo)

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** `Feeling of School-Avoidance Scale (FSAS)` (6 itens sobre aversao/evitacao escolar), `Loneliness Orientation Test (LOT)` (7 pares semanticos de -3 a +3, desenvolvido no estudo), `Three-Item Loneliness Scale (TILS)`, `Athens Insomnia Scale (AIS)` (8 itens, corte >=6), `Sleep Debt Index (SDI)` e `Circadian Energy Scale (CIRENS)` (2 itens)
- **Natureza da Ferramenta:** Bateria de escalas psicometricas tradicionais de autorrelato + registro de numero de dias ausentes desde abril de 2023
- **Forma de Aplicacao:** Autorrelato do aluno (levantamento presencial)
- **Finalidade:** Triagem e avaliacao psicometrica de sentimentos de recusa escolar, solidao (intensidade e orientacao) e disturbios do sono

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Analise Estatistica Avancada e Psicometria (Analise Fatorial Exploratoria [EFA], Analise Fatorial Confirmatoria [CFA], Modelos Lineares Generalizados [GLM Gamma e Poisson] e Clustering Hierarquico nao supervisionado pelo metodo de Ward). Nao emprega Machine Learning supervisionado preditivo
- **Algoritmos Empregados:** EFA, CFA, Modelos Lineares Generalizados (GLM Gamma com log-link e Poisson com log-link), Clustering Hierarquico (Ward)
- **Tarefa do Modelo:** Validacao fatorial (EFA/CFA), regressao explicativa (GLM para TILS, FSAS e numero de faltas) e agrupamento (clustering de perfis de solidao: LN, nLP, LP)
- **Estagio de Deteccao:** Triagem preventiva e analise de mecanismos etiologicos (sentimentos de evitacao escolar `FSAS` como antecedente do absenteismo e Recusa_Escolar)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Intensidade da solidao (`TILS`), orientacao a solidao (`LOT` - positiva vs. negativa), sentimentos de recusa/evitacao escolar (`FSAS`), sintomas de insonia (`AIS`), divida de sono (`SDI`), cronotipo (`CIRENS`)
- **Variaveis Comportamentais / Historico:** Numero de dias de ausencia escolar entre abril de 2023 e a data da pesquisa (media = 3,26 +- 0,48 dias)
- **Variaveis Familiares / Sociodemograficas:** Idade (16,55 +- 0,64 anos), sexo, rede escolar (publica e privada em Toquio)
- **Variaveis Institucionais / Contextuais:** Criterio institucional japones de recusa escolar (>=30 dias de ausencia anual nao causados por doenca ou dificuldade financeira)
- **Features Mais Relevantes Identificadas:** No GLM: intensidade da solidao (`TILS`, $\beta=0,13, p<0,001$) foi o principal preditor de sentimentos de recusa escolar (`FSAS`, $R^2=0,29$), junto a tendencia de insonia (`AIS`, $\beta=0,05, p=0,07$). Para o numero de faltas ($R^2=0,38$), os preditores significativos foram `FSAS` ($\beta=0,32, p<0,001$) e cronotipo vespertino (`CIRENS`, $\beta=0,13, p<0,05$). Nos clusters, o grupo com solidao e orientacao negativa (`LN`, 28%) apresentou maior divida de sono e vespertinidade que o grupo com orientacao positiva (`LP`, 22%)

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** `LOT`: Alfa de Cronbach = 0,94; Omega de McDonald = 0,94; CFA com bom ajuste ($\chi^2_{14}=16,58, p=0,28$, CFI = 0,99, RMSEA = 0,05); cargas fatoriais de 0,76 a 0,85 (64% de variancia explicada)
- **Metricas Computacionais (ML):** N/A (estudo estatistico/psicometrico; reporta Nagelkerke's $R^2$ = 0,12 [TILS], 0,29 [FSAS] e 0,38 [faltas], alem de Hedges' $g$ entre clusters)
- **Estrategia de Validacao:** Calculo previo de poder amostral ($1-\beta=0,80$, n minimo = 110); analise paralela + EFA/CFA para o LOT; validacao do numero de clusters via *silhouette*, *gap statistic* e `NbClust`
- **Desafios Metodologicos Relatados:** Delineamento transversal (sem inferencia causal), vies de selecao por incluir apenas alunos frequentes, baixa variancia explicada (~10%) para intensidade da solidao
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao do Comite de Etica da Tokyo Kasei University (Ita-E2023-16), consentimento informado (Declaracao de Helsinque) e disponibilizacao aberta dos dados no Zenodo
- **Limitacoes Declaradas:** Amostra relativamente pequena (N=128 analisados); amostra limitada ao ensino medio; inclusao apenas de estudantes que conseguiam comparecer a escola (excluindo casos ja afastados); impossibilidade de estabelecer causalidade; ausencia de validacao concorrente do LOT com construtos como resiliencia
- **Direcoes Futuras:** Estudar amostras do ensino fundamental II a universidade, incluir estudantes atualmente afastados da escola, e investigar a relacao da orientacao a solidao com resiliencia, autocrescimento e bem-estar

---

### 4. Avaliacao de Qualidade Metodologica (QA)
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

---

## S0120: Belongingness and School Refusal in Adolescents: Psychometric Validation and Identification of Risk Profiles

> - **ID do Estudo:** `S0120`
> - **Autores:** María Pérez-Marco, Carolina Gonzálvez, Andrea Fuster, Ángel Amat, Alba Lorenzo-Rumbo, Graciela Arráez-Vera
> - **Ano:** 2026
> - **Veículo (Venue):** *Behavioral Sciences*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.3390/bs16071225](https://doi.org/10.3390/bs16071225)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105045792956?origin=resultslist)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0120`
- **Titulo Completo:** Belongingness and School Refusal in Adolescents: Psychometric Validation and Identification of Risk Profiles
- **Autores:** María Pérez-Marco, Carolina Gonzálvez, Andrea Fuster, Ángel Amat, Alba Lorenzo-Rumbo, Graciela Arráez-Vera
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico (Artigo Original)
- **Nome do Veiculo:** Behavioral Sciences (16, 1225)
- **DOI:** [10.3390/bs16071225](https://doi.org/10.3390/bs16071225)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Espanha (Provincia de Alicante)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Ensino Secundario Obrigatorio e Pos-Obrigatorio)
- **Faixa Etaria / Amostra ($N$):** N = 690 adolescentes de 12 a 17 anos (Mage = 14,21; DP = 1,42; 50,4% meninos, 48,3% meninas, 1,3% outro genero), selecionados de 802 iniciais em 6 escolas secundarias (publicas e privadas) apos exclusoes e remocao de 7 outliers multivariados.
- **Publico-alvo Avaliado:** Adolescentes escolares avaliados quanto ao pertencimento social geral e risco de recusa escolar
- **Fonte dos Dados / Dataset:** Questionarios de autorrelato aplicados em sala de aula durante o horario escolar (predominantemente via Google Forms com resposta forcada, e versao impressa quando sem acesso digital).

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** General Belongingness Scale (GBS; Malone et al., 2012; versao espanhola de Checa & Oberst, 2022; 12 itens em 2 fatores: Acceptance/Inclusion e Rejection/Exclusion, Likert 0-6) e SCREEN (School Refusal Evaluation Scale; Gallé-Tessonneau & Gana, 2019; versao espanhola de Pérez-Marco et al., 2026; 18 itens em 4 fatores: Anxious anticipation, Difficult transition, Interpersonal discomfort, School avoidance, Likert 1-5).
- **Natureza da Ferramenta:** Instrumentos psicometricos tradicionais (escalas de autorrelato validadas).
- **Forma de Aplicacao:** Autorrelato do aluno em contexto escolar, anonimo e voluntario, com presenca de pesquisador.
- **Finalidade:** Validacao psicometrica e invariancia fatorial da GBS em adolescentes espanhois, validade convergente com recusa escolar (SCREEN) e identificacao de perfis socioemocionais de risco para intervencao preventiva.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Analise Estatistica Avancada / Modelagem Centrada na Pessoa (Latent Profile Analysis - LPA) e Modelagem de Equacoes Estruturais (CFA/MGCFA). Nao utiliza ML supervisionado.
- **Algoritmos Empregados:** Confirmatory Factor Analysis (CFA com Maximum Likelihood e bootstrap de 5000 reamostragens no AMOS 28), Multigroup CFA (MGCFA), Latent Profile Analysis (LPA no Mplus 8.10) e MANOVA com testes post hoc de Bonferroni (SPSS 28).
- **Tarefa do Modelo:** Clustering latente (identificacao de 4 perfis de pertencimento: Highly Excluded, Socially Disconnected, Mixed Belonging e Highly Included) e comparacao multivariada de escores de recusa escolar.
- **Estagio de Deteccao:** Triagem preventiva e identificacao precoce de perfis de vulnerabilidade socioemocional antes do agravamento da evitacao escolar (integracao sugerida em EWS escolares).

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Pertencimento geral (inclusao/aceitacao vs. exclusao/rejeicao), antecipacao ansiosa, transicao dificil, desconforto interpessoal, evitacao escolar, solidao e afeto negativo.
- **Variaveis Comportamentais / Historico:** Faltas/evitacao escolar autorrelatada (subescala School avoidance do SCREEN).
- **Variaveis Familiares / Sociodemograficas:** Idade (12-17 anos) e genero (meninos, meninas e outro genero).
- **Variaveis Institucionais / Contextuais:** Tipo de escola (publica e privada), distribuicao geografica em Alicante e discussao sobre clima escolar e vitimizacao por pares.
- **Features Mais Relevantes Identificadas:** O perfil Highly Excluded (17,2%; z_Inclusao = -1,05, z_Exclusao = 1,59) apresentou os maiores escores em todas as dimensoes da SCREEN, com destaque para Anxious anticipation (M = 3,58 vs. M = 1,03 no Highly Included; d = 1,15), Interpersonal discomfort (M = 5,82 vs. 3,81; d = 0,68) e School avoidance (M = 3,14 vs. 1,55; d = 0,69). Exclusao correlacionou-se positivamente com Anxious anticipation (r = 0,40, p < 0,001).

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** GBS CFA (M3): chi2/df = 2,953, RMSEA = 0,053 (IC 90%: 0,044-0,063), SRMR = 0,039, CFI = 0,958, TLI = 0,947, AIC = 206,491, BIC = 319,908. Confiabilidade GBS: Inclusion (alfa = 0,81, omega = 0,81, CR = 0,82); Exclusion (alfa = 0,78, omega = 0,78, CR = 0,79). Invariancia de genero: configural, metrica (Delta CFI = 0,003), escalar (Delta CFI = 0,009) e estrita parcial. SCREEN: alfa = 0,71-0,74, omega = 0,73-0,74. LPA (4 perfis): Entropia = 0,825, AIC = 3153,264, BIC = 3211,836, LRT/BLRT p < 0,001. MANOVA: Wilks' lambda = 0,83, F(3, 686) = 10,86, p < 0,001, eta_p2 = 0,06.
- **Metricas Computacionais (ML):** N/A.
- **Estrategia de Validacao:** Comparacao de 4 modelos fatoriais (M0-M3), analise classica de itens, MGCFA por genero, validade convergente via correlacoes de Pearson com SCREEN, selecao de modelo LPA via AIC/BIC/entropia/LRT/BLRT e tamanho minimo de cluster (>= 25).
- **Desafios Metodologicos Relatados:** Ausencia de normalidade multivariada (mitigada com bootstrap de 5000 reamostragens); remocao de 7 outliers multivariados (Mahalanobis); grupo nao binario (n = 9) insuficiente para MGCFA.
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao etica pela Universidade de Alicante (UA-2023-06-29-4), conformidade com Declaracao de Helsinki, consentimento informado dos pais e assentimento dos adolescentes, participacao anonima e voluntaria.
- **Limitacoes Declaradas:** Uso exclusivo de autorrelato; amostra de um unico contexto cultural (Alicante, Espanha); subgrupos reduzidos aos 17 anos; desenho transversal impede inferencias causais; exclusao de identidades de genero nao binarias na MGCFA; ausencia de abordagem mista (qualitativa).
- **Direcoes Futuras:** Estudos longitudinais e em outros paises de lingua espanhola; inclusao de amostras maiores com diversidade de genero; investigacao de vitimizacao por pares (bullying) como mediador/moderador; integracao da GBS em sistemas escolares de alerta precoce e programas de apoio entre pares.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Quatro objetivos explicitos e seis hipoteses claramente formuladas sobre validacao da GBS, invariancia de genero, validade convergente com SCREEN e perfis latentes. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Amostragem aleatoria por conglomerados multiestagio, tratamento de outliers (Mahalanobis), CFA com bootstrap, MGCFA e criterios completos de selecao na LPA. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Apresenta CFI, TLI, RMSEA, SRMR, alfa de Cronbach, omega de McDonald, CR, entropia, LRT/BLRT, Wilks' lambda e tamanhos de efeito (d de Cohen). |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Aprofunda o papel do pertencimento (inclusao/exclusao), antecipacao ansiosa, desconforto interpessoal e clima escolar na vulnerabilidade a recusa escolar. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute vies de autorrelato, generalizacao cultural, tamanho de subgrupos etarios, corte transversal e limitacao da MGCFA para genero nao binario. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **10 / 10** | |

---

---

## S0091: Understanding School Non-Attendance in Adolescence: Perceived Competence, Psychological and Social Barriers, and Educational Vulnerability

> - **ID do Estudo:** `S0091`
> - **Autores:** Luana Sorrenti, Concettina Caparello, Carmelo Francesco Meduri, Pina Filippello
> - **Ano:** 2026
> - **Veículo (Venue):** *Education Sciences*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.3390/educsci16071074](https://doi.org/10.3390/educsci16071074)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105045730024?origin=resultslist)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0091`
- **Titulo Completo:** Understanding School Non-Attendance in Adolescence: Perceived Competence, Psychological and Social Barriers, and Educational Vulnerability
- **Autores:** Luana Sorrenti, Concettina Caparello, Carmelo Francesco Meduri, Pina Filippello
- **Ano de Publicacao:** 2026
- **Tipo de Publicacao:** Periodico (Artigo Original)
- **Nome do Veiculo:** Education Sciences (16, 1074)
- **DOI:** [10.3390/educsci16071074](https://doi.org/10.3390/educsci16071074)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Italia (Sul da Italia)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Ensino Medio / Upper Secondary Schools)
- **Faixa Etaria / Amostra ($N$):** Estudo 1: EFA n = 391 (14-20 anos; Mage = 15,70, DP = 0,99; media de 22,87 faltas/ano) e CFA n = 593 (14-20 anos; Mage = 16,00, DP = 0,99; media de 24 faltas/ano). Estudo 2: n = 183 adolescentes em risco de SAPs (14-19 anos; Mage = 16,17, DP = 1,02; 83 meninos, 96 meninas, 4 nao declarados; GPA medio = 6,61, DP = 0,42; media de 0,67 disciplinas reprovadas).
- **Publico-alvo Avaliado:** Adolescentes estudantes de escolas publicas de ensino medio, incluindo subamostra em risco de problemas de frequencia escolar (SAPs / Recusa_Escolar / absenteismo)
- **Fonte dos Dados / Dataset:** Questionarios de autorrelato aplicados presencialmente em sala de aula durante o horario escolar regular (bateria de 15-20 min).

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** Adolescent Reasons for School Non-Attendance Scale (ARSNA; Havik et al., 2015), versao italiana validada e refinada para 13 itens em 4 fatores (Somatic reasons, Subjective health complaints, Truancy-related reasons, School refusal-related reasons; Likert 0-3); Perception of Competence in Life Domains Scale (PCLDS; Losier et al., 1993; 16 itens em 4 dominios; Likert 1-7).
- **Natureza da Ferramenta:** Instrumentos psicometricos tradicionais (escalas de autorrelato validadas).
- **Forma de Aplicacao:** Autorrelato do aluno em ambiente escolar padronizado (supervisionado por pesquisadores treinados).
- **Finalidade:** Validacao psicometrica transcultural da ARSNA e identificacao diferencial de motivacoes de nao comparecimento escolar (queixas somaticas, queixas subjetivas de saude, truancy e recusa escolar) associadas a competencia percebida.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Analise Estatistica Avancada / Modelagem Psicometrica e Preditiva Linear (nao utiliza algoritmos de Machine Learning).
- **Algoritmos Empregados:** Analise Fatorial Exploratoria (EFA via MINRES com rotacao Oblimin), Analise Fatorial Confirmatoria (CFA via Maximum Likelihood no Jamovi 2.6.26 / 2.5.6.0) e Regressao Linear Multipla Hierarquica (HMRA em 2 passos para 4 desfechos).
- **Tarefa do Modelo:** Validacao fatorial (comparacao de 4 modelos concorrentes M1-M4) e regressao hierarquica para predicao da variancia incremental das motivacoes de absenteismo.
- **Estagio de Deteccao:** Identificacao precoce de vulnerabilidades psicologicas (baixa competencia percebida) antes da cronificacao dos problemas de frequencia (integracao sugerida em EWS).

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Competencia geral percebida, competencia academica percebida, competencia em relacoes interpessoais, competencia no lazer (Teoria da Autodeterminacao - SDT); medo/ansiedade relacionada a escola; queixas somaticas e subjetivas de saude (fadiga, dor muscular, nausea).
- **Variaveis Comportamentais / Historico:** Numero de faltas escolares no ano anterior, media de notas (GPA), numero de disciplinas reprovadas, razoes de absenteismo nos ultimos 3 meses (truancy vs. recusa escolar).
- **Variaveis Familiares / Sociodemograficas:** Idade, genero, nacionalidade (italiana vs. estrangeira no Estudo 1; apenas nativos italianos sem necessidades educacionais especiais no Estudo 2).
- **Variaveis Institucionais / Contextuais:** Contexto de escolas publicas de ensino medio no Sul da Italia (menciona na discussao fatores de clima escolar e exclusao/pertencimento).
- **Features Mais Relevantes Identificadas:** Para Recusa Escolar (R2 = 0,257; Delta R2 = 0,142, p < 0,001): baixa competencia geral percebida (beta = -0,23, p <= 0,01), baixa competencia academica percebida (beta = -0,18, p <= 0,05) e genero feminino (beta = 0,20, p < 0,01). Para Truancy (R2 = 0,075; Delta R2 = 0,063, p <= 0,05): baixa competencia academica percebida (beta = -0,27, p <= 0,01). Para Queixas Subjetivas de Saude: genero feminino (beta = 0,29, p <= 0,001). Para Sintomas Somaticos: menor desempenho academico/GPA (beta = -0,19, p <= 0,05).

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** ARSNA M4 (13 itens, 4 fatores): chi2 = 271 (df = 59, p < 0,001), CFI = 0,90, TLI = 0,87, RMSEA = 0,07 (IC 90%: 0,06-0,08), SRMR = 0,06, BIC = 174; Alfa de Cronbach (Estudo 1 / Estudo 2): SRR = 0,78 / 0,77, SR = 0,62 / 0,64, TR = 0,76 / 0,68, SHR = 0,65 / 0,67. PCLDS Alfa de Cronbach: geral = 0,78, academica = 0,74, interpessoal = 0,75, lazer = 0,70.
- **Metricas Computacionais (ML):** N/A (Regressao hierarquica: R2, Delta R2, estatistica F, t e coeficientes padronizados beta).
- **Estrategia de Validacao:** Amostras independentes para EFA (n = 391) e CFA (n = 593) com comparacao de 4 modelos concorrentes; regressao hierarquica em amostra independente (n = 183) controlando idade, genero, GPA e reprovacoes.
- **Desafios Metodologicos Relatados:** Necessidade de remocao de 4 itens da ARSNA original (itens 7, 17, 2 e 13) para atingir ajuste aceitavel (TLI marginal = 0,87); alfas moderados (~0,62-0,68) em subescalas curtas de 3-4 itens; risco de confusao entre sintomas somaticos normativos e sofrimento emocional.
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao pelo Comite de Etica da Universidade de Alicante (UA-2023-03-07), conformidade com AIP e Declaracao de Helsinki, consentimento informado escrito dos pais/responsaveis e coleta anonima voluntaria.
- **Limitacoes Declaradas:** Delineamento transversal impede inferencias causais; amostra restrita ao Sul da Italia limita generalizacao; exclusao de estudantes com necessidades educacionais especiais; dependencia exclusiva de autorrelato (variancia de metodo compartilhado); ausencia de analise de invariancia de medida por genero e idade.
- **Direcoes Futuras:** Estudos longitudinais e transnacionais; inclusao de estudantes com necessidades educacionais especiais; coleta multinformante (professores, pais e registros administrativos); testes de invariancia da ARSNA por genero e idade; integracao de indicadores de competencia percebida em sistemas de monitoramento escolar precoce.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Duas questoes de pesquisa explicitas: validar psicometricamente a ARSNA italiana (Estudo 1) e testar o valor preditivo incremental da competencia percebida multidimensional (Estudo 2). |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Amostras independentes para EFA (n=391) e CFA (n=593), traducao via diretrizes ITC, criterios de retencao fatorial e regressao hierarquica em 2 passos descritos com rigor. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta CFI, TLI, RMSEA, SRMR, BIC, cargas fatoriais, alfa de Cronbach, correlacoes de Pearson, R2, Delta R2 e betas padronizados. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analisa competencia percebida em 4 dominios sob a Teoria da Autodeterminacao, diferenciando seus efeitos sobre recusa escolar, truancy, sintomas somaticos e queixas subjetivas. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute explicitamente corte transversal, especificidade regional, exclusao de NEE, vies de autorrelato e falta de invariancia de medida. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **10 / 10** | |

---

---

## S0145: Early Identification of School Refusal from Parents’ Perspectives

> - **ID do Estudo:** `S0145`
> - **Autores:** Geir Møller
> - **Ano:** 2025
> - **Veículo (Venue):** *Education Sciences*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.3390/educsci15091211](https://doi.org/10.3390/educsci15091211)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105017420477?origin=resultslist)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0145`
- **Titulo Completo:** Early Identification of School Refusal from Parents' Perspectives
- **Autores:** Geir Møller
- **Ano de Publicacao:** 2025
- **Tipo de Publicacao:** Periodico (Artigo Original)
- **Nome do Veiculo:** Education Sciences (15(9), 1211)
- **DOI:** [10.3390/educsci15091211](https://doi.org/10.3390/educsci15091211)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Noruega

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Pre-escola/Kindergarten, Ensino Fundamental e Ensino Medio)
- **Faixa Etaria / Amostra ($N$):** Pesquisa em duas fases com pais de criancas/adolescentes com recusa escolar. Fase 1: 250 respondentes (196 responderam a questao aberta, 184 retidos apos codificacao em 30 categorias). Fase 2: 850 respondentes iniciais, 658 completos e N = 509 na amostra liquida final (57% meninos, 43% meninas; idade media atual = 12,8 anos, DP = 2,58, faixa 6,5-19 anos; idade media de inicio da recusa = 10,1 anos, DP = 2,42, faixa 0-16 anos).
- **Publico-alvo Avaliado:** Criancas e adolescentes com recusa escolar emergente ou manifestada, avaliados pela perspectiva dos pais/responsaveis.
- **Fonte dos Dados / Dataset:** Questionario online em duas etapas divulgado em grupo do Facebook para pais de filhos com recusa escolar na Noruega.

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** Bateria de questionario padronizado de 30 categorias de sinais e sintomas precoces desenvolvida no estudo (escala de 3 opcoes: "no", "yes, to some extent", "yes, to a large extent"). Na revisao de literatura, discute SRAS, SCREEN e SNACK, apontando que essas escalas focam casos ja manifestados ou acompanhamento clinico.
- **Natureza da Ferramenta:** Questionario de triagem baseado em observacoes parentais (30 sinais/sintomas agrupados em 7 fatores).
- **Forma de Aplicacao:** Relato dos pais/responsaveis via questionario online.
- **Finalidade:** Identificacao precoce de sinais de alerta da recusa escolar emergente (antes da ausencia cronica manifestada) e construcao de entendimento compartilhado entre familia e escola.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Analise Estatistica Avancada / Analise Fatorial e Regressao Linear (nao utiliza algoritmos de Machine Learning; contribui com taxonomia empirica de sinais para sistemas de alerta precoce).
- **Algoritmos Empregados:** Analise Fatorial Exploratoria (Principal Axis Factoring com rotacao obliqua Oblimin), Analise Fatorial Confirmatoria (CFA via Maximum Likelihood no Jamovi 2.7 em apendice) e Regressao Linear (associacao dos 7 fatores com genero e idade de inicio).
- **Tarefa do Modelo:** Reducao dimensional de 30 sinais precoces em 7 fatores latentes e analise de variacao por genero e idade de inicio.
- **Estagio de Deteccao:** Alerta precoce na fase de recusa escolar emergente (quando o estudante ainda frequenta a escola, mas manifesta resistencia ou sofrimento).

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Aversao/medo de ir a escola (76%), ansiedade de desempenho (51%), tristeza e tedio em casa (63%), choro inexplicavel (32%), raiva/acting out em casa (50%), inseguranca na escola (54%), baixo senso de dominio (66%) e queixas psicossomaticas (dor de estomago/nausea/vomito 65%; dor de cabeca 52%).
- **Variaveis Comportamentais / Historico:** Protestos para ir a escola (72%), relutancia em fazer tarefas de casa (71%), dificuldades de sono (65%), dificuldade para acordar (60%), dificuldade de concentracao (59%), dificuldade em acompanhar academicamente (41%), recusa a disciplinas especificas (59%), perda de amigos (38%), isolamento social (46%), sair da escola durante o turno (21%) e faltas sem conhecimento dos pais/truancy (5%).
- **Variaveis Familiares / Sociodemograficas:** Genero da crianca, idade de inicio da recusa (picos aos 6 anos e aos 12-13 anos), duracao da recusa e escolaridade parental (69% com ensino superior na amostra).
- **Variaveis Institucionais / Contextuais:** Medo de professores (28%), discussoes com professores (17%), bullying/exclusao (31%), insatisfacao geral com a escola (61%) e dificuldade nas transicoes entre niveis escolares (46%).
- **Features Mais Relevantes Identificadas:** Sete dimensoes latentes na EFA: (1) Dificuldades sociais, (2) Dificuldades academicas, (3) Aversao a adultos na escola/professores, (4) Ansiedade de desempenho, (5) Queixas psicossomaticas, (6) Relutancia em relacao a escola/ambiente escolar e (7) Expressoes emocionais (tristeza, choro, raiva em casa). Meninas apresentaram mais queixas psicossomaticas, ansiedade de desempenho e dificuldades sociais; meninos apresentaram mais dificuldades academicas.

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** EFA (24 variaveis retidas apos exclusao de 6 com comunalidade/carga < 0,30): KMO = 0,86; 7 fatores extraidos. CFA no mesmo conjunto de dados (Apendice B): chi2(228) = 977 (p < 0,001), CFI = 0,871, TLI = 0,844, RMSEA = 0,070 (IC 90%: 0,066-0,075), SRMR = 0,054; cargas padronizadas entre 0,32 e 0,66. Nao reporta alfa de Cronbach ou omega de McDonald.
- **Metricas Computacionais (ML):** N/A.
- **Estrategia de Validacao:** Survey em duas fases (codificacao qualitativa em 3 etapas na Fase 1 + questionario estruturado na Fase 2 com limpeza de respostas incompletas, implausiveis e casos > 5 anos); EFA e CFA exploratoria no mesmo dataset.
- **Desafios Metodologicos Relatados:** Sobreposicao de sinais precoces de recusa escolar com indicadores de ansiedade geral, estresse transitorio e negligencia familiar (risco de notificacao equivocada a servicos de protecao infantil); sinais escolares pouco observaveis diretamente pelos pais (ex.: conflitos com professores); confusao entre fase emergente e fase manifestada.
- **Aspectos Eticos e Transparencia (XAI):** Conformidade com Declaracao de Helsinki; dados anonimizados avaliados pela agencia norueguesa SIKT (Ref. 316229) como dispensados de notificacao formal; consentimento informado obtido dos participantes.
- **Limitacoes Declaradas:** Vies de selecao por recrutamento em grupo do Facebook (super-representacao de pais com ensino superior: 69% vs. 51% nacional); vies de memoria retrospectiva nos relatos parentais; ausencia de triangulacao com professores, clinicos ou os proprios estudantes; ajuste moderado da CFA (CFI/TLI < 0,90) realizada na mesma amostra da EFA.
- **Direcoes Futuras:** Investigacao de sinais precoces em subgrupos neurodivergentes (TDAH e autismo); estudos multinformantes combinando pais, professores e autorrelato dos alunos; validacao da estrutura fatorial em amostras independentes e maiores.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo claro: explorar se a sistematizacao das experiencias dos pais permite identificar sinais e sintomas precoces da recusa escolar emergente. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Desenho em duas fases (N=196 aberta -> 30 categorias; N=509 estruturada apos limpeza), criterios de exclusao e especificacao da EFA (PAF/Oblimin, corte 0,30) bem descritos. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Reporta KMO (0,86), cargas fatoriais, indices de ajuste da CFA em apendice (CFI=0,871, RMSEA=0,070) e regressoes, mas sem alfa/omega e sem amostra independente para CFA. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analise aprofundada de 7 dimensoes socioemocionais, psicossomaticas, academicas e relacionais da recusa emergente, incluindo risco de confusao com negligencia. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Secao dedicada discute vies de selecao (escolaridade parental no Facebook), vies retrospectivo de memoria e falta de triangulacao multinformante. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | |

---

---

## S0154: Pre-Birth Household Challenges Predict Future Child’s School Readiness and Academic Achievement

> - **ID do Estudo:** `S0154`
> - **Autores:** Robyn A. Husa, Jared W. Parrish, Heidi S. Johnson
> - **Ano:** 2022
> - **Veículo (Venue):** *Children*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.3390/children9030414](https://doi.org/10.3390/children9030414)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/85127077209?origin=resultslist)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0154`
- **Titulo Completo:** Pre-Birth Household Challenges Predict Future Child’s School Readiness and Academic Achievement
- **Autores:** Robyn A. Husa, Jared W. Parrish, Heidi S. Johnson
- **Ano de Publicacao:** 2022
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Children
- **DOI:** [10.3390/children9030414](https://doi.org/10.3390/children9030414)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (Alasca)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Jardim de Infancia ao 3o ano do Ensino Fundamental)
- **Faixa Etaria / Amostra ($N$):** n = 3.549 respondentes (pessoas gestantes) da coorte PRAMS 2009-2011, representando 33.417 (+/- 233) criancas nascidas no Alasca acompanhadas ate 2019 (registros escolares de 2015-2019)
- **Publico-alvo Avaliado:** Criancas em idade escolar inicial avaliadas quanto a prontidao escolar, proficiencia em leitura e absenteismo cronico (<90% de frequencia)
- **Fonte dos Dados / Dataset:** Vinculacao retrospectiva (ALCANLink) entre o Alaska Pregnancy Risk Assessment Monitoring System (PRAMS 2009-2011) e registros administrativos/educacionais do Alaska Department of Education and Early Development (DEED, 2015-2019)

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** Questionario padronizado CDC PRAMS de eventos estressantes pre-natais (14 desafios familiares); Alaska Developmental Profile (ADP, 13 metas em 5 dominios); Performance Evaluation for Alaska's Schools (PEAKS) English Language Arts (ELA)
- **Natureza da Ferramenta:** Questionario populacional de triagem pre-natal e avaliacoes educacionais padronizadas estaduais
- **Forma de Aplicacao:** Autorrelato da pessoa gestante (PRAMS, referente aos 12 meses anteriores ao nascimento) e avaliacoes/registros escolares oficiais (DEED)
- **Finalidade:** Triagem precoce de fatores de risco pre-natais e predicao de prontidao escolar, proficiencia em leitura e absenteismo cronico

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Analise Estatistica Avancada / Modelos Lineares Generalizados (GLM com distribuicao Quasi-Poisson) e regressao stepwise com eliminacao retrograda (backward elimination)
- **Algoritmos Empregados:** Modelos Lineares Generalizados (Quasi-Poisson GLM) ponderados por pos-estratificacao e regressao stepwise backward em R (pacotes `survey` e `srvyr`)
- **Tarefa do Modelo:** Classificacao/predicao de risco relativo (Risk Ratio) para desfechos binarios: absenteismo cronico (<90% vs. >=90% de frequencia media), ADP (<11 vs. >=11 metas) e PEAKS ELA (abaixo da proficiencia vs. proficiente/avancado)
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (identificacao de risco no periodo pre-natal para prevencao antes do ingresso escolar)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Ansiedade ou depressao da pessoa gestante avaliada ou tratada por profissional medico; desenvolvimento socioemocional da crianca no ADP
- **Variaveis Comportamentais / Historico:** Absenteismo_Cronico (frequencia media <90% entre 2015-2019, presente em 22% da populacao), prontidao no Jardim de Infancia (ADP) e leitura no 3o ano (PEAKS)
- **Variaveis Familiares / Sociodemograficas:** 14 desafios familiares pre-natais (situacao de rua/sem-teto, divorcio/separacao, mudanca de endereco, perda de emprego da gestante ou parceiro, aumento de discussoes com parceiro, contas nao pagas, agressao fisica, encarceramento da gestante ou parceiro, problema de alcool/drogas em pessoa proxima, morte de pessoa proxima, doenca grave de familiar, violencia por parceiro intimo); raca/etnia (Alaska Native), escolaridade materna e idade materna ao nascimento
- **Variaveis Institucionais / Contextuais:** Condado urbano vs. rural, cobertura por Medicaid no parto e acesso a programas de apoio precoce (Head Start, Child FIRST, visitas domiciliares)
- **Features Mais Relevantes Identificadas:** Acumulo de >=4 desafios pre-natais foi preditor significativo de absenteismo cronico (ARR = 1,29; IC 95% 1,04-1,60), baixo ADP (ARR = 1,16; IC 95% 1,07-1,25) e baixa leitura PEAKS (ARR = 1,36; IC 95% 1,21-1,53); entre os desafios individuais, situacao de rua (homelessness) apresentou o maior risco consistente, acompanhada por encarceramento, divorcio/separacao, luto, discussoes com parceiro e abuso de substancias

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** N/A (Estudo epidemiologico baseado em dados de vigilancia PRAMS e registros administrativos escolares)
- **Metricas Computacionais (ML):** Risk Ratios (RR) e Adjusted Risk Ratios (ARR) com IC 95%: para absenteismo cronico, 4+ desafios obteve RR = 1,38 (IC 95% 1,12-1,70) e ARR = 1,29 (IC 95% 1,04-1,60); 2-3 desafios obteve ARR = 1,12 (IC 95% 0,93-1,36, nao significativo)
- **Estrategia de Validacao:** Ponderacao populacional pos-estratificacao (PRAMS) e selecao de covariaveis via eliminacao retrograda mantendo variaveis cuja remocao alterasse o efeito em >10% (raca Alaska Native e escolaridade materna)
- **Desafios Metodologicos Relatados:** Superdispersao dos dados (tratada via distribuicao Quasi-Poisson), respostas ausentes nos itens de exposicao (tratadas como "nao", gerando possivel subestimacao) e longo intervalo temporal entre exposicao pre-natal e desfechos escolares
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao pelos IRBs da University of Alaska Anchorage e CDC, revisao etica DPH MCH-Epidemiology e acordos legais estaduais de confidencialidade (Alaska DHSS/DEED)
- **Limitacoes Declaradas:** Amostra restrita ao Alasca (perfil demografico distinto do restante dos EUA); possivel vies de desejabilidade social no autorrelato do PRAMS; baixa heterogeneidade nos desfechos (>50% abaixo dos padroes no ADP e PEAKS); imputacao de respostas ausentes como zero
- **Direcoes Futuras:** Avaliar mediadores pos-nascimento (ex.: apego parental e experiencias adversas na infancia - ACEs) e testar intervencoes intersetoriais de coordenacao de cuidado desde o pre-natal

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo claro de avaliar se desafios familiares pre-natais predizem prontidao escolar, leitura no 3o ano e absenteismo cronico. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Coorte retrospectiva estadual (n = 3.549 / 33.417 ponderado), linkage ALCANLink, definicoes operacionais e GLM Quasi-Poisson descritos com clareza. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Reporta RRs/ARRs e IC 95% completos, mas nao reporta metricas de discriminacao preditiva (ex.: AUC-ROC, acuracia ou F1-score). |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Examina ansiedade/depressao gestacional, violencia domestica, instabilidade habitacional e determinantes socioambientais ligados ao absenteismo cronico. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discutem generalizacao geografica, vies de desejabilidade social, codificacao de dados faltantes e janela temporal longa. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | |

---

---

## S0030: Developing an Anxiety Screening Tool for Children in South Africa: Protocol for a Mixed Methods Study

> - **ID do Estudo:** `S0030`
> - **Autores:** Fatiema Benjamin, Babatope O. Adebiyi, Edna Rich, Nicolette Vanessa Roman
> - **Ano:** 2022
> - **Veículo (Venue):** *JMIR Research Protocols*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.2196/37364](https://doi.org/10.2196/37364)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/85139725821?origin=resultslist)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0030`
- **Titulo Completo:** Developing an Anxiety Screening Tool for Children in South Africa: Protocol for a Mixed Methods Study
- **Autores:** Fatiema Benjamin, Babatope O. Adebiyi, Edna Rich, Nicolette Vanessa Roman
- **Ano de Publicacao:** 2022
- **Tipo de Publicacao:** Periodico (Protocolo de Pesquisa revisado por pares)
- **Nome do Veiculo:** JMIR Research Protocols
- **DOI:** [10.2196/37364](https://doi.org/10.2196/37364)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Africa do Sul (Provincia de Western Cape)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Infantil e Ensino Fundamental Inicial (Preschool e Foundation Phase)
- **Faixa Etaria / Amostra ($N$):** Populacao-alvo: criancas de 4 a 8 anos (nao respondentes diretos). Amostra planejada do protocolo: Estagio 1 (revisao de escopo); Estagio 2 (N ~ 60 participantes em entrevistas: pais/cuidadores, professores e especialistas dos 6 distritos); Estagio 3 (N ~ 20 especialistas em painel e-Delphi); Estagio 4 (estudo piloto com estimativa de N ~ 400 professores de pre-escola e fase inicial, ~67 por distrito).
- **Publico-alvo Avaliado:** Criancas de 4 a 8 anos em risco de ansiedade infantil na Africa do Sul (avaliadas por professores, pais e especialistas)
- **Fonte dos Dados / Dataset:** Dados primarios planejados via revisao de escopo (Academic Search Complete, APA PsycArticles, CINAHL Plus, ERIC, MEDLINE), entrevistas semiestruturadas, rodadas e-Delphi online (Google Chat) e aplicacao piloto presencial/online do instrumento desenvolvido.

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** Proposta de nova ferramenta de triagem de ansiedade infantil para criancas sul-africanas (4-8 anos), ainda sem nome definitivo; referencia ferramentas internacionais existentes como SCARED (Screen for Anxiety-Related Disorders), SCAS (Spence Children's Anxiety Scale) e PAS (Preschool Anxiety Scale).
- **Natureza da Ferramenta:** Questionario de triagem / instrumento psicometrico em desenvolvimento (metodos mistos sequenciais exploratorios com abordagem participativa PAR).
- **Forma de Aplicacao:** Relato dos professores (administrado por professores de pre-escola e fase inicial, com consentimento previo dos pais e da crianca), informado previamente por entrevistas com pais, cuidadores, professores e especialistas.
- **Finalidade:** Triagem inicial precoce de sintomas de ansiedade infantil no contexto escolar para encaminhamento a servicos de tratamento.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** N/A (Protocolo de pesquisa qualitativa e psicometrica tradicional; nao emprega IA ou Machine Learning).
- **Algoritmos Empregados:** N/A (Analise tematica indutiva de Braun e Clarke para dados qualitativos/e-Delphi; testes estatisticos em SPSS 28: Shapiro-Wilk, teste de esfericidade de Bartlett, KMO e Analise Fatorial Exploratoria no Estagio 4).
- **Tarefa do Modelo:** N/A (Desenvolvimento e validacao estrutural de escala de triagem).
- **Estagio de Deteccao:** Triagem preventiva / identificacao precoce na primeira infancia (4-8 anos), antes de desfechos futuros como evasao escolar na adolescencia.

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Sintomas de ansiedade infantil (ansiedade generalizada, ansiedade de separacao, fobia social, fobia escolar, panico), temperamento infantil, inibicao comportamental e sofrimento emocional.
- **Variaveis Comportamentais / Historico:** Dificuldades de aprendizagem, problemas comportamentais na escola, comportamento agressivo na transicao casa-escola, dificuldade de engajamento com pares e conteudo educacional, bullying e rejeicao; evasao escolar e abuso de substancias citados como consequencias tardias.
- **Variaveis Familiares / Sociodemograficas:** Trauma na primeira infancia, exposicao a violencia, pobreza, controle psicologico parental, superprotecao e estilo parental, psicopatologia materna, conflito familiar, negligencia/abuso infantil e falta de relacoes proximas com adultos.
- **Variaveis Institucionais / Contextuais:** Contexto multicultural e multilingue sul-africano (ingles, afrikaans, isiXhosa), transicao para nova escola, ambiente escolar e politicas de saude mental infantil e adolescente (CAMH).
- **Features Mais Relevantes Identificadas:** N/A (protocolo em andamento; fatores e itens serao definidos nas etapas qualitativas, e-Delphi e analise fatorial).

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Planejadas para o Estagio 4: consistencia interna, validade de face, conteudo, criterio (concorrente e preditiva) e construto (convergente, discriminante e divergente), normalidade (Shapiro-Wilk), adequacao amostral (KMO), esfericidade de Bartlett e Analise Fatorial Exploratoria (EFA). Ainda sem valores empiricos obtidos.
- **Metricas Computacionais (ML):** N/A.
- **Estrategia de Validacao:** Validacao sequencial em 4 estagios: revisao de escopo (PRISMA-ScR), entrevistas qualitativas ate saturacao, consenso e-Delphi com 20 especialistas e piloto quantitativo com amostragem aleatoria estratificada por distrito.
- **Desafios Metodologicos Relatados:** Ausencia de ferramenta culturalmente adaptada ao contexto multilingue sul-africano; falta de definicao desenvolvimental universal da ansiedade infantil no DSM-5; restricoes da pandemia de COVID-19 na coleta presencial; baixa implementacao provincial de politicas CAMH.
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao etica obtida (BM21/9/12, University of the Western Cape), consentimento informado de pais e criancas, anonimato via pseudonimos, protecao por senha dos dados, encaminhamento para servicos de aconselhamento gratuito em caso de desconforto emocional e protocolos sanitarios de COVID-19.
- **Limitacoes Declaradas:** A ferramenta nao sera aplicada diretamente as criancas como respondentes (apenas via professores), e o projeto nao possui delineamento longitudinal, impossibilitando monitorar a efetividade da ferramenta ao longo do tempo.
- **Direcoes Futuras:** Execucao das etapas empiricas (coleta qualitativa, e-Delphi e piloto), refinamento/descarte de itens problematicos via EFA, disseminacao para subsidiar politicas publicas de saude mental infantil (CAMH) na Africa do Sul e realizacao de estudos longitudinais futuros.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo explicitamente definido: explorar percepcoes sobre ansiedade infantil e desenvolver uma ferramenta de triagem para criancas de 4 a 8 anos na Africa do Sul. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Desenho misto sequencial exploratorio em 4 estagios (PRISMA-ScR, entrevistas com N=60, e-Delphi com N=20, piloto estratificado com N~400) detalhado de forma replicavel. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 0 | Por se tratar de um protocolo de estudo publicado antes da conclusao da coleta, nao apresenta resultados empiricos nem metricas de validacao obtidas. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Analisa fatores psicologicos, parentais, traumaticos e culturais da ansiedade infantil, mencionando evasao escolar como desfecho futuro, mas sem foco direto em recusa escolar. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute explicitamente limitacoes na secao dedicada: ausencia de autorrelato infantil e ausencia de acompanhamento longitudinal. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **7 / 10** | |

---

---

## S0075: School Refusal Behavior: A Narrative Review Journal of Indian Association for Child and

> - **ID do Estudo:** `S0075`
> - **Autores:** Manoj Kumar Sahoo, Snigdha Awasthi, Harshita Biswas, Susanta Kumar Padhy
> - **Ano:** 2023
> - **Veículo (Venue):** *Journal of Indian Association for Child and Adolescent Mental Health*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.1177/09731342231220705](https://doi.org/10.1177/09731342231220705)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/85185127916?origin=resultslist)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0075`
- **Titulo Completo:** School Refusal Behavior: A Narrative Review
- **Autores:** Manoj Kumar Sahoo, Snigdha Awasthi, Harshita Biswas, Susanta Kumar Padhy
- **Ano de Publicacao:** 2023
- **Tipo de Publicacao:** Periodico (Artigo de Revisao Narrativa)
- **Nome do Veiculo:** Journal of Indian Association for Child and Adolescent Mental Health (19(4), 344-354)
- **DOI:** [10.1177/09731342231220705](https://doi.org/10.1177/09731342231220705)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** India (revisao com escopo internacional e enfase no contexto indiano)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Ensino Fundamental e Ensino Medio / criancas e adolescentes)
- **Faixa Etaria / Amostra ($N$):** Revisao narrativa de 38 artigos originais em ingles (publicados nos ultimos 10 anos); excluidos estudos restritos a subgrupos especificos (ex.: criancas autistas ou imigrantes).
- **Publico-alvo Avaliado:** Criancas e adolescentes com comportamento de recusa escolar
- **Fonte dos Dados / Dataset:** Bases bibliograficas MEDLINE e Scopus.

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** SRAS-R (School Refusal Assessment Scale), ISAP (Inventory of School Attendance Problems), CBCL (Child Behavior Checklist), TRF (Teacher's Report Form) e criterios diagnosticos operacionais de Berg / Maric (< 80% de frequencia nas ultimas 2 semanas, transtorno de ansiedade DSM-IV, ausencia de transtorno de conduta, ciencia e compromisso dos pais).
- **Natureza da Ferramenta:** Instrumentos psicometricos tradicionais, escalas de avaliacao clinica/funcional e criterios diagnosticos clinicos.
- **Forma de Aplicacao:** Multinformante: autorrelato do aluno, relato dos pais, relato dos professores e avaliacao/entrevista clinica e medica.
- **Finalidade:** Diagnostico diferencial (entre recusa escolar e truancy), avaliacao funcional e sintomatica, triagem escolar e planejamento de intervencoes.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** N/A (Revisao narrativa clinica e educacional; nao emprega modelos de IA/ML. Discute programas estruturados de triagem e prevencao em etapas, como triagem pre-escolar em 3 passos no Japao, programa Min-Iku de educacao do sono e modelo comunitario multinivel MTSS/RTI/PBIS nos EUA).
- **Algoritmos Empregados:** N/A.
- **Tarefa do Modelo:** N/A.
- **Estagio de Deteccao:** Enfatiza deteccao precoce e prevencao em nivel escolar/comunitario (Tier 1-3 no MTSS e triagem aos 5 anos) em contraste com encaminhamento clinico tardio.

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Ansiedade de separacao, ansiedade social, transtorno emocional infantil nao especificado, depressao, transtorno somatoforme/conversivo, temperamento inibido/introvertido, sensibilidade a critica, pensamentos automaticos negativos sobre fracasso pessoal e hostilidade, supergeneralizacao, desregulacao emocional e sintomas somaticos (palpitacoes, dor abdominal).
- **Variaveis Comportamentais / Historico:** Padrao de faltas (< 80% em 2 semanas), desempenho academico/dificuldades de aprendizagem, isolamento de pares, bullying (incluindo bias-based bullying), privacao cronica de sono/dificuldade para acordar e doencas medicas cronicas previas.
- **Variaveis Familiares / Sociodemograficas:** Genero, tipo familiar, renda familiar regular, escolaridade parental, abuso de substancias ou transtorno psiquiatrico nos pais, separacao/morte parental, maus-tratos, discordia familiar, estilos parentais e baixa acessibilidade financeira a servicos de saude mental (especialmente na India).
- **Variaveis Institucionais / Contextuais:** Controle psicologico percebido do professor, relacionamento pobre com pares, pressao academica/discrepancia entre expectativas parentais e aptidao, transicoes escolares (inicio do primario e passagem para o secundario) e clima escolar.
- **Features Mais Relevantes Identificadas:** Fatores protetivos destacados: resiliencia academica, participacao em atividades prossociais e engajamento social; entre os fatores de risco: ansiedade, depressao, disfuncao familiar e dificuldades de sono.

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Nao reporta indices psicometricos proprios (aponta ausencia de consenso sobre uma ferramenta psicometrica culturalmente sensivel para diagnostico de campo na India).
- **Metricas Computacionais (ML):** N/A.
- **Estrategia de Validacao:** Busca narrativa em MEDLINE e Scopus com selecao de 38 artigos originais; sintetiza taxas de prevalencia (2% a 16% globalmente; ate 7% na India) e taxas de retorno escolar de estudos de intervencao (ex.: CBT intensiva 12% para 60%; rapid return 72%; In2School 6/7 jovens; CBT+fluoxetina 15% para 52-54%).
- **Desafios Metodologicos Relatados:** Heterogeneidade causal da recusa escolar; confusao terminologica entre recusa escolar e truancy/mau comportamento; interpretacao equivocada de queixas somaticas como puramente fisicas; falta de consenso em instrumento diagnostico padronizado; escassez de estudos indianos sobre intervencoes em larga escala.
- **Aspectos Eticos e Transparencia (XAI):** Discute questoes eticas relevantes em intervencoes (ex.: abordagem rapid return considerada eticamente complexa e contraindicada quando pais tem depressao/dificuldades de manejo; uso cauteloso e de ultimo recurso de farmacoterapia devido a riscos ao crescimento fisico e desenvolvimento cognitivo).
- **Limitacoes Declaradas:** Escassez de pesquisas indianas focadas em metodos de avaliacao e intervencao em larga escala; falta de conhecimento completo sobre os mecanismos exatos mediadores da recusa escolar; natureza narrativa da revisao (sem meta-analise ou avaliacao formal de risco de vies).
- **Direcoes Futuras:** Desenvolvimento e validacao de instrumentos psicometricos culturalmente sensiveis para operacionalizar o diagnostico da recusa escolar; testes de intervencoes direcionadas e protocolos comunitarios adaptados a populacao indiana envolvendo escola, pais e profissionais de saude mental.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo claro: identificar conceitos-chave, fatores de risco e discutir metodos praticos de avaliacao e tratamento para recusa escolar. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 1 | Descreve bases (MEDLINE, Scopus), palavras-chave, periodo (10 anos) e n = 38 artigos, mas sem string booleana exata, protocolo PRISMA ou avaliacao sistematica de qualidade. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Reporta prevalencias e desfechos quantitativos de estudos primarios citados, mas nao conduz validacao estatistica propria nem meta-analise. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 2 | Analise detalhada de comorbidades psiquiatricas, temperamento, cognicoes, fatores parentais/familiares, fatores escolares e fatores protetivos. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 1 | Discute lacunas da literatura indiana e limitacoes/riscos eticos das intervencoes revisadas, mas nao discute sistematicamente o vies de selecao da propria revisao narrativa. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **7 / 10** | |

---

---


---

# Parte III — Estudos Excluidos Apos Leitura do PDF Completo (2 estudos)

## S0133: A PSO weighted ensemble framework with SMOTE balancing for student dropout prediction in smart education systems

> - **ID do Estudo:** `S0133`
> - **Autores:** Achin Jain, Arun Kumar Dubey, Shakir Khan, Arvind Panwar, Mohammad Alkhatib, Abdulaziz M Alshahrani
> - **Ano:** 2025
> - **Veículo (Venue):** *Scientific Reports*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Springer Link']`)
> - **DOI:** [10.1038/s41598-025-97506-1](https://doi.org/10.1038/s41598-025-97506-1)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105005547670?origin=resultslist)
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC2]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0133`
- **Titulo Completo:** A PSO weighted ensemble framework with SMOTE balancing for student dropout prediction in smart education systems
- **Autores:** Achin Jain, Arun Kumar Dubey, Shakir Khan, Arvind Panwar, Mohammad Alkhatib, Abdulaziz M Alshahrani
- **Ano de Publicacao:** 2025
- **Tipo de Publicacao:** Periodico (Artigo Original)
- **Nome do Veiculo:** Scientific Reports (15:17463)
- **DOI:** [10.1038/s41598-025-97506-1](https://doi.org/10.1038/s41598-025-97506-1)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Autores da India e Arabia Saudita; dataset publico UCI originario do Ensino Superior em Portugal (Martins et al., 2021).

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Superior (Higher Education) — **Motivo de exclusao na Fase 2 (EC2):** embora triado inicialmente como K-12 na Fase 1, a leitura integral comprova que o dataset utilizado refere-se a estudantes universitarios e nao contempla fatores socioemocionais ou recusa escolar.
- **Faixa Etaria / Amostra ($N$):** N = 4.424 registros de estudantes (2.209 Graduate, 1.421 Dropout, 794 Enrolled), com 36 features.
- **Publico-alvo Avaliado:** Estudantes de Ensino Superior classificados em tres classes (Dropout, Enrolled, Graduate).
- **Fonte dos Dados / Dataset:** Dataset publico UCI Machine Learning Repository (*Predict Student Dropout and Academic Success*).

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** N/A (nao utiliza instrumentos psicometricos).
- **Natureza da Ferramenta:** N/A.
- **Forma de Aplicacao:** N/A.
- **Finalidade:** N/A.

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Machine Learning Supervisionado (Ensemble Ponderado com Otimizacao Meta-heuristica), Tecnicas de Balanceamento de Dados e XAI (SHAP).
- **Algoritmos Empregados:** Random_Forest (RF) e XGBoost (XGB) em ensemble ponderado otimizado por Particle Swarm Optimization (PSO), comparados a Ant Colony Optimization (ACO), Firefly Algorithm (FA), Logistic Regression (LR), Decision Tree (DT), KNN, CNN, LSTM, CNN+LSTM, CatBoost+Optuna e LightGBM+Optuna. Balanceamento: SMOTE, ADASYN e Random Under-sampling (RU).
- **Tarefa do Modelo:** Classificacao multiclasse (Dropout, Enrolled, Graduate).
- **Estagio de Deteccao:** Predicao precoce de evasao academica em plataformas de ensino superior/smart education.

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Nenhuma (o estudo apenas menciona bem-estar mental e estresse de forma generica na introducao e conclusao, sem incluir variaveis psicologicas no modelo).
- **Variaveis Comportamentais / Historico:** Desempenho academico semestral (unidades curriculares aprovadas no 1o e 2o semestres, notas de admissao) e situacao de pagamento de mensalidades (tuition fees up to date).
- **Variaveis Familiares / Sociodemograficas:** Genero, nacionalidade, estado civil, ocupacao parental e bolsa de estudos (scholarship).
- **Variaveis Institucionais / Contextuais:** Indicadores macroeconomicos e institucionais (PIB/GDP, taxa de inflacao).
- **Features Mais Relevantes Identificadas:** Via SHAP: (1) Curricular units 2nd sem (approved) (~0,8), (2) Curricular units 1st sem (approved) (~0,5), (3) Tuition fees up to date (~0,5); importancia intermediaria para bolsa de estudos, nota de admissao, PIB e taxa de inflacao; menor importancia (< 0,1) para nacionalidade, estado civil e ocupacao parental.

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** N/A.
- **Metricas Computacionais (ML):** Modelo proposto (PSO-Weighted Ensemble RF+XGB com SMOTE): Acuracia = 86%, AUC-ROC = 0,9593, Macro F1-Score = 0,8633 (Precisao = 0,8633, Recall = 0,86). Por classe: Dropout (F1 = 0,88, Precisao = 0,93, Recall = 0,83, Acuracia = 0,86), Enrolled (F1 = 0,84, Precisao = 0,82, Recall = 0,86), Graduate (F1 = 0,87, Precisao = 0,84, Recall = 0,89). Comparado a ACO (83%, AUC 0,9490) e Firefly (85%, AUC 0,9575). Analise multicriterio TOPSIS (C* = 1,0000 para PSO) e paired t-test (p <= 0,01 contra todos os comparadores).
- **Estrategia de Validacao:** Split treino/teste (80% treino, 20% teste), 10 execucoes para comparacao de estabilidade dos otimizadores, teste t pareado e TOPSIS.
- **Desafios Metodologicos Relatados:** Forte desbalanceamento de classes no dataset original (especialmente classe Enrolled com baixo F1 = 0,305-0,471 sem balanceamento) e custo computacional de ajuste de hiperparametros.
- **Aspectos Eticos e Transparencia (XAI):** Aplica SHAP (TreeSHAP) para interpretabilidade global e local das predicoes; menciona conformidade com leis de privacidade de dados estudantis como requisito para implantacao real.
- **Limitacoes Declaradas:** Generalizacao limitada entre diferentes instituicoes educacionais e escalabilidade para grandes conjuntos de dados.
- **Direcoes Futuras:** Integracao em sistemas de gestao academica com retreinamento periodico anual, exploracao de arquiteturas de Deep Learning e ampliacao de tecnicas de XAI.

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo claramente definido: propor um framework ensemble ponderado por PSO com SMOTE para predicao de evasao estudantil em dados desbalanceados. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Pipeline detalhado (SMOTE/ADASYN/RU, espaco de busca de hiperparametros, pesos PSO, split 80/20, TOPSIS e paired t-test). |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Reporta Acuracia, Precisao, Recall, F1-Score por classe, Macro F1, AUC-ROC, matrizes de confusao, curvas ROC/PR e testes estatisticos. |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 0 | Nao contempla variaveis socioemocionais, psicologicas ou de recusa escolar (dataset exclusivamente academico, administrativo e macroeconomico do Ensino Superior; excluido por EC2). |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 1 | Menciona brevemente limitacoes de generalizacao institucional, escalabilidade e privacidade, sem aprofundar vieses de geracao sintetica (SMOTE) ou do dataset UCI. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **7 / 10** | |

---

---

## S0153: Transactions between Problem Behaviors and Academic Performance in Early Childhood

> - **ID do Estudo:** `S0153`
> - **Autores:** Chin-Chih Chen, Sheng-Lun Cheng, Yaoying Xu, Kathleen Rudasill, Reed Senter, Fa Zhang, Melissa Washington-Nortey, Nikki Adams
> - **Ano:** 2022
> - **Veículo (Venue):** *International Journal of Environmental Research and Public Health*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus']`)
> - **DOI:** [10.3390/ijerph19159583](https://doi.org/10.3390/ijerph19159583)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/85136341980?origin=resultslist)
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC2 (Fora de Escopo / Sem Desfecho de Absenteismo ou Recusa Escolar)]`

---

### 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0153`
- **Titulo Completo:** Transactions between Problem Behaviors and Academic Performance in Early Childhood
- **Autores:** Chin-Chih Chen, Sheng-Lun Cheng, Yaoying Xu, Kathleen Rudasill, Reed Senter, Fa Zhang, Melissa Washington-Nortey, Nikki Adams
- **Ano de Publicacao:** 2022
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** International Journal of Environmental Research and Public Health
- **DOI:** [10.3390/ijerph19159583](https://doi.org/10.3390/ijerph19159583)
- **Base de Dados:** Scopus
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (EUA)

---

### 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Jardim de Infancia ao 3o ano do Ensino Fundamental - K-3)
- **Faixa Etaria / Amostra ($N$):** N = 18.135 estudantes (51,22% meninos, n = 9.288; 48,78% meninas, n = 8.847); idade media inicial de 73,44 meses (DP = 4,47) no Jardim de Infancia (T1)
- **Publico-alvo Avaliado:** Criancas norte-americanas acompanhadas longitudinalmente do Jardim de Infancia ao 3o ano (sem avaliacao direta de absenteismo ou recusa escolar)
- **Fonte dos Dados / Dataset:** Early Childhood Longitudinal Study, Kindergarten Class of 2011 (ECLS-K: 2011), amostra probabilistica multiestagio nacionalmente representativa dos EUA (970 escolas em 90 PSUs)

---

### 3. Extracao Orientada as Questoes de Pesquisa (RQs)

#### RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos
- **Nome do Instrumento/Escala:** Versao modificada do Social Skills Rating System (SSRS) para comportamentos internalizantes (4 itens) e externalizantes (5 itens); avaliacoes diretas de leitura (EBRS/SERS) e matematica via Teoria de Resposta ao Item (IRT)
- **Natureza da Ferramenta:** Escala psicometrica comportamental (Likert de 4 pontos) combinada com avaliacoes academicas padronizadas baseadas em IRT
- **Forma de Aplicacao:** Relato dos professores (SSRS) e avaliacao direta da crianca (leitura e matematica)
- **Finalidade:** Avaliacao longitudinal de comportamentos problematicos e desempenho academico (nao realiza triagem de recusa escolar ou absenteismo)

#### RQ2: Abordagens Computacionais e de Inteligencia Artificial
- **Tipo de Abordagem:** Analise Estatistica Avancada / Modelagem de Equacoes Estruturais Longitudinal (Cross-Lagged Panel Modeling - CLPM com caminhos autorregressivos de segunda ordem AR2)
- **Algoritmos Empregados:** N/A (CLPM estimado em Mplus 8.4 via Full Information Maximum Likelihood - FIML, com pesos amostrais complexos e replicacao jackknife JK2; nao utiliza IA/ML)
- **Tarefa do Modelo:** Estimacao de relacoes bidirecionais/transacionais longitudinais entre comportamentos problematicos e desempenho academico em 4 ondas (T1-T4)
- **Estagio de Deteccao:** N/A (Estudo explicativo longitudinal sobre desempenho academico e comportamento; embora cite evasao escolar como motivacao, nao mensura nem prediz absenteismo, recusa escolar ou evasao)

#### RQ3: Variaveis e Features Consideradas
- **Variaveis Psicologicas/Socioemocionais:** Comportamentos internalizantes (baixa autoestima, ansiedade, solidao e tristeza)
- **Variaveis Comportamentais / Historico:** Comportamentos externalizantes (brigar, discutir, demonstrar raiva, agir impulsivamente e comportamentos disruptivos em aula) e desempenho academico composto (leitura e matematica)
- **Variaveis Familiares / Sociodemograficas:** Sexo e raca/etnia (covariaveis nos modelos); estrutura familiar, escolaridade parental e linha de pobreza (descritos na caracterizacao da amostra)
- **Variaveis Institucionais / Contextuais:** Escolas publicas e privadas da amostra ECLS-K: 2011
- **Features Mais Relevantes Identificadas:** Efeitos cross-lagged bidirecionais significativos: comportamentos internalizantes previram menor desempenho academico (beta = -0,052 em K->1o ano; -0,014 em 1o->2o; -0,013 em 2o->3o) e menor desempenho previu maior internalizacao (beta = -0,134; -0,170; -0,113); comportamentos externalizantes previram menor desempenho em K->1o (beta = -0,053) e 2o->3o (beta = -0,015), enquanto menor desempenho previu maior externalizacao em todos os intervalos (beta = -0,070; -0,045; -0,028)

#### RQ4: Metricas de Avaliacao, Desempenho e Limitacoes
- **Metricas Psicometricas:** Alfa de Cronbach: 0,89 (comportamentos internalizantes), 0,78 (comportamentos externalizantes), 0,95 (leitura) e 0,94 (matematica)
- **Metricas Computacionais (ML):** N/A (Indices de ajuste global do CLPM: modelo internalizante CFI = 0,980, TLI = 0,937, RMSEA = 0,046, SRMR = 0,057; modelo externalizante CFI = 0,973, TLI = 0,913, RMSEA = 0,059, SRMR = 0,068)
- **Estrategia de Validacao:** Modelagem longitudinal em 4 ondas com pesos amostrais complexos (W7C27P_2T270 e 80 pesos replicados via metodo jackknife pareado JK2) e FIML para dados faltantes
- **Desafios Metodologicos Relatados:** Tratamento de dados faltantes longitudinais em variaveis endogenas, desenho amostral complexo multiestagio e heterogeneidade na conceituacao de sintomas internalizantes
- **Aspectos Eticos e Transparencia (XAI):** Uso de base publica anonimizada (ECLS-K: 2011 / NCES)
- **Limitacoes Declaradas:** Escopo restrito a dois dominios comportamentais e um escore composto unico de leitura/matematica; avaliacao comportamental baseada exclusivamente no relato de professores (possivel vies de avaliacao); ausencia de analise de moderadores (genero, SES, racismo estrutural) e mediadores
- **Direcoes Futuras:** Examinar moderadores sociodemograficos (genero, nivel socioeconomico, raca/etnia) e mediadores (habilidades sociais, competencia com pares, comportamento evitativo de tarefas), desagregar ansiedade e depressao e utilizar multiplos informantes

---

### 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Objetivo explicitamente definido para testar relacoes transacionais entre comportamentos internalizantes/externalizantes e desempenho academico do K ao 3o ano. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Amostra representativa (N = 18.135), medidas SSRS/IRT e especificacao do CLPM com AR2, FIML e pesos JK2 em Mplus 8.4 descritas de forma replicavel. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 2 | Apresenta alfas de Cronbach (0,78 a 0,95) e indices de ajuste do modelo (CFI, TLI, RMSEA, SRMR). |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Analisa fatores internalizantes e externalizantes longitudinalmente, mas nao mensura nem analisa diretamente a recusa escolar ou o absenteismo (motivo de exclusao EC2 na Fase 2). |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discutem vies do informante unico (professores), agregacao de construtos (ansiedade/depressao e leitura/matematica) e necessidade de moderadores/mediadores. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **9 / 10** | |

---

---
