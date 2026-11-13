import os
import re
import json
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def normalizar_texto(txt):
    if not isinstance(txt, str): return ""
    return re.sub(r'\s+', ' ', txt).strip()

def avaliar_registro(row):
    title = normalizar_texto(row.get('Title', ''))
    abstract = normalizar_texto(row.get('Abstract', ''))
    keywords = normalizar_texto(row.get('Keywords', ''))
    venue = normalizar_texto(row.get('Venue', ''))
    entry_type = normalizar_texto(row.get('Entry_Type', '')).lower()
    source_db = row.get('Source_Database', '')
    study_id = row.get('Study_ID', '')
    
    text = f"{title} {abstract} {keywords}".lower()
    title_lower = title.lower()
    
    # 1. EC1: Documentos que não são artigos/conferências originais
    if entry_type in ('proceedings', 'book', 'collection'):
        return {
            'Decision': 'Excluído', 'Criterion': 'EC1',
            'Reason': 'Tipo de documento incompatível: Volume completo de anais (Proceedings) ou livro integral, e não um artigo individual de pesquisa.',
            'Population_Scope': 'N/A', 'Intervention_Scope': 'N/A', 'Outcome_Scope': 'N/A'
        }
    if re.search(r'\b(table of contents|scientific abstract sessions|poster abstracts|index|e-poster viewing|preface|editorial)\b', title_lower):
        return {
            'Decision': 'Excluído', 'Criterion': 'EC1',
            'Reason': 'Tipo de documento incompatível: Front matter, índice, resumo de pôster ou editorial de conferência sem dados empíricos.',
            'Population_Scope': 'N/A', 'Intervention_Scope': 'N/A', 'Outcome_Scope': 'N/A'
        }
        
    # 2. EC2.1: População fora do escopo (Ensino Superior / Graduação / MOOCs / Adultos corporativos)
    has_k12 = bool(re.search(r'\b(k-12|k12|primary school|elementary school|middle school|secondary school|high school|school-aged|adolescent|adolescents|child|children|youth|pupil|pupils|school student|school students|pediatric|escola pública|educação básica|ensino médio|ensino fundamental)\b', text))
    is_higher_ed = bool(re.search(r'\b(undergraduate|university student|university students|college student|college students|higher education|medical student|medical students|medical school|nursing student|nursing students|tertiary education|postsecondary|mba student|engineering student|engineering students|bachelor|mooc|university dropout|college dropout|faculty of)\b', text))
    
    if is_higher_ed and not has_k12:
        return {
            'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'População fora do escopo (EC2): Estudo focado exclusivamente no Ensino Superior (estudantes universitários, faculdade, graduação ou MOOCs), sem aplicação na Educação Básica (K-12).',
            'Population_Scope': 'Ensino Superior / Universitário', 'Intervention_Scope': 'Modelos Preditivos / Estatística', 'Outcome_Scope': 'Evasão no Ensino Superior'
        }
        
    # Absenteísmo corporativo / de trabalho
    if re.search(r'\b(workplace absenteeism|sickness absence among employees|occupational health|corporate absenteeism|worker absenteeism|employee turnover)\b', text):
        return {
            'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'População e contexto fora do escopo (EC2): Estudo focado em absenteísmo no ambiente de trabalho corporativo / licenças médicas de funcionários adultos, sem relação com recusa ou absenteísmo escolar.',
            'Population_Scope': 'Trabalhadores Adultos / Corporativo', 'Intervention_Scope': 'Saúde Ocupacional', 'Outcome_Scope': 'Absenteísmo no Trabalho'
        }

    # 3. EC2.3: Condições puramente médicas/clínicas sem relação com ferramentas de triagem escolar
    if re.search(r'\b(bowel disorders|fibromyalgia|asthma-friendly|ciliary dyskinesia|chinese-western medicine|tuberculosis survivors|air quality in cities|firearm injury deaths)\b', text) and not re.search(r'\b(school refusal|chronic absenteeism|school attendance)\b', text):
        return {
            'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Desfecho e contexto fora do escopo (EC2): Pesquisa biomédica / clínica sobre enfermidades físicas ou poluição ambiental, sem relação com ferramentas preditivas ou diagnósticas de recusa ou assiduidade escolar.',
            'Population_Scope': 'Clínica Médica Geral', 'Intervention_Scope': 'Tratamento Clínico / Farmacológico', 'Outcome_Scope': 'Condição Médica Física'
        }

    # 4. Checagem de Fenômeno Central
    has_school_refusal = bool(re.search(r'\b(school refusal|school avoidance|recusa escolar|evitação escolar|ebsa|emotionally based school avoidance|school aversion)\b', text))
    has_absenteeism = bool(re.search(r'\b(chronic absenteeism|school absenteeism|persistent absenteeism|school attendance problem|school attendance problems|school non-attendance|school nonattendance|truancy|absenteísmo escolar|attendance problem|attendance problems)\b', text))
    has_dropout_k12 = bool(re.search(r'\b(school dropout|student dropout|high school dropout|early school leaving|school disengagement|evasão escolar|dropout risk)\b', text)) and (has_k12 or "school" in text)

    if not (has_school_refusal or has_absenteeism or has_dropout_k12):
        return {
            'Decision': 'Excluído', 'Criterion': 'EC2',
            'Reason': 'Desfecho fora do escopo (EC2): O estudo não investiga recusa escolar, absenteísmo crônico, problemas de assiduidade escolar ou evasão na Educação Básica.',
            'Population_Scope': 'Educação / Psicologia Geral', 'Intervention_Scope': 'Diversas', 'Outcome_Scope': 'Desfechos Não Escolares / Gerais'
        }

    # 5. Checagem de Ferramenta / Intervenção (IA, ML, Predição, EWS, Instrumentos Psicométricos, Triagem)
    has_ai_ml = bool(re.search(r'\b(machine learning|artificial intelligence|deep learning|predictive model|predictive models|predictive analytics|neural network|neural networks|random forest|decision tree|decision trees|support vector|svm|early warning|early warning systems|early detection|early identification|classification model|classification models|data mining|natural language processing|nlp|xgboost|gradient boosting|learning analytics|supervised learning|risk prediction|predicting|prediction|nomogram|network analysis|latent profile|latent class)\b', text))
    has_scale = bool(re.search(r'\b(scared|sras|sras-r|dass|cbcl|sdq|qta30|screen|screening tool|screening instrument|psychometric|diagnostic instrument|scale|scales|inventory|questionnaire|questionnaires|assessment)\b', text))
    has_socioemotional = bool(re.search(r'\b(socio-emotional|socioemotional|social-emotional|mental health|anxiety|depression|bullying|peer victimization|loneliness|stress|psychological distress|wellbeing|well-being|psychosocial|behavioral|behavioural|adhd|autism|autistic)\b', text))

    # Critério de Inclusão Central: Fenômeno Escolar + (IA/ML ou Instrumento Psicométrico/Diagnóstico) + (Socioemocional ou Assiduidade)
    if (has_school_refusal or has_absenteeism or has_dropout_k12):
        pop_desc = "Educação Básica (K-12)"
        if "primary" in text or "elementary" in text: pop_desc = "Educação Básica (Ensino Fundamental Inicial)"
        elif "middle school" in text: pop_desc = "Educação Básica (Ensino Fundamental Final)"
        elif "high school" in text or "médio" in text: pop_desc = "Educação Básica (Ensino Médio)"
        elif "adolescent" in text: pop_desc = "Educação Básica (Adolescentes)"
        elif "children" in text or "child" in text: pop_desc = "Educação Básica (Crianças)"
        elif "youth" in text: pop_desc = "Educação Básica (Jovens/Youth)"

        out_desc = "Predição / Detecção de Absenteísmo e Evasão"
        if has_school_refusal: out_desc = "Rastreio e Diagnóstico de Recusa Escolar / EBSA"
        elif has_absenteeism: out_desc = "Predição de Absenteísmo Crônico Escolar"
        elif has_dropout_k12: out_desc = "Predição de Risco de Abandono Escolar no K-12"

        if has_ai_ml:
            interv_desc = "Modelos de Machine Learning / IA e Análise Preditiva"
            if "deep learning" in text or "cnn" in text: interv_desc = "Deep Learning / Redes Neurais"
            elif "random forest" in text: interv_desc = "Random Forest / Ensemble Learning"
            elif "early warning" in text: interv_desc = "Sistemas de Alerta Precoce (EWS) baseados em IA"
            elif "latent" in text or "network analysis" in text: interv_desc = "Modelagem Analítico-Preditiva / Network Analysis"
            elif has_scale: interv_desc = "Instrumentos Psicométricos combinados com Modelos Preditivos"

            return {
                'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
                'Reason': f'Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos para rastreio ou predição de {out_desc.lower()} na {pop_desc.lower()}, associando fatores de assiduidade e variáveis contextuais/socioemocionais (Responde a RQ2, RQ3 e/ou RQ4).',
                'Population_Scope': pop_desc, 'Intervention_Scope': interv_desc, 'Outcome_Scope': out_desc
            }
            
        elif (has_scale or has_socioemotional) and (has_school_refusal or "attendance problem" in text or "refusal" in text):
            # Artigo psicométrico / diagnóstico com foco direto em recusa escolar ou attendance problems
            interv_desc = "Instrumentos Diagnósticos e Escalas Psicométricas"
            if "scared" in text: interv_desc = "Escala SCARED para Ansiedade e Evitação Escolar"
            elif "screen" in text: interv_desc = "Instrumento SCREEN para Recusa Escolar"
            elif "sras" in text: interv_desc = "Escala SRAS / SRAS-R para Recusa Escolar"

            return {
                'Decision': 'Incluído', 'Criterion': 'IC1, IC2, IC4',
                'Reason': f'Elegível para Leitura de Texto Completo: Avalia, valida ou investiga instrumentos diagnósticos, escalas psicométricas ou ferramentas de triagem clínica/educacional focadas especificamente em recusa escolar e problemas de assiduidade em crianças/adolescentes (Responde à RQ1 e RQ3).',
                'Population_Scope': pop_desc,
                'Intervention_Scope': interv_desc,
                'Outcome_Scope': 'Diagnóstico e Rastreio de Recusa Escolar (SRAS/SCREEN/EBSA)'
            }
            
        else:
            return {
                'Decision': 'Excluído', 'Criterion': 'EC2',
                'Reason': 'Intervenção fora do escopo (EC2): Embora aborde infrequência ou evasão, o estudo não propõe, valida ou investiga ferramentas computacionais de IA/ML, modelos preditivos ou instrumentos diagnósticos psicométricos específicos (análise sociológica qualitativa, descritiva ou ensaio conceitual).',
                'Population_Scope': 'Educação Básica', 'Intervention_Scope': 'Sem Ferramenta Computacional/Psicométrica', 'Outcome_Scope': 'Análise Descritiva de Frequência'
            }

    return {
        'Decision': 'Excluído', 'Criterion': 'EC2',
        'Reason': 'Fora do escopo temático da RSL (EC2): Não atende simultaneamente aos critérios de população, intervenção diagnóstica/preditiva e desfecho de recusa escolar.',
        'Population_Scope': 'Fora do Escopo', 'Intervention_Scope': 'N/A', 'Outcome_Scope': 'N/A'
    }

