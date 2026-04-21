# Análisis Exploratorio de Datos (EDA)

## Dataset de ventas

- Archivo: `data/sales_data_sample.csv`
- Filas: 2,823
- Columnas: 25

## Observaciones principales

- Hay columnas que no son necesarias para el análisis de ventas: `ADDRESSLINE1`, `ADDRESSLINE2`, `PHONE`, `STATUS`, `TERRITORY`, `QTR_ID`, `MONTH_ID`, `YEAR_ID`, `MSRP`.
- Valores nulos presentes en `ADDRESSLINE2`, `STATE` y `TERRITORY`.
- La fecha de pedido viene en formato `MM/DD/YYYY HH:MM` y debe convertirse a tipo fecha.
- El dataset tiene ventas en varios países: `USA`, `Spain`, `France`, `Australia`, `UK`, `Italy`, `Finland`, `Norway`, `Singapore`, `Canada`, `Denmark`, `Germany`, `Sweden`, `Austria`, `Japan`, `Belgium`, `Switzerland`, `Philippines`, `Ireland`.

## Columnas seleccionadas para el modelo

- `ORDERNUMBER`
- `ORDERDATE`
- `PRODUCTCODE`
- `QUANTITYORDERED`
- `PRICEEACH`
- `SALES`
- `COUNTRY`
- `PRODUCTLINE`
- `DEALSIZE`

## Enseñanzas

- El dataset original es transaccional y permite construir un modelo de facturación con dimensiones de producto, cliente y región.
- La limpieza principal consiste en normalizar fechas, reducir columnas y crear identificadores numéricos para productos y clientes.
"