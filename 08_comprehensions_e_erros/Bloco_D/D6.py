# D6

manutencoes = [
    {"maquina": "M1", "custo": "450.50"},
    {"maquina": "M2", "custo": "invalido"},
    {"maquina": "M3", "custo": "1200.00"},
    {"maquina": "M4", "custo": ""}
]

def funcao_auxiliar(dict_entrada, chave_procurada, valor_padrao=0):
    try:
        custo_valido = float(dict_entrada[chave_procurada])
        return custo_valido
    except (ValueError, KeyError):
        return valor_padrao

lista_custo_valido = [item["maquina"] for item in manutencoes if funcao_auxiliar(item, "custo") > 500 ]
print(lista_custo_valido)