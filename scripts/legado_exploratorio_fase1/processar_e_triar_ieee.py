import glob
import re
import os
import json
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def parse_ieee_bib(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    entries = []
    i = 0
    n = len(content)
    while i < n:
        at_pos = content.find('@', i)
        if at_pos == -1:
            break
            
        brace_open = content.find('{', at_pos)
        if brace_open == -1:
            break
            
        entry_type = content[at_pos+1:brace_open].strip().lower()
        if not entry_type.isalnum():
            i = at_pos + 1
            continue
            
        depth = 1
        curr = brace_open + 1
        body_start = curr
        
        while curr < n and depth > 0:
            ch = content[curr]
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
            curr += 1
            
        if depth != 0:
            i = brace_open + 1
            continue
            
        entry_body = content[body_start:curr-1]
        i = curr
        
        comma_pos = entry_body.find(',')
        if comma_pos == -1:
            continue
        cite_key = entry_body[:comma_pos].strip()
        fields_str = entry_body[comma_pos+1:]
        
        data = {
            'entry_type': entry_type,
            'cite_key': cite_key,
            'source_file': os.path.basename(filepath),
            'title': '',
            'author': '',
            'year': '',
            'abstract': '',
            'doi': '',
            'url': '',
            'booktitle': '',
            'journal': '',
            'pages': '',
            'keywords': ''
        }
        
        pos = 0
        fn = len(fields_str)
        while pos < fn:
            m_field = re.search(r'\b([a-zA-Z_]+)\s*=', fields_str[pos:])
            if not m_field:
                break
                
            fname = m_field.group(1).lower()
            val_start = pos + m_field.end()
            
            while val_start < fn and fields_str[val_start].isspace():
                val_start += 1
                
            if val_start >= fn:
                break
                
            first_ch = fields_str[val_start]
            if first_ch == '{':
                d = 1
                c = val_start + 1
                while c < fn and d > 0:
                    if fields_str[c] == '{':
                        d += 1
                    elif fields_str[c] == '}':
                        d -= 1
                    c += 1
                val = fields_str[val_start+1:c-1]
                pos = c
            elif first_ch == '"':
                c = val_start + 1
                while c < fn and fields_str[c] != '"':
                    if fields_str[c] == '\\' and c + 1 < fn:
                        c += 2
                    else:
                        c += 1
                val = fields_str[val_start+1:c]
                pos = c + 1
            else:
                c = val_start
                while c < fn and fields_str[c] not in (',', '\n', '\r'):
                    c += 1
                val = fields_str[val_start:c]
                pos = c
                
            val = re.sub(r'\s+', ' ', val).strip()
            val = re.sub(r'[{}]', '', val)
            if fname in data:
                data[fname] = val
                
        entries.append(data)
        
    return entries

def avaliar_estudo_ieee(item, study_id, acm_dois, acm_titles, vistos_ieee_dois, vistos_ieee_titles):
    title = item.get('title', '').strip()
    abstract = item.get('abstract', '').strip()
    year = item.get('year', '').strip()
    authors = item.get('author', '').strip()
    doi = item.get('doi', '').strip().lower()
    source_file = item.get('source_file', '')
    entry_type = item.get('entry_type', '').lower()
    booktitle = item.get('booktitle', '').strip()
    journal = item.get('journal', '').strip()
    venue = booktitle if booktitle else journal
    
    title_clean = re.sub(r'[^a-zA-Z0-9]', '', title).lower()
    text_full = f"{title} {abstract}".lower()

    # 1. Duplicatas (EC3)
    if doi and (doi in acm_dois or doi in vistos_ieee_dois):
        origem = "ACM" if doi in acm_dois else "IEEE (sub-busca anterior)"
        return {
            'Study_ID': study_id, 'Decision': 'Duplicado', 'Criterion': 'EC3',
            'Reason': f'Estudo duplicado: Artigo já identificado e avaliado na base {origem} (DOI correspondente).',
            'Population_Scope': 'N/A', 'Intervention_Scope': 'N/A', 'Outcome_Scope': 'N/A',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }
        
    if title_clean and (title_clean in acm_titles or title_clean in vistos_ieee_titles):
        origem = "ACM" if title_clean in acm_titles else "IEEE (sub-busca anterior)"
        return {
            'Study_ID': study_id, 'Decision': 'Duplicado', 'Criterion': 'EC3',
            'Reason': f'Estudo duplicado: Artigo com mesmo título já presente na base {origem}.',
            'Population_Scope': 'N/A', 'Intervention_Scope': 'N/A', 'Outcome_Scope': 'N/A',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    if doi: vistos_ieee_dois.add(doi)
    if title_clean: vistos_ieee_titles.add(title_clean)

    # 2. Artigos Específicos Altamente Relevantes (Incluídos)
    # IEEE_001: Ishikura et al. (2020)
    if 'classification of worries and consultations with school refusal students' in title.lower():
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Aplica Machine Learning para classificar motivos de recusa escolar e absenteísmo (truancy) a partir de consultas e relatos de alunos, categorizando fatores interpessoais e familiares. Responde a RQ1, RQ2 e RQ3.',
            'Population_Scope': 'Educação Básica (Alunos com Recusa Escolar)', 'Intervention_Scope': 'Machine Learning / Classificação de Texto', 'Outcome_Scope': 'Recusa Escolar e Motivos de Absenteísmo',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # IEEE_008: Orooji & Chen (2019)
    if 'predicting louisiana public high school dropout' in title.lower():
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Modela a predição de abandono escolar no Ensino Médio público utilizando técnicas de aprendizado de máquina para dados desbalanceados, analisando fatores comportamentais e de assiduidade. Responde a RQ2 e RQ4.',
            'Population_Scope': 'Ensino Médio (High School Pública)', 'Intervention_Scope': 'Machine Learning com Aprendizado Desbalanceado', 'Outcome_Scope': 'Predição de Abandono Escolar',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # IEEE_032: Estudo de predição de ansiedade e School Avoidance (2026)
    if 'predicting the anxiety status among o/l students' in title.lower() or 'school avoidance' in text_full and 'scared' in text_full:
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Integra instrumento psicométrico clínico (questionário SCARED) com algoritmos de Machine Learning (Random Forest) para predição precoce de ansiedade e Evitação Escolar (School Avoidance) em estudantes de ensino básico. Responde diretamente a RQ1, RQ2 e RQ3.',
            'Population_Scope': 'Ensino Secundário / Básico (Estudantes O/L)', 'Intervention_Scope': 'Questionário SCARED + Random Forest Classifier', 'Outcome_Scope': 'Predição de Evitação Escolar (School Avoidance) e Ansiedade',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # IEEE_107: Fezzan Secondary School Dropout & XAI (2026)
    if 'explainable ensemble learning for student dropout prediction' in title.lower():
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Utiliza modelos de ensemble (XGBoost/Random Forest) combinados com técnicas de explicabilidade (XAI via LIME) para predição de risco de evasão em egressos do ensino secundário, analisando ansiedade, estresse e apoio familiar. Responde a RQ2, RQ3 e RQ4.',
            'Population_Scope': 'Ensino Secundário / Médio', 'Intervention_Scope': 'XGBoost / Ensemble Learning + XAI (LIME)', 'Outcome_Scope': 'Predição de Risco de Evasão + Fatores Socioemocionais',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # IEEE_141: Revisão Sistemática de ML em Student Dropout (2026)
    if 'machine learning for student dropout prediction: a systematic review' in title.lower():
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Revisão sistemática sobre o uso de Machine Learning para predição de abandono escolar desde o ensino básico até o superior, mapeando métricas de validação, algoritmos e atributos psicológicos/comportamentais. Atende a IC4 e apoia todas as RQs.',
            'Population_Scope': 'Educação Básica e Superior', 'Intervention_Scope': 'Revisão Sistemática de Modelos de ML', 'Outcome_Scope': 'Métricas, Desafios e Síntese de Predição de Evasão',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # IEEE_206: Detecção de estados emocionais e engajamento via vídeo para evitar dropout (2024)
    if 'analyzing recorded video to evaluate how engaged and emotional students are' in title.lower():
        return {
            'Study_ID': study_id, 'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Propõe método baseado em visão computacional e Machine Learning para monitorar engajamento e estado emocional de alunos, visando identificar precocemente o risco de abandono escolar. Responde a RQ2 e RQ3.',
            'Population_Scope': 'Contexto Escolar / Educacional', 'Intervention_Scope': 'Visão Computacional e Machine Learning', 'Outcome_Scope': 'Engajamento Emocional e Prevenção de Abandono',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # 3. Exclusões por tipo de publicação (EC1)
    if entry_type in ('proceedings', 'book'):
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC1',
            'Reason': 'Tipo de documento incompatível: Volume completo de conferência (Proceedings) ou livro.',
            'Population_Scope': 'N/A', 'Intervention_Scope': 'N/A', 'Outcome_Scope': 'N/A',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # 4. Exclusões Temáticas Refinadas (EC2)
    # Violência digital pura / cyberbullying sem predição de recusa ou assiduidade escolar
    if 'pupils internet safety' in text_full or 'electronic violence' in text_full:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Tema fora do escopo: O estudo foca exclusivamente em segurança digital e violência na internet, sem propor ferramentas diagnósticas ou modelos de predição de absenteísmo ou recusa escolar.',
            'Population_Scope': 'Ensino Básico', 'Intervention_Scope': 'Sem IA/Predição', 'Outcome_Scope': 'Segurança na Internet',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # Sistemas de orientação vocacional ou de carreira universitária
    if 'guidance systems for moroccan students' in text_full or 'career building' in text_full:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Tema fora do escopo: Sistema de recomendação para orientação vocacional e escolha de carreira universitária, sem relação com recusa ou absenteísmo escolar.',
            'Population_Scope': 'Ensino Médio / Superior', 'Intervention_Scope': 'Orientação Vocacional', 'Outcome_Scope': 'Escolha de Carreira',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # Art-education / intervenção pedagógica puramente em artes sem IA ou diagnóstico
    if 'proactive art education' in text_full:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Intervenção fora do escopo: Proposta puramente pedagógica de oficinas artísticas, sem ferramentas de diagnóstico, rastreio psicométrico ou modelos de IA.',
            'Population_Scope': 'Ensino Básico', 'Intervention_Scope': 'Artes / Pedagogia', 'Outcome_Scope': 'Comportamento',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # Evasão escolar por pobreza severa / infraestrutura / casamento infantil (EC2 explícito do protocolo)
    if 'poverty, natural calamities, and early marriages' in text_full:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Desfecho fora do escopo (EC2): Focado exclusivamente em fatores socioeconômicos e estruturais severos (pobreza extrema, desastres naturais, casamento infantil), sem relação com comportamento de recusa ou saúde mental.',
            'Population_Scope': 'Países em Desenvolvimento', 'Intervention_Scope': 'Modelo Geral', 'Outcome_Scope': 'Evasão Socioeconômica Estrutural',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # Captura mecânica de chamada por grafos
    if 'attendance capturing' in text_full and 'alibi' in text_full:
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Intervenção fora do escopo: Sistema de registro automatizado de presença (chamada escolar), sem funções de diagnóstico, triagem preditiva ou suporte socioemocional.',
            'Population_Scope': 'Escolar', 'Intervention_Scope': 'Registro de Presença', 'Outcome_Scope': 'Chamada Eletrônica',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # Ensino superior
    ensino_superior_terms = [
        'higher education', 'undergraduate', 'university students', 'universities', 'college students',
        'tertiary education', 'mooc', 'moocs', 'college dropout', 'university degree', 'engineering students',
        'medical students', 'bachelor', 'undergraduates'
    ]
    ensino_basico_terms = [
        'k-12', 'k12', 'elementary', 'primary school', 'middle school', 'high school',
        'public schools', 'secondary school', 'basic education', 'school-age', 'schoolchildren'
    ]
    if any(h in text_full for h in ensino_superior_terms) and not any(b in text_full for b in ensino_basico_terms):
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'População fora do escopo: Estudo voltado exclusivamente ao Ensino Superior (Graduação, Universidades ou MOOCs), sem contemplar a Educação Básica (K-12).',
            'Population_Scope': 'Ensino Superior', 'Intervention_Scope': 'IA Presente', 'Outcome_Scope': 'Evasão Universitária',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    # Demais estudos
    ai_terms = ['machine learning', 'artificial intelligence', 'deep learning', 'neural network', 'predictive', 'prediction', 'classifier', 'early warning', 'algorithm']
    if not any(t in text_full for t in ai_terms):
        return {
            'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Intervenção fora do escopo: O trabalho não desenvolve nem avalia ferramentas diagnósticas, modelos preditivos de Machine Learning/IA ou escalas psicométricas.',
            'Population_Scope': 'Geral', 'Intervention_Scope': 'Ausente', 'Outcome_Scope': 'Não aplicável',
            'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
            'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
        }

    return {
        'Study_ID': study_id, 'Decision': 'Excluído', 'Criterion': 'EC2',
        'Reason': 'Desfecho fora do escopo: Embora empregue inteligência artificial ou algoritmos, não aborda recusa escolar, absenteísmo crônico ou fatores socioemocionais no ensino básico.',
        'Population_Scope': 'Geral', 'Intervention_Scope': 'IA Presente', 'Outcome_Scope': 'Fora do escopo',
        'Title': title, 'Authors': authors, 'Year': year, 'Venue': venue, 'Entry_Type': entry_type,
        'DOI': doi, 'Source_File': source_file, 'Abstract': abstract
    }

def exportar_excel_ieee(df, excel_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Triagem IEEE - Fase 1"
    
    headers = [
        "ID Estudo", "Decisão", "Critério", "Justificativa Específica e Única",
        "População (P)", "Intervenção (I)", "Desfecho (O)",
        "Título do Artigo", "Autores", "Ano", "Veículo (Conferência / Revista)",
        "Tipo BibTeX", "DOI", "Arquivo Fonte", "Abstract (Resumo)"
    ]
    ws.append(headers)
    
    header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    
    inc_fill = PatternFill(start_color="D9EAD3", end_color="D9EAD3", fill_type="solid")
    inc_font = Font(name="Segoe UI", size=10, bold=True, color="274E13")
    
    dup_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
    dup_font = Font(name="Segoe UI", size=10, bold=True, color="7F6000")
    
    exc_fill = PatternFill(start_color="FCE5CD", end_color="FCE5CD", fill_type="solid")
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
        ws.row_dimensions[r_num].height = 36
        excel_row = [
            row['Study_ID'], row['Decision'], row['Criterion'], row['Reason'],
            row['Population_Scope'], row['Intervention_Scope'], row['Outcome_Scope'],
            row['Title'], row['Authors'], row['Year'], row['Venue'],
            row['Entry_Type'], row['DOI'], row['Source_File'], row['Abstract']
        ]
        ws.append(excel_row)
        
        dec = row['Decision']
        d_cell = ws.cell(row=r_num, column=2)
        if dec == 'Incluído':
            d_cell.fill = inc_fill
            d_cell.font = inc_font
        elif dec == 'Duplicado':
            d_cell.fill = dup_fill
            d_cell.font = dup_font
        else:
            d_cell.fill = exc_fill
            d_cell.font = exc_font
        d_cell.alignment = Alignment(horizontal="center", vertical="center")
        
        for c_idx in range(1, len(headers) + 1):
            c = ws.cell(row=r_num, column=c_idx)
            c.border = border_subtle
            if c_idx not in (2, 8, 15):
                c.alignment = Alignment(vertical="center")
            if c_idx in (4, 8, 15):
                c.alignment = Alignment(vertical="top", wrap_text=True)

    col_widths = {
        1: 12, 2: 12, 3: 14, 4: 50, 5: 22, 6: 25, 7: 28,
        8: 45, 9: 25, 10: 8, 11: 30, 12: 14, 13: 25, 14: 25, 15: 55
    }
    for col_idx, width in col_widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = width
        
    ws.freeze_panes = 'C2'
    ws.auto_filter.ref = ws.dimensions
    wb.save(excel_path)
    print(f"Planilha Excel IEEE salva em: {excel_path}")

def main():
    acm_dois = set()
    acm_titles = set()
    acm_raw_path = '02_buscas_brutas/ACM/acm_consolidado_raw.json'
    if os.path.exists(acm_raw_path):
        with open(acm_raw_path, 'r', encoding='utf-8') as f:
            acm_data = json.load(f)
            for item in acm_data:
                d = item.get('doi', '').strip().lower()
                t = re.sub(r'[^a-zA-Z0-9]', '', item.get('title', '')).lower()
                if d: acm_dois.add(d)
                if t: acm_titles.add(t)

    ieee_files = sorted(glob.glob('02_buscas_brutas/IEE/*.bib'))
    all_ieee_entries = []
    for f in ieee_files:
        parsed = parse_ieee_bib(f)
        all_ieee_entries.extend(parsed)

    vistos_ieee_dois = set()
    vistos_ieee_titles = set()
    avaliacoes = []

    for idx, item in enumerate(all_ieee_entries, start=1):
        study_id = f"IEEE_{idx:03d}"
        av = avaliar_estudo_ieee(item, study_id, acm_dois, acm_titles, vistos_ieee_dois, vistos_ieee_titles)
        avaliacoes.append(av)

    df = pd.DataFrame(avaliacoes)

    csv_path = '03_selecao_triagem/02_triagem_resumo/triagem_ieee.csv'
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')

    xlsx_path = '03_selecao_triagem/02_triagem_resumo/triagem_ieee.xlsx'
    exportar_excel_ieee(df, xlsx_path)

    total = len(df)
    duplicados = len(df[df['Decision'] == 'Duplicado'])
    incluidos = len(df[df['Decision'] == 'Incluído'])
    excluidos = len(df[df['Decision'] == 'Excluído'])

    print("\n" + "="*60)
    print("RESULTADO CALIBRADO DA TRIAGEM DA BASE IEEE XPLORE")
    print("="*60)
    print(f"Total bruto de registros coletados na IEEE: {total}")
    print(f"Duplicatas identificadas (EC3): {duplicados}")
    print(f"Estudos únicos avaliados por Título/Resumo: {total - duplicados}")
    print(f"Estudos INCLUÍDOS para Leitura Completa: {incluidos}")
    print(f"Estudos EXCLUÍDOS na triagem: {excluidos}")
    print("="*60)

if __name__ == '__main__':
    main()
