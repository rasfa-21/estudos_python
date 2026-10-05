# C7

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

df_group_status_bruto = df.groupby("Status")["Valor_Total"].size()   # .size() conta todas as linhas 
df_group_status = df.groupby("Status")["Valor_Total"].count()        # .count() ignora linhas faltando

print(df_group_status_bruto)
print()
print(df_group_status)
