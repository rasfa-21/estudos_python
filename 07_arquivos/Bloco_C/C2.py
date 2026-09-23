# C2 

import csv

caminho_arquivo = r"07_arquivos\Bloco_C\chamados.csv"

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    soma_concluidos = 0

    for linha in leitor:
        if linha['status'] == "Concluído":
            # convertendo p float pois toda leitura de arquivo vem como string
            soma_concluidos += float(linha['valor']) 

print(f'Valor total dos chamados concluídos: R$ {soma_concluidos:.2f}')

