# A10. Criar o mesmo DataFrame de dois jeitos e comparar pra ver se são iguais

import pandas as pd

dict_listas = {
    "valor": [1200, 850], 
    "tecnico": ["Rafael", "João"]
}

lista_dicts = [
    {"valor": 1200, "tecnico": "Rafael"},
    {"valor": 850, "tecnico": "João"} 
]

df_dict = pd.DataFrame(dict_listas)
df_lista = pd.DataFrame(lista_dicts)

print(df_lista.equals(df_lista))
# retorna True ou False
