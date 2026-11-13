# Strings de Busca Oficiais e Adaptações por Base de Dados

Este documento registra a **estratégia de busca oficial adotada** na condução desta Revisão Sistemática da Literatura (RSL), além do detalhamento e adaptação específica para motores com restrições de sintaxe.

> **Nota Metodológica de Transparência:**  
> - **ACM Digital Library:** A consulta foi executada de forma direta nos campos de título e resumo integrados (*Title/Abstract*), sem a exigência de partição prévia em blocos booleanos rígidos, gerando o universo bruto de **198 registros**.
> - **IEEE Xplore:** A consulta foi estruturada na formulação formal em **três blocos conceituais combinados via operadores `AND`** (Fenômeno AND Socioemocional AND IA/Predição), gerando o universo bruto de **14 registros** de alta aderência temática.

---

## 1. String Canônica com Fatores Socioemocionais Explícitos

Esta formulação alinha-se diretamente ao desfecho do PICOC: **Recusa Escolar OR (Evasão Escolar AND Fatores Socioemocionais)** combinada com tecnologias de **IA/Predição**:

### Bloco 1: O Fenômeno (Recusa Escolar e Absenteísmo)
```text
(
    "school refusal"
    OR "school avoidance"
    OR "school absenteeism"
    OR "school absence"
    OR "school non-attendance"
    OR "school nonattendance"
    OR "school dropout"
    OR "school disengagement"
    OR "persistent absenteeism"
    OR "chronic absenteeism"
    OR truancy
)
```

### Bloco 2: Fatores Socioemocionais, Psicológicos e de Saúde Mental
```text
(
    "socio-emotional"
    OR socioemotional
    OR "social-emotional"
    OR "social emotional"
    OR "emotional factor*"
    OR "emotional difficulties"
    OR "psychosocial factor*"
    OR "mental health"
    OR anxiety
    OR depression
    OR bullying
    OR "peer victimization"
    OR loneliness
    OR stress
    OR "psychological distress"
    OR wellbeing
    OR "well-being"
    OR "affective factor*"
)
```

### Bloco 3: Tecnologias de IA, Modelos Preditivos e Detecção
```text
(
    "artificial intelligence"
    OR "machine learning"
    OR "deep learning"
    OR "predictive model*"
    OR "predictive analytics"
    OR "data mining"
    OR "natural language processing"
    OR NLP
    OR "large language model*"
    OR LLM
    OR "neural network*"
    OR "classification model*"
    OR "risk prediction"
    OR "risk assessment"
    OR "early detection"
    OR "early identification"
    OR "early warning systems"
    OR "learning analytics"
)
```

---

## 2. String Oficial Adotada para a IEEE Xplore (Resultado: 14 Artigos)

Esta é a formulação exata executada na **IEEE Xplore**, combinando os 3 blocos conceituais completos via operadores `AND`:

```text
(
  ( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
  AND
  ( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor*" OR "emotional difficulties" OR "psychosocial factor*" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor*" )
  AND
  ( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model*" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model*" OR LLM OR "neural network*" OR "classification model*" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
)
```
* **Base:** IEEE Xplore
* **Campos:** Metadata / Title, Abstract, Keywords
* **Total bruto retornado:** **14 artigos**

---

## 3. Adaptações para Outras Bases (Sem limite rígido de 10 argumentos)

### 3.1 Scopus
```text
TITLE-ABS-KEY (
  ( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
  AND
  ( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor*" OR "emotional difficulties" OR "psychosocial factor*" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor*" )
  AND
  ( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model*" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model*" OR LLM OR "neural network*" OR "classification model*" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
)
```

### 3.2 Web of Science
```text
TS=(
  ( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
  AND
  ( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor*" OR "emotional difficulties" OR "psychosocial factor*" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor*" )
  AND
  ( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model*" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model*" OR LLM OR "neural network*" OR "classification model*" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
)
```

