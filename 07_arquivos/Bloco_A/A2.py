# A2 

caminho = '07_arquivos\\Bloco_A\\notas.txt'

with open(caminho, 'r', encoding='utf-8') as arquivo:
    for i, linhas in enumerate(arquivo, start=1):
        # . strip remove espaços em brancos e o caractere '\n' do texto
        print(f'{i}. {linhas.strip()}')

