# Registro de Decisoes Metodologicas da RSL (decisoes_metodologicas.md)

**Projeto:** Revisao Sistematica da Literatura (RSL) sobre Recusa Escolar e Inteligencia Artificial  
**Pesquisador:** Matheus Henrique Assuncao de Medeiros  
**Programa:** PGCC UERN / UFERSA  
**Responsavel:** Especialista 4 (Gestao de Memoria) sob supervisao do Agente Gerente  

---

## Estrutura do Registro de Decisao (ADR - Architectural/Methodological Decision Record)

Cada decisao registrada contem:
- **ID:** Identificador sequencial unico (`DEC-XXX`).
- **Data:** Data de homologacao da decisao.
- **Titulo:** Descricao sucinta da deliberacao.
- **Contexto:** Situacao fática ou problema identificado.
- **Decisao Tomada:** Acao ou alteracao metodologica formalizada.
- **Justificativa Academica:** Fundamentacao teorico-metodologica (Kitchenham, PRISMA 2020 ou literatura seminal).
- **Impacto no Projeto:** Arquivos gerados/alterados e reflexos no funil ou manuscrito.
- **Status:** `[Aprovado]` ou `[Em Revisao]`.

---

## Log de Decisoes

### [DEC-001] Definicao da String de Busca Canonica e Coleta nas Seis Bases
- **Data:** Outubro de 2026
- **Status:** `[Aprovado]`
- **Contexto:** Necessidade de capturar com alta sensibilidade a convergencia entre recusa escolar/absenteismo, aspectos socioemocionais e inteligencia artificial.
- **Decisao Tomada:** Estruturou-se a busca em 3 eixos semanticos booleanos com operador `AND`: (1) Fenomeno da infrequencia escolar (*school refusal*, *truancy*, *chronic absenteeism*, *school non-attendance*); (2) Dimensao socioemocional/saude mental (*anxiety*, *depression*, *mental health*, *bullying*, *peer victimization*); (3) Modelos computacionais e IA (*machine learning*, *artificial intelligence*, *deep learning*, *predictive model*, *early warning systems*, *data mining*). A restricao populacional a Educacao Basica (K-12) e instrumentos psicometricos foi delegada aos criterios de triagem (IC/EC) e RQs, evitando falso-negativo por ausencia do termo K-12 no resumo.
- **Justificativa Academica:** Garantir sensibilidade de busca conforme diretrizes de Kitchenham (2007) sem restringir previamente registros seminais em periodicos interdisciplinares.
- **Impacto no Projeto:** Recuperacao bruta de 1.552 registros (Springer: 1.000, ACM: 198, Scopus: 195, WoS: 83, ScienceDirect: 62, IEEE: 14). Arquivos brutos preservados em `02_buscas_brutas/`.

---

### [DEC-002] Algoritmo de Deduplicacao Automatizada Hibrida (DOI + Similaridade Textual)
- **Data:** Outubro de 2026
- **Status:** `[Aprovado]`
- **Contexto:** Intersecao entre as 6 bases indexadas resultando em duplicatas de metadados com pequenas variacoes ortograficas de titulos e pontuacoes.
- **Decisao Tomada:** Implementou-se rotina Python que confronta prioritariamente identificadores digitais DOI normalizados e, subsidiariamente, aplica distancia de edicao e normalizacao alfanumerica de titulos (Title Matching).
- **Justificativa Academica:** Atendimento rigoroso a Fase de Identificacao das diretrizes PRISMA 2020.
- **Impacto no Projeto:** Expurgadas 81 duplicatas inter-bases (WoS: 58, Springer: 19, IEEE: 3, ACM: 1). Estabelecimento do corpus unico de 1.471 registros para a Fase 1 de triagem (`03_selecao_triagem/01_deduplicacao/`).

---

