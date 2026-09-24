# D10. pipeline de funções 

import csv
from collections import Counter

CAMINHO_CSV = r"07_arquivos\Bloco_C\chamados.csv"
# Etapa 01. leitura de dados e retorno de dict

def ler_dados(arquivo_csv):
    lista_dados = []
    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
        for linha in csv.DictReader(arquivo):
            lista_dados.append(linha())

dados = ler_dados(CAMINHO_CSV)
print(dados)





