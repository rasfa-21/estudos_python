# A5

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

print(df.iloc[0])      # acessa a PRIMEIRA linha, por posição (0, 1, 2...)
print(df.loc[0])       # acessa a linha pelo "rótulo" do índice (geralmente igual ao número, mas nem sempre)