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

# Declaramos as chaves numéricas como uma constante (fácil de manter/expandir)
CAMPOS_NUMERICOS = ("planejado_min", "parada_min", "boas", "refugo")
CAMINHO_ARQUIVO = r"08_comprehensions_e_erros\Bloco_D\auditoria_producao.txt"

def sanitizar_apontamento(op: dict) -> dict | None:
    """
    Tenta converter todos os campos numéricos da OP.
    Retorna uma nova OP com os tipos corretos ou None se houver qualquer anomalia.
    """
    try:
        # Cria uma cópia para preservar o original
        op_limpa = dict(op)

        # Converte apenas os campos que devem ser números
        for campo in CAMPOS_NUMERICOS:
            op_limpa[campo] = int(op[campo])

        return op_limpa

    except (ValueError, KeyError, TypeError):
        return None

# Guardando as OPs inconsistentes e validas
ops_inconsistentes = [op["id"] for op in lote_apontamentos if sanitizar_apontamento(op) is None]
ops_validas = [sanitizar_apontamento(op) for op in lote_apontamentos if sanitizar_apontamento(op) is not None]

# 02. Calcula indicadores para OPs válidas

def calcular_disponibilidade(op_valida):
    try:
        disponibilidade = (op_valida["planejado_min"] - op_valida["parada_min"])/ op_valida["planejado_min"]
        return disponibilidade
    except ZeroDivisionError:
        return 0

def calcular_taxa_refugos(op_valida):
    try:
        taxa_refugo = op_valida["refugo"]/(op_valida["boas"] + op_valida["refugo"])
        return taxa_refugo
    except ZeroDivisionError:
        return 0.0

# 03. Filtrando OPs válidas com taxa de refugo superior a 3% 

ops_filtradas = [op for op in ops_validas if calcular_taxa_refugos(op) > 0.03]

#  04. Gerar relatório txt

def gerar_relatorio(caminho_arquivo):
    with open(caminho_arquivo, 'a', encoding="utf-8") as arquivo:
        arquivo.write("=" * 40 + "\n")
        arquivo.write("    RELATÓRIO DE AUDITORIA DE PRODUÇÃO\n")
        arquivo.write("=" * 40 + "\n\n")

        # 01. Quantidades gerais

        total_analisadas = len(lote_apontamentos)
        total_validas = len(ops_validas)
        total_descartadas = len(ops_inconsistentes)

        arquivo.write(f"Total de OPs analisadas: {total_analisadas}\n")
        arquivo.write(f"Total de OPs válidas: {total_validas}\n")
        arquivo.write(f"Total de OPs descartadas: {total_descartadas}\n")

        # 02. OPS descartadas por dados inconsistentes

        arquivo.write(f"--- OPs DESCARTADAS (DADOS CORROMPIDOS) ---\n")
        if ops_inconsistentes:
            for op_id in ops_inconsistentes:
                arquivo.write(f"- {op_id}\n")
        else:
            arquivo.write("Nenhuma OP descartada.\n")
        arquivo.write("\n")

        # 03. OPs com alta taxa de refugo (> 3%)
        arquivo.write("--- OPs COM ALTA TAXA DE REFUGO (> 3%) ---\n")
        if ops_filtradas:
            for op in ops_filtradas:
                taxa = calcular_taxa_refugos(op) * 100
                arquivo.write(f"-{op["id"]} (linha {op["linha"]}): {taxa:.2}% de refugo\n")
        else:
            arquivo.write("Nenhuma OP com alta taxa de refugo.\n")

gerar_relatorio(CAMINHO_ARQUIVO)
print("Relatório gerado com sucesso!")







                