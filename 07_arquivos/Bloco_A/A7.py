# A7

caminho = '07_arquivos\\Bloco_A\\notas.txt'

with open(caminho, 'r', encoding='utf-8') as arquivo:
    # .readlines() lê todo o conteúdo de um arquivo e o transforma em uma lista de strings
    # onde cada elemento dessa lista corresponde a uma linha do arquivo original.
    lista_palavras_arquivo = arquivo.readlines()
    print(lista_palavras_arquivo[-1])


