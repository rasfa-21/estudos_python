# A4

import pandas as pd 

CAMINHO_ARQUIVO =  r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

print(df.shape)     # retorna tupla com (qtd_linhas, qtd colunas)
print(df.columns)   # lista os nomes das colunas 

