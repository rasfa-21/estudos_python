# A6. Função que conta palavras em um arquivo (usando .read())

caminho = '07_arquivos\\Bloco_A\\notas.txt'

def contar_palavras(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        # .read le o arquivo tdo e devolve uma string gigante com todo o texto
        conteudo = arquivo.read()
        contagem_palavras = len(conteudo.split())

    return contagem_palavras

resultado = contar_palavras(caminho)
print(resultado)
