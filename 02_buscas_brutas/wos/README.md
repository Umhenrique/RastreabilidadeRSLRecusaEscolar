# Buscas Brutas - Web of Science (Clarivate)

Nesta pasta devem ser armazenados os arquivos brutos exportados diretamente da **Web of Science Core Collection** (Clarivate Analytics).

---

## Strings de Busca Prontas para Uso

### Opção 1: Para a Busca Padrão (Campo "Topic / Tópico") — RECOMENDADA
> No campo de busca do Web of Science, selecione **Topic** no menu suspenso e cole o texto abaixo (sem o prefixo `TS=`, evitando erros de sintaxe na interface):

```text
( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
AND
( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor*" OR "emotional difficulties" OR "psychosocial factor*" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor*" )
AND
( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model*" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model*" OR LLM OR "neural network*" OR "classification model*" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
```

---

### Opção 2: Para a Busca Avançada (Advanced Search Query)
> Caso utilize o editor de linha de comando da Busca Avançada do WoS:

```text
TS=(
  ( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
  AND
  ( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor*" OR "emotional difficulties" OR "psychosocial factor*" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor*" )
  AND
  ( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model*" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model*" OR LLM OR "neural network*" OR "classification model*" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
)
```

---

## Filtros Recomendados no Web of Science
1. **Base de dados:** Selecione **Web of Science Core Collection** (Coleção Principal).
2. **Document Types (Tipos de Documento):** No painel de filtros lateral, marque:
   - **Articles**
   - **Proceeding Papers** (Artigos de Conferências)
3. **Open Access:** Deixe todos os modelos marcados (não restrinja apenas a Open Access).

---

## Orientações de Exportação
1. Na tela de resultados, clique no botão **Export** no topo da lista.
2. Escolha **BibTeX** (ou *Tab delimited file* / *Plain text file*).
3. Na janela modal:
   - **Record options:** Escolha *Records from 1 to [total]* (máximo de 1.000 por lote no WoS).
   - **Record content:** Selecione **Full Record** (essencial para vir com Título, Autores, Resumo e Palavras-chave).
4. Salve o arquivo nesta pasta como `wos_export.bib` (ou `.txt` / `.tsv`).
5. Registre o quantitativo e data em [log_execucao_buscas.md](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/log_execucao_buscas.md).
