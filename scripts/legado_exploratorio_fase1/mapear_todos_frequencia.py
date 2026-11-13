import json

with open('02_buscas_brutas/ACM/acm_consolidado_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total de artigos: {len(data)}")

termos = ['early warning', 'attendance', 'absenteeism', 'truancy', 'refusal', 'dropout', 'drop out', 'disengagement']

matches = []
for idx, it in enumerate(data):
    txt = (it.get('title', '') + ' ' + it.get('abstract', '')).lower()
    encontrados = [t for t in termos if t in txt]
    if encontrados:
        matches.append((idx + 1, it, encontrados))

print(f"Total de artigos com menções a problemas de frequência/evasão: {len(matches)}")
for num, it, enc in matches:
    print(f"ID: ACM_{num:03d} | Ano: {it.get('year')} | Tipo: {it.get('entry_type')}")
    print(f"Título: {it.get('title')}")
    print(f"Termos: {enc}")
    print(f"Abstract inicial: {it.get('abstract')[:180]}...")
    print("-" * 60)
