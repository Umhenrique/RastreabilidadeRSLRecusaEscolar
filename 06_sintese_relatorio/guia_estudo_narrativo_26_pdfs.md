# Guia de Estudo Narrativo — 26 PDFs Analisados (Fase 2)

**Pesquisador:** Matheus Henrique Assuncao de Medeiros (PGCC UERN / UFERSA)  
**Objetivo deste documento:** Explicar cada um dos 26 artigos lidos na integra em 2 a 3 paragrafos corridos, em linguagem direta, para facilitar seu estudo e preparacao para a reuniao de orientacao.

---

## Parte I — Eixo Computacional: IA, Machine Learning e Sistemas de Alerta Precoce (12 estudos)

### 1. S0501 — Barros et al. (2026): *Interpretable machine learning for predicting school absenteeism at-scale in Brazil: evidence from 22,000 schools*
Este estudo e a referencia brasileira mais relevante da sua revisao. Os autores analisaram dados oficiais de 22.476 escolas publicas de Ensino Medio em todo o Brasil, agrupadas em seis niveis de complexidade de gestao (ICG 1 a 6), com o objetivo de prever o risco de absenteismo escolar em escala nacional usando apenas dados administrativos disponiveis na rede publica.

Para isso, compararam cinco algoritmos de aprendizado de maquina (Random Forest, CatBoost, XGBoost, LightGBM e Regressao Logistica) e selecionaram o Random Forest por seu equilibrio entre desempenho e interpretabilidade. Alem da predicao, os autores aplicaram tecnicas de IA Explicavel (SHAP e simulacoes contrafactuais *what-if*) para identificar quanto cada fator (como infraestrutura, localizacao, nivel socioeconomico e indicadores academicos) precisaria mudar para tirar uma escola da zona de risco.

Os resultados mostraram acuracia entre 67% e 85% (com F1-Score entre 0,58 e 0,81), funcionando melhor nas escolas de menor complexidade de gestao. Para a sua dissertacao, o ponto mais valioso e a lacuna que o proprio artigo deixa evidente: mesmo com uma amostra gigantesca de 22 mil escolas brasileiras, os sistemas governamentais nao registram variaveis de saude mental, ansiedade ou sofrimento emocional, tratando tudo apenas como falta administrativa.

---

### 2. S0290 — Abas et al. (2026): *Explainable Ensemble Learning for Student Dropout Prediction in Conflict-Affected Educational Systems*
Neste trabalho, os autores investigaram a evasao escolar de estudantes do ensino medio em cinco escolas de Sabha, na Libia, um contexto marcado por conflitos e vulnerabilidade social. Ao todo, participaram 1.158 estudantes que responderam a um questionario estruturado de 34 itens cobrindo fatores psicossociais, economicos, escolares e de seguranca.

Para lidar com o desbalanceamento dos dados (apenas 16% estavam na categoria de risco), os pesquisadores combinaram selecao de atributos via LASSO, balanceamento sintetico SMOTE e dois modelos de *ensemble*: XGBoost e Random Forest. Em seguida, aplicaram a tecnica de explicabilidade local LIME para que educadores pudessem enxergar, aluno por aluno, quais respostas pesaram mais na classificacao de risco.

O XGBoost obteve desempenho muito alto, com 94,1% de acuracia e F1-Score de 0,941 na validacao cruzada, praticamente empatado com o Random Forest (93,9%). Trata-se de um exemplo pratico claro de como combinar um questionario psicossocial estruturado com modelos baseados em arvores e explicabilidade local para apoiar decisoes escolares.

---

### 3. S0315 — Perdomo et al. (2025): *Difficult Lessons on Social Prediction from Wisconsin Public Schools*
Este estudo faz uma auditoria critica de grande porte sobre o sistema oficial de alerta precoce do estado de Wisconsin, nos Estados Unidos (DEWS), analisando mais de 200 mil estudantes do 8o ano acompanhados entre 2013 e 2021. Em vez de propor apenas mais um algoritmo, os autores quiseram testar se gerar escores de risco realmente ajuda os alunos na pratica.

