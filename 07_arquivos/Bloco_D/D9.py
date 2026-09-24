# D9 

from D8 import validar_arquivo # valida se um arquivo existe ou n

CAMINHO_VALIDO = r"07_arquivos\Bloco_D\listaD1.txt"
CAMINHO_INVALIDO = "arquivo_inexistente.txt"

def carregar_lista(caminho_arquivo):
    lista_carregada = []

    if not validar_arquivo(caminho_arquivo): # clausula de guarda, retorna lista vazia sem quebrar
        print('Arquivo não encontrado')
        return []

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                lista_carregada.append(linha.strip())

    return lista_carregada

resultado_valido = carregar_lista(CAMINHO_VALIDO)
print(resultado_valido)
print()
resultado_invalido = carregar_lista(CAMINHO_INVALIDO)
print(resultado_invalido)

