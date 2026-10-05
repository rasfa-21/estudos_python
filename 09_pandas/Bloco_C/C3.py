# C3 

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

# agrupando por status e calculando a media por cada grupo

df_media_por_status = df.groupby("Status")["Valor_Total"].mean() #.mean() calcula a media 

print(df_media_por_status)
