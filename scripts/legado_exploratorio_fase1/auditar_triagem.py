import pandas as pd

df = pd.read_csv('03_selecao_triagem/02_triagem_resumo/triagem_acm.csv')

print('--- ESTUDO INCLUIDO ---')
inc = df[df['Decision'] == 'Incluído']
for _, r in inc.iterrows():
    print(r['Study_ID'], '|', r['Title'], '|', r['Year'])
    print('Abstract:', str(r['Abstract'])[:300])
    print()

print('--- AUDITORIA: ESTUDOS COM TERMOS DE FALTAS/EVASAO/ABSENTEISMO EXCLUIDOS ---')
text = (df['Title'].fillna('') + ' ' + df['Abstract'].fillna('')).str.lower()
mask = text.str.contains('dropout|absenteeism|attendance|refusal|evasão|recusa')
cand = df[mask & (df['Decision'] == 'Excluído')]

print(f"Total de estudos com palavras-chave de interesse que foram excluídos: {len(cand)}")
for idx, r in cand.iterrows():
    print(f"[{r['Study_ID']}] ({r['Year']}) {r['Title']}")
    print(f"   Critério: {r['Criterion']} | Motivo: {r['Reason']}")
    print(f"   Trecho do resumo: {str(r['Abstract'])[:200]}...")
    print('-'*60)
