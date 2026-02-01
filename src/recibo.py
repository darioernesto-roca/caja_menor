import csv
from calculos import calcular_total
from num2text import num2text

def cargar_movimientos():
    movimientos = []
    with open('data/movimientos.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['cantidad'] = int(row['cantidad'])
            row['valor_unitario'] = float(row['valor_unitario'])
            row['total'] = float(row['total'])
            movimientos.append(row)
    return movimientos


def total_recibo(movimientos):
    return sum(m['total'] for m in movimientos)


def total_en_letras(movimientos):
    return num2text(total_recibo(movimientos))
