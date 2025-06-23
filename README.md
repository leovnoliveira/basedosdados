# 📊 Case Técnico - Base dos Dados

Repositório criado para o desafio técnico de Engenheiro de Dados da [Base dos Dados](https://basedosdados.org/).


## Descrição

### Pipeline de ELT: Trade Cites Database para BigQuery
Esta primeira etapa do pipeline de dados, que consiste em extrair, carregar e transformar (ELT) os dados brutos da Trade Cites Database. Os dados originais possuem 16 colunas e estão armazenados em arquivos .csv localizados na pasta `data/raw`, tendo sido baixados diretamente do site oficial. Devido ao grande volume de dados e limitações de consulta impostas pelo site, o download foi realizado de forma reparticionada, abrangendo o período de 1975 a 2024.

## 💡 Sobre o Projeto

Este projeto demonstra um fluxo completo de **ETL/ELT** aplicado a dados públicos, com as seguintes etapas:

- **Extração** dos dados originais em formato Parquet (disponíveis em pastas anuais).
- **Transformação**: limpeza, padronização, tratamento de nulos, renomeação e ajuste de tipos.
- **Carregamento** dos dados tratados em um banco de dados **PostgreSQL** para análises SQL locais.

Etapas principais:
- Extração dos arquivos .csv brutos da pasta `data/raw`
- Tratamento e padronização dos dados (nível bronze)
- Transformações e validações adicionais (nível silver)
- Dados tratados, particionados e salvos em `data/ouput`

Cobertura temporal dos dados: 1975 a 2024.
"""

### 📂 Estrutura dos Dados

- Dados organizados por ano em arquivos Parquet (`data/output/ano=YYYY/data.parquet`)
- Dados consolidados em um único DataFrame no Python.
- Upload do DataFrame final para uma tabela no banco PostgreSQL: `comercio_especies_ameacadas`.

## 🚀 Como Reproduzir Localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/leovnoliveira/basedosdados.git
cd basedosdados
```

## 2. Criar ambiente virtual e instalar dependências

Com Poetry:
```bash
poetry env activate
poetry install
```
Com o uv:
```bash
uv init
uv venv --python 3.10 #para usar a versão 3.10 do Python, a mesma que a minha
source .venv/bin/activate #no Linux ou MacOS
source .venv/Scripts/activate #em Windows
uv pip install -r requirements.txt
```
Ou com o pip:
```bash
python3 -m venv .venv
source .venv/bin/activate #no Linux ou MacOS
source .venv/Scripts/activate #em Windows
pip install -r requirements.txt
``` 

## 3. Configurar o PostgreSQL

* Instale o PostgreSQL localmente (ou rode via Docker).
* Crie um banco de dados chamado `mundo_cites`:

```sql
CREATE DATABASE mundo_cites;
```
* Defina a senha do usuário postgres (exemplo: senha123).
* Ajuste o arquivo `.env-example` - e renomeei-o para `.env` com os dados de acesso:

```ini
DB_PORT=5432
DB_NAME=mundo_cites
DB_USER=postgres
PASSOWORD_POSTEGRES=senha123
```
## 4. Rodar o ETL
Execute o script de ingestão para popular a tabela no banco de dados:

```bash
python src/database.py
```


## Stacks Utilizadas

- **pyenv**: Utilizado para o versionamento do Python, garantindo que o projeto utilize a versão correta e facilitando a gestão de múltiplas versões no mesmo ambiente.
- **uv**: Ferramenta para gerenciamento de ambientes virtuais e instalação eficiente de dependências, proporcionando ambientes isolados e reprodutíveis para o desenvolvimento e execução da task.
- **Python**: (`pandas`, `sqlalchemy`, `python-dotenv`)
- **PostgreSQL**
- **Parquet**
- **Docker** (opcional)
- **WSL** (Linux local via Windows Subsystem for Linux)
""

## 🔍 Como acessar e consultar o banco de dados PostgreSQL
Você pode usar ferramentas como PGAdmin, DBeaver ou o próprio terminal.

### Conectando via linha de comando
```bash
psql -U postgres -h localhost -p 5432 -d mundo_cites
```
Digite a senha quando solicitado (senha123).

### Consultando registros
Exemplo de consulta para ver as primeiras linhas:

```sql
SELECT * FROM comercio_especies_ameacadas LIMIT 10;
```
### Consultar proporção de valores não nulos em uma coluna
```sql
SELECT 
    100.0 * COUNT(nome_cientifico) / COUNT(*) AS perc_not_null
FROM comercio_especies_ameacadas;
```

## 📝 Observações
Caso encontre problemas de conexão, certifique-se que o serviço do PostgreSQL está rodando e ouvindo na porta correta.

Os scripts Python e SQL podem ser facilmente adaptados para outros bancos relacionais.

Documentação e comentários no código orientam o passo-a-passo para manutenção e reuso do pipeline.

