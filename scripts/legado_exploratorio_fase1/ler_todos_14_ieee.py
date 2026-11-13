import sys
sys.path.append('scripts')
from analisar_14_ieee import parse_ieee_bib

entries = parse_ieee_bib('02_buscas_brutas/IEE/IEEE Xplore Citation BibTeX Download 2026.9.24.19.12.30.bib')

for idx, e in enumerate(entries, 1):
    print(f"==================================================")
    print(f"[{idx}] {e.get('title')} ({e.get('year')})")
    print(f"Autores: {e.get('author')}")
    print(f"Veículo: {e.get('booktitle') or e.get('journal')}")
    print(f"DOI: {e.get('doi')}")
    print(f"RESUMO COMPLETO:\n{e.get('abstract')}\n")
