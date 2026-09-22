# B3 

caminho_arquivo = '07_arquivos\\Bloco_B\\estoque.txt'
produtos = ["Parafuso", "Porca", "Arruela"]
precos = [0.5, 0.3, 0.2]

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    for i, item in zip(precos, produtos):
        arquivo.write(f'{item} - R$ {i:.2f}\n')

print('Estoque criado com sucesso!')
