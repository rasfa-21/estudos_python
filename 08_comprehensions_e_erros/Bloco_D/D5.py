# D5

manutencoes = [
    {"maquina": "M1", "custo": "450.50"},
    {"maquina": "M2", "custo": "invalido"},
    {"maquina": "M3", "custo": "1200.00"},
    {"maquina": "M4", "custo": ""}
]

soma_validos = 0
contador_invalidos = 0

for maquina in manutencoes:
    try:
        valor_numerico = float(maquina["custo"])
        soma_validos += valor_numerico 

    except (ValueError, TypeError):
        contador_invalidos += 1
        pass

print(soma_validos)
print(contador_invalidos)

