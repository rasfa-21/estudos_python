# D1 

dados_parada = ["15", "45", "N/A", "120", "sem parada", "60"]

# 01. função auxiliar que retorna o inteiro ou None caso dê erro

def seguro_int(valor_entrada):
    try:
        valor_int = int(valor_entrada)
        return valor_int
    except ValueError:
        return None

# 02. Filtrar a lista combinada com a função para ter inteirs válidos

lista_filtrada = [seguro_int(item) for item in dados_parada if seguro_int(item) is not None]
print(lista_filtrada)