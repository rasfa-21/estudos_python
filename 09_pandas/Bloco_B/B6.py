# B6

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

try: 
    # filtrando chamados de duas fazenda com .isin()
    # equivale a "cliente IN lista ["cliente A, Cliente B"]" (vários "ou" de uma vez)
    df_filtro_fazenda = df[df["Cliente"].isin(["Fazenda Paraíso", "Agro Vitória"])]
    print(df_filtro_fazenda)
except KeyError:
    print("Chave(s) não encontrada(s)")

