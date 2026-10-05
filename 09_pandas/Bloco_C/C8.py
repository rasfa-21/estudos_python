# C8 

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

# .sort_values() ordena por padrao (ordem crescente)
df_estado = df.groupby("Estado")["Valor_Total"].sum().sort_values(ascending=False)

print(df_estado)