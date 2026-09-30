# D6

manutencoes = [
    {"maquina": "M1", "custo": "450.50"},
    {"maquina": "M2", "custo": "invalido"},
    {"maquina": "M3", "custo": "1200.00"},
    {"maquina": "M4", "custo": ""}
]

def funcao_auxiliar(lista_entrada):
    for item in lista_entrada:
        try:
            float()

lista_custo_valido = [float(manutencoes["custo"]) for maquina in manutencoes if ]