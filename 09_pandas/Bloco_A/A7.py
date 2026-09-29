# A7. Descobrir quais produtos e quantos sao

import pandas as pd

CAMINHO_ARQUIVO =  r"09_pandas\dados_didaticos.xlsx"
df = pd.read_excel(CAMINHO_ARQUIVO)

print(df["Produto"].unique()) # lista dos valores DISTINTOS da coluna (sem repetição) nesse caso nome dos produtos
print(df["Produto"].nunique()) # QUANTOS valores distintos existem (um número) nesse caso a qntd de produtos




