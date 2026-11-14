---
id: S0191
study_id: S0191
title: "Medical expert system as a chatbot for screening of anxiety disorders in children and adolescents"
year: 2026
database: "Scopus"
venue: "Journal of Medical Artificial Intelligence"
doi: "10.21037/jmai-24-366"
url: "https://www.scopus.com/pages/publications/105030280295?origin=resultslist"
status: "[Incluido Fase 2 - Extracao Concluida]"
qa_score: 9
population_scope: "Educação Básica (Adolescentes)"
intervention_scope: "Instrumentos Psicométricos combinados com Modelos Preditivos"
outcome_scope: "Rastreio e Diagnóstico de Recusa Escolar / EBSA"
authors:
  - "Venkateshwar Rao Madasu"
  - "Mohammadreza Hajiarbabi"
rqs:
  - "[[RQ1_Instrumentos_Psicometricos|RQ1]]"
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "[[SCARED]]"
algorithms:
  - "Forward Chaining Expert System (BPMN + AIML)"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/scopus
  - fenomeno/recusa_escolar
---
# S0191: Medical expert system as a chatbot for screening of anxiety disorders in children and adolescents

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0191`
> - **Autores:** Venkateshwar Rao Madasu, Mohammadreza Hajiarbabi
> - **Ano:** 2026
> - **Veículo (Venue):** *Journal of Medical Artificial Intelligence*
> - **Base de Origem:** `Scopus` (Bases: `['Scopus', 'Web of Science']`)
> - **DOI:** [10.21037/jmai-24-366](https://doi.org/10.21037/jmai-24-366)
> - **URL:** [Link da Publicação](https://www.scopus.com/pages/publications/105030280295?origin=resultslist)
> - **Status da Extração:** `[Incluido Fase 2 - Extracao Concluida]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> Background: Mental health disorders, particularly anxiety among children and adolescents, pose a significant global health challenge, often exacerbated by a severe shortage of specialized medical personnel and accessible diagnostic services, especially in low and middle-income countries. Early identification of anxiety disorder symptoms through systematic screening is crucial for timely intervention and prevention of associated developmental and physical health issues. This study aims to develop and evaluate a novel, accessible, and scalable medical expert system chatbot for the preliminary identification of anxiety disorders in children and adolescents. Methods: We implemented a self-assessment medical expert system as a chatbot, utilizing a forward-chaining inference methodology. The system integrates 41 standardized rules derived from the Screen for Child Anxiety Related Disorders (SCARED) questionnaire to identify symptoms across five specific anxiety disorder categories: panic disorder, generalized anxiety disorder, separation anxiety disorder, social anxiety disorder, and school avoidance. A key novelty of this expert system is the integration of business process model and notation (BPMN) with Artificial Intelligence Markup Language (AIML), which facilitates faster implementation and global deployment. An experimental study involving 100 participants (70 parents and 30 healthcare professionals) was conducted to assess the chatbot's performance and user acceptance. Results: The chatbot demonstrated high user acceptance, with 85% of participants finding it intuitive and 90% expressing satisfaction with its usability. In terms of performance, the system achieved a high concordance rate in identifying anxiety disorder symptom categories when compared to the expected outcomes based on SCARED questionnaire responses. Specifically, the chatbot accurately categorized symptoms for panic disorder, generalized anxiety disorder, separation anxiety disorder, social anxiety disorder, and school avoidance, offering a reliable 24/7 self-assessment service. Conclusions: This study successfully developed and evaluated a user-friendly and acceptable medical expert system chatbot for the preliminary identification of anxiety disorders in children and adolescents, addressing a critical gap in accessible mental healthcare. The novel BPMN-AIML integration proved effective in streamlining development and enhancing deployability. This system offers a scalable solution for early symptom identification, particularly beneficial in resource-limited settings, and lays foundational work for future expert systems in broader non-communicable diseases (NCDs). © AME Publishing Company.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Adolescentes)
- **Intervencao/Tecnologia (Intervention Scope):** Instrumentos Psicométricos combinados com Modelos Preditivos
- **Desfecho (Outcome Scope):** Rastreio e Diagnóstico de Recusa Escolar / EBSA
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de rastreio e diagnóstico de recusa escolar / ebsa na educação básica (adolescentes), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
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

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica (Criancas e Adolescentes, 6-18 anos)
- **Faixa Etaria / Amostra ($N$):** N = 100 participantes no estudo experimental (70 pais de criancas/adolescentes de 6-18 anos, idade media 41,5 anos, DP = 7,2, 65% mulheres; 30 profissionais de saude - pediatras, conselheiros escolares e psicologos infantis, idade media 38,1 anos, DP = 5,8, 70% mulheres)
- **Publico-alvo Avaliado:** Rastreio e identificacao preliminar de transtornos de ansiedade e [[Recusa_Escolar|evitacao escolar]] em criancas e adolescentes (6-18 anos)
- **Fonte dos Dados / Dataset:** Dados experimentais anonimizados coletados via interface web do chatbot administrando o questionario SCARED (41 itens) e pesquisa pos-interacao de aceitacao/usabilidade

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** [[SCARED]] (Screen for Child Anxiety Related Disorders - 41 itens, versao autorrelato e relato dos pais)
- **Natureza da Ferramenta:** Ferramenta digitalizada / Questionario de triagem psicometrica integrado a chatbot especialista
- **Forma de Aplicacao:** Autorrelato do aluno ou relato dos pais via interface conversacional web 24/7
- **Finalidade:** Triagem inicial / identificacao preliminar de sintomas em 5 categorias de ansiedade, incluindo evitacao escolar significativa (School Avoidance)

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** Sistema Especialista Baseado em Regras (Medical Expert System) / Chatbot Conversacional
- **Algoritmos Empregados:** Motor de inferencia por encadeamento para frente (Forward Chaining), modelagem de conhecimento via BPMN (Business Process Model and Notation) convertida em AIML (Artificial Intelligence Markup Language) por modelo de estados finitos
- **Tarefa do Modelo:** Classificacao multiclasse baseada em regras e limiares clinicos (somatorio de respostas 0/1/2 do SCARED para Panico >=7, Ansiedade Generalizada >=9, Separacao >=5, Fobia Social >=8 e Evitacao Escolar >=3)
- **Estagio de Deteccao:** Alerta precoce / triagem preventiva preliminar 24/7 para encaminhamento a avaliacao clinica especializada

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Sintomas de transtorno de panico/somaticos (13 itens), ansiedade generalizada (9 itens), ansiedade de separacao (8 itens), fobia social (7 itens) e evitacao escolar significativa (4 itens)
- **Variaveis Comportamentais / Historico:** Respostas somaticas e evitativas associadas a escola (ex.: dores de cabeca na escola, medo de dormir fora de casa, evitacao de pessoas desconhecidas)
- **Variaveis Familiares / Sociodemograficas:** Perspectiva parental (versao para pais do SCARED), idade/genero dos avaliadores e experiencia previa com interfaces digitais
- **Variaveis Institucionais / Contextuais:** Contexto de paises de baixa e media renda (LMICs) e ambientes com escassez de profissionais especializados em saude mental infantil
- **Features Mais Relevantes Identificadas:** Subescala de Evitacao Escolar do SCARED (itens 2, 11, 17 e 36 com limiar de corte >= 3) e demais 4 subescalas de ansiedade

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** Concordancia com os criterios padronizados de pontuacao do SCARED (92% para ansiedade generalizada e 89% para transtorno de panico; categorizacao correta nas 5 dimensoes incluindo evitacao escolar)
- **Metricas Computacionais (ML):** Taxa de concordancia com pontuacao esperada do SCARED (89% a 92% reportados) e avaliacao de aceitacao/usabilidade (85% consideraram intuitivo e facil de usar; 90% satisfeitos com o processo e feedback)
- **Estrategia de Validacao:** Estudo experimental com N = 100 participantes (70 pais e 30 profissionais de saude) recrutados em centro comunitario e convites online, comparando saidas do chatbot aos criterios do SCARED
- **Desafios Metodologicos Relatados:** Manutencao de contexto em conversas multi-turno, gerenciamento de dialogo para entradas ambiguas, representacao de conhecimento sem dependencia de engenheiros de IA e adaptabilidade linguistica/cultural
- **Aspectos Eticos e Transparencia (XAI):** Alta transparencia por raciocinio explicito baseado em regras (BPMN-AIML); discussao aprofundada sobre privacidade (GDPR/HIPAA), consentimento parental para menores, risco de sobrediagnostico, medicalizacao de comportamento normal e sobrecarga do sistema de saude
- **Limitacoes Declaradas:** Identificacao apenas preliminar (nao substitui diagnostico clinico); dependencia da precisao do relato do usuario; necessidade de adaptacao linguistica e cultural; dados empiricos limitados (amostra de 100 participantes)
- **Direcoes Futuras:** Integrar algoritmos de ML e NLP/NLU para compreensao de linguagem natural, decisoes sensiveis ao contexto clinico, integracao com IoT/wearables e aprendizado continuo da base de conhecimento

---

## 4. Avaliacao de Qualidade Metodologica (QA)
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

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- **[EM DUVIDA - Reuniao]:** Foca em triagem de transtornos de ansiedade (SCARED); o absenteismo/evitacao escolar aparece apenas como subescala secundaria.
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
