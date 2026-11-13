# -*- coding: utf-8 -*-
import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_protocol_docx(filepath):
    doc = Document()

    # Configurar idioma padrão do documento para Português do Brasil (pt-BR)
    langs = doc.styles.element.xpath('//w:rPrDefault/w:rPr/w:lang')
    for l in langs:
        l.set(qn('w:val'), 'pt-BR')
        l.set(qn('w:eastAsia'), 'pt-BR')
        l.set(qn('w:bidi'), 'pt-BR')

    normal_style = doc.styles['Normal']
    rPr = normal_style.element.get_or_add_rPr()
    lang_elem = OxmlElement('w:lang')
    lang_elem.set(qn('w:val'), 'pt-BR')
    lang_elem.set(qn('w:eastAsia'), 'pt-BR')
    lang_elem.set(qn('w:bidi'), 'pt-BR')
    rPr.append(lang_elem)

    # Margens padrão A4 (2.5 cm = 1 polegada)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Título Principal (Preto, limpo, sem azul)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("PROTOCOLO DE REVIS\u00c3O SISTEM\u00c1TICA DA LITERATURA")
    run_title.font.name = "Arial"
    run_title.font.size = Pt(14)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0, 0, 0)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = p_sub.add_run(
        "Identifica\u00e7\u00e3o e Predi\u00e7\u00e3o de Recusa Escolar na Educa\u00e7\u00e3o B\u00e1sica:\n"
        "Converg\u00eancia entre Instrumentos Psicom\u00e9tricos e Intelig\u00eancia Artificial"
    )
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(11)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(0, 0, 0)

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_meta = p_meta.add_run(
        "Pesquisador: Matheus Henrique Assun\u00e7\u00e3o de Medeiros\n"
        "Programa de P\u00f3s-Gradua\u00e7\u00e3o em Ci\u00eancia da Computa\u00e7\u00e3o \u2014 PGCC UERN / UFERSA"
    )
    run_meta.font.name = "Arial"
    run_meta.font.size = Pt(10)
    run_meta.font.color.rgb = RGBColor(0, 0, 0)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    def add_section_heading(title_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title_text)
        run.font.name = "Arial"
        run.font.size = Pt(11.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    def add_sub_heading(title_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title_text)
        run.font.name = "Arial"
        run.font.size = Pt(10.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

    def add_body_p(text, bold_prefix=""):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = "Arial"
            r_pre.font.size = Pt(10)
            r_pre.font.bold = True
            r_pre.font.color.rgb = RGBColor(0, 0, 0)
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0, 0, 0)
        return p

    # 1. OBJETIVOS
    add_section_heading("1. Objetivos da Revis\u00e3o")
    add_body_p(
        "Mapear, analisar e sintetizar a literatura cient\u00edfica sobre ferramentas, instrumentos e abordagens "
        "computacionais de Intelig\u00eancia Artificial e Aprendizado de M\u00e1quina utilizadas para o rastreio, "
        "avalia\u00e7\u00e3o, diagn\u00f3stico ou predi\u00e7\u00e3o de recusa escolar e absente\u00edsmo cr\u00f4nico.",
        "1.1 Objetivo Geral: "
    )
    
    add_sub_heading("1.2 Objetivos Espec\u00edficos")
    add_body_p(
        "Identificar instrumentos psicom\u00e9tricos, escalas e ferramentas tradicionais empregados no diagn\u00f3stico "
        "cl\u00ednico ou educacional da recusa escolar.",
        "1. "
    )
    add_body_p(
        "Investigar o uso de modelos de Intelig\u00eancia Artificial, Aprendizado de M\u00e1quina e sistemas de alerta "
        "precoce aplicados \u00e0 tem\u00e1tica.",
        "2. "
    )
    add_body_p(
        "Analisar as principais m\u00e9tricas de desempenho, valida\u00e7\u00e3o e limita\u00e7\u00f5es das ferramentas "
        "descritas na literatura.",
        "3. "
    )
    add_body_p(
        "Identificar lacunas de pesquisa atuais para orientar futuros desenvolvimentos tecnol\u00f3gicos na \u00e1rea.",
        "4. "
    )

    # 2. ESTRUTURA PICOC
    add_section_heading("2. Estrutura do Estudo (Crit\u00e9rio PICOC)")
    
    table_picoc = doc.add_table(rows=1, cols=2)
    table_picoc.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table_picoc.rows[0].cells
    hdr[0].text = "Elemento"
    hdr[1].text = "Defini\u00e7\u00e3o no Estudo"
    for cell in hdr:
        set_cell_background(cell, "F2F2F2")
        p = cell.paragraphs[0]
        p.runs[0].font.name = "Arial"
        p.runs[0].font.size = Pt(10)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(0, 0, 0)
        set_cell_margins(cell, top=80, bottom=80, left=120, right=120)

    picoc_data = [
        ("Population", "Ensino B\u00e1sico"),
        ("Intervention", "Ferramentas diagn\u00f3sticas e preditivas baseadas em Intelig\u00eancia Artificial"),
        ("Outcomes", "Recusa escolar ou evas\u00e3o escolar associada a fatores socioemocionais")
    ]

    for elem, desc in picoc_data:
        row = table_picoc.add_row().cells
        row[0].text = elem
        row[1].text = desc
        for i, c in enumerate(row):
            set_cell_background(c, "FFFFFF")
            p = c.paragraphs[0]
            p.runs[0].font.name = "Arial"
            p.runs[0].font.size = Pt(9.5)
            p.runs[0].font.color.rgb = RGBColor(0, 0, 0)
            if i == 0: p.runs[0].font.bold = True
            set_cell_margins(c, top=60, bottom=60, left=100, right=100)

    # 3. QUESTÕES DE PESQUISA (RQs)
    add_section_heading("3. Quest\u00f5es de Pesquisa")
    add_body_p(
        "Quais s\u00e3o as ferramentas, escalas ou instrumentos psicom\u00e9tricos utilizados para diagnosticar ou "
        "rastrear a recusa escolar e o absente\u00edsmo cr\u00f4nico?",
        "RQ1: "
    )
    add_body_p(
        "De que forma t\u00e9cnicas de Intelig\u00eancia Artificial, Aprendizado de M\u00e1quina e an\u00e1lise de dados "
        "t\u00eam sido aplicadas na predi\u00e7\u00e3o ou detec\u00e7\u00e3o precoce da recusa escolar?",
        "RQ2: "
    )
    add_body_p(
        "Quais vari\u00e1veis socioemocionais, comportamentais ou contextuais s\u00e3o mais frequentemente consideradas "
        "por essas ferramentas preditivas e diagn\u00f3sticas?",
        "RQ3: "
    )
    add_body_p(
        "Quais s\u00e3o as principais limita\u00e7\u00f5es, desafios metodol\u00f3gicos e m\u00e9tricas de avalia\u00e7\u00e3o "
        "relatados nos estudos ao implementar essas ferramentas?",
        "RQ4: "
    )

    # 4. ESTRATÉGIA DE BUSCA
    add_section_heading("4. Estrat\u00e9gia de Busca")
    add_sub_heading("4.1 Bases de Dados Selecionadas")
    add_body_p("Scopus, IEEE Xplore, ACM Digital Library, ScienceDirect, Springer Link e Web of Science.")

    add_sub_heading("4.2 Crit\u00e9rios de Idioma e Formato")
    add_body_p("Ingl\u00eas, Portugu\u00eas e Espanhol.", "Idiomas: ")
    add_body_p("Artigos de peri\u00f3dicos e anais de confer\u00eancias cient\u00edficas revisados por pares.", "Tipo de publica\u00e7\u00e3o: ")

    add_sub_heading("4.3 Estrutura Booleana de Busca")
    add_body_p(
        "A busca formal combina tr\u00eas blocos conceituais mediante o operador booleano AND: "
        "Fen\u00f4meno de Infrequ\u00eancia AND Dimens\u00e3o Socioemocional AND Intelig\u00eancia Artificial e Modelos Preditivos."
    )

    # 5. CRITÉRIOS DE ELEGIBILIDADE (IC / EC)
    add_section_heading("5. Crit\u00e9rios de Elegibilidade")
    
    add_sub_heading("5.1 Crit\u00e9rios de Inclus\u00e3o (IC)")
    add_body_p(
        "Artigos originais de pesquisa revisados por pares publicados em peri\u00f3dicos cient\u00edficos e anais de confer\u00eancias.",
        "IC1: "
    )
    add_body_p(
        "Estudos que abordem o desenvolvimento, valida\u00e7\u00e3o, aplica\u00e7\u00e3o ou revis\u00e3o de ferramentas "
        "diagn\u00f3sticas, triagem ou predi\u00e7\u00e3o voltadas \u00e0 recusa escolar, absente\u00edsmo cr\u00f4nico ou evas\u00e3o associada.",
        "IC2: "
    )
    add_body_p("Publica\u00e7\u00f5es redigidas em ingl\u00eas, portugu\u00eas ou espanhol.", "IC3: ")
    add_body_p(
        "Trabalhos que apresentem dados emp\u00edricos, arquiteturas computacionais ou valida\u00e7\u00e3o formal relevante ao escopo.",
        "IC4: "
    )

    add_sub_heading("5.2 Crit\u00e9rios de Exclus\u00e3o (EC)")
    add_body_p(
        "Literatura cinzenta n\u00e3o validada, anais completos sem artigos desagrupados, editoriais, cartas ou resumos estendidos sem dados completos.",
        "EC1: "
    )
    add_body_p(
        "Estudos focados exclusivamente na evas\u00e3o escolar por motivos socioecon\u00f4micos ou estruturais sem rela\u00e7\u00e3o com o comportamento de recusa escolar ou fatores socioemocionais.",
        "EC2: "
    )
    add_body_p("Trabalhos duplicados nas bases de dados, mantendo-se a vers\u00e3o mais completa.", "EC3: ")
    add_body_p(
        "Artigos cujo texto completo n\u00e3o esteja acess\u00edvel mesmo ap\u00f3s busca institucional ou contato com os autores.",
        "EC4: "
    )

    # 6. CRITÉRIOS DE AVALIAÇÃO DE QUALIDADE (QA)
    add_section_heading("6. Avalia\u00e7\u00e3o de Qualidade Metodol\u00f3gica")
    add_body_p("Pontua\u00e7\u00e3o por crit\u00e9rio: 2 = Atende totalmente; 1 = Atende parcialmente; 0 = N\u00e3o atende. Total m\u00e1ximo: 10 pontos.")
    add_body_p("O objetivo do estudo e a ferramenta proposta est\u00e3o claramente definidos?", "QA1: ")
    add_body_p(
        "A metodologia de coleta de dados, a sele\u00e7\u00e3o da amostra e a arquitetura do modelo est\u00e3o descritas de forma replic\u00e1vel?",
        "QA2: "
    )
    add_body_p("O estudo apresenta m\u00e9tricas objetivas de valida\u00e7\u00e3o da ferramenta?", "QA3: ")
    add_body_p("H\u00e1 an\u00e1lise de fatores socioemocionais ou psicol\u00f3gicos associados \u00e0 recusa escolar?", "QA4: ")
    add_body_p(
        "Os autores discutem claramente as limita\u00e7\u00f5es metodol\u00f3gicas, restri\u00e7\u00f5es da amostra ou potenciais vieses da abordagem?",
        "QA5: "
    )

    doc.save(filepath)
    print(f"Documento DOCX salvo com sucesso em: {filepath}")

if __name__ == "__main__":
    create_protocol_docx("review protocol.docx")
    create_protocol_docx("01_protocolo/review protocol.docx")
