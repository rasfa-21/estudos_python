# B10

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

df_filtrados = df[(df["Status"] == "Concluído") | (df["Valor_Total"] > 2000)]
resultado = len(df_filtrados)

print(resultado)
print(df_filtrados)