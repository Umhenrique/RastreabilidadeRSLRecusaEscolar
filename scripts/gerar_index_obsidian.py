#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script estruturante para geracao do 00_INDEX.md (Master MOC e Dashboard Obsidian) da RSL.
Sincronizado com o corpus auditado de 101 estudos incluidos para a Fase 2.
Autor: Matheus Henrique Assuncao de Medeiros (PGCC UERN/UFERSA)
"""

import os
import re
import yaml
import pandas as pd

def clean_text(s):
    if not isinstance(s, str):
        return ""
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def read_note_frontmatter(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
        if m:
            return yaml.safe_load(m.group(1)) or {}
    except Exception:
        pass
    return {}

def main():
    excel_path = os.path.join("03_selecao_triagem", "02_triagem_resumo", "artigos_incluidos_leitura_completa.xlsx")
    df = pd.read_excel(excel_path)

    estudos_dir = os.path.join("04_extracao_dados", "estudos")
    files_map = {}
    meta_map = {}
    for fname in sorted(os.listdir(estudos_dir)):
        if fname.endswith(".md"):
            m = re.match(r'^(S\d{4})\b', fname)
            if m:
                sid = m.group(1)
                files_map[sid] = fname[:-3]
                meta_map[sid] = read_note_frontmatter(os.path.join(estudos_dir, fname))

    print(f"[OK] Total de notas mapeadas em 04_extracao_dados/estudos: {len(files_map)}")

    db_counts = df['Source_Database'].value_counts()

    table_rows = []
    for _, row in df.iterrows():
        sid = str(row['Study_ID']).strip()
        fname_no_ext = files_map.get(sid, f"{sid}")
        title = clean_text(str(row['Title']))
        year = str(int(row['Year'])) if pd.notna(row['Year']) else "N/D"
        db = str(row['Source_Database']).strip()
        pop = str(row['Population_Scope']).strip()

        fm = meta_map.get(sid, {})
        raw_status = str(fm.get("status", "[Pendente Leitura Completa]")).strip()
        if not raw_status.startswith("["):
            raw_status = f"[{raw_status}]"

        note_link = f"[[04_extracao_dados/estudos/{fname_no_ext}\\|{sid}]]"
        short_title = title if len(title) <= 65 else title[:62] + "..."
        short_title = short_title.replace('|', '/')

        table_rows.append(f"| {note_link} | {short_title} | {year} | `{db}` | {pop} | `{raw_status}` |")

    master_table = "\n".join(table_rows)

    index_content = f"""---
id: 00_INDEX
title: "Dashboard & Mapa de Conteudo (MOC) - RSL Recusa Escolar e IA"
type: moc
author: "Matheus Henrique Assuncao de Medeiros"
institution: "PGCC UERN/UFERSA"
date: 2026-10-30
total_estudos: {len(df)}
status: "Fase 2: Extracao e Sintese de Evidencias"
tags:
  - rsl/index
  - rsl/dashboard
  - rsl/moc
---

# Revisao Sistematica da Literatura (RSL)
## Identificacao e Predicao de Recusa Escolar e Absenteismo Cronico: Instrumentos Psicometricos e Modelos Computacionais de Inteligencia Artificial

> [!INFO] Informacoes do Projeto
> - **Pesquisador:** Matheus Henrique Assuncao de Medeiros
> - **Programa:** Programa de Pos-Graduacao em Ciencia da Computacao em Associacao Ampla (PGCC UERN / UFERSA)
> - **Status da RSL:** `[Concluido]` Fase 1 (Triagem Auditada) | `[Em Andamento]` Fase 2 (Leitura Completa e Extracao de Dados)
> - **Estudos Selecionados:** **{len(df)} artigos** aceitos para leitura de texto integral e extracao sistematica.
> - **Artigo Principal:** [[06_sintese_relatorio/artigo_rsl_ieee|Manuscrito IEEE (LaTeX)]] | [PDF Renderizado](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/artigo_rsl_ieee.pdf)
> - **Relatorio de Progresso:** [[06_sintese_relatorio/relatorio_progresso_rsl|Relatorio Tecnico (LaTeX)]] | [PDF Renderizado](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/06_sintese_relatorio/relatorio_progresso_rsl.pdf)

---

## Mapa de Navegacao Rapida (Vault MOC)

