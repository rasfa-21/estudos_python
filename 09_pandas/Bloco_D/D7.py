import pandas as pd

CAMINHO_ARQUIVO = r"09_pandas\Bloco_D\dados_didaticos_tratados"

df = pd.read_csv(CAMINHO_ARQUIVO)
df = df.drop(columns=['Imposto']) # temq reatribuir, nao altera o df original

print(df.columns)
