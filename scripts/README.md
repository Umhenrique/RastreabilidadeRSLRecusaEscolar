# Pipeline de Automacao da RSL (`scripts/`)

**Projeto:** Revisao Sistematica da Literatura (RSL) sobre Recusa Escolar e Inteligencia Artificial  
**Pesquisador:** Matheus Henrique Assuncao de Medeiros (PGCC UERN / UFERSA)

Este diretorio contem os scripts estruturantes em Python responsaveis pela reprodutibilidade, auditoria e integridade dos dados em todas as fases da revisao sistematica.

---

## 1. Scripts Estruturantes (Core Pipeline)

| Script | Fase / Escopo | Funcao e Artefatos Gerados |
| :--- | :--- | :--- |
| `consolidar_e_triar_rsl.py` | Fase 1 (Deduplicacao e Triagem) | Processa os 1.552 registros brutos das 6 bases em `02_buscas_brutas/`, remove 81 duplicatas (`EC3`) e gera os 1.471 registros unicos em `03_selecao_triagem/01_deduplicacao/`. |
| `auditar_e_saneamento_triagem.py` | Fase 1 (Auditoria Metodologica) | Executa o saneamento auditado (`[DEC-003]`), preservando versoes legadas e consolidando os 101 estudos incluidos e 1.370 excluidos em `03_selecao_triagem/02_triagem_resumo/`. |
| `preparar_asreview.py` | Fase 1 (Triagem Ativa / ASReview) | Converte a matriz de triagem consolidada (1.471 registros com 101 incluidos) para o formato do ASReview LAB em `03_selecao_triagem/asreview/`. |
| `gerar_notas_obsidian_estudos.py` | Fase 2 (Obsidian Setup) | Gera as notas individuais `.md` em `04_extracao_dados/estudos/` a partir da planilha de artigos incluidos e do `00_templates/template_estudo.md`. |
| `consolidar_extracao_fase2.py` | Fase 2 (Extracao e QA) | Le as 101 notas de `04_extracao_dados/estudos/*.md` (Fonte Unica da Verdade), verifica PDFs em `04_extracao_dados/pdfs/`, sincroniza `qa_score` (`QA1-QA5`) e exporta `04_extracao_dados/matriz_extracao.csv` e `.xlsx`. |
| `gerar_index_obsidian.py` | Fase 2 (Dashboard Obsidian) | Sincroniza o arquivo mestre `00_INDEX.md` com os 101 estudos, seus status de leitura em tempo real e as estatisticas auditadas do funil PRISMA 2020. |
| `gerar_pdf_artigo.py` | Fase 3 (Relatorios e LaTeX) | Auxilia na compilacao e renderizacao dos manuscritos em `06_sintese_relatorio/`. |
| `gerar_review_protocol_docx.py` | Governanca (Protocolo) | Gera o arquivo Word `01_protocolo/review protocol.docx` (e copia na raiz) com fidelidade literal ao `01_protocolo/protocolo_rsl.md` (`[DEC-005]`). |
| `limpar_emojis_geral.py` | Governanca (QA Academico) | Inspeciona e remove qualquer caractere emoji em arquivos do repositorio, assegurando conformidade estrita com `AGENTS.md` e `GEMINI.md`. |

---

## 2. Como Executar na Fase 2 (Fluxo Recomendado)

Sempre que preencher ou atualizar notas de estudos em `04_extracao_dados/estudos/*.md` ou adicionar PDFs em `04_extracao_dados/pdfs/`:

```powershell
python scripts/consolidar_extracao_fase2.py
python scripts/gerar_index_obsidian.py
```

---

## 3. Historico Exploratorio (`scripts/legado_exploratorio_fase1/`)

Os 16 scripts exploratorios e de inspecao pontual utilizados durante a conducao inicial da Fase 1 (testes de parsing da IEEE/ACM e inspecoes parciais) estao preservados no subdiretorio `scripts/legado_exploratorio_fase1/` para fins de rastreabilidade historica.
