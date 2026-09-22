# B4 

caminho_arquivo = '07_arquivos\\Bloco_B\\estoque.txt'

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: 
    lista_itens = []

    for linha in arquivo:
        linha_limpa = linha.strip().split(" - ")

        itens = {
            "Produto": linha_limpa[0],  
            "Preco": float(linha_limpa[1].replace('R$', '').strip())
            # .replace substitui um trecho por outro na string
            # nesse caso 'R$' por um espaço '' pra deixar o dict limpo 
        }                                                            

        lista_itens.append(itens)
        

    print(lista_itens)