Na etapa preditiva, compararam o modelo estadual (baseado em Random Forest / GBDT) com um modelo CatBoost que separava variaveis individuais do aluno e variaveis ambientais da escola, alcancando boa capacidade de discriminacao (AUC de 0,80 no DEWS e 0,863 no CatBoost). Porem, na segunda etapa, usaram inferencia causal (Regressao Descontinua) exatamente na linha de corte que separa alunos de risco moderado dos de alto risco.

A conclusao e um alerta metodologico valioso para a sua banca: embora os algoritmos consigam prever quem vai faltar ou evadir, o simples fato de o sistema emitir um alerta nao produziu melhora estatisticamente garantida nos alunos, porque muitas escolas nao tinham um protocolo claro do que fazer apos o aviso. Isso reforca a necessidade de ligar o alerta computacional a uma triagem psicologica ou intervencao real.

---

### 4. S0322 — Xu et al. (2021): *Early Alert Systems During a Pandemic: A Simulation Study on the Impact of Concept Drift*
Os autores estudaram um sistema real de alerta precoce da rede publica de Rhode Island (EUA), treinado com dados de 2007 a 2015 e testado no ano letivo de 2016, para entender o que acontece quando uma crise (como a pandemia de COVID-19) muda bruscamente os padroes de comportamento dos alunos — fenomeno conhecido como *concept drift*.

O modelo utilizado foi uma variante rapida de Random Forest (`FastForest`), avaliada em tres cenarios simulados de mudanca de dados e cinco estrategias de imputacao. No cenario original, o sistema atingiu 91,3% de acuracia e AUC de 0,890, mas com F1-Score de apenas 0,493, mostrando o quanto o desbalanceamento natural entre alunos que evadem e alunos que permanecem na escola dificulta a precisao dos alertas.

Mesmo sob simulacoes de crise, o modelo manteve AUC entre 0,868 e 0,891 quando adaptado adequadamente. O artigo ensina duas licoes tecnicas importantes para a sua RSL: a importancia de avaliar metricas adequadas a classes desbalanceadas (como F1-Score e Recall, nao apenas acuracia) e a necessidade de recalibrar modelos escolares ao longo do tempo.

---

### 5. S0325 — Su et al. (2022): *Re-envisioning a K-12 Early Warning System with School Climate Factors*
Neste trabalho em andamento, os pesquisadores analisaram dados de cerca de 60 mil alunos em 277 escolas (2019) e 75 mil alunos em 261 escolas (2021) do estado de Nevada (EUA) com o objetivo de enriquecer o sistema comercial de alerta precoce *Infinite Campus* (que normalmente usa GBDT e SHAP apenas sobre notas e faltas).

Para testar o valor real de variaveis socioemocionais e ambientais, os autores cruzaram indicadores escolares de atraso e comportamento com a escala estadual de clima escolar (NV-SCSEL), que mede seguranca fisica, seguranca emocional, relacionamentos e competencia cultural. Utilizaram regressao linear multipla no nivel das escolas antes de avancar para o modelo individual.

Os resultados comprovaram que o clima escolar explica ate 15% da variacao nas taxas de atraso escolar e ate 14% dos problemas comportamentais, com significancia estatistica elevada. Isso fornece uma justificativa empirica direta para incluir percepcao de clima escolar e seguranca emocional em modelos preditivos de recusa e absenteismo.

---

### 6. S0198 — Goh et al. (2026): *A Machine Learning Approach to Classifying School Absenteeism Patterns in Youth with ADHD*
Os autores investigaram padroes de absenteismo escolar em 194 criancas e adolescentes canadenses (entre 4 e 17 anos) diagnosticados com TDAH, uma populacao com risco particularmente alto de dificuldades de frequencia e sofrimento emocional na escola.

O estudo combinou um checklist clinico biopsicossocioeducacional de 80 itens com um modelo Random Forest de 1.000 arvores, validado por validacao cruzada repetida (5x5-fold) e divisao treino/teste (67%/33%). Entre as variaveis analisadas estavam sintomas internalizantes e externalizantes, sono, clima familiar e historico escolar.

