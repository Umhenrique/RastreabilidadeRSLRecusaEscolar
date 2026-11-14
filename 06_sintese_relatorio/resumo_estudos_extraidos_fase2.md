# RSL Recusa Escolar e IA - Sintese Atualizada (DEC-008)

**Pesquisador:** Matheus Henrique Assuncao de Medeiros (PGCC UERN/UFERSA)  
**Data da Atualizacao:** 13 de Novembro de 2026  
**Criterio IC1 Atualizado:** Artigos empiricos revisados por pares que apliquem tecnicas de IA, Machine Learning ou modelagem preditiva associadas a recusa escolar ou ao absenteismo escolar com fatores socioemocionais (escalas psicometricas isoladas e revisoes secundarias sem modelo preditivo nao entram como estudos primarios).

## 1. Estado Consolidado da Fase 2 (101 Elegiveis)

| Situacao na Fase 2 | Quantidade | Observacao |
| :--- | :---: | :--- |
| `[Incluido Fase 2 - Extracao Concluida]` | 5 | 4 validados (`S0198`, `S0104`, `S0501`, `S0290`) + 1 `[EM DUVIDA]` (`S0191`) |
| `[Excluido Fase 2]` | 37 | **16** na auditoria pre-extracao (`DEC-007`, antes dos PDFs) + **21** apos leitura completa dos 26 PDFs (`2` iniciais `S0133`/`S0153` + `19` `DEC-008`) |
| `[Pendente Leitura Completa]` | 59 | Aguardando obtencao e leitura integral dos PDFs |

---

## 2. Tabela Comparativa dos Estudos Ativos (5 Estudos)

| ID | Titulo resumido + nome | Algoritmo + tecnicas | Amostra | Fatores socioemocionais | Resultados | OBS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `S0198` | ML para Classificacao de Padroes de Absenteismo em Jovens com TDAH (Goh et al., 2026) | Random Forest (1.000 arvores; 5x5-fold CV; split 67/33) + checklist biopsicossocioeducacional (80 itens) | N = 194 jovens com TDAH (4-17 anos, Canada) | Sintomas internalizantes e externalizantes, sono, clima familiar e funcionamento escolar | AUC = 0,75 (CV) e 0,79 (teste); Acuracia = 0,73; Sensibilidade = 0,80 (limiar 0,42) | `[INCLUIDO]` Dentro do tema: une ML + fatores socioemocionais + absenteismo escolar |
| `S0104` | Deteccao Precoce de Saude Mental via Observacao Diaria Digitalizada no Japao (Nishimura et al., 2024) | Group-Based Trajectory Modeling (ZIP) + Rolling Z-Score (7 dias) + Regressao Binomial Negativa Multinivel + PHQ-4 + JaSC | N = 2.143 alunos (1o ao 9o ano, 76 dias letivos, 5 escolas, Japao) | Emocoes diarias (*Zones of Regulation*), dor/sono, depressao e ansiedade (PHQ-4) e clima escolar (JaSC) | Grupo cronico (5,4%): IRR = 5,17 para depressao/ansiedade e IRR = 2,14 para dias de falta | `[INCLUIDO]` Promissor e explicavel (enquadrado em *Futoukou*, mas registra total de faltas sem separar doenca vs. recusa) |
| `S0501` | ML Interpretavel para Predicao de Absenteismo Escolar em Larga Escala no Brasil (Barros et al., 2026) | Random Forest, CatBoost, XGBoost, LightGBM e Regressao Logistica + XAI (SHAP e contrafactuais *what-if*) | N = 22.476 escolas de Ensino Medio (Brasil; SGP + Censo Escolar + ICG 2024) | Nao possui variaveis socioemocionais individuais (apenas infraestrutura, docentes, equipe pedagogica e regiao) | Acuracia = 0,67-0,85; F1 = 0,58-0,81; Recall = 0,43-0,89 | `[INCLUIDO]` Referencia brasileira em larga escala; evidencia lacuna de variaveis de saude mental no SGP/INEP |
| `S0290` | Ensemble Learning Explicavel para Predicao de Evasao em Contexto de Conflito (Abas et al., 2026) | XGBoost e Random Forest + SMOTE + LASSO + XAI (LIME) + questionario de 34 itens | N = 1.158 estudantes (5 escolas, Sabha, Libia) | Coesao familiar, ambiente escolar, motivacao e *Stress and Anxiety Index* (SAI) | XGBoost Acc/F1 = 0,941 (CV F1 = 0,939); Random Forest Acc/F1 = 0,939 | `[INCLUIDO]` Alvo binario sintetico/heuristico e focado na transicao para o ensino superior (*higher-education non-enrollment*) |
| `S0191` | Chatbot Especialista para Triagem de Transtornos de Ansiedade Infantil (Madasu & Hajiarbabi, 2026) | Sistema Especialista Baseado em Regras (*Forward Chaining*, BPMN convertido em AIML) + escala SCARED (41 itens) | N = 100 participantes (70 pais e 30 profissionais de saude, EUA) | Ansiedade generalizada, panico, ansiedade de separacao, fobia social e evitacao escolar (subescala SCARED) | Concordancia clinica: 92% (ansiedade generalizada) e 89% (panico); 90% de satisfacao | `[EM DUVIDA]` Foca em triagem de ansiedade infantil, tendo evitacao escolar apenas como subescala secundaria |

