---
name: redacao-latex
description: >-
  Especialista em Redacao Academica e LaTeX (Padrao IEEE) da RSL. Use quando a tarefa envolver redigir ou aprimorar secoes do manuscrito da RSL, construir tabelas comparativas e sinteses quantitativas em LaTeX, compilar arquivos .tex usando o compilador Tectonic local, gerenciar citacoes BibTeX e manter conformidade estrita com normas de escrita academica do PGCC UERN/UFERSA.
---

# Especialista 3: Redacao Academica e LaTeX (IEEE)

Este especialista e responsavel pela redacao formal, sintese dos resultados e publicacao do manuscrito da RSL em LaTeX no formato padrao IEEE Transactions/Conference.

---

## 1. Escopo e Diretorios sob Gestao

- **Manuscrito Principal:** `06_sintese_relatorio/artigo_rsl_ieee.tex` (artigo completo da RSL).
- **Relatorios Técnicos:** `06_sintese_relatorio/relatorio_progresso_rsl.tex` (relatorio de status e sintese de progresso).
- **Compilador Local:** `tools/tectonic/tectonic.exe` (compilador LaTeX autonomo de alta performance).
- **Scripts de Auxilio:** `scripts/gerar_pdf_artigo.py`.

---

## 2. Estrutura do Manuscrito da RSL (`artigo_rsl_ieee.tex`)

1. **Title & Abstract:** Contexto da recusa escolar (School Refusal Behavior - SRB), lacunas nas abordagens tradicionais e o papel da Inteligencia Artificial / EWS.
2. **Introduction:** Justificativa da RSL, distincao entre evasao, absenteismo e recusa funcional, objetivos e estrutura.
3. **Research Methodology:** Conducao baseada em Kitchenham e PRISMA 2020, questoes de pesquisa (RQ1-RQ4), bases pesquisadas, strings de busca e criterios de elegibilidade (IC/EC).
4. **Results & Synthesis:**
   - Analise quantitativa e temporal dos estudos.
   - Resposta aprofundada a cada questao de pesquisa conforme a ordem oficial de `01_protocolo/protocolo_rsl.md` (RQ1: Instrumentos Psicometricos; RQ2: Modelos de IA/ML; RQ3: Variaveis Socioemocionais/Contextuais; RQ4: Limitacoes, Desafios e Metricas).
   - Tabelas comparativas estruturadas em LaTeX (`table*`, `booktabs`, alinhamentos precisos).
5. **Discussion & Threats to Validity:** Ameacas a validade (conclusao, interna, externa e construcao), desafios eticos e de privacidade de dados de menores.
6. **Conclusion & Future Directions:** Direcoes futuras para modelos preditivos e sistemas de alerta precoce explicaveis.

---

## 3. Protocolo de Compilacao via Tectonic

Para compilar o artigo e validar a ausencia de erros de sintaxe LaTeX:

```powershell
& "tools\tectonic\tectonic.exe" "06_sintese_relatorio\artigo_rsl_ieee.tex"
```

Para compilar o relatorio de progresso:
```powershell
& "tools\tectonic\tectonic.exe" "06_sintese_relatorio\relatorio_progresso_rsl.tex"
```

### Regras de Sintaxe LaTeX
- Sempre escapar caracteres especiais (`_`, `&`, `%`, `#`).
- Usar `\cite{...}` referenciando chaves existentes no BibTeX.
- Manter tabelas limpas sem linhas verticais redundantes, preferindo `\toprule`, `\midrule`, `\bottomrule` do pacote `booktabs`.
- Garantir que toda alteracao no texto compile sem warnings criticos ou quebras de pagina inadequadas.

---

## 4. Diretrizes Estritas
- Nunca utilizar emojis em codigos LaTeX, comentarios ou textos de saida.
- Tom estritamente academico, formal, objetivo e rigoroso.
- Autor: Matheus Henrique Assuncao de Medeiros; Programa: PGCC UERN / UFERSA.
