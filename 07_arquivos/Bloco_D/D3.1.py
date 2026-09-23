# D3 refatorado usando collections.counter

import csv 
from collections import Counter

caminho = r"07_arquivos\Bloco_C\chamados.csv"

def resumo_csv(caminho_arquivo):
        contagem_status = Counter()
        total_geral = 0

        # Com o Counter, qualquer chave nova já nasce com valor zero automaticamente, 
        # permitindo fazer direto contagem_status[status] += 1.
        
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in csv.DictReader(arquivo): # sem necessidade da variavel leitor
                contagem_status[linha['status']] += 1
                total_geral += float(linha['valor'])

        return dict(contagem_status), total_geral

if __name__ == '__main__':
    status_dict, total = resumo_csv(caminho)
    print(f'Valor total: R$ {total:.2f}')
    print(f'Chamados por status: {status_dict}')
