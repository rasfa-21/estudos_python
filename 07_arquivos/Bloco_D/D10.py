# D10. pipeline de funções 

import csv
from collections import Counter

CAMINHO_CSV = r"07_arquivos\Bloco_C\chamados.csv"
CAMINHO_TXT = r"07_arquivos\Bloco_D\metricas.txt"

# Etapa 01. leitura de dados e retorno de dict

def ler_dados(arquivo_csv):
    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
        dict_dados = list(csv.DictReader(arquivo)) # list() transforma todos os dicts em uma lista 

    return dict_dados

# Etapa 02. receber a lista de dados (dict_dados) e retornar um dict com total, media e contagem por status

def calcular_metricas(dados_entrada):

    if not dados_entrada: # evita quebrar se não houver dados de entrada
        return {'total': 0.0, 'media': 0.0, 'Chamados por status': {}}
     
    contagem_status = Counter()
    total_geral = 0

    # não precisa abrir o arquivo novamente, vamos reaproveitar os dados da etapa 1
    # o percorre os dados como parametro

    for linha in dados_entrada:
        contagem_status[linha['status']] += 1
        total_geral += float(linha['valor'])

    media = total_geral/len(dados_entrada) # divide pelo tamanho da lsita de dados de entrada

    # empacota tudo em um unico dict
    return {
            'total': total_geral,
            'media': media,
            'Chamados por status': dict(contagem_status)
        }

# Etapa 3. receber o dict metricas e escrever em um arquivo txt

def salvar_metricas(dados_metricas, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:

        for chave, valor in dados_metricas.items(): 
            arquivo.write(f'{chave}: {valor}\n')          

# etapa 04: função que executa o pipeline

def executar_pipeline(arquivo_csv, arquivo_saida):
    dados = ler_dados(arquivo_csv) # guardando o resultado para reaproveitar depois
    metricas = calcular_metricas(dados)
    metricas_salvas = salvar_metricas(metricas, arquivo_saida)

try:
    executar_pipeline(CAMINHO_CSV, CAMINHO_TXT)
    print("Pipeline executado com sucesso!")
except FileNotFoundError:
    print(f"Erro: arquivo de entrada '{CAMINHO_CSV}' não foi encontrado")


















