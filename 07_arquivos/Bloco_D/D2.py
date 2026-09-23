# D2 

caminho = r"07_arquivos\Bloco_D\listaD1.txt"

def carregar_lista(caminho_arquivo):
    lista_carregada = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        # fiz com for por ser mais usual e se o arquivo for mt grande evita sobrecarga na memoria
        for linha in arquivo:
            lista_carregada.append(linha.strip())

    return lista_carregada

if __name__ == '__main__':
    resultado = carregar_lista(caminho)
    print(resultado)