# B7

caminho_arquivo = '07_arquivos\\Bloco_B\\vendas.txt'
lista_vendas = []

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: 
     # .readlines() ler todas as linhas de um arquivo de texto e guarda numa lista
     linhas = arquivo.readlines()

     for linha in linhas[:-2]:
          linha_limpa = int(linha.strip())
          lista_vendas.append(linha_limpa)

print(lista_vendas)

          