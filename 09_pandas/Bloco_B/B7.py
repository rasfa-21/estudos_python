# B7

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

try:
    # entre valor1 e valor2 (inclusive nas pontas)
    df_chamados_por_faixa = df[df["Valor_Total"].between(1500, 2500)]
    print(df_chamados_por_faixa)
    
except KeyError:
    print("Chave(s) não encontradas")

