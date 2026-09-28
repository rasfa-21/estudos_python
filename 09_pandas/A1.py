# A1

import pandas as pd   # convenção universal: sempre importado como "pd"

# Criando um DataFrame a partir de uma lista de dicionários 
chamados = [
    {"fazenda": "Terra Norte", "valor": 1200, "tecnico": "Rafael", "status": "Concluído"},
    {"fazenda": "Boa Vista", "valor": 850, "tecnico": "João", "status": "Aberto"},
]

# Converte a lista de dicionários numa tabela do Pandas
df = pd.DataFrame(chamados)

print("\n--- 1. df.head() ---")     # util para mostrar uma previa, verificar se ta tudo ok
print(df.head(2))                   # Por padrão mostra as 5 primeiras linhas (aq limitamos a 2)

print("\n--- 2. df.info() ---")     # raio x do DataFrame, util para saber se precisa converter tipos, detectar faltantes e afins
df.info()                           # Não precisa de print(), o próprio método já imprime na tela

print("\n--- 3. df.describe() ---") # Um resumo estatístico automático apenas para colunas de números (neste caso, a coluna "valor")
print(df.describe())                

# count: quantidade de registros numéricos válidos.
# mean: média dos valores.
# std: desvio padrão (o quanto os dados variam em torno da média).
# min / max: menor e maior valor.
# 25%, 50% (mediana) e 75%: percentis da distribuição.