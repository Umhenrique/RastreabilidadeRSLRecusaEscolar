# Sintese da Extracao de Texto Completo — Fase 2 (26 PDFs Analisados)

**Projeto:** Revisao Sistematica da Literatura (RSL) sobre Recusa Escolar e Inteligencia Artificial  
**Autor:** Matheus Henrique Assuncao de Medeiros (PGCC UERN / UFERSA)  
**Data:** 13 de Novembro de 2026  

---

## 1. Estado Atual do Funil na Fase 2
- **Elegiveis iniciais (pos-Fase 1):** `101` estudos
- **Extraidos integralmente a partir dos PDFs:** `24` estudos (`S0012`, `S0104` + `22` novos estudos analisados hoje)
- **Excluidos na Fase 2:** `18` estudos (`16` na auditoria pre-extracao `DEC-007` + `2` apos leitura integral dos PDFs: `S0133` e `S0153`)
- **Pendentes de leitura completa:** `59` estudos

---

## 2. Eixo Computacional: IA, Machine Learning, EWS e XAI (12 estudos)

| ID | Estudo (Autor, Ano) | Abordagem / Algoritmos | Amostra / Contexto | Principais Resultados e Metricas | QA |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **S0501** | Barros et al. (2026) | Random Forest (selecionado), CatBoost, XGBoost, LightGBM, Regressao Logistica + XAI (SHAP e contrafactuais *what-if*) | 22.476 escolas de Ensino Medio (Brasil, ICG 1-6) | Acc = 0,67-0,85; F1 = 0,58-0,81; Recall = 0,43-0,89. Melhor desempenho em escolas ICG 1; evidencia lacuna de variaveis de saude mental em dados administrativos brasileiros. | 9/10 |
| **S0290** | Abas et al. (2026) | Ensemble Learning (XGBoost, RF) + SMOTE + LASSO + XAI (LIME) + questionario 34 itens | 1.158 alunos (5 escolas, Libia) | XGBoost: Acc = 0,941, F1 = 0,941 (CV F1 = 0,939), LogLoss = 0,161; RF: Acc/F1 = 0,939. | 9/10 |
| **S0315** | Perdomo et al. (2025) | EWS estadual (DEWS: RF/GBDT) + CatBoost + Inferencia Causal (RDD) | ~215.000 alunos (Wisconsin, EUA, 2013-2021) | DEWS AUC = 0,80; CatBoost AUC = 0,863. Critica importante: alertas sociais sem protocolo de acao tem efeito causal incerto. | 9/10 |
| **S0322** | Xu et al. (2021) | EWS (`FastForest` / Random Forest) + simulacao de *concept drift* pandemico | Rede publica de Rhode Island (EUA) | Original: Acc = 0,913, F1 = 0,493, AUC = 0,890, Acc@Top3% = 0,645 (AUC 0,868-0,891 sob *drift*). | 8/10 |
| **S0325** | Su et al. (2022) | Regressao Linear Multipla + plano EWS Infinite Campus (GBDT/SHAP) com escala NV-SCSEL | ~60.000-75.000 alunos (261-277 escolas, Nevada) | Clima escolar explicou ate R2_change = 0,15 para atrasos e 0,14 para comportamento (p < 0,001). | 8/10 |
| **S0198** | Goh et al. (2026) | Random Forest (1.000 arvores, 5x5-fold CV) + checklist biopsicossocioeducacional (80 itens) | 194 jovens com TDAH (4-17 anos, Canada) | AUC = 0,75 (CV) e 0,79 (teste, IC 95% [0,68, 0,90]); Acc = 0,73; Sensibilidade = 0,80 (thr=0,42). | 10/10 |
| **S0191** | Madasu & Hajiarbabi (2026) | Sistema especialista baseado em regras (Forward Chaining, BPMN -> AIML) + escala SCARED (41 itens) | 100 avaliadores (70 pais, 30 profissionais de saude) | Concordancia clinica de 92% (ansiedade generalizada) e 89% (panico); 90% de satisfacao; inclui subescala de Evitacao Escolar. | 9/10 |
| **S0283** | Fernandez et al. (2025) | ANN, SVM, Decision Trees + System Dynamics (`EduAnalytics Huila`) | 2.000 alunos secundarios (Colombia) | ANN: Acc = 85,4%, F1 = 0,84, ROC-AUC = 0,88; SVM: Acc = 81,2%; DT: Acc = 77,3%. | 6/10 |
| **S0104** | Nishimura et al. (2024) | Group-Based Trajectory Modeling (ZIP) + Rolling Z-Score + Regressao Binomial Negativa Multinivel + PHQ-4 + JaSC | 2.143 alunos (1o-9o ano, 76 dias letivos, Japao) | Grupo cronico (5,4%): IRR = 5,17 para depressao/ansiedade e IRR = 2,14 para faltas; alfa = 0,71; Entropia = 0,900. | 9/10 |
| **S0012** | Zhou & Geng (2026) | Mini-revisao sobre IA como suporte a decisao clinica (*decision-first*), fenotipagem digital e LLMs | Revisao narrativa (adolescentes, depressao/ansiedade) | Define requisitos de calibracao, *net benefit*, prevencao de *outcome leakage* e conformidade TRIPOD+AI / PROBAST+AI. | 6/10 |
| **S0204** | Kearney (2021) | Revisao integrativa (5 dominios): EWS, ML (CART, RF, SVM, Ensemble, LCA) + triagem RCADS-25 / MTSS | Revisao teorico-metodologica (K-12) | Propoe integracao sistemico-analitica para problemas de frequencia escolar em camadas (MTSS). | 8/10 |
| **S0206** | Kearney & Childs (2023) | Sintese de metodos algoritmo-baseados (CART, CHAID, SVM, Boosting, LASSO, RF) e modelo-baseados (SEM, LCA) | Sintese de politicas educacionais (K-12) | Orienta traducao de metricas ROC/AUC e analise de causa raiz para politicas escolares. | 8/10 |

