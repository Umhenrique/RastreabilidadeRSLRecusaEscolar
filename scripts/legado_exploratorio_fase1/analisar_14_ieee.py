import os
import re
import json
import sys
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding='utf-8')

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

def main():
    bib_file = '02_buscas_brutas/IEE/IEEE Xplore Citation BibTeX Download 2026.9.24.19.12.30.bib'
    entries = parse_ieee_bib(bib_file)
    print(f"Total de artigos lidos no arquivo: {len(entries)}")
    for idx, e in enumerate(entries, 1):
        print(f"\n[{idx}] {e.get('title')} ({e.get('year')})")
        print(f"    Autores: {e.get('author')[:80]}")
        print(f"    Veículo: {e.get('booktitle') or e.get('journal')}")
        print(f"    DOI: {e.get('doi')}")
        print(f"    Abstract: {e.get('abstract')[:200]}...")

if __name__ == '__main__':
    main()
