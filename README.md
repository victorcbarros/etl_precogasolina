# Extração e Processamento de Dados de Preços de Gasolina

## Visão Geral
Este projeto tem como objetivo extrair, processar e transformar tabelas de preços de gasolina contidas em arquivos PDF em um formato estruturado no Excel. Utilizamos a biblioteca **Camelot** para extração de tabelas, **Pandas** para tratamento dos dados e manipulação de DataFrames, e **OS** para gerenciamento de arquivos.

## Estrutura do Projeto
- **etl_pdf.py**: Script principal responsável por realizar a extração, processamento e exportação dos dados.
- **files/**: Diretório onde os arquivos PDF de origem devem ser armazenados.
- **Preços de Gasolina A sem tributos, à vista, por vigência.xlsx**: Arquivo gerado contendo os dados tratados e consolidados.
- **pyproject.toml**: Arquivo de configuração do Poetry para gerenciamento de dependências.

## Funcionamento do Script
O script executa as seguintes etapas:

1. **Leitura do PDF**: 
   - Define o nome do arquivo a ser processado e sua localização.
   - Utiliza a biblioteca **Camelot** para extrair as tabelas das páginas do PDF.

2. **Tratamento dos Dados**:
   - **Função `tratamento_dataframe(df)`**:
     - Mescla cabeçalhos divididos em várias linhas.
     - Remove linhas desnecessárias.
     - Renomeia as colunas corretamente.
   
   - **Função `converter_colunas_numericas(df)`**:
     - Identifica colunas numéricas.
     - Converte valores formatados como string para números corretamente, lidando com separadores de milhar e decimais.

3. **Concatenação das Tabelas**:
   - Agrupa os DataFrames extraídos e tratados em um único DataFrame consolidado.
   - Remove colunas duplicadas para manter um formato limpo e padronizado.

4. **Exportação para Excel**:
   - Salva o DataFrame final no arquivo **Preços de Gasolina A sem tributos, à vista, por vigência.xlsx**.

## Configuração do Ambiente com Poetry
Este projeto utiliza o **Poetry** para gerenciamento de dependências. Siga os passos abaixo para configurar o ambiente:

### Instalação do Poetry
Caso não tenha o **Poetry** instalado, execute:
```sh
pip install poetry
```

### Instalação das Dependências
Com o **Poetry** instalado, navegue até a pasta do projeto e execute:
```sh
poetry install
```
Isso instalará todas as dependências listadas no **pyproject.toml**.

### Ativação do Ambiente Virtual
Para ativar o ambiente virtual do **Poetry**, utilize:
```sh
poetry shell
```

## Como Executar
1. Certifique-se de que o arquivo PDF desejado está na pasta `files/`.
2. Altere a variável `file_name` no script `etl_pdf.py` para corresponder ao nome correto do arquivo PDF.
3. Execute o script dentro do ambiente Poetry com o comando:
```sh
poetry run python etl_pdf.py
```
4. O arquivo Excel gerado estará disponível no diretório de execução do script.

## Observações
- O script foi configurado para processar PDFs com um formato específico de tabelas. Se houver alterações na estrutura do PDF, pode ser necessário ajustar os parâmetros do `camelot.read_pdf()`.
- Caso alguma tabela não seja extraída corretamente, verifique a área definida no parâmetro `table_areas` e ajuste conforme necessário.

## Autor
Victor C. Barros

