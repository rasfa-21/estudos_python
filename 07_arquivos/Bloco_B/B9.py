# B9

caminho = '07_arquivos\\Bloco_B\\itensb7.txt'

def arquivo_numerado_p_lista(caminho_arquivo):
    lista_itens = []
    with open(caminho_arquivo, 'r', encoding= 'utf-8') as arquivo:

        for linha in arquivo:
            # encadeamento: .strip limpa, .split separa em sublistas pelo caractere'.'
            linha_l = linha.strip().split('. ', maxsplit=1)
            lista_itens.append(linha_l[1])

    return lista_itens

result = arquivo_numerado_p_lista(caminho)
print(result)
