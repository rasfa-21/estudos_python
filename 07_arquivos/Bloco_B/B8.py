# B8 

itens = ['Parafuso', 'Porca', 'Arruela']

caminho = '07_arquivos\\Bloco_B\\itensb7.txt'

def lista_p_arquivo_numerado(lista, caminho_arquivo):
    with open(caminho_arquivo, 'w') as arquivo:

        for i, item in enumerate(lista, start=1):
            arquivo.write(f'{i}. {item}\n')

resultado = lista_p_arquivo_numerado(itens, caminho)