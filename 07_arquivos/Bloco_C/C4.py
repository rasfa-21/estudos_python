# C4 - contando quntos chamados cada tecnico tem 

import csv

caminho_arquivo = r"07_arquivos\Bloco_C\chamados.csv"

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: 
    leitor = csv.DictReader(arquivo)
    chamados_por_tec = {}

    for linha in leitor:
        chamados_por_tec[linha['tecnico']] = chamados_por_tec.get(linha['tecnico'], 0) + 1

print(chamados_por_tec)