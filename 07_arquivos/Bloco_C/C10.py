# C10 - função q exporta filtro em outro arquivo csv

import csv
from C6 import filtrar_status

caminho_entrada = r"07_arquivos\Bloco_C\chamados.csv"
caminho_saida = r"07_arquivos\Bloco_C\chamados_filtrados.csv"

def exportar_filtrado(arquivo_entrada, arquivo_saida, status_buscado):
    dados_filtrados = filtrar_status(arquivo_entrada, status_buscado)

    # verificar se os dados não estão vazios
    if not dados_filtrados: # clausula de guarda
        print(f'({status_buscado}) Not Found')
        return

    # estrutura padrao de escrita modo "a"
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo: 
        # busca dinamica ao invés de campos = ['fazenda'...]
        campos = dados_filtrados[0].keys()
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()              # escrevendo as chaves como cabecalho
        escritor.writerows(dados_filtrados) # escrevendo todas as linhas no novo csv

resultado = exportar_filtrado(caminho_entrada, caminho_saida, "")

