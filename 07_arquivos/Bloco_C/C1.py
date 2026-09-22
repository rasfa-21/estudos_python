# arquivos csv
# NOTE: csv.DictReader Lê cada linha como um dicionario, usando a primeira linha do arquivo como nome das chaves 

import csv # sempre tem que importar esse módulo

chamados = [
    {"fazenda": "Terra Norte", "valor": 1200, "tecnico": "Rafael", "status": "Concluído"},
    {"fazenda": "Boa Vista", "valor": 1500, "tecnico": "Paulo", "status": "Em aberto"},     
]
    
caminho = '07_arquivos\\Bloco_C\\chamados.csv'

# estrutura padrão de escrita 
with open(caminho, 'w', newline='', encoding='utf-8') as arquivo: # newline='' evita linhas em branco
    campos = ['fazenda', 'valor', 'tecnico', 'status']            
    escritor = csv.DictReader(arquivo, fieldnames=campos)         # fieldnames precisa ter os mesmos nomes das chaves
    escritor.writeheader()       # escreve a linha de cabeçalho (nomes das colunas) só deve ser chamado uma vez
    escritor.writerows(chamados) # # escreve todas as linhas de uma vez




