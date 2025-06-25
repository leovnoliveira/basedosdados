import pandas as pd
import glob
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# Caminho do arquivo parquet
caminho_parquet = os.path.abspath(os.path.join(os.path.dirname(__name__), "data", "output"))
anos = sorted([d for d in os.listdir(caminho_parquet) if d.startswith("year=")])
arquivos_path = [os.path.join(caminho_parquet, ano, "data.parquet") for ano in anos]

# Leia o parquet com pandas
df = pd.concat([pd.read_parquet(parquet_path) for parquet_path in arquivos_path], ignore_index=True)

# Configuração da conexão: ajuste usuário/senha se mudou!
usuario = os.getenv('DB_USER')
senha = os.getenv('PASSWORD_POSTGRES')         # Sua senha
host = 'localhost'
porta = os.getenv('DB_PORT')
banco = os.getenv('DB_NAME')

engine = create_engine(f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')

# Exemplo: nome da tabela no PostgreSQL
nome_tabela = 'trade_endangered_species'

# Se já existe, pode usar if_exists='replace' para sobrescrever, ou 'append' para adicionar
df.to_sql(nome_tabela, engine, if_exists='replace', index=False)

print('Upload concluído!')
