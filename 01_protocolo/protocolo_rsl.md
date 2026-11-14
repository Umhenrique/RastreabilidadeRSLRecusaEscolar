# Protocolo da Revisão Sistemática da Literatura (RSL)

> **Tema da Pesquisa:** Ferramentas, Instrumentos e Abordagens Computacionais (IA/ML) para Diagnóstico, Rastreio e Predição de Recusa Escolar e Absenteísmo Crônico  
> **Status:** Em Planejamento / Condução  
> **Data de Atualização:** 2026-09-24  

---

## 1. Objetivos da Revisão

### 1.1 Objetivo Geral
Mapear, analisar e sintetizar a literatura científica sobre ferramentas, instrumentos e abordagens computacionais (incluindo inteligência artificial e aprendizado de máquina) utilizadas para o rastreio, avaliação, diagnóstico ou predição de casos de recusa escolar e absenteísmo crônico.

### 1.2 Objetivos Específicos
1. **Identificar** quais instrumentos psicométricos, escalas e ferramentas tradicionais são mais empregados no diagnóstico clínico ou educacional da recusa escolar.
2. **Investigar** o uso de modelos de Inteligência Artificial, aprendizado de máquina (*Machine Learning*) e sistemas de alerta precoce (*Early Warning Systems*) aplicados a essa temática.
3. **Analisar** as principais métricas de desempenho, validação e limitações das ferramentas descritas na literatura.
4. **Identificar** lacunas de pesquisa atuais para orientar futuros desenvolvimentos tecnológicos na área.

---

## 2. Estrutura do Estudo (Critério PICOC)

| Elemento | Definição no Estudo |
|---|---|
| **Population** | Ensino Básico |
| **Intervention** | IA (Ferramentas de diagnóstico ou diagnóstico) |
| **Outcomes** | Recusa escolar OR (evasão escolar AND socio-emotional factor) |

---

## 3. Questões de Pesquisa (Research Questions - RQs)

* **RQ1:** Quais são as ferramentas, escalas ou instrumentos psicométricos utilizados para diagnosticar ou rastrear a recusa escolar e o absenteísmo crônico?
  * *Foco:* Instrumentos clínicos, educacionais e escalas psicométricas (ex: SRAS-R, DASS-21, etc.).
* **RQ2:** De que forma técnicas de Inteligência Artificial, Machine Learning e análise de dados têm sido aplicadas na predição ou detecção precoce da recusa escolar?
  * *Foco:* Algoritmos empregados, pipelines de dados, sistemas de alerta precoce (*Early Warning Systems*) e arquiteturas de modelos.
* **RQ3:** Quais variáveis socioemocionais, comportamentais ou contextuais são mais frequentemente consideradas por essas ferramentas preditivas e diagnósticas?
  * *Foco:* Features dos modelos (aspectos psicológicos, ansiedade, depressão, dinâmicas familiares, clima escolar, assiduidade, dados sociodemográficos).
* **RQ4:** Quais são as principais limitações, desafios metodológicos e métricas de avaliação relatados nos estudos ao implementar essas ferramentas?
  * *Foco:* Métricas de validação, desbalanceamento de dados, interpretabilidade/explicabilidade (XAI), viés amostral e barreiras práticas de implantação.

---

## 4. Estratégia de Busca

### 4.1 Fontes de Pesquisa (Bases de Dados)
- [x] Scopus
- [x] IEEE Xplore
- [x] ACM Digital Library
- [x] ScienceDirect (Elsevier)
- [x] Springer Link (Springer Nature)
- [x] Web of Science
- [ ] PubMed / Periódicos CAPES

### 4.2 Critérios de Idioma e Formato
- **Idiomas:** Inglês, Português e Espanhol.
- **Tipo de publicação:** Artigos de periódicos e anais de conferências científicas revisados por pares.

### 4.3 String de Busca Canônica Oficial e Aplicação na IEEE
A estratégia de busca formal combina os três blocos conceituais via `AND` (Fenômeno AND Fatores Socioemocionais AND IA/Predição), conforme detalhado em [strings_de_busca.md](file:///c:/Users/mathe/Documents/mestrado/RSL%20peojeto/01_protocolo/strings_de_busca.md).

Na **IEEE Xplore**, a aplicação da string completa de 3 blocos resultou em **14 artigos brutos recuperados**, representando um conjunto altamente focado na interseção direta entre absenteísmo/recusa escolar, saúde mental/fatores socioemocionais e inteligência artificial.

---

## 5. Critérios de Seleção (Critérios de Elegibilidade)

### 5.1 Critérios de Inclusão (Inclusion Criteria - IC)
* **IC1:** Artigos originais empiricos revisados por pares (*peer-reviewed*), publicados em periodicos ou anais de conferencias cientificas, que apresentem aplicacao concreta de modelos de Inteligencia Artificial, Machine Learning ou analise preditiva voltados a recusa escolar ou ao absenteismo escolar associado a fatores sociais e emocionais (escalas psicometricas isoladas ou revisoes sem modelo preditivo nao entram como estudos primarios da RSL, podendo compor o referencial teorico).
* **IC2:** Estudos que abordem explicitamente o desenvolvimento, validação, aplicação ou revisão de ferramentas de diagnóstico, triagem (*screening*), avaliação ou predição voltadas à recusa escolar (*school refusal*), absenteísmo crônico ou evasão associada.
* **IC3:** Estudos publicados nos idiomas inglês, português ou espanhol (ou traduzidos por ferramentas oficiais).
* **IC4:** Trabalhos que apresentem dados empíricos, arquiteturas de sistemas ou revisões sistemáticas/integrativas relevantes ao escopo.

### 5.2 Critérios de Exclusão (Exclusion Criteria - EC)
* **EC1:** Literatura cinzenta não validada (teses, dissertações sem artigos derivados, relatórios técnicos informais, *preprints* sem revisão, editoriais, cartas ou resumos estendidos sem dados completos).
* **EC2:** Estudos focados exclusivamente na evasão escolar (*dropout*) por motivos estritamente socioeconômicos ou estruturais (ex: pobreza severa, falta de infraestrutura escolar) sem relação com o comportamento de recusa escolar ou fatores socioemocionais/psicológicos.
* **EC3:** Trabalhos duplicados nas bases de dados (mantém-se apenas a versão mais completa/recente).
* **EC4:** Artigos cujo texto completo não esteja acessível mesmo após tentativa de contato com os autores ou busca institucional.

---

## 6. Critérios de Avaliação de Qualidade (Quality Assessment - QA)

Escala de pontuação por critério: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Não atende. (Pontuação máxima: 10 pontos).

* **QA1 (Clareza do Objetivo):** O objetivo do estudo ou o desenvolvimento da ferramenta de diagnóstico/predição está claramente definido?
* **QA2 (Rigor Metodológico):** A metodologia de coleta de dados, a seleção da amostra (estudantes/participantes) ou a arquitetura do modelo computacional/psicométrico está descrita de forma replicável?
* **QA3 (Validação e Desempenho):** O estudo apresenta métricas claras de validação da ferramenta (ex: acurácia, F1-score, alfa de Cronbach, validade convergente, etc.)?
* **QA4 (Consideração de Fatores Socioemocionais):** Há uma análise aprofundada dos fatores psicológicos ou contextuais associados à recusa escolar?
* **QA5 (Limitações e Viés):** Os autores discutem claramente as limitações metodológicas, restrições da amostra ou possíveis vieses da ferramenta proposta?

