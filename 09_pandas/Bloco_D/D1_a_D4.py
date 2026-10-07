import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

#   D1. criando coluna de imposto 
df["Imposto"] = df["Valor_Total"] * 0.05

# D2. criando a coluna valor final somando com imposto
df["Valor_Final"] = df["Valor_Total"] + df["Imposto"]

# D3. Ordenando de forma descrescente (ascendindg=false)
df.sort_values("Valor_Final", ascending=False)

# D4. Salvando o novo relatorio em csv
df.to_csv(r"09_pandas\dados_didaticos_tratados.csv", index=False)
