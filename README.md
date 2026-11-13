# Projeto de Dissertacao de Mestrado: RSL Recusa Escolar e IA
**Autor:** Matheus Henrique Assuncao de Medeiros  
**Programa:** PGCC UERN / UFERSA  
**Data de Atualizacao:** Outubro de 2026  
**Status Global:** `[Concluido]` Fase 1 (Triagem Auditada: 101 Estudos) | `[Em Andamento]` Fase 2 (Extracao e Leitura Completa)

> [!TIP] Obsidian Vault Integrado
> Este repositorio esta totalmente adaptado e configurado como um **Obsidian Vault**.  
> Para navegar com grafos de conhecimento, links bidirecionais e paineis interativos, abra o arquivo principal:
> **[[00_INDEX|00_INDEX.md - Dashboard e Mapa de Conteudo (MOC)]]**

---

## Estrutura do Repositorio / Vault

```text
├── 00_INDEX.md                        # Dashboard Principal e MOC no Obsidian (101 estudos)
├── 00_templates/                      # Templates padronizados do projeto
│   └── template_estudo.md             # Template de extracao individual (RQ1-RQ4 e QA1-QA5)
├── 01_protocolo/                      # Protocolo metodologico autoral (Soberania Autoral)
│   ├── protocolo_rsl.md               # Objetivos, PICOC, RQ1-RQ4, IC1-IC4, EC1-EC4, QA1-QA5
│   ├── strings_de_busca.md            # Strings booleanas canonicas e adaptadas por base
│   └── review protocol.docx           # Versao Word fiel ao protocolo_rsl.md
├── 02_buscas_brutas/                  # Exportacoes brutas das 6 bases (1.552 registros)
├── 03_selecao_triagem/                # Deduplicacao, triagem auditada e ASReview
│   ├── 01_deduplicacao/               # 81 duplicatas removidas (1.471 registros unicos)
│   ├── 02_triagem_resumo/             # 101 estudos incluidos e 1.370 excluidos (+ pasta legado_pre_revisao)
│   └── asreview/                      # Base consolidada e projeto ASReview LAB
├── 04_extracao_dados/                 # Ambiente de extracao da Fase 2 (Fonte Unica da Verdade)
│   ├── conceitos/                     # Hubs conceituais e RQs (SRAS-R, SCREEN, EWS, XAI, etc.)
│   ├── estudos/                       # 101 notas individuais dos estudos aceitos para Fase 2
│   ├── estudos_excluidos_auditoria/   # 58 notas preservadas dos estudos reclassificados na auditoria
│   ├── pdfs/                          # Textos integrais em PDF (SXXXX.pdf)
│   ├── formulario_extracao.md         # Especificacao do formulario de extracao
│   ├── matriz_extracao.csv            # Planilha consolidada gerada automaticamente das notas
│   └── matriz_extracao.xlsx           # Planilha Excel consolidada da Fase 2
├── 05_memoria_projeto/                # Governanca de conhecimento e linhagem cientifica (Especialista 4)
│   ├── decisoes_metodologicas.md      # Registro formal de decisoes (ADRs: DEC-001 a DEC-006)
│   ├── diario_de_bordo.md             # Linha do tempo cumulativa de sessoes
│   ├── estado_conhecimento_rsl.md     # Funil PRISMA consolidado, sintese das RQs e lacunas
│   └── taxonomia_e_conceitos.md       # Vocabulario padronizado (SRB, EBSA, Truancy, EWS, SRAS-R)
├── 06_sintese_relatorio/              # Manuscritos em LaTeX e relatorios tecnicos (Especialista 3)
│   ├── artigo_rsl_ieee.tex            # Manuscrito no padrao IEEE Transactions/Conference
│   ├── artigo_rsl_ieee.pdf            # PDF compilado via Tectonic
│   ├── relatorio_progresso_rsl.tex    # Relatorio tecnico executivo de andamento
│   ├── relatorio_progresso_rsl.pdf    # PDF do relatorio tecnico
│   └── prisma_flowchart.md            # Contabilidade detalhada do fluxograma PRISMA 2020
├── PRISMA/                            # Diretrizes e auditoria PRISMA 2020
│   ├── checklist_prisma_2020_status.md
│   └── checklist_prisma_2020_status.xlsx
└── scripts/                           # Pipeline de automacao em Python
    ├── README.md                      # Documentacao dos scripts estruturantes
    └── legado_exploratorio_fase1/     # Scripts exploratorios historicos da Fase 1
```

---

## Fundamentacao Metodologica do Fluxo Multi-Agente

A orquestracao desta Revisao Sistematica da Literatura adota uma arquitetura multi-agente especializada (Agente Gerente e Especialistas 1 a 4) sob supervisao continua e aprovacao explicita do pesquisador (**Human-in-the-Loop** e Soberania Autoral do Protocolo definidos em `AGENTS.md`).

Essa abordagem alinha-se a literatura recente sobre automacao assistida de revisoes sistematicas:

- **Ren, Z., Zhao, Z., Li, Q., Wu, Y., Wang, L., Luo, R., Xu, Y., Guo, Q., Shi, J., Xie, E., Hu, F., & Shi, Q. (2026).** *Systematic Literature Reviews With Two Multi-Agentic Systems And Human-In-The-Loop*. arXiv preprint arXiv:2607.21920. Disponivel em: https://arxiv.org/abs/2607.21920

