# Buscas Brutas - ScienceDirect (Elsevier)

Nesta pasta devem ser armazenados os arquivos brutos exportados diretamente da base **ScienceDirect** (Elsevier).

---

## [Pendente] Restrição Técnica Importante da Base
1. O ScienceDirect impõe um limite estrito de **no máximo 8 operadores booleanos (`AND`, `OR`, `NOT`) no total da consulta**.
2. **Atenção ao Campo:** A busca deve ser feita **obrigatoriamente** no campo **"Title, abstract or author-specified keywords"** da Busca Avançada. Nunca busque no texto completo (*Full text* / *Find articles with these terms*), pois isso atrairia milhares de artigos dispersos sobre evasão universitária, psiquiatria geral ou computação teórica.

---

## String Única Enxuta Oficial (Exatamente 8 Operadores)

Esta formulação concentra-se estritamente no núcleo do problema, unindo o fenômeno escolar, o construto socioemocional e as abordagens de IA/predição em **uma única execução**:

```text
("school refusal" OR "chronic absenteeism" OR "school absenteeism") AND ("socio-emotional" OR "social-emotional" OR "mental health") AND ("machine learning" OR "artificial intelligence" OR "early warning")
```

* **Contagem de operadores:** 2 `OR` + 1 `AND` + 2 `OR` + 1 `AND` + 2 `OR` = **8 operadores booleanos**.
* **Benefício:** Elimina o ruído de evasão de ensino superior/MOOCs e dispensa o trabalho de executar múltiplas sub-buscas.

---

## Alternativa Hiper-Enxuta (Núcleo Duro - 6 Operadores)

```text
("school refusal" OR "chronic absenteeism" OR "school absenteeism") AND ("socio-emotional" OR "mental health") AND ("machine learning" OR "artificial intelligence")
```

---

## Orientações de Exportação
1. Acesse o **ScienceDirect Advanced Search**: [https://www.sciencedirect.com/search/advanced](https://www.sciencedirect.com/search/advanced)
2. Cole a string oficial no campo **Title, abstract or author-specified keywords**.
3. Selecione os artigos retornados e clique em **Export** -> **Export citation to BibTeX** (ou RIS).
4. Salve o arquivo nesta pasta como `sciencedirect_export.bib` (ou `.ris`).
5. Registre a data e o total de artigos no arquivo [log_execucao_buscas.md](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/log_execucao_buscas.md).
