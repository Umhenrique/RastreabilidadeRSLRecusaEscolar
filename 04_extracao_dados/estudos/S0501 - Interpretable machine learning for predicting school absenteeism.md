---
id: S0501
study_id: S0501
title: "Interpretable machine learning for predicting school absenteeism at-scale in Brazil: evidence from 22,000 schools"
year: 2026
database: "Springer Link"
venue: "Scientific Reports"
doi: "10.1038/s41598-026-48729-3"
url: "https://link.springer.com/article/10.1038/s41598-026-48729-3"
status: "[Incluido Fase 2 - Extracao Concluida]"
qa_score: 9
population_scope: "Educação Básica (K-12)"
intervention_scope: "Instrumentos Psicométricos combinados com Modelos Preditivos"
outcome_scope: "Predição de Absenteísmo Crônico Escolar"
authors:
  - "Abílio Nogueira Barros, Felipe Vieira Roque, Tiago Paulino, Augusto Schmidt, Flavia Galvani, Rafael Oliveira, Leonardo Brandão Marques, Diego Dermeval, Anita Gea Martinez Stefani, Marisa de Santana da Costa, Emanuel Marques Queiroga, Elthon Oliveira, Cristian Cechinel, Thales Vieira"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
algorithms:
  - "[[Random_Forest]]"
  - "[[XGBoost]]"
  - "[[LightGBM]]"
  - "[[CatBoost]]"
  - "[[Regressao_Logistica]]"
  - "[[Explicabilidade_XAI]]"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/springer_link
  - fenomeno/absenteismo_cronico
