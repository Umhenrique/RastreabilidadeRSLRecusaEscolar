import sys
sys.path.append('scripts')
from analisar_14_ieee import parse_ieee_bib

entries = parse_ieee_bib('02_buscas_brutas/IEE/IEEE Xplore Citation BibTeX Download 2026.9.24.19.12.30.bib')

for idx in range(4):
    e = entries[idx]
    print(f"[{idx+1}] {e.get('title')} ({e.get('year')})")
    print("ABSTRACT:", e.get('abstract'))
    print("-" * 60)
