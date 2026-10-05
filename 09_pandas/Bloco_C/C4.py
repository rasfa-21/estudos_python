# C4

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

# agrupando por fazenda e obtendo varias métricas com .agg([...])

df_metricas = df.groupby("Cliente")["Valor_Total"].agg(["sum", "mean", "count"])

print(df_metricas)