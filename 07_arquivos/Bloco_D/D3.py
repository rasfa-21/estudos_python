# D3 

import csv

caminho = r"07_arquivos\Bloco_C\chamados.csv"

def resumo_csv(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        contagem_status = {}
        total_chamados = 0

        for linha in leitor:
            contagem_status[linha['status']] = contagem_status.get(linha['status'], 0) + 1
            total_chamados += float(linha['valor'])

    return contagem_status, total_chamados

# desempacotando
contagem_status, total_chamados = resumo_csv(caminho)
print(f'Total faturado: R$ {total_chamados:.2f}')
print(f'Chamados por status: {contagem_status}')



            

