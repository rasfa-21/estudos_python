# B6

vendas = [1200, 850, 3000, 450]
caminho_arquivo = '07_arquivos\\Bloco_B\\vendas.txt'

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    for venda in vendas:
        arquivo.write(f'{venda}\n')

    arquivo.write(f'--------\n')
    arquivo.write(f'{sum(vendas)}\n')


print('Arquivo criado com sucesso!')