# Exercício 01 de fixação 

leituras = [
    ["Sensor_Norte", 24.5, 25.1, 23.8],
    ["Sensor_Sul", 19.0, 18.7, 19.4],
    ["Sensor_Leste", 31.2, 30.5, 31.0]
]

caminho = '07_arquivos\\Bloco_B\\relatorio_sensores.txt'

with open(caminho, 'w', encoding='utf-8') as arquivo: 

    for leitura in leituras:
        lista_leituras = []

        # no loop interno preciso converter os dados e adicionar na lista
        for dado in leitura:
            lista_leituras.append(str(dado))

        # depois de adicionar os dados convertidos na lista, junto os itens com .join e escrevo no arquivo
        dado_formatado = "; ".join(lista_leituras)
        arquivo.write(f'{dado_formatado}\n')

print('Relatório criado com sucesso!')


