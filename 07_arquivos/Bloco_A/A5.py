# A5

caminho = '07_arquivos\\Bloco_A\\notas.txt'

with open(caminho, 'r', encoding='utf-8') as arquivo: 
    for linha in arquivo:
        # sempre bom usar por conta do caractere de quebra de linha q o python adiciona automaticamente ('\n')
        linha_limpa = linha.strip()
        if len(linha) > 10:
            print(linha)
        

