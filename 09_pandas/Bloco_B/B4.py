# B4

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

df_chamados_manutencao = df[(df["Tipo"] == "Manutenção")]
# resultado: uma Series, com o técnico como índice
soma_manutencao = df_chamados_manutencao.groupby("Tipo")["Valor_Total"].sum() 
# resultado: DataFrame normal, com colunas 'tecnico' e 'valor'
df_soma_manutencao = df_chamados_manutencao.groupby("Tipo")["Valor_Total"].sum().reset_index()

print(soma_manutencao)
print(df_soma_manutencao)