No conjunto de teste, o modelo alcancou AUC de 0,79, acuracia de 73% e sensibilidade de 80% ao ajustar o limiar de decisao para priorizar a deteccao precoce (evitando deixar casos graves passarem despercebidos). E um dos estudos mais completos da sua revisao por unir avaliacao clinica estruturada, neurodivergencia e aprendizado de maquina.

---

### 7. S0191 — Madasu & Hajiarbabi (2026): *Medical expert system as a chatbot for screening of anxiety disorders in children and adolescents*
Este artigo apresenta o desenvolvimento de um sistema especialista conversacional (chatbot) voltado a triagem de transtornos de ansiedade em criancas e adolescentes, pensado para contextos onde ha escassez de psicologos e psiquiatras infantis.

Diferente de modelos baseados em redes neurais opacas, os autores modelaram o raciocinio clinico com regras explicitas (*Forward Chaining* mapeado em BPMN e implementado em AIML) a partir da escala validada SCARED de 41 itens — que possui uma subescala especifica para **Evitacao Escolar** (*School Avoidance*). O prototipo foi avaliado por 100 usuarios, sendo 70 pais e 30 profissionais de saude.

Os testes mostraram concordancia clinica de 92% para ansiedade generalizada e 89% para transtorno do panico, alem de 90% de satisfacao geral e 85% de avaliacao positiva quanto a facilidade de uso. Para o seu mestrado, e um otimo exemplo de como digitalizar uma escala clinica validada em uma interface acessivel para pais e escolas.

---

### 8. S0283 — Fernandez et al. (2025): *Predicting School Dropout and Simulating Educational Scenarios in Colombia Using Machine Learning*
Desenvolvido no departamento de Huila, na Colombia, este trabalho criou a plataforma `EduAnalytics Huila` utilizando dados de 2.000 estudantes do ensino secundario e uma validacao de campo com 120 usuarios da rede educacional.

Os autores compararam tres algoritmos classicos de Machine Learning — Redes Neurais Artificiais (ANN), Maquinas de Vetores de Suporte (SVM) e Arvores de Decisao — e integraram os resultados a um modulo de simulacao baseado em Dinamica de Sistemas para projetar cenarios futuros de evasao.

A Rede Neural obteve o melhor desempenho, com 85,4% de acuracia, F1-Score de 0,84 e AUC de 0,88, superando a SVM (81,2%) e a Arvore de Decisao (77,3%). Embora menos aprofundado em psicometria, o estudo ilustra a aplicacao pratica de ferramentas preditivas na realidade educacional latino-americana.

---

### 9. S0104 — Nishimura et al. (2024): *Early detection of students' mental health issues from a traditional daily health observation scheme in Japanese schools and its digitalization*
Aproveitando a tradicao japonesa de checagem diaria de saude nas escolas e a distribuicao de tablets do programa *GIGA School*, os autores acompanharam 2.143 alunos (do 1o ao 9o ano) durante 76 dias letivos em cinco escolas publicas. Todos os dias, os alunos registravam rapidamente queixas fisicas, sono e estado emocional (inspirado em *Zones of Regulation*).

Para analisar essa serie temporal curta, combinaram Modelagem de Trajetorias Baseada em Grupos (identificando 5 perfis longitudinais) com uma tecnica simples de deteccao de anomalias chamada *Rolling Z-Score* (comparando o dia atual com os ultimos 7 dias do proprio aluno), validando tudo contra a escala de depressao/ansiedade PHQ-4 e a escala de clima escolar JaSC.

Os resultados foram expressivos: o grupo com maior carga diaria de queixas (5,4% dos alunos) teve risco mais de cinco vezes maior de desenvolver sintomas depressivos/ansiosos (*IRR = 5,17*) e mais que o dobro de dias de falta (*IRR = 2,14*). Alem disso, os autores destacam que o *Rolling Z-Score* e tao simples e transparente que os proprios professores conseguem entender e explicar por que o sistema sinalizou um aluno.

