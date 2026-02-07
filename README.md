# Caja Menor

Sistema básico para gestionar caja menor por obra. El flujo actual permite:

- Registrar movimientos y calcular totales con base en un listado de ítems.
- Consultar el consecutivo de recibos.
- Generar un recibo en HTML y convertirlo a PDF.
- Obtener un resumen de gastos por centro de costos.

## Estructura del proyecto

- `src/`: scripts de la lógica principal.
- `data/`: archivos CSV con la información de movimientos, recibos e ítems.
- `templates/`: plantilla HTML usada para generar el recibo.
- `output/`: archivos generados (HTML/PDF).

## Requisitos

- Python 3.10+ (o equivalente).
- Dependencias adicionales:
  - `weasyprint` para generar PDF (`src/generar_pdf.py`).
  - `num2text` para convertir totales a letras (`src/recibo.py`).

Instalación de dependencias (ejemplo):

```bash
pip install weasyprint num2text
```

## Datos de entrada

Los scripts leen y escriben en los CSV de `data/`:

- `data/descriciones.cvs`: listado de ítems y valor unitario. Se usa en `src/calculos.py`.
- `data/movimientos.csv`: movimientos registrados (fecha, obra, ítem, cantidad, valor unitario, total).
- `data/recibos.csv`: consecutivo y metadatos del recibo.

Asegúrate de que los encabezados de los CSV coincidan con los que se esperan en cada script.

## Uso

### 1. Calcular totales y registrar movimientos

El módulo `src/movimientos.py` registra un movimiento en `data/movimientos.csv` y retorna el total.
Ejemplo en un script interactivo:

```python
from calculos import cargar_descripciones
from movimientos import registrar_movimiento

descripciones = cargar_descripciones('data/descriciones.cvs')

registro_total = registrar_movimiento(
    obra='OBRA 1',
    item='ALIMENTACION 12000',
    cantidad=2,
    descripciones=descripciones,
)

print(registro_total)
```

### 2. Obtener el consecutivo de recibo

```bash
python src/consecutivo.py
```

El script imprime el próximo consecutivo disponible según `data/recibos.csv`.

### 3. Generar recibo HTML

```bash
python src/generar_html.py
```

Esto crea `output/recibo.html` usando la plantilla `templates/recibo.html`.

### 4. Convertir HTML a PDF

```bash
python src/generar_pdf.py
```

Genera `output/recibo.pdf` a partir del HTML.

### 5. Resumen por centro de costos

```bash
python src/resumen.py
```

Imprime el total agrupado por centro de costos tomando los datos en `data/recibos.csv`
y `data/movimientos.csv`.

## Notas

- Los scripts actuales asumen rutas relativas (ejecuta los comandos desde la raíz del proyecto).
- Revisa los CSV de ejemplo en `data/` para entender los formatos esperados.
