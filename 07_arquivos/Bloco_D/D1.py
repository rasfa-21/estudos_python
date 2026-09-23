# D1. função q escreve cada item numa linha

caminho_arquivo = r"07_arquivos\Bloco_D\listaD1.txt"
lista_itens = ['parafuso', 'porca', 'arruela', 'arame', 'bucha']

def salvar_lista(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for item in lista:
            arquivo.write(item + '\n')

    print('Arquivo salvo com sucesso!')

resultado = salvar_lista(lista_itens, caminho_arquivo)
        
