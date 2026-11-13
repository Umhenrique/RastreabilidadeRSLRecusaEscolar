import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Relatório Técnico de RSL - Mestrado</title>
<style>
  @page {
    size: A4;
    margin: 16mm 14mm 16mm 14mm;
    @bottom-right {
      content: counter(page);
    }
  }
  
  body {
    font-family: "Times New Roman", Times, "Liberation Serif", serif;
    font-size: 9.5pt;
    line-height: 1.25;
    color: #111;
    margin: 0;
    padding: 0;
    text-align: justify;
  }

  .header-journal {
    font-size: 7.8pt;
    font-style: italic;
    color: #444;
    border-bottom: 0.5pt solid #888;
    padding-bottom: 3px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
  }

  .title-area {
    text-align: center;
    margin-bottom: 12px;
  }

  h1.paper-title {
    font-size: 16pt;
    font-weight: bold;
    margin: 0 0 6px 0;
    line-height: 1.18;
    color: #111;
  }

  .authors {
    font-size: 10pt;
    margin-bottom: 3px;
    font-weight: 500;
  }

  .affiliation {
    font-size: 8.2pt;
    font-style: italic;
    color: #333;
    margin-bottom: 12px;
  }

  .abstract-box {
    margin: 0 15px 12px 15px;
    font-size: 8.6pt;
    line-height: 1.24;
    background-color: #f8f9fa;
    border-left: 2.5pt solid #1f497d;
    padding: 7px 11px;
  }

  .abstract-box strong {
    font-weight: bold;
  }

  .keywords {
    margin-top: 4px;
    font-size: 8.2pt;
  }

  /* Two Column Layout */
  .columns {
    column-count: 2;
    column-gap: 6.5mm;
    column-rule: 0.3pt solid #e0e0e0;
  }

  h2.section-title {
    font-size: 9.8pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-top: 9px;
    margin-bottom: 3px;
    border-bottom: 0.5pt solid #333;
    padding-bottom: 1px;
    break-after: avoid;
  }

  h3.subsection-title {
    font-size: 9.1pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 6px;
    margin-bottom: 2px;
    break-after: avoid;
  }

  p {
    margin-top: 0;
    margin-bottom: 4.5px;
    text-indent: 1.2em;
  }

  p.no-indent {
    text-indent: 0;
  }

  ul, ol {
    margin-top: 2px;
    margin-bottom: 5px;
    padding-left: 1.2em;
  }

  li {
    margin-bottom: 2px;
    font-size: 9pt;
  }

  /* Tables */
  .table-container {
    width: 100%;
    margin: 7px 0;
    break-inside: avoid;
  }

  .full-width {
    column-span: all;
    margin: 10px 0;
  }

  table.academic-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.6pt;
    line-height: 1.18;
  }

  table.academic-table th {
    border-top: 1.5pt solid #000;
    border-bottom: 1pt solid #000;
    font-weight: bold;
    padding: 3.5px 4.5px;
    text-align: left;
    background-color: #f2f5f9;
  }

  table.academic-table td {
    padding: 3px 4.5px;
    border-bottom: 0.4pt solid #ddd;
    vertical-align: top;
  }

  table.academic-table tr:last-child td {
    border-bottom: 1.5pt solid #000;
  }

  .tag-inc {
    font-weight: bold;
    color: #274e13;
    background: #d9ead3;
    padding: 1px 4px;
    border-radius: 2px;
    display: inline-block;
  }

  .tag-exc {
    color: #783f04;
    background: #fce5cd;
    padding: 1px 4px;
    border-radius: 2px;
    display: inline-block;
  }

  /* PRISMA Diagram Box */
  .prisma-box {
    border: 1pt solid #1f497d;
    background-color: #fafbfc;
    padding: 8px 12px;
    border-radius: 4px;
    margin: 8px 0;
    font-size: 8.2pt;
    break-inside: avoid;
  }

  .prisma-step {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 4px 6px;
    margin: 3px 0;
    border-radius: 3px;
  }

  .step-id { background: #e8f0fe; border-left: 3pt solid #1a73e8; }
  .step-dedup { background: #f1f3f4; border-left: 3pt solid #5f6368; }
  .step-screen { background: #e6f4ea; border-left: 3pt solid #188038; }
  .step-elig { background: #fef7e0; border-left: 3pt solid #f29900; }
  .step-inc { background: #ceead6; border-left: 3pt solid #137333; font-weight: bold; }

  /* References */
  .references {
    font-size: 7.8pt;
    line-height: 1.22;
  }
  .references p {
    text-indent: -1.4em;
    padding-left: 1.4em;
    margin-bottom: 3.5px;
  }
</style>
</head>
<body>

<div class="header-journal">
  <span>RELATÓRIO TÉCNICO DE CONDUÇÃO DE PESQUISA DE MESTRADO</span>
  <span>OUTUBRO DE 2026 — FLUXO PRISMA 2020 CONSOLIDADO</span>
</div>

<div class="title-area">
  <h1 class="paper-title">Ferramentas Computacionais, Inteligência Artificial e Instrumentos Diagnósticos para Recusa Escolar e Absenteísmo Crônico na Educação Básica: Relatório Consolidado de Triagem da RSL</h1>
  <div class="authors">Matheus Santos</div>
  <div class="affiliation">Programa de Pós-Graduação em Ciência da Computação / Informática • E-mail: matheus@universidade.edu.br</div>
</div>

<div class="abstract-box">
  <strong>Resumo</strong>— A recusa escolar e o absenteísmo crônico configuram fenômenos biopsicossociais complexos com profundas consequências para a trajetória educacional e a saúde mental infanto-juvenil. Esta pesquisa conduz uma Revisão Sistemática da Literatura (RSL) formal segundo as diretrizes de Kitchenham & Charters (2007) e o padrão internacional PRISMA 2020, investigando a convergência entre abordagens computacionais (Inteligência Artificial, Machine Learning e Sistemas de Alerta Precoce) e instrumentos psicométricos diagnósticos na Educação Básica (K-12). Este relatório consolida os resultados da busca abrangente executada em seis bases acadêmicas internacionais: ACM Digital Library (198), IEEE Xplore (14), ScienceDirect (62), Scopus (195), Springer Link (1.000) e Web of Science Core Collection (83), totalizando <strong>1.552 registros brutos</strong>. A etapa automatizada de deduplicação inter-bases eliminou <strong>81 duplicatas</strong> (Critério EC3), gerando um corpus de <strong>1.471 registros únicos</strong>. A triagem sistemática de título e resumo (Fase 1) selecionou <strong>159 estudos científicos de alta aderência temática</strong> para avaliação em texto completo (Fase 2), excluindo 1.312 publicações fora do escopo. Os resultados evidenciam a maturidade de algoritmos supervisionados (Random Forest, Redes Neurais Convolucionais e Ensembles) associados a escalas clínicas consagradas (SCARED, SRAS-R, SCREEN) para a detecção precoce do absenteísmo escolar e intervenção oportuna.
  <div class="keywords"><strong>Palavras-chave:</strong> Recusa Escolar, Absenteísmo Crônico, Inteligência Artificial, Machine Learning, Sistemas de Alerta Precoce, Instrumentos Psicométricos, PRISMA 2020, Triagem Sistemática.</div>
</div>

<div class="columns">

<h2 class="section-title">1. Introdução e Justificativa</h2>
<p>A não frequência discente sustentada manifesta-se historicamente sob duas naturezas etiológicas fundamentais: a evasão de origem socioeconômica estrutural (associada à necessidade precoce de ingresso no mercado de trabalho ou carências de infraestrutura básica) e a <em>recusa escolar</em> (<em>school refusal</em> / <em>school avoidance</em>), caracterizada por sofrimento psicológico, fobia escolar, ansiedade de separação e dificuldades de regulação socioemocional. Enquanto a evasão tradicional tem sido objeto primordial de políticas assistenciais governamentais, a recusa escolar exige detecção precoce, métodos diagnósticos e intervenções pedagógicas e psicológicas tempestivas.</p>

<p>O crescimento da digitalização dos registros acadêmicos e a evolução das técnicas de Ciência de Dados e Inteligência Artificial (IA) impulsionaram o desenvolvimento de <em>Early Warning Systems</em> (EWS) e modelos preditivos de <em>Machine Learning</em> (ML) voltados à sinalização precoce do risco de desengajamento escolar. Todavia, nota-se uma nítida desconexão na literatura científica: pesquisas de computação frequentemente operam com dados administrativos agregados sem considerar construtos socioemocionais validados, ao passo que a literatura clínica da Psicologia e Psiquiatria da Infância raramente explora a escalabilidade dos algoritmos contemporâneos.</p>

<p>O presente projeto de mestrado preenche essa lacuna através de uma Revisão Sistemática da Literatura (RSL) formal e auditável, estruturada no fluxo metodológico PRISMA 2020.</p>

<h2 class="section-title">2. Protocolo Metodológico da RSL</h2>
<p class="no-indent">O enquadramento da investigação delineia-se estritamente conforme o critério PICOC (Tabela I) e quatro Questões de Pesquisa (RQs):</p>
<ul>
  <li><strong>RQ1:</strong> <em>Quais ferramentas, escalas ou instrumentos psicométricos são utilizados para diagnosticar ou rastrear a recusa escolar e o absenteísmo crônico?</em></li>
  <li><strong>RQ2:</strong> <em>De que forma técnicas de Inteligência Artificial e Machine Learning têm sido aplicadas na predição ou detecção precoce da recusa escolar?</em></li>
  <li><strong>RQ3:</strong> <em>Quais variáveis socioemocionais, comportamentais ou contextuais são mais frequentemente consideradas por essas ferramentas?</em></li>
  <li><strong>RQ4:</strong> <em>Quais são as principais limitações, desafios metodológicos e métricas de avaliação relatados nos estudos?</em></li>
</ul>

<div class="table-container">
  <table class="academic-table">
    <caption><strong>TABELA I:</strong> ESTRUTURAÇÃO DO CRITÉRIO PICOC</caption>
    <thead>
      <tr><th>Elemento</th><th>Definição Adotada no Estudo</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Population</strong></td><td>Estudantes da Educação Básica (K-12 / Fundamental e Médio).</td></tr>
      <tr><td><strong>Intervention</strong></td><td>Modelos de IA, Aprendizado de Máquina, EWS e ferramentas diagnósticas.</td></tr>
      <tr><td><strong>Comparison</strong></td><td>Métodos tradicionais e ausência de ferramentas automatizadas.</td></tr>
      <tr><td><strong>Outcomes</strong></td><td>Recusa escolar OU (absenteísmo/evasão com fatores socioemocionais).</td></tr>
      <tr><td><strong>Context</strong></td><td>Ambientes educacionais escolares públicos e privados.</td></tr>
    </tbody>
  </table>
</div>

<h3 class="subsection-title">Critérios de Elegibilidade (IC / EC)</h3>
<p class="no-indent">Foram aplicados critérios formais de inclusão e exclusão:</p>
<ul>
  <li><strong>IC1:</strong> Artigos originais revisados por pares em periódicos e anais de conferências.</li>
  <li><strong>IC2:</strong> Desenvolvimento, validação, aplicação empírica ou revisão de ferramentas diagnósticas ou modelos de IA para recusa/absenteísmo no K-12.</li>
  <li><strong>IC3:</strong> Idiomas inglês, português ou espanhol.</li>
  <li><strong>IC4:</strong> Validação empírica, métricas de acurácia/F1-score ou revisões sistemáticas.</li>
  <li><strong>EC1:</strong> Literatura cinzenta não validada, volumes de anais completos (proceedings inteiros) e resumos sem dados empíricos.</li>
  <li><strong>EC2:</strong> Ensino Superior (graduação/MOOCs), absenteísmo laboral adulto ou evasão puramente financeira/estrutural sem componentes de IA ou saúde mental.</li>
  <li><strong>EC3:</strong> Publicações duplicadas entre as bases.</li>
  <li><strong>EC4:</strong> Textos integrais não recuperáveis institucionalmente.</li>
</ul>

<h2 class="section-title">3. Execução das Buscas Brutas</h2>
<p>A formulação booleana oficial combinou três eixos conceituais (<em>Fenômeno</em> ∧ <em>Dimensão Socioemocional</em> ∧ <em>IA/Predição</em>), com adaptações sintáticas validadas para as particularidades de cada motor de busca (Tabela II):</p>

</div> <!-- End Columns -->

<div class="full-width">
  <table class="academic-table">
    <caption><strong>TABELA II:</strong> REGISTRO GERAL DAS BUSCAS BRUTAS EXECUTADAS NAS SEIS BASES ACADÊMICAS (PRISMA 2020)</caption>
    <thead>
      <tr>
        <th>ID</th>
        <th>Data</th>
        <th>Base de Dados</th>
        <th style="text-align:center;">Total</th>
        <th>Formato</th>
        <th>Campos da Busca</th>
        <th>Filtros e Características Metodológicas</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>B01</strong></td>
        <td>24/09/2026</td>
        <td>ACM Digital Library</td>
        <td style="text-align:center;"><strong>198</strong></td>
        <td>BibTeX</td>
        <td>Title / Abstract</td>
        <td>Consulta direta nos metadados integrados.</td>
      </tr>
      <tr>
        <td><strong>B02</strong></td>
        <td>24/09/2026</td>
        <td>IEEE Xplore</td>
        <td style="text-align:center;"><strong>14</strong></td>
        <td>BibTeX</td>
        <td>Metadata (Title, Abs, Key)</td>
        <td>String canônica tripartite completa via operador <code>AND</code>.</td>
      </tr>
      <tr>
        <td><strong>B03</strong></td>
        <td>04/10/2026</td>
        <td>ScienceDirect (Elsevier)</td>
        <td style="text-align:center;"><strong>62</strong></td>
        <td>BibTeX</td>
        <td>Title, Abstract, Keywords</td>
        <td>String oficial enxuta (limite rígido de 8 operadores booleanos).</td>
      </tr>
      <tr>
        <td><strong>B04</strong></td>
        <td>04/10/2026</td>
        <td>Scopus (Elsevier)</td>
        <td style="text-align:center;"><strong>195</strong></td>
        <td>BibTeX</td>
        <td>Title, Abstract, Keywords</td>
        <td>Execução dos 3 blocos completos via interface gráfica de busca.</td>
      </tr>
      <tr>
        <td><strong>B05</strong></td>
        <td>04/10/2026</td>
        <td>Web of Science (Clarivate)</td>
        <td style="text-align:center;"><strong>83</strong></td>
        <td>BibTeX</td>
        <td>Topic (Title, Abs, Key)</td>
        <td>Core Collection; Articles & Proceeding Papers (2 lotes: 50+33).</td>
      </tr>
      <tr>
        <td><strong>B06</strong></td>
        <td>04/10/2026</td>
        <td>Springer Link (Springer)</td>
        <td style="text-align:center;"><strong>1.000</strong></td>
        <td>CSV</td>
        <td>Todo o texto / Metadados</td>
        <td>Filtros de Content Type: Articles (921) e Conference papers (79).</td>
      </tr>
      <tr style="background:#e8f0fe;">
        <td colspan="3"><strong>TOTAL GERAL DE REGISTROS IDENTIFICADOS</strong></td>
        <td style="text-align:center; font-size:9pt;"><strong>1.552</strong></td>
        <td colspan="3"><strong>Universo bruto completo consolidado para deduplicação</strong></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="columns">

<h2 class="section-title">4. Triagem Inicial (Fase 1)</h2>

<h3 class="subsection-title">4.1 Deduplicação Inter-bases (Critério EC3)</h3>
<p>O algoritmo automatizado de deduplicação cruzou os 1.552 registros brutos através da normalização sistemática de DOIs e títulos alfanuméricos. Foram identificadas e removidas <strong>81 duplicatas inter-bases</strong>:</p>
<ul>
  <li><strong>Web of Science:</strong> 58 duplicatas (58 dos 83 artigos já haviam sido catalogados pelo Scopus, IEEE ou ACM).</li>
  <li><strong>Springer Link:</strong> 19 duplicatas (já indexadas no Scopus ou ScienceDirect).</li>
  <li><strong>IEEE Xplore:</strong> 3 duplicatas (presentes no Scopus).</li>
  <li><strong>ACM DL:</strong> 1 duplicata (presente no Scopus).</li>
</ul>
<p>O universo para a avaliação sistemática por título e resumo resultou em <strong>1.471 registros únicos</strong>.</p>

<h3 class="subsection-title">4.2 Avaliação de Título e Resumo</h3>
<p>A aplicação dos critérios de elegibilidade sobre os 1.471 registros únicos resultou em:</p>
<ul>
  <li><strong>1.312 estudos excluídos:</strong> 70 por EC1 (volumes de anais completos, índices, resumos de pôster) e 1.242 por EC2 (ensino superior universitário, evasão puramente socioeconômica ou estudos biomédicos não escolares).</li>
  <li><strong>159 estudos incluídos para Leitura Integral (Fase 2):</strong> Estudos de alta densidade que abordam diretamente predição de absenteísmo, recusa escolar ou instrumentos diagnósticos no K-12.</li>
</ul>

<div class="table-container">
  <table class="academic-table">
    <caption><strong>TABELA III:</strong> RESULTADOS DA TRIAGEM POR BASE DE DADOS</caption>
    <thead>
      <tr><th>Base de Dados</th><th style="text-align:center;">Avaliados</th><th style="text-align:center;">Excluídos</th><th style="text-align:center;">Incluídos (Fase 2)</th></tr>
    </thead>
    <tbody>
      <tr><td>Scopus</td><td style="text-align:center;">195</td><td style="text-align:center;">85</td><td style="text-align:center;"><strong>110</strong> (56,4%)</td></tr>
      <tr><td>Springer Link</td><td style="text-align:center;">981</td><td style="text-align:center;">961</td><td style="text-align:center;"><strong>20</strong> (2,0%)</td></tr>
      <tr><td>Web of Science</td><td style="text-align:center;">25</td><td style="text-align:center;">9</td><td style="text-align:center;"><strong>16</strong> (64,0%)</td></tr>
      <tr><td>IEEE Xplore</td><td style="text-align:center;">11</td><td style="text-align:center;">6</td><td style="text-align:center;"><strong>5</strong> (45,5%)*</td></tr>
      <tr><td>ScienceDirect</td><td style="text-align:center;">62</td><td style="text-align:center;">58</td><td style="text-align:center;"><strong>4</strong> (6,5%)</td></tr>
      <tr><td>ACM Digital Library</td><td style="text-align:center;">197</td><td style="text-align:center;">193</td><td style="text-align:center;"><strong>4</strong> (2,0%)</td></tr>
      <tr style="background:#e8f0fe;"><td><strong>Total Geral</strong></td><td style="text-align:center;"><strong>1.471</strong></td><td style="text-align:center;"><strong>1.312</strong></td><td style="text-align:center;"><strong>159</strong> (<strong>10,8%</strong>)</td></tr>
    </tbody>
  </table>
  <div style="font-size:7pt; color:#555; margin-top:2px;">*Outros 3 estudos da IEEE foram catalogados primariamente via Scopus (totalizando 8).</div>
</div>

<h3 class="subsection-title">4.3 Fluxo PRISMA 2020 Consolidado</h3>
<div class="prisma-box">
  <div style="text-align:center; font-weight:bold; color:#1f497d; margin-bottom:5px; font-size:8.8pt;">FLUXO PRISMA 2020 — TRIAGEM INICIAL</div>
  <div class="prisma-step step-id">
    <span><strong>1. IDENTIFICAÇÃO:</strong> Registros Brutos Catalogados nas 6 Bases</span>
    <span><strong>1.552 registros</strong></span>
  </div>
  <div class="prisma-step step-dedup">
    <span><strong>2. DEDUPLICAÇÃO:</strong> Duplicatas Inter-bases Removidas (EC3)</span>
    <span><strong>-81 duplicatas</strong></span>
  </div>
  <div class="prisma-step step-screen">
    <span><strong>3. REGISTROS ÚNICOS:</strong> Submetidos à Triagem de Título e Resumo</span>
    <span><strong>1.471 artigos</strong></span>
  </div>
  <div class="prisma-step step-elig">
    <span><strong>4. EXCLUSÃO NA TRIAGEM:</strong> Excluídos por Critérios Formais (EC1 e EC2)</span>
    <span><strong>-1.312 excluídos</strong></span>
  </div>
  <div class="prisma-step step-inc">
    <span><strong>5. ELEGÍVEIS (FASE 2):</strong> Selecionados para Leitura de Texto Completo</span>
    <span><strong>159 estudos incluídos</strong></span>
  </div>
</div>

<h2 class="section-title">5. Discussão das Evidências Iniciais</h2>

<h3 class="subsection-title">5.1 Instrumentos Diagnósticos e Psicométricos (RQ1)</h3>
<p>A triagem revelou o protagonismo de instrumentos estruturados para triagem de infrequência e comorbidades socioemocionais no K-12. Destacam-se a <em>School Refusal Assessment Scale-Revised</em> (SRAS-R), o instrumento <em>SCREEN</em> (validado em 2026 para recusa escolar na Itália) e a escala <em>SCARED</em> para ansiedade de separação e evitação escolar, frequentemente combinados a registros acadêmicos para alimentação de modelos de IA.</p>

<h3 class="subsection-title">5.2 Modelos de IA e Aprendizado de Máquina (RQ2)</h3>
<p>Verifica-se a transição de algoritmos lineares clássicos para modelos avançados de ensemble (Random Forest, XGBoost, CatBoost) e Redes Neurais Convolucionais (CNNs). Sobressai o estudo de Barros et al. (2026), que desenvolveu um modelo interpretável de predição de absenteísmo discente em escala massiva abrangendo mais de 22.000 escolas públicas brasileiras, demonstrando a viabilidade técnica de implantação em redes estaduais e municipais.</p>

<h3 class="subsection-title">5.3 Preditores Socioemocionais e Contextuais (RQ3)</h3>
<p>Ao contrário dos sistemas tradicionais de alerta que consideram apenas médias de notas, os modelos contemporâneos priorizam variáveis contextuais: índices de vitimização por bullying, desconexão com a comunidade escolar, dinâmicas parentais e sintomas internalizantes de ansiedade e depressão, os quais manifestam correlação precoce com o absenteísmo crônico.</p>

<h3 class="subsection-title">5.4 Desafios Metodológicos e Éticos (RQ4)</h3>
<p>A literatura destaca o desbalanceamento severo de classes como o maior desafio técnico (técnicas como SMOTE e custo sensível são indispensáveis). Além disso, a explicabilidade dos modelos (<em>eXplainable AI</em> via SHAP e LIME) consolidou-se como exigência ética indispensável para que gestores escolares compreendam as recomendações algorítmicas sem incorrer em rotulação estigmatizante.</p>

<h2 class="section-title">6. Cronograma e Próximos Passos</h2>
<p class="no-indent">Com a Fase 1 integralmente concluída, o projeto segue para:</p>
<ol>
  <li><strong>Recuperação de Textos Completos:</strong> Obtenção dos 159 artigos via convênio CAPES/CAFe e repositórios institucionais abertos.</li>
  <li><strong>Avaliação de Texto Integral:</strong> Aplicação minuciosa dos critérios de elegibilidade e registro de exclusões na leitura integral.</li>
  <li><strong>Extração Estruturada e Avaliação de Qualidade:</strong> Aplicação da matriz de extração e checklist metodológico QA1 a QA5.</li>
  <li><strong>Síntese e Redação:</strong> Redação dos capítulos da dissertação respondendo formalmente às 4 RQs.</li>
</ol>

</div> <!-- End Columns -->

<div class="full-width">
  <table class="academic-table">
    <caption><strong>TABELA IV:</strong> SÍNTESE DE ESTUDOS REPRESENTATIVOS SELECIONADOS NA TRIAGEM INICIAL POR BASE ACADÊMICA (FASE 1)</caption>
    <thead>
      <tr>
        <th>ID</th>
        <th>Ano</th>
        <th>Título do Estudo</th>
        <th>Base</th>
        <th>Veículo de Publicação</th>
        <th>Abordagem / Foco Técnico e Instrumentos</th>
        <th>RQs</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>S0008</strong></td>
        <td>2026</td>
        <td>Investigating School Refusal in Italy: SCREEN Validation</td>
        <td>Scopus</td>
        <td>Children</td>
        <td>Validação psicométrica da escala SCREEN para Recusa Escolar (CFA/SEM).</td>
        <td>RQ1, RQ3</td>
      </tr>
      <tr>
        <td><strong>S0013</strong></td>
        <td>2019</td>
        <td>Emerging School Refusal: A School-Based Framework</td>
        <td>Scopus</td>
        <td>J. School Psychology</td>
        <td>Framework multinível de intervenção precoce em problemas de assiduidade escolar.</td>
        <td>RQ1, RQ2</td>
      </tr>
      <tr>
        <td><strong>S0197</strong></td>
        <td>2022</td>
        <td>Revealing Underlying Factors of Absenteeism: A ML Approach</td>
        <td>WoS</td>
        <td>Computers & Education</td>
        <td>Modelos de Machine Learning (Random Forest e XGBoost) para predizer infrequência.</td>
        <td>RQ2, RQ3, RQ4</td>
      </tr>
      <tr>
        <td><strong>S0224</strong></td>
        <td>2019</td>
        <td>Developing an Online Early Detection System for Attendance</td>
        <td>ScienceDirect</td>
        <td>Cognitive and Behavioral Practice</td>
        <td>Sistema Web de Alerta Precoce baseado em parceria de pesquisa comunitária.</td>
        <td>RQ2, RQ3, RQ4</td>
      </tr>
      <tr>
        <td><strong>S0265</strong></td>
        <td>2026</td>
        <td>Interpretable ML Framework for Psychological Risk</td>
        <td>ScienceDirect</td>
        <td>Computers in Biology and Medicine</td>
        <td>Machine Learning Interpretável (XAI) para triagem de risco comportamental discente.</td>
        <td>RQ2, RQ4</td>
      </tr>
      <tr>
        <td><strong>S0315</strong></td>
        <td>2025</td>
        <td>Difficult Lessons on Social Prediction from Wisconsin Public Schools</td>
        <td>ACM DL</td>
        <td>ACM FAccT</td>
        <td>Avaliação empírica e crítica de Sistemas de Alerta Precoce (EWS) em escolas públicas.</td>
        <td>RQ2, RQ4</td>
      </tr>
      <tr>
        <td><strong>S0501</strong></td>
        <td>2026</td>
        <td>Interpretable ML for Predicting School Absenteeism at-Scale in Brazil</td>
        <td>Springer Link</td>
        <td>Scientific Reports (Nature)</td>
        <td>Machine Learning interpretável aplicado a mais de 22.000 escolas públicas no Brasil.</td>
        <td>RQ2, RQ3, RQ4</td>
      </tr>
      <tr>
        <td><strong>S0502</strong></td>
        <td>2026</td>
        <td>Interpretable ML Framework for Predicting School Dropout</td>
        <td>Springer Link</td>
        <td>Innovations in Data Analytics</td>
        <td>Framework de ML preditivo de risco comportamental e evasão em jovens vulneráveis.</td>
        <td>RQ2, RQ3</td>
      </tr>
      <tr>
        <td><strong>S0001</strong></td>
        <td>2025</td>
        <td>Predicting School Dropout and Simulating Educational Scenarios</td>
        <td>IEEE Xplore</td>
        <td>IEEE AmITIC</td>
        <td>Redes Neurais Artificiais e SVM com acurácia >85% e simulação de políticas públicas.</td>
        <td>RQ2, RQ4</td>
      </tr>
      <tr>
        <td><strong>S0002</strong></td>
        <td>2026</td>
        <td>Predicting Anxiety Status: SCARED Questionnaire + Machine Learning</td>
        <td>IEEE Xplore</td>
        <td>IEEE ICARC</td>
        <td>Questionário psicométrico clínico SCARED + Random Forest para Evitação Escolar.</td>
        <td>RQ1, RQ2, RQ3</td>
      </tr>
      <tr>
        <td><strong>S0004</strong></td>
        <td>2026</td>
        <td>AI-Driven Psychoeducational Analytics in Colombian Schools</td>
        <td>IEEE Xplore</td>
        <td>IEEE EDUNINE</td>
        <td>Instrumentos psicométricos validados + Algoritmos de regressão e clustering para risco.</td>
        <td>RQ1, RQ2, RQ3</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="columns">

<h2 class="section-title">7. Conclusão</h2>
<p>Este relatório formaliza o encerramento com êxito da Fase 1 da RSL. O mapeamento exaustivo em seis bases internacionais (1.552 registros brutos) e a posterior deduplicação (1.471 registros únicos) resultaram na seleção rigorosa de 159 estudos científicos de alta aderência temática. As evidências obtidas demonstram a robustez e a contemporaneidade da pesquisa, pavimentando um caminho consistente para o desenvolvimento e a análise crítica de ferramentas computacionais voltadas ao enfrentamento da recusa escolar e do absenteísmo crônico na Educação Básica.</p>

<h2 class="section-title">Referências</h2>
<div class="references">
  <p>[1] B. Kitchenham and S. Charters, "Guidelines for performing Systematic Literature Reviews in Software Engineering," Keele Univ., Tech. Rep. EBSE-2007-01, 2007.</p>
  <p>[2] M. J. Page <em>et al.</em>, "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews," <em>BMJ</em>, vol. 372, p. n71, 2021.</p>
  <p>[3] C. A. Kearney and P. Graczyk, "A Response to Intervention Model to Promote School Attendance and Decrease School Absenteeism," <em>Child & Youth Care Forum</em>, vol. 49, pp. 1–25, 2020.</p>
  <p>[4] B. C. Chu <em>et al.</em>, "Developing an Online Early Detection System for School Attendance Problems," <em>Cognitive and Behavioral Practice</em>, vol. 26, no. 1, pp. 35–45, 2019.</p>
  <p>[5] A. N. Barros <em>et al.</em>, "Interpretable machine learning for predicting school absenteeism at-scale in Brazil: evidence from 22,000 schools," <em>Scientific Reports</em>, vol. 16, p. 48729, 2026.</p>
  <p>[6] C. F. Meduri <em>et al.</em>, "Investigating School Refusal in the Italian Context: SCREEN Validation," <em>Children</em>, vol. 13, no. 3, pp. 1–15, 2026.</p>
  <p>[7] I. G. G. Umayangana and R. Abeygunawardana, "A Machine Learning Approach for Predicting Anxiety Status: SCARED Questionnaire," in <em>Proc. IEEE ICARC</em>, 2026.</p>
  <p>[8] R. Y. Zuleta Torres <em>et al.</em>, "AI-Driven Psychoeducational Analytics in Colombian Schools," in <em>Proc. IEEE EDUNINE</em>, 2026.</p>
  <p>[9] J. C. Perdomo <em>et al.</em>, "Difficult Lessons on Social Prediction from Wisconsin Public Schools," in <em>Proc. ACM FAccT</em>, pp. 2682–2704, 2025.</p>
  <p>[10] F. Çimen, İ. Seçer, and E. Ay, "Latent Profile and Network Analysis of School Attendance Problems in Adolescents," <em>School Mental Health</em>, vol. 17, pp. 1–16, 2025.</p>
</div>

</div> <!-- End Columns -->

</body>
</html>
"""

html_path = "06_sintese_relatorio/relatorio_artigo_temp.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

edge_exe = None
for p in edge_paths:
    if os.path.exists(p):
        edge_exe = p
        break

pdf_path = os.path.abspath("06_sintese_relatorio/relatorio_andamento_rsl.pdf")
abs_html = os.path.abspath(html_path)

if edge_exe:
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        abs_html
    ]
    print(f"Executando renderização com Edge: {edge_exe}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path):
        print(f"PDF compilado com sucesso: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
    else:
        print("Erro ao gerar PDF:", res.stderr)
else:
    print("Edge não encontrado!")
