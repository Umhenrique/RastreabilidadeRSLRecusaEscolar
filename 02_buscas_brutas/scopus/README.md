# Buscas Brutas - Scopus (Elsevier)

Nesta pasta devem ser armazenados os arquivos brutos exportados diretamente da base de dados **Scopus**.

---

## String de Busca Oficial para o Scopus

A string abaixo já se encontra estruturada para a sintaxe nativa do Scopus, aplicando a busca aos campos de Título, Resumo e Palavras-chave (`TITLE-ABS-KEY`):

```text
TITLE-ABS-KEY (
  ( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
  AND
  ( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor*" OR "emotional difficulties" OR "psychosocial factor*" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor*" )
  AND
  ( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model*" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model*" OR LLM OR "neural network*" OR "classification model*" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
)
```

---

## Orientações de Exportação
1. Acesse o **Scopus Search**: [https://www.scopus.com/search/form.uri](https://www.scopus.com/search/form.uri) (ou use a Busca Avançada).
2. Cole a consulta acima no campo de busca ou no editor avançado.
3. Na página de resultados:
   - Marque a caixa de seleção **All** (Selecionar todos). Se houver mais de 200 resultados, escolha a opção de exportar todos os resultados até o limite da base (normalmente até 2.000 registros por exportação).
   - Clique em **Export**.
   - Escolha o formato **BibTeX** (`.bib`) ou **CSV** (`.csv`).
   - Garanta que os seguintes campos estejam marcados:
     - *Citation information* (Autor, título, ano, fonte, volume, páginas, DOI)
     - *Bibliographical information* (Afiliações, editora, etc.)
     - *Abstract & keywords* (Resumo, Author keywords, Index keywords)
4. Salve o arquivo exportado nesta pasta como `scopus_export.bib` (ou `.csv`).
5. Registre a data, filtros e o quantitativo retornado em [log_execucao_buscas.md](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/log_execucao_buscas.md).
