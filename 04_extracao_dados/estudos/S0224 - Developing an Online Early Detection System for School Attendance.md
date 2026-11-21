---
id: S0224
study_id: S0224
title: "Developing an Online Early Detection System for School Attendance Problems: Results From a Research-Community Partnership"
year: 2019
database: "ScienceDirect"
venue: "Cognitive and Behavioral Practice"
doi: "https://doi.org/10.1016/j.cbpra.2018.09.001"
url: "https://www.sciencedirect.com/science/article/pii/S1077722918300750"
status: "[Excluido Fase 2 - Criterio EC2 (Regressao linear classica sem escalas clinicas nem ML implementado)]"
qa_score: 8
population_scope: "Educação Básica (Ensino Fundamental Inicial)"
intervention_scope: "Modelos de Machine Learning / IA e Análise Preditiva"
outcome_scope: "Rastreio e Diagnóstico de Recusa Escolar / EBSA"
authors:
  - "Brian C. Chu"
  - "Denise Guarino"
  - "Christina Mele"
  - "Jean O’Connell"
  - "Patricia Coto"
rqs:
  - "[[RQ2_Modelos_IA_e_Predicao|RQ2]]"
  - "[[RQ3_Variaveis_Socioemocionais|RQ3]]"
  - "[[RQ4_Metricas_e_Desafios|RQ4]]"
scales:
  - "ACFS (Attendance and Critical Factors Survey)"
  - "District-Level School Refusal Survey"
algorithms:
  - "[[Early_Warning_Systems]]"
  - "Regressao Multipla Simultanea"
tags:
  - rsl/estudo
  - rsl/fase2_leitura_completa
  - base/sciencedirect
  - fenomeno/recusa_escolar
