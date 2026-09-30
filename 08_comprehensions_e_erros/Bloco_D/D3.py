# D3

linhas_csv = [
    "linha,pecas_boas,pecas_refugo",
    "L1,500,10",
    "L2,450,erro",
    "L3,480,15",
    "L4,,8"
]

def converter_texto(texto_linha):
    try:
        linha, boas, refugos = texto_linha.split(",")
        return linha, int(boas), int(refugos)
    except ValueError:
        return None

lista_extraida = [converter_texto(item) for item in linhas_csv[1:] if converter_texto(item) is not None]
print(lista_extraida)