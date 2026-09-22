# A1. Escrever um arquiv, ler e imprimir 
# escrevendo linhas em um arquivo
with open('notas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Frase 1\n')
    arquivo.write('Frase 2\n')
    arquivo.write('Frase 3\n')

# lendo linhas de um arquivo modo 'r'
with open('notas.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)