### [DEC-003] Auditoria Metodologica e Saneamento da Triagem de Fase 1 (159 para 101 Estudos)
- **Data:** 16 de Outubro de 2026
- **Status:** `[Aprovado]`
- **Contexto:** Na triagem preliminar de titulo e resumo, rotinas por palavras-chave geraram falsos positivos severos: artigos da area de saude publica continham termos de presenca (*truancy*) apenas como covariavel demografica de controle secundária, enquanto os desfechos centrais eram substancias quimicas, trauma de veteranos de guerra ou estudantes de faculdade de medicina (Ensino Superior).
- **Decisao Tomada:** Conduziu-se uma auditoria minuciosa e manual sobre os 159 artigos candidatos. 58 estudos foram formalmente reclassificados para Excluidos (EC1: 1 caso; EC2: 57 casos), consolidando 101 artigos cientificos definitivos para a Fase 2 (Leitura Completa). As planilhas legadas foram integralmente preservadas na pasta `03_selecao_triagem/02_triagem_resumo/legado_pre_revisao/`, acompanhadas do relatorio de auditoria individualizada.
- **Justificativa Academica:** Preservacao da validade interna do estudo, prevencao de dispersao tematica e aderencia aos criterios de elegibilidade do protocolo registrado (PRISMA 2020).
- **Impacto no Projeto:** Ajuste dos numeros oficiais: 1.552 brutos -> 81 duplicatas -> 1.471 unicos -> 1.370 excluidos na Fase 1 -> 101 incluidos na Fase 2. Atualizacao dos relatorios tecnicos (`relatorio_progresso_rsl.tex` / `RSL_recusa.pdf`) e do manuscrito IEEE (`artigo_rsl_ieee.tex` / `artigo_rsl_ieee.pdf`).

---

### [DEC-004] Criacao do Diretorio 05_memoria_projeto e Integracao do Especialista 4 (Gestao de Memoria)
- **Data:** 17 de Outubro de 2026
- **Status:** `[Aprovado]`
- **Contexto:** Necessidade de manter uma linhagem cientifica continua, rastreabilidade historica e sincronia entre os especialistas multi-agente, alem de garantir substrato formal pronto para prestacao de contas ao orientador e a banca de mestrado.
- **Decisao Tomada:** Criou-se o modulo de governanca de conhecimento no diretorio `05_memoria_projeto/` composto por 4 pilares: Decisoes Metodologicas, Diario de Bordo, Taxonomia/Conceitos e Estado do Conhecimento da RSL. Formalizou-se o papel do Especialista 4 (`gestao-memoria`) operando sob orquestracao direta do Agente Gerente.
- **Justificativa Academica:** Boas praticas de reprodutibilidade cientifica na Engenharia de Software e em Revisoes Sistematicas de grande porte (Kitchenham & Charters, 2007).
- **Impacto no Projeto:** Atualizacao dos manuais `AGENTS.md` e `GEMINI.md`, criacao da habilidade `.agents/skills/gestao-memoria/` e documentacao de linhagem no repositorio.

---

### [DEC-005] Restauracao e Blindagem da Soberania Autoral do Protocolo Original
- **Data:** 17 de Outubro de 2026
- **Status:** `[Aprovado]`
- **Contexto:** Identificou-se que a geracao automatizada do arquivo `review protocol.docx` havia interpolado e expandido unilateralmente as Questoes de Pesquisa (adicionando focos em parenteses), o criterio PICOC (adicionando Comparacao e Contexto nao definidos) e os criterios de exclusao/inclusao, descaracterizando o texto autoral de Matheus registrado em `01_protocolo/protocolo_rsl.md`.
- **Decisao Tomada:** Restaurou-se o documento oficial `review protocol.docx` para a reproducao exata e literal do protocolo original do pesquisador. Estabeleceu-se regra global mandatoria proibindo qualquer modificacao, adicao ou elaboracao unilateral de elementos do protocolo sem aprovacao previa e deliberada do pesquisador.
- **Justificativa Academica:** Soberania autoral e fidelidade estrita ao plano de pesquisa formalmente aprovado no programa de pos-graduacao.
- **Impacto no Projeto:** Regeneracao dos arquivos `review protocol.docx` e `01_protocolo/review protocol.docx` com a redacao original fiel; atualizacao de `AGENTS.md` e `GEMINI.md`.

---

