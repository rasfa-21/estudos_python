# C6

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

# pegando o maximo de cada tipo
df_max_por_tipo = df.groupby("Tipo")["Valor_Total"].max()

print(df_max_por_tipo)
