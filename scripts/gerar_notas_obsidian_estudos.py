#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para geração automática das notas de literatura no Obsidian para os 159 estudos incluídos na RSL.
Autor: Matheus Henrique Assunção de Medeiros (PGCC UERN/UFERSA)
"""

import os
import re
import yaml
import pandas as pd

def sanitize_filename(title, max_len=70):
    t = str(title)
    # normalizar aspas tipográficas
    t = t.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    # remover caracteres proibidos no Windows / Obsidian
    t = re.sub(r'[\\/*?:\x22<>|]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    if len(t) > max_len:
        parts = t[:max_len].rsplit(' ', 1)
        t = parts[0] if len(parts) > 1 else t[:max_len]
    return t

def format_author_name(author_str):
    author_str = author_str.strip()
    if ',' in author_str:
        parts = author_str.split(',', 1)
        return f"{parts[1].strip()} {parts[0].strip()}"
    return author_str

def parse_authors(authors_raw):
    if pd.isna(authors_raw):
        return []
    raw_str = str(authors_raw).strip()
    # BibTeX separa autores por ' and '
    authors = [a.strip() for a in raw_str.split(' and ') if a.strip()]
    formatted = [format_author_name(a) for a in authors]
    return formatted

def detect_concepts(text):
    text_lower = text.lower()
    scales = []
    algorithms = []
    
    # Escalas psicométricas
    if 'sras' in text_lower or 'school refusal assessment scale' in text_lower:
        scales.append("[[SRAS-R]]")
    if 'screen' in text_lower and ('school refusal' in text_lower or 'attendance' in text_lower):
        scales.append("[[SCREEN]]")
    if 'scared' in text_lower or 'child anxiety related' in text_lower:
        scales.append("[[SCARED]]")
    if 'dass' in text_lower:
        scales.append("DASS-21")
    if 'cbcl' in text_lower or 'child behavior checklist' in text_lower:
        scales.append("CBCL")
        
    # Algoritmos e abordagens computacionais
    if 'random forest' in text_lower or 'floresta aleatória' in text_lower:
        algorithms.append("[[Random_Forest]]")
    if 'xgboost' in text_lower or 'gradient boost' in text_lower or 'lightgbm' in text_lower:
        algorithms.append("[[XGBoost]]")
    if 'support vector' in text_lower or 'svm' in text_lower:
        algorithms.append("SVM")
    if 'logistic regression' in text_lower or 'regressão logística' in text_lower:
        algorithms.append("Regressão Logística")
    if 'neural network' in text_lower or 'deep learning' in text_lower or 'rede neural' in text_lower or 'lstm' in text_lower:
        algorithms.append("Redes Neurais / Deep Learning")
    if 'early warning' in text_lower or 'alerta precoce' in text_lower or 'ews' in text_lower:
        algorithms.append("[[Early_Warning_Systems]]")
    if 'shap' in text_lower or 'lime' in text_lower or 'explainab' in text_lower or 'explicab' in text_lower:
        algorithms.append("[[Explicabilidade_XAI]]")
        
    return sorted(list(set(scales))), sorted(list(set(algorithms)))

def main():
    excel_path = os.path.join("03_selecao_triagem", "02_triagem_resumo", "artigos_incluidos_leitura_completa.xlsx")
    output_dir = os.path.join("04_extracao_dados", "estudos")
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Lendo base consolidada: {excel_path}")
    df = pd.read_excel(excel_path)
    print(f"Total de artigos para geração: {len(df)}")
    
    generated_files = []
    
    for idx, row in df.iterrows():
        study_id = str(row['Study_ID']).strip()
        title_raw = str(row['Title']).strip() if pd.notna(row['Title']) else f"Sem Título {study_id}"
        # limpar aspas e quebras de linha no título
        title_clean = title_raw.replace('\n', ' ').replace('\r', ' ')
        title_clean = re.sub(r'\s+', ' ', title_clean).strip()
        
        authors_list = parse_authors(row['Authors'])
        authors_display = ", ".join(authors_list) if authors_list else "Não informado"
        
        year = int(row['Year']) if pd.notna(row['Year']) else "N/D"
        venue = str(row['Venue']).strip() if pd.notna(row['Venue']) else "Não informado"
        database = str(row['Source_Database']).strip() if pd.notna(row['Source_Database']) else "Desconhecida"
        sources = str(row['Sources']).strip() if pd.notna(row['Sources']) else database
        doi = str(row['DOI']).strip() if pd.notna(row['DOI']) else ""
        url = str(row['URL']).strip() if pd.notna(row['URL']) else ""
        abstract = str(row['Abstract']).strip() if pd.notna(row['Abstract']) else "Resumo não disponível na base de origem."
        reason = str(row['Reason']).strip() if pd.notna(row['Reason']) else ""
        pop_scope = str(row['Population_Scope']).strip() if pd.notna(row['Population_Scope']) else "Educação Básica"
        interv_scope = str(row['Intervention_Scope']).strip() if pd.notna(row['Intervention_Scope']) else "Modelos Preditivos / Psicométricos"
        outc_scope = str(row['Outcome_Scope']).strip() if pd.notna(row['Outcome_Scope']) else "Recusa Escolar / Absenteísmo Crônico"
        keywords = str(row['Keywords']).strip() if pd.notna(row['Keywords']) else ""
        
        # Detecção de conceitos e tags
        full_text = f"{title_clean} {abstract} {keywords} {interv_scope} {outc_scope}"
        scales_detected, algos_detected = detect_concepts(full_text)
        
        # Mapeamento de RQs
        rqs = ["[[RQ4_Metricas_e_Desafios|RQ4]]"] # Todas são avaliadas em QA e Métricas
        if "Psicométric" in interv_scope or scales_detected or "escala" in full_text.lower():
            rqs.append("[[RQ1_Instrumentos_Psicometricos|RQ1]]")
        if "Machine Learning" in interv_scope or "Modelos" in interv_scope or algos_detected:
            rqs.append("[[RQ2_Modelos_IA_e_Predicao|RQ2]]")
        # Quase todos os preditivos com dados escolares/pessoais analisam variáveis contextuais/socioemocionais
        rqs.append("[[RQ3_Variaveis_Socioemocionais|RQ3]]")
        rqs = sorted(list(set(rqs)))
        
        # Tags Obsidian
        db_tag = f"base/{database.lower().replace(' ', '_').replace('.', '')}"
        tags = ["rsl/estudo", "rsl/fase2_leitura_completa", db_tag]
        if "recusa" in outc_scope.lower() or "ebsa" in outc_scope.lower():
            tags.append("fenomeno/recusa_escolar")
        if "absenteísmo" in outc_scope.lower() or "abandono" in outc_scope.lower() or "evasão" in outc_scope.lower():
            tags.append("fenomeno/absenteismo_cronico")
            
        # Nome do arquivo
        sanitized_title = sanitize_filename(title_clean)
        filename = f"{study_id} - {sanitized_title}.md"
        filepath = os.path.join(output_dir, filename)
        
        # DOI formatado com link
        doi_link = f"[{doi}](https://doi.org/{doi})" if doi and doi != "nan" else "Não informado"
        url_link = f"[Link da Publicação]({url})" if url and url != "nan" else "Não informado"
        
        # Montar YAML Frontmatter manualmente para manter formatação limpa e compatível com Obsidian Properties
        yaml_lines = [
            "---",
            f"id: {study_id}",
            f"study_id: {study_id}",
            f'title: "{title_clean.replace(chr(34), chr(92)+chr(34))}"',
            f"year: {year}",
            f'database: "{database}"',
            f'venue: "{venue.replace(chr(34), chr(92)+chr(34))}"',
            f'doi: "{doi}"',
            f'url: "{url}"',
            'status: "Pendente Leitura Completa"',
            "qa_score: 0",
            f'population_scope: "{pop_scope}"',
            f'intervention_scope: "{interv_scope}"',
            f'outcome_scope: "{outc_scope}"',
            "authors:"
        ]
        for a in (authors_list if authors_list else ["Não informado"]):
            yaml_lines.append(f'  - "{a}"')
            
        yaml_lines.append("rqs:")
        for r in rqs:
            yaml_lines.append(f'  - "{r}"')
            
        yaml_lines.append("scales:")
        for s in scales_detected:
            yaml_lines.append(f'  - "{s}"')
            
        yaml_lines.append("algorithms:")
        for alg in algos_detected:
            yaml_lines.append(f'  - "{alg}"')
            
        yaml_lines.append("tags:")
        for t in tags:
            yaml_lines.append(f"  - {t}")
        yaml_lines.append("---\n")
        
        yaml_content = "\n".join(yaml_lines)
        
        # Corpo da nota
        body = f"""# {study_id}: {title_clean}

