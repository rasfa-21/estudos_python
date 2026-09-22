# A9

caminho = '07_arquivos\\Bloco_A\\notas.txt'

with open(caminho, 'r') as arquivo:
    # da pra usar .read().upper() tambem 
    for linha in arquivo:
        linha_limpa_upper = linha.strip().upper()
        
        print(linha_limpa_upper)