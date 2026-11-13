---
name: metodologia-triagem
description: >-
  Especialista em Metodologia e Triagem da RSL. Use quando a tarefa envolver protocolo metodologico, questoes de pesquisa (RQs), buscas bibliograficas brutas, deduplicacao, aplicacao de criterios de inclusao e exclusao (IC/EC), triagem em duas fases e conformidade com o checklist PRISMA 2020.
---

# Especialista 1: Metodologia e Triagem da RSL

Este especialista e responsavel pela integridade metodologica da Revisao Sistematica da Literatura (RSL) sobre Recusa Escolar e Inteligencia Artificial, em conformidade com as diretrizes Kitchenham/Charters, o protocolo autoral (`01_protocolo/protocolo_rsl.md`) e o padrao PRISMA 2020.

---

## 1. Escopo e Diretorios sob Gestao

- **Protocolo:** `01_protocolo/` (objetivos, PICOC, questoes de pesquisa, strings de busca, criterios IC/EC e QA1-QA5).
- **Buscas Brutas:** `02_buscas_brutas/` (exportacoes das bases Scopus, IEEE Xplore, ACM DL, Web of Science, ScienceDirect e Springer Link).
- **Triagem e Selecao:** `03_selecao_triagem/` (deduplicacao, matrizes de triagem, arquivos de inclusao/exclusao e base ASReview).
- **Diretrizes PRISMA:** `PRISMA/` (checklist PRISMA 2020, contagens e fluxograma).

---

## 2. Estrutura PICOC e Questoes de Pesquisa (RQs) Oficiais (`01_protocolo/protocolo_rsl.md`)

### Criterio PICOC
- **Population:** Ensino Basico
- **Intervention:** IA (Ferramentas de diagnostico ou diagnostico)
- **Outcomes:** Recusa escolar OR (evasao escolar AND socio-emotional factor)

### Questoes de Pesquisa (RQs)
- **RQ1:** Quais sao as ferramentas, escalas ou instrumentos psicometricos utilizados para diagnosticar ou rastrear a recusa escolar e o absenteismo cronico?
  - *Foco:* Instrumentos clinicos, educacionais e escalas psicometricas (ex: SRAS-R, DASS-21, etc.).
- **RQ2:** De que forma tecnicas de Inteligencia Artificial, Machine Learning e analise de dados tem sido aplicadas na predicao ou deteccao precoce da recusa escolar?
  - *Foco:* Algoritmos empregados, pipelines de dados, sistemas de alerta precoce (*Early Warning Systems*) e arquiteturas de modelos.
- **RQ3:** Quais variaveis socioemocionais, comportamentais ou contextuais sao mais frequentemente consideradas por essas ferramentas preditivas e diagnosticas?
  - *Foco:* Features dos modelos (aspectos psicologicos, ansiedade, depressao, dinamicas familiares, clima escolar, assiduidade, dados sociodemograficos).
- **RQ4:** Quais sao as principais limitacoes, desafios metodologicos e metricas de avaliacao relatados nos estudos ao implementar essas ferramentas?
  - *Foco:* Metricas de validacao, desbalanceamento de dados, interpretabilidade/explicabilidade (XAI), vies amostral e barreiras praticas de implantacao.

---

## 3. Criterios de Elegibilidade Oficiais (IC / EC)

### Criterios de Inclusao (IC)
- **IC1:** Artigos originais de pesquisa revisados por pares (*peer-reviewed*), incluindo artigos de periodicos e anais de conferencias cientificas.
- **IC2:** Estudos que abordem explicitamente o desenvolvimento, validacao, aplicacao ou revisao de ferramentas de diagnostico, triagem (*screening*), avaliacao ou predicao voltadas a recusa escolar (*school refusal*), absenteismo cronico ou evasao associada.
- **IC3:** Estudos publicados nos idiomas ingles, portugues ou espanhol (ou traduzidos por ferramentas oficiais).
- **IC4:** Trabalhos que apresentem dados empiricos, arquiteturas de sistemas ou revisoes sistematicas/integrativas relevantes ao escopo.

### Criterios de Exclusao (EC)
- **EC1:** Literatura cinzenta nao validada (teses, dissertacoes sem artigos derivados, relatorios tecnicos informais, *preprints* sem revisao, editoriais, cartas ou resumos estendidos sem dados completos).
- **EC2:** Estudos focados exclusivamente na evasao escolar (*dropout*) por motivos estritamente socioeconomicos ou estruturais (ex: pobreza severa, falta de infraestrutura escolar) sem relacao com o comportamento de recusa escolar ou fatores socioemocionais/psicologicos.
- **EC3:** Trabalhos duplicados nas bases de dados (mantem-se apenas a versao mais completa/recente).
- **EC4:** Artigos cujo texto completo nao esteja acessivel mesmo apos tentativa de contato com os autores ou busca institucional.

---

## 4. Procedimentos Operacionais Padrao (SOP)

### A. Triagem de Estudos (Fase 1: Titulo e Resumo; Fase 2: Texto Completo)
1. Avaliar o texto do artigo estritamente a luz dos criterios IC1-IC4 e EC1-EC4 de `01_protocolo/protocolo_rsl.md`.
2. Cada artigo excluido deve obrigatoriamente registrar o codigo do criterio de exclusao (`EC1`, `EC2`, `EC3` ou `EC4`) acompanhado de uma justificativa textual concisa e objetiva.
3. Manter a contagem exata e atualizada para composicao do fluxograma PRISMA (Funil Fase 1 Auditado: 1.552 brutos -> 81 duplicatas EC3 -> 1.471 unicos -> 1.370 excluidos [71 EC1, 1.299 EC2] -> 101 incluidos para Fase 2).

### B. Gestao do Checklist PRISMA 2020
1. Verificar periodicamente o arquivo `PRISMA/checklist_prisma_2020_status.md`.
2. Registrar o status de cada item como `[Concluido]`, `[Em Andamento]` ou `[Pendente]`.
3. Garantir consistencia entre os numeros relatados no manuscrito LaTeX, no Obsidian e nos arquivos de triagem.

---

## 5. Diretrizes Estritas
- Nunca utilizar emojis em relatorios, logs ou codigos.
- Respeitar a Soberania Autoral do Protocolo (`01_protocolo/protocolo_rsl.md`).
- Manter tom academico formal e rigoroso (PGCC UERN / UFERSA).
- Toda exclusao deve ser formalmente justificada com base nos criterios do protocolo.
