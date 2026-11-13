import json
import re
import os
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def avaliar_estudo_detalhado(item, study_id):
    entry_type = item.get('entry_type', '').lower()
    title = item.get('title', '').strip()
    abstract = item.get('abstract', '').strip()
    year = item.get('year', '').strip()
    authors = item.get('author', '').strip()
    doi = item.get('doi', '').strip()
    url = item.get('url', '').strip()
    source_file = item.get('source_file', '')
    numpages = item.get('numpages', '').strip()
    booktitle = item.get('booktitle', '').strip()
    journal = item.get('journal', '').strip()
    venue = booktitle if booktitle else journal
    
    text_full = f"{title} {abstract}".lower()
    
    # 1. Checagem de tipo de documento (EC1)
    if entry_type in ('proceedings', 'book'):
        return {
            'Study_ID': study_id,
            'Decision': 'Excluído',
            'Criterion': 'EC1',
            'Reason': 'Tipo de documento incompatível: Volume completo de anais de conferência (Proceedings) ou livro, e não um artigo de pesquisa original individual.',
            'Population_Scope': 'N/A',
            'Intervention_Scope': 'N/A',
            'Outcome_Scope': 'N/A',
            'Title': title,
            'Authors': authors,
            'Year': year,
            'Venue': venue,
            'Entry_Type': entry_type,
            'DOI': doi,
            'Source_File': source_file,
            'Abstract': abstract
        }
        
    try:
        pages_int = int(numpages)
        if pages_int <= 2 and not abstract:
            return {
                'Study_ID': study_id,
                'Decision': 'Excluído',
                'Criterion': 'EC1',
                'Reason': f'Tipo de documento incompatível: Resumo estendido/front matter de apenas {pages_int} página(s) sem dados empíricos completos.',
                'Population_Scope': 'N/A',
                'Intervention_Scope': 'N/A',
                'Outcome_Scope': 'N/A',
                'Title': title,
                'Authors': authors,
                'Year': year,
                'Venue': venue,
                'Entry_Type': entry_type,
                'DOI': doi,
                'Source_File': source_file,
                'Abstract': abstract
            }
    except (ValueError, TypeError):
        pass

    # 2. Casos Falsos Cognatos no termo Refusal
    if 'ai refusal' in text_full or 'refuse ai' in text_full or 'decenter ai solutionism' in text_full:
        return {
            'Study_ID': study_id,
            'Decision': 'Excluído',
            'Criterion': 'EC2',
            'Reason': 'Falso cognato de recusa: O estudo aborda recusa do uso de IA (AI refusal / governança algorítmica) por jovens, e não recusa escolar (School Refusal).',
            'Population_Scope': 'Jovens / Ativismo',
            'Intervention_Scope': 'Educação Crítica em IA',
            'Outcome_Scope': 'Recusa de Adoção de IA',
            'Title': title,
            'Authors': authors,
            'Year': year,
            'Venue': venue,
            'Entry_Type': entry_type,
            'DOI': doi,
            'Source_File': source_file,
            'Abstract': abstract
        }

    # 3. Análise de População Exclusivamente Universitária / Superior (EC2)
    ensino_superior_explicit = [
        'higher education', 'undergraduate', 'university students', 'universities', 'college students',
        'tertiary education', 'mooc', 'moocs', 'dropping out of university'
    ]
    ensino_basico_explicit = [
        'k-12', 'k12', 'elementary', 'primary school', 'middle school', 'high school',
        'public schools', 'secondary school', 'basic education', 'school-age', 'schoolchildren'
    ]
    
    is_higher_ed = any(h in text_full for h in ensino_superior_explicit) and not any(b in text_full for b in ensino_basico_explicit)
    if is_higher_ed:
        return {
            'Study_ID': study_id,
            'Decision': 'Excluído',
            'Criterion': 'EC2',
            'Reason': 'População fora do escopo: Estudo voltado exclusivamente ao Ensino Superior (Graduação, Faculdades ou MOOCs universitários), não atendendo ao critério de Educação Básica (K-12).',
            'Population_Scope': 'Ensino Superior / Terciário',
            'Intervention_Scope': 'Modelagem / IA Presente',
            'Outcome_Scope': 'Evasão Universitária',
            'Title': title,
            'Authors': authors,
            'Year': year,
            'Venue': venue,
            'Entry_Type': entry_type,
            'DOI': doi,
            'Source_File': source_file,
            'Abstract': abstract
        }

    # 4. Avaliação Específica de Estudos Elegíveis da Educação Básica
    # Caso 1: ACM_001 - Rubinstein (2019)
    if 'reducing school absenteeism' in title.lower() or 'gothenburg' in text_full:
        return {
            'Study_ID': study_id,
            'Decision': 'Incluído',
            'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Aplica Machine Learning e aplicativo móvel de questionários para prever assiduidade e absenteísmo escolar de estudantes, relacionando fatores de saúde e intervenções preventivas.',
            'Population_Scope': 'Ensino Básico (Alunos de Gotemburgo)',
            'Intervention_Scope': 'Machine Learning + App de Questionários',
            'Outcome_Scope': 'Predição de Absenteísmo e Presença Escolar',
            'Title': title,
            'Authors': authors,
            'Year': year,
            'Venue': venue,
            'Entry_Type': entry_type,
            'DOI': doi,
            'Source_File': source_file,
            'Abstract': abstract
        }

    # Caso 2: ACM_032 - Difficult Lessons on Social Prediction from Wisconsin Public Schools (2025)
    if 'wisconsin public schools' in text_full:
        return {
            'Study_ID': study_id,
            'Decision': 'Incluído',
            'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Avaliação empírica em larga escala de sistemas de alerta precoce (Early Warning Systems - EWS) com modelos preditivos de evasão em mais de 200 mil estudantes da rede pública de ensino básico (Wisconsin). Responde diretamente às RQ2 e RQ4.',
            'Population_Scope': 'Ensino Básico (Escolas Públicas K-12)',
            'Intervention_Scope': 'Early Warning Systems / Modelos Preditivos',
            'Outcome_Scope': 'Predição de Evasão Escolar e Efeito de Intervenções',
            'Title': title,
            'Authors': authors,
            'Year': year,
            'Venue': venue,
            'Entry_Type': entry_type,
            'DOI': doi,
            'Source_File': source_file,
            'Abstract': abstract
        }

    # Caso 3: ACM_039 - Early Alert Systems During a Pandemic (2021)
    if 'early alert systems during a pandemic' in title.lower() or 'concept drift' in text_full and 'high school dropout' in text_full:
        return {
            'Study_ID': study_id,
            'Decision': 'Incluído',
            'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Investiga a robustez e desempenho de modelos de Machine Learning implementados em sistemas de alerta precoce (EWS) para predição de abandono no Ensino Médio (High School Dropout). Responde diretamente às RQ2 e RQ4.',
            'Population_Scope': 'Ensino Médio (High School / Ensino Básico)',
            'Intervention_Scope': 'Machine Learning em Early Warning Systems',
            'Outcome_Scope': 'Predição de Abandono Escolar frente a Desvios de Dados',
            'Title': title,
            'Authors': authors,
            'Year': year,
            'Venue': venue,
            'Entry_Type': entry_type,
            'DOI': doi,
            'Source_File': source_file,
            'Abstract': abstract
        }

    # Caso 4: ACM_042 - Re-envisioning a K-12 Early Warning System with School Climate Factors (2022)
    if 're-envisioning a k-12 early warning system' in title.lower() or ('school climate factors' in text_full and 'k-12' in text_full):
        return {
            'Study_ID': study_id,
            'Decision': 'Incluído',
            'Criterion': 'IC1, IC2, IC4',
            'Reason': 'Elegível para Leitura de Texto Completo: Aplica Machine Learning em Early Warning Systems no Ensino Básico (K-12) integrando diretamente assiduidade escolar (Attendance) com fatores socioemocionais (Socioemotional Learning - SEL) e clima escolar para suporte ao bem-estar do aluno. Responde diretamente às RQ2 e RQ3.',
            'Population_Scope': 'Ensino Básico (K-12)',
            'Intervention_Scope': 'Machine Learning em Early Warning Systems',
            'Outcome_Scope': 'Assiduidade Escolar + Aprendizagem Socioemocional',
            'Title': title,
            'Authors': authors,
            'Year': year,
            'Venue': venue,
            'Entry_Type': entry_type,
            'DOI': doi,
            'Source_File': source_file,
            'Abstract': abstract
        }

    # 5. Demais Estudos: Avaliação por falta de intervenção ou desfecho
    ai_tech_terms = [
        'machine learning', 'artificial intelligence', 'deep learning', 'predictive model',
        'neural network', 'early warning system', 'early alert', 'data mining', 'classification algorithm'
    ]
    has_ai = any(t in text_full for t in ai_tech_terms)
    
    attendance_terms = [
        'school refusal', 'absenteeism', 'attendance', 'truancy', 'dropout', 'drop out', 'disengagement'
    ]
    has_attendance = any(t in text_full for t in attendance_terms)
    
    if not has_ai:
        return {
            'Study_ID': study_id,
            'Decision': 'Excluído',
            'Criterion': 'EC2',
            'Reason': 'Intervenção fora do escopo: O trabalho não desenvolve nem avalia ferramentas diagnósticas, modelos preditivos de Machine Learning/IA ou escalas psicométricas.',
            'Population_Scope': 'Geral/Escolar',
            'Intervention_Scope': 'Ausente',
            'Outcome_Scope': 'Não aplicável',
            'Title': title,
            'Authors': authors,
            'Year': year,
            'Venue': venue,
            'Entry_Type': entry_type,
            'DOI': doi,
            'Source_File': source_file,
            'Abstract': abstract
        }
        
    if not has_attendance:
        return {
            'Study_ID': study_id,
            'Decision': 'Excluído',
            'Criterion': 'EC2',
            'Reason': 'Desfecho fora do escopo: Embora empregue inteligência artificial ou algoritmos, não aborda recusa escolar, absenteísmo crônico, infrequência ou evasão associada a fatores socioemocionais.',
            'Population_Scope': 'Geral',
            'Intervention_Scope': 'IA Presente',
            'Outcome_Scope': 'Fora do escopo',
            'Title': title,
            'Authors': authors,
            'Year': year,
            'Venue': venue,
            'Entry_Type': entry_type,
            'DOI': doi,
            'Source_File': source_file,
            'Abstract': abstract
        }

    # Caso tenha termos gerais mas seja de outro contexto
    return {
        'Study_ID': study_id,
        'Decision': 'Excluído',
        'Criterion': 'EC2',
        'Reason': 'Desfecho e contexto não atendem cumulativamente ao PICOC: O estudo trata de evasão puramente conceitual/estrutural sem mensuração de fatores socioemocionais ou não foca na recusa escolar no ensino básico.',
        'Population_Scope': 'Indeterminado / Misto',
        'Intervention_Scope': 'IA / Algoritmo',
        'Outcome_Scope': 'Geral / Não socioemocional',
        'Title': title,
        'Authors': authors,
        'Year': year,
        'Venue': venue,
        'Entry_Type': entry_type,
        'DOI': doi,
        'Source_File': source_file,
        'Abstract': abstract
    }