---
# S0224: Developing an Online Early Detection System for School Attendance Problems: Results From a Research-Community Partnership

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `S0224`
> - **Autores:** Brian C. Chu, Denise Guarino, Christina Mele, Jean O’Connell, Patricia Coto
> - **Ano:** 2019
> - **Veículo (Venue):** *Cognitive and Behavioral Practice*
> - **Base de Origem:** `ScienceDirect` (Bases: `['ScienceDirect']`)
> - **DOI:** [https://doi.org/10.1016/j.cbpra.2018.09.001](https://doi.org/https://doi.org/10.1016/j.cbpra.2018.09.001)
> - **URL:** [Link da Publicação](https://www.sciencedirect.com/science/article/pii/S1077722918300750)
> - **Status da Extração:** `[Excluido Fase 2 - Criterio EC2 (Regressao linear classica sem escalas clinicas nem ML implementado)]`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> School refusal and other school attendance problems are vexing problems for school-aged youth, families, school personnel, and clinicians. However, few resources exist to detect problematic attendance. The current report describes three steps of a research-community partnership to develop an early identification program to detect youth at risk for problematic attendance. First, a survey was conducted to estimate the scope and cost of school refusal across grades K–12. School administrators estimated relatively few youth exhibiting significant school refusal (missing 5 or more days per year) but estimated the costs associated with services for these youth to be very high (mean cost of in-district programs: $94,052; mean cost of out-of-district placements: $496,657). Second, elementary school counselors were tasked with tracking absenteeism among at-risk youth using an online attendance tracking prototype. Counselors identified a high number of youth who showed elevated absences, lates, or early departures (17.2% of enrolled students), and counselor ratings were significantly related to whether the student (a) had received an individualized education plan or 504 plan, (b) had a sibling with similar attendance problems, (c) was older, or (d) had divorced or separated parents. In a final step, counselor feedback was sought and revisions were incorporated in the attendance tracker. Findings reinforce the prevalence and cost of school attendance problems, provide guidance for using technology to monitor attendance and related indices (tardies, early departures), and direct attention to youth factors that may be useful in identifying youth at risk for poor attendance.

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** Educação Básica (Ensino Fundamental Inicial)
- **Intervencao/Tecnologia (Intervention Scope):** Modelos de Machine Learning / IA e Análise Preditiva
- **Desfecho (Outcome Scope):** Rastreio e Diagnóstico de Recusa Escolar / EBSA
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de rastreio e diagnóstico de recusa escolar / ebsa na educação básica (ensino fundamental inicial), associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `S0224`
- **Titulo Completo:** Developing an Online Early Detection System for School Attendance Problems: Results From a Research-Community Partnership
- **Autores:** Brian C. Chu, Denise Guarino, Christina Mele, Jean O’Connell, Patricia Coto
- **Ano de Publicacao:** 2019
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** Cognitive and Behavioral Practice
- **DOI:** [https://doi.org/10.1016/j.cbpra.2018.09.001](https://doi.org/https://doi.org/10.1016/j.cbpra.2018.09.001)
- **Base de Dados:** ScienceDirect
- **Pais/Regiao de Realizacao do Estudo:** Estados Unidos (tres distritos escolares suburbanos em estado do Medio Atlantico; referencia a codigo administrativo de Nova Jersey)

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** Educacao Basica — Passo 1: K-12 (3 distritos, 9.900 matriculados); Passo 2 e 3: Ensino Fundamental Inicial (Grades K-5, 4 escolas primarias, 2.372 matriculados)
- **Faixa Etaria / Amostra ($N$):** Passo 1: 3 diretores de servicos estudantis/especiais (cobrindo 9.900 alunos). Passo 2: 4 conselheiros escolares e 1 assistente administrativo monitorando 2.372 alunos (idades 5-11 anos; 63% brancos, 28% asiaticos, 7% hispanicos, 1% negros, 1% outros; 2,2% elegiveis para almoco gratuito/reduzido), dos quais N = 409 estudantes (17,2%) atingiram o limiar de >=5 faltas ou atrasos (175 meninas [42,8%], 234 meninos [57,2%]; idade M = 8,18 anos, DP = 1,89, faixa 5-12; serie M = 2,6, DP = 1,75)
- **Publico-alvo Avaliado:** Estudantes da educacao basica em risco de recusa escolar (*School Refusal* - SR) e problemas de frequencia escolar (*School Attendance Problems* - SAPs)
- **Fonte dos Dados / Dataset:** Questionario distrital de diretores (Passo 1), sistema administrativo escolar de presenca + planilha Google Tables com avaliacoes de conselheiros no ACFS ao longo de 1 ano letivo / 180 dias / 4 periodos trimestrais (Passo 2), e feedback qualitativo dos conselheiros (Passo 3)

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** *District-Level School Refusal Survey* (criado para o Passo 1) e *Attendance and Critical Factors Survey* (ACFS, 31 itens criados para o Passo 2; sem escalas clinicas padronizadas devido a restricoes praticas de tempo)
- **Natureza da Ferramenta:** Questionario institucional de estimativa de custos/prevalencia (Passo 1) + checklist digitalizado de rastreio psicossocial e frequencia em Google Tables (Passo 2)
- **Forma de Aplicacao:** Relato de diretores distritais (Passo 1) e relato dos conselheiros escolares baseado em interacoes/familiaridade com pais e alunos quando o aluno atinge >=5 faltas (Passo 2)
- **Finalidade:** Triagem inicial e monitoramento longitudinal continuo (4 periodos trimestrais) de problemas emergentes de frequencia escolar e recusa escolar

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** [[Early_Warning_Systems|Sistema de Deteccao Precoce Online]] (prototipo em Google Tables com alerta por limiar >=5 faltas e classificacao revisada por cores verde/amarelo/vermelho) + Analise Estatistica (3 Regressoes Multiplas Simultaneas e ANOVAs). Nao implementa Machine Learning neste piloto (ML e citado explicitamente apenas como direcao futura)
- **Algoritmos Empregados:** Regressao Linear Multipla Simultanea (3 modelos separados para faltas, atrasos e saidas antecipadas) e ANOVA unidirecional (comparacao por sexo)
- **Tarefa do Modelo:** Regressao explicativa/preditiva continua sobre contagem anual de faltas (*absences*), atrasos (*lates*) e saidas antecipadas (*early departures*)
- **Estagio de Deteccao:** Alerta precoce / deteccao preventiva (limiar >=5 faltas ou atrasos antes da cronicidade de 10+ ou 15+ dias)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** Passo 1 estimou casos de faltas ligadas a ansiedade ou problemas de humor/depressao; Passo 2 avaliou posse de Plano 504 ou IEP (incluindo comprometimento emocional/comportamental), presenca de ao menos um bom amigo, qualidade das amizades (0-10) e participacao em atividades extracurriculares (0-10)
- **Variaveis Comportamentais / Historico:** Faltas acumuladas (*absences*), atrasos (*lates*), saidas antecipadas (*early departures*) por periodo trimestral (MP1-MP4) e aluno recem-chegado a escola (*new to school*)
- **Variaveis Familiares / Sociodemograficas:** Estado civil dos pais (divorciados/separados), qualidade da resposta parental a problemas de recusa escolar, historico de irmao com problema semelhante de frequencia, serie escolar e sexo do aluno
- **Variaveis Institucionais / Contextuais:** Elegibilidade para almoco gratuito/reduzido (nivel distrital/escolar) e acomodacoes escolares formais (IEP / Secao 504)
- **Features Mais Relevantes Identificadas:** Faltas anuais: Plano 504 (`Std beta = 0,16, t = 2,90, p = 0,00`) e irmao com baixa frequencia (`Std beta = 0,10, t = 1,85, p = 0,06`). Atrasos anuais: irmao com baixa frequencia (`Std beta = 0,29, t = 5,56, p = 0,00`), pais divorciados/separados (`Std beta = 0,14, t = 2,78, p = 0,01`) e serie mais alta (`Std beta = 0,11, t = 2,05, p = 0,04`). Saidas antecipadas: irmao com baixa frequencia (`Std beta = 0,12, t = 2,23, p = 0,03`), sexo masculino (`Std beta = -0,11 para feminino, t = -1,93, p = 0,05`) e novo na escola (`Std beta = 0,09, t = 1,68, p = 0,09`)

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** N/A (instrumento ACFS criado ad hoc para o piloto; autores declaram ausencia de confiabilidade estabelecida por nao usarem escalas padronizadas longas)
- **Metricas Computacionais (ML):** N/A para metricas de ML (Acuracia/AUC/F1); reporta coeficientes padronizados `Std beta`, estatisticas `t` e valores-p das 3 regressoes multiplas simultaneas (Tabela 5), alem de medias, desvios-padrao e custos distritais (Passo 1: custo medio anual intra-distrito US\$ 94.052 e fora do distrito US\$ 496.657)
- **Estrategia de Validacao:** Acompanhamento longitudinal de 1 ano letivo (4 periodos trimestrais / 180 dias) com regressao simultanea sobre os preditores com variancia suficiente e coleta de feedback qualitativo de usabilidade/viabilidade junto aos conselheiros (Passo 3)
- **Desafios Metodologicos Relatados:** Sobrecarga de tempo dos conselheiros ao preencher manualmente a planilha mensalmente e avaliar muitos itens psicossociais; necessidade de dividir trabalho com secretarias escolares e reduzir frequencia para trimestral; julgamentos subjetivos no esquema de cores (verde/amarelo/vermelho) sem limiares empiricos; inclusao de todas as faltas (sem distinguir recusa por sofrimento de doenca fisica ou *truancy* no Passo 2)
- **Aspectos Eticos e Transparencia (XAI):** Aprovacao por IRB universitario e Conselhos de Educacao distritais; uso de IDs nao identificaveis no Google Tables atendendo normas de privacidade do distrito; destaque para restricoes legais/privacidade ao integrar plataformas publicas com sistemas locais (ex.: PowerSchool)
- **Limitacoes Declaradas:** Amostra pequena e restrita (3 distritos no Passo 1; 4 escolas primarias de 1 distrito no Passo 2, baixa vulnerabilidade economica [2,2% almoco gratuito]); criterios distintos entre Passo 1 (faltas por ansiedade/humor) e Passo 2 (todas as faltas); ausencia de relato de professores, pais e proprios alunos; nao utilizacao de instrumentos psicometricos padronizados
- **Direcoes Futuras:** Integrar automaticamente o rastreador aos sistemas de gestao escolar (SIS) com feedback em tempo real (pontos verde/amarelo/vermelho), ampliar base de dados com multiplos informantes e preditores (ex.: bullying) e aplicar Machine Learning para gerar algoritmos preditivos baseados em perfis socioemocionais-escolares multidimensionais

### 3.1 Aprofundamento Metodologico (Diretriz do Orientador)
- **Dados de entrada para identificar ansiedade/sofrimento:** No Passo 1, estimativa retrospectiva de diretores sobre alunos com >=5 faltas anuais associadas a ansiedade ou problemas de humor. No Passo 2, formulario ACFS de 31 itens preenchido por conselheiros escolares (2 itens 0-10 para qualidade de amizades e atividades extracurriculares; demais itens binarios sim/nao e contagens de frequencia), acionado quando o aluno atinge >=5 faltas/atrasos no sistema de gestao escolar e atualizado a cada periodo trimestral (MP1-MP4), inicialmente mensal e ajustado para trimestral apos feedback.
- **Inventario completo de variaveis e justificativa de escolha:** Demograficas (serie, sexo), historico de frequencia (faltas, atrasos, saidas antecipadas), historico escolar (novo na escola), apoios academicos/comportamentais (IEP, Plano 504), funcionamento familiar (estado civil dos pais, qualidade da resposta parental a SR, historico de irmao com baixa frequencia), amizades (presenca de ao menos 1 bom amigo, qualidade das amizades) e engajamento escolar (atividades extracurriculares). Selecionadas em reunioes participativas entre pesquisadores, administradores e conselheiros com base em revisoes da literatura de recusa escolar (Kearney, 2008; McShane et al., 2001).
- **Fundamentacao teorica do identificador:** Baseia-se no modelo *Multitiered Systems of Support* (MTSS / Kearney & Graczyk, 2014) para diferenciar absenteismo transitorio (Tier 1) de problemas emergentes (Tier 2) e cronicos (Tier 3), associado a definicao clinica de recusa escolar baseada em ansiedade/sofrimento emocional e ao modelo de pesquisa participativa baseada na comunidade (*community-based participatory research*).
- **Restricoes de recursos e limitacoes:** Prototipo construido propositalmente com ferramenta gratuita (Google Tables) por ser inviavel financeiramente e prematuro programar extensao paga no PowerSchool durante a fase piloto. Mesmo assim, conselheiros relataram alta demanda de tempo para rastreamento manual e excesso de variaveis, levando a redistribuicao de tarefas com secretarias escolares e reducao para coleta trimestral.

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 2 | Descreve claramente os 3 passos da parceria pesquisa-comunidade para estimar escopo/custos da SR, pilotar sistema online de deteccao precoce e refina-lo. |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 2 | Detalha amostra (N = 409 de 2.372 alunos), limiar (>=5 faltas), fluxo Google Tables, itens do ACFS e 3 modelos de regressao simultanea. |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 1 | Apresenta `Std beta`, `t` e `p` das regressoes e descritivos trimestrais, mas nao reporta confiabilidade do ACFS nem metricas preditivas out-of-sample (AUC/R2/RMSE). |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 1 | Passo 1 foca recusa por ansiedade/humor, e Passo 2 analisa variaveis familiares/pares e Plano 504/IEP, porem sem instrumentos psicometricos diretos de ansiedade/depressao. |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 2 | Discute explicitamente amostra restrita e pouco diversa, divergencia de criterios entre Passo 1 e 2, ausencia de relato de pais/alunos/professores e falta de escalas validadas. |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **8 / 10** | `[EM DUVIDA]` para inclusao definitiva: sistema online de deteccao precoce de SR/absenteismo muito relevante, porem usa regressao estatistica classica (ML apenas como trabalho futuro) e preditores psicossociais parciais. |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- ---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
