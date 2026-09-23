# C5 -- calculando imposto sobre valor de serviço

import csv

caminho_arquivo = r"07_arquivos\Bloco_C\chamados.csv"

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: 
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        imposto = float(linha['valor']) * 0.05 # tem q converter

        print(f"{linha['fazenda']}: valor: R$ {float(linha['valor']):.2f}, imposto R$ {imposto:.2f}")