def main():
    df_unique = pd.read_csv('03_selecao_triagem/01_deduplicacao/registros_unicos.csv')
    print(f"Total de registros a triar: {len(df_unique)}")
    
    # Preservar decisões de IEEE e ACM anteriores
    ieee_prev = {}
    if os.path.exists('03_selecao_triagem/02_triagem_resumo/triagem_ieee.csv'):
        df_ieee_prev = pd.read_csv('03_selecao_triagem/02_triagem_resumo/triagem_ieee.csv')
        for idx, r in df_ieee_prev.iterrows():
            title_norm = re.sub(r'\W+', '', str(r['Title'])).lower()
            ieee_prev[title_norm] = r
            
    acm_prev = {}
    if os.path.exists('03_selecao_triagem/02_triagem_resumo/triagem_acm.csv'):
        df_acm_prev = pd.read_csv('03_selecao_triagem/02_triagem_resumo/triagem_acm.csv')
        for idx, r in df_acm_prev.iterrows():
            title_norm = re.sub(r'\W+', '', str(r['Title'])).lower()
            acm_prev[title_norm] = r
            
    screened_results = []
    
    for idx, row in df_unique.iterrows():
        title = normalizar_texto(row.get('Title', ''))
        title_norm = re.sub(r'\W+', '', title).lower()
        source_db = row.get('Source_Database', '')
        
        if source_db == 'IEEE Xplore' and title_norm in ieee_prev:
            prev = ieee_prev[title_norm]
            eval_dict = {
                'Decision': prev['Decision'],
                'Criterion': prev['Criterion'],
                'Reason': prev['Reason'],
                'Population_Scope': prev['Population_Scope'],
                'Intervention_Scope': prev['Intervention_Scope'],
                'Outcome_Scope': prev['Outcome_Scope']
            }
        elif source_db == 'ACM DL' and title_norm in acm_prev:
            prev = acm_prev[title_norm]
            eval_dict = {
                'Decision': prev['Decision'],
                'Criterion': prev['Criterion'],
                'Reason': prev['Reason'],
                'Population_Scope': prev['Population_Scope'],
                'Intervention_Scope': prev['Intervention_Scope'],
                'Outcome_Scope': prev['Outcome_Scope']
            }
        else:
            eval_dict = avaliar_registro(row)
            
        res_row = dict(row)
        res_row.update(eval_dict)
        screened_results.append(res_row)
        
    df_screened = pd.DataFrame(screened_results)
    
    print("\n--- Resultados Gerais da Triagem por Título e Resumo ---")
    print(f"Total Avaliado: {len(df_screened)}")
    print(df_screened['Decision'].value_counts())
    
    print("\nDetalhamento por Base:")
    cross_tab = pd.crosstab(df_screened['Source_Database'], df_screened['Decision'], margins=True)
    print(cross_tab)
    
    print("\nCritérios de Exclusão Aplicados:")
    excl = df_screened[df_screened['Decision'] == 'Excluído']
    print(excl['Criterion'].value_counts())
    
    out_dir = '03_selecao_triagem/02_triagem_resumo'
    os.makedirs(out_dir, exist_ok=True)
    
    csv_consolidado = os.path.join(out_dir, 'matriz_triagem_consolidada.csv')
    xlsx_consolidado = os.path.join(out_dir, 'matriz_triagem_consolidada.xlsx')
    
    df_screened.to_csv(csv_consolidado, index=False, encoding='utf-8-sig')
    print(f"\nSalvo: {csv_consolidado}")
    
    incluidos = df_screened[df_screened['Decision'] == 'Incluído']
    csv_incluidos = os.path.join(out_dir, 'artigos_incluidos_leitura_completa.csv')
    xlsx_incluidos = os.path.join(out_dir, 'artigos_incluidos_leitura_completa.xlsx')
    
    incluidos.to_csv(csv_incluidos, index=False, encoding='utf-8-sig')
    print(f"Salvo: {csv_incluidos} ({len(incluidos)} estudos incluídos para texto completo)")
    
    try:
        with pd.ExcelWriter(xlsx_consolidado, engine='openpyxl') as writer:
            df_screened.to_excel(writer, sheet_name='Triagem_Geral_Consolidada', index=False)
            incluidos.to_excel(writer, sheet_name='Estudos_Incluidos', index=False)
            excl.to_excel(writer, sheet_name='Estudos_Excluidos', index=False)
        with pd.ExcelWriter(xlsx_incluidos, engine='openpyxl') as writer:
            incluidos.to_excel(writer, sheet_name='Estudos_Incluidos', index=False)
        print(f"Salvo com formatação Excel: {xlsx_consolidado} e {xlsx_incluidos}")
    except Exception as e:
        print(f"Nota Excel: {e}")
        
    for db in df_screened['Source_Database'].unique():
        sub_df = df_screened[df_screened['Source_Database'] == db]
        db_clean = re.sub(r'\W+', '_', db).lower().strip('_')
        sub_csv = os.path.join(out_dir, f"triagem_{db_clean}.csv")
        sub_df.to_csv(sub_csv, index=False, encoding='utf-8-sig')
        print(f"Salvo arquivo da base {db}: {sub_csv} ({len(sub_df[sub_df['Decision']=='Incluído'])} incluídos)")

if __name__ == '__main__':
    main()
