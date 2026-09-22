# Exercício de fixação 2

caminho = '07_arquivos\\Bloco_B\\temperaturas.txt'

with open(caminho, 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'28.5\n')
    arquivo.write(f'32.1\n')
    arquivo.write(f'27.0\n')
    arquivo.write(f'35.4\n')
    arquivo.write(f'29.8\n')

def buscar_alertas(caminho_arquivo, limite): 
    # preciso primeiro ler e converter o arquivo para numeros para comparar com o limite
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas_acima_limite = []

        # estrutura 'padrão' de leitura linha por linha
        for i, linha in enumerate(arquivo, start=1): # O objeto que contém as linhas do arquivo aberto é a variável arquivo
            valor = float(linha.strip())

            # se for maior que o limite adiciono o indice na lista
            if valor > limite: 
                linhas_acima_limite.append(i)

        return linhas_acima_limite

resultado = buscar_alertas(caminho, 30)
print(f'Temperaturas acima do limite: {resultado}')

