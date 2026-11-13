---
id: S0325
study_id: S0325
title: "Re-envisioning a K-12 Early Warning System with School Climate Factors"
year: 2022
database: "ACM DL"
venue: "Proceedings of the Ninth ACM Conference on Learning @ Scale"
doi: "10.1145/3491140.3528670"
url: "https://doi-org.ez13.periodicos.capes.gov.br/10.1145/3491140.3528670"
status: "[Pendente Leitura Completa]"
qa_score: 0
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
> - **Status da Extração:** `[Pendente Leitura Completa]`

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
- **Pais/Regiao de Realizacao do Estudo:** *(Preencher durante leitura completa)*

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Básico (K-12)
- **Faixa Etaria / Amostra ($N$):** *(Ex: N = 1.250 estudantes, 12-16 anos)*
- **Publico-alvo Avaliado:** Assiduidade Escolar + Aprendizagem Socioemocional
- **Fonte dos Dados / Dataset:** *(Ex: Sistema de Gestao Escolar, registros clinicos, questionarios)*

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** *(Identificar na leitura ou N/A)*
- **Natureza da Ferramenta:** (Instrumento psicometrico tradicional / Escala clinica / Ferramenta digitalizada / Questionario de triagem)
- **Forma de Aplicacao:** (Autorrelato do aluno / Relato dos pais / Relato dos professores / Entrevista clinica)
- **Finalidade:** (Diagnostico diferencial / Triagem inicial / Avaliacao de evolucao)

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** (Machine Learning Supervisionado / Nao Supervisionado / Deep Learning / Early Warning System - EWS / Analise Estatistica Avancada / XAI)
- **Algoritmos Empregados:** [[Early_Warning_Systems]]
- **Tarefa do Modelo:** (Classificacao binaria [risco sim/nao] / Regressao [probabilidade de infrequencia] / Clustering [perfis de comportamento])
- **Estagio de Deteccao:** (Alerta precoce / deteccao preventiva vs. diagnostico a posteriori)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** (Ansiedade de separacao, ansiedade social, depressao, estresse, regulacao emocional, somatizacao)
- **Variaveis Comportamentais / Historico:** (Padrao de faltas/atrasos, historico de notas, engajamento escolar, conflitos, bullying)
- **Variaveis Familiares / Sociodemograficas:** (Estrutura familiar, dinamica parental, renda, historico medico)
- **Variaveis Institucionais / Contextuais:** (Clima escolar, relacao professor-aluno, localizacao da escola)
- **Features Mais Relevantes Identificadas:** (Feature importance / SHAP / coeficientes principais)

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** (Alfa de Cronbach, Omega de McDonald, Validade convergente/discriminante)
- **Metricas Computacionais (ML):** (Acuracia, Sensibilidade/Recall, Precisao, F1-Score, AUC-ROC, MCC)
- **Estrategia de Validacao:** (K-Fold Cross-validation, split temporal treino/teste, validacao externa)
- **Desafios Metodologicos Relatados:** (Desbalanceamento de classes, dados faltantes/ruidosos, tamanho restrito da amostra)
- **Aspectos Eticos e Transparencia (XAI):** (Privacidade dos dados dos alunos, interpretabilidade do modelo, mitigacao de vies)
- **Limitacoes Declaradas:** 
- **Direcoes Futuras:** 

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 0 | |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 0 | |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 0 | |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 0 | |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 0 | |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **/ 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