---

## 3. Eixo Psicometrico, Redes e Fatores Socioemocionais (12 estudos)

| ID | Estudo (Autor, Ano) | Instrumentos / Tecnicas | Amostra / Contexto | Principais Resultados e Metricas | QA |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **S0735** | Yu et al. (2024) | SRAS-R (21 itens, 5 fatores e SRAS-R-A 4 fatores) + PHQ-9 (EFA, CFA MLR, MGCFA) | 1.108 adolescentes (12-19 anos, China) | CFA 5 fatores: CFI = 0,92, TLI = 0,90, RMSEA = 0,05; alfa = 0,79-0,85; invariancia escalar confirmada; r = 0,27-0,63 com PHQ-9. | 10/10 |
| **S0561** | Pérez-Marco et al. (2026) | SCREEN (12 itens, 4 fatores) — EFA, CFA, MGCFA | 681 estudantes (13-16 anos, Espanha) | CFI = 0,949, TLI = 0,930, RMSEA = 0,052, SRMR = 0,043; alfa = 0,71-0,74; omega = 0,73-0,74; invariancia por genero/idade. | 10/10 |
| **S0567** | Boudouda et al. (2024) | SCREEN (arabe 18 itens, 3 fatores) + SCARED + GAD-7 (EFA, CFA MLR) | Estudo 1: 658; Estudo 2: 485 (12-16 anos, Argelia) | CFI = 0,909, RMSEA = 0,063; alfa total = 0,85, omega = 0,86; r = 0,54 com fobia escolar SCARED. | 9/10 |
| **S0555** | Dong et al. (2026) | Network Analysis (GGM / EBICglasso) + SRAS-R, GAD-7, PHQ-9, ANSSIAQ, AIS, YDQ | 303 adolescentes clinicos com SRB (China) | Alfas = 0,73-0,93; nos centrais: depressao (EI = 1,30) e evitacao emocional na escola (EI = 1,19); CS > 0,50. | 10/10 |
| **S0505** | Gök et al. (2026) | Regressao Linear Multipla + SRAS-R, K-SADS-PL, RCADS, DERS, SDQ, SNAP-IV | 102 jovens com EBSA (40 criancas, 62 adolescentes, Turquia) | Ansiedade de separacao maior em criancas (p = 0,004); R2 = 0,47 (criancas) vs. R2 = 0,18 (adolescentes). | 9/10 |
| **S0500** | Okajima & Hiruma (2025) | EFA, CFA, GLM Gamma/Poisson, Clustering de Ward + FSAS, LOT, TILS, AIS, SDI, CIRENS | 128 estudantes de ensino medio (Toquio, Japao) | LOT alfa = 0,94, CFI = 0,99, RMSEA = 0,05; GLM: TILS -> FSAS (R2 = 0,29), FSAS -> faltas (R2 = 0,38). | 10/10 |
| **S0120** | Pérez-Marco et al. (2026) | CFA/MGCFA + Latent Profile Analysis (LPA) + MANOVA + GBS e SCREEN | 690 adolescentes (12-17 anos, Espanha) | GBS CFI = 0,958, RMSEA = 0,053; LPA 4 perfis (Entropia = 0,825); grupo *Highly Excluded* com maior risco em SCREEN (d = 1,15). | 10/10 |
| **S0091** | Sorrenti et al. (2026) | EFA/CFA + Regressao Linear Hierarquica + ARSNA (13 itens, 4 fatores) e PCLDS | Estudo 1: 391/593; Estudo 2: 183 (14-19 anos, Italia) | ARSNA CFA: CFI = 0,90, RMSEA = 0,07; alfa = 0,62-0,78; School Refusal HMRA: R2 = 0,257. | 10/10 |
| **S0145** | Møller et al. (2025) | Survey 2 fases + EFA, CFA e Regressao Linear; 30 sinais precoces (7 fatores) | Fase 1: 196; Fase 2: 509 pais (Noruega) | EFA KMO = 0,86 (24 itens, 7 fatores); CFA CFI = 0,871, RMSEA = 0,070; idade media de inicio: 10,1 anos. | 9/10 |
| **S0154** | Husa et al. (2022) | GLM Quasi-Poisson + regressao stepwise + CDC PRAMS (14 desafios pre-natais) | 3.549 respondentes (33.417 criancas ponderado, Alasca) | 22% absenteismo cronico (<90%); 4+ desafios pre-natais aumentam risco (ARR = 1,29; IC 95% 1,04-1,60). | 9/10 |
| **S0030** | Benjamin et al. (2022) | Protocolo de metodos mistos (revisao, e-Delphi, EFA piloto); cita SCARED, SCAS, PAS | Criancas 4-8 anos (Africa do Sul; planejado N~400) | Protocolo publicado sem metricas empiricas ainda; foca triagem escolar precoce por professores. | 7/10 |
| **S0075** | Sahoo et al. (2024) | Revisao narrativa clinico-educacional; cita SRAS, ISAP, CBCL, TRF | 38 artigos originais (MEDLINE/Scopus) | Sintetiza prevalencia global de recusa escolar (2-16%; ate 7% na India) e taxas de retorno. | 7/10 |

---

## 4. Excluidos Apos Leitura Integral do PDF (`2` estudos)
* **`S0133` (Jain et al., 2025):** *A PSO weighted ensemble framework with SMOTE balancing for student dropout prediction* — Excluido por `EC2` porque o texto completo utiliza o dataset da UCI de **Ensino Superior** (`N = 4.424` universitarios), apenas com variaveis academicas/economicas, sem recusa escolar ou educacao basica.
* **`S0153` (Chen et al., 2022):** *Transactions between Problem Behaviors and Academic Performance in Early Childhood* — Excluido por `EC2` porque o texto completo mensura apenas problemas de comportamento e desempenho em leitura/matematica (IRT), sem desfecho de absenteismo, frequencia ou recusa escolar.
