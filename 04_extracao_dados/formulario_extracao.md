# Formulário de Extração de Dados (Data Extraction Form)

Este formulário padroniza a coleta de dados de cada artigo aceito para a fase final de síntese, mapeando diretamente as Questões de Pesquisa (**RQ1** a **RQ4**) e os Critérios de Qualidade (**QA1** a **QA5**).

---

## 1. Identificação e Metadados do Estudo
- **ID do Estudo:** (Ex: `S01`, `S02`...)
- **Título do Artigo:**
- **Autores:**
- **Ano de Publicação:**
- **Tipo de Publicação:** (Periódico / Anais de Conferência)
- **Nome do Veículo (Journal/Conference):**
- **DOI / Link:**
- **Base de Dados de Origem:** (Scopus, IEEE Xplore, ACM DL, Web of Science, etc.)
- **País/Região do Estudo:**

---

## 2. Caracterização da População e Contexto (PICOC)
- **Nível Educacional:** (Ensino Fundamental I / II, Ensino Médio, Ensino Superior, Clínico)
- **Faixa Etária / Amostra:** (Idade dos participantes, tamanho da amostra $N$)
- **Público-alvo Avaliado:** (Estudantes com histórico de recusa, absenteísmo crônico, população geral)
- **Fonte dos Dados / Dataset:** (Dados administrativos escolares, prontuários clínicos, questionários próprios, datasets abertos)

---

## 3. Extração Orientada às Questões de Pesquisa (RQs)

### RQ1: Ferramentas, Escalas ou Instrumentos Psicométricos
- **Nome do Instrumento/Escala:** (Ex: SRAS-R - School Refusal Assessment Scale-Revised, etc.)
- **Natureza da Ferramenta:** (Instrumento psicométrico tradicional / Escala clínica / Ferramenta digitalizada / Questionário de triagem)
- **Forma de Aplicação:** (Autorrelato do aluno, relato dos pais, relato dos professores, entrevista clínica)
- **Finalidade:** (Diagnóstico diferencial, triagem inicial, avaliação contínua)

### RQ2: Abordagens Computacionais e de Inteligência Artificial
- **Tipo de Abordagem:** (Machine Learning Supervisionado, Não Supervisionado, Deep Learning, Early Warning System - EWS, Análise Estatística Avançada, XAI)
- **Algoritmos Empregados:** (Ex: Random Forest, XGBoost, SVM, Redes Neurais, Regressão Logística, etc.)
- **Tarefa do Modelo:** (Classificação binária [risco sim/não], regressão [probabilidade de infrequência], clustering [perfis de comportamento])
- **Estágio de Detecção:** (Alerta precoce / detecção preventiva vs. diagnóstico a posteriori)

### RQ3: Variáveis e Features Consideradas (Socioemocionais, Comportamentais e Contextuais)
- **Variáveis Psicológicas/Socioemocionais:** (Ansiedade de separação, ansiedade social, depressão, estresse, regulação emocional, etc.)
- **Variáveis Comportamentais / Histórico:** (Padrão de faltas/atrasos, histórico de notas, engajamento escolar, conflitos, bullying)
- **Variáveis Familiares / Sociodemográficas:** (Estrutura familiar, dinâmica parental, renda, histórico médico)
- **Variáveis Institucionais / Contextuais:** (Clima escolar, relação professor-aluno, localização da escola)
- **Features Mais Relevantes Identificadas pelos Autores:** (Feature importance / SHAP / coeficientes principais)

### RQ4: Métricas de Avaliação, Desempenho, Desafios e Limitações
- **Métricas de Validação:**
  - *Psicométricas:* (Alfa de Cronbach, Ômega de McDonald, Validade convergente/discriminante)
  - *Computacionais/ML:* (Acurácia, Sensibilidade/Recall, Precisão, F1-Score, AUC-ROC, MCC)
- **Estratégia de Validação:** (K-Fold Cross-validation, split treino/teste, validação externa)
- **Desafios Metodológicos Relatados:** (Desbalanceamento de classes, dados faltantes/ruidosos, tamanho restrito da amostra)
- **Aspectos Éticos e de Transparência:** (Discussão sobre privacidade dos dados dos alunos, interpretabilidade do modelo - XAI, mitigação de viés)
- **Limitações Gerais Declaradas pelos Autores:**
- **Lacunas e Direções Futuras Apontadas:**

---

## 4. Avaliação de Qualidade Metodológica (QA)
*Pontuação: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Não atende.*

| Critério | Avaliação | Nota (0, 1 ou 2) | Justificativa / Trecho do Artigo |
|---|---|:---:|---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta está claramente definido? | | |
| **QA2 (Rigor Metodológico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicável? | | |
| **QA3 (Validação e Desempenho)** | Apresenta métricas claras de validação (Acurácia, F1, Cronbach, etc.)? | | |
| **QA4 (Fatores Socioemocionais)** | Há análise aprofundada dos fatores psicológicos ou contextuais associados à recusa escolar? | | |
| **QA5 (Limitações e Viés)** | Os autores discutem limitações metodológicas, restrições da amostra ou vieses? | | |
| **TOTAL** | *(Soma de 0 a 10)* | **/ 10** | |
