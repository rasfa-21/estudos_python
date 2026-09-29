# A6 

import pandas as pd 

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"
df = pd.read_excel(CAMINHO_ARQUIVO)

# pegar o nome das colunas 
print(df.columns)

# contagem por status
print(df["Status"].value_counts())