### [DEC-006] Alinhamento Integral de Governanca ao Protocolo Oficial, Saneamento de Scripts e Pipeline de Extracao da Fase 2
- **Data:** 30 de Outubro de 2026
- **Status:** `[Aprovado]`
- **Contexto:** Em auditoria de governanca e arquitetura de dados conduzida em conjunto com o pesquisador (sessao `/grill-me`), identificaram-se tres necessidades: (1) algumas skills de especialistas, documentos de memoria, o fluxograma/checklist PRISMA e trechos de `artigo_rsl_ieee.tex` apresentavam divergencias na ordem das RQs (`RQ1-RQ4`), nos criterios `IC1-IC4`/`EC1-EC4`, na tabela PICOC ou nos contadores pre-auditoria (`159` em vez de `101` estudos incluidos); (2) o diretorio `scripts/` continha 16 scripts exploratorios temporarios da Fase 1 misturados aos scripts estruturantes; e (3) faltava o pipeline automatizado da Fase 2 para consolidar as 101 notas do Obsidian (`04_extracao_dados/estudos/*.md`) na planilha `04_extracao_dados/matriz_extracao.xlsx` e atualizar `00_INDEX.md` sem links quebrados.
- **Decisao Tomada:** (1) Padronizaram-se 100% dos artefatos secundarios (Skills dos Especialistas 1, 2 e 3, arquivos de `05_memoria_projeto/`, `PRISMA/checklist_prisma_2020_status.md` e `.xlsx`, `06_sintese_relatorio/prisma_flowchart.md`, `06_sintese_relatorio/artigo_rsl_ieee.tex` e `README.md`) em estrita conformidade com `01_protocolo/protocolo_rsl.md` (RQ1: Instrumentos Psicometricos; RQ2: IA/ML; RQ3: Variaveis Socioemocionais/Contextuais; RQ4: Limitacoes e Metricas; PICOC de 3 elementos; IC1-IC4 e EC1-EC4) e com os numeros auditados (`101 incluidos` / `1.370 excluidos`); (2) Movimentaram-se os 16 scripts exploratorios da Fase 1 para `scripts/legado_exploratorio_fase1/` e planilhas duplicadas da raiz para `03_selecao_triagem/02_triagem_resumo/legado_pre_revisao/`; e (3) Estabeleceram-se as 101 notas do Obsidian como Fonte Unica da Verdade da Fase 2, criou-se `04_extracao_dados/pdfs/` e implementou-se `scripts/consolidar_extracao_fase2.py` para validar os 4 status oficiais da Fase 2, calcular `qa_score` (`QA1-QA5`) e exportar `04_extracao_dados/matriz_extracao.csv` e `.xlsx`, alem de atualizar `scripts/gerar_index_obsidian.py` e regenerar `00_INDEX.md` para os 101 estudos.
- **Justificativa Academica:** Garantia de consistencia interna, rastreabilidade fim-a-fim (Single Source of Truth) e conformidade integral com o protocolo registrado e com os itens 8, 9, 11, 16a, 17 e 27 do checklist PRISMA 2020.
- **Impacto no Projeto:** Atualizacao das skills em `.agents/skills/`, recompilacao de `06_sintese_relatorio/artigo_rsl_ieee.pdf`, regeneracao de `00_INDEX.md` (101 estudos sem links quebrados), criacao de `04_extracao_dados/pdfs/`, `scripts/consolidar_extracao_fase2.py`, `04_extracao_dados/matriz_extracao.csv` e `.xlsx`, e organizacao de `scripts/legado_exploratorio_fase1/`.

---

### [DEC-007] Saneamento Retroativo da Fase 2 (Exclusao de 16 Falsos Positivos e Preservacao de S0022)
- **Data:** 13 de Novembro de 2026
- **Status:** `[Aprovado]`
- **Contexto:** No inicio da leitura de texto completo da Fase 2, identificou-se que o estudo `S0203` (relato de caso clinico unico) havia sido capturado na Fase 1 por falso positivo da palavra `"AI"` presente na nota de *copyright* da Elsevier. Uma auditoria automatizada subsequente sobre os demais 100 registros identificou 16 registros adicionais suspeitos (1 duplicata inter-bases exata e estudos qualitativos/descritivos sem IA, ML ou instrumentos psicometricos).
- **Decisao Tomada:** Por deliberacao explicita do pesquisador, manteve-se `S0022` (*Compulsory educational mental health support system in Japan*) no corpus ativo e reclassificaram-se formalmente **16 estudos** para exclusao na Fase 2: `S0199` por `EC3` (duplicata exata de `S0183`) e `S0203`, `S0183`, `S0001`, `S0105`, `S0113`, `S0136`, `S0152`, `S0018`, `S0033`, `S0042`, `S0053`, `S0080`, `S0202`, `S0019` e `S0214` por `EC2` (fora de escopo / ausencia de IA, ML ou escala psicometrica).
- **Justificativa Academica:** Preservar a validade interna e a aderencia estrita ao criterio `IC1` durante a triagem de Fase 2, mantendo rastreabilidade integral no funil PRISMA 2020.
- **Impacto no Projeto:** Corpus ativo da Fase 2 atualizado de `101` para `85` estudos (`2` extraidos integralmente: `S0012`, `S0104`; `83` pendentes; `16` excluidos na Fase 2). Atualizacao das 16 notas em `04_extracao_dados/estudos/`, `04_extracao_dados/matriz_extracao.csv` e `.xlsx`, `00_INDEX.md`, `05_memoria_projeto/estado_conhecimento_rsl.md` e repositorio GitHub.