> [!INFO] Metadados Rápidos
> - **ID do Estudo:** `{study_id}`
> - **Autores:** {authors_display}
> - **Ano:** {year}
> - **Veículo (Venue):** *{venue}*
> - **Base de Origem:** `{database}` (Bases: `{sources}`)
> - **DOI:** {doi_link}
> - **URL:** {url_link}
> - **Status da Extração:** `Pendente Leitura Completa`

---

## Resumo (Abstract)
> [!ABSTRACT] Resumo do Artigo
> {abstract}

---

## Escopos e Elegibilidade na Triagem (Fase 1)
- **Populacao (Population Scope):** {pop_scope}
- **Intervencao/Tecnologia (Intervention Scope):** {interv_scope}
- **Desfecho (Outcome Scope):** {outc_scope}
- **Criterios de Inclusao:** `IC1, IC2, IC4`
- **Motivo da Inclusao:**
  > {reason}

---

## 1. Identificacao e Metadados Detalhados
- **ID do Estudo:** `{study_id}`
- **Titulo Completo:** {title_clean}
- **Autores:** {authors_display}
- **Ano de Publicacao:** {year}
- **Tipo de Publicacao:** Periodico / Conferencia
- **Nome do Veiculo:** {venue}
- **DOI:** {doi_link}
- **Base de Dados:** {database}
- **Pais/Regiao de Realizacao do Estudo:** *(Preencher durante leitura completa)*

