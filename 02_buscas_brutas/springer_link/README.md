# Buscas Brutas - Springer Link (Springer Nature)

Nesta pasta devem ser armazenados os arquivos brutos exportados diretamente da plataforma **Springer Link** (Springer Nature).

---

## String de Busca Adaptada para o Springer Link

O mecanismo de busca do Springer Link interpreta operadores booleanos em maiúsculas (`AND`, `OR`, `NOT`) e expressões exatas entre aspas duplas (`"..."`). Como o Springer não aceita caracteres curinga (`*`) dentro de expressões entre aspas, as variações de singular/plural foram explicitadas:

```text
( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
AND
( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor" OR "emotional factors" OR "emotional difficulties" OR "psychosocial factor" OR "psychosocial factors" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor" OR "affective factors" )
AND
( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model" OR "predictive models" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model" OR "large language models" OR LLM OR "neural network" OR "neural networks" OR "classification model" OR "classification models" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
```

---

## Filtros e Recomendações Metodológicas no Springer Link
1. **Acesso:** [https://link.springer.com](https://link.springer.com)
2. **Preview-Only Content:**
   - [Pendente] **Importante para RSL:** No painel lateral esquerdo, verifique a opção **"Include Preview-Only content"**. Para evitar viés de publicação/assinatura na identificação do PRISMA, recomenda-se buscar todos os registros e obter textos completos posteriormente via convênio institucional (CAPES/CAFe).
3. **Content Type:**
   - Filtrar por **Article** e **Conference Paper** (conforme critérios IC1 e EC1 da RSL).
4. **Discipline / Subdiscipline (Opcional):**
   - Caso o retorno seja muito disperso, pode-se refinar pelas disciplinas *Computer Science*, *Education* e *Psychology*.

---

## Orientações de Exportação
1. Após aplicar a busca e os filtros de tipo de conteúdo, clique no botão **"Download search results"** (exportação padrão em formato `.csv`).
2. Salve o arquivo gerado nesta pasta como `springer_results.csv` (ou `.bib` se exportado via plugin/gerenciador).
3. Atualize o quantitativo e a data no arquivo [log_execucao_buscas.md](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/log_execucao_buscas.md).
