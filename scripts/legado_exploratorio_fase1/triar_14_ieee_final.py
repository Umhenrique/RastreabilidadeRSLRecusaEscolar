import os
import re
import json
import sys
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding='utf-8')

from analisar_14_ieee import parse_ieee_bib

def avaliar_estudo_14(item, idx):
    study_id = f"IEEE_{idx:02d}"
    title = item.get('title', '').strip()
    abstract = item.get('abstract', '').strip()
    year = item.get('year', '').strip()
    authors = item.get('author', '').strip()
    doi = item.get('doi', '').strip()
    source_file = item.get('source_file', '')
    entry_type = item.get('entry_type', '').lower()
    booktitle = item.get('booktitle', '').strip()
    journal = item.get('journal', '').strip()
    venue = booktitle if booktitle else journal
    
    # Avaliação rigorosa estudo a estudo
    if idx == 1:
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Desenvolve e avalia modelos de Machine Learning (Redes Neurais, SVM, Árvores de Decisão com acurácia >85%) para predição precoce de evasão escolar e simulação de intervenções em estudantes vulneráveis do ensino básico. Responde a RQ2 e RQ4.',
            'Population_Scope': 'Educação Básica (Colômbia)', 'Intervention_Scope': 'Redes Neurais, SVM, Árvores de Decisão', 'Outcome_Scope': 'Predição de Evasão Escolar e Simulação de Intervenções',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 2:
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Integra diretamente instrumento psicométrico clínico (questionário SCARED) com algoritmos de Machine Learning (Random Forest Multioutput) para rastreio e predição precoce de cinco dimensões de ansiedade, destacando a Evitação Escolar (School Avoidance). Responde perfeitamente a RQ1, RQ2 e RQ3.',
            'Population_Scope': 'Ensino Secundário / Básico (Estudantes O/L)', 'Intervention_Scope': 'Escala Psicométrica SCARED + Random Forest Classifier', 'Outcome_Scope': 'Evitação Escolar (School Avoidance) e Ansiedade',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 3:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'População e desfecho fora do escopo: O estudo realiza classificação clínica geral de ansiedade, depressão e estresse usando o questionário DASS-42 em amostra genérica, sem qualquer aplicação ou menção a ambiente escolar, recusa escolar ou evasão de alunos.',
            'Population_Scope': 'Geral / Não escolar', 'Intervention_Scope': 'SVM / Regressão Logística', 'Outcome_Scope': 'Transtornos Emocionais Gerais (DASS-42)',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 4:
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Desenvolve modelo de gestão acadêmica com Inteligência Artificial integrando instrumentos psicométricos cientificamente validados e variáveis de saúde mental (mental health) para detecção precoce de risco escolar em escolas públicas. Responde a RQ1, RQ2 e RQ3.',
            'Population_Scope': 'Ensino Básico (Escolas Públicas)', 'Intervention_Scope': 'Instrumentos Psicométricos Validados + IA (Regressão/Clustering)', 'Outcome_Scope': 'Predição Precoce de Risco Escolar e Saúde Mental',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 5:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'População fora do escopo: Estudo voltado ao Serviço Nacional de Aprendizagem (SENA), com aplicação explícita voltada a instituições de ensino superior e formação técnica pós-secundária, não se enquadrando na Educação Básica (K-12).',
            'Population_Scope': 'Ensino Superior / Técnico Profissional (SENA)', 'Intervention_Scope': 'Árvores de Decisão', 'Outcome_Scope': 'Evasão em Ensino Técnico/Superior',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 6:
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Propõe arquitetura de rede neural convolucional (CNN-DBAM) para rastreio proativo precoce de comportamentos disruptivos e risco psicológico em crianças da escola primária, com o objetivo explícito de prevenir o abandono no ensino médio (high school dropout). Responde a RQ1, RQ2 e RQ3.',
            'Population_Scope': 'Ensino Básico (Escola Primária)', 'Intervention_Scope': 'Deep Learning (CNN) para Rastreio Comportamental/Psicológico', 'Outcome_Scope': 'Rastreio Precoce de Risco e Prevenção de Abandono',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 7:
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Modela a predição de risco de abandono escolar no Ensino Médio público (366k+ alunos) utilizando técnicas avançadas de aprendizado de máquina para lidar com classes severamente desbalanceadas, avaliando assiduidade e fatores disciplinares. Responde a RQ2 e RQ4.',
            'Population_Scope': 'Ensino Médio Público (Louisiana)', 'Intervention_Scope': 'Machine Learning com Aprendizado Desbalanceado', 'Outcome_Scope': 'Predição de Risco de Abandono Escolar',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 8:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Desfecho fora do escopo: O trabalho desenvolve modelos de Machine Learning para classificação de violência contra crianças no contexto de programas de assistência social externa, sem relação com ferramentas educacionais de recusa ou assiduidade escolar.',
            'Population_Scope': 'Assistência Social Geral', 'Intervention_Scope': 'Machine Learning', 'Outcome_Scope': 'Detecção de Violência Infantil',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 9:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Desfecho fora do escopo (EC2): Estudo focado exclusivamente em evasão escolar decorrente de privação socioeconômica severa e fatores estruturais em países em desenvolvimento (extrema pobreza, calamidades naturais, casamentos infantis), sem abordar recusa escolar ou fatores socioemocionais.',
            'Population_Scope': 'Educação Básica (Índia/Bangladesh)', 'Intervention_Scope': 'Machine Learning', 'Outcome_Scope': 'Evasão por Causas Estruturais/Pobreza',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 10:
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Utiliza modelos de ensemble (XGBoost e Random Forest) integrados à interpretabilidade por IA Explicável (XAI via LIME) para predizer risco de abandono no ensino secundário, analisando variáveis compostas de estresse-ansiedade (Stress-Anxiety) e apoio parental. Responde a RQ2, RQ3 e RQ4.',
            'Population_Scope': 'Ensino Secundário / Médio', 'Intervention_Scope': 'Ensemble Learning (XGBoost/RF) + XAI (LIME)', 'Outcome_Scope': 'Risco de Evasão Escolar + Fatores de Estresse e Ansiedade',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 11:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Desfecho fora do escopo: Pesquisa demográfica/epidemiológica focada em fertilidade na adolescência e saúde reprodutiva usando regressão estatística linear sobre dados censitários (NFHS e ASER), sem propor ferramentas de IA ou diagnóstico de recusa escolar.',
            'Population_Scope': 'População Geral / Saúde Pública', 'Intervention_Scope': 'Regressão Estatística', 'Outcome_Scope': 'Fertilidade na Adolescência',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 12:
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Investiga a transição do ensino fundamental ao médio, abordando explicitamente o absenteísmo crônico e motivacional, sentimentos de alienação do aluno, problemas de relacionamento, bullying e recusa em ir à aula, aplicando Deep Learning (DNN e CNN) para predizer e combater as faltas. Responde diretamente a RQ2 e RQ3.',
            'Population_Scope': 'Educação Básica (Fundamental e Médio)', 'Intervention_Scope': 'Deep Learning (DNN / CNN) e Data Analytics', 'Outcome_Scope': 'Predição de Absenteísmo Escolar, Bullying e Alienação',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 13:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Tema fora do escopo: Simulação econométrica de políticas públicas e alívio de pobreza rural (MNREGA / despesas domiciliares), sem propor ferramentas de diagnóstico, rastreio ou predição educacional.',
            'Population_Scope': 'Famílias Rurais (West Bengal)', 'Intervention_Scope': 'Simulação Econométrica', 'Outcome_Scope': 'Pobreza e Consumo Domiciliar',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
    elif idx == 14:
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Propõe método baseado em visão computacional e Machine Learning para identificar emoções e mensurar o nível de engajamento dos estudantes em ambientes educacionais, visando alertar e diminuir precocemente a evasão escolar. Responde a RQ2 e RQ3.',
            'Population_Scope': 'Ambiente Escolar / Educacional', 'Intervention_Scope': 'Visão Computacional e Machine Learning', 'Outcome_Scope': 'Monitoramento Emocional e Prevenção de Evasão',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type, 'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

