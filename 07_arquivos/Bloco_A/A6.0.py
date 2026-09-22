# A6. função que conta palavras em um arquivo (usando loop)

caminho = '07_arquivos\\Bloco_A\\notas.txt'

def contar_palavras(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        total_palavras = 0 
        
        for linha in arquivo:
            # . split divide um texto e retorna uma lista de palavras
            lista_palavras = linha.split()
            total_palavras += len(lista_palavras)
            
    return total_palavras

resultado = contar_palavras(caminho)
print(resultado)

