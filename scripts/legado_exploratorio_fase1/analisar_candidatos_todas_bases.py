import pandas as pd
import re
import json

df_unique = pd.read_csv('03_selecao_triagem/01_deduplicacao/registros_unicos.csv')
print(f"Total de registros únicos: {len(df_unique)}")

sd_records = df_unique[df_unique['Source_Database'] == 'ScienceDirect']
scopus_records = df_unique[df_unique['Source_Database'] == 'Scopus']
wos_records = df_unique[df_unique['Source_Database'] == 'Web of Science']
springer_records = df_unique[df_unique['Source_Database'] == 'Springer Link']

k12_pattern = re.compile(r'\b(k-12|k12|primary school|elementary school|middle school|secondary school|high school|school-aged|adolescent|adolescents|child|children|youth|pupils|school attendance|school refusal|school avoidance|school absenteeism|absenteeism in school|student dropout)\b', re.IGNORECASE)
higher_ed_pattern = re.compile(r'\b(undergraduate|university student|college student|higher education|medical student|medical school|nursing student|tertiary education|postsecondary|mba student|engineering student|bachelor|mooc|university dropout)\b', re.IGNORECASE)
ai_pattern = re.compile(r'\b(machine learning|artificial intelligence|deep learning|predictive model|neural network|random forest|decision tree|support vector|early warning|classification model|data mining|natural language processing|nlp|xgboost|gradient boosting|logistic regression|learning analytics)\b', re.IGNORECASE)
scale_pattern = re.compile(r'\b(scared|sras|sras-r|dass|cbcl|sdq|screening instrument|psychometric|scale|questionnaire|inventory|diagnostic tool)\b', re.IGNORECASE)
phenom_pattern = re.compile(r'\b(school refusal|school avoidance|school absenteeism|chronic absenteeism|school attendance problem|truancy|school dropout|school disengagement|truant)\b', re.IGNORECASE)

for db_name, subset in [('ScienceDirect', sd_records), ('Scopus', scopus_records), ('Web of Science', wos_records), ('Springer Link', springer_records)]:
    cands = []
    for idx, row in subset.iterrows():
        text = f"{row['Title']} {row['Abstract']} {row.get('Keywords', '')}".lower()
        has_phenom = bool(phenom_pattern.search(text))
        has_ai_or_scale = bool(ai_pattern.search(text) or scale_pattern.search(text))
        is_higher_ed = bool(higher_ed_pattern.search(text)) and not bool(k12_pattern.search(text))
        
        if has_phenom and has_ai_or_scale and not is_higher_ed:
            cands.append(row)
    print(f"{db_name}: {len(cands)} candidatos preliminares de alta aderência temática")
