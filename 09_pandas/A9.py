# A9

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

# renomeando a coluna 'Cliente' para 'Fazenda'
df = df.rename(columns={"Cliente": "Fazenda"})

print(df.columns)

