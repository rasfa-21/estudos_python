# D5 contando todos os chamados por fazenda

import csv
from collections import Counter

caminho = r"07_arquivos\Bloco_C\chamados.csv"

def chamado_por_fazenda(caminho_arquivo): 
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: 
        contagem_fazenda = Counter() # no lugar do dict vazio {}

        for linha in csv.DictReader(arquivo):
            contagem_fazenda[linha['fazenda']] += 1

    return dict(contagem_fazenda)

resultado = chamado_por_fazenda(caminho)
print(resultado)



            
