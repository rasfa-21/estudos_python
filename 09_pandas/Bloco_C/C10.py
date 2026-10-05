# C10

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

df_concluidos = df[df["Status"] == "Concluído"]

df_concluidos_estado = df_concluidos.groupby("Estado")["Valor_Total"].sum()

estado_campeao = df_concluidos_estado.idxmax() # dava pra aplicar o metodo diretamente tambem

print(estado_campeao)