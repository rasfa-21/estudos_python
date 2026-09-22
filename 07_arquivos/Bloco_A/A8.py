# A8

caminho = '07_arquivos\\Bloco_A\\log.txt'

with open(caminho, 'a', encoding='utf-8') as arquivo:
    for i in range(5):
        arquivo.write(f'Evento {i+1} registado\n')
