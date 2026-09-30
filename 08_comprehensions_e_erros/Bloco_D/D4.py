# D4

def obter_campo_seguro(dict_entrada, chave_buscada, valor_padrao=0.0):
    try:
        valor = float(dict_entrada[chave_buscada])
        return valor
    except (KeyError, ValueError):
        return valor_padrao

registros = {
    "tensao": 218.5,
    "corrente": 10,
    "fase": "L1"
}

print(obter_campo_seguro(registros, "tensao"))
print(obter_campo_seguro(registros, "corrente"))
print(obter_campo_seguro(registros, "resistencia"))