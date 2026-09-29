# B9

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

# "quero SÓ estas colunas, das linhas que atendem a esta condição", numa expressão só.
# formato: df.loc[condição_das_linhas, colunas_desejadas]

df_concluidos = df.loc[df["Status"] == "Concluído", ["Cliente", "Valor_Total"]]
print(df_concluidos)