---

### 10. S0012 — Zhou & Geng (2026): *Artificial intelligence as decision support for adolescent depression and anxiety: a mini review of clinical utility, safety, and implementation*
Esta mini-revisao publicada na *Frontiers in Psychiatry* analisa de forma critica o que a Inteligencia Artificial — incluindo modelos preditivos, fenotipagem digital por smartphones e chatbots com LLMs — pode realmente entregar no cuidado de adolescentes com depressao e ansiedade.

Os autores nao apresentam experimentos proprios, mas propoe um framework pratico chamado ***decision-first***: a IA nunca deve fazer diagnostico autonomo, mas sim apoiar decisoes concretas (quem avaliar primeiro, quem monitorar mais de perto, quando acionar familia e escola). Eles citam explicitamente a **recusa escolar** (*school refusal*) como um dos principais sinais precoces indiretos antes do diagnostico formal.

O artigo tambem detalha armadilhas tecnicas e eticas essenciais para a sua secao de limitacoes (RQ4), como o *outcome leakage* (modelos que aprendem a prever registros administrativos em vez do adoecimento real), falta de calibracao de probabilidades, privacidade de menores e a exigencia de seguir padroes como TRIPOD+AI e PROBAST+AI.

---

### 11. S0204 — Kearney (2021) e 12. S0206 — Kearney & Childs (2023)
Estes dois artigos de Christopher Kearney (um dos pesquisadores mais citados do mundo em recusa escolar) funcionam como a espinha dorsal teorica da sua RSL. No primeiro (`S0204`), o autor integra cinco dominios da pesquisa sobre problemas de frequencia escolar e propoe unir a visao psicologica/sistemica com metodos analiticos modernos (como EWS, Random Forest, CART, SVM e analise de classes latentes).

No segundo (`S0206`), Kearney e Childs traduzem essas estrategias analiticas complexas para a pratica de politicas educacionais no ensino basico (K-12), diferenciando metodos baseados em algoritmos (Machine Learning para predicao e curvas ROC/AUC) de metodos baseados em modelos estatisticos (para entender causas profundas).

Juntos, ambos os estudos legitimam diretamente o argumento central da sua dissertacao: o futuro da deteccao precoce da recusa escolar depende de sistemas em camadas (MTSS) que combinem dados escolares continuos com triagem socioemocional valida.

---

## Parte II — Eixo Psicometrico, Redes e Fatores Socioemocionais (12 estudos)

### 13. S0735 — Yu et al. (2024): *Validation of the School Refusal Assessment Scale-Revised (SRAS-R) in the General Adolescent Population in China*
Este estudo validou a principal escala especifica de recusa escolar do mundo — a *School Refusal Assessment Scale-Revised* (SRAS-R) — na populacao geral de 1.108 adolescentes chineses entre 12 e 19 anos, divididos em amostras independentes para analise fatorial exploratoria e confirmatoria.

Os pesquisadores testaram a estrutura da versao adaptada de 21 itens e confirmaram excelentes indices de ajuste estatistico (CFI = 0,92; TLI = 0,90; RMSEA = 0,05), confiabilidade interna consistente (Alfa de Cronbach entre 0,79 e 0,85) e correlacoes significativas com sintomas depressivos medidos pelo PHQ-9 (r entre 0,27 e 0,63).

Alem disso, comprovaram a invariancia escalar por sexo e tipo de escola, garantindo que a escala mede o fenomeno de forma justa tanto em meninos quanto em meninas. Para a RQ1, e uma das validacoes mais solidas da SRAS-R em larga escala escolar.

---

### 14. S0561 — Perez-Marco et al. (2026): *School refusal evaluation scale: factorial invariance and latent means differences across gender and age in Spanish adolescents*
Focado na escala SCREEN (*School Refusal Evaluation*), este trabalho avaliou 681 estudantes espanhois de 13 a 16 anos para testar a versao reduzida de 12 itens em quatro fatores (como antecipacao ansiosa, fobia escolar, desconforto interpessoal e evitacao).