---

## 2. Caracterizacao da Populacao e Contexto (PICOC)
- **Nivel Educacional:** {pop_scope}
- **Faixa Etaria / Amostra ($N$):** *(Ex: N = 1.250 estudantes, 12-16 anos)*
- **Publico-alvo Avaliado:** {outc_scope}
- **Fonte dos Dados / Dataset:** *(Ex: Sistema de Gestao Escolar, registros clinicos, questionarios)*

---

## 3. Extracao Orientada as Questoes de Pesquisa (RQs)

### [[RQ1_Instrumentos_Psicometricos|RQ1: Ferramentas, Escalas ou Instrumentos Psicometricos]]
- **Nome do Instrumento/Escala:** {", ".join(scales_detected) if scales_detected else "*(Identificar na leitura ou N/A)*"}
- **Natureza da Ferramenta:** (Instrumento psicometrico tradicional / Escala clinica / Ferramenta digitalizada / Questionario de triagem)
- **Forma de Aplicacao:** (Autorrelato do aluno / Relato dos pais / Relato dos professores / Entrevista clinica)
- **Finalidade:** (Diagnostico diferencial / Triagem inicial / Avaliacao de evolucao)

### [[RQ2_Modelos_IA_e_Predicao|RQ2: Abordagens Computacionais e de Inteligencia Artificial]]
- **Tipo de Abordagem:** (Machine Learning Supervisionado / Nao Supervisionado / Deep Learning / Early Warning System - EWS / Analise Estatistica Avancada / XAI)
- **Algoritmos Empregados:** {", ".join(algos_detected) if algos_detected else "*(Identificar na leitura ou N/A)*"}
- **Tarefa do Modelo:** (Classificacao binaria [risco sim/nao] / Regressao [probabilidade de infrequencia] / Clustering [perfis de comportamento])
- **Estagio de Deteccao:** (Alerta precoce / deteccao preventiva vs. diagnostico a posteriori)

