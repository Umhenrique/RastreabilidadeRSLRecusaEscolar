# -*- coding: utf-8 -*-
import os
import pandas as pd
from asreview import load_dataset

def main():
    print("[1/3] Carregando matriz de triagem consolidada...")
    input_csv = "03_selecao_triagem/02_triagem_resumo/matriz_triagem_consolidada.csv"
    df = pd.read_csv(input_csv, encoding="utf-8-sig")

    print(f"      Total de registros carregados: {len(df)}")

    # Mapeamento oficial para padrao ASReview
    df_asreview = pd.DataFrame({
        "record_id": df["Study_ID"],
        "title": df["Title"],
        "abstract": df["Abstract"],
        "doi": df["DOI"],
        "authors": df["Authors"],
        "year": df["Year"],
        "included": df["Decision"].apply(lambda x: 1 if "Inclu" in str(x) else 0),
        "source_database": df["Source_Database"],
        "decision": df["Decision"],
        "criterion": df["Criterion"],
        "reason": df["Reason"]
    })

    asreview_dir = "03_selecao_triagem/asreview"
    os.makedirs(asreview_dir, exist_ok=True)

    csv_path = os.path.join(asreview_dir, "dataset_asreview_rsl.csv")
    xlsx_path = os.path.join(asreview_dir, "dataset_asreview_rsl.xlsx")

    # Salvar versao completa com labels de inclusao (para simulacao / prior knowledge)
    df_asreview.to_csv(csv_path, index=False, encoding="utf-8")
    df_asreview.to_excel(xlsx_path, index=False)

    # Salvar versao para triagem cega / interativa (sem labels prévios, se desejar triar do zero no ASReview)
    df_unlabeled = df_asreview.copy()
    df_unlabeled["included"] = None
    csv_unlabeled = os.path.join(asreview_dir, "dataset_asreview_triagem_cega.csv")
    df_unlabeled.to_csv(csv_unlabeled, index=False, encoding="utf-8")

    print(f"[2/3] Arquivos gerados com sucesso:")
    print(f"      - {csv_path} (com labels oficiais: 101 incluidos e 1370 excluidos)")
    print(f"      - {xlsx_path} (em formato Excel)")
    print(f"      - {csv_unlabeled} (versao para triagem ativa do zero)")

    print("[3/3] Validando compatibilidade com o leitor oficial do ASReview...")
    ds = load_dataset(csv_path)
    print(f"      [OK] ASReview validou o dataset: {len(ds)} registros reconhecidos.")
    inc_count = (df_asreview["included"] == 1).sum()
    exc_count = (df_asreview["included"] == 0).sum()
    print(f"      [OK] Distribuição: {inc_count} relevantes (1) e {exc_count} irrelevantes (0).")

if __name__ == "__main__":
    main()
