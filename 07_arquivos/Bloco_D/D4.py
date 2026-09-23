# D4. pegando o maior de um CSV chamado sem usar o max

import csv

caminho = r"07_arquivos\Bloco_C\chamados.csv"

def maior_chamado(caminho_arquivo): 
    maior_dict = None
    maior_valor = float('-inf')

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in csv.DictReader(arquivo):
            valor_convertido = float(linha['valor'])

            if valor_convertido > maior_valor:
                maior_valor = valor_convertido
                maior_dict = linha

    return maior_dict

resultado = maior_chamado(caminho)
print(resultado)
                