### [DEC-008] Refinamento do Criterio IC1 e Reclassificacao em Lote apos Debate Metodologico da Fase 2
- **Data:** 13 de Novembro de 2026
- **Status:** `[Aprovado]`
- **Contexto:** Durante o debate metodologico sobre os 26 PDFs lidos integralmente na Fase 2 (24 extraidos + 2 ja excluidos em leitura previa: `S0133` e `S0153`), identificou-se que varios estudos aplicavam apenas escalas psicometricas ou modelos estatisticos tradicionais sem IA/ML preditivo, ou constituiam revisoes secundarias/protocolos WIP sem implementacao empirica.
- **Decisao:** Por deliberacao explicita do pesquisador (Matheus), o criterio **IC1** em `01_protocolo/protocolo_rsl.md` foi ajustado para exigir que o estudo primario aplique efetivamente tecnicas de IA, Machine Learning ou modelagem preditiva associadas a recusa escolar ou ao absenteismo escolar com fatores socioemocionais, nao bastando a presenca isolada de escala psicometrica ou revisao teorica. Consequentemente:
  - **19 estudos reclassificados para `[Excluido Fase 2]`:**
    - `S0325` (`EC2` - trabalho em progresso WIP sem ML implementado);
    - `S0283` (`EC2` - EWS administrativo focado em risco economico/saude, sem fatores socioemocionais ou IA/ML);
    - `S0315`, `S0322`, `S0561`, `S0567`, `S0555`, `S0505`, `S0500`, `S0120`, `S0091`, `S0145`, `S0154` (`EC2` - estudos psicometricos, epidemiologicos ou de intervencao sem modelos preditivos de IA/ML; mantidos apenas como referencia teorica);
    - `S0012`, `S0075`, `S0204`, `S0206` (`EC1` - revisoes narrativa/integrativa/sintese de politicas sem modelo empirico proprio);
    - `S0030` (`EC1` - protocolo metodologico sem dados empiricos nem IA/ML);
    - `S0735` (`EC2` - estudo de intervencao clinica/preventiva sem IA/ML).
  - **1 estudo mantido com observacao `[EM DUVIDA]`:** `S0191` (chatbot especialista baseado em regras com escala SCARED, focado em ansiedade infantil tendo evitacao escolar como subescala secundaria), aguardando decisao final na proxima reuniao de triagem.
  - **4 estudos validados como incluidos ativos:** `S0198`, `S0104`, `S0501`, `S0290` (totalizando `5` estudos no grupo ativo `[Incluido Fase 2 - Extracao Concluida]` junto a `S0191`).
- **Impacto no Projeto:** Total de excluidos na Fase 2 elevado de `18` para `37` (`16` da DEC-007 + `2` leitura previa `S0133`/`S0153` + `19` da DEC-008); estudos ativos extraidos atualizados de `24` para `5` (`4` validados + `1` em duvida); `59` estudos seguem `[Pendente Leitura Completa]`. Atualizados `01_protocolo/protocolo_rsl.md`, notas em `04_extracao_dados/estudos/`, `matriz_extracao.csv/.xlsx`, `matriz_extracao_concluidos.csv/.xlsx`, `00_INDEX.md`, `06_sintese_relatorio/resumo_estudos_extraidos_fase2.md` e Google Docs.
