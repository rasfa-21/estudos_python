# B5

caminho = '07_arquivos\\Bloco_B\\arquivob5.txt'

def anexar_linha(caminho_arquivo, texto):
    with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo: 
        arquivo.write(f'{texto}\n')

    print('Arquivo adicionado com sucesso!')

result = anexar_linha(caminho, 'Linha de teste 3')

