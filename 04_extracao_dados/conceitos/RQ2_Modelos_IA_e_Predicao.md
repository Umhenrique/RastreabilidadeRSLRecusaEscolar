---
id: RQ2_Modelos_IA_e_Predicao
title: "RQ2: Abordagens Computacionais e de Inteligência Artificial"
type: questao_pesquisa
tags:
  - rsl/rq
  - machine_learning
  - inteligencia_artificial
  - predicao
---

# RQ2: Que abordagens de inteligência artificial ou modelos preditivos vêm sendo aplicados na previsão de absenteísmo crônico e recusa escolar?

> [!ABSTRACT] Objetivo da RQ2
> Identificar a taxonomia de modelos computacionais, algoritmos de Machine Learning, Deep Learning e sistemas inteligentes aplicados na modelagem preventiva do absenteísmo escolar crônico, evasão e recusa escolar.

---

## Famílias de Modelos e Algoritmos Mapeados
- **Modelos Ensemble Baseados em Árvores:**
  - [[Random_Forest|Random Forest (RF)]]: Alta robustez contra overfitting e capacidade de lidar com dados tabulares heterogêneos.
  - [[XGBoost|XGBoost / LightGBM / CatBoost]]: Algoritmos de gradiente boosting predominantes em competições e dados de registros escolares desbalanceados.
- **Modelos Tradicionais de Classificação:**
  - **Regressão Logística:** Modelo baseline explicável para odds ratio de risco.
  - **SVM (Support Vector Machines):** Eficaz em margens de separação com features padronizadas.
- **Deep Learning e Redes Neurais:**
  - **MLP (Multilayer Perceptrons):** Redes neurais densas para dados tabulares.
  - **RNNs / LSTM / Transformers:** Utilizados para modelar séries temporais de frequência diária/semanal ao longo dos anos letivos.
- **Arquiteturas de Sistema:**
  - [[Early_Warning_Systems|Sistemas de Alerta Precoce (EWS)]]: Plataformas que consolidam dados de presença, notas e comportamento para acionar intervenções preventivas.
  - [[Explicabilidade_XAI|Técnicas de IA Explicável (XAI)]]: SHAP, LIME para justificar as predições a coordenadores e psicólogos.

---

## Perguntas-Chave de Extração
1. Qual o tipo de tarefa computacional (Classificação binária de risco, regressão de dias de falta, clustering de perfis)?
2. A predição é realizada em tempo hábil (início do bimestre/ano letivo) ou post-hoc?
3. O modelo foi avaliado com estratégias adequadas de validação temporal ou cross-validation estratificada?

---

## Estudos Relacionados a esta RQ
```dataview
TABLE title, year, algorithms, database, qa_score
FROM "04_extracao_dados/estudos"
WHERE contains(rqs, "RQ2")
SORT year DESC
```

---
- **MOC Geral:** [[00_INDEX|Voltar ao Índice da RSL]]