---

## 3. Resumo dos 19 Estudos Reclassificados para Excluido na Fase 2 (DEC-008)

Estes estudos foram lidos integralmente no lote inicial de 26 PDFs e reclassificados para `[Excluido Fase 2]` apos o ajuste do criterio `IC1` (permanecendo disponiveis apenas para apoio ao referencial teorico do manuscrito, quando aplicavel):

| Study ID | Motivo da Exclusao (EC1 / EC2) | Uso no Texto (Opcional) |
| :--- | :--- | :--- |
| `S0325` | `EC2` - Trabalho em progresso (WIP) sem modelo de ML implementado | N/A |
| `S0283` | `EC2` - EWS administrativo focado em risco economico/saude, sem fatores socioemocionais ou IA/ML | N/A |
| `S0012` | `EC1` - Mini revisao narrativa (nao e estudo primario empirico) | Referencial teorico / introducao |
| `S0075` | `EC1` - Revisao narrativa clinica (nao e estudo primario com IA/ML) | Referencial teorico / definicoes |
| `S0204` | `EC1` - Revisao integrativa (nao e estudo primario com IA/ML) | Referencial teorico / sintese |
| `S0206` | `EC1` - Sintese de politicas / framework conceitual (sem IA/ML empirico) | Referencial teorico / contexto |
| `S0030` | `EC1` - Protocolo metodologico sem dados empiricos nem IA/ML | N/A |
| `S0315`, `S0322` | `EC2` - Estudos psicometricos/estatisticos fora do escopo preditivo de IA/ML | N/A |
| `S0561`, `S0567`, `S0555`, `S0505`, `S0500`, `S0120`, `S0091`, `S0145`, `S0154` | `EC2` - Estudos psicometricos, epidemiologicos ou estatisticos sem modelos preditivos de IA/ML | Referencial teorico (escalas e construtos, ex.: `S0505` sobre EBSA) |
| `S0735` | `EC2` - Estudo de intervencao clinica/preventiva sem IA/ML | N/A |

---

## 4. Declaracao dos Demais Estudos Excluidos na Fase 2 (18 Estudos Previos)

Para rastreabilidade completa dos **37** excluidos na Fase 2 (`19` da `DEC-008` + `18` previos = `37`), registram-se abaixo os **2** estudos excluidos apos leitura integral inicial e os **16** estudos barrados na auditoria pre-extracao (`DEC-007`) antes da obtencao dos PDFs:

### 4.1 Excluidos na Leitura Integral Inicial (2 Estudos)

| Study ID | Motivo da Exclusao (EC2) | Etapa |
| :--- | :--- | :--- |
| `S0133` | `EC2` - Dataset de Ensino Superior (UCI), fora da populacao-alvo (educacao basica) | Leitura integral previa |
| `S0153` | `EC2` - Nao mensura desfecho de absenteismo ou recusa escolar | Leitura integral previa |

### 4.2 Excluidos na Auditoria Pre-Extracao (`DEC-007`, 16 Estudos)

Estes 16 estudos passaram inicialmente na triagem da Fase 1, mas foram excluidos na auditoria de elegibilidade na entrada da Fase 2 (antes da leitura dos PDFs):

| Study ID | Motivo da Exclusao (`DEC-007`) | Etapa |
| :--- | :--- | :--- |
| `S0199` | `EC3` - Duplicata tardia de `S0183` | Auditoria pre-extracao (`DEC-007`) |
| `S0203` | `EC2` - Fora de escopo (relato de caso clinico) | Auditoria pre-extracao (`DEC-007`) |
| `S0001`, `S0018`, `S0019`, `S0033`, `S0042`, `S0053`, `S0080`, `S0105`, `S0113`, `S0136`, `S0152`, `S0183`, `S0202`, `S0214` | `EC2` - Fora de escopo (sem aplicacao de IA/ML ou escala psicometrica) | Auditoria pre-extracao (`DEC-007`) |
