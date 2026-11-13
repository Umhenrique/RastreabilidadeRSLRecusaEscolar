#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script estruturante da Fase 2: Consolidacao e Validacao da Extracao de Dados.
Le as 101 notas do Obsidian em 04_extracao_dados/estudos/ (Fonte Unica da Verdade),
verifica a presenca dos PDFs em 04_extracao_dados/pdfs/, sincroniza qa_score (QA1-QA5)
e status padronizados no YAML, e gera 04_extracao_dados/matriz_extracao.csv e .xlsx.

Autor: Matheus Henrique Assuncao de Medeiros (PGCC UERN/UFERSA)
"""

import os
import re
import glob
import yaml
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

VALID_STATUS_PREFIXES = (
    "[Pendente Leitura Completa]",
    "[Extracao em Andamento]",
    "[Incluido Fase 2 - Extracao Concluida]",
    "[Excluido Fase 2 - Criterio EC",
)

def normalize_status(raw_status):
    s = str(raw_status or "").strip()
    if not s:
        return "[Pendente Leitura Completa]"
    if not s.startswith("["):
        s = f"[{s}]"
    return s

def extract_bullet_value(body, label_pattern):
    pattern = rf'-\s*\*\*{label_pattern}:\*\*\s*(.*)'
    m = re.search(pattern, body, flags=re.IGNORECASE)
    if not m:
        return ""
    val = m.group(1).strip()
    if val.startswith("*(") and val.endswith(")*"):
        return ""
    if val.startswith("(") and val.endswith(")"):
        return ""
    return val

def parse_qa_table(body):
    scores = {}
    justifications = {}
    for q_idx in range(1, 6):
        q_key = f"QA{q_idx}"
        pattern = rf'\|\s*\*\*{q_key}[^|]*\|\s*[^|]*\|\s*([0-2])\s*\|\s*([^|\n]*)\|'
        m = re.search(pattern, body)
        if m:
            scores[q_key] = int(m.group(1))
            justifications[q_key] = m.group(2).strip()
        else:
            scores[q_key] = 0
            justifications[q_key] = ""
    return scores, justifications

def sync_note_file(filepath, norm_status, qa_total):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    updated = content.replace(r'\&', '&')
    updated = re.sub(
        r'^(status:\s*).*$',
        f'\\g<1>"{norm_status}"',
        updated,
        count=1,
        flags=re.MULTILINE
    )
    updated = re.sub(
        r'^(qa_score:\s*).*$',
        f'\\g<1>{qa_total}',
        updated,
        count=1,
        flags=re.MULTILINE
    )
    updated = re.sub(
        r'(- \*\*Status da Extra[cç][aã]o:\*\* ).*$',
        f'\\g<1>`{norm_status}`',
        updated,
        count=1,
        flags=re.MULTILINE
    )
    updated = re.sub(
        r'(\|\s*\*\*TOTAL\*\*\s*\|\s*\*\*Pontua[cç][aã]o de Rigor\*\*\s*\|\s*)\*\*[^|]*\*\*(\s*\|)',
        f'\\g<1>**{qa_total} / 10**\\g<2>',
        updated,
        count=1
    )

    if updated != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated)
        return True
    return False

def find_pdf_for_study(pdfs_dir, study_id):
    if not os.path.exists(pdfs_dir):
        return "Nao"
    matches = glob.glob(os.path.join(pdfs_dir, f"{study_id}*.pdf"))
    return "Sim" if matches else "Nao"

def format_excel_workbook(xlsx_path, df_main, df_summary):
    wb = openpyxl.Workbook()
    ws_main = wb.active
    ws_main.title = "Matriz_Extracao_Fase2"

    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_font = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
    cell_font = Font(name="Calibri", size=10)
    thin_border = Border(
        left=Side(style="thin", color="D9D9D9"),
        right=Side(style="thin", color="D9D9D9"),
        top=Side(style="thin", color="D9D9D9"),
        bottom=Side(style="thin", color="D9D9D9"),
    )

    cols = list(df_main.columns)
    ws_main.append(cols)
    for col_idx in range(1, len(cols) + 1):
        cell = ws_main.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    for row_data in df_main.itertuples(index=False):
        ws_main.append(list(row_data))

    for row in ws_main.iter_rows(min_row=2, max_row=ws_main.max_row, min_col=1, max_col=len(cols)):
        for cell in row:
            cell.font = cell_font
            cell.border = thin_border
            cell.alignment = Alignment(vertical="top", wrap_text=True)

    ws_main.freeze_panes = "C2"
    for col_idx, col_name in enumerate(cols, start=1):
        col_letter = get_column_letter(col_idx)
        if col_name in ("Study_ID", "Ano", "PDF_Disponivel", "QA1", "QA2", "QA3", "QA4", "QA5", "QA_Total"):
            ws_main.column_dimensions[col_letter].width = 12
        elif col_name in ("Titulo", "Resumo_RQs"):
            ws_main.column_dimensions[col_letter].width = 42
        else:
            ws_main.column_dimensions[col_letter].width = 24

    ws_sum = wb.create_sheet(title="Resumo_PRISMA_Fase2")
    sum_cols = list(df_summary.columns)
    ws_sum.append(sum_cols)
    for col_idx in range(1, len(sum_cols) + 1):
        cell = ws_sum.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    for row_data in df_summary.itertuples(index=False):
        ws_sum.append(list(row_data))

    for col_idx in range(1, len(sum_cols) + 1):
        ws_sum.column_dimensions[get_column_letter(col_idx)].width = 36

    wb.save(xlsx_path)

def main():
    estudos_dir = os.path.join("04_extracao_dados", "estudos")
    pdfs_dir = os.path.join("04_extracao_dados", "pdfs")
    os.makedirs(pdfs_dir, exist_ok=True)

    note_files = sorted([f for f in os.listdir(estudos_dir) if f.endswith(".md")])
    print(f"[1/4] Lendo {len(note_files)} notas de estudos em {estudos_dir}...")

    records = []
    synced_count = 0

    for fname in note_files:
        fpath = os.path.join(estudos_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', text, re.DOTALL)
        if not m:
            continue

        raw_fm = m.group(1).replace(r'\&', '&')
        fm = yaml.safe_load(raw_fm) or {}
        body = m.group(2)

        sid = str(fm.get("study_id") or fm.get("id") or fname.split(" ")[0]).strip()
        norm_status = normalize_status(fm.get("status", "[Pendente Leitura Completa]"))
        qa_scores, qa_just = parse_qa_table(body)
        qa_total = sum(qa_scores.values())

        if sync_note_file(fpath, norm_status, qa_total):
            synced_count += 1

        authors_list = fm.get("authors") or []
        authors_str = ", ".join(authors_list) if isinstance(authors_list, list) else str(authors_list)
        scales_list = fm.get("scales") or []
        scales_str = ", ".join(scales_list) if isinstance(scales_list, list) else str(scales_list or "")
        algos_list = fm.get("algorithms") or []
        algos_str = ", ".join(algos_list) if isinstance(algos_list, list) else str(algos_list or "")

        records.append({
            "Study_ID": sid,
            "Titulo": str(fm.get("title", "")).strip(),
            "Autores": authors_str,
            "Ano": fm.get("year", ""),
            "Base_Origem": str(fm.get("database", "")).strip(),
            "Veiculo": str(fm.get("venue", "")).strip(),
            "DOI": str(fm.get("doi", "")).strip(),
            "PDF_Disponivel": find_pdf_for_study(pdfs_dir, sid),
            "Status_Fase2": norm_status,
            "Escopo_Populacao": str(fm.get("population_scope", "")).strip(),
            "Escopo_Intervencao": str(fm.get("intervention_scope", "")).strip(),
            "Escopo_Desfecho": str(fm.get("outcome_scope", "")).strip(),
            "Pais_Regiao": extract_bullet_value(body, r"Pa[ií]s/Regi[aã]o[^*]*"),
            "Amostra_Faixa_Etaria": extract_bullet_value(body, r"Faixa Et[aá]ria / Amostra[^*]*"),
            "Fonte_Dados_Dataset": extract_bullet_value(body, r"Fonte dos Dados / Dataset"),
            "RQ1_Instrumentos_Escalas": extract_bullet_value(body, r"Nome do Instrumento/Escala") or scales_str,
            "RQ1_Finalidade": extract_bullet_value(body, r"Finalidade"),
            "RQ2_Abordagem_IA": extract_bullet_value(body, r"Tipo de Abordagem"),
            "RQ2_Algoritmos": extract_bullet_value(body, r"Algoritmos Empregados") or algos_str,
            "RQ2_Tarefa_Modelo": extract_bullet_value(body, r"Tarefa do Modelo"),
            "RQ3_Variaveis_Psicologicas": extract_bullet_value(body, r"Vari[aá]veis Psicol[oó]gicas/Socioemocionais"),
            "RQ3_Variaveis_Comportamentais": extract_bullet_value(body, r"Vari[aá]veis Comportamentais / Hist[oó]rico"),
            "RQ3_Features_Relevantes": extract_bullet_value(body, r"Features Mais Relevantes Identificadas"),
            "RQ4_Metricas_Psicometricas": extract_bullet_value(body, r"M[eé]tricas Psicom[eé]tricas"),
            "RQ4_Metricas_Computacionais": extract_bullet_value(body, r"M[eé]tricas Computacionais \(ML\)"),
            "RQ4_Validacao": extract_bullet_value(body, r"Estrat[eé]gia de Valida[cç][aã]o"),
            "RQ4_Desafios": extract_bullet_value(body, r"Desafios Metodol[oó]gicos Relatados"),
            "RQ4_Etica_XAI": extract_bullet_value(body, r"Aspectos [EÉ]ticos e Transpar[eê]ncia \(XAI\)"),
            "RQ4_Limitacoes": extract_bullet_value(body, r"Limita[cç][oõ]es Declaradas"),
            "QA1": qa_scores["QA1"],
            "QA2": qa_scores["QA2"],
            "QA3": qa_scores["QA3"],
            "QA4": qa_scores["QA4"],
            "QA5": qa_scores["QA5"],
            "QA_Total": qa_total,
            "Arquivo_Obsidian": fname,
        })

    df_main = pd.DataFrame(records).sort_values("Study_ID").reset_index(drop=True)
    print(f"[2/4] Notas sincronizadas com tags de status/QA: {synced_count}")

    status_counts = df_main["Status_Fase2"].value_counts().to_dict()
    pdf_sim = int((df_main["PDF_Disponivel"] == "Sim").sum())
    summary_rows = [
        {"Indicador_Fase2": "Total de Estudos Elegiveis para Leitura Completa (Fase 2)", "Valor": len(df_main)},
        {"Indicador_Fase2": "PDFs Integrais Disponiveis em 04_extracao_dados/pdfs/", "Valor": pdf_sim},
        {"Indicador_Fase2": "Status: [Pendente Leitura Completa]", "Valor": status_counts.get("[Pendente Leitura Completa]", 0)},
        {"Indicador_Fase2": "Status: [Extracao em Andamento]", "Valor": status_counts.get("[Extracao em Andamento]", 0)},
        {"Indicador_Fase2": "Status: [Incluido Fase 2 - Extracao Concluida]", "Valor": status_counts.get("[Incluido Fase 2 - Extracao Concluida]", 0)},
        {"Indicador_Fase2": "Status: [Excluido Fase 2 - Criterio EC1/EC2/EC3/EC4]", "Valor": sum(v for k, v in status_counts.items() if k.startswith("[Excluido Fase 2"))},
    ]
    df_summary = pd.DataFrame(summary_rows)

    csv_out = os.path.join("04_extracao_dados", "matriz_extracao.csv")
    xlsx_out = os.path.join("04_extracao_dados", "matriz_extracao.xlsx")
    df_main.to_csv(csv_out, index=False, encoding="utf-8-sig")
    format_excel_workbook(xlsx_out, df_main, df_summary)

    print(f"[3/4] Planilha CSV exportada: {csv_out}")
    print(f"[4/4] Planilha Excel exportada: {xlsx_out}")

if __name__ == "__main__":
    main()
