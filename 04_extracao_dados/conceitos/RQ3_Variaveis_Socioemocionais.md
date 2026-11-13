---
id: RQ3_Variaveis_Socioemocionais
title: "RQ3: Variáveis Socioemocionais, Comportamentais e Contextuais"
type: questao_pesquisa
tags:
  - rsl/rq
  - variaveis
  - socioemocional
  - contexto_escolar
---

# RQ3: Quais variáveis e características (socioemocionais, comportamentais, contextuais) são mais relevantes nesses modelos?

> [!ABSTRACT] Objetivo da RQ3
> Catalogar as dimensões de dados integradas aos modelos preditivos e instrumentos psicométricos, identificando se os modelos se limitam a registros acadêmicos/frequência ou se incorporam determinantes socioemocionais, familiares e psicossociais.

---

## Dimensões e Grupos de Variáveis Mapeadas

### 1. Dimensão Psicológica e Socioemocional
- **Ansiedade:** Fobia escolar, ansiedade social, ansiedade de separação, somatização pré-escolar (medo, náuseas matinais).
- **Humor e Afeto:** Sintomas depressivos, anedonia, desesperança.
- **Autorregulação:** Resiliência emocional, autoeficácia acadêmica, mecanismos de enfrentamento (*coping*).

### 2. Dimensão Comportamental e Acadêmica
- **Padrão de Presença:** Micro-faltas, atrasos frequentes nas primeiras aulas, saídas antecipadas, faltas consecutivas na sexta ou segunda-feira.
- **Desempenho Escolar:** Queda abrupta no rendimento, não entrega de tarefas, reprovações anteriores.
- **Comportamento e Disciplina:** Ocorrências disciplinares, episódios de isolamento no recreio, vitimização por *bullying*.

### 3. Dimensão Familiar e Domiciliar
- **Dinâmica Parental:** Práticas parentais excessivamente protetoras ou negligentes, conflitos familiares.
- **Saúde Familiar:** Doença crônica ou transtorno psiquiátrico de cuidadores.
- **Condição Socioeconômica:** Vulnerabilidade social, necessidade de trabalho precoce, instabilidade habitacional.

### 4. Dimensão Institucional e do Clima Escolar
- **Relação com Professores:** Sentimento de pertencimento e acolhimento escolar.
- **Segurança Escolar:** Percepção de segurança no trajeto e no ambiente escolar.

---

## Perguntas-Chave de Extração
1. Quais variáveis apresentaram maior importância relativa (SHAP values, Gini importance, coeficientes)?
2. As variáveis socioemocionais aumentaram o poder preditivo além das variáveis puramente históricas de presença?

---

## Estudos Relacionados a esta RQ
```dataview
TABLE title, year, population_scope, qa_score
FROM "04_extracao_dados/estudos"
WHERE contains(rqs, "RQ3")
SORT year DESC
```

---
- **MOC Geral:** [[00_INDEX|Voltar ao Índice da RSL]]
