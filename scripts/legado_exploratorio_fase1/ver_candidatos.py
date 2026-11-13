import json

with open('02_buscas_brutas/ACM/acm_consolidado_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for idx in [0, 31, 38, 41, 47, 70]:
    it = data[idx]
    print(f"=== ITEM {idx+1}: {it.get('title')} ({it.get('year')}) ===")
    print("VENUE:", it.get('booktitle') or it.get('journal'))
    print("PAGES:", it.get('pages'), "| NUMPAGES:", it.get('numpages'))
    print("ABSTRACT:", it.get('abstract'))
    print("-" * 80)