Por meio de Analise Fatorial Confirmatoria e Analise Fatorial Multigrupo, os autores obtiveram indices de ajuste excelentes (CFI = 0,949; RMSEA = 0,052) e confiabilidade adequada (Alfa e Omega entre 0,71 e 0,74). Tambem confirmaram invariancia escalar entre generos e faixas etarias.

Como achado pratico, observaram que as meninas apresentaram pontuacoes significativamente maiores na dimensao de desconforto interpessoal (tamanho de efeito d = 0,47), sugerindo sensibilidade diferente a fatores relacionais e de ansiedade social na escola.

---

### 15. S0567 — Boudouda et al. (2024): *Assessing School Refusal: Arabic Adaptation and Psychometric Properties of the School Refusal Evaluation (SCREEN) from Adolescents in Algeria*
Os autores conduziram dois estudos na Argelia, somando 1.143 adolescentes (658 no Estudo 1 e 485 no Estudo 2, entre 12 e 16 anos), para adaptar e validar a versao arabe da escala SCREEN (18 itens organizados em 3 fatores).

A estrutura apresentou bom ajuste confirmatorio (CFI = 0,909; RMSEA = 0,063) e alta consistencia interna total (Alfa de Cronbach = 0,85; Omega de McDonald = 0,86). Para checar a validade convergente, os autores cruzaram a SCREEN com a escala SCARED e a GAD-7.

Os resultados mostraram correlacoes fortes com a subescala de fobia escolar da SCARED (r = 0,54) e com ansiedade generalizada (r = 0,56), reforcando a robustez transcultural da SCREEN como instrumento rapido de triagem escolar.

---

### 16. S0555 — Dong et al. (2026): *Network analysis of school refusal behavior and internalizing and externalizing problems among Chinese adolescents*
Em vez de tratar a recusa escolar como um bloco isolado, os pesquisadores aplicaram Analise de Redes Psicologicas (modelo GGM com regularizacao EBICglasso) em 303 adolescentes chineses atendidos clinicamente por comportamento de recusa escolar.

Os participantes responderam a SRAS-R (21 itens) junto com escalas de ansiedade (GAD-7), depressao (PHQ-9), insonia (AIS), uso problematico de internet (YDQ) e problemas externalizantes/internalizantes. Todas as escalas mantiveram confiabilidade entre 0,73 e 0,93.

A rede revelou que **depressao** e **evitacao emocional da escola** sao os dois nos mais centrais que sustentam o problema, alem de identificar sintomas-ponte que ligam dificuldades emocionais e uso excessivo de internet ao afastamento escolar. Isso ajuda muito a responder a RQ3 sobre quais variaveis tem maior poder explicativo.

---

### 17. S0505 — Gok et al. (2026): *Developmental Differences in the Emotional and Behavioural Profiles of Emotionally Based School Avoidance (EBSA) in Children and Adolescents*
Este estudo clinico turco investigou 102 jovens diagnosticados com evitacao escolar de base emocional (EBSA), comparando diretamente 40 criancas (menores de 12 anos) com 62 adolescentes (12 anos ou mais).

Os participantes e responsaveis passaram por entrevista diagnostica estruturada (K-SADS-PL) e responderam a SRAS-R e escalas de ansiedade/depressao (RCADS), regulacao emocional (DERS), dificuldades comportamentais (SDQ) e TDAH (SNAP-IV). Em seguida, modelos de regressao linear multipla testaram o que melhor explicava a gravidade do quadro em cada faixa etaria.

O achado principal mostra que a **ansiedade de separacao** e significativamente mais forte em criancas (p = 0,004). Alem disso, o modelo explicou 47% da variancia em criancas contra apenas 18% em adolescentes, indicando que na adolescencia a recusa escolar envolve fatores sociais e comorbidades mais complexas.

---

### 18. S0500 — Okajima & Hiruma (2025): *How is loneliness orientation implicated in the relationship between sleep problems, loneliness intensity, and school refusal in adolescents?*
Realizado com 128 estudantes do ensino medio em Toquio, no Japao, este artigo investigou como a qualidade do sono e a solidao (tanto a intensidade quanto a atitude frente a solidao) se conectam ao comportamento de recusa escolar e as faltas reais.

