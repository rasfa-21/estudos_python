# D8. Validar arquivo usando try/except

ARQUIVO_ENTRADA = r"07_arquivos\Bloco_D\listaD1.txt"

def validar_arquivo(caminho_arquivo):

    # o Python tenta rodar tudo dentro do try. Se nenhum erro acontecer,
    #  o except é ignorado completamente.

    # Se qualquer erro acontecer em qualquer linha do try, ele pula direto pro except, 
    # executa aquele bloco, e o programa continua rodando normalmente depois — em vez de travar.

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return True
    except FileNotFoundError:   # tratando erro arquivo nao encontrado
        return False

if __name__ == '__main__':
    validacao = validar_arquivo(ARQUIVO_ENTRADA)
    print(validacao)