### 3.3 Springer Link
*(Sintaxe adaptada sem asterisco dentro de aspas duplas, com termos singulares e plurais explicitados)*
```text
( "school refusal" OR "school avoidance" OR "school absenteeism" OR "school absence" OR "school non-attendance" OR "school nonattendance" OR "school dropout" OR "school disengagement" OR "persistent absenteeism" OR "chronic absenteeism" OR truancy )
AND
( "socio-emotional" OR socioemotional OR "social-emotional" OR "social emotional" OR "emotional factor" OR "emotional factors" OR "emotional difficulties" OR "psychosocial factor" OR "psychosocial factors" OR "mental health" OR anxiety OR depression OR bullying OR "peer victimization" OR loneliness OR stress OR "psychological distress" OR wellbeing OR "well-being" OR "affective factor" OR "affective factors" )
AND
( "artificial intelligence" OR "machine learning" OR "deep learning" OR "predictive model" OR "predictive models" OR "predictive analytics" OR "data mining" OR "natural language processing" OR NLP OR "large language model" OR "large language models" OR LLM OR "neural network" OR "neural networks" OR "classification model" OR "classification models" OR "risk prediction" OR "risk assessment" OR "early detection" OR "early identification" OR "early warning systems" OR "learning analytics" )
```

---

## 4. Adaptação Específica para ScienceDirect (Elsevier)

> [Pendente] **Restrição Técnica do ScienceDirect:**  
> O ScienceDirect impõe um limite estrito de **no máximo 8 operadores booleanos (`AND`, `OR`, `NOT`) no total da consulta**. Além disso, a busca **NUNCA deve ser feita no texto integral (*Full text*)**, pois isso retorna milhares de falsos positivos (artigos de evasão universitária, psiquiatria adulta ou computação genérica).

Para garantir uma **busca única, executável em uma só etapa e com alta precisão temática** (sem ruído de milhares de artigos irrelevantes), a string foi enxugada focando estritamente no núcleo do PICOC:
1. **Fenômeno específico:** Recusa escolar e absenteísmo crônico (eliminando termos genéricos como "dropout" solto, que atraem evasão universitária/MOOCs).
2. **Socioemocional:** O construto central socioemocional e saúde mental (eliminando termos clínicos genéricos isolados como estresse ou depressão geral).
3. **Tecnologia:** Aprendizado de máquina, inteligência artificial e sistemas de alerta precoce.

---

### 4.1 String Única Enxuta Oficial para ScienceDirect (Exatamente 8 Operadores)

> **Onde colar:** No campo **Title, abstract or author-specified keywords** da [Busca Avançada do ScienceDirect](https://www.sciencedirect.com/search/advanced).

```text
("school refusal" OR "chronic absenteeism" OR "school absenteeism") AND ("socio-emotional" OR "social-emotional" OR "mental health") AND ("machine learning" OR "artificial intelligence" OR "early warning")
```

* **Total de operadores booleanos:** Exatamente **8** (2 `OR` + 1 `AND` + 2 `OR` + 1 `AND` + 2 `OR`).
* **Vantagem:** Execução em **etapa única**, resultado limpo, de alta precisão e sem necessidade de combinar sub-buscas.
* **Arquivo de exportação:** `sciencedirect_export.bib` em [`02_buscas_brutas/sciencedirect/`](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/02_buscas_brutas/sciencedirect).

---

### 4.2 Alternativa Hiper-Enxuta (Núcleo Duro - 6 Operadores)
Caso deseje uma filtragem ainda mais restrita focada exclusivamente nos métodos de aprendizado computacional:

```text
("school refusal" OR "chronic absenteeism" OR "school absenteeism") AND ("socio-emotional" OR "mental health") AND ("machine learning" OR "artificial intelligence")
```
* **Total de operadores booleanos:** **6** (2 `OR` + 1 `AND` + 1 `OR` + 1 `AND` + 1 `OR`).


