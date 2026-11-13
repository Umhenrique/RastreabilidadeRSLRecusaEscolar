#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para remocao completa de emojis de todos os arquivos Markdown e de texto do repositorio.
"""

import os
import re

# Lista de codepoints de emojis conhecidos e ranges
def remove_emojis_from_text(text):
    # Substituir emojis especificos de status no checklist por texto formal
    text = text.replace('\u2705', '[Concluido]').replace('\u23F3', '[Em Andamento]').replace('\u26A0', '[Pendente]').replace('\U0001F6A8', '[Atencao]')
    
    # Remover variacao e seletores
    text = text.replace('\uFE0E', '').replace('\uFE0F', '').replace('\u200D', '')
    
    # Regex para todos os emojis comuns e pictogramas
    emoji_regex = re.compile(
        r'['
        r'\U0001F300-\U0001FAFF'  # Todos os blocos suplementares de emojis
        r'\U00002600-\U000027BF'  # Simbolos diversos e dingbats (escalas, raios, avisos)
        r'\U00002300-\U000023FF'  # Simbolos tecnicos (ampulheta, etc.)
        r'\U00002B50-\U00002B55'  # Estrelas e circulos
        r']+',
        flags=re.UNICODE
    )
    
    cleaned = emoji_regex.sub('', text)
    
    # Limpar espacos duplos em cabecalhos decorrentes da remocao do emoji
    cleaned = re.sub(r'^(#{1,6})\s{2,}', r'\1 ', cleaned, flags=re.MULTILINE)
    # Limpar espacos duplos apos marcadores de lista
    cleaned = re.sub(r'^(\s*[-*])\s{2,}', r'\1 ', cleaned, flags=re.MULTILINE)
    # Limpar espacos no inicio de linhas dentro de callouts
    cleaned = re.sub(r'^(>\s*[-*]?)\s{2,}', r'\1 ', cleaned, flags=re.MULTILINE)
    
    return cleaned

def main():
    root_dir = "."
    modified_count = 0
    total_files = 0
    
    for r, dirs, files in os.walk(root_dir):
        if ".obsidian" in r or ".git" in r or "tools" in r:
            continue
        for f in files:
            if f.endswith(".md") or f.endswith(".txt"):
                total_files += 1
                fpath = os.path.join(r, f)
                try:
                    with open(fpath, "r", encoding="utf-8") as fh:
                        orig = fh.read()
                except UnicodeDecodeError:
                    continue
                    
                cleaned = remove_emojis_from_text(orig)
                if cleaned != orig:
                    with open(fpath, "w", encoding="utf-8") as fh:
                        fh.write(cleaned)
                    modified_count += 1
                    print(f"Limpo: {fpath}")
                    
    print(f"\nVarredura concluida: {modified_count} de {total_files} arquivos foram limpos.")

if __name__ == "__main__":
    main()
