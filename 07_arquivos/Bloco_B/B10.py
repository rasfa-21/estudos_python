# B10

notas_turma = [[7,8,9],[5,6,4]]
caminho = '07_arquivos\\Bloco_B\\notas_turmasB10.txt'

with open(caminho, 'w', encoding='utf-8') as arquivo:
    for nota_p_aluno in notas_turma:
        notas_str = []

        # no loop interno tenho q converter cada nota pra str e adicionar na lista convertida
        for nota_ in nota_p_aluno:
            nota_covertida = str(nota_)
            notas_str.append(nota_covertida) # sintaxe alternativa: notas_str.append(str(nota_))

        linha_convertida = ','.join(notas_str)
        arquivo.write(f'{linha_convertida}\n')
            