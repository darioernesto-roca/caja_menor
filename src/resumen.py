import csv
from collections import defaultdict

resumen = defaultdict(float)

with open('data/recibos.csv', newline='', encoding='utf-8') as r:
    recibos = {x['consecutivo']: x['centro_costos'] for x in csv.DictReader(r)}

with open('data/movimientos.csv', newline='', encoding='utf-8') as f:
    for m in csv.DictReader(f):
        centro = recibos[m['consecutivo']]
        resumen[centro] += float(m['total'])

for centro, total in resumen.items():
    print(f"{centro}: ${total:,.0f}")
