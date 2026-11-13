# Estado Atual do Conhecimento da RSL (estado_conhecimento_rsl.md)

**Projeto:** Revisao Sistematica da Literatura (RSL) sobre Recusa Escolar e Inteligencia Artificial  
**Pesquisador:** Matheus Henrique Assuncao de Medeiros  
**Programa:** PGCC UERN / UFERSA  
**Responsavel:** Especialista 4 (Gestao de Memoria)  
**Data da Ultima Atualizacao:** 30 de Outubro de 2026  
**Status Global:** `[Concluido]` Fase 1 (Triagem Auditada) | `[Em Andamento]` Fase 2 (Extracao de 101 Estudos)  

---

## 1. Funil PRISMA 2020 Consolidado e Auditado

```text
[Identificacao Bruta]
   Total coletado em 6 bases academicas: N = 1.552
   ├── Springer Link: 1.000
   ├── ACM Digital Library: 198
   ├── Scopus: 195
   ├── Web of Science: 83
   ├── ScienceDirect: 62
   └── IEEE Xplore: 14
        │
        ▼
[Deduplicacao Inter-Bases (EC3)]
   Duplicatas expurgadas: N = 81
        │
        ▼
[Fase 1: Triagem de Titulo e Resumo]
   Corpus unico avaliado: N = 1.471
   Registros excluidos na triagem auditada: N = 1.370
   ├── Incompatibilidade documental / literatura cinzenta (EC1): N = 71
   └── Fora do escopo / covariavel demografica / populacao inadequada (EC2): N = 1.299
        │
        ▼
[Fase 2: Elegiveis para Leitura de Texto Completo e Extracao]
   Corpus oficial aprovado: N = 101 artigos cientificos (Taxa de selecao: 6,9%)
   ├── Scopus: 61
   ├── Springer Link: 20
   ├── Web of Science: 10
   ├── ACM Digital Library: 4
   ├── ScienceDirect: 3
   └── IEEE Xplore: 3
```

---

## 2. Status de Resposta as Questoes de Pesquisa (Ordem Oficial de `01_protocolo/protocolo_rsl.md`)

| Questao de Pesquisa | Foco Tematico Oficial | Status Atual | Sintese Preliminar dos Achados |
| :--- | :--- | :--- | :--- |
| **RQ1 (Instrumentos Psicometricos)** | Ferramentas, escalas ou instrumentos psicometricos para diagnosticar ou rastrear recusa escolar e absenteismo cronico | `[Em Andamento]` | A literatura clinica e psicometrica converge no modelo funcional da escala SRAS-R (4 funcoes operantes), em triagens escolares rapidas (SCREEN) e escalas de ansiedade comorbida (SCARED, DASS-21). |
| **RQ2 (Modelos de IA e ML)** | Tecnicas de IA, Machine Learning e analise de dados na predicao ou deteccao precoce da recusa escolar | `[Em Andamento]` | Forte predominancia de algoritmos de ensemble em arvores (Random Forest e XGBoost) para dados tabulares e emergencia de arquiteturas sequenciais (LSTM) e Early Warning Systems (EWS). |
| **RQ3 (Variaveis e Features)** | Variaveis socioemocionais, comportamentais ou contextuais consideradas pelas ferramentas | `[Em Andamento]` | Frequencia escolar semanal, notas, clima escolar, vitimizacao por bullying, ansiedade, suporte parental e neurodivergencia (TEA/TDAH). Bases administrativas governamentais carecem de variaveis de saude mental. |
| **RQ4 (Limitacoes e Metricas)** | Limitacoes, desafios metodologicos e metricas de avaliacao relatados nos estudos | `[Em Andamento]` | Metricas de F1-Score, Recall, AUC-ROC e Alfa de Cronbach destacam-se frente ao severo desbalanceamento de classes. Exigencia crescente de tecnicas de explicabilidade (XAI: SHAP e LIME) para uso pedagogico etico. |

---

## 3. Infraestrutura de Extracao da Fase 2

- **Fonte Unica da Verdade:** 101 notas individuais em `04_extracao_dados/estudos/*.md` sincronizadas com `00_INDEX.md`.
- **Repositorio de Textos Integrais:** `04_extracao_dados/pdfs/` (convencao `SXXXX.pdf`).
- **Consolidacao Automatizada:** `scripts/consolidar_extracao_fase2.py` exporta `04_extracao_dados/matriz_extracao.csv` e `04_extracao_dados/matriz_extracao.xlsx` com validacao de status e calculo automatico de `QA1-QA5` (`0 a 10 pontos`).

---

## 4. Principais Lacunas Identificadas (Gaps para a Dissertacao)

1. **A Invisibilidade Diagnostica da Recusa Escolar no Brasil:**
   - Dados governamentais (Censo Escolar / INEP) registram apenas presenca binaria e rotulam o estudante como "abandono/evasao". Nao ha captura de dados socioemocionais ou ansiedade escolar.
   - O estudo seminal de Barros et al. (Nature Scientific Reports, 2026) demonstra a viabilidade de predizer absenteismo em 22.000 escolas brasileiras com ML interpretavel, mas opera estritamente com atributos economicos e academicos, sem rastreio de sofrimento emocional.
2. **Desconexao entre Ferramentas de IA e Instrumentos Psicometricos:**
   - A literatura de Ciencia da Computacao foca em grandes volumes de dados tabulares passivos (Early Warning Systems).
   - A literatura de Psicologia e Saude foca em aplicacoes individuais da SRAS-R em clinica ou pesquisa amostral.
   - Quase nao ha sistemas hibridos que utilizem a IA para sinalizar o risco e acionar protocolos de triagem socioemocional em ambiente escolar basico.
