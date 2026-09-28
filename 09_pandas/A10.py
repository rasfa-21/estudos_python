# A10

import pandas as pd

CAMINHO_ARQUVIO = r"09_pandas\dados_didaticos.xlsx"

df = pd.read_excel(CAMINHO_ARQUVIO)

dict_listas = {
    "valor": [1200, 850], 
    "tecnico": ["Rafael", "João"]
}

lista_dicts = [
    {"valor": 1200, "tecnico": "Rafael"},
    {"valor": 850, "tecnico": "João"}
]