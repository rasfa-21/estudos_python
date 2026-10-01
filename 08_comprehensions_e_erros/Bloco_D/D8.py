# D8

from datetime import datetime

CAMINHO_ARQUIVO = r"08_comprehensions_e_erros\Bloco_D\erros_sensores.log"

def gerar_log_incidentes(lista_bruta):    
    with open(CAMINHO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
        for item in lista_bruta:        
            try:
                float(item)
                pass

            except ValueError:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                arquivo.write(f"[{timestamp}] ERRO_LEITURA: '{item}'\n")

dados_brutos = [
    "24.8",
    "FALHA_CONEXAO",
    "31.2",
    "TIMEOUT",
    "19.5",
    "",
    "45.0",
    "SENSOR_OFFLINE",
    "28.3",
    "ERR_VAL_NULO",
    "33.7"
]

gerar_log_incidentes(dados_brutos)

