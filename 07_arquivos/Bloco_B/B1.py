# B1 

caminho_arquivo = '07_arquivos\\Bloco_B\\produtos.txt'
produtos = ["Parafuso", "Porca", "Arruela"]

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    for produto in produtos:
        arquivo.write(f'{produto}\n')

    print('Arquivo criado com sucesso!')