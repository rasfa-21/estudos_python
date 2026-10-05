# C5

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

# agrupando duas colunas e somando 
df_tec_status = df.groupby(["Tipo", "Status"]).sum()

print(df_tec_status)