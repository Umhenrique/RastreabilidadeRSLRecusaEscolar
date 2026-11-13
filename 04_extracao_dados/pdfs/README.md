# Repositorio de Textos Integrais (PDFs da Fase 2)

Deposite neste diretorio os arquivos PDF integrais dos 101 estudos incluidos para leitura completa.

## Padrao de Nomenclatura
- Utilize o identificador unico do estudo (`Study_ID`) no inicio do nome do arquivo:
  - Exemplo 1: `S0001.pdf`
  - Exemplo 2: `S0001 - Clinical practitioners experiences.pdf`
- O script `scripts/consolidar_extracao_fase2.py` detecta automaticamente qualquer arquivo `.pdf` cujo nome comece com `SXXXX` (ex.: `S0001*.pdf`) e marca a coluna `PDF_Disponivel` como `Sim` na planilha `04_extracao_dados/matriz_extracao.xlsx`.

