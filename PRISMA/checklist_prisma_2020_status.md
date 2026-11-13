# Checklist PRISMA 2020 -- Controle e Status da Revisao Sistematica (RSL)

> **Projeto de Dissertacao de Mestrado:** *Ferramentas Computacionais, Inteligencia Artificial e Instrumentos Diagnosticos para Recusa Escolar e Absenteismo Cronico na Educacao Basica*  
> **Autor:** Matheus Henrique Assuncao de Medeiros  
> **Programa:** Programa de Pos-Graduacao em Ciencia da Computacao (PGCC) -- Associacao Ampla UERN/UFERSA  
> **Documento Oficial de Referencia:** [`PRISMA_2020_checklist.pdf`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/PRISMA/PRISMA_2020_checklist.pdf)  
> **Ultima Atualizacao:** 30 de outubro de 2026 (Fechamento Auditado da Fase 1: 101 Estudos Incluidos e Estrutura da Fase 2)

---

## Painel Geral de Conformidade PRISMA 2020

| Status | Total de Itens | Percentual | Fase do Projeto |
|:---:|:---:|:---:|---|
| `[Concluido]` **Atendido com Rigor** | **11** | **40,7%** | Fase 1: Protocolo, Execucao de Buscas, Deduplicacao e Triagem Auditada (101 estudos) |
| `[Em Andamento]` **Estruturado no Protocolo / Em Execucao** | **9** | **33,3%** | Criterios, templates Obsidian, script consolidador e matrizes prontas para a Fase 2 |
| `[Pendente]` **Pendente de Execucao Final** | **7** | **26,0%** | Conclusao da Fase 2 (Leitura Completa dos 101 artigos) e Fase 3 (Sintese Final) |
| **Total** | **27** | **100,0%** | Checklist Completo PRISMA 2020 |

---

## Matriz Detalhada de Acompanhamento (27 Itens)

### 1. TITULO (TITLE)

| Item | Topico | Descricao Oficial PRISMA 2020 | Status | Local de Reporte no Projeto | Detalhamento / Evidencias Atuais | Proxima Acao |
|:---:|:---|:---|:---:|:---|:---|:---|
| **1** | **Title** | Identificar o manuscrito expressamente como uma Revisao Sistematica. | `[Concluido]` | [`06_sintese_relatorio/artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex)<br>Linha 31 | O titulo oficial traz: *"[...] Relatorio Consolidado de Triagem da RSL (PRISMA 2020)"*, explicitando o metodo e o protocolo. | Nenhuma pendencia para o titulo. |

---

### 2. RESUMO (ABSTRACT)

| Item | Topico | Descricao Oficial PRISMA 2020 | Status | Local de Reporte no Projeto | Detalhamento / Evidencias Atuais | Proxima Acao |
|:---:|:---|:---|:---:|:---|:---|:---|
| **2** | **Abstract** | Fornecer resumo estruturado conforme o checklist de abstracts do PRISMA 2020. | `[Concluido]` | [`06_sintese_relatorio/artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex)<br>Linhas 43-45 | Resumo estruturado com contexto, objetivos, bases, quantitativos auditados do funil (1.552 $\rightarrow$ 81 duplicatas $\rightarrow$ 1.471 unicos $\rightarrow$ 1.370 excluidos $\rightarrow$ 101 incluidos) e sintese dos achados preliminares. | Atualizar os numeros finais quando a leitura de texto completo (Fase 2) for concluida. |

---

### 3. INTRODUCAO (INTRODUCTION)

| Item | Topico | Descricao Oficial PRISMA 2020 | Status | Local de Reporte no Projeto | Detalhamento / Evidencias Atuais | Proxima Acao |
|:---:|:---|:---|:---:|:---|:---|:---|
| **3** | **Rationale** | Descrever a justificativa da revisao no contexto do conhecimento existente. | `[Concluido]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Secao I)<br>[`01_protocolo/protocolo_rsl.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/protocolo_rsl.md) | Fundamentacao sobre a lacuna entre pesquisas de Computacao/IA (que usam dados administrativos sem fatores socioemocionais) e a Psicologia/Psiquiatria clinica. | Expandir referencias teoricas classicas na escrita da dissertacao. |
| **4** | **Objectives** | Declarar explicitamente os objetivos e questoes de pesquisa (PICOC). | `[Concluido]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Secao II)<br>[`01_protocolo/protocolo_rsl.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/protocolo_rsl.md) | Criterio PICOC de 3 elementos formalmente mapeado na Tabela I e quatro Questoes de Pesquisa formuladas (RQ1: Escalas/Diagnostico; RQ2: Algoritmos de IA/ML; RQ3: Variaveis socioemocionais; RQ4: Limitacoes, Desafios e Metricas). | Concluido. |