def exportar_excel_ieee_14(df, excel_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Triagem IEEE - Oficial (14)"
    
    headers = [
        "ID Estudo", "Decisão", "Critério", "Justificativa Específica e Única",
        "População (P)", "Intervenção (I)", "Desfecho (O)",
        "Título do Artigo", "Autores", "Ano", "Veículo (Conferência / Revista)",
        "Tipo BibTeX", "DOI", "Arquivo Fonte", "Abstract (Resumo)"
    ]
    ws.append(headers)
    
    header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    
    inc_fill = PatternFill(start_color="D9EAD3", end_color="D9EAD3", fill_type="solid") # Verde claro
    inc_font = Font(name="Segoe UI", size=10, bold=True, color="274E13")
    
    exc_fill = PatternFill(start_color="FCE5CD", end_color="FCE5CD", fill_type="solid") # Laranja claro
    exc_font = Font(name="Segoe UI", size=10, bold=False, color="783F04")
    
    border_subtle = Border(
        left=Side(style='thin', color='E0E0E0'),
        right=Side(style='thin', color='E0E0E0'),
        top=Side(style='thin', color='E0E0E0'),
        bottom=Side(style='thin', color='E0E0E0')
    )
    
    ws.row_dimensions[1].height = 28
    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
    for row_idx, row in df.iterrows():
        r_num = row_idx + 2
        ws.row_dimensions[r_num].height = 38
        excel_row = [
            row['Study_ID'], row['Decision'], row['Criterion'], row['Reason'],
            row['Population_Scope'], row['Intervention_Scope'], row['Outcome_Scope'],
            row['Title'], row['Authors'], row['Year'], row['Venue'],
            row['Entry_Type'], row['DOI'], row['Source_File'], row['Abstract']
        ]
        ws.append(excel_row)
        
        dec = row['Decision']
        d_cell = ws.cell(row=r_num, column=2)
        d_cell.fill = inc_fill if dec == 'Incluído' else exc_fill
        d_cell.font = inc_font if dec == 'Incluído' else exc_font
        d_cell.alignment = Alignment(horizontal="center", vertical="center")
        
        for c_idx in range(1, len(headers) + 1):
            c = ws.cell(row=r_num, column=c_idx)
            c.border = border_subtle
            if c_idx not in (2, 8, 15):
                c.alignment = Alignment(vertical="center")
            if c_idx in (4, 8, 15):
                c.alignment = Alignment(vertical="top", wrap_text=True)

    col_widths = {
        1: 12, 2: 12, 3: 14, 4: 52, 5: 24, 6: 28, 7: 30,
        8: 45, 9: 25, 10: 8, 11: 30, 12: 14, 13: 25, 14: 25, 15: 55
    }
    for col_idx, width in col_widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = width
        
    ws.freeze_panes = 'C2'
    ws.auto_filter.ref = ws.dimensions
    wb.save(excel_path)
    print(f"Planilha Excel IEEE atualizada: {excel_path}")

def main():
    bib_file = '02_buscas_brutas/IEE/IEEE Xplore Citation BibTeX Download 2026.9.24.19.12.30.bib'
    entries = parse_ieee_bib(bib_file)
    print(f"Processando {len(entries)} artigos oficiais da IEEE...")

    avaliacoes = []
    for idx, item in enumerate(entries, start=1):
        av = avaliar_estudo_14(item, idx)
        avaliacoes.append(av)

    df = pd.DataFrame(avaliacoes)

    csv_path = '03_selecao_triagem/02_triagem_resumo/triagem_ieee.csv'
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f"CSV de triagem IEEE salvo em: {csv_path}")

    xlsx_path = '03_selecao_triagem/02_triagem_resumo/triagem_ieee.xlsx'
    exportar_excel_ieee_14(df, xlsx_path)

    total = len(df)
    incluidos = len(df[df['Decision'] == 'Incluído'])
    excluidos = len(df[df['Decision'] == 'Excluído'])

    print("\n" + "="*60)
    print("RESULTADO DEFINITIVO DA BASE IEEE XPLORE (14 ARTIGOS)")
    print("="*60)
    print(f"Total de registros da consulta: {total}")
    print(f"Estudos INCLUÍDOS para Leitura Completa: {incluidos} ({incluidos/total*100:.1f}%)")
    print(f"Estudos EXCLUÍDOS: {excluidos} ({excluidos/total*100:.1f}%)")
    print("\nEstudos Incluídos:")
    for _, r in df[df['Decision'] == 'Incluído'].iterrows():
        print(f" - [{r['Study_ID']}] ({r['Year']}) {r['Title']}")
    print("="*60)

if __name__ == '__main__':
    main()
