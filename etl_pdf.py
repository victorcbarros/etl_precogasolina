import os
import camelot
import pandas as pd

#função que trata o dataframe
def tratamento_dataframe(df):
    df.iloc[0] = df.iloc[0].fillna('') + ' ' + df.iloc[2].fillna('')
    df = df.drop(2).reset_index(drop=True)
    df.iloc[0] = df.iloc[0].fillna('') + df.iloc[1].fillna('')
    df = df.drop(1).reset_index(drop=True)
    df.columns = df.iloc[0]
    df = df.drop(0)
    return df 

#função que converte as colunas numéricas
def converter_colunas_numericas(df):
    # Função para converter string para float
    def converter_para_float(value):
        if isinstance(value, str):  
            # Remove separador de milhar e troca vírgula por ponto
            value = value.replace('.', '').replace(',', '.')  
        return pd.to_numeric(value, errors='coerce')  

    # Identificar colunas numéricas (assumindo que as 2 primeiras colunas são texto)
    numeric_columns = df.columns[2:]  # Do índice 2 em diante

    # Aplicar a conversão apenas nas colunas numéricas
    df[numeric_columns] = df[numeric_columns].applymap(converter_para_float)
    
    return df

#nome do arquivo
file_name = 'Gasolina 01-02-25'
#path do arquivo
path = os.path.abspath(f'files/Tabelas de Preços - {file_name}.pdf')

#leitura do arquivo e extração das tabelas
tables = camelot.read_pdf(
    path,
    pages='1-9',
    flavor='stream',
    table_areas=['9, 776, 573, 42']
)


#tratamento das tabelas criando um dicionário de dataframes
dfs = {}
for i, table in enumerate(tables, start=1):
    dfs[f'df{i}'] = table.df

#tratamento dos dataframes atraves das funções criadas e do dicionario de dataframes
dfs = {key: tratamento_dataframe(df) for key, df in dfs.items()}

#conversão das colunas numéricas atraves do dicionario de dataframes
dfs = {key: converter_colunas_numericas(df) for key, df in dfs.items()}

#concatenação dos dataframes ja que são os mesmos dados em todas as tabelas
df_concatenado = pd.concat(dfs.values(), axis=1)

#remoção de colunas duplicadas retirando as colunas de nome da cidade e modalidade de vendas
df_concatenado = df_concatenado.loc[:, ~df_concatenado.columns.duplicated()]

#salvando o arquivo em excel 
df_concatenado.to_excel('Preços de Gasolina A sem tributos, à vista, por vigência.xlsx', index=False)