### [[RQ3_Variaveis_Socioemocionais|RQ3: Variaveis e Features Consideradas]]
- **Variaveis Psicologicas/Socioemocionais:** (Ansiedade de separacao, ansiedade social, depressao, estresse, regulacao emocional, somatizacao)
- **Variaveis Comportamentais / Historico:** (Padrao de faltas/atrasos, historico de notas, engajamento escolar, conflitos, bullying)
- **Variaveis Familiares / Sociodemograficas:** (Estrutura familiar, dinamica parental, renda, historico medico)
- **Variaveis Institucionais / Contextuais:** (Clima escolar, relacao professor-aluno, localizacao da escola)
- **Features Mais Relevantes Identificadas:** (Feature importance / SHAP / coeficientes principais)

### [[RQ4_Metricas_e_Desafios|RQ4: Metricas de Avaliacao, Desempenho e Limitacoes]]
- **Metricas Psicometricas:** (Alfa de Cronbach, Omega de McDonald, Validade convergente/discriminante)
- **Metricas Computacionais (ML):** (Acuracia, Sensibilidade/Recall, Precisao, F1-Score, AUC-ROC, MCC)
- **Estrategia de Validacao:** (K-Fold Cross-validation, split temporal treino/teste, validacao externa)
- **Desafios Metodologicos Relatados:** (Desbalanceamento de classes, dados faltantes/ruidosos, tamanho restrito da amostra)
- **Aspectos Eticos e Transparencia (XAI):** (Privacidade dos dados dos alunos, interpretabilidade do modelo, mitigacao de vies)
- **Limitacoes Declaradas:** 
- **Direcoes Futuras:** 

---

## 4. Avaliacao de Qualidade Metodologica (QA)
*Criterios de pontuacao: `2` = Atende totalmente; `1` = Atende parcialmente; `0` = Nao atende.*

| Criterio | Avaliacao | Nota (0-2) | Justificativa / Trecho do Artigo |
|:---|:---|:---:|:---|
| **QA1 (Clareza do Objetivo)** | O objetivo do estudo ou o desenvolvimento da ferramenta esta claramente definido? | 0 | |
| **QA2 (Rigor Metodologico)** | Metodologia de coleta de dados, amostra ou arquitetura do modelo descrita de forma replicavel? | 0 | |
| **QA3 (Validacao e Desempenho)** | Apresenta metricas claras de validacao (Acuracia, F1, Cronbach, etc.)? | 0 | |
| **QA4 (Fatores Socioemocionais)** | Ha analise aprofundada dos fatores psicologicos ou contextuais associados a recusa escolar? | 0 | |
| **QA5 (Limitacoes e Vies)** | Os autores discutem limitacoes metodologicas, restricoes da amostra ou vieses? | 0 | |
| **TOTAL** | **Pontuacao de Rigor Metodologico** | **/ 10** | |

---

## 5. Anotacoes Pessoais e Insights do Pesquisador (Matheus Medeiros)
- 

---

## Navegacao e Conexoes
- **MOC Geral:** [[00_INDEX|Mapa de Conteudo da RSL]]
- **Formulario Base de Extracao:** [[04_extracao_dados/formulario_extracao|Formulario de Extracao]]
- **Protocolo de Pesquisa:** [[01_protocolo/protocolo_rsl|Protocolo RSL]]
- **Checklist PRISMA 2020:** [[PRISMA/checklist_prisma_2020_status|Status do PRISMA]]
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(yaml_content + body)
            
        generated_files.append({
            "study_id": study_id,
            "filename": filename,
            "title": title_clean,
            "year": year,
            "database": database,
            "authors": authors_display,
            "scopes": f"{pop_scope} | {interv_scope}"
        })
        
    print(f"Sucesso! Geradas {len(generated_files)} notas em: {output_dir}")
    
    # Salvar índice json/csv para uso posterior
    index_df = pd.DataFrame(generated_files)
    index_df.to_csv("04_extracao_dados/indice_estudos_gerados.csv", index=False, encoding="utf-8")
    print("Salvo arquivo de índice: 04_extracao_dados/indice_estudos_gerados.csv")

if __name__ == "__main__":
    main()
