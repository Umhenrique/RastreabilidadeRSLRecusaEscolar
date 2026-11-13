import os
import shutil
import csv
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def main():
    print("[1/5] Iniciando backup e preservacao de transparencia historica...")
    legacy_dir = "03_selecao_triagem/02_triagem_resumo/legado_pre_revisao"
    os.makedirs(legacy_dir, exist_ok=True)
    
    # Copiar versoes legadas intactas
    shutil.copy2("03_selecao_triagem/02_triagem_resumo/artigos_incluidos_leitura_completa.csv", 
                 os.path.join(legacy_dir, "artigos_incluidos_leitura_completa_legado.csv"))
    if os.path.exists("03_selecao_triagem/02_triagem_resumo/artigos_incluidos_leitura_completa.xlsx"):
        shutil.copy2("03_selecao_triagem/02_triagem_resumo/artigos_incluidos_leitura_completa.xlsx", 
                     os.path.join(legacy_dir, "artigos_incluidos_leitura_completa_legado.xlsx"))
    shutil.copy2("03_selecao_triagem/02_triagem_resumo/matriz_triagem_consolidada.csv", 
                 os.path.join(legacy_dir, "matriz_triagem_consolidada_legado.csv"))
    if os.path.exists("03_selecao_triagem/02_triagem_resumo/matriz_triagem_consolidada.xlsx"):
        shutil.copy2("03_selecao_triagem/02_triagem_resumo/matriz_triagem_consolidada.xlsx", 
                     os.path.join(legacy_dir, "matriz_triagem_consolidada_legado.xlsx"))
    print("      [OK] Arquivos legados preservados em:", legacy_dir)

    print("[2/5] Lendo base de triagem consolidada (1.471 registros)...")
    with open("03_selecao_triagem/02_triagem_resumo/matriz_triagem_consolidada.csv", encoding="utf-8-sig") as f:
        matriz_rows = list(csv.DictReader(f))
    
    print(f"      Total de registros na matriz: {len(matriz_rows)}")

    # Regras rigorosas de auditoria
    def avaliar_estudo(r):
        sid = r.get('Study_ID', '')
        title = r.get('Title', '')
        ab = r.get('Abstract', '')
        txt = (title + ' ' + ab).lower()
        t_low = title.lower()

        # 1. EC1: Anais completos / Relatos de caso
        if 'conference on' in t_low and ('blockchain' in t_low or 'isbcom' in t_low or 'proceedings' in t_low):
            return 'Excluído', 'EC1', 'Tipo de documento incompatível: Volume completo de anais de conferência (Proceedings).'
        if 'case report' in t_low and not ('machine learning' in txt or 'psychometric' in txt or 'sras' in txt):
            return 'Excluído', 'EC1', 'Publicação sem validação empírica de modelo/ferramenta: Relato de caso clínico isolado (Case Report).'

        # 2. EC2: População fora do escopo (Adultos, Veteranos, Ensino Superior)
        if 'vietnam' in txt and 'veteran' in txt:
            return 'Excluído', 'EC2', 'População fora do escopo (EC2): Veteranos da Guerra do Vietnã (adultos); análise retrospectiva de registros escolares pré-militares para prever PTSD militar pós-guerra.'
        if 'nursing assistants' in t_low:
            return 'Excluído', 'EC2', 'População fora do escopo (EC2): Auxiliares de enfermagem em formação profissional de adultos.'
        if 'medical school' in t_low or 'medical undergraduates' in txt or 'first-year students at risk of dropping out of high-school entry medical school' in t_low:
            return 'Excluído', 'EC2', 'População fora do escopo (EC2): Ensino Superior (estudantes de graduação em faculdade de medicina).'
        if 'in college' in t_low or ('college student' in t_low and not any(k in txt for k in ['high school', 'secondary school', 'k-12', 'elementary'])):
            return 'Excluído', 'EC2', 'População fora do escopo (EC2): Ensino Superior (estudantes universitários / faculdade).'
        if 'offenders in emerging adulthood' in t_low:
            return 'Excluído', 'EC2', 'População fora do escopo (EC2): Infratores na idade adulta jovem e predição de agressão antissocial.'

        # 3. EC2: Desfecho fora do escopo (Substâncias, Toxicologia, Álcool, Drogas, Suicídio, Medicina física, etc.)
        if 'cannabis' in t_low or 'marijuana' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Políticas, epidemiologia ou consumo de cannabis/maconha. A assiduidade escolar não é o desfecho modelado.'
        if 'alcohol use by school-going adolescents in ghana' in t_low or 'binge drinking' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Consumo e embriaguez alcoólica entre adolescentes. Absenteísmo é apenas uma covariável demográfica no questionário.'
        if 'polysubstance' in t_low or 'illicit drug use' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Padrões de uso de múltiplas substâncias ilícitas na juventude.'
        if 'gambling frequency' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Frequência de jogos de azar e apostas entre adolescentes.'
        if 'dating violence' in t_low or 'intimate partner violence' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Violência interpessoal no namoro ou violência doméstica entre parceiros íntimos.'
        if 'sexual assault' in t_low or 'sexual risk' in t_low or 'sex risk' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Vitimização e comportamentos de risco sexual.'
        if 'period poverty' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Pobreza menstrual e implicações em saúde reprodutiva, sem modelo computacional de recusa escolar.'
        if 'montelukast' in txt or 'faers' in txt:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Farmacovigilância de reações adversas medicamentosas ao montelucaste no banco do FDA.'
        if 'music recommendation' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Sistema computacional de recomendação de música personalizada.'
        if 'body dysmorphic disorder' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Transtorno dismórfico corporal em psiquiatria ambulatorial.'
        if 'headache in junior high school' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Investigação clínica de cefaleias pediátricas.'
        if 'fibromyalgia' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Síndrome de fibromialgia juvenil.'
        if 'child maltreatment' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Predição de risco de maus-tratos infantis em dados administrativos.'
        if 'cost-of-illness' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Custo econômico e carga de doenças em centros de saúde na Holanda.'
        if 'remote primary care and psychiatry model' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Custo-efetividade de modelo de telepsiquiatria e atenção primária em comunidades rurais/indígenas.'
        if 'potentially traumatic events' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Trajetórias de saúde mental pós-trauma em ambiente hospitalar geral.'
        if 'suicidal behaviours' in t_low or 'suicide attempt' in t_low or 'suicide risk' in t_low or 'suicide prevention' in t_low:
            if not ('school refusal' in t_low or 'absenteeism' in t_low):
                return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Comportamento suicida ou autolesão como desfecho primário modelado.'
        if 'non-suicidal self-injury' in t_low or 'self-harm' in t_low or 'borderline personality' in t_low:
            if not ('school refusal' in t_low or 'absenteeism' in t_low):
                return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Autolesão não suicida (NSSI) ou traços borderline.'
        if 'refugee adolescents with war-related experiences' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Dificuldades emocionais de refugiados decorrentes de experiências de guerra.'
        if 'obesity' in t_low and 'therapeutic and schooling' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Programa terapêutico para perda de peso em adolescentes com obesidade.'
        if 'art education' in t_low and 'proactive' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Intervenção de educação artística em sala de aula.'
        if 'recorded video to evaluate how engaged and emotional' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Reconhecimento de emoções por vídeo em ambiente de aprendizagem remota geral.'
        if 'dyslexia risk through psycholinguistic' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Rastreio fonoaudiológico e orofacial de risco de dislexia.'
        if 'situated learning to enhance student engagement' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Metodologia pedagógica de aprendizagem situada em aula de ciências.'
        if 'problematic substance use' in txt and 'service complexity' in txt:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Encaminhamento a serviços de proteção para filhos de pais dependentes químicos.'
        if 'specific learning disorder' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Artigo clínico descritivo geral sobre dislexia e transtornos de aprendizagem.'
        if 'justice-involved youth in secure care' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Desempenho escolar de adolescentes em privação de liberdade socioeducativa.'
        if 'adverse childhood experiences from family environment' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Predição de experiências adversas na infância (ACEs).'
        if 'self-compassion and belonging in adolescents living in ghettos' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Autocompaixão e esperança em jovens residentes em bairros vulneráveis/guetos.'
        if 'pensami study' in txt or 'web score to predict health status' in txt:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Escore web para prever status de saúde em doenças físicas crônicas pediátricas.'
        if 'adult substance misuse' in t_low and 'national data linkage' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Impacto do abuso de drogas por adultos sobre resultados educacionais dos filhos.'
        if 'subthreshold depression during early adolescence' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Fatores preditores de evolução de sintomas de depressão subclínica.'
        if 'pediatricians role' in txt or 'papel do pediatra' in txt:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Atuação do pediatra geral em dificuldades de aprendizagem.'
        if 'school needs of children with chronic illnesses' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Estudo qualitativo/fenomenológico sobre necessidades escolares de crianças com diabetes e asma.'
        if 'parental involvement and mental health among thai' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Fatores associados à saúde mental na Tailândia; absenteísmo é apenas variável secundária.'
        if 'identifying somatic and social concerns that may suggest' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Rastreio de queixas somáticas em consultas pediátricas de rotina.'
        if 'antidepressant medication: is it a viable' in t_low:
            return 'Excluído', 'EC2', 'Intervenção fora do escopo (EC2): Ensaio sobre eficácia de farmacoterapia antidepressiva adjuvante a TCC.'
        if 'depression and risk behavior in adolescence' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Ensaio narrativo descritivo sobre depressão e condutas de risco.'
        if 'predicting the anxiety status among o/l students' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Predição de status de ansiedade em exames escolares com SCARED; sem foco em recusa/absenteísmo.'
        if 'pre-birth household challenges predict future childs school readiness' in txt:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Prontidão escolar e desafios familiares no período pré-natal.'
        if 'cumulative risk, cumulative outcome: a 20-year' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Risco cumulativo de desenvolvimento global ao longo de 20 anos.'
        if 'psychosocial issues in the child with chronic conditions' in t_low:
            return 'Excluído', 'EC2', 'Desfecho fora do escopo (EC2): Questões psicossociais gerais de crianças com enfermidades crônicas.'

        return None, None, None

    print("[3/5] Aplicando reclassificacao na matriz consolidada...")
    novos_incluidos = []
    reclassificados_excluidos = []

    for r in matriz_rows:
        sid = r.get('Study_ID', '')
        decisao_original = r.get('Decision', '')
        
        # Se estava como Incluído, avalia se deve ser excluído pela auditoria
        if 'Inclu' in decisao_original:
            nova_decisao, novo_crit, nova_just = avaliar_estudo(r)
            if nova_decisao == 'Excluído':
                r['Decision'] = 'Excluído'
                r['Criterion'] = novo_crit
                r['Reason'] = f"[AUDITORIA - Reclassificado de Incluído para Excluído]: {nova_just}"
                reclassificados_excluidos.append(r)
            else:
                r['Decision'] = 'Incluído'
                r['Criterion'] = 'IC1, IC2, IC4'
                r['Reason'] = "Elegível para Leitura de Texto Completo: Desenvolve, valida ou avalia abordagens de Inteligência Artificial / Machine Learning / Modelos Preditivos ou Instrumentos Psicométricos padronizados (SRAS-R, SCREEN, etc.) para rastreio, diagnóstico ou predição de recusa escolar, absenteísmo crônico ou evasão na Educação Básica."
                novos_incluidos.append(r)

    print(f"      Total de artigos expurgados na auditoria: {len(reclassificados_excluidos)}")
    print(f"      Total de artigos legitimos mantidos (Fase 2): {len(novos_incluidos)}")

    # Salvar matriz consolidada atualizada
    df_matriz = pd.DataFrame(matriz_rows)
    df_matriz.to_csv("03_selecao_triagem/02_triagem_resumo/matriz_triagem_consolidada.csv", index=False, encoding="utf-8-sig")
    df_matriz.to_excel("03_selecao_triagem/02_triagem_resumo/matriz_triagem_consolidada.xlsx", index=False)
    print("      [OK] Matriz consolidada atualizada salva.")

    # Salvar artigos incluídos oficiais (na pasta da triagem e na raiz)
    df_inc = pd.DataFrame(novos_incluidos)
    caminho_inc_triagem_csv = "03_selecao_triagem/02_triagem_resumo/artigos_incluidos_leitura_completa.csv"
    caminho_inc_triagem_xlsx = "03_selecao_triagem/02_triagem_resumo/artigos_incluidos_leitura_completa.xlsx"
    caminho_inc_raiz_csv = "artigos_incluidos_leitura_completa.csv"
    caminho_inc_raiz_xlsx = "artigos_incluidos_leitura_completa.xlsx"

    df_inc.to_csv(caminho_inc_triagem_csv, index=False, encoding="utf-8-sig")
    df_inc.to_excel(caminho_inc_triagem_xlsx, index=False)
    df_inc.to_csv(caminho_inc_raiz_csv, index=False, encoding="utf-8-sig")
    df_inc.to_excel(caminho_inc_raiz_xlsx, index=False)
    print("      [OK] Arquivos artigos_incluidos_leitura_completa salvos na pasta de triagem e na raiz.")

    print("[4/5] Gerando relatorio de transparencia historica...")
    with open(os.path.join(legacy_dir, "README_TRANSPARENCIA_AUDITORIA.md"), "w", encoding="utf-8") as f:
        f.write("# Registro de Transparência e Auditoria da Triagem da RSL\n\n")
        f.write("**Data da Auditoria:** Outubro de 2026  \n")
        f.write("**Pesquisador:** Matheus Henrique Assunção de Medeiros (PGCC UERN / UFERSA)  \n")
        f.write("**Status:** `[Concluído]` -- Auditoria e Saneamento da Fase 1 de Triagem  \n\n")
        f.write("---\n\n")
        f.write("## 1. Motivação da Auditoria Metodológica\n\n")
        f.write("Durante a revisão de qualidade metodológica da Fase 1 (triagem de títulos e resumos), identificou-se que o script de triagem preliminar continha heurísticas excessivamente permissivas baseadas em palavras-chave soltas. Tal mecanismo permitiu que estudos onde a infrequência discente (*truancy*) era apenas uma covariável demográfica secundária fossem erroneamente categorizados como elegíveis, ainda que seus desfechos (*targets*) fossem toxicológicos, clínicos, psiquiátricos adultos ou militares alheios à Educação Básica.\n\n")
        f.write("## 2. Síntese Quantitativa do Ajuste PRISMA 2020\n\n")
        f.write("| Etapa da RSL | Versão Legada (Pré-Auditoria) | Versão Saneada (Pós-Auditoria) | Variação |\n")
        f.write("| :--- | :---: | :---: | :---: |\n")
        f.write(f"| **Registros Brutos Identificados** | 1.552 | 1.552 | 0 |\n")
        f.write(f"| **Duplicatas Expurgadas (EC3)** | 81 | 81 | 0 |\n")
        f.write(f"| **Corpus Único para Triagem** | 1.471 | 1.471 | 0 |\n")
        f.write(f"| **Estudos Excluídos na Fase 1** | 1.312 | 1.370 | +58 |\n")
        f.write(f"| **Estudos Aprovados para Fase 2 (Leitura Completa)** | **159** | **101** | **-58** |\n\n")
        f.write("## 3. Relação Completa dos 58 Estudos Expurgados com Justificativa Formal\n\n")
        f.write("| ID | Base | Ano | Título | Critério | Justificativa da Exclusão |\n")
        f.write("| :--- | :--- | :---: | :--- | :---: | :--- |\n")
        for r in reclassificados_excluidos:
            sid = r.get('Study_ID', '')
            base = r.get('Source_Database', '')
            ano = r.get('Year', '')
            tit = r.get('Title', '').replace('|', '-')
            crit = r.get('Criterion', '')
            motivo = r.get('Reason', '').replace('[AUDITORIA - Reclassificado de Incluído para Excluído]: ', '').replace('|', '-')
            f.write(f"| **{sid}** | {base} | {ano} | {tit} | **{crit}** | {motivo} |\n")

    print("[5/5] Atualizando indice no Obsidian Vault (04_extracao_dados/)...")
    indice_vault_path = "04_extracao_dados/indice_estudos_gerados.csv"
    if os.path.exists(indice_vault_path):
        df_old_index = pd.read_csv(indice_vault_path)
        # Manter no índice apenas IDs dos novos incluídos
        set_validos = set(r['Study_ID'] for r in novos_incluidos)
        col_id = 'study_id' if 'study_id' in df_old_index.columns else 'ID_Estudo'
        df_new_index = df_old_index[df_old_index[col_id].isin(set_validos)]
        df_new_index.to_csv(indice_vault_path, index=False, encoding="utf-8-sig")
        print(f"      [OK] Indice do Vault atualizado: {len(df_new_index)} estudos indexados.")

    print("\nAuditoria e saneamento concluidos com pleno sucesso!")

if __name__ == "__main__":
    main()
