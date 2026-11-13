import os
import re
import glob
import csv
import json
import pandas as pd

def parse_bib_file(filepath, source_db):
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
            if ch == '{': depth += 1
            elif ch == '}': depth -= 1
            curr += 1
        if depth != 0:
            i = brace_open + 1
            continue
        entry_body = content[body_start:curr-1]
        i = curr
        comma_pos = entry_body.find(',')
        if comma_pos == -1: continue
        cite_key = entry_body[:comma_pos].strip()
        fields_str = entry_body[comma_pos+1:]
        
        data = {
            'Source_Database': source_db,
            'Original_ID': cite_key,
            'Entry_Type': entry_type,
            'Source_File': os.path.basename(filepath),
            'Title': '',
            'Authors': '',
            'Year': '',
            'Abstract': '',
            'DOI': '',
            'URL': '',
            'Venue': '',
            'Keywords': ''
        }
        
        pos = 0
        fn = len(fields_str)
        while pos < fn:
            m_field = re.search(r'\b([a-zA-Z_\-]+)\s*=', fields_str[pos:])
            if not m_field: break
            raw_field = m_field.group(1).lower().replace('-', '_')
            val_start = pos + m_field.end()
            while val_start < fn and fields_str[val_start].isspace(): val_start += 1
            if val_start >= fn: break
            first_ch = fields_str[val_start]
            if first_ch == '{':
                d = 1; c = val_start + 1
                while c < fn and d > 0:
                    if fields_str[c] == '{': d += 1
                    elif fields_str[c] == '}': d -= 1
                    c += 1
                val = fields_str[val_start+1:c-1]
                pos = c
            elif first_ch == '"':
                c = val_start + 1
                while c < fn and fields_str[c] != '"':
                    if fields_str[c] == '\\' and c + 1 < fn: c += 2
                    else: c += 1
                val = fields_str[val_start+1:c]
                pos = c + 1
            else:
                c = val_start
                while c < fn and fields_str[c] not in (',', '\n', '\r', '}'): c += 1
                val = fields_str[val_start:c].strip()
                pos = c + 1
            
            clean_val = re.sub(r'\s+', ' ', val).strip(' {}\"\'')
            if raw_field in ('title',): data['Title'] = clean_val
            elif raw_field in ('author', 'authors'): data['Authors'] = clean_val
            elif raw_field in ('year', 'publication_year'): data['Year'] = clean_val
            elif raw_field in ('abstract',): data['Abstract'] = clean_val
            elif raw_field in ('doi',): data['DOI'] = clean_val
            elif raw_field in ('url',): data['URL'] = clean_val
            elif raw_field in ('booktitle', 'journal', 'journal_title'):
                if not data['Venue']: data['Venue'] = clean_val
            elif raw_field in ('keywords', 'author_keywords', 'index_keywords'):
                data['Keywords'] = (data['Keywords'] + '; ' + clean_val).strip('; ')
        
        entries.append(data)
    return entries

def parse_springer_csv(filepath):
    df = pd.read_csv(filepath)
    entries = []
    for idx, row in df.iterrows():
        entries.append({
            'Source_Database': 'Springer Link',
            'Original_ID': f"SPRINGER_{idx+1:04d}",
            'Entry_Type': str(row.get('Content Type', 'article')).lower(),
            'Source_File': os.path.basename(filepath),
            'Title': str(row.get('Item Title', '')).strip(),
            'Authors': str(row.get('Authors', '')).strip(),
            'Year': str(row.get('Publication Year', '')).strip(),
            'Abstract': '',
            'DOI': str(row.get('Item DOI', '')).strip(),
            'URL': str(row.get('URL', '')).strip(),
            'Venue': str(row.get('Publication Title', '')).strip(),
            'Keywords': ''
        })
    return entries

def normalize_doi(doi):
    if not doi: return ''
    doi = doi.lower().strip()
    doi = re.sub(r'^https?://(dx\.)?doi\.org/', '', doi)
    doi = re.sub(r'^doi:', '', doi)
    doi = re.sub(r'\s+', '', doi)
    return doi.strip().strip('/')

def normalize_title(title):
    if not title: return ''
    t = title.lower()
    t = re.sub(r'[^a-z0-9\s]', '', t)
    return re.sub(r'\s+', ' ', t).strip()

