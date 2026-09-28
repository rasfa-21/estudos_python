# A8

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"
df = pd.read_excel(CAMINHO_ARQUIVO)

# pegando o nome das colunas
print(df.columns)

# Operações com a Coluna Valor_Total
soma_chamados = df["Valor_Total"].sum()         # soma todos os valores da coluna 
media_chamados = df["Valor_Total"].mean()       # Media dos valores da coluna
max_chamados = df["Valor_Total"].max()          # Valor Max da coluna
min_chamados = df["Valor_Total"].min()          # Valor Minimo da coluna

print(f"Soma total dos chamados: {soma_chamados}. Média: {media_chamados}. Maior chamado: {max_chamados}. Menor Chamado: {min_chamados}")