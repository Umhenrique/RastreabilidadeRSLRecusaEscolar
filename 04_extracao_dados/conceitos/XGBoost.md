---
id: XGBoost
title: "XGBoost (Extreme Gradient Boosting)"
type: algoritmo_ia
tags:
  - machine_learning
  - gradient_boosting
  - xgboost
  - predicao
---

# XGBoost: Extreme Gradient Boosting

> [!ABSTRACT] Definição
> O **XGBoost** é uma implementação otimizada e escalável de algoritmos de *gradient boosting* que constrói sequencialmente árvores de decisão corrigindo os resíduos das iterações anteriores através de otimização de segunda ordem (gradiente e hessiano) e regularização ($L_1$ e $L_2$).

---

## Aplicação em Desbalanceamento de Presença Escolar
- Em problemas de absenteísmo crônico e recusa escolar, a proporção de alunos em risco é minoritária (desbalanceamento severo).
- O parâmetro `scale_pos_weight` e funções de perda customizadas do XGBoost permitem calibrar a sensibilidade para maximizar a captura de estudantes vulneráveis sem colapsar a precisão.
- Frequentemente alcança o topo de ROC-AUC e PR-AUC em estudos empíricos comparativos.

---

## Conexões
- Questões: [[RQ2_Modelos_IA_e_Predicao]], [[RQ4_Metricas_e_Desafios]]
- Algoritmos Relacionados: [[Random_Forest]]
- MOC Geral: [[00_INDEX|Voltar ao Índice]]
