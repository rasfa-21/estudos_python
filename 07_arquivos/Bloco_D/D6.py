# D6

from D5 import chamado_por_fazenda

caminho_entrada = r"07_arquivos\Bloco_C\chamados.csv"
caminho_saida = r"07_arquivos\Bloco_D\relatorio_chamadosD6.txt"

dados = chamado_por_fazenda(caminho_entrada) # retorna um dict 

def salvar_relatorio(dados_entrada, arquivo_saida): 
    
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
        for nome_fazenda, qtd_chamados in dados_entrada.items():
            arquivo.write(f'{nome_fazenda}: {qtd_chamados} chamados\n')

if __name__ == '__main__':
    print('Relatório criado com sucesso!')
    resultado = salvar_relatorio(dados, caminho_saida)

