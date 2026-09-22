# O Fechamento de Médias (Foco: Escopo do Acumulador e Reset por Linha)

equipes = [
    ["Alfa", 8, 9, 7],
    ["Beta", 5, 6, 4],
    ["Gama", 10, 9, 8]
]

caminho = '07_arquivos\\Bloco_B\\medias_equipe.txt'

with open(caminho, 'w', encoding='utf-8') as arquivo:

    for equipe in equipes:
        medias = []

        for nota in equipe:
            # adicionando somente as notas na lista
            if type(nota) != str:       # dava pra usar fatiamento aqui jovem mancebo
                medias.append(nota)
                # agora preciso calcular as medias

        media_notas = sum(medias)/len(medias)
        nome_equipes = equipe[0]
        arquivo.write(f'{nome_equipes} - Média: {media_notas:.1f}\n')

    
