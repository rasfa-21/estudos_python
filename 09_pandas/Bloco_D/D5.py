import pandas as pd

def gerar_relatorio_pandas_csv(arquivo_entrada, arquivo_saida):
    try:
        # O Pandas lê o arquivo diretamente pelo caminho, sem necessidade de open()
        df = pd.read_excel(arquivo_entrada)

        # Criando a coluna de imposto
        df["Imposto"] = df["Valor_Total"] * 0.05

        # Criando a coluna Valor_Final somada com a coluna Imposto
        df["Valor_Final"] = df["Imposto"] + df["Valor_Total"]

        # Ordenando de forma decrescente
        df = df.sort_values("Valor_Final", ascending=False)

        # Gerando arquivo de saída
        df.to_csv(arquivo_saida, index=False)
        print("Arquivo CSV gerado com sucesso")

    except FileNotFoundError:
        return f"Arquivo não encontrado"

CAMINHO_ENTRADA = r"09_pandas\Bloco_D\dados_didaticos.xlsx"
CAMINHO_SAIDA = r"09_pandas\Bloco_D\dados_didaticos_tratados"

gerar_relatorio_pandas_csv(CAMINHO_ENTRADA, CAMINHO_SAIDA)