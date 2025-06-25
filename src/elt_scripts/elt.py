import os
import glob
import numpy as np
import pandas as pd

def data_path():
    """
    Returns the absolute path to the data directory.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "data", "raw"))

def get_all_csv_files() -> list:
    """
    Returns a list of all CSV files in the data directory.
    """
    dir_path = data_path()

    # Using glob to find all CSV files
    return glob.glob(os.path.join(dir_path, "*.csv"))


def load_and_concat_csv(files: list) -> pd.DataFrame:
    """
    Loads multiple CSV files and concatenates them into a single DataFrame.
    Args:
        files (list): List of CSV file names to load.
    Returns:
        pd.DataFrame: Concatenated DataFrame containing all data from the specified CSV files.
    """

    dataframes = []
    for file_path in files:
        df = pd.read_csv(file_path)
        dataframes.append(df)


    return pd.concat(dataframes, ignore_index=True)

def rename_and_treat_columns(df: pd.DataFrame, column_mapping: dict) -> pd.DataFrame:
    """
    Renames columns in a DataFrame based on a provided mapping.
    Args:
        df (pd.DataFrame): DataFrame to rename columns in.
        column_mapping (dict): Dictionary mapping old column names to new column names.
    Returns:
        pd.DataFrame: DataFrame with renamed columns.
    """
    # Remove espaços extras das colunas
    df.columns = [col.strip() for col in df.columns]
    # Renomeia usando o dict
    df = df.rename(columns=column_mapping)
    # (Opcional) Deixa todas as colunas em minúsculas
    df.columns = [col.lower() for col in df.columns]
    return df

def apply_typing(df, typing: dict) -> pd.DataFrame:
    """ Applies data type conversions to specified columns in a DataFrame.
    Args:
        df (pd.DataFrame): DataFrame to apply typing to.
        typing (dict): Dictionary mapping column names to their desired data types.
    Returns:
        pd.DataFrame: DataFrame with columns converted to specified data types.
    """

    for col, tipo in tipagem.items():
        if col in df.columns:
            if tipo == 'int':
                df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
            elif tipo == 'float':
                df[col] = pd.to_numeric(df[col], errors='coerce')
            else:
                df[col] = df[col].astype(str).str.strip()
    return df


def convert_to_parquet(df: pd.DataFrame, output_file: str) -> None:
    """
    Converts a DataFrame to a Parquet file.
    Args:
        df (pd.DataFrame): DataFrame to convert.
        output_file (str): Path to the output Parquet file.
    """
    df.to_parquet(output_file, engine='pyarrow', index=False)
    print(f"Data successfully converted to {output_file}")


def replace_nan_to_none(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces NaN values in a DataFrame with None.
    Args:
        df (pd.DataFrame): DataFrame to process.
    Returns:
        pd.DataFrame: DataFrame with NaN values replaced by None.
    """
    colunas = df.columns
    for coluna in colunas:
        df[coluna] = df[coluna].replace(['nan', 'NaN', np.nan, ''], None)

    return df

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drops duplicate rows from a DataFrame.
    Args:
        df (pd.DataFrame): DataFrame to process.
    Returns:
        pd.DataFrame: DataFrame with duplicate rows removed.
    """
    return df.drop_duplicates()


def split_df_by_year_and_convert_to_parquet(df, output_dir='data/output'):
    """
    Splits a DataFrame into a dictionary of DataFrames by year.
    Args:
        df (pd.DataFrame): DataFrame to split.
    Returns:
        dict: Dictionary with years as keys and DataFrames as values.
    """
    anos = df['year'].unique()
    

    for ano in anos:
        df_ano = df[df['year'] == ano]
        output_path = os.path.join(output_dir, f"year={ano}")
        os.makedirs(output_path, exist_ok=True)
        save_path = os.path.join(output_path, "data.parquet")
        df_ano.to_parquet(save_path, index=False)
        print(f"Ano: {ano} | Linhas: {len(df_ano)} | Salvo em: {save_path}")

    return df

if __name__ == "__main__":

    dir_path = data_path()
    csv_files = get_all_csv_files()
    if not csv_files:
        print("No CSV files found in the data directory.")
    else:
        df = load_and_concat_csv(csv_files)
        column_mapping = {
            'Year': 'year',
            'App.': 'cites_appendix',
            'Taxon': 'scientific_name',
            'Class': 'taxonomic_class',
            'Order': 'taxonomic_order',
            'Family': 'taxonomic_family',
            'Genus': 'taxonomic_genus',
            'Importer': 'importer_country',
            'Exporter': 'exporter_country',
            'Origin': 'origin_country',
            'Importer reported quantity': 'importer_reported_quantity',
            'Exporter reported quantity': 'exporter_reported_quantity',
            'Term': 'term',
            'Unit': 'unit_of_measure',
            'Purpose': 'purpose',
            'Source': 'source',
        }
        tipagem = {
            'year': 'int',
            'cites_appendix': 'str',
            'scientific_name': 'str',
            'taxonomic_class': 'str',
            'taxonomic_order': 'str',
            'taxonomic_family': 'str',
            'taxonomic_genus': 'str',
            'importer_country': 'str',
            'exporter_country': 'str',
            'origin_country': 'str',
            'importer_reported_quantity': 'float',
            'exporter_reported_quantity': 'float',
            'term': 'str',
            'unit_of_measure': 'str',
            'purpose': 'str',
            'source': 'str'
        }

        df = rename_and_treat_columns(df, column_mapping)
        df = apply_typing(df, tipagem)
        df = replace_nan_to_none(df)
        df = drop_duplicates(df)
        split_df_by_year_and_convert_to_parquet(df, output_dir='data/output')

