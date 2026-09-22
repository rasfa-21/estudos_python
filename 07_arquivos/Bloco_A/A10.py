# A10

caminho = '07_arquivos\\Bloco_A\\notas.txt'

def buscar_palavra(caminho_arquivo, palavra):
    lista_linhas = []
    
    with open(caminho_arquivo, 'r') as arquivo: 

        for i, linha in enumerate(arquivo, start=1):
            if palavra in linha: 
                lista_linhas.append(i)

    return lista_linhas

resultado = f'Palavra encontrada na(s) linhas(s): {buscar_palavra(caminho, 'Arroz')}'
print(resultado)
    