import glob
import re
import os
import json

def parse_bib_balanced(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    entries = []
    # Encontra @tipo{
    i = 0
    n = len(content)
    while i < n:
        at_pos = content.find('@', i)
        if at_pos == -1:
            break
            
        # Pega tipo
        brace_open = content.find('{', at_pos)
        if brace_open == -1:
            break
            
        entry_type = content[at_pos+1:brace_open].strip().lower()
        if not entry_type.isalnum():
            i = at_pos + 1
            continue
            
        # Agora acha o fechamento da entrada balanceando chaves
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
            # Não balanceou, pula
            i = brace_open + 1
            continue
            
        entry_body = content[body_start:curr-1]
        i = curr
        
        # Primeira parte é cite_key até a primeira vírgula
        comma_pos = entry_body.find(',')
        if comma_pos == -1:
            continue
        cite_key = entry_body[:comma_pos].strip()
        fields_str = entry_body[comma_pos+1:]
        
        # Agora faz o parser de cada campo field = { ... } ou field = "..." ou field = 123
        fields = {
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
            'numpages': '',
            'keywords': '',
            'publisher': ''
        }
        
        # Regex para achar nome do campo
        pos = 0
        fn = len(fields_str)
        while pos < fn:
            # Procura nome do campo seguido de =
            m_field = re.search(r'\b([a-zA-Z_]+)\s*=', fields_str[pos:])
            if not m_field:
                break
                
            fname = m_field.group(1).lower()
            val_start = pos + m_field.end()
            
            # Pula espaços
            while val_start < fn and fields_str[val_start].isspace():
                val_start += 1
                
            if val_start >= fn:
                break
                
            first_ch = fields_str[val_start]
            if first_ch == '{':
                # Balanceia chaves para o valor
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
                # Procura aspas de fechamento
                c = val_start + 1
                while c < fn and fields_str[c] != '"':
                    if fields_str[c] == '\\' and c + 1 < fn:
                        c += 2
                    else:
                        c += 1
                val = fields_str[val_start+1:c]
                pos = c + 1
            else:
                # Número ou literal até a próxima vírgula
                c = val_start
                while c < fn and fields_str[c] not in (',', '\n', '\r'):
                    c += 1
                val = fields_str[val_start:c]
                pos = c
                
            val = re.sub(r'\s+', ' ', val).strip()
            val = re.sub(r'[{}]', '', val)
            if fname in fields:
                fields[fname] = val
                
        entries.append(fields)
        
    return entries

def main():
    bib_files = sorted(glob.glob('02_buscas_brutas/ACM/*.bib'))
    all_entries = []
    
    for f in bib_files:
        parsed = parse_bib_balanced(f)
        print(f"Lidos {len(parsed)} artigos de {f}")
        all_entries.extend(parsed)
        
    print(f"Total de registros lidos da ACM: {len(all_entries)}")
    
    with open('02_buscas_brutas/ACM/acm_consolidado_raw.json', 'w', encoding='utf-8') as out:
        json.dump(all_entries, out, ensure_ascii=False, indent=2)
        
    print("Salvo com sucesso em 02_buscas_brutas/ACM/acm_consolidado_raw.json")

if __name__ == '__main__':
    main()
