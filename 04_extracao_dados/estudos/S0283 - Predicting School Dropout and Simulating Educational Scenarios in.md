---
id: S0283
study_id: S0283
title: "Predicting School Dropout and Simulating Educational Scenarios in Colombia Using Machine Learning"
year: 2025
database: "IEEE Xplore"
venue: "2025 IEEE VIII Congreso Internacional en Inteligencia Ambiental, Ingenieria de Software y Salud Electronica y Movil (AmITIC)"
doi: "10.1109/AmITIC68284.2025.11214605"
url: ""
status: "[Incluido Fase 2 - Extracao Concluida]"
qa_score: 6
population_scope: "Educação Básica (Colômbia)"
intervention_scope: "Redes Neurais, SVM, Árvores de Decisão"
outcome_scope: "Predição de Evasão Escolar e Simulação de Intervenções"
authors:
  - "Mairely Narvaez Fernandez"
  - "Fernando Rafael Morales Nuñez"
  - "Ruthber Rodrȷguez Serrezuela"
  - "Daniel Felipe Bermeo Cuenca"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
  - "Redes Neurais / Deep Learning"
  - "SVM"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/ieee_xplore
  - fenomeno/absenteismo_cronico
---
# S0283: Predicting School Dropout and Simulating Educational Scenarios in Colombia Using Machine Learning

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0283`
> - **Autores:** Mairely Narvaez Fernandez, Fernando Rafael Morales Nuñez, Ruthber Rodrȷguez Serrezuela, Daniel Felipe Bermeo Cuenca
> - **Ano:** 2025
> - **Veículo (Venue):** *2025 IEEE VIII Congreso Internacional en Inteligencia Ambiental, Ingenieria de Software y Salud Electronica y Movil (AmITIC)*
> - **Base de Origem:** `IEEE Xplore` (Bases: `['IEEE Xplore']`)
> - **DOI:** [10.1109/AmITIC68284.2025.11214605](https://doi.org/10.1109/AmITIC68284.2025.11214605)
> - **URL:** Não informado
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> School dropout continues to be a critical issue affecting the Colombian educational system, particularly among socioeconomically vulnerable populations. This study presents the design and implementation of an intelligent software platform that leverages Machine Learning (ML) algorithms to predict student dropout risk and simulate the impact of future educational interventions. Using historical data from national databases and local institutions, various predictive models-including decision trees, support vector machines, and artificial neural networks-were developed and evaluated. The best-performing model, based on neural networks, achieved over 85% accuracy in identifying students at high risk of dropping out. In addition to prediction, the system incorporates a simulation module that enables educational stakeholders to explore the effects of policy changes-such as increased access to subsidies, improved teacher quality, or expanded enrollment-within a controlled virtual environment. This dual approach not only supports data-driven decision-making but also enhances the equity and efficiency of educational interventions. By combining predictive analytics and scenario modeling, this research contributes a novel methodology and practical tool for addressing dropout in complex educational ecosystems. The proposed solution promotes early intervention and fosters the development of more inclusive and sustainable public policies in education.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Colômbia)
- **Intervencao/Tecnologia (Intervention Scope):** Redes Neurais, SVM, Árvores de Decisão
- **Desfecho (Outcome Scope):** Predição de Evasão Escolar e Simulação de Intervenções
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve e avalia modelos de Machine Learning (Redes Neurais, SVM, Árvores de Decisão com acurácia >85%) para predição precoce de evasão escolar e simulação de intervenções em estudantes vulneráveis do ensino básico. Responde a RQ2 e RQ4.

---

## 1. Identificacao e Metadados Detalhados
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

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica / Ensino Secundario (Colombia)
- **Faixa Etaria / Amostra ($N$):** N = 2.000 estudantes do ensino secundario (analise de fatores preditivos); validacao de campo piloto com N = 120 usuarios finais (gestores escolares, professores e assessores de politicas publicas)
- **Publico-alvo Avaliado:** Estudantes do ensino secundario em contextos socioeconomicos vulneraveis (predicao de risco de evasao escolar e simulacao de cenarios de intervencao)
- **Fonte dos Dados / Dataset:** Repositorios nacionais oficiais (Ministerio da Educacao da Colombia e Departamento Nacional de Estatistica) e instituicoes educacionais locais (nota: o texto menciona "hypothetical dataset" na Secao III-A para os 2.000 estudantes)

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** N/A (nao utiliza instrumento psicometrico padronizado)
- **Natureza da Ferramenta:** Registros administrativos/academicos e indicadores autorrelatados de saude mental (sem especificacao de escala clinica validada)
- **Forma de Aplicacao:** Registros institucionais e autorrelato dos alunos (para ansiedade e depressao)
- **Finalidade:** Triagem inicial de risco de evasao integrada a sistema de apoio a decisao

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Machine Learning Supervisionado + Simulacao de Cenarios baseada em Dinamica de Sistemas (System Dynamics), integrados na plataforma `EduAnalytics Huila` ([[Early_Warning_Systems]])
- **Algoritmos Empregados:** Artificial Neural Networks (ANN), Support Vector Machines (SVM), Decision Trees (DT)
- **Tarefa do Modelo:** Classificacao binaria (risco de evasao escolar) combinada com simulacao dinamica do impacto de politicas educacionais
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva ([[Early_Warning_Systems]]) e simulacao ex-ante de intervencoes

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Ansiedade ou depressao autorrelatadas (presentes em 42% dos casos de evasao, p < 0,01), perda de confianca e desmotivacao academica
- **Variaveis Comportamentais / Historico:** Baixo desempenho academico em matematica e leitura (72% dos evadidos, p < 0,001), [[Absenteismo_Cronico]] (>20% do ano letivo; 65% dos evadidos, p < 0,001), repetencia escolar
- **Variaveis Familiares / Sociodemograficas:** Baixo nivel socioeconomico / renda familiar / instabilidade habitacional (58% dos evadidos, p < 0,01), pais sem ensino medio completo (49% dos evadidos, p < 0,05)
- **Variaveis Institucionais / Contextuais:** Infraestrutura escolar, razao professor-aluno, acesso a subsidios educacionais, programas de apoio em saude mental e aconselhamento
- **Features Mais Relevantes Identificadas:** Baixo desempenho em matematica e leitura (72%), [[Absenteismo_Cronico]] >20% (65%), baixo nivel socioeconomico (58%), baixa escolaridade dos pais (49%) e ansiedade/depressao autorrelatada (42%)

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A (nao aplicavel; sem validacao psicometrica de escalas)
- **Metricas Computacionais (ML):** ANN: Acuracia = 85,4%, F1-Score = 0,84, ROC-AUC = 0,88; SVM: Acuracia = 81,2%; Decision Trees: Acuracia = 77,3%. Validacao de campo (N=120): 91% facilidade de uso (p < 0,001), 88% melhoria na identificacao precoce (p < 0,001), 84% eficacia para intervencoes direcionadas (p < 0,01), 79% viabilidade em baixo recurso (p < 0,01), 87% valor para politicas publicas (p < 0,001)
- **Estrategia de Validacao:** Validacao cruzada estratificada (stratified cross-validation) e validacao piloto em campo via entrevistas e estudos de caso (N = 120)
- **Desafios Metodologicos Relatados:** Natureza multifatorial e nao linear da evasao, limitacoes de infraestrutura em escolas de baixos recursos, interpretabilidade para usuarios nao tecnicos
- **Aspectos Eticos e Transparencia (XAI):** Anonimizacao dos dados; interface visual exploratoria (mapas de calor de correlacao e histogramas) voltada a gestores sem formacao tecnica, embora nao empregue metodos formais de XAI (ex.: SHAP/LIME)
- **Limitacoes Declaradas:** Os autores nao apresentam secao dedicada a limitacoes; mencionam apenas menor profundidade analitica das Arvores de Decisao frente as ANNs e referem "hypothetical dataset" na Secao III-A sem detalhar hiperparametros ou divisao exata treino/teste
- **Direcoes Futuras:** Ampliar a adocao da plataforma para planejamento de politicas publicas e reformas educacionais abrangentes orientadas a equidade

---

## 4. Avaliacao de Qualidade Metodologica (QA)
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

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
