# B1

import pandas as pd
CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)
# estrutura padrão de filtragem do Pandas, Equivalente a um if dentro de um for 
df_concluidos = df[df["Status"]== "Concluído"] 
print(df_concluidos)


