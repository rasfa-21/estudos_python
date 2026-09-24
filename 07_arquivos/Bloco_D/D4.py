# D4. pegando o maior de um CSV chamado sem usar o max

import csv

caminho = r"07_arquivos\Bloco_C\chamados.csv"

def maior_chamado(caminho_arquivo):
    # None serve como sentinela: indica que ainda nenhum registro foi processado.
    # Se o arquivo estiver vazio (só cabeçalho), a função retornará None com segurança. 

    # float('-inf') é o infinito negativo. Garante que qualquer número real
    # (inclusive negativos ou zero) vença na 1ª comparação e vire o primeiro campeão.
    
    maior_dict = None
    maior_valor = float('-inf')

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in csv.DictReader(arquivo):
            valor_convertido = float(linha['valor'])

            if valor_convertido > maior_valor:
                maior_valor = valor_convertido
                maior_dict = linha # Guarda a linha inteira para não perder o contexto (técnico, fazenda, etc.)

    return maior_dict

resultado = maior_chamado(caminho)
print(resultado)
                


