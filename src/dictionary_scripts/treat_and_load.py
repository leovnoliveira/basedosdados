import os
import glob
import pandas as pd

data_dir = os.path.abspath(os.path.join(os.path.dirname(__name__), "data", "columns"))
archives = [d for d in os.listdir(data_dir) if d.endswith(".csv")]

def add_news_columns() -> pd.DataFrame:
    id_tabela = 'trade_endangered_species'
    cobertura_temporal = '(1)'
    dfs = []
    for archive in archives:
        name_archive = os.path.basename(archive)
        nome_coluna = name_archive.split('_')[1].split('.')[0]
        df = pd.read_csv(os.path.join(data_dir, archive))
        # Add cols
        df['id_tabela'] = id_tabela
        df['nome_coluna'] = nome_coluna
        df["cobertura_temporal"] = cobertura_temporal
        # Reorganiza para o modelo da BD
        df = df[["id_tabela", "nome_coluna", "chave", "cobertura_temporal", "valor"]]
        dfs.append(df)

    df_final = pd.concat(dfs, ignore_index=True)

    return df_final

def load_csv():
    df = add_news_columns()
    dicionario_dir = os.path.join(data_dir, "..", "dicionario")
    if not os.path.exists(dicionario_dir):
        os.makedirs(dicionario_dir)
        df.to_csv(os.path.join(dicionario_dir, "dicionario.csv"), index=False)

if "__main__" == __name__:
    # df = load_data()
    df = add_news_columns()
    print(df)
    load_csv()