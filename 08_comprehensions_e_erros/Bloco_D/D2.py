# A2

consumos_kwh = ["120.5", "invalid", "340.2", "450.0", "", "98.1"]

# função auxiliar
def only_200(valor_entrada):
    try:
        valor_numerico = float(valor_entrada)
        if valor_numerico > 200:
            return valor_numerico
    except ValueError:
        None

lista_valida = [only_200(item) for item in consumos_kwh if only_200(item) if not None]
print(lista_valida)