---

### 4. METODOS (METHODS)

| Item | Topico | Descricao Oficial PRISMA 2020 | Status | Local de Reporte no Projeto | Detalhamento / Evidencias Atuais | Proxima Acao |
|:---:|:---|:---|:---:|:---|:---|:---|
| **5** | **Eligibility criteria** | Especificar os criterios de inclusao e exclusao e agrupamento de estudos. | `[Concluido]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Secao II.C)<br>[`01_protocolo/protocolo_rsl.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/protocolo_rsl.md) | Criterios formais definidos: IC1 (peer-reviewed), IC2 (IA/rastreio recusa escolar), IC3 (idiomas), IC4 (dados empiricos); EC1 (literatura cinzenta), EC2 (evasao estritamente socioeconomica/fora de escopo), EC3 (duplicatas), EC4 (texto completo inacessivel). | Manter registro estrito das exclusoes por EC4 durante a obtencao dos textos integrais. |
| **6** | **Information sources** | Especificar todas as bases consultadas e datas da ultima busca. | `[Concluido]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Tabela II)<br>[`02_buscas_brutas/log_execucao_buscas.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/log_execucao_buscas.md) | Seis bases internacionais documentadas com datas exatas: ACM DL (24/09), IEEE Xplore (24/09), ScienceDirect (04/10), Scopus (04/10), WoS (04/10) e Springer Link (04/10). | Fontes encerradas e salvas em `02_buscas_brutas/`. |
| **7** | **Search strategy** | Apresentar estrategias de busca completas com sintaxe, operadores e filtros. | `[Concluido]` | [`01_protocolo/strings_de_busca.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/strings_de_busca.md) | Todas as strings completas e adaptadas para as restricoes sintaticas de cada base (ex: limite de 8 operadores da ScienceDirect). | Concluido. |
| **8** | **Selection process** | Descrever o metodo de selecao (deduplicacao, triagem de resumo e ferramentas automatizadas). | `[Concluido]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Secao IV)<br>[`scripts/consolidar_e_triar_rsl.py`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/scripts/consolidar_e_triar_rsl.py)<br>[`scripts/auditar_e_saneamento_triagem.py`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/scripts/auditar_e_saneamento_triagem.py) | Algoritmo Python de deduplicacao (DOI + titulo normalizado), triagem de 1.471 artigos unicos e auditoria analitica que consolidou 101 estudos incluidos para a Fase 2. | Executar o processo de selecao em texto completo para os 101 artigos selecionados. |
| **9** | **Data collection process** | Descrever os metodos usados para coletar e extrair dados dos relatorios. | `[Em Andamento]` | [`04_extracao_dados/formulario_extracao.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/04_extracao_dados/formulario_extracao.md)<br>[`scripts/consolidar_extracao_fase2.py`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/scripts/consolidar_extracao_fase2.py) | 101 notas individuais geradas no Obsidian (`04_extracao_dados/estudos/`) com consolidacao automatizada para [`04_extracao_dados/matriz_extracao.xlsx`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/04_extracao_dados/matriz_extracao.xlsx). | Preencher as 101 fichas de extracao durante a leitura integral. |
| **10a** | **Data items (Outcomes)** | Listar e definir todos os desfechos para os quais dados foram buscados. | `[Em Andamento]` | [`01_protocolo/protocolo_rsl.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/protocolo_rsl.md) (Secao 2 e 3) | Desfechos primarios definidos: predicao de risco de recusa escolar, infrequencia cronica discente e diagnostico psicometrico. | Extrair dados pontuais de desempenho de cada estudo. |
| **10b** | **Data items (Outras variaveis)** | Listar variaveis de participantes, intervencao, algoritmos e contexto escolar. | `[Em Andamento]` | [`01_protocolo/protocolo_rsl.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/protocolo_rsl.md) | Mapeamento das variaveis: tamanho da amostra (Ensino Basico), variaveis socioemocionais (ansiedade, bullying, suporte familiar), hiperparametros e algoritmos. | Preenchimento sistematico nas notas do Obsidian. |
| **11** | **Study risk of bias assessment** | Metodos para avaliar o risco de vies e rigor metodologico dos estudos incluidos. | `[Em Andamento]` | [`01_protocolo/protocolo_rsl.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/protocolo_rsl.md) (Secao 6) | Checklist Quality Assessment (QA1 a QA5) com escala de pontuacao de 0 a 10 pontos formalizado no protocolo e em cada nota do Obsidian. | Aplicar a pontuacao QA1-QA5 a cada um dos 101 artigos apos leitura integral. |
| **12** | **Effect measures** | Especificar medidas de efeito / metricas de desempenho. | `[Em Andamento]` | [`01_protocolo/protocolo_rsl.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/protocolo_rsl.md) (RQ4) | Definidas: Acuracia, F1-Score, Sensibilidade, Especificidade, AUC-ROC e consistencia interna ($\alpha$ de Cronbach, $\omega$ de McDonald). | Tabular metricas comparativas na Fase 2. |
| **13a** | **Synthesis eligibility** | Descrever o processo para determinar elegibilidade para cada sintese. | `[Em Andamento]` | [`01_protocolo/protocolo_rsl.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/protocolo_rsl.md) | Agrupamento dos estudos por Questao de Pesquisa (RQ1: Ferramentas Psicometricas; RQ2: Modelos de IA/ML; RQ3: Variaveis Socioemocionais; RQ4: Limitacoes e Validacao). | Concluir agrupamento fino apos leitura integral. |
| **13b** | **Data preparation** | Tratamento de dados ausentes, conversoes e padronizacoes. | `[Em Andamento]` | [`03_selecao_triagem/`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/03_selecao_triagem/) | Normalizacao de DOIs, titulos alfanumericos e categorias de intervencao padronizadas. | Tratar metricas incompletas durante a extracao. |
| **13c** | **Tabulation and display** | Metodos para tabular e exibir visualmente os resultados dos estudos. | `[Concluido]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Tabela IV) | Diagramacao de tabelas consolidadas com ID, Ano, Base, Veiculo, Abordagem Tecnica e RQs. | Gerar graficos de sintese adicionais para a dissertacao. |
| **13d** | **Synthesis methods** | Metodo de sintese e justificativa da escolha (sintese tematica/narrativa). | `[Em Andamento]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Secao V) | Sintese tematica e analise narrativa estruturada de acordo com o padrao Kitchenham. | Aprofundar redacao na dissertacao de mestrado. |
| **13e** | **Exploring heterogeneity** | Exploracao de causas de heterogeneidade entre estudos. | `[Pendente]` | -- | Analise das diferencas entre niveis escolares (Ensino Fundamental vs. Medio) e tipos de intervencao (EWS institucional vs. triagem clinica). | Executar na sintese da dissertacao. |
| **13f** | **Sensitivity analyses** | Analises de sensibilidade para avaliar robustez da sintese. | `[Pendente]` | -- | Verificar se estudos com baixo escore de qualidade metodologica (QA < 5) alteram as conclusoes gerais sobre as melhores arquiteturas de IA. | Executar apos aplicar QA1-QA5. |
| **14** | **Reporting bias assessment** | Avaliacao de vies de relato / vies de publicacao. | `[Pendente]` | -- | Discussao critica sobre vies de publicacao de algoritmos (tendencia de publicar apenas modelos com acuracias altas/otimistas). | Incluir no capitulo de discussao da dissertacao. |
| **15** | **Certainty assessment** | Avaliacao de certeza ou confianca no corpo de evidencias. | `[Pendente]` | -- | Analise da maturidade das abordagens de IA aplicadas a ambientes escolares reais. | Redigir na sintese final. |

