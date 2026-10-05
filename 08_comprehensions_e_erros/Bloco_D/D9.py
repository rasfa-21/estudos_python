# D9

import pandas as pd

registros_operacionais = [
    # Caso 1: Dados numéricos válidos (float)
    {"linha": "L1", "tempo_operacional": 42.5, "tempo_planejado": 48.0},
    
    # Caso 2: Divisão por zero (tempo planejado zerado)
    {"linha": "L2", "tempo_operacional": 10.0, "tempo_planejado": 0.0},
    
    # Caso 3: Chave faltante (ausência de tempo_operacional -> KeyError)
    {"linha": "L3", "tempo_planejado": 40.0},
    
    # Caso 4: Chave faltante (ausência de tempo_planejado -> KeyError)
    {"linha": "L4", "tempo_operacional": 35.0},
    
    # Caso 5: Dado textual não numérico (falha de conversão -> ValueError)
    {"linha": "L5", "tempo_operacional": "manutencao", "tempo_planejado": "48.0"},
    
    # Caso 6: Strings numéricas que devem ser convertidas com sucesso
    {"linha": "L6", "tempo_operacional": "38.0", "tempo_planejado": "40.0"},
    
    # Caso 7: String vazia (falha de conversão -> ValueError)
    {"linha": "L7", "tempo_operacional": "", "tempo_planejado": "44.0"}
]

def calcular_disponibilidade_operacional(dict_entrada):
    try:
        disponibilidade = float(dict_entrada["tempo_operacional"])/float(dict_entrada["tempo_planejado"])
        return disponibilidade
    except (KeyError, ValueError, ZeroDivisionError, TypeError):
        return 0.0

lista_disponibilidade = [calcular_disponibilidade_operacional(item) for item in registros_operacionais]
print(lista_disponibilidade)
