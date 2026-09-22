# A4 

caminho = '07_arquivos\\Bloco_A\\notas.txt'

with open(caminho, 'a', encoding='utf-8') as arquivo:
    arquivo.write('frase 4\n')

with open(caminho, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)