def main():
    all_records = []
    for f in sorted(glob.glob('02_buscas_brutas/ACM/*.bib')):
        all_records.extend(parse_bib_file(f, 'ACM DL'))
    for f in sorted(glob.glob('02_buscas_brutas/IEE/*.bib')):
        all_records.extend(parse_bib_file(f, 'IEEE Xplore'))
    for f in sorted(glob.glob('02_buscas_brutas/sciencedirect/*.bib')):
        all_records.extend(parse_bib_file(f, 'ScienceDirect'))
    for f in sorted(glob.glob('02_buscas_brutas/scopus/*.bib')):
        all_records.extend(parse_bib_file(f, 'Scopus'))
    for f in sorted(glob.glob('02_buscas_brutas/wos/*.bib')):
        all_records.extend(parse_bib_file(f, 'Web of Science'))
    springer_file = '02_buscas_brutas/springer_link/SearchResults (3).csv'
    all_records.extend(parse_springer_csv(springer_file))
    
    print(f"Total bruto: {len(all_records)}")
    
    # Deduplicação
    seen_dois = {}
    seen_titles = {}
    unique_records = []
    duplicates = []
    
    # Prioridade para manter registro com resumo completo
    # Scopus, WoS, ScienceDirect, IEEE, ACM > Springer
    def db_priority(db):
        return {
            'Scopus': 1,
            'Web of Science': 2,
            'ScienceDirect': 3,
            'IEEE Xplore': 4,
            'ACM DL': 5,
            'Springer Link': 6
        }.get(db, 99)
        
    all_records.sort(key=lambda r: (db_priority(r['Source_Database']), 0 if r['Abstract'] else 1))
    
    for r in all_records:
        doi = normalize_doi(r['DOI'])
        norm_title = normalize_title(r['Title'])
        
        is_dup = False
        dup_of = None
        match_type = None
        
        if doi and doi in seen_dois:
            is_dup = True
            dup_of = seen_dois[doi]
            match_type = f"DOI ({doi})"
        elif len(norm_title) >= 20 and norm_title in seen_titles:
            is_dup = True
            dup_of = seen_titles[norm_title]
            match_type = f"Title ({norm_title[:40]}...)"
            
        if is_dup:
            duplicates.append({
                'Source_Database': r['Source_Database'],
                'Original_ID': r['Original_ID'],
                'Title': r['Title'],
                'DOI': r['DOI'],
                'Duplicate_Of_ID': dup_of['Study_ID'],
                'Duplicate_Of_DB': dup_of['Source_Database'],
                'Match_Type': match_type
            })
            # Se o registro duplicado tiver dados adicionais (como DOI ou Abstract), preenche no primário
            if not dup_of['DOI'] and r['DOI']: dup_of['DOI'] = r['DOI']
            if not dup_of['Abstract'] and r['Abstract']: dup_of['Abstract'] = r['Abstract']
            if r['Source_Database'] not in dup_of['Sources']:
                dup_of['Sources'].append(r['Source_Database'])
        else:
            study_id = f"S{len(unique_records)+1:04d}"
            r['Study_ID'] = study_id
            r['Sources'] = [r['Source_Database']]
            if doi: seen_dois[doi] = r
            if len(norm_title) >= 20: seen_titles[norm_title] = r
            unique_records.append(r)
            
    print(f"\n--- Estatísticas de Deduplicação ---")
    print(f"Total Bruto: {len(all_records)}")
    print(f"Duplicatas Removidas (EC3): {len(duplicates)}")
    print(f"Registros Únicos para Triagem: {len(unique_records)}")
    
    dup_by_db = pd.DataFrame(duplicates)['Source_Database'].value_counts()
    print("\nDuplicatas por Base de Origem:")
    print(dup_by_db)
    
    unique_by_db = pd.DataFrame(unique_records)['Source_Database'].value_counts()
    print("\nRegistros Únicos por Base Primária:")
    print(unique_by_db)
    
    # Criar pasta 01_deduplicacao se não existir
    os.makedirs('03_selecao_triagem/01_deduplicacao', exist_ok=True)
    pd.DataFrame(duplicates).to_csv('03_selecao_triagem/01_deduplicacao/duplicatas_removidas.csv', index=False, encoding='utf-8-sig')
    pd.DataFrame(unique_records).to_csv('03_selecao_triagem/01_deduplicacao/registros_unicos.csv', index=False, encoding='utf-8-sig')
    print("\nArquivos salvos em 03_selecao_triagem/01_deduplicacao/ com sucesso!")

if __name__ == '__main__':
    main()
