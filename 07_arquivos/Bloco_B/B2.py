# B2 

caminho_arquivo = '07_arquivos\\Bloco_B\\produtos.txt'

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    lista_produtos = [] # sintaxe alternativa: lista_produtos = [linha.strip() for linha in arquivo]

    for linha in arquivo:
        # .strip remove os espaços em branco e caracter de quebra de linha do texto('\n')
        linha_limpa = linha.strip()
        lista_produtos.append(linha_limpa)

print(lista_produtos)