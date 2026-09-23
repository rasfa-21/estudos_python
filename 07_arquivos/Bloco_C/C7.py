# C7 -- contando os chamados buscados

import csv
from C6 import filtrar_status

caminho = r"07_arquivos\Bloco_C\chamados.csv"
status_buscado = "Em aberto"

print(f'Numero de chamados {status_buscado}: {len(filtrar_status(caminho, status_buscado))}')