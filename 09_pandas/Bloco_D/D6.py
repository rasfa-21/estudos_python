import pandas as pd

def classificar(valor):
    if valor >= 8000:
        return 'ALTA'
    elif valor >= 4000:
        return 'MEDIA'
    else:
        return 'Baixa'

CAMINNHO_ARQUIVO = r"09_pandas\Bloco_D\dados_didaticos_tratados"

df = pd.read_csv(CAMINNHO_ARQUIVO)
df["Categoria"] = df["Valor_Final"].apply(classificar)

print(df)