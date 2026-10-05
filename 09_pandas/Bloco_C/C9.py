# C9

import pandas as pd
from C2 import df_soma_por_tipo

df = df_soma_por_tipo.reset_index()
df_renomeado = df.rename(columns={"Valor_Total": "Total_Faturado"})

print(df_renomeado)

