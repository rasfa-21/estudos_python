# C9 adicionar nova linha (append)

import csv

nova_linha = [
    {"fazenda": "Semear", "valor": 1900, "tecnico": "Rafael", "status": "Concluído" }
]
caminho_arquivo = r"07_arquivos\Bloco_C\chamados.csv"

with open(caminho_arquivo, 'a', newline='', encoding='utf-8') as arquivo: 
    campos = ['fazenda', 'valor', 'tecnico', 'status']
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    # sem .writeheade() para não rescrever o cabeçalho no meio do arquivo
    escritor.writerows(nova_linha)