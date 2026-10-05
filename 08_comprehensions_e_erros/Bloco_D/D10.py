# D10- Auditor de OEE e Sanitização de Chão de Fábrica

lote_apontamentos = [
    {"id": "OP-01", "linha": "L1", "planejado_min": "480", "parada_min": "45", "boas": "520", "refugo": "10"},
    {"id": "OP-02", "linha": "L2", "planejado_min": "480", "parada_min": "corrompido", "boas": "480", "refugo": "5"},
    {"id": "OP-03", "linha": "L1", "planejado_min": "0", "parada_min": "0", "boas": "0", "refugo": "0"},
    {"id": "OP-04", "linha": "L3", "planejado_min": "480", "parada_min": "120", "boas": "410", "refugo": "35"},
    {"id": "OP-05", "linha": "L2", "planejado_min": "480", "parada_min": "60", "boas": "invalido", "refugo": "8"},
    {"id": "OP-06", "linha": "L3", "planejado_min": "480", "parada_min": "30", "boas": "590", "refugo": "12"},
]

# 01. Higienização e Validação de campos numericos para inteiros 

def converter_campos(dict_entrada):
    try:
        

    