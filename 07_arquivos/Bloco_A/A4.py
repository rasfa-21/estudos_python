# A4. Função que conta linhas de um arquivo

caminho = '07_arquivos\\Bloco_A\\notas.txt'


def contar_linhas(caminho_arquivo):
    contador_linhas = 0
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            contador_linhas += 1

    return contador_linhas

resultado = contar_linhas(caminho)
print(resultado)

