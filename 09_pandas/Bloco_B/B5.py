# B5

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

df_outros_chamados = df[(df["Tipo"] != "Manutenção")]

print(df_outros_chamados)

