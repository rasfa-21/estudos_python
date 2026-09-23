# C6 -- função de filtrar

import csv

caminho = r"07_arquivos\Bloco_C\chamados.csv"

def filtrar_status(caminho_arquivo, status_buscado):
    buscado = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: 
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            if status_buscado == linha['status']:
                buscado.append(linha)

    return buscado

if __name__ == '__main__':
    resultado = filtrar_status(caminho, 'Concluído')
    print(resultado)

        

