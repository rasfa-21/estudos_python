# C8. função q retorna media por status

import csv 

caminho = r"07_arquivos\Bloco_C\chamados.csv"

def media_valor_status(caminho_arquivo, status_buscado):
    soma_status = 0
    len_status = 0

    with open(caminho, 'r', encoding='utf-8') as arquivo: 
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            if linha['status'].strip() == status_buscado:
                soma_status += float(linha['valor'])
                len_status += 1

    # evita divisão por zero caso o status não seja encontrado
    if len_status == 0: 
        return 0.0

    return soma_status/len_status # retorna a media fora do loop

resultado = media_valor_status(caminho, 'Concluído')
print(f' Média: {resultado:.2f}')