# B3

import pandas as pd 

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

try:
    df_abertos_1000 = df[(df["Status"] == "Em andamento") & (df["Valor_Total"] > 1000)]
    print(df_abertos_1000)
except KeyError:
    print("Nome da(s) coluna(s) não encontrado(as) no arquivo.")
