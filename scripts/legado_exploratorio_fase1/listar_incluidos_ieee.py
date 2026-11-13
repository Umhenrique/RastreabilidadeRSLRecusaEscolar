import sys
import pandas as pd
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv('03_selecao_triagem/02_triagem_resumo/triagem_ieee.csv')
inc = df[df['Decision'] == 'Incluído']
print(f"Total de estudos incluídos inicialmente na IEEE: {len(inc)}\n")

for idx, r in inc.iterrows():
    print(f"[{r['Study_ID']}] ({r['Year']}) {r['Title']}")
    print(f"   Veículo: {r['Venue']}")
    print(f"   Outcome: {r['Outcome_Scope']}")
    print(f"   Abstract: {str(r['Abstract'])[:250]}...")
    print("-" * 75)
