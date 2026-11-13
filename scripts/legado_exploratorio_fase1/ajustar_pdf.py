import re

with open('scripts/gerar_pdf_artigo.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Substituir o trecho do PICOC
pattern = r'<h3 class="subsection-title">A\. Estrutura do Estudo \(PICOC\)</h3>.*?</ul>'
replacement = """<h3 class="subsection-title">A. Estrutura do Estudo (Critério PICOC)</h3>
  <p class="no-indent">O escopo da investigação estrutura-se estritamente nos seguintes eixos:</p>
  <ul>
    <li><strong>Population:</strong> Ensino Básico</li>
    <li><strong>Intervention:</strong> IA (Ferramentas de diagnóstico ou diagnóstico)</li>
    <li><strong>Outcomes:</strong> Recusa escolar OR (evasão escolar AND socio-emotional factor)</li>
  </ul>"""

new_text = re.sub(pattern, replacement, text, flags=re.DOTALL)

with open('scripts/gerar_pdf_artigo.py', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("PICOC ajustado com sucesso em scripts/gerar_pdf_artigo.py!")