Os autores desenvolveram e validaram uma escala de orientacao a solidao (LOT, com excelente Alfa = 0,94 e CFI = 0,99) e a cruzaram com escalas de sono (AIS, SDI, CIRENS), solidao (TILS) e recusa escolar (FSAS), utilizando modelos lineares generalizados e agrupamento hierarquico de Ward.

Os modelos mostraram que a intensidade da solidao prediz significativamente a recusa escolar (explicando 29% da variancia) e que o escore de recusa escolar prediz diretamente o numero de faltas (explicando 38% da variancia). O estudo destaca o sono e a solidao como preditores socioemocionais frequentemente ignorados em sistemas escolares tradicionais.

---

### 19. S0120 — Perez-Marco et al. (2026): *Belongingness and School Refusal in Adolescents: Psychometric Validation and Identification of Risk Profiles*
Avaliando 690 adolescentes espanhois de 12 a 17 anos, os autores investigaram o papel do **pertencimento escolar** — medido pela *General Belongingness Scale* (GBS) — como fator protetivo ou de risco para a recusa escolar medida pela escala SCREEN.

Apos confirmar a validade da GBS (CFI = 0,958; RMSEA = 0,053), aplicaram Analise de Perfis Latentes (LPA, com entropia de 0,825), classificando os estudantes em quatro perfis distintos de inclusao versus exclusao social dentro da escola.

O grupo identificado como *"Altamente Excluido"* apresentou pontuacoes drasticamente maiores de recusa escolar, com tamanho de efeito grande (d = 1,15 na dimensao de antecipacao ansiosa) em comparacao ao grupo altamente incluido. Isso reforca que o sentimento de exclusao e nao pertencimento e uma feature critica para triagem precoce.

---

### 20. S0091 — Sorrenti et al. (2026): *Understanding School Non-Attendance in Adolescence: Perceived Competence, Psychological and Social Barriers, and Educational Vulnerability*
Este artigo italiano validou a nova escala ARSNA (13 itens e 4 fatores focados em barreiras psicologicas e sociais a frequencia escolar) em mais de 1.100 adolescentes de 14 a 19 anos (391 na exploratoria, 593 na confirmatoria e 183 no segundo estudo preditivo).

A escala atingiu bom ajuste (CFI = 0,90; RMSEA = 0,07) e confiabilidade entre 0,62 e 0,78. Na segunda etapa, uma regressao hierarquica testou quanto a percepcao de competencia do aluno (geral e academica) explicava o comportamento de recusa escolar.

Os resultados mostraram que quanto menor a percepcao de competencia geral e academica do adolescente, maior a tendencia a recusa escolar (explicando 25,7% da variancia). E mais um instrumento recente que captura barreiras subjetivas nao registradas nos diarios de classe.

---

### 21. S0145 — Moller et al. (2025): *Early Identification of School Refusal from Parents' Perspectives*
Realizado na Noruega, este estudo partiu da perspectiva das familias para mapear os primeiros sinais visiveis em casa antes de o aluno parar de ir a escola. Na primeira fase, 196 pais relataram sinais iniciais observados; na segunda fase, 509 pais responderam a um questionario estruturado de 30 itens.

Por meio de Analises Fatoriais Exploratoria e Confirmatoria, os autores chegaram a uma estrutura de 24 itens em 7 fatores (como queixas somaticas matinais, sofrimento ao falar da escola e mudancas emocionais), com indice KMO de 0,86 e ajuste confirmatorio aceitavel (CFI = 0,871; RMSEA = 0,070).

Um dado muito util relatado pelos pais e que a idade media de inicio dos primeiros sinais de recusa escolar foi de 10,1 anos — mostrando que a prevencao precisa comecar ainda no Ensino Fundamental, antes da transicao para o Ensino Medio.

---

