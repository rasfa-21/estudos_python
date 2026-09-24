# D7

import csv
from collections import Counter     
from D6 import salvar_relatorio     # salva em txt

ARQUIVO_ENTRADA = r"07_arquivos\Bloco_C\chamados.csv"
ARQUIVO_SAIDA = r"07_arquivos\Bloco_D\relatorio_chamadosD6.txt"

def processar_chamados(caminho_entrada, caminho_saida): 
    contagem_tecnico = Counter() # no lugar do dict vazio
    valor_total = 0

    with open(caminho_entrada, 'r', encoding='utf-8') as arquivo: 
        for linha in csv.DictReader(arquivo):
            contagem_tecnico[linha['tecnico']] += 1 # ao inves de usar .get()
            valor_total += float(linha['valor']) # sempre convertendo 

    # dados de entrada tem q ser o dict contagem_tecnico 
    # fora do with pra fechar o arquivo de entrada
    salvar_relatorio(contagem_tecnico, caminho_saida) 
             
# chamando a função orquestradora 
processar_chamados(ARQUIVO_ENTRADA, ARQUIVO_SAIDA)

    

    