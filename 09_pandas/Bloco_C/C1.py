# C1

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

# .size() conta quantas linhas existem para cada grupo da coluna informada
df_chamados_por_tipo = df.groupby("Tipo").size()

print(df_chamados_por_tipo)
