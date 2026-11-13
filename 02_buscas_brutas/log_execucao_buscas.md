# Log de Execução das Buscas

Este registro é crucial para a reprodutibilidade da RSL. Cada vez que uma busca for executada em uma base de dados, anote os detalhes exatos abaixo.

---

## Registro Geral de Buscas

| ID Busca | Data | Base de Dados | Filtros Aplicados (Anos, Tipos, etc.) | Total de Artigos Retornados | Arquivo Bruto Exportado | Responsável / Notas |
|---|---|---|---|---|---|---|
| B01 | 2026-09-24 | ACM Digital Library | String Canônica nos campos Title/Abstract | 198 | `02_buscas_brutas/ACM/*.bib` | 4 arquivos BibTeX consolidados |
| B02 | 2026-09-24 | IEEE Xplore | String Oficial dos 3 blocos (Title/Abstract) | 14 | `02_buscas_brutas/IEE/*.bib` | 1 arquivo BibTeX com 14 artigos |
| B03 | 2026-10-04 | ScienceDirect | String Oficial Enxuta (Title/Abstract/Keywords) | 62 | `02_buscas_brutas/sciencedirect/ScienceDirect_citations_1791116111454.bib` | Executada em etapa única (8 operadores) |
| B04 | 2026-10-04 | Scopus | String dos 3 blocos (Title/Abstract/Keywords via UI) | 195 | `02_buscas_brutas/scopus/export_0f9434dc-7609-4f1c-a5ef-61b619094e79_2026-10-04T121840.201981761.bib` | Exportados com citações e resumos |
| B05 | 2026-10-04 | Web of Science | Topic (Title/Abstract/Keywords via UI) | 83 | `02_buscas_brutas/wos/savedrecs (*).bib` | 2 lotes BibTeX consolidados (50 + 33) |
| B06 | 2026-10-04 | Springer Link | Content Type: Article & Conference Paper | 1000 | `02_buscas_brutas/springer_link/SearchResults (3).csv` | 921 Articles, 79 Conference papers |

---

## Detalhamento das Strings Exatas Executadas

### Busca B01 - ACM Digital Library
- **Data:** 2026-09-24
- **Campos:** Title/Abstract
- **Total:** 198 artigos

### Busca B02 - IEEE Xplore
- **Data:** 2026-09-24
- **Campos:** Metadata / Title, Abstract, Keywords
- **Total:** 14 artigos

### Busca B03 - ScienceDirect
- **Data:** 2026-10-04
- **Campos:** Title, abstract or author-specified keywords
- **String exata:**
  ```text
  ("school refusal" OR "chronic absenteeism" OR "school absenteeism") AND ("socio-emotional" OR "social-emotional" OR "mental health") AND ("machine learning" OR "artificial intelligence" OR "early warning")
  ```
- **Arquivo bruto:** [`02_buscas_brutas/sciencedirect/ScienceDirect_citations_1791116111454.bib`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/sciencedirect/ScienceDirect_citations_1791116111454.bib)
- **Total retornado:** **62 artigos**

### Busca B04 - Scopus
- **Data:** 2026-10-04
- **Campos:** Title, Abstract, Keywords (via campos da busca do Scopus)
- **String exata:**
  ```text
  ( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
  AND
  ( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor*" OR "emotional difficulties" OR "psychosocial factor*" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor*" )
  AND
  ( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model*" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model*" OR LLM OR "neural network*" OR "classification model*" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
  ```
- **Arquivo bruto:** [`02_buscas_brutas/scopus/export_0f9434dc-7609-4f1c-a5ef-61b619094e79_2026-10-04T121840.201981761.bib`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/scopus/export_0f9434dc-7609-4f1c-a5ef-61b619094e79_2026-10-04T121840.201981761.bib)
- **Total retornado:** **195 artigos**

### Busca B05 - Web of Science (Clarivate)
- **Data:** 2026-10-04
- **Campos:** Topic (Título, Resumo, Palavras-chave via interface)
- **Filtros aplicados:** Coleção Principal (Core Collection), Document Types: Articles e Proceeding Papers
- **String exata:**
  ```text
  ( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
  AND
  ( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor*" OR "emotional difficulties" OR "psychosocial factor*" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor*" )
  AND
  ( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model*" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model*" OR LLM OR "neural network*" OR "classification model*" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
  ```
- **Arquivos brutos:** [`02_buscas_brutas/wos/savedrecs (1).bib`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/wos/savedrecs%20%281%29.bib) e [`02_buscas_brutas/wos/savedrecs (2).bib`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/wos/savedrecs%20%282%29.bib)
- **Total retornado:** **83 artigos** (50 no lote 1 + 33 no lote 2, sem sobreposição)

### Busca B06 - Springer Link
- **Data:** 2026-10-04
- **Filtros aplicados:** Content Type: **Article** e **Conference Paper**
- **String exata:**
  ```text
  ( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
  AND
  ( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor" OR "emotional factors" OR "emotional difficulties" OR "psychosocial factor" OR "psychosocial factors" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor" OR "affective factors" )
  AND
  ( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model" OR "predictive models" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model" OR "large language models" OR LLM OR "neural network" OR "neural networks" OR "classification model" OR "classification models" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
  ```
- **Arquivo bruto:** [`02_buscas_brutas/springer_link/SearchResults (3).csv`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/springer_link/SearchResults%20%283%29.csv)
- **Total retornado no arquivo:** **1.000 registros** (921 artigos de periódicos e 79 artigos de conferência)
