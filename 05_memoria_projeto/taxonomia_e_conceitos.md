# Taxonomia e Conceitos Padronizados da Pesquisa (taxonomia_e_conceitos.md)

**Projeto:** Revisao Sistematica da Literatura (RSL) sobre Recusa Escolar e Inteligencia Artificial  
**Pesquisador:** Matheus Henrique Assuncao de Medeiros  
**Programa:** PGCC UERN / UFERSA  
**Responsavel:** Especialista 4 (Gestao de Memoria) em cooperacao com Especialista 2  

---

## 1. Distincoes Terminologicas Centrais da Infrequencia Escolar

| Conceito / Termo | Definicao Operacional e Clinica | Diferenciacao em Relacao aos Demais |
| :--- | :--- | :--- |
| **School Refusal Behavior (SRB)** | Dificuldade ou recusa da crianca/adolescente em frequentar a escola decorrente de angustia emocional severa (ansiedade, panico, fobia social ou sintomas somatizados). | Os pais sabem onde a crianca esta (ela fica em casa); ha ausencia de comportamento antissocial grave. |
| **Emotionally Based School Avoidance (EBSA)** | Terminologia contemporanea britanica e europeia para SRB, enfatizando a raiz emocional e os fatores ambientais e sistemicos que causam a aversao escolar. | Supera o rotulo punitivo individualista, enfatizando a interacao entre contexto escolar e sofrimento psicologico. |
| **Truancy (Infrequencia Evasiva / Vadiagem)** | Ausencia escolar nao autorizada sem justificativa plausivel, na qual a crianca nao permanece em casa e os responsaveis frequentemente ignoram a falta. | Associada a condutas antissociais, delinquencia juvenil ou desengajamento escolar; nao e motivada por ansiedade ou sofrimento emocional. |
| **School Withdrawal (Retencao Parental)** | Ausencia escolar deliberada promovida ou consentida pelos proprios pais/cuidadores (ex.: trabalho domestico, cuidado de irmaos ou neglicencia familiar). | A motivacao primaria nao parte do estudante, mas de pressoes ou necessidades familiares externas a escola. |
| **Chronic Absenteeism (Absenteismo Cronico)** | Metrica administrativa educacional que define o estudante que perde 10% ou mais dos dias letivos no ano letivo (por faltas justificadas ou injustificadas). | Conceito guarda-chuva puramente quantitativo; no Brasil, absorve indiferenciadamente a recusa emocional, a retencao e a evasao sob a rubrica generica de abandono escolar. |

---

## 2. Instrumentos Psicometricos e Clinicos Fundamentais (Eixo RQ1)

### SRAS-R (School Refusal Assessment Scale - Revised)
- **Autores:** Kearney & Silverman.
- **Estrutura Funcional:** Instrumento de 24 itens, com versoes para criancas/adolescentes e para os pais, avaliando 4 condicoes motivacionais (fatores funcionais):
  1. *Fator 1 (Evitacao de estimulos negativos escolares):* Sintomas somáticos, panico ou nausea ao aproximar-se da escola.
  2. *Fator 2 (Fuga de situacoes sociais avaliativas/aversivas):* Medo de testes, apresentacao em publico, interacoes com colegas ou bullying.
  3. *Fator 3 (Busca de atencao de figuras de apego):* Ansiedade de separacao, permanencia em casa junto a mae/pai.
  4. *Fator 4 (Reforco positivo tangivel fora da escola):* Jogar videogame, assistir televisao, dormir ou encontrar pares fora da escola.

### SCREEN (School Refusal Evaluation and Engagement Network)
- Instrumento contemporaneo de triagem rapida aplicado por educadores diretamente em ambiente escolar para identificacao precoce de risco de EBSA.

### SCARED e DASS-21
- Escalas complementares empregadas nos estudos para mensurar comorbidades de ansiedade somatica, fobia escolar e sintomas depressivos associados a recusa.

---

## 3. Arquiteturas Computacionais de Inteligencia Artificial (Eixo RQ2 / RQ4)

| Paradigma | Algoritmos Predominantes | Aplicacao na Literatura da RSL |
| :--- | :--- | :--- |
| **Tree-based Ensembles** | Random Forest, XGBoost, LightGBM, CatBoost | Predicao supervisionada sobre dados administrativos escolares tabulares (presenca semanal, notas, demografia). |
| **Deep Learning Sequencial** | LSTM (Long Short-Term Memory), GRU, 1D-CNN | Modelagem temporal de series temporais de frequencia e padroes de faltas ao longo dos bimestres. |
| **Sistemas de Alerta Precoce (EWS)** | Early Warning Systems baseados em regras ou ML | Plataformas de gestao escolar que emitem alertas de risco de evasao antes da consolidacao do abandono. |
| **Explicabilidade (XAI)** | SHAP (SHapley Additive exPlanations), LIME | Tecnicas para interpretar a contribuicao das variaveis em cada predicao, essenciais para conformidade etica e atuacao pedagogica. |

---

## 4. Glossario de Siglas do Projeto
- **RSL:** Revisao Sistematica da Literatura.
- **EBSA:** *Emotionally Based School Avoidance*.
- **SRAS-R:** *School Refusal Assessment Scale - Revised*.
- **EWS:** *Early Warning System* (Sistema de Alerta Precoce).
- **XAI:** *Explainable Artificial Intelligence* (Inteligencia Artificial Explicavel).
- **PRISMA:** *Preferred Reporting Items for Systematic Reviews and Meta-Analyses*.
- **PICOC (Estrutura Oficial do Protocolo):** *Population* (Ensino Basico), *Intervention* (IA - Ferramentas de diagnostico ou diagnostico), *Outcomes* (Recusa escolar OR [evasao escolar AND socio-emotional factor]).
