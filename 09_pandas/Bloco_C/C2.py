# C2 

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

# agrupando por tipo e somando o valor de cada um

df_soma_por_tipo = df.groupby("Tipo")["Valor_Total"].sum()

print(df_soma_por_tipo)


