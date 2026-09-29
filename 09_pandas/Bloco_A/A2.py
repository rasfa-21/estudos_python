# A2

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx" 

# 01: ler chamados.csv com o pandas
# O pandas ja lê, identifica as colunas pelo cabeçalho e converte os tipos automaticamente
df = pd.read_excel(CAMINHO_ARQUIVO)
print(df)

# df = pd.read_csv('planilha.csv')   funciona igual pra csv