```mermaid
graph TD
    MOC["00_INDEX (Dashboard Geral)"]
    MOC --> PROT["01_protocolo/protocolo_rsl"]
    MOC --> MEM["05_memoria_projeto/estado_conhecimento_rsl"]
    MOC --> CHK["PRISMA/checklist_prisma_2020_status"]
    MOC --> FLOW["06_sintese_relatorio/prisma_flowchart"]
    MOC --> FORM["04_extracao_dados/formulario_extracao"]
    MOC --> TEMPL["00_templates/template_estudo"]
    
    MOC --> RQS["Questoes de Pesquisa (RQs)"]
    RQS --> RQ1["RQ1: Instrumentos Psicometricos"]
    RQS --> RQ2["RQ2: Modelos IA & Predicao"]
    RQS --> RQ3["RQ3: Variaveis Socioemocionais"]
    RQS --> RQ4["RQ4: Metricas & Desafios"]
    
    MOC --> CONC["Hub Conceitual"]
    CONC --> SCALES["Escalas (SRAS-R, SCREEN, SCARED)"]
    CONC --> ML["IA (EWS, Random Forest, XGBoost, XAI)"]
    CONC --> PHEN["Fenomenos (Recusa Escolar, Absenteismo)"]
    
    MOC --> ESTUDOS["04_extracao_dados/estudos ({len(df)} Notas)"]
```

---

## Documentos Centrais, Governanca e Protocolo
- **[[01_protocolo/protocolo_rsl|Protocolo Metodologico da RSL]]:** Definicao autoral do PICOC, strings de busca, bases, criterios de elegibilidade (`IC1-IC4`, `EC1-EC4`), questoes de pesquisa (`RQ1-RQ4`) e avaliacao de qualidade (`QA1-QA5`).
- **[[05_memoria_projeto/estado_conhecimento_rsl|Estado Consolidado do Conhecimento]]:** Painel do funil PRISMA 2020 auditado, sintese preliminar por RQ e lacunas de pesquisa.
- **[[05_memoria_projeto/decisoes_metodologicas|Registro de Decisoes Metodologicas (ADRs)]]:** Historico formal de deliberacoes (`DEC-001` a `DEC-006`).
- **[[05_memoria_projeto/diario_de_bordo|Diario de Bordo da Pesquisa]]:** Linha do tempo cumulativa de sessoes e entregas.
- **[[05_memoria_projeto/taxonomia_e_conceitos|Taxonomia e Conceitos Padronizados]]:** Distincoes operacionais entre SRB, EBSA, Truancy, School Withdrawal e Absenteismo Cronico.
- **[[PRISMA/checklist_prisma_2020_status|Checklist PRISMA 2020 Auditado]]:** Acompanhamento rigoroso dos 27 itens da diretriz PRISMA 2020.
- **[[06_sintese_relatorio/prisma_flowchart|Fluxograma de Selecao PRISMA]]:** Contabilidade auditada de cada etapa de identificacao e triagem.
- **[[04_extracao_dados/formulario_extracao|Formulario Padrao de Extracao]]:** Especificacao detalhada dos campos para preenchimento de cada estudo.
- **[[00_templates/template_estudo|Template Obsidian para Extracao]]:** Molde com propriedades YAML e secoes padronizadas.

---

## Questoes de Pesquisa (Research Questions - RQs)

| Questao | Titulo do Hub | Foco Investigativo |
|:---:|:---|:---|
| **RQ1** | [[04_extracao_dados/conceitos/RQ1_Instrumentos_Psicometricos\\|RQ1: Instrumentos Psicometricos]] | Ferramentas, escalas ou instrumentos psicometricos utilizados para diagnosticar ou rastrear a recusa escolar e o absenteismo cronico. |
| **RQ2** | [[04_extracao_dados/conceitos/RQ2_Modelos_IA_e_Predicao\\|RQ2: Modelos de IA e Predicao]] | Tecnicas de Inteligencia Artificial, Machine Learning e analise de dados aplicadas na predicao ou deteccao precoce da recusa escolar. |
| **RQ3** | [[04_extracao_dados/conceitos/RQ3_Variaveis_Socioemocionais\\|RQ3: Variaveis Socioemocionais]] | Variaveis socioemocionais, comportamentais ou contextuais mais frequentemente consideradas pelas ferramentas preditivas e diagnosticas. |
| **RQ4** | [[04_extracao_dados/conceitos/RQ4_Metricas_e_Desafios\\|RQ4: Metricas, Desafios e Limitacoes]] | Principais limitacoes, desafios metodologicos e metricas de avaliacao relatados nos estudos ao implementar essas ferramentas. |

