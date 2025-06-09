# Pipeline de ELT: Trade Cites Database para BigQuery

## Descrição
Esta task refere-se à primeira etapa do pipeline de dados, que consiste em extrair, carregar e transformar (ELT) os dados brutos da Trade Cites Database. Os dados originais possuem 14 colunas e estão armazenados em arquivos .csv localizados na pasta `data/raw`, tendo sido baixados diretamente do site oficial. Devido ao grande volume de dados e limitações de consulta impostas pelo site, o download foi realizado de forma reparticionada, abrangendo o período de 1975 a 2024.

## Objetivo 

O objetivo desta etapa é tratar os dados brutos (nível raw) para um estágio bronze, realizando limpezas e padronizações iniciais, posteriormente evoluindo para o nível silver, onde serão aplicadas transformações adicionais e validações. Após essas etapas, os dados estarão prontos para serem carregados no BigQuery da Base dos Dados, garantindo qualidade, integridade e usabilidade para análises futuras.

Etapas principais:
- Extração dos arquivos .csv brutos da pasta `data/raw`
- Tratamento e padronização dos dados (nível bronze)
- Transformações e validações adicionais (nível silver)
- Dados tratados, particionados e salvos em `data/ouput`
- Carga final dos dados tratados no BigQuery da Base dos Dados

Cobertura temporal dos dados: 1975 a 2024.
"""

## Stacks Utilizadas

- **pyenv**: Utilizado para o versionamento do Python, garantindo que o projeto utilize a versão correta e facilitando a gestão de múltiplas versões no mesmo ambiente.
- **uv**: Ferramenta para gerenciamento de ambientes virtuais e instalação eficiente de dependências, proporcionando ambientes isolados e reprodutíveis para o desenvolvimento e execução da task.
""
Processo de ELT dos dados da Trade Cites Database para o BigQuery da Base dos Dados (basedosdados.org).
