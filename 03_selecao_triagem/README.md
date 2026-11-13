# Processo de Seleção e Triagem dos Estudos

Esta pasta armazena os registros e planilhas das etapas de triagem.

---

## 1. Etapas do Processo

```
[Buscas Brutas Consolidadas]
         │
         ▼
[Etapa 1: Deduplicação] ──► Artigos Duplicados Removidos (salvos em 01_deduplicacao/)
         │
         ▼
[Artigos Únicos]
         │
         ▼
[Etapa 2: Triagem Título & Resumo] ──► Excluídos com Motivo (CE) (em 02_triagem_resumo/)
         │
         ▼
[Artigos Pré-Selecionados]
         │
         ▼
[Etapa 3: Leitura de Texto Completo] ──► Excluídos pós-leitura integral (em 03_leitura_completa/)
         │
         ▼
[Artigos Incluídos na RSL] ──► Seguem para Extração e Síntese
```

---

## 2. Padrão de Codificação de Artigos

Para garantir rastreabilidade, cada estudo único deve receber um identificador:
- Formato: `ID_ESTUDO` (Ex: `S001`, `S002`, `S003`...)
- Cada decisão deve ter:
  - **Decisão:** `[INCLUÍDO / EXCLUÍDO / DUPLICADO / DÚVIDA]`
  - **Motivo de Exclusão:** Código do critério violado (ex: `CE1`, `CE2`, `CE3`...).
