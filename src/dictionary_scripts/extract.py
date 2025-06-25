import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()

# Configuração da conexão: ajuste usuário/senha se mudou!
usuario = os.getenv('DB_USER')
senha = os.getenv('PASSWORD_POSTGRES')         # Sua senha
host = 'localhost'
porta = os.getenv('DB_PORT')
banco = os.getenv('DB_NAME')
# Parâmetros da sua conexão
engine = create_engine(f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')


covered_by_dictionary = ['term', 'purpose', 'source']

for coluna in covered_by_dictionary:
    cols = pd.read_sql(f"SELECT {coluna} FROM trade_endangered_species LIMIT 1", engine).columns
    for col in cols:
        uniques = pd.read_sql(f"SELECT DISTINCT {col} FROM trade_endangered_species WHERE {col} IS NOT NULL", engine)
        base_path = os.path.abspath(os.path.join(os.path.dirname(__name__), "data", "columns"))
        uniques.to_csv(os.path.join(base_path, f'unique_{col}.csv'), index=False)


