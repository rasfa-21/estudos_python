# D7

horas_semana = {"L1": "44", "L2": "parada", "L3": "48", "L4": "40", "L5": "pendente"}

def converter_valor(valor_entrada):
    try: 
        valor_convertido = int(float(valor_entrada))
        return valor_convertido
    except (ValueError, TypeError):
       return None

horas_validadas = {
    chave: converter_valor(valor) for chave, valor in horas_semana.items() 
    if converter_valor(valor) is not None
}

print(horas_validadas)