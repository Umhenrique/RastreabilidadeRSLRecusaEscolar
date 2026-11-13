import sys
import pandas as pd
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv('03_selecao_triagem/02_triagem_resumo/triagem_ieee.csv')

for sid in ['IEEE_001', 'IEEE_008', 'IEEE_032', 'IEEE_107', 'IEEE_141', 'IEEE_206']:
    r = df[df['Study_ID'] == sid].iloc[0]
    print(f"=== {r['Study_ID']}: {r['Title']} ({r['Year']}) ===")
    print("Venue:", r['Venue'])
    print("Abstract:", r['Abstract'])
    print("-" * 80)