def exportar_excel_completo(df, excel_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Triagem ACM - Fase 1"
    
    headers = [
        "ID Estudo", "Decisão", "Critério", "Justificativa Específica e Única",
        "População (P)", "Intervenção (I)", "Desfecho (O)",
        "Título do Artigo", "Autores", "Ano", "Veículo (Conferência / Revista)",
        "Tipo BibTeX", "DOI", "Arquivo Fonte", "Abstract (Resumo)"
    ]
    ws.append(headers)
    
    # Cores
    header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid") # Azul corporativo
    header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    
    inc_fill = PatternFill(start_color="D9EAD3", end_color="D9EAD3", fill_type="solid") # Verde suave
    inc_font = Font(name="Segoe UI", size=10, bold=True, color="274E13")
    
    exc_fill = PatternFill(start_color="FCE5CD", end_color="FCE5CD", fill_type="solid") # Laranja suave
    exc_font = Font(name="Segoe UI", size=10, bold=False, color="783F04")
    
    border_subtle = Border(
        left=Side(style='thin', color='E0E0E0'),
        right=Side(style='thin', color='E0E0E0'),
        top=Side(style='thin', color='E0E0E0'),
        bottom=Side(style='thin', color='E0E0E0')
    )
    
    # Estiliza cabeçalho
    ws.row_dimensions[1].height = 28
    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
    for row_idx, row in df.iterrows():
        r_num = row_idx + 2
        ws.row_dimensions[r_num].height = 36 # Altura confortável para visualização
        excel_row = [
            row['Study_ID'], row['Decision'], row['Criterion'], row['Reason'],
            row['Population_Scope'], row['Intervention_Scope'], row['Outcome_Scope'],
            row['Title'], row['Authors'], row['Year'], row['Venue'],
            row['Entry_Type'], row['DOI'], row['Source_File'], row['Abstract']
        ]
        ws.append(excel_row)
        
        is_inc = (row['Decision'] == 'Incluído')
        d_cell = ws.cell(row=r_num, column=2)
        d_cell.fill = inc_fill if is_inc else exc_fill
        d_cell.font = inc_font if is_inc else exc_font
        d_cell.alignment = Alignment(horizontal="center", vertical="center")
        
        for c_idx in range(1, len(headers) + 1):
            c = ws.cell(row=r_num, column=c_idx)
            c.border = border_subtle
            if c_idx not in (2, 8, 15):
                c.alignment = Alignment(vertical="center")
            if c_idx in (4, 8, 15):
                c.alignment = Alignment(vertical="top", wrap_text=True)

    col_widths = {
        1: 12,  # ID
        2: 12,  # Decisao
        3: 14,  # Criterio
        4: 50,  # Justificativa
        5: 22,  # Populacao
        6: 25,  # Intervencao
        7: 28,  # Desfecho
        8: 45,  # Titulo
        9: 25,  # Autores
        10: 8,  # Ano
        11: 30, # Veiculo
        12: 14, # Tipo BibTeX
        13: 25, # DOI
        14: 15, # Fonte
        15: 55  # Abstract
    }
    for col_idx, width in col_widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = width
        
    ws.freeze_panes = 'C2'
    ws.auto_filter.ref = ws.dimensions
    wb.save(excel_path)
    print(f"Planilha Excel profissional criada com sucesso: {excel_path}")

def main():
    with open('02_buscas_brutas/ACM/acm_consolidado_raw.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    avaliacoes = []
    for idx, item in enumerate(data, start=1):
        study_id = f"ACM_{idx:03d}"
        av = avaliar_estudo_detalhado(item, study_id)
        avaliacoes.append(av)

    df = pd.DataFrame(avaliacoes)
    
    csv_path = '03_selecao_triagem/02_triagem_resumo/triagem_acm.csv'
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f"CSV de triagem salvo em: {csv_path}")

    xlsx_path = '03_selecao_triagem/02_triagem_resumo/triagem_acm.xlsx'
    exportar_excel_completo(df, xlsx_path)

    total = len(df)
    incluidos = len(df[df['Decision'] == 'Incluído'])
    excluidos = len(df[df['Decision'] == 'Excluído'])
    
    print("\n" + "="*60)
    print("RESULTADO FINAL DA TRIAGEM DA BASE ACM")
    print("="*60)
    print(f"Total de registros avaliados: {total}")
    print(f"Estudos INCLUÍDOS para Leitura de Texto Completo: {incluidos}")
    print(f"Estudos EXCLUÍDOS: {excluidos}")
    print("\nDetalhamento dos Critérios de Exclusão:")
    print(df[df['Decision'] == 'Excluído']['Criterion'].value_counts())
    print("="*60)

if __name__ == '__main__':
    main()