---
# S0501: Interpretable machine learning for predicting school absenteeism at-scale in Brazil: evidence from 22,000 schools

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0501`
> - **Autores:** Abílio Nogueira Barros, Felipe Vieira Roque, Tiago Paulino, Augusto Schmidt, Flavia Galvani, Rafael Oliveira, Leonardo Brandão Marques, Diego Dermeval, Anita Gea Martinez Stefani, Marisa de Santana da Costa, Emanuel Marques Queiroga, Elthon Oliveira, Cristian Cechinel, Thales Vieira
> - **Ano:** 2026
> - **Veículo (Venue):** *Scientific Reports*
> - **Base de Origem:** `Springer Link` (Bases: `['Springer Link']`)
> - **DOI:** [10.1038/s41598-026-48729-3](https://doi.org/10.1038/s41598-026-48729-3)
> - **URL:** [Link da Publicação](https://link.springer.com/article/10.1038/s41598-026-48729-3)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Resumo não disponível na base de origem.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (K-12)
- **Intervencao/Tecnologia (Intervention Scope):** Instrumentos Psicométricos combinados com Modelos Preditivos
- **Desfecho (Outcome Scope):** Predição de Absenteísmo Crônico Escolar
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de predição de absenteísmo crônico escolar na educação básica (k-12), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
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

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Ensino Médio (Educação Básica / K-12)
- **Faixa Etaria / Amostra ($N$):** N = 22.476 escolas brasileiras de Ensino Médio (filtradas de 29.993 escolas no Censo Escolar 2024 após integração com SGP), estratificadas em 6 níveis do Indicador de Complexidade de Gestão da Escola (ICG 1 a 6). Análise em nível institucional (escolar), sem dados individuais de alunos.
- **Publico-alvo Avaliado:** Escolas públicas/participantes de Ensino Médio no Brasil classificadas quanto ao risco sistêmico de absenteísmo escolar elevado.
- **Fonte dos Dados / Dataset:** Consolidação de três fontes oficiais brasileiras (INEP/MEC, ano-base 2024): (1) Sistema Gestão Presente (SGP, registros de frequência de estudantes do Ensino Médio); (2) Censo Escolar da Educação Básica 2024; (3) Indicador de Complexidade de Gestão da Escola (ICG 2024).

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** N/A (não utiliza escalas psicométricas; emprega as faixas de absenteísmo de Kearney [Low >=96%, Moderate 91-95%, Significant 81-90%, High 71-80%, Severe <=70%] apenas como critério de rotulagem da variável-alvo a partir de registros administrativos de frequência).
- **Natureza da Ferramenta:** N/A (baseada exclusivamente em registros administrativos educacionais e censo escolar).
- **Forma de Aplicacao:** N/A (coleta administrativa automatizada via SGP e Censo Escolar/INEP).
- **Finalidade:** Classificação institucional de risco de absenteísmo escolar elevado para apoio a políticas públicas.

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** [[Machine_Learning]] Supervisionado, [[Early_Warning_Systems]] em nível institucional, [[Explicabilidade_XAI]] (SHAP e análise de sensibilidade contrafactual "what-if").
- **Algoritmos Empregados:** [[Random_Forest]] (modelo principal selecionado pelo equilíbrio entre desempenho, interpretabilidade e equivalência estatística via teste de DeLong), [[CatBoost]], [[XGBoost]], [[LightGBM]] e [[Regressao_Logistica]] (baseline linear). Seleção de atributos via Informação Mútua + Mean Decrease in Impurity (MDI) do Random Forest (cutoff = 0.01, ~35 features por ICG); balanceamento via SMOTE.
- **Tarefa do Modelo:** Classificação binária em nível escolar (por faixa de ICG): Classe 1 (baixo risco: >50% dos alunos com frequência Low/Moderate) vs. Classe 0 (alto risco: >50% dos alunos com frequência Significant/High/Severe).
- **Estagio de Deteccao:** Alerta precoce institucional e diagnóstico exploratório de fatores estruturais/organizacionais associados ao absenteísmo.

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** N/A (o estudo opera exclusivamente no nível agregado da escola e declara explicitamente a ausência de variáveis socioemocionais ou psicológicas individuais).
- **Variaveis Comportamentais / Historico:** Taxa agregada de frequência escolar no Ensino Médio (SGP 2024) usada para compor a variável-alvo binária por escola.
- **Variaveis Familiares / Sociodemograficas:** N/A no nível individual; contexto regional capturado indiretamente por localização urbano/rural (`tp_location`) e composição de modalidades (regular, técnico, EJA).
- **Variaveis Institucionais / Contextuais:** ~350 atributos iniciais do Censo Escolar (294 após filtragem de correlação >0.85 e baixa informação mútua), agrupados em: (a) infraestrutura (`qt_classroom_used`, `qt_classroom_aircon`, `qt_pc_student`, `qt_projector`, `qt_tv`, `in_distance_learning`, `in_sewage_public`, `in_sewage_septic`, `in_material_none`); (b) recursos humanos (`qt_teacher_hs`, `qt_pedagogical_staff`, `qt_general_staff`, `qt_librarian_staff`, `qt_food_staff`, `qt_admin_staff`); (c) organização/governança (`in_regular`, `in_parent_teacher_association`, `qt_enroll_hs`, `qt_enroll_tech_hs`, `qt_class_hs`, `tp_location`) e estratificação pelo ICG (níveis 1 a 6).
- **Features Mais Relevantes Identificadas:** Via MDI e SHAP, `qt_pc_student`, `qt_pedagogical_staff`, `qt_teacher_hs` e `qt_class_hs` figuraram em 5 dos 6 modelos. `in_regular` destacou-se no ICG 1; `qt_classroom_aircon` nos ICGs 2, 3, 4 e 6 (Flip Rate >4% no ICG 3); `qt_pedagogical_staff` e `in_distance_learning` nos ICGs 5 e 6. Nas simulações contrafactuais (+1 DP), a taxa de reversão (Flip Rate 0->1) foi de 49,38% no ICG 1, 16,29% no ICG 2, 18,84% no ICG 3, 8,55% no ICG 4, 2,60% no ICG 5 e 0,57% no ICG 6.

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A.
- **Metricas Computacionais (ML):** Acurácia, Precisão, Recall, F1-Score e teste de DeLong para AUC-ROC (sem diferença estatística entre RF e CatBoost). Desempenho do Random Forest no conjunto de teste: ICG 1 (Acc=0,85; Prec=0,76; Rec=0,89; F1=0,81), ICG 2 (Acc=0,75; Prec=0,76; Rec=0,82; F1=0,79), ICG 3 (Acc=0,67; Prec=0,68; Rec=0,81; F1=0,74), ICG 4 (Acc=0,74; Prec=0,69; Rec=0,64; F1=0,67), ICG 5 (Acc=0,78; Prec=0,80; Rec=0,72; F1=0,75), ICG 6 (Acc=0,84; Prec=0,86; Rec=0,43; F1=0,58). CatBoost obteve leve vantagem em ICG 3 (Acc=0,71; F1=0,77) e ICG 4 (Acc=0,75; F1=0,68).
- **Estrategia de Validacao:** Split estratificado 75/25 treino/teste com validação cruzada estratificada 5-fold (`StratifiedKFold`, k=5) e grid-search no conjunto de treino; comparação estatística de AUC-ROC via teste de DeLong.
- **Desafios Metodologicos Relatados:** Desbalanceamento de classes entre ICGs (54,70% classe 0 vs. 45,30% classe 1 no total, chegando a 75% classe 0 no ICG 6), mitigado com SMOTE; alta dispersão/desigualdade estrutural nas variáveis escolares; baixo recall no ICG 6 (0,43 no RF); risco de interpretar variáveis proxy (como ar-condicionado) como alavancas causais diretas.
- **Aspectos Eticos e Transparencia (XAI):** Conformidade com a LGPD (dados do SGP restritos por conterem informações sensíveis ligadas a programa de transferência de renda); uso de SHAP e simulações contrafactuais para transparência; alerta explícito contra interpretações causais/prescritivas diretas.
- **Limitacoes Declaradas:** Granularidade agregada em nível escolar (não individual por estudante), omitindo fatores pessoais, familiares e socioemocionais; natureza observacional/associativa (não causal); dependência da qualidade dos registros administrativos; presença de variáveis proxy socioeconômicas.
- **Direcoes Futuras:** Estender a modelagem para o nível individual do aluno integrando Censo Escolar, histórico individual de frequência, dados sociodemográficos e indicadores de vizinhança; avaliar LIME e Anchors; incorporar técnicas de fairness-aware ML.

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
1. **Dados de entrada para identificar ansiedade/sofrimento:** Nao informado no artigo / Nao aplicavel. O estudo nao coleta nem utiliza dados de entrada, escalas psicometricas ou questionarios para identificar ansiedade, depressao ou sofrimento socioemocional individual dos alunos. Toda a modelagem opera exclusivamente em nivel institucional agregado (escola), utilizando registros administrativos governamentais (variaveis tabulares do Censo Escolar 2024 normalizadas pelo numero de matriculas e codificadas via *one-hot encoding*, estratificadas pelo ICG 2024, e percentuais de frequencia escolar do Sistema Gestao Presente - SGP 2024 convertidos em rotulo binario de risco escolar segundo as faixas de Kearney [2021]). A fonte dos dados e exclusivamente estatal (INEP e Ministerio da Educacao - MEC), sem informantes alunos, pais, professores ou equipe clinica, e a periodicidade e anual (recorte transversal consolidado referente ao ano-base de 2024).
2. **Inventario completo de variaveis e justificativa de escolha:** Partindo de ~350 atributos brutos resultantes da integracao SGP + Censo Escolar 2024 + ICG 2024, apos curadoria manual (exclusao de variaveis de Ensino Fundamental, EJA e infraestrutura nao vinculada ao Ensino Medio), normalizacao por matriculas e filtragem por informacao mutua (< 0,04 / < 0,05 conforme texto) e alta correlacao (> 0,85), restaram **294 atributos** para 22.476 escolas, dos quais ~35 atributos por nivel de ICG foram selecionados via *Random Forest Mean Decrease in Impurity* (cutoff = 0,01). Os autores informam explicitamente que nem todas as 294/35 variaveis sao listadas nas tabelas por alta granularidade, apresentando na Tabela 2 uma lista representativa de 21 variaveis organizadas em tres dominios principais (alem da variavel de estratificacao ICG e da variavel-alvo `Flag Absenteeism`): (a) **Infraestrutura escolar e recursos tecnologicos/pedagogicos:** `qt_classroom_used` (salas usadas), `qt_classroom_aircon` (salas com ar-condicionado), `qt_pc_student` (computadores portateis por aluno), `qt_projector` (projetores), `qt_tv` (televisores), `in_distance_learning` (mediacao por educacao a distancia), `in_material_none` (ausencia de materiais socioculturais/pedagogicos), `in_sewage_public` (esgoto em rede publica), `in_sewage_septic` (fossa septica); (b) **Recursos humanos:** `qt_teacher_hs` (professores do Ensino Medio), `qt_pedagogical_staff` (equipe pedagogica: pedagogos, coordenadores, orientadores), `qt_general_staff` (servicos gerais), `qt_librarian_staff` (bibliotecarios), `qt_food_staff` (alimentacao), `qt_admin_staff` (equipe administrativa/gestao); (c) **Organizacao escolar, matriculas e contexto regional:** `in_regular` (modalidade regular), `in_parent_teacher_association` (Associacao de Pais e Mestres), `qt_enroll_hs` (matriculas no Ensino Medio), `qt_enroll_tech_hs` (matriculas no Ensino Medio tecnico), `qt_class_hs` (turmas do Ensino Medio) e `tp_location` (urbano/rural). **Justificativa de escolha:** os autores justificam a selecao por (i) disponibilidade nacional em sistemas oficiais quando dados individuais sao restritos ou ausentes, permitindo apoiar decisoes de politica publica em infraestrutura e pessoal (Queiroga et al., 2024; Masci et al., 2018); (ii) heterogeneidade estrutural das escolas brasileiras, justificando a estratificacao pelos 6 niveis do ICG (porte, turnos, etapas); (iii) foco em absenteismo sistemico institucional via regra de maioria (>50% nas faixas de Kearney), escolhida apos testar limiares de 30%, 40% e 60% que degradaram o balanceamento; e (iv) evidencias de que condicoes fisicas/ambientais, densidade docente, suporte pedagogico e contexto urbano/rural moldam o engajamento e a permanencia escolar.
3. **Fundamentacao teorica do identificador:** O identificador apoia-se em: (a) **referencial conceitual de absenteismo:** as cinco faixas de gravidade de frequencia de Kearney (2021) (Low >=96%, Moderate 91–95%, Significant 81–90%, High 71–80%, Severe <=70%) usadas para rotular risco institucional; (b) **referencial institucional brasileiro:** o Indicador de Complexidade de Gestao da Escola (ICG, Nota Tecnica INEP nº 40/2014) para segmentacao contextual; (c) **referencial de *Learning Analytics* e *Early Warning Systems* institucionais:** modelos baseados em arvores (Ho, 1995; gradient boosting) voltados a gestores e politicas publicas; e (d) **IA Explicavel (XAI) e analise contrafactual:** valores SHAP baseados na teoria dos jogos cooperativos (Lundberg & Lee, 2017), *Mean Decrease in Impurity* (MDI), teste nao parametrico de DeLong (1988) para comparacao de AUC-ROC e simulacoes contrafactuais *what-if* (*Flip Rate* por perturbacao de ±1 DP e inversao binaria). Os autores adotam explicitamente uma fundamentacao **associativa e diagnostica**, rejeitando interpretacoes causais diretas dos modelos preditivos.
4. **Restricoes de recursos e limitacoes do trabalho:** **Dependencias e aplicabilidade:** o modelo depende integralmente de infraestrutura governamental centralizada de registros educacionais — integracao entre **SGP**, **Censo Escolar** e **ICG** (INEP/MEC) — e de autorizacao legal especifica junto ao MEC devido a restricoes da **LGPD** (os dados do SGP sao sensiveis por integrarem politicas de transferencia de renda). Na etapa de integracao, 29.993 escolas do Censo caem para 22.476 apos pareamento valido com o SGP, evidenciando dependencia critica da completude e qualidade dos registros administrativos. Por nao exigir aplicacao de testes psicologicos, tablets para estudantes ou equipe clinica nas escolas, o custo operacional incremental por escola e baixo (software Python aberto sobre bases oficiais). Contudo, para escolas com restricao de recursos, ha limitacoes praticas severas: o modelo nao detecta casos individuais de sofrimento psiquico ou recusa escolar; ha forte desigualdade estrutural nas variaveis (desvios padrao muito superiores as medias); preditores como `qt_classroom_aircon` atuam como **proxies socioeconomicas** e de capacidade de investimento municipal, gerando risco de alocacao equivocada caso gestores tomem correlacoes como prescricoes causais; e escolas de maior complexidade (ICG 6) tiveram baixo *recall* (0,43 no RF) e *Flip Rate* contrafactual quase nulo (0,57%), mostrando que contextos altamente complexos nao respondem a ajustes isolados. **Limitacoes declaradas pelos autores:** (i) granularidade exclusivamente agregada em nivel escolar (omite heterogeneidade individual, fatores pessoais, familiares e socioemocionais); (ii) natureza observacional/associativa e nao causal (presenca de variaveis proxy); (iii) dependencia da qualidade, integridade e granularidade dos registros administrativos; (iv) correlacoes elevadas entre preditores no ICG 1 e assimetria entre perturbacoes de +1 DP e -1 DP nas simulacoes contrafactuais; e (v) necessidade futura de incorporar outros metodos de XAI (LIME, Anchors) e tecnicas de *fairness-aware ML* para evitar reforco de desigualdades.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
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

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
