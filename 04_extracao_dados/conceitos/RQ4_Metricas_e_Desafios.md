---
id: RQ4_Metricas_e_Desafios
title: "RQ4: Métricas de Avaliação, Desempenho, Desafios Metodológicos e Éticos"
type: questao_pesquisa
tags:
  - rsl/rq
  - metricas
  - desafios
  - etica_ia
  - limitacoes
---

# RQ4: Quais métricas de desempenho e validação são reportadas, e quais os principais desafios metodológicos e éticos identificados?

> [!ABSTRACT] Objetivo da RQ4
> Avaliar o rigor científico dos estudos incluídos, examinando a robustez das métricas reportadas, os protocolos de validação (para evitar data leakage), o tratamento do desbalanceamento extremo de classes e as salvaguardas éticas e de privacidade para dados infanto-juvenis.

---

## Métricas de Avaliação
- **Métricas Psicométricas:**
  - Consistência interna: Alfa de Cronbach ($\alpha$), Ômega de McDonald ($\omega$).
  - Validade de construto: Análise Fatorial Confirmatória (CFA - RMSEA, CFI, TLI).
- **Métricas Computacionais (Machine Learning):**
  - **Sensibilidade / Recall:** Essencial para minimizar falsos negativos (alunos em risco que não são detectados).
  - **Precisão / Valor Preditivo Positivo (VPP):** Para evitar fadiga de alerta em professores e pedagogos.
  - **F1-Score / PR-AUC:** Cruciais em conjuntos de dados com classes raras/desbalanceadas.
  - **ROC-AUC:** Medida global de discriminação.
  - **Matthews Correlation Coefficient (MCC):** Medida balanceada para cenários binários assimétricos.

---

## [Pendente] Desafios Metodológicos Recorrentes
1. **Desbalanceamento Severo de Classes:** A taxa de recusa escolar grave ou absenteísmo crônico costuma ser de 5% a 15% na população geral, induzindo modelos a prever apenas a classe majoritária se não houver ajuste de custo ou reamostragem (SMOTE, Class Weights).
2. **Vazamento de Dados (*Data Leakage*):** O uso de variáveis futuras (ex.: total de faltas do final do ano letivo para prever risco no 1º bimestre) invalida a aplicação prática do alerta precoce.
3. **Generalização Multicêntrica:** Dificuldade de aplicar um modelo treinado em uma rede de ensino específica em outras regiões com realidades socioeconômicas distintas.

---

## Desafios Éticos e de Transparência
- **Privacidade e Proteção de Dados (LGPD / GDPR / FERPA):** Sensibilidade extrema ao lidar com histórico médico, saúde mental de crianças e registros disciplinares escolares.
- **Risco de Estigmatização (*Self-fulfilling prophecy*):** O perigo de rotular alunos como "propensos à evasão", gerando preconceito velado por parte de docentes.
- **Interpretabilidade e Confiança:** Necessidade imperativa de [[Explicabilidade_XAI|XAI]] para que psicólogos e orientadores escolares compreendam a justificativa da bandeira de risco emitida.

---

## Estudos Relacionados a esta RQ
```dataview
TABLE title, year, database, qa_score
FROM "04_extracao_dados/estudos"
WHERE contains(rqs, "RQ4")
SORT qa_score DESC
```

---
- **MOC Geral:** [[00_INDEX|Voltar ao Índice da RSL]]