---

### 5. RESULTADOS (RESULTS)

| Item | Topico | Descricao Oficial PRISMA 2020 | Status | Local de Reporte no Projeto | Detalhamento / Evidencias Atuais | Proxima Acao |
|:---:|:---|:---|:---:|:---|:---|:---|
| **16a** | **Study selection (Flow)** | Resultados do processo de busca e selecao em numeros com diagrama de fluxo. | `[Concluido]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Fig. 1)<br>[`06_sintese_relatorio/prisma_flowchart.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/prisma_flowchart.md) | Diagrama PRISMA 2020 completo e auditado: 1.552 brutos $\rightarrow$ 81 duplicatas $\rightarrow$ 1.471 avaliados $\rightarrow$ 1.370 excluidos (71 EC1; 1.299 EC2) $\rightarrow$ 101 selecionados para Fase 2. | Adicionar numeros de exclusao da Fase 2 pos-leitura integral. |
| **16b** | **Excluded studies** | Citar estudos excluidos e justificar as razoes de exclusao. | `[Concluido]` | [`03_selecao_triagem/02_triagem_resumo/matriz_triagem_consolidada.xlsx`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/03_selecao_triagem/02_triagem_resumo/matriz_triagem_consolidada.xlsx) | Registro individual e detalhado de cada um dos 1.370 estudos excluidos na Fase 1, com o criterio exato (EC1 ou EC2) e justificativa textual. | Registrar motivos de exclusao pos-leitura de texto completo. |
| **17** | **Study characteristics** | Apresentar caracteristicas de cada estudo incluido. | `[Em Andamento]` | [`03_selecao_triagem/02_triagem_resumo/artigos_incluidos_leitura_completa.xlsx`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/03_selecao_triagem/02_triagem_resumo/artigos_incluidos_leitura_completa.xlsx)<br>[`04_extracao_dados/matriz_extracao.xlsx`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/04_extracao_dados/matriz_extracao.xlsx) | Metadados completos dos 101 estudos aceitos para leitura integral (Titulo, Autores, Ano, Periodico, DOI, URL, Resumo e RQs preliminares). | Complementar com variaveis extraidas na leitura integral. |
| **18** | **Risk of bias in studies** | Apresentar a avaliacao de risco de vies de cada estudo incluido. | `[Pendente]` | [`04_extracao_dados/matriz_extracao.xlsx`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/04_extracao_dados/matriz_extracao.xlsx) | Pontuacao individual de qualidade (QA1 a QA5) estruturada nas 101 notas do Obsidian. | Preencher nas notas e consolidar via script apos avaliacao dos artigos. |
| **19** | **Results of individual studies** | Dados sumarizados de desfechos para cada estudo individual. | `[Pendente]` | -- | Tabelas individuais com metricas de cada modelo (Acuracia, F1, Escalas aplicadas). | Montar tabelas comparativas apos a extracao. |
| **20a** | **Results of syntheses (Summary)** | Sumarizar caracteristicas e risco de vies entre os estudos contribuintes. | `[Em Andamento]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Secao V) | Sintese preliminar respondendo a RQ1 (SRAS-R, SCREEN, SCARED), RQ2 (Random Forest, XGBoost, LSTM, EWS), RQ3 (bullying, ansiedade, clima escolar) e RQ4 (desbalanceamento, XAI). | Finalizar sintese pos-Fase 2. |
| **20b** | **Results of statistical syntheses** | Apresentar resultados de sinteses estatisticas/meta-analises (se aplicavel). | `[Pendente]` | -- | Sintese de distribuicoes de desempenho (intervalos de acuracia e F1 mais comuns na literatura). | Calcular estatisticas descritivas pos-extracao. |
| **20c** | **Causes of heterogeneity** | Apresentar resultados da investigacao de causas de heterogeneidade. | `[Pendente]` | -- | Impacto do tamanho da base discente e das features adotadas no desempenho dos modelos. | Descrever na dissertacao. |
| **20d** | **Sensitivity analyses results** | Apresentar resultados das analises de sensibilidade. | `[Pendente]` | -- | Validacao da estabilidade dos achados independentemente de estudos de menor rigor tecnico. | Descrever na dissertacao. |
| **21** | **Reporting biases results** | Apresentar avaliacoes de vies de relato para as sinteses. | `[Pendente]` | -- | Sintese qualitativa de lacunas e vieses observados. | Redigir na dissertacao. |
| **22** | **Certainty of evidence results** | Apresentar avaliacao da certeza da evidencia para cada desfecho. | `[Pendente]` | -- | Grau de recomendacao e maturidade para implantacao de ferramentas preditivas no ambiente escolar. | Redigir nas conclusoes da dissertacao. |

---

### 6. DISCUSSAO (DISCUSSION)

| Item | Topico | Descricao Oficial PRISMA 2020 | Status | Local de Reporte no Projeto | Detalhamento / Evidencias Atuais | Proxima Acao |
|:---:|:---|:---|:---:|:---|:---|:---|
| **23a** | **Discussion (Interpretation)** | Interpretar resultados no contexto de outras evidencias. | `[Em Andamento]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Secao V) | Discussao do avanco dos EWS modernos frente aos modelos arcaicos baseados apenas em medias de notas e faltas. | Expandir na dissertacao. |
| **23b** | **Limitations of evidence** | Discutir limitacoes das evidencias incluidas na revisao. | `[Em Andamento]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Secao V.D) | Desbalanceamento severo de classes, vies de rotulacao e escassez de validacao externa em larga escala na Educacao Basica. | Aprofundar na dissertacao. |
| **23c** | **Limitations of review processes** | Discutir limitacoes do proprio processo de conducao da revisao. | `[Em Andamento]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Secao II e V) | Limite operacional de 8 operadores da ScienceDirect e restricao de idiomas (ingles, portugues e espanhol). | Registrar detalhadamente na metodologia da dissertacao. |
| **23d** | **Implications** | Discutir implicacoes para a pratica pedagogica, politicas publicas e pesquisas futuras. | `[Em Andamento]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) (Secao V e VII) | Necessidade de explicabilidade (XAI/SHAP) para suporte a orientadores e psicologos escolares; diretrizes eticas contra estigmatizacao discente. | Consolidar no fechamento da dissertacao. |

---

### 7. OUTRAS INFORMACOES (OTHER INFORMATION)

| Item | Topico | Descricao Oficial PRISMA 2020 | Status | Local de Reporte no Projeto | Detalhamento / Evidencias Atuais | Proxima Acao |
|:---:|:---|:---|:---:|:---|:---|:---|
| **24a** | **Registration info** | Fornecer informacoes sobre registro da revisao (nome do registro e numero). | `[Em Andamento]` | [`01_protocolo/protocolo_rsl.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/protocolo_rsl.md) | Protocolo interno estruturado. *(Recomendacao consultiva: registrar no OSF -- Open Science Framework).* | Definir se sera submetido ao OSF (osf.io) para geracao de DOI publico do protocolo. |
| **24b** | **Protocol access** | Indicar onde o protocolo da revisao pode ser acessado. | `[Concluido]` | Repositorio local: [`01_protocolo/protocolo_rsl.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/protocolo_rsl.md) | Protocolo completo, versionado e acessivel no projeto. | Atualizar caso haja emendas aprovadas pelo pesquisador. |
| **24c** | **Amendments to protocol** | Descrever e explicar quaisquer emendas ou alteracoes feitas ao protocolo. | `[Concluido]` | [`05_memoria_projeto/decisoes_metodologicas.md`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/05_memoria_projeto/decisoes_metodologicas.md) | Registro transparente das deliberacoes metodologicas (DEC-001 a DEC-006) e adaptacoes sintaticas nas bases. | Documentar qualquer alteracao futura. |
| **25** | **Support / Funding** | Fontes de apoio financeiro ou nao financeiro e papel dos financiadores. | `[Em Andamento]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex)<br>Linha 34 | Registrada filiacao institucional ao PGCC UERN/UFERSA. | Declarar bolsa de mestrado (ex: CAPES / CNPq / FAPERN), se houver. |
| **26** | **Competing interests** | Declarar potenciais conflitos de interesse dos autores. | `[Concluido]` | [`artigo_rsl_ieee.tex`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.tex) | Inexistencia de conflitos de interesse comerciais ou financeiros. | Concluido. |
| **27** | **Availability of data & code** | Disponibilidade publica de formularios, dados extraidos, codigo e materiais. | `[Concluido]` | Arvore completa do repositorio ([`02_buscas_brutas/`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/), [`03_selecao_triagem/`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/03_selecao_triagem/), [`04_extracao_dados/`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/04_extracao_dados/), [`05_memoria_projeto/`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/05_memoria_projeto/), [`scripts/`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/scripts/)) | Repositorio 100% auditavel com todos os scripts Python, planilhas brutas e auditadas, notas Obsidian e memoria metodologica. | Manter versionamento git atualizado. |

---

## Guia de Atualizacao Continua deste Checklist

Conforme avancarmos na Fase 2, atualizaremos este arquivo mudando o status e os links nas seguintes transicoes:

1. **Ao baixar os PDFs integrais em `04_extracao_dados/pdfs/`:**
   - Atualizar **Item 5 e 8** registrando eventuais estudos nao recuperados institucionalmente (Criterio EC4).
2. **Ao concluir o preenchimento das notas em `04_extracao_dados/estudos/` e gerar `04_extracao_dados/matriz_extracao.xlsx`:**
   - Mudar **Itens 9, 10a, 10b e 17** de `[Em Andamento]` para `[Concluido]`.
3. **Ao avaliar a qualidade metodologica (QA1 a QA5):**
   - Mudar **Itens 11 e 18** para `[Concluido]`.
4. **Ao consolidar a sintese tematica dos resultados na dissertacao:**
   - Mudar **Itens 12, 13a-f, 19, 20a-d, 21, 22 e 23a-d** para `[Concluido]`.