---

## Rede Conceitual e Teorica

### Instrumentos e Escalas Psicometricas (RQ1)
- [[04_extracao_dados/conceitos/SRAS-R|SRAS-R (School Refusal Assessment Scale - Revised)]]: Avaliacao das 4 funcoes operantes da recusa escolar.
- [[04_extracao_dados/conceitos/SCREEN|SCREEN (School Refusal Evaluation and Screening Instrument)]]: Triagem rapida de risco no ambiente escolar.
- [[04_extracao_dados/conceitos/SCARED|SCARED (Screen for Child Anxiety Related Disorders)]]: Diagnostico de ansiedade comorbida e fobia escolar.

### Abordagens Computacionais e Machine Learning (RQ2 e RQ4)
- [[04_extracao_dados/conceitos/Early_Warning_Systems|Sistemas de Alerta Precoce (EWS)]]: Plataformas de monitoramento preventivo longitudinal.
- [[04_extracao_dados/conceitos/Random_Forest|Random Forest]]: Modelo ensemble de arvores para dados tabulares heterogeneos.
- [[04_extracao_dados/conceitos/XGBoost|XGBoost]]: Gradient boosting otimizado para desbalanceamento de classes escolares.
- [[04_extracao_dados/conceitos/Explicabilidade_XAI|Explicabilidade em IA (XAI)]]: SHAP, LIME e transparencia pedagogica/clinica.

### Fenomenos Investigados
- [[04_extracao_dados/conceitos/Recusa_Escolar|Recusa Escolar (School Refusal / EBSA)]]: Foco em etiologia emocional e ansiedade.
- [[04_extracao_dados/conceitos/Absenteismo_Cronico|Absenteismo Cronico]]: Indicador quantitativo (perda >= 10% dos dias letivos).

---

## Estatisticas do Funil de Triagem (Fase 1 Concluida e Auditada)

> [!ABSTRACT] Sintese Auditada da Triagem (PRISMA 2020)
> - **Total de Registros Brutos Identificados (6 Bases):** `1.552`
> - **Duplicatas Inter-Bases Removidas (EC3):** `81`
> - **Registros Unicos Triados (Titulo e Resumo):** `1.471`
> - **Registros Excluidos na Fase 1 (EC1: 71 | EC2: 1.299):** `1.370`
> - **Total de Artigos Incluidos para Leitura Completa (Fase 2):** **`{len(df)}`** (Taxa de selecao: 6,9%)

### Distribuicao dos {len(df)} Estudos por Base de Dados Primaria
- **Scopus:** `{db_counts.get('Scopus', 0)}` estudos
- **Springer Link:** `{db_counts.get('Springer Link', 0)}` estudos
- **Web of Science:** `{db_counts.get('Web of Science', 0)}` estudos
- **ACM Digital Library:** `{db_counts.get('ACM Digital Library', 0)}` estudos
- **ScienceDirect:** `{db_counts.get('ScienceDirect', 0)}` estudos
- **IEEE Xplore:** `{db_counts.get('IEEE Xplore', 0)}` estudos

---

## Visualizacao Dinamica (Obsidian Dataview)
*(Se voce possui o plugin **Dataview** ativado no Obsidian, o bloco abaixo renderiza interativamente a tabela filtrada e ordenavel)*

```dataview
TABLE id, year, database, population_scope, status, qa_score
FROM "04_extracao_dados/estudos"
SORT id ASC
```

---

## Tabela Master dos {len(df)} Estudos Incluidos (Navegacao Direta)

| ID | Titulo do Estudo | Ano | Base | Escopo da Populacao | Status |
|:---:|:---|:---:|:---:|:---|:---:|
{master_table}

---
*Gerado para o ecossistema Obsidian Vault - RSL Matheus Medeiros (PGCC UERN/UFERSA).*
"""

    index_path = "00_INDEX.md"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"[OK] Arquivo de indice mestre atualizado: {index_path}")

if __name__ == "__main__":
    main()
