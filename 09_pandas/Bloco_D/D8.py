import pandas as pd

os_jan = [
    {"id": 1000, "cliente": "Fazenda Terra Norte", "tecnico": "Rafael", "valor": 7400},
    {"id": 1001, "cliente": "Fazenda Boa Vista", "tecnico": "João", "valor": 5500}
]

os_fev = [
    {"id": 1002, "cliente": "Fazenda Sykue", "tecnico": "João", "valor": 5600},
    {"id": 1003, "cliente": "Fazenda Santo Antonio", "tecnico": "Rafael", "valor": 6500}
]

df_jan = pd.DataFrame(os_jan)
df_fev = pd.DataFrame(os_fev)

df_total = pd.concat([df_jan, df_fev], ignore_index=True)

print(df_total.shape)
print(df_total)