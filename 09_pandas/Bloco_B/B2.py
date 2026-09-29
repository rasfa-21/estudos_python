# B2

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

# estrutura de multiplas condicoes no Pandas: "&" equivale "and" e "|" equivale a "or"
# sempre entre parenteses e boolean indexing: df[...(df[chave] + condicao) "&" ou "|" df[chave] + condicao2]

try:
    concluidos_1000_df = df[(df["Valor_Total"] > 1000) & (df["Status"] == "Concluído")] 
    print(concluidos_1000_df)   
except KeyError:
    print("Nome da(s) coluna(s) não encontrado(as) no arquivo.")