### 22. S0154 — Husa et al. (2022): *Pre-Birth Household Challenges Predict Future Child's School Readiness and Academic Achievement*
Utilizando dados populacionais do Alasca (3.549 respondentes representando 33.417 criancas ponderadas), os autores investigaram se adversidades familiares presentes antes mesmo do nascimento (medidas por 14 indicadores do questionario CDC PRAMS, como violencia, estresse financeiro e instabilidade) predizem absenteismo cronico anos depois na escola.

Aplicando modelos lineares generalizados (Quasi-Poisson) sobre dados longitudinais vinculados a rede publica de ensino, observaram que 22% das criancas apresentaram absenteismo cronico (frequencia abaixo de 90%).

Criancas expostas a 4 ou mais desafios familiares pre-natais tiveram risco 29% maior de desenvolver absenteismo cronico escolar (*ARR = 1,29*). O estudo amplia a visao da RQ3 ao mostrar o peso de determinantes familiares precoces no historico de frequencia.

---

### 23. S0030 — Benjamin et al. (2022): *Developing an Anxiety Screening Tool for Children in South Africa: Protocol for a Mixed Methods Study*
Este trabalho e um protocolo metodologico publicado na Africa do Sul para criar uma ferramenta culturalmente adaptada de triagem de ansiedade infantil (criancas de 4 a 8 anos) aplicada por professores em ambiente escolar.

O desenho preve revisao de escopo, entrevistas qualitativas com 60 participantes, painel de especialistas e-Delphi e um estudo piloto com cerca de 400 professores usando Analise Fatorial Exploratoria, apoiado em escalas consolidadas como SCARED, SCAS e PAS.

Como se trata de um protocolo publicado, ainda nao ha resultados empiricos ou metricas de validacao, mas o estudo e relevante para mapear iniciativas de triagem escolar precoce em paises em desenvolvimento.

---

### 24. S0075 — Sahoo et al. (2024): *School Refusal Behavior: A Narrative Review*
Esta revisao narrativa sintetiza 38 estudos originais publicados ao longo de 10 anos (buscados na MEDLINE e Scopus) para oferecer um panorama clinico-educacional atualizado sobre o comportamento de recusa escolar.

O artigo revisa criterios diagnosticos, fatores de risco individuais/familiares e principais escalas clinicas utilizadas na pratica (como SRAS, ISAP, CBCL e TRF), alem de resumir estrategias de intervencao multidisciplinar entre familia, escola e equipe de saude.

Os autores reportam que a prevalencia global de recusa escolar varia de 2% a 16% dependendo do criterio adotado (chegando a cerca de 7% em estudos indianos), servindo como um bom texto de contextualizacao geral para a introducao da RSL.

---

## Parte III — Estudos Excluidos Apos Leitura do PDF Completo (2 estudos)

### 25. S0133 — Jain et al. (2025): *A PSO weighted ensemble framework with SMOTE balancing for student dropout prediction in smart education systems*
Embora este artigo apresente uma arquitetura tecnicamente interessante (combinando Random Forest, XGBoost, otimizacao por enxame de particulas PSO, balanceamento SMOTE e explicabilidade SHAP), a leitura integral do PDF revelou que todos os experimentos foram conduzidos exclusivamente com o conhecido dataset da UCI de **Ensino Superior** (4.424 estudantes universitarios), usando apenas variaveis academicas e financeiras. Como nao aborda educacao basica nem recusa escolar ou fatores socioemocionais, foi formalmente excluido pelo criterio **EC2**.

### 26. S0153 — Chen et al. (2022): *Transactions between Problem Behaviors and Academic Performance in Early Childhood*
Este estudo longitudinal acompanhou 18.135 criancas americanas da coorte ECLS-K:2011 (do jardim de infancia ao 3o ano) usando modelos de painel cruzado para investigar a relacao entre problemas comportamentais e desempenho academico. No entanto, a leitura completa confirmou que o trabalho mede apenas notas em testes padronizados de leitura e matematica (IRT) e comportamento em sala, sem mensurar faltas, absenteismo ou recusa escolar. Por nao atender ao desfecho do protocolo, foi excluido pelo criterio **EC2**.
