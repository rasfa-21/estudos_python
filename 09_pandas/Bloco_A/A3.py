# A3 

import pandas as pd

CAMINHHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHHO_ARQUIVO)

print(df['Valor_Total']) # imprime a coluna "valor_Total"
print()
print(df[["Cliente", "Status"]]) # imprime as duas colunas juntas (df[['coluna1', 'coluna2']])
