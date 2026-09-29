# B8

import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUIVO)

#O .str. na frente dá acesso, coluna inteira de uma vez, aos mesmos métodos 
# de string (.upper(), .strip(), .split()...): df['fazenda'].str.upper().

filtro_fazenda = df[df["Cliente"].str.contains("Agro")]
print(filtro_fazenda) 