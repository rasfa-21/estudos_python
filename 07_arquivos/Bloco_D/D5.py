# D5 contando todos os chamados por fazenda do CSV

import csv
from collections import Counter

caminho = r"07_arquivos\Bloco_C\chamados.csv"

def chamado_por_fazenda(caminho_arquivo): 
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: 
        contagem_fazenda = Counter() # no lugar do dict vazio {}

        for linha in csv.DictReader(arquivo):
            contagem_fazenda[linha['fazenda']] += 1 # ao inves de usar .get()

    return dict(contagem_fazenda)

if __name__ == '__main__':
    resultado = chamado_por_fazenda(caminho)
    print(